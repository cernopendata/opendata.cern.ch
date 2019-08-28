# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017, 2018 CERN.
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

from invenio_records_files.api import _Record
from invenio_records_rest.config import RECORDS_REST_ENDPOINTS
from invenio_records_rest.facets import range_filter, terms_filter
from invenio_records_rest.utils import allow_all

from cernopendata.modules.pages.config import *
from cernopendata.modules.theme.config import *

# Debug
DEBUG = os.environ.get(
    'DEBUG',
    False
)
TEMPLATES_AUTO_RELOAD = DEBUG

# Piwik tracking code: set None to disabled it
THEME_PIWIK_ID = os.environ.get('PIWIK_ID', None)

SITE_URL = os.environ.get('CERNOPENDATA_SITE_URL', 'opendata.cern.ch')

# Logging - Set up Sentry for Invenio-Logging
SENTRY_DSN = os.environ.get(
        "SENTRY_DSN", None
    )

LOGGING_SENTRY_CELERY = os.environ.get(
        "LOGGING_SENTRY_CELERY", False
    )

# Assets
# ======
#: Switch of assets debug.
# ASSETS_DEBUG = DEBUG
#: Switch of automatic building.
# ASSETS_AUTO_BUILD = True


# Static file
COLLECT_STORAGE = 'flask_collect.storage.link' \
    if DEBUG else 'flask_collect.storage.file'

# Cache
CACHE_TYPE = 'redis'

# Celery
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']

# JSONSchemas
JSONSCHEMAS_ENDPOINT = '/schema'
JSONSCHEMAS_HOST = 'opendata.cern.ch'
JSONSCHEMAS_URL_SCHEME = 'http'

# HOST_URI
HOST_URI = '{}://{}'.format(JSONSCHEMAS_URL_SCHEME,
                            JSONSCHEMAS_HOST)

# OAI Server
OAISERVER_RECORD_INDEX = 'records'
OAISERVER_ID_PREFIX = 'oai:cernopendata:recid/'

# Records
# Add tuple as array type on record validation
# http://python-jsonschema.readthedocs.org/en/latest/validate/#validating-types
RECORDS_VALIDATION_TYPES = {
    'array': (list, tuple),
}

RECORDS_UI_EXPORT_FORMATS = dict(
    docid=dict(
        json=dict(
            title='JSON',
            serializer='cernopendata.modules.records.serializers.json',
        ),
        jsonld=dict(
            title='JSON-LD',
            serializer='cernopendata.modules.records.serializers.'
                       'schemaorg_jsonld',
        )
    ),
    recid=dict(
        json=dict(
            title='JSON',
            serializer='cernopendata.modules.records.serializers.json',
        ),
        jsonld=dict(
            title='JSON-LD',
            serializer='cernopendata.modules.records.serializers.'
                       'schemaorg_jsonld',
        )
    ),
)

RECORDS_UI_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        route='/record/<pid_value>',
        permission_factory_imp=None,
        record_class='invenio_records_files.api:Record',
        view_imp='cernopendata.modules.records.utils:record_metadata_view',
    ),
    recid_files=dict(
        pid_type='recid',
        route='/record/<pid_value>/files/<path:filename>',
        view_imp='cernopendata.modules.records.utils:file_download_ui',
        record_class='invenio_records_files.api:Record',
    ),
    recid_files_assets=dict(
        pid_type='recid',
        route='/record/<pid_value>/files/assets/<path:filepath>',
        view_imp='cernopendata.modules.records.utils:eos_file_download_ui',
        record_class='invenio_records_files.api:Record',
    ),
    recid_files_page=dict(
        pid_type='recid',
        route='/record/<pid_value>/filepage/<int:page>',
        view_imp='cernopendata.modules.records.utils:record_file_page',
        record_class='invenio_records_files.api:Record',
    ),
    recid_preview=dict(
        pid_type='recid',
        route='/record/<pid_value>/preview/<path:filename>',
        view_imp='invenio_previewer.views:preview',
        record_class='invenio_records_files.api:Record',
    ),
    recid_export=dict(
        pid_type='recid',
        route='/record/<pid_value>/export/<format>',
        view_imp='cernopendata.modules.records.utils:export_json_view',
        record_class='invenio_records_files.api:Record',
    ),
    termid=dict(
        pid_type='termid',
        route='/glossary/<pid_value>',
        template='cernopendata_records_ui/terms/detail.html',
        permission_factory_imp=None,
    ),
    docid=dict(
        pid_type='docid',
        route='/docs/<pid_value>',
        template='cernopendata_records_ui/docs/detail.html',
        permission_factory_imp=None,
        record_class='invenio_records_files.api:Record',
    ),
    docid_export=dict(
        pid_type='docid',
        route='/docs/<pid_value>/export/<format>',
        view_imp='invenio_records_ui.views.export',
        template='cernopendata_records_ui/default_export.html',
    ),
)

