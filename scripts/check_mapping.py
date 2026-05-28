#!/usr/bin/env python

"""Check if license fields are valid in all records."""

import asyncio
import dataclasses
import itertools
import json
import logging
import os
import time
import typing
from glob import glob
from pathlib import Path

import click
import yaml

LOOP = asyncio.get_event_loop()
MAPPING = Path(os.getcwd()) / "scripts" / "record_mapping.yaml"
FILES = Path(os.getcwd()) / "data" / "records" / "*"


@dataclasses.dataclass
class InvalidRecord:
    """Dataclass to hold information about a validated file."""

    recid: typing.Optional[str]
    path: Path
    msg: str


@click.command()
@click.option(
    "-m",
    "--mapping",
    default=MAPPING,
    type=click.Path(readable=True, path_type=Path, dir_okay=False),
    help="Path to check records against.",
)
@click.option(
    "-v", "--verbose", default=False, is_flag=True, help="Print verbose output."
)
@click.argument("files", type=click.Path(readable=True, path_type=Path), nargs=-1)
def command(**kwargs):
    """Validate a files of supplied paths. Arguments support unix-like patterns."""
    try:
        LOOP.run_until_complete(main(**kwargs))
    finally:
        LOOP.close()


async def main(mapping, verbose, files) -> None:
    """Validate record fields against a defined mapping."""
    start_time = time.perf_counter()
    files = files or (FILES,)

    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=log_level, format="[%(levelname)s] %(message)s")

    logging.info("Loading mapping file...")
    mapping: dict = await LOOP.run_in_executor(
        None, lambda: yaml.safe_load(open(mapping, "r"))
    )

    globs = [glob(str(f)) for f in files]
    paths = [Path(g) for g in itertools.chain(*globs)]
    logging.info("Found %d files. Validating...", len(paths))

    tasks = [LOOP.create_task(validate_single(path, mapping)) for path in paths]
    results = await asyncio.gather(*tasks)

    finish = f"within {time.perf_counter() - start_time:.2f} seconds"
    logging.info(
        "Validated %d files (%d records) %s.",
        len(paths),
        sum(r[0] for r in results),
        finish,
    )

    errors = {p: e for _, e, p in results if len(e)}
    if not errors:
        logging.info("All files validated successfully. No errors found.")
        exit(0)

    logging.error(
        "Found %d errors in %d files.",
        sum(len(e) for e in errors.values()),
        len(errors),
    )

    for p, err in errors.items():
        logging.error("File %s has %d errors:", p.name, len(err))

        for e in err:
            logging.error(" - %s: %s", e.recid or "UNSET", e.msg)

    exit(1)


async def validate_single(
    path: Path, mapping: dict
) -> tuple[int, list[InvalidRecord], Path]:
    """Validate a single file against the mapping schema."""
    errors = []
    try:
        records = await asyncio.get_event_loop().run_in_executor(
            None, lambda p: json.loads(open(p, "rb").read()), path
        )

    except Exception as e:
        logging.error("Failed to load json file %s: %s", path.name, e)
        records = []

    def rcheck(doc, validation, stack=None) -> typing.Generator[str, None, None]:
        """Recursively checks a record against the validation schema."""
        stack = stack or []

        if isinstance(validation, dict):
            for v_key, v_value in validation.items():
                is_optional = v_key.startswith("?")
                v_key = v_key.removeprefix("?")

                if v_key not in doc:
                    if not is_optional:
                        yield f"Missing required key [{']['.join(stack)}]->{v_key}"
                    continue

                sub_docs = v if isinstance((v := doc[v_key]), list) else [v]
                for sub_doc in sub_docs:
                    yield from rcheck(sub_doc, v_value, stack + [v_key])

        else:
            if validation is None:
                return

            allowed = validation if isinstance(validation, list) else [validation]

            if not any(doc == pattern for pattern in allowed):
                yield f"Value of [{']['.join(stack)}]: `{doc}` does not match any valid patterns: {allowed}"

    for record in records:
        if error_list := list(rcheck(record, mapping)):
            for e in error_list:
                rec = InvalidRecord(recid=record.get("recid"), path=path, msg=e)
                errors.append(rec)

    logging.debug("Validated file %s with %d records.", path.name, len(records))
    return len(records), errors, path


if __name__ == "__main__":
    command()
