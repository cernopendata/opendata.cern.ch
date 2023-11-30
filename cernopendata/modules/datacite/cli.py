# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Open Data Portal; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.
"""Command line interface for DataCite related commands."""

import os

import click
from click import ClickException
from datacite import schema40
from flask import current_app
from flask.cli import with_appcontext
from invenio_db import db
from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_pidstore.models import PersistentIdentifier
from invenio_records.api import Record

from .client import DataCiteMDSClientWrapper
from .providers import DataCiteProviderWrapper
from .serializers import DataCiteSerializer
from .utils import generate_doi


@click.group()
def datacite():
    """Commands for DataCite DOIs management."""


@datacite.command()
@with_appcontext
def registered():
    """Print all registered DOIs from DataCite."""
    dcp = DataCiteMDSClientWrapper()

    click.echo(dcp.doi_get_all())


@datacite.command(name="sync-pidstore")
@with_appcontext
def sync_pidstore():
    """Populate PID store with all DOIs registered in DataCite."""
    cli = DataCiteMDSClientWrapper()
    dois = cli.doi_get_all().split("\n")

    for doi in dois:
        try:
            PersistentIdentifier.get("doi", doi)
        except PIDDoesNotExistError:
            DataCiteProviderWrapper.create(pid_value=doi)
            click.echo("Record with doi {} added to PID store".format(doi))
    db.session.commit()

    click.echo("PID Store updated")


@datacite.command(name="gen-doi")
@with_appcontext
@click.option("--exp", help="Experiment name for DOI")
def gen_doi(exp):
    """Generate DOI for given experiment, unique within PID store."""
    prefix = current_app.config.get("PIDSTORE_DATACITE_DOI_PREFIX")
    doi = generate_doi(prefix, exp)

    click.echo(doi)


@datacite.command()
@click.option("--recid", help="Test serialisation of record with given recid")
@with_appcontext
def test_serialisation(recid):
    """Test serialisation of record with given recid."""
    uuid = PersistentIdentifier.get("recid", recid).object_uuid
    record = Record.get_record(uuid)
    experiment = record.get("experiment", None)
    doi = record["doi"]
    # serialize record to schema40
    doc = DataCiteSerializer().dump(record)
    schema40.validate(doc)
    doc = schema40.tostring(doc)
    click.echo(doc)


@datacite.command()
@click.option("--recid", help="Register record with given recid")
@with_appcontext
def register(recid):
    """Register record with given recid in DataCite."""
    uuid = PersistentIdentifier.get("recid", recid).object_uuid
    record = Record.get_record(uuid)
    experiment = record.get("experiment", None)
    doi = record["doi"]

    try:
        provider = DataCiteProviderWrapper.get(pid_value=doi, pid_type="doi")
    except PIDDoesNotExistError:
        provider = DataCiteProviderWrapper.create(pid_value=doi, experiment=experiment)

    # serialize record to schema40
    doc = DataCiteSerializer().dump(record)
    schema40.validate(doc)
    doc = schema40.tostring(doc)
    landing_page = os.path.join(
        current_app.config.get("PIDSTORE_LANDING_BASE_URL"), recid
    )

    provider.register(url=landing_page, doc=doc)
    db.session.commit()

    click.echo("Record registered with DOI {}".format(doi))


@datacite.command()
@click.option("--recid", help="Update metadata for record with given recid")
@with_appcontext
def update(recid):
    """Update metadata for record with given recid in DataCite."""
    uuid = PersistentIdentifier.get("recid", recid).object_uuid
    record = Record.get_record(uuid)
    doi = record["doi"]

    try:
        provider = DataCiteProviderWrapper.get(pid_value=doi, pid_type="doi")
    except PIDDoesNotExistError:
        raise ClickException(
            "Record with DOI {} not registered in DataCite.".format(doi)
        )

    # serialize record to schema40
    doc = DataCiteSerializer().dump(record)
    schema40.validate(doc)
    doc = schema40.tostring(doc)
    landing_page = os.path.join(
        current_app.config.get("PIDSTORE_LANDING_BASE_URL"), recid
    )

    provider.update(url=landing_page, doc=doc)
    db.session.commit()

    click.echo("Record with DOI {} updated in DataCite".format(doi))
