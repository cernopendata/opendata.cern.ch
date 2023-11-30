# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017, 2018, 2020,2022 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Command line interface for CERN Open Data Portal."""

import glob
import json
import os
import uuid

import click
import pkg_resources
from flask import current_app
from flask.cli import with_appcontext
from invenio_db import db
from invenio_files_rest.models import Bucket, FileInstance, ObjectVersion
from invenio_indexer.api import RecordIndexer
from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_pidstore.models import PersistentIdentifier
from invenio_records_files.api import Record
from invenio_records_files.models import RecordsBuckets
from sqlalchemy.orm.attributes import flag_modified

from cernopendata.modules.records.minters.docid import cernopendata_docid_minter
from cernopendata.modules.records.minters.recid import cernopendata_recid_minter
from cernopendata.modules.records.minters.termid import cernopendata_termid_minter


def get_jsons_from_dir(dir):
    """Get JSON files inside a dir."""
    res = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".json"):
                res.append(os.path.join(root, file))
    return res


def handle_record_files(data, bucket, files, skip_files):
    """Handles record files."""
    for file in files:
        if skip_files:
            break
        assert "uri" in file
        assert "size" in file
        assert "checksum" in file

        try:
            f = FileInstance.create()
            filename = file.get("uri").split("/")[-1:][0]
            f.set_uri(file.get("uri"), file.get("size"), file.get("checksum"))
            obj = ObjectVersion.create(bucket, filename, _file_id=f.id)

            file.update(
                {
                    "bucket": str(obj.bucket_id),
                    "checksum": obj.file.checksum,
                    "key": obj.key,
                    "version_id": str(obj.version_id),
                }
            )

        except Exception as e:
            click.echo(
                "Recid {0} file {1} could not be loaded due "
                "to {2}.".format(data.get("recid"), filename, str(e))
            )
            continue


def create_record(schema, data, files, skip_files):
    """Creates a new record."""
    id = uuid.uuid4()
    cernopendata_recid_minter(id, data)
    data["$schema"] = schema
    record = Record.create(data, id_=id, with_bucket=not skip_files)
    if not skip_files:
        handle_record_files(data, record.bucket, files, skip_files)

    return record


def update_record(pid, schema, data, files, skip_files):
    """Updates the given record."""
    record = Record.get_record(pid.object_uuid)
    with db.session.begin_nested():
        if record.files and not skip_files:
            bucket_id = record.files.bucket
            bucket = Bucket.get(bucket_id.id)
            for o in ObjectVersion.get_by_bucket(bucket).all():
                o.remove()
                o.file.delete()
            RecordsBuckets.query.filter_by(record=record.model, bucket=bucket).delete()
            bucket_id.remove()
    db.session.commit()
    record.update(data)
    if not skip_files:
        bucket = Bucket.create()
        handle_record_files(data, bucket, files, skip_files)
        RecordsBuckets.create(record=record.model, bucket=bucket)
    return record


def create_doc(data, schema):
    """Creates a new doc record."""
    from invenio_records import Record

    id = uuid.uuid4()
    cernopendata_docid_minter(id, data)
    data["$schema"] = schema
    record = Record.create(data, id_=id)
    return record


def update_doc(pid, data):
    """Updates the given doc record."""
    from invenio_records import Record

    record = Record.get_record(pid.object_uuid)
    record.update(data)
    return record


def create_glossary_term(data, schema):
    """Creates a new glossary term record."""
    from invenio_records import Record

    id = uuid.uuid4()
    cernopendata_termid_minter(id, data)
    data["$schema"] = schema
    record = Record.create(data, id_=id)
    return record


def update_glossary_term(pid, data):
    """Updates the given glossary term record."""
    from invenio_records import Record

    record = Record.get_record(pid.object_uuid)
    record.update(data)
    return record


@click.group(chain=True)
def fixtures():
    """Automate site bootstrap process and testing."""


