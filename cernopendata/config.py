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

"""CERN Open Data configuration."""

from __future__ import absolute_import, print_function

import os

from invenio_marc21.config import \
    MARC21_REST_ENDPOINTS as RECORDS_REST_ENDPOINTS
from invenio_records_rest.facets import terms_filter

from cernopendata.modules.pages.config import *
from cernopendata.modules.theme.config import *

# Debug
DEBUG = True
TEMPLATES_AUTO_RELOAD = True

# Static file
COLLECT_STORAGE = 'flask_collect.storage.file'
# COLLECT_STORAGE = 'flask_collect.storage.link'

# Cache
CACHE_TYPE = 'redis'

# Celery
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']

# JSONSchemas
JSONSCHEMAS_ENDPOINT = '/schema'
JSONSCHEMAS_HOST = '127.0.0.1'
# JSONSCHEMAS_URL_SCHEME = 'http'

# OAI Server
OAISERVER_RECORD_INDEX = 'marc21'
OAISERVER_ID_PREFIX = 'oai:cernopendata:recid/'

# Records
# Add tuple as array type on record validation
# http://python-jsonschema.readthedocs.org/en/latest/validate/#validating-types
RECORDS_VALIDATION_TYPES = {
    'array': (list, tuple),
}

RECORDS_UI_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        route='/record/<pid_value>',
        template='invenio_marc21/detail.html',
        permission_factory_imp=None,
    ),
    termid=dict(
        pid_type='termid',
        route='/terms/<pid_value>',
        template='cernopendata_records_ui/terms/detail.html',
        permission_factory_imp=None,
    )
)

RECORDS_REST_ENDPOINTS['recid']['search_index'] = '_all'
RECORDS_REST_ENDPOINTS['termid'] = {
    'pid_type': 'termid',
    'pid_minter': 'cernopendata_termid_minter',
    'pid_fetcher': 'cernopendata_termid_fetcher',
    'default_media_type': 'application/json',
    'max_result_window': 10000,
    'item_route': '/terms/<pid(termid):pid_value>',
    'list_route': '/terms',
    'record_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_response'),
    },
    'search_index': 'records-term-v1.0.0',
    'search_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_search'),
    },
}

RECORDS_REST_FACETS = dict(
    _all=dict(
        aggs=dict(
            category=dict(terms=dict(field='collections.secondary')),
            collections=dict(terms=dict(field='collections.primary')),
            run=dict(terms=dict(
                field='production_publication_distribution_manufacture_and_'
                      'copyright_notice.'
                      'date_of_production_publication_distribution_'
                      'manufacture_or_copyright_notice'
            )),
        ),
        post_filters=dict(
            category=terms_filter('collections.secondary'),
            collections=terms_filter('collections.primary'),
            run=terms_filter(
                'production_publication_distribution_manufacture_and_'
                'copyright_notice.'
                'date_of_production_publication_distribution_'
                'manufacture_or_copyright_notice'
            ),
        )
    )
)
"""Facets per index for the default facets factory."""

# Search
# ======
#: Default API endpoint for search UI.
SEARCH_UI_SEARCH_API = "/api/records/"
#: Default template for search UI.
# SEARCH_UI_BASE_TEMPLATE = 'cernopendata/page.html'
#: Default template for search UI.
SEARCH_UI_SEARCH_TEMPLATE = 'cernopendata/search.html'
#: Default Elasticsearch document type.
SEARCH_DOC_TYPE_DEFAULT = None
#: Do not map any keywords.
SEARCH_ELASTIC_KEYWORD_MAPPING = {}

# OAI-PMH
# =======
#: Default Elasticsearch index.
OAISERVER_RECORD_INDEX = '_all'
#: OAI ID prefix.
OAISERVER_ID_PREFIX = 'oai:opendata.cern.ch:recid/'

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'APP_SQLALCHEMY_DATABASE_URI',
    'postgresql+psycopg2://localhost/cernopendata'
)
