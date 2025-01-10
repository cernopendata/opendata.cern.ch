#!/usr/bin/env python3

"""Clean JSON file.

Cleans JSON file so as to fix indentation, order fields, and remove trailing
whitespace.
"""

import json
import sys

import click


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option(
    "--check",
    is_flag=True,
    default=False,
    help="Don't write the file back, only check whether the file is well formatted.",
)
def clean_json_file(filename, check):  # noqa: D301
    """Clean JSON file.

    Clean JSON file so as to fix indentation, order fields, and remove trailing
    whitespace.

    \b
    :param filename: The file name to be reformatted.
    :param check: Do not modify file, only check whether it is well formatted.
    :type filename: str
    :type check: bool
    """
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
            print(f"[ERROR] File {filename} is badly formatted.")
            sys.exit(1)
        else:
            with open(filename, "w") as fdesc:
                fdesc.write(new_content)


if __name__ == "__main__":
    clean_json_file()
