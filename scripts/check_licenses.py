#!/usr/bin/env python

"""Check if license fields are valid in all records."""

import argparse
import asyncio
import json
import logging
import os
import pathlib
import time

VALID_LICENSE_IDENTIFIERS = [
    "CC0-1.0",
    "GPL-3.0-only",
    "MIT",
    "Apache-2.0",
    "BSD-3-Clause",
]

logging.basicConfig(level=logging.WARNING, format="[%(levelname)s] %(message)s")


async def validate_file(path: pathlib.Path) -> int:
    """Validate a single file."""
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
        if rec_licenses := record.get("license"):
            try:
                attr = rec_licenses["attribution"]
            except KeyError:
                recid = record.get("recid", "UNSET")
                message = f"License field set but without attribution in file {path.name} with recid {recid}!"

                logging.error(message)
                errors += 1
                continue

            if attr not in VALID_LICENSE_IDENTIFIERS:
                recid = record.get("recid", "UNSET")
                message = f"Invalid license identifier `{attr}` in file {path.name} for recid {recid}! "

                logging.error(message)
                errors += 1
            else:
                checks += 1

    if errors:
        raise ValueError(errors)

    logging.debug(f"Successfully validated file {path.name}")
    return checks


async def check_paths(file_paths):
    """Execute checks on specified files."""
    start_time = time.perf_counter()
    loop = asyncio.get_event_loop()

    tasks = [loop.create_task(validate_file(file_path)) for file_path in file_paths]
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
        logging.error(
            f"Validation completed with {errors} errors!\n"
            f"\tPlease ensure the licenses are one of the following: {VALID_LICENSE_IDENTIFIERS}.\n"
            f"\tIf you are using a valid SPDX license string that is not in the above list, "
            f"please contact `opendata-team@cern.ch`."
        )
        exit(1)
    else:
        logging.info(f"Successfully validated {sum(results)} records. No errors found.")


def main():
    """Test to validate license fields."""
    parser = argparse.ArgumentParser(
        description="Check if license fields are valid in records."
    )
    parser.add_argument(
        "files",
        metavar="[FILE]",
        nargs="*",
        type=pathlib.Path,
        help="Optional specific JSON files to check. If omitted, checks all files in data/records.",
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
        loop.run_until_complete(check_paths(all_paths))
    finally:
        loop.close()


if __name__ == "__main__":
    main()
