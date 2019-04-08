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

"""Cernopendata Query factory for REST API."""

from __future__ import absolute_import, print_function

from elasticsearch_dsl.query import Q
from flask import current_app, request
from invenio_records_rest.errors import InvalidQueryRESTError
from invenio_records_rest.sorter import default_sorter_factory

from .facets import cernopendata_facets_factory


def cernopendata_search_factory(self, search, query_parser=None):
    """Customized Parse query using Invenio-Query-Parser.

    By default we hide the results that have availability:ondemand.

    :param self: REST view.
    :param search: Elastic search DSL search instance.
    :returns: Tuple with search instance and URL arguments.
    """
    def _default_parser(qstr=None, ondemand=None):
        """Default parser that uses the Q() from elasticsearch_dsl."""
        q = Q('query_string', query=qstr) if qstr else Q()

        # by default hide ondemand ones
        if not ondemand:
            q = q & ~Q('match', **{'availability.keyword': 'ondemand'})

        return q

    query_string = request.values.get('q')
    ondemand = request.values.get('ondemand', False)  # this is a workaround
    query_parser = query_parser or _default_parser

    try:
        search = search.query(query_parser(query_string, ondemand))

    except SyntaxError:
        current_app.logger.debug(
            "Failed parsing query: {0}".format(
                request.values.get('q', '')),
            exc_info=True)
        raise InvalidQueryRESTError()

    search_index = search._index[0]
    search, urlkwargs = cernopendata_facets_factory(search, search_index)
    search, sortkwargs = default_sorter_factory(search, search_index)
    for key, value in sortkwargs.items():
        urlkwargs.add(key, value)

    urlkwargs.add('q', query_string)
    return search, urlkwargs
