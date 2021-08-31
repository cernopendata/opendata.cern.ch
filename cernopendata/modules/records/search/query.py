# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2021 CERN.
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

"""Cernopendata Query factory for REST API."""

import itertools
import operator
from elasticsearch_dsl.query import Q, Range, Bool
from flask import current_app, request
from invenio_records_rest.errors import InvalidQueryRESTError
from invenio_records_rest.sorter import default_sorter_factory
from invenio_records_rest.facets import default_facets_factory

from .facets import cernopendata_facets_factory


def cernopendata_query_parser(query_string=None, show_ondemand=None):
    """Default parser that uses the Q() from elasticsearch_dsl.

    :param query_string: Query string from user

    :return: Query instance with raw query string
    """
    _query_string = query_string.split(" ")
    for index, _query_term in enumerate(_query_string):
        if "/" in _query_term and '"' not in _query_term:
            _query_string[index] = '"' + _query_term + '"'
        if "-" in _query_term and '"' not in _query_term:
            _query_string[index] = '"' + _query_term + '"'
    query_string = " ".join(_query_string)
    if query_string:
        _query = Q("query_string", query=query_string)
    else:
        _query = Q()

    if show_ondemand != 'true':
        _query = _query & \
            ~Q('match', **{'distribution.availability.keyword': 'ondemand'})

    return _query


def cernopendata_search_factory(self, search):
    """Customized parse query using invenio query parser.

    :param self: REST view
    :param search: Elastic search DSL search instance

    :return: Tuple with search instance and URL arguments
    """
    query_string = request.values.get("q")
    show_ondemand = request.values.get("ondemand")
    try:
        search = search.query(
            cernopendata_query_parser(query_string, show_ondemand)
        )
    except SyntaxError:
        current_app.logger.debug(
            "Failed parsing query: {0}".format(
                request.values.get("q", "")),
            exc_info=True)
        raise InvalidQueryRESTError()

    search_index = search._index[0]
    search, url_kwargs = cernopendata_facets_factory(search, search_index)
    search, sort_kwargs = default_sorter_factory(search, search_index)
    for key, value in sort_kwargs.items():
        url_kwargs.add(key, value)
    url_kwargs.add("q", query_string)

    return search, url_kwargs


def cernopendata_range_filter(field):
    """Create a range filter.

    :param field: Field name.
    :returns: Function that returns the Range query.
    """
    def inner(values):
        ineq_opers = [
            {'strict': 'gt', 'nonstrict': 'gte'},
            {'strict': 'lt', 'nonstrict': 'lte'}]
        range_query = []
        for _range in values:
            range_ends = _range.split('--')
            range_args = dict()
            # Add the proper values to the dict
            for (range_end, strict, opers) in zip(range_ends, ['>', '<'], ineq_opers):  # noqa
                if range_end:
                    # If first char is '>' for start or '<' for end
                    if range_end[0] == strict:
                        dict_key = opers['strict']
                        range_end = range_end[1:]
                    else:
                        dict_key = opers['nonstrict']
                    range_args[dict_key] = range_end
            range_query.append(Range(**{field: range_args}))
        return Bool(should=range_query)
    return inner


def cernopendata_nested_terms_filter(field, subfield, splitchar):
    """Create a nested term filter used for nested aggregations.

    :param field: Field name.
    :param subfield: Subfield name of a Field.
    :param splitchar: Character dividing the Field and Subfield.
    :returns: Function that returns the Nested terms query.
    """
    def inner(values):
        field_values = {}
        term_queries = []
        # Iterating through aggregation and nested aggregations
        for filter in values:
            # Get the aggregation type
            field_name = filter.split(splitchar)[0]

            # If aggregation type is not present in field_values,
            # add them to dict with a empty list
            if field_name not in field_values:
                field_values[field_name] = []

            # If `splitchar` is present in filter, append the
            # subfield aggregations to the belonging aggregation type key
            if splitchar in filter:
                subfield_value = filter.split(splitchar)[-1]
                field_values[field_name].append(subfield_value)

        # Iterate through aggregation type and
        # create term query with `AND` operation
        for k in field_values.keys():
            if field_values[k]:
                term_queries.append(
                    Q('term', **{field: k}) &
                    Q('terms', **{subfield: field_values[k]})
                )
            else:
                term_queries.append(Q('term', **{field: k}))

        # Return the query after creating a chain of `OR` queries.
        query = list(itertools.accumulate(term_queries, operator.or_))[-1]
        return query

    return inner
