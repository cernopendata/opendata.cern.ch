#!/usr/bin/env python
"""Ensure that the records satisfy the json schema."""
import glob
import json

from jsonschema import Draft202012Validator

with open("/code/cernopendata/jsonschemas/records/record-v1.0.0.json") as f:
    schema = json.load(f)

validator = Draft202012Validator(schema)

CHECKS = [
    {"schema": "record-v1.0.0.json", "glob": "/content/data/records/*.json"},
    {"schema": "docs-v1.0.0.json", "glob": "/content/data/docs/*/*.json"},
    {
        "schema": "docs-v1.0.0.json",
        "glob": "/code/cernopendata/modules/fixtures/data/docs/*/*.json",
    },
    {
        "schema": "glossary-term-v1.0.0.json",
        "glob": "/code/cernopendata/modules/fixtures/data/terms/terms.json",
    },
]

COLORS = {
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "YELLOW": "\033[93m",
    "RESET": "\033[0m",
}


def fix_note_error(record, error):
    """Fix the error of a methodology.step.note being a string instead of an object."""
    path = list(error.path)

    if (
        len(path) > 2
        and path[-1] == "note"
        and path[:2] == ["methodology", "steps"]
        and error.validator == "type"
        and error.validator_value == "object"
    ):
        obj = record

        # Walk to the parent object of "note"
        for key in path[:-1]:
            obj = obj[key]

        if isinstance(obj["note"], str):
            obj["note"] = {"description": obj["note"]}
            return True

    return False


def validate_file(filename, validator):
    """Check if a file validates a particular schema."""
    with open(filename) as f:
        data = json.load(f)

    # The JSON file contains a list of objects
    if not isinstance(data, list):
        print(f"{filename}: expected a list")
        return False

    valid = True
    modified = False

    for i, record in enumerate(data):
        try:
            errors = list(validator.iter_errors(record))
        except Exception as e:
            print(
                f"{filename}: validator error on record #{i}: "
                f"{type(e).__name__}: {e}"
            )
            return False, False, []

        for error in errors:
            valid = False
            if fix_note_error(record, error):
                modified = True
                print(
                    f"{COLORS['YELLOW']}{filename}: fixed record #{i}{COLORS['RESET']}"
                )
            else:
                path = ".".join(map(str, error.path))
                print(
                    f"{COLORS['RED']}{filename} record #{i}: {path}: {error.message}{COLORS['RESET']}"
                )

    return valid, modified, data


for check in CHECKS:
    print(f"\n=== Checking {check['glob']} ===")
    with open(f"/code/cernopendata/jsonschemas/records/{check['schema']}") as f:
        schema = json.load(f)

    validator = Draft202012Validator(schema)

    for filename in glob.glob(check["glob"]):
        ok, modified, records = validate_file(filename, validator)
        if ok:
            print(f"{COLORS['GREEN']}{filename}: OK{COLORS['RESET']}")
        if modified:
            with open(filename, "w") as f:
                json.dump(records, f, indent=2)
