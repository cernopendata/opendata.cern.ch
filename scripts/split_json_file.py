#!/usr/bin/env python3

"""Split big JSON file into smaller files.

Splits big JSON file into smaller files by a group of say 100 records at most.
Useful for uploading big CMS files to OpenShift pods.
"""

import json
import math

import click


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option("-s", "--split", help="Split by how many records?", default=100)
def split_json_file(filename, split):
    """Split JSON file into a group of SPLIT records."""

    with open(filename, "r") as fdesc:
        records = json.loads(fdesc.read())

    if len(records) > split:
        num_output_files = math.ceil(len(records) / split)

        for i in range(0, math.ceil(len(records) / split)):
            filenamepart = filename.replace(
                ".json", f"-part_{i+1:0{len(str(num_output_files))}}.json"
            )
            print("[INFO] Creating file %s..." % filenamepart)
            split_content = json.dumps(
                records[split * i : split * (i + 1)],
                indent=2,
                sort_keys=True,
                ensure_ascii=False,
                separators=(",", ": "),
            )
            with open(filenamepart, "w") as fdesc:
                fdesc.write(split_content + "\n")
    else:
        print("[INFO] Nothing to do, the file is small already.")


if __name__ == "__main__":
    split_json_file()
