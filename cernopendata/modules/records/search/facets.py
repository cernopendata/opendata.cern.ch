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

"""Cernopendata facets factory for REST API."""

from __future__ import absolute_import, print_function

from flask import current_app
from invenio_records_rest.facets import (
    _create_filter_dsl,
    _post_filter,
    _query_filter
)
from werkzeug.datastructures import MultiDict


def _aggregations(search, definitions, urlkwargs, filters):
    """Add aggregations to query.

    :param search: Invenio Search Object
    :param definitions: Dictionary of all available facets definitions
    :param urlkwargs: Argument from the query
    :param filters: Filters applied on facets

    :return: Search object with custom filtered object in aggregation
             after every filter is applied.
    """

    def without_nested_subtypes(facet_filters, facet_names):
        """Remove the nested subtypes from the filter.

        Example: If `CMS` from Experiment type is selected
        then aggregation count of other subtypes in Experiment
        type will not be changed.
        """
        new_facet_filters = facet_filters.copy()
        for name in facet_names:
            new_facet_filters.pop(name)
        return new_facet_filters

    if definitions:
        for facet_name, aggregation in definitions.items():
            # get nested aggs
            facet_names = [facet_name]
            facet_names.extend(aggregation.get("aggs", {}).keys())

            # collect filters except for aggs and nested aggs (if any)
            facet_filters, _ = _create_filter_dsl(
                            urlkwargs,
                            without_nested_subtypes(
                                filters,
                                facet_names)
                        )
            if facet_filters:
                aggregation = {
                    "filter":
                        {
                            "bool":
                                {
                                    "must": [
                                            facet_filter.to_dict()
                                            for facet_filter in facet_filters
                                        ]
                                }
                        },
                    "aggs": {"filtered": aggregation},
                }
            search.aggs[facet_name] = aggregation
    return search


def cernopendata_facets_factory(search, index):
    """Add a cernopendata facets to query.

    :param search: Search object.
    :param index: Index name.

    :returns: A tuple containing the new search object
              and a dictionary with all fields and values used.
    """
    urlkwargs = MultiDict()
    facets = current_app.config["RECORDS_REST_FACETS"].get(index)

    if facets is not None:
        # Aggregations
        search = _aggregations(
            search,
            facets.get("aggs", {}), urlkwargs, facets.get("post_filters", {}))

        # Query filter
        search, urlkwargs = _query_filter(
            search, urlkwargs, facets.get("filters", {}))

        # Post filter
        search, urlkwargs = _post_filter(
            search, urlkwargs, facets.get("post_filters", {}))

    return (search, urlkwargs)
