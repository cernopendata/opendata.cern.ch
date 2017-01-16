# -*- coding: utf-8 -*-

"""Command line interface for CERN Open Data Portal."""

from __future__ import absolute_import, print_function

import click
from flask import current_app
from invenio_base.app import create_cli
from sqlalchemy.orm.attributes import flag_modified

from .factory import create_app

cli = create_cli(create_app=create_app)