@fixtures.command()
@click.option("--skip-files", is_flag=True, default=False, help="Skip loading of files")
@click.option(
    "files",
    "--file",
    "-f",
    multiple=True,
    type=click.Path(exists=True),
    help="Path to the file(s) to be loaded. If not provided, all"
    "files will be loaded",
)
@click.option("--profile", is_flag=True, help="Output profiling information.")
@click.option(
    "--mode",
    required=True,
    type=click.Choice(["insert", "replace", "insert-or-replace"]),
)
@with_appcontext
def records(skip_files, files, profile, mode):
    """Load all records."""
    if profile:
        import cProfile
        import pstats
        from io import StringIO

        pr = cProfile.Profile()
        pr.enable()

    indexer = RecordIndexer()
    schema = current_app.extensions["invenio-jsonschemas"].path_to_url(
        "records/record-v1.0.0.json"
    )
    data = pkg_resources.resource_filename(
        "cernopendata", "modules/fixtures/data/records"
    )
    action = None

    if files:
        record_json = files
    else:
        record_json = glob.glob(os.path.join(data, "*.json"))

    for filename in record_json:
        # name = filename.split('/')[-1]
        # if name.startswith('opera'):
        #     click.echo('Skipping opera records ...')
        #     continue
        click.echo("Loading records from {0} ...".format(filename))
        with open(filename, "rb") as source:
            for data in json.load(source):
                if not data:
                    click.echo(
                        "IGNORING a possibly broken or corrupted "
                        "record entry in file {0} ...".format(filename)
                    )
                    continue

                files = data.get("files", [])

                try:
                    pid = PersistentIdentifier.get("recid", data["recid"])
                    if mode == "insert":
                        click.secho(
                            "Record recid {} exists already;"
                            " cannot insert it.  ".format(data.get("recid")),
                            fg="red",
                            err=True,
                        )
                        return
                    record = update_record(pid, schema, data, files, skip_files)
                    action = "updated"
                except PIDDoesNotExistError:
                    if mode == "replace":
                        click.secho(
                            "Record recid {} does not exist; "
                            "cannot replace it.".format(data.get("recid")),
                            fg="red",
                            err=True,
                        )
                        return
                    record = create_record(schema, data, files, skip_files)
                    action = "inserted"

                if not skip_files:
                    record.files.flush()
                record.commit()
                db.session.commit()
                click.echo("Record recid {0} {1}.".format(data.get("recid"), action))
                indexer.index(record)
                db.session.expunge_all()

    if profile:
        pr.disable()
        s = StringIO()
        sortby = "cumulative"
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())


@fixtures.command()
@with_appcontext
@click.option(
    "files",
    "--file",
    "-f",
    multiple=True,
    type=click.Path(exists=True),
    help="Path to the file(s) to be loaded. If not provided, all"
    "files will be loaded",
)
@click.option(
    "--mode",
    required=True,
    type=click.Choice(["insert", "replace", "insert-or-replace"]),
)
def glossary(files, mode):
    """Load glossary term records."""
    indexer = RecordIndexer()
    schema = current_app.extensions["invenio-jsonschemas"].path_to_url(
        "records/glossary-term-v1.0.0.json"
    )
    data = pkg_resources.resource_filename("cernopendata", "modules/fixtures/data")

    if files:
        glossary_terms_json = files
    else:
        glossary_terms_json = glob.glob(os.path.join(data, "terms", "*.json"))

    for filename in glossary_terms_json:
        click.echo("Loading glossary terms from {0} ...".format(filename))

        with open(filename, "rb") as source:
            for data in json.load(source):
                if "collections" not in data and not isinstance(
                    data.get("collections", None), str
                ):
                    data["collections"] = []
                data["collections"].append({"primary": "Terms"})

                record = None
                action = None
                if mode == "insert-or-replace":
                    try:
                        pid = PersistentIdentifier.get("termid", data["anchor"])
                        if pid:
                            record = update_glossary_term(pid, data)
                            action = "updated"
                    except PIDDoesNotExistError:
                        record = create_glossary_term(data, schema)
                        action = "inserted"
                elif mode == "insert":
                    try:
                        pid = PersistentIdentifier.get("termid", data["anchor"])
                        if pid:
                            click.echo(
                                "Glossary term termid {} exists already;"
                                " cannot insert it.  ".format(data.get("anchor")),
                                err=True,
                            )
                            return
                    except PIDDoesNotExistError:
                        record = create_glossary_term(data, schema)
                        action = "inserted"
                else:
                    try:
                        pid = PersistentIdentifier.get("termid", data["anchor"])
                    except PIDDoesNotExistError:
                        click.echo(
                            "Glossary term {} does not exist; "
                            "cannot replace it.".format(data.get("anchor")),
                            err=True,
                        )
                        return
                    record = update_glossary_term(pid, data)
                    action = "updated"

                if record:
                    record.commit()

                db.session.commit()
                click.echo("Glossary term {0} {1}.".format(data.get("anchor"), action))
                indexer.index(record)
                db.session.expunge_all()