RECORDS_REST_ENDPOINTS['recid']['search_index'] = '_all'

RECORDS_REST_ENDPOINTS['recid'].update({
    'search_factory_imp': 'cernopendata.modules.records.search.query'
                          ':cernopendata_search_factory',
    'pid_minter': 'cernopendata_recid_minter',
    'pid_fetcher': 'cernopendata_recid_fetcher',
    'record_class': _Record,
    'links_factory_imp': 'cernopendata.modules.records.links:links_factory',
    'record_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_response'),
        'application/ld+json': ('cernopendata.modules.records.serializers'
                                ':schemaorg_jsonld_response'),
    },
})

RECORDS_REST_ENDPOINTS['termid'] = {
    'pid_type': 'termid',
    'pid_minter': 'cernopendata_termid_minter',
    'pid_fetcher': 'cernopendata_termid_fetcher',
    'record_class': _Record,
    'links_factory_imp': 'cernopendata.modules.records.links:links_factory',
    'default_media_type': 'application/json',
    'max_result_window': 10000,
    'item_route': '/glossary/<pid(termid):pid_value>',
    'list_route': '/glossary',
    'record_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_response'),
        'application/ld+json': ('cernopendata.modules.records.serializers'
                                ':schemaorg_jsonld_response'),
    },
    'search_index': 'records-glossary-term-v1.0.0',
    'search_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_search'),
    },
}

RECORDS_REST_ENDPOINTS['docid'] = {
    'pid_type': 'docid',
    'pid_minter': 'cernopendata_docid_minter',
    'pid_fetcher': 'cernopendata_docid_fetcher',
    'record_class': _Record,
    'links_factory_imp': 'cernopendata.modules.records.links:links_factory',
    'default_media_type': 'application/json',
    'max_result_window': 10000,
    'item_route': '/docs/<pid(docid):pid_value>',
    'list_route': '/docs',
    'record_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_response'),
        'application/ld+json': ('cernopendata.modules.records.serializers'
                                ':schemaorg_jsonld_response'),
    },
    'search_index': 'records-docs-v1.0.0',
    'search_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_search'),
    },
}

RECORDS_REST_SORT_OPTIONS = {
    "_all": {
        'bestmatch': dict(
            fields=['-_score'],
            title='Best match',
            default_order='asc',
            order=1,
        ),
        'mostrecent': dict(
            fields=['-_created'],
            title='Most recent',
            default_order='asc',
            order=2,
        ),
        'title': dict(fields=['title.keyword'],
                      title='Title A-Z',
                      default_order='asc',
                      order=1)
    },
    "records-glossary-term-v1.0.0": {
        'anchor': dict(fields=['anchor'],
                       title='Title',
                       default_order='asc',
                       order=1),
    }
}

RECORDS_REST_DEFAULT_SORT = {
    'records-glossary-term-v1.0.0': {
        'noquery': 'anchor'
    }
}

RECORDS_REST_FACETS = {
    '_all': {
        'aggs': dict(
            experiment=dict(terms=dict(
                field='experiment.keyword',
                order=dict(_term='asc'))),
            type=dict(terms=dict(
                field='type.primary.keyword',
                order=dict(_term='asc')),
                aggs=dict(subtype=dict(terms=dict(
                          field="type.secondary.keyword",
                          order=dict(_term='asc'))))),
            file_type=dict(terms=dict(
                field='distribution.formats.keyword',
                size=50,
                order=dict(_term='asc'))),
            year=dict(terms=dict(
                field='date_created.keyword',
                order=dict(_term='asc'))),
            keywords=dict(terms=dict(
                field='keywords.keyword',
                order=dict(_term='asc'))),
            collision_type=dict(terms=dict(
                field='collision_information.type.keyword',
                order=dict(_term='asc'))),
            collision_energy=dict(terms=dict(
                field='collision_information.energy.keyword',
                order=dict(_term='asc'))),
            category=dict(terms=dict(
                field='categories.primary.keyword',
                order=dict(_term='asc')),
                aggs=dict(subcategory=dict(terms=dict(
                          field="categories.secondary.keyword",
                          order=dict(_term='asc'))))),
            availability=dict(terms=dict(
                field='distribution.availability.keyword',
                order=dict(_term='asc'))),
            signature=dict(terms=dict(
                field='signature.keyword',
                order=dict(_term='asc'))),
            event_number={
                'range': {
                    'field': 'distribution.number_events',
                    'ranges': [
                        {
                            'key': '0--999',
                            'from': 0,
                            'to': 999
                        },
                        {
                            'key': '1000--9999',
                            'from': 1000,
                            'to': 9999
                        },
                        {
                            'key': '10000--99999',
                            'from': 10000,
                            'to': 99999
                        },
                        {
                            'key': '100000--999999',
                            'from': 100000,
                            'to': 999999
                        },
                        {
                            'key': '1000000--9999999',
                            'from': 1000000,
                            'to': 9999999
                        },
                        {
                            'key': '10000000--',
                            'from': 10000000
                        }
                    ]
                }
            }
        ),
        'post_filters': dict(
            experiment=terms_filter('experiment.keyword'),
            type=terms_filter('type.primary.keyword'),
            subtype=terms_filter('type.secondary.keyword'),
            year=terms_filter('date_created.keyword'),
            tags=terms_filter('tags.keyword'),
            keywords=terms_filter('keywords.keyword'),
            collision_type=terms_filter('collision_information.type.keyword'),
            collision_energy=terms_filter('collision_information.energy'
                                          '.keyword'),
            category=terms_filter('categories.primary.keyword'),
            subcategory=terms_filter('categories.secondary.keyword'),
            file_type=terms_filter('distribution.formats.keyword'),
            collections=terms_filter('collections.keyword'),
            availability=terms_filter('distribution.availability.keyword'),
            signature=terms_filter('signature.keyword'),
            event_number=range_filter('distribution.number_events')
        )
    }
}

