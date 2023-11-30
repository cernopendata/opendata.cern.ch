#!/usr/bin/env python3

"""Clean JSON file.

Cleans JSON file so as to fix indentation, order fields, and remove trailing
whitespace.
"""

import json

import click


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def clean_json_file(filename):
    """Clean JSON file.

    Cleans JSON file so as to fix indentation, order fields, and remove
    trailing whitespace.
    """
    with open(filename, "r") as fdesc:
        records = json.loads(fdesc.read())

    new_content = json.dumps(
        records, indent=2, sort_keys=True, ensure_ascii=False, separators=(",", ": ")
    )

    with open(filename, "w") as fdesc:
        fdesc.write(new_content + "\n")


if __name__ == "__main__":
    clean_json_file()