@fixtures.command()
@click.option(
    "files",
    "--file",
    "-f",
    multiple=True,
    type=click.Path(exists=True),
    help="Path to the file(s) to be loaded. If not provided, all"
    "files will be loaded",
)
@click.option(
    "--mode",
    required=True,
    type=click.Choice(["insert", "replace", "insert-or-replace"]),
)
@with_appcontext
def docs(files, mode):
    """Load demo article records."""
    from slugify import slugify

    indexer = RecordIndexer()
    schema = current_app.extensions["invenio-jsonschemas"].path_to_url(
        "records/docs-v1.0.0.json"
    )
    data = pkg_resources.resource_filename("cernopendata", "modules/fixtures/data/docs")

    if files:
        articles_json = files
    else:
        articles_json = get_jsons_from_dir(data)

    for filename in articles_json:
        # name = filename.split('/')[-1]
        # if name.startswith('opera'):
        #     click.echo('Skipping opera records ...')
        #     continue

        click.echo("Loading docs from {0} ...".format(filename))
        with open(filename, "rb") as source:
            for data in json.load(source):
                # Replace body with responding content
                assert data["body"]["content"]
                content_filename = os.path.join(
                    *(
                        [
                            "/",
                        ]
                        + filename.split("/")[:-1]
                        + [
                            data["body"]["content"],
                        ]
                    )
                )

                with open(content_filename) as body_field:
                    data["body"]["content"] = body_field.read()
                if "collections" not in data and not isinstance(
                    data.get("collections", None), str
                ):
                    data["collections"] = []
                if mode == "insert-or-replace":
                    try:
                        pid = PersistentIdentifier.get(
                            "docid", str(slugify(data.get("slug", data["title"])))
                        )
                        if pid:
                            record = update_doc(pid, data)
                            action = "updated"
                    except PIDDoesNotExistError:
                        record = create_doc(data, schema)
                        action = "inserted"
                elif mode == "insert":
                    try:
                        pid = PersistentIdentifier.get(
                            "docid", str(slugify(data.get("slug", data["title"])))
                        )
                        if pid:
                            click.echo(
                                "Record docid {} exists already;"
                                " cannot insert it.  ".format(
                                    str(slugify(data.get("slug", data["title"])))
                                ),
                                err=True,
                            )
                            return
                    except PIDDoesNotExistError:
                        record = create_doc(data, schema)
                        action = "inserted"
                else:
                    try:
                        pid = PersistentIdentifier.get(
                            "docid", str(slugify(data.get("slug", data["title"])))
                        )
                    except PIDDoesNotExistError:
                        click.echo(
                            "Record docid {} does not exist; "
                            "cannot replace it.".format(
                                str(slugify(data.get("slug", data["title"])))
                            ),
                            err=True,
                        )
                        return
                    record = update_doc(pid, data)
                    action = "updated"
                record.commit()
                db.session.commit()
                click.echo(
                    " Record docid {0} {1}.".format(
                        str(slugify(data.get("slug", data["title"]))), action
                    )
                )
                indexer.index(record)
                db.session.expunge_all()


@fixtures.command()
@with_appcontext
def pids():
    """Fetch and register PIDs."""
    from invenio_db import db
    from invenio_oaiserver.fetchers import onaiid_fetcher
    from invenio_oaiserver.minters import oaiid_minter
    from invenio_pidstore.errors import PIDDoesNotExistError
    from invenio_pidstore.fetchers import recid_fetcher
    from invenio_pidstore.models import PersistentIdentifier, PIDStatus
    from invenio_records.models import RecordMetadata

    recids = [r.id for r in RecordMetadata.query.all()]
    db.session.expunge_all()

    with click.progressbar(recids) as bar:
        for record_id in bar:
            record = RecordMetadata.query.get(record_id)
            try:
                pid = recid_fetcher(record.id, record.json)
                found = PersistentIdentifier.get(
                    pid_type=pid.pid_type,
                    pid_value=pid.pid_value,
                    pid_provider=pid.provider.pid_provider,
                )
                click.echo("Found {0}.".format(found))
            except PIDDoesNotExistError:
                db.session.add(
                    PersistentIdentifier.create(
                        pid.pid_type,
                        pid.pid_value,
                        object_type="rec",
                        object_uuid=record.id,
                        status=PIDStatus.REGISTERED,
                    )
                )
            except KeyError:
                click.echo("Skiped: {0}".format(record.id))
                continue

            pid_value = record.json.get("_oai", {}).get("id")
            if pid_value is None:
                assert "control_number" in record.json
                pid_value = current_app.config.get("OAISERVER_ID_PREFIX") + str(
                    record.json["control_number"]
                )

                record.json.setdefault("_oai", {})
                record.json["_oai"]["id"] = pid.pid_value

            pid = oaiid_fetcher(record.id, record.json)
            try:
                found = PersistentIdentifier.get(
                    pid_type=pid.pid_type,
                    pid_value=pid.pid_value,
                    pid_provider=pid.provider.pid_provider,
                )
                click.echo("Found {0}.".format(found))
            except PIDDoesNotExistError:
                pid = oaiid_minter(record.id, record.json)
                db.session.add(pid)

            flag_modified(record, "json")
            assert record.json["_oai"]["id"]
            db.session.add(record)
            db.session.commit()
            db.session.expunge_all()