"""Facets per index for the default facets factory."""

# Files
# ======
#: Permission factory to control the files access from the REST interface.
FILES_REST_PERMISSION_FACTORY = allow_all
#: Allow URI's longer than 255 chars.
FILES_REST_FILE_URI_MAX_LEN = os.environ.get(
    "FILES_REST_FILE_URI_MAX_LEN",
    512
)
#: Files max size threshold(bytes)
CERNOPENDATA_MAX_DOWNLOAD_SIZE = os.environ.get(
    "CERNOPENDATA_MAX_DOWNLOAD_SIZE",
    200000000
)
#: Make download availalbe for Root files
CERNOPENDATA_DISABLE_DOWNLOADS = os.environ.get(
    "CERNOPENDATA_DISABLE_DOWNLOADS",
    False
)
# Search
# ======
#: Default API endpoint for search UI.
SEARCH_UI_SEARCH_API = "/api/records/"
#: Default template for search UI.
# SEARCH_UI_BASE_TEMPLATE = 'cernopendata/page.html'
#: Default template for search UI.
SEARCH_UI_SEARCH_TEMPLATE = 'cernopendata/search.html'
SEARCH_UI_JSTEMPLATE_FACETS = 'templates/cernopendata_search_ui/facets.html'
SEARCH_UI_JSTEMPLATE_ERROR = 'templates/cernopendata_search_ui/error.html'
#: Default Elasticsearch document type.
SEARCH_DOC_TYPE_DEFAULT = None
#: Do not map any keywords.
SEARCH_ELASTIC_KEYWORD_MAPPING = {}

SEARCH_UI_SEARCH_INDEX = '_all'

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

# DataCite
# ========
#: DataCite API - URL endpoint.
PIDSTORE_DATACITE_URL = "https://mds.datacite.org"

#: DataCite API - Disable test mode (we however use the test prefix).
PIDSTORE_DATACITE_TESTMODE = os.environ.get(
    "APP_PIDSTORE_DATACITE_TESTMODE",
    False
)

#: DataCite API - Prefix for minting DOIs in (10.5072 is a test prefix).
PIDSTORE_DATACITE_DOI_PREFIX = os.environ.get(
    "APP_PIDSTORE_DATACITE_DOI_PREFIX",
    "10.5072"
)

#: DataCite MDS username.
PIDSTORE_DATACITE_USERNAME = os.environ.get(
    "APP_PIDSTORE_DATACITE_USERNAME",
    "CERN.OPENDATA"
)

#: DataCite MDS password.
PIDSTORE_DATACITE_PASSWORD = os.environ.get(
    "APP_PIDSTORE_DATACITE_PASSWORD",
    "CHANGE_ME"
)

#: Base URL for landing page
PIDSTORE_LANDING_BASE_URL = os.environ.get(
    "APP_PIDSTORE_LANDING_BASE_URL",
    "http://opendata.cern.ch/record"
)

if os.environ.get('ELASTICSEARCH_USER') and \
   os.environ.get('ELASTICSEARCH_PASSWORD'):
    params = dict(
        http_auth=(os.environ.get('ELASTICSEARCH_USER'),
                   os.environ.get('ELASTICSEARCH_PASSWORD')),
        use_ssl=str(os.environ.get('ELASTICSEARCH_USE_SSL')).lower()
        in ('true'),
        verify_certs=str(os.environ.get('ELASTICSEARCH_VERIFY_CERTS')).lower()
        in ('true'),
    )
else:
    params = {}

SEARCH_ELASTIC_HOSTS = [
    dict(
        host=os.environ.get('ELASTICSEARCH_HOST',
                            'elasticsearch'),
        port=int(os.environ.get('ELASTICSEARCH_PORT',
                                '9200')),
        **params
    )
]
