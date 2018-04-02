# -*- coding: utf-8 -*-

"""Command line interface for CERN Open Data Portal."""

from __future__ import absolute_import, print_function

from invenio_base.app import create_cli

from .factory import create_app
from .modules.datacite.cli import datacite
from .modules.fixtures.cli import fixtures

cli = create_cli(create_app=create_app)
cli.add_command(fixtures)
cli.add_command(datacite)
