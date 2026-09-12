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


async def validate_file(path: pathlib.Path) -> int:
    """Validate a single file."""
    checks = 0
    errors = 0
    try:
        content = await asyncio.get_event_loop().run_in_executor(
            None, lambda p: open(p, "rb").read(), path
        )
        records = json.loads(content)
    except Exception as e:
        logging.error(f"Failed to read or parse JSON file {path.name}: {e}")
        raise ValueError(1)

    for record in records:
        if rec_licenses := record.get("license"):
            try:
                attr = rec_licenses["attribution"]
            except KeyError:
                recid = record.get("recid", "UNSET")
                message = (
                    f"License field set but without attribution in file {path.name} "
                    f"with recid {recid}!"
                )

                logging.error(message)
                errors += 1
                continue

            if attr not in VALID_LICENSE_IDENTIFIERS:
                recid = record.get("recid", "UNSET")
                message = (
                    f"Invalid license identifier `{attr}` in file {path.name} "
                    f"for recid {recid}!"
                )

                logging.error(message)
                errors += 1
            else:
                checks += 1

    if errors:
        raise ValueError(errors)

    logging.info(f"Successfully validated file {path.name}")
    return checks


async def check_all_paths(verbose: bool = False):
    """Execute checks on all found files."""
    start_time = time.perf_counter()

    loop = asyncio.get_event_loop()

    root_path = pathlib.Path(os.getcwd()) / "data" / "records"
    all_paths = list(root_path.glob("*.json"))

    tasks = [loop.create_task(validate_file(file_path)) for file_path in all_paths]
    results = await asyncio.gather(*tasks, return_exceptions=True)

    finish_time = time.perf_counter() - start_time
    if verbose:
        logging.info(
            f"Processed {len(all_paths)} files within {finish_time:.2f} seconds."
        )

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
            f"\tPlease ensure the licenses are one of the following: "
            f"{VALID_LICENSE_IDENTIFIERS}.\n"
            f"\tIf you are using a valid SPDX license string that is not in the "
            f"above list, please contact `opendata-team@cern.ch`."
        )
        exit(1)

    else:
        if verbose:
            logging.info(
                f"Successfully validated {sum(results)} records. No errors found."
            )


def main():
    """Test to validate all license fields."""
    parser = argparse.ArgumentParser(
        description="Check if license fields are valid in all records."
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Increase output verbosity to show informational messages.",
    )
    args = parser.parse_args()

    log_level = logging.INFO if args.verbose else logging.WARNING
    logging.basicConfig(level=log_level, format="[%(levelname)s] %(message)s")

    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(check_all_paths(verbose=args.verbose))
    finally:
        loop.close()


if __name__ == "__main__":
    main()
