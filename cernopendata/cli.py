# -*- coding: utf-8 -*-

"""Command line interface for CERN Open Data Portal."""

from __future__ import absolute_import, print_function

import click

from flask import current_app
from invenio_base.app import create_cli
from sqlalchemy.orm.attributes import flag_modified

from .factory import create_app

cli = create_cli(create_app=create_app)

@cli.group()
def fixtures():
    """Automate site bootstrap process and testing."""


@fixtures.command()
def collections():
    """Load default collections."""
    from invenio_db import db
    from invenio_collections.models import Collection

    from .fixtures import COLLECTIONS

    def load(collections, parent=None):
        """Create new collection."""
        for data in collections or []:
            collection = Collection(
                name=data['name'], dbquery=data.get('dbquery'),
                parent=parent
            )
            db.session.add(collection)
            db.session.flush()
            load(data.get('children'), parent=collection)

    load(COLLECTIONS)
    db.session.commit()


@fixtures.command()
def pids():
    """Fetch and register PIDs."""
    from invenio_db import db
    from invenio_oaiserver.fetchers import oaiid_fetcher
    from invenio_oaiserver.minters import oaiid_minter
    from invenio_pidstore.errors import PIDDoesNotExistError, \
        PersistentIdentifierError
    from invenio_pidstore.models import PIDStatus, PersistentIdentifier
    from invenio_pidstore.fetchers import recid_fetcher
    from invenio_records.models import RecordMetadata

    with click.progressbar(RecordMetadata.query.all()) as bar:
        for record in bar:
            pid = recid_fetcher(record.id, record.json)
            try:
                found = PersistentIdentifier.get(
                    pid_type=pid.pid_type,
                    pid_value=pid.pid_value,
                    pid_provider=pid.provider.pid_provider
                )
                click.echo('Found {0}.'.format(found))
            except PIDDoesNotExistError:
                db.session.add(
                    PersistentIdentifier.create(
                        pid.pid_type, pid.pid_value,
                        object_type='rec', object_uuid=record.id,
                        status=PIDStatus.REGISTERED
                    )
                )

            pid_value = record.json.get('_oai', {}).get('id')
            if pid_value is None:
                assert 'control_number' in record.json
                pid_value = current_app.config.get(
                    'OAISERVER_ID_PREFIX'
                ) + str(record.json['control_number'])

                record.json.setdefault('_oai', {})
                record.json['_oai']['id'] = pid.pid_value

            pid = oaiid_fetcher(record.id, record.json)
            try:
                found = PersistentIdentifier.get(
                    pid_type=pid.pid_type,
                    pid_value=pid.pid_value,
                    pid_provider=pid.provider.pid_provider
                )
                click.echo('Found {0}.'.format(found))
            except PIDDoesNotExistError:
                pid = oaiid_minter(record.id, record.json)
                db.session.add(pid)

            flag_modified(record, 'json')
            assert record.json['_oai']['id']
            db.session.add(record)

    db.session.commit()
