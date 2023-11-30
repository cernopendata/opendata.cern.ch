#!/usr/bin/python3

"""Helper script to check record fixtures."""

import json
import os
import sys

GENERAL_MANDATORY_FIELDS = [
    "date_created",
    "date_published",
    "experiment",
    "publisher",
    "recid",
    "title",
    "type",
]


def print_warning(filename, recid="", field="", message="missing-field"):
    """Print warning for given record."""
    print("File {0} record {1} {2} {3}.".format(filename, recid, message, field))


def main():
    """Check record fixtures for basic fields."""
    problems_found = False
    fixtures_directory = "cernopendata/modules/fixtures/data/records"
    for filename in os.listdir(fixtures_directory):
        records = json.loads(open(fixtures_directory + os.sep + filename, "r").read())
        for record in records:
            recid = record.get("recid", None)
            # (1) check general mandatory fields
            for field in GENERAL_MANDATORY_FIELDS:
                if not record.get(field, None):
                    problems_found = True
                    print_warning(filename, recid, field)
            # (2) check presence of authors or collaboration
            authors = record.get("authors", None)
            collaboration = record.get("collaboration", None)
            if not authors and not collaboration:
                problems_found = True
                print_warning(filename, recid, "authors-or-collaboration")
            # (3) check type primary and secondary:
            type_primary = record.get("type", {}).get("primary", None)
            type_secondary = record.get("type", {}).get("secondary", None)
            if not (type_primary and type_secondary):
                problems_found = True
                print_warning(filename, recid, "type-primary-secondary")
    # we are done
    if problems_found:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
