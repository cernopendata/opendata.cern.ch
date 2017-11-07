# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2016, 2017 CERN.
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

"""CERN Open Data views."""

from __future__ import absolute_import, print_function

from flask import Blueprint, redirect, request, url_for
from invenio_search_ui.views import search as invenio_search_view

blueprint = Blueprint(
    'cernopendata',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.record_once
def redefine_search_endpoint(blueprint_setup):
    """Redefine invenio search endpoint."""
    blueprint_setup.app.view_functions[
        'invenio_search_ui.search'] = search_wrapper


def search_wrapper():
    """Wrap default invenio search endpoint."""
    # translate p parameter to q (backwards compatibility)
    # only if q itself not passed
    if 'p' in request.args and 'q' not in request.args:
        values = request.args.to_dict()
        values['q'] = values.pop('p')
        return redirect(url_for('invenio_search_ui.search', **values))
    else:
        return invenio_search_view()


@blueprint.route('/ping', methods=['HEAD', 'GET'])
def ping():
    """Load balancer ping view."""
    return 'OK'
