"""A script to populate the 'validated_runs' field in data records."""
import json
import os
import re


def build_validation_lookup(directory):
    """Scan all 'validated-runs' files to build a lookup table.

    This function maps a record's recid to its validation type ('full' or 'muonsonly').
    """
    validation_lookup = {}
    validated_files_regex = re.compile(r".*validated-runs.*\.json", re.IGNORECASE)
    muons_only_regex = re.compile(r"only valid muons", re.IGNORECASE)

    for filename in os.listdir(directory):
        if validated_files_regex.match(filename):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)

                records_to_process = []
                if isinstance(data, dict):
                    records_to_process.append(data)
                elif isinstance(data, list):
                    records_to_process.extend(data)

                for record in records_to_process:
                    if not isinstance(record, dict):
                        continue

                    recid = record.get("recid")
                    title = record.get("title", "")
                    title_additional = record.get("title_additional", "")

                    if recid and (title or title_additional):
                        validation_type = "full"
                        if muons_only_regex.search(title) or muons_only_regex.search(
                            title_additional
                        ):
                            validation_type = "muonsonly"
                        validation_lookup[str(recid)] = validation_type

            except json.JSONDecodeError as e:
                print(f"An error occurred decoding JSON from {filename}: {e}")
            except Exception as e:
                print(f"An unexpected error occurred with {filename}: {e}")

    return validation_lookup, validated_files_regex


def fix_and_add_validated_runs(directory, validation_lookup, validated_files_regex):
    """Add a 'validated_runs' field to records based on a lookup table.

    This function uses a pre-built validation lookup table and skips all
    validated-run files themselves.
    """
    validated_description_regex = re.compile(
        r"validated (runs|lumi sections)", re.IGNORECASE
    )

    for filename in os.listdir(directory):
        if not validated_files_regex.match(filename):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    data = json.load(f)

                records_to_process = []
                if isinstance(data, dict):
                    records_to_process.append(data)
                elif isinstance(data, list):
                    records_to_process.extend(data)

                modified = False
                for record in records_to_process:
                    if not isinstance(record, dict) or "validated_runs" in record:
                        continue

                    if (
                        "abstract" in record
                        and isinstance(record.get("abstract"), dict)
                        and validated_description_regex.search(
                            record["abstract"].get("description", "")
                        )
                    ):

                        links = record["abstract"].get("links", [])
                        if links:
                            record["validated_runs"] = []
                            for link in links:
                                link_recid = link.get("recid")
                                if link_recid:
                                    validation_type = validation_lookup.get(
                                        str(link_recid), "full"
                                    )
                                    record["validated_runs"].append(
                                        {
                                            "recid": link_recid,
                                            "validation": validation_type,
                                        }
                                    )
                                    modified = True
                if modified:
                    final_data = (
                        records_to_process
                        if isinstance(data, list)
                        else records_to_process[0]
                    )
                    with open(filepath, "w", encoding="utf-8") as f:
                        json.dump(final_data, f, indent=2, ensure_ascii=False)
                        f.write("\n")
                    print(f"Updated validated runs in {filename}")

            except (json.JSONDecodeError, IOError) as e:
                print(f"An error occurred with {filename}: {e}")


if __name__ == "__main__":
    data_directory = "data/records"
    print("Building validation lookup table...")
    validation_map, validated_files_pattern = build_validation_lookup(data_directory)
    print(f"Found {len(validation_map)} validated run records.")

    print("\nProcessing dataset records...")
    fix_and_add_validated_runs(data_directory, validation_map, validated_files_pattern)
    print("\nScript finished.")
