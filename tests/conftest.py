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

import os
import shutil
import tempfile

import pytest
from flask import Flask

from cernopendata.factory import create_api


@pytest.fixture(scope="session")
def instance_path():
    """Default instance path."""
    path = tempfile.mkdtemp()

    yield path

    shutil.rmtree(path)


@pytest.fixture(scope="session")
def env_config(instance_path):
    """Default instance path."""
    os.environ.update(
        APP_INSTANCE_PATH=os.environ.get("INSTANCE_PATH", instance_path),
    )

    return os.environ


@pytest.fixture(scope="session")
def default_config():
    """Default configuration."""
    return dict(
        DEBUG_TB_ENABLED=False,
        SQLALCHEMY_DATABASE_URI=os.environ.get(
            "SQLALCHEMY_DATABASE_URI", "sqlite:///test.db"
        ),
        TESTING=True,
    )


@pytest.fixture(scope="session")
def app(env_config, default_config, instance_path):
    """Flask application fixture."""
    app = create_api(**default_config)

    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def database(app):
    """Setup database.

    Scope: module

    Normally, tests should use the function-scoped :py:data:`db` fixture
    instead. This fixture takes care of creating the database/tables and
    removing the tables once tests are done.
    """
    from invenio_db import db as db_
    from sqlalchemy_utils.functions import create_database, database_exists

    if not database_exists(str(db_.engine.url)):
        create_database(str(db_.engine.url))

    # Use unlogged tables for PostgreSQL (see https://github.com/sqlalchemy/alembic/discussions/1108)
    if db_.engine.name == "postgresql":
        from sqlalchemy.ext.compiler import compiles
        from sqlalchemy.schema import CreateTable

        @compiles(CreateTable)
        def _compile_unlogged(element, compiler, **kwargs):
            return compiler.visit_create_table(element).replace(
                "CREATE TABLE ",
                "CREATE UNLOGGED TABLE ",
            )

    db_.create_all()

    yield db_

    db_.session.remove()
    db_.drop_all()


def _search_create_indexes(current_search, current_search_client):
    """Create all registered search indexes."""
    from invenio_search.engine import search

    try:
        list(current_search.create())
    except search.RequestError:
        list(current_search.delete(ignore=[404]))
        list(current_search.create())
    current_search_client.indices.refresh()


def _search_delete_indexes(current_search):
    """Delete all registered search indexes."""
    list(current_search.delete(ignore=[404]))


@pytest.fixture(scope="module")
def search(app):
    """Setup and teardown all registered search indices.

    Scope: module

    This fixture will create all registered indexes in search and remove
    once done. Fixtures that perform changes (e.g. index or remove documents),
    should used the function-scoped :py:data:`search_clear` fixture to leave the
    indexes clean for the following tests.
    """
    from invenio_search import current_search, current_search_client

    _search_create_indexes(current_search, current_search_client)
    yield current_search_client
    _search_delete_indexes(current_search)
