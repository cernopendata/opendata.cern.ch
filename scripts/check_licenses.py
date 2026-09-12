#!/usr/bin/env python

"""Check if metadata fields adhere to controlled vocabularies in all records."""

import argparse
import asyncio
import json
import logging
import os
import pathlib
import time

try:
    import yaml
except ImportError:
    yaml = None

DEFAULT_CONTROLLED_VOCABULARIES = {
    "license.attribution": [
        "CC0-1.0",
        "GPL-3.0-only",
        "MIT",
        "Apache-2.0",
        "BSD-3-Clause",
    ],
    "collision_information.type": [
        "e+e-",
        "pp",
        "pPb",
        "Pb-Pb",
        "PbPb",
        "Interfill",
    ],
    "experiment": [
        "ALICE",
        "ATLAS",
        "CMS",
        "DELPHI",
        "JADE",
        "LHCb",
        "OPERA",
        "PHENIX",
        "TOTEM",
    ],
}

logging.basicConfig(level=logging.WARNING, format="[%(levelname)s] %(message)s")


def load_vocabularies(config_path: pathlib.Path = None) -> dict:
    """Load controlled vocabularies from a YAML/JSON configuration file or use defaults."""
    vocabularies = {k: list(v) for k, v in DEFAULT_CONTROLLED_VOCABULARIES.items()}
    if not config_path:
        for fname in ["controlled_vocabularies.yml", "controlled_vocabularies.json"]:
            cand = pathlib.Path(__file__).parent / fname
            if cand.is_file():
                config_path = cand
                break

    if config_path and config_path.is_file():
        try:
            content = config_path.read_text(encoding="utf-8")
            if yaml:
                data = yaml.safe_load(content)
            else:
                data = json.loads(content)
            if isinstance(data, dict):

                def _flatten_vocab(prefix, obj):
                    flat = {}
                    if isinstance(obj, list):
                        flat[prefix] = obj
                    elif isinstance(obj, dict):
                        for k, v in obj.items():
                            sub_prefix = f"{prefix}.{k}" if prefix else k
                            flat.update(_flatten_vocab(sub_prefix, v))
                    return flat

                parsed = _flatten_vocab("", data)
                for field, allowed in parsed.items():
                    if isinstance(allowed, list):
                        vocabularies[field] = allowed
        except Exception as exc:
            logging.warning(
                f"Could not load vocabulary configuration from {config_path}: {exc}"
            )

    return vocabularies


def _get_nested_field_values(data, field_parts):
    """Retrieve values at a nested dot-separated path in data (handling lists)."""
    current_values = [data]
    for part in field_parts:
        next_values = []
        for val in current_values:
            if isinstance(val, dict) and part in val:
                next_val = val[part]
                if isinstance(next_val, list):
                    next_values.extend(next_val)
                else:
                    next_values.append(next_val)
        current_values = next_values
        if not current_values:
            break
    return current_values


async def validate_file(path: pathlib.Path, vocabularies: dict) -> int:
    """Validate a single file against the controlled vocabularies."""
    checks = 0
    errors = 0
    try:
        records = await asyncio.get_event_loop().run_in_executor(
            None, lambda p: json.loads(open(p, "rb").read()), path
        )
    except Exception as exc:
        logging.error(f"Failed to load or parse JSON in file {path.name}: {exc}")
        raise ValueError(1)

    for record in records:
        recid = record.get("recid", "UNSET")

        # Specific license attribution missing check
        if rec_licenses := record.get("license"):
            if "attribution" not in rec_licenses:
                message = f"License field set but without attribution in file {path.name} with recid {recid}!"
                logging.error(message)
                errors += 1

        # Check all controlled vocabularies
        for field_path, allowed_values in vocabularies.items():
            parts = field_path.split(".")
            values = _get_nested_field_values(record, parts)
            for val in values:
                if val is None:
                    continue
                if val not in allowed_values:
                    message = f"Invalid value `{val}` for field `{field_path}` in file {path.name} for recid {recid}! "
                    logging.error(message)
                    errors += 1
                else:
                    checks += 1

    if errors:
        raise ValueError(errors)

    logging.debug(f"Successfully validated file {path.name}")
    return checks


async def check_paths(file_paths, vocabularies: dict):
    """Execute checks on specified files."""
    start_time = time.perf_counter()
    loop = asyncio.get_event_loop()

    tasks = [
        loop.create_task(validate_file(file_path, vocabularies))
        for file_path in file_paths
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    finish_time = time.perf_counter() - start_time
    logging.info(f"Processed {len(file_paths)} files within {finish_time:.2f} seconds.")

    if any(isinstance(result, Exception) for result in results):
        errors = sum(
            [
                int(str(result)) if str(result).isdigit() else 1
                for result in results
                if isinstance(result, Exception)
            ]
        )
        allowed_summary = "\n".join(
            f"\t{field}: {allowed}" for field, allowed in vocabularies.items()
        )
        logging.error(
            f"Validation completed with {errors} errors!\n"
            f"Please ensure values are from the controlled vocabularies:\n{allowed_summary}\n"
            f"\tIf you are using a valid value that is not in the above list, "
            f"please contact `opendata-team@cern.ch`."
        )
        exit(1)
    else:
        logging.info(f"Successfully validated {sum(results)} fields. No errors found.")


def main():
    """Test to validate metadata fields against controlled vocabularies."""
    parser = argparse.ArgumentParser(
        description="Check if metadata fields are valid against controlled vocabularies in records."
    )
    parser.add_argument(
        "files",
        metavar="[FILE]",
        nargs="*",
        type=pathlib.Path,
        help="Optional specific JSON files to check. If omitted, checks all files in data/records.",
    )
    parser.add_argument(
        "-c",
        "--config",
        type=pathlib.Path,
        default=None,
        help="Path to YAML/JSON configuration file for controlled vocabularies.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase output verbosity to include info and statistics.",
    )
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.INFO)

    vocabularies = load_vocabularies(args.config)

    if args.files:
        all_paths = [p for p in args.files if p.is_file() and p.name.endswith(".json")]
        if not all_paths:
            logging.info("No JSON files matched the provided arguments.")
            return
    else:
        root_path = pathlib.Path(os.getcwd()) / "data" / "records"
        all_paths = list(root_path.glob("*.json"))

    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(check_paths(all_paths, vocabularies))
    finally:
        loop.close()


if __name__ == "__main__":
    main()
