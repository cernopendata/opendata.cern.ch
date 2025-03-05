#!/usr/bin/env python3

"""
Clean JSON files.

Clean one or more JSON files so as to fix indentation, order fields, and remove
trailing whitespace.
"""

import json
import sys

import click


@click.command()
@click.argument(
    "filenames", metavar="[FILENAME] ...", type=click.Path(exists=True), nargs=-1
)
@click.option(
    "--check",
    is_flag=True,
    default=False,
    help="Don't write the file back, only check whether the file is well formatted.",
)
def clean_json_file(filenames, check):  # noqa: D301
    """
    Clean JSON files.

    Clean one or more JSON files so as to fix indentation, order fields, and
    remove trailing whitespace.
    """
    problematic_files = []
    for filename in list(set(filenames)):
        with open(filename, "r") as fdesc:
            old_content = fdesc.read()
            records = json.loads(old_content)
            new_content = (
                json.dumps(
                    records,
                    indent=2,
                    sort_keys=True,
                    ensure_ascii=False,
                    separators=(",", ": "),
                )
                + "\n"
            )

        if old_content != new_content:
            if check:
                problematic_files.append(filename)
            else:
                with open(filename, "w") as fdesc:
                    fdesc.write(new_content)

    if check and problematic_files:
        for filename in problematic_files:
            print(f"[ERROR] File {filename} is badly formatted.")
        sys.exit(1)


if __name__ == "__main__":
    clean_json_file()
