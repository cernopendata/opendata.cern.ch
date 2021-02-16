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

from flask import Blueprint, current_app, redirect, request, url_for
from invenio_search_ui.views import search as invenio_search_view

from cernopendata.config import FACET_HIERARCHY

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
    # translate old search query params to new format
    # e.g. type=Dataset => f=type:Dataset
    facets = current_app.config['RECORDS_REST_FACETS']
    facet_keys = facets['_all']['aggs'].keys()
    args = request.args.to_dict(flat=False)
    if set(facet_keys).intersection(set(args.keys())):
        qs = translate_search_url(args, facets)
        return redirect(url_for('invenio_search_ui.search', **qs))

    # translate p parameter to q (backwards compatibility)
    # only if q itself not passed
    if 'p' in request.args and 'q' not in request.args:
        values = request.args.to_dict()
        values['q'] = values.pop('p')
        return redirect(url_for('invenio_search_ui.search', **values))
    else:
        return invenio_search_view()


def translate_search_url(args, facets):
    """Translate old search querystring args to new ones."""
    subagg_agg_mapping = {}
    aggs = facets["_all"]["aggs"]
    for agg, agg_value in aggs.items():
        if agg_value.get("aggs"):
            for subagg in agg_value["aggs"].keys():
                subagg_agg_mapping[subagg] = agg

    parent_child_qs = []
    for subagg, agg in subagg_agg_mapping.items():
        if subagg in args:
            agg_values = args.pop(agg)
            subagg_values = args.pop(subagg)
            for agg_v in agg_values:
                matching_subaggs = [
                    subagg_v
                    for subagg_v in FACET_HIERARCHY[agg]
                    .get(agg_v, {})
                    .get(subagg, {})
                    .intersection(set(subagg_values))
                ]
                if matching_subaggs:
                    for subagg_v in matching_subaggs:
                        parent_child_qs.append(
                            f"{agg}:{agg_v}+{subagg}:{subagg_v}"
                        )
                else:
                    parent_child_qs.append(f"{agg}:{agg_v}")

    qs_values = {"f": []}
    if parent_child_qs:
        qs_values["f"].extend(parent_child_qs)

    for arg, arg_v in args.items():
        if arg in aggs.keys():
            qs_values["f"].append(f"{arg}:{arg_v[0]}")
        else:
            qs_values[arg] = arg_v
    return qs_values


@blueprint.route('/ping', methods=['HEAD', 'GET'])
def ping():
    """Load balancer ping view."""
    return 'OK'
