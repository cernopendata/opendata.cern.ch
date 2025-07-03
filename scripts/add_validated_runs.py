import json
import os
import re

def add_validated_runs_field(directory):
    """
    Adds a 'validated_runs' field to records based on links in the abstract,
    without modifying the original abstract content. The script processes
    records where the abstract description explicitly mentions 'validated runs'
    or 'validated lumi sections'.
    """
    validated_regex = re.compile(r'validated (runs|lumi sections)', re.IGNORECASE)

    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r+', encoding='utf-8') as f:
                    data = json.load(f)
                    modified = False
                    for record in data:
                        if 'validated_runs' in record:
                            continue

                        if ('abstract' in record and
                                'description' in record['abstract'] and
                                'links' in record['abstract'] and
                                validated_regex.search(record['abstract']['description'])):

                            links = record['abstract']['links']
                            if links:
                                record['validated_runs'] = []
                                for link in links:
                                    validation_type = "full"
                                    if 'description' in link and "muons only" in link['description'].lower():
                                        validation_type = "muonsonly"
                                    record['validated_runs'].append({
                                        "recid": link['recid'],
                                        "validation": validation_type
                                    })
                                modified = True

                    if modified:
                        f.seek(0)
                        json.dump(data, f, indent=2)
                        f.truncate()
                        print(f"Updated {filename}")

            except json.JSONDecodeError:
                print(f"Could not decode JSON from {filename}")
            except Exception as e:
                print(f"An error occurred with {filename}: {e}")

if __name__ == "__main__":
    add_validated_runs_field("data/records")