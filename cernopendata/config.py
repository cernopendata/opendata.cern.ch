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

from invenio_records_files.api import _Record
from invenio_records_rest.config import RECORDS_REST_ENDPOINTS
from invenio_records_rest.facets import terms_filter
from invenio_records_rest.utils import allow_all

from cernopendata.modules.pages.config import *
from cernopendata.modules.theme.config import *

# Debug
DEBUG = True
TEMPLATES_AUTO_RELOAD = True

# Assets
# ======
#: Switch of assets debug.
# ASSETS_DEBUG = True
#: Switch of automatic building.
# ASSETS_AUTO_BUILD = True


# Static file
# COLLECT_STORAGE = 'flask_collect.storage.file'
COLLECT_STORAGE = 'flask_collect.storage.link'

# Cache
CACHE_TYPE = 'redis'

# Celery
CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']

# JSONSchemas
JSONSCHEMAS_ENDPOINT = '/schema'
JSONSCHEMAS_HOST = '127.0.0.1'
# JSONSCHEMAS_URL_SCHEME = 'http'

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
    artid=dict(
        json=dict(
            title='JSON',
            serializer='cernopendata.modules.records.serializers.json',
        )
    ),
    recid=dict(
        json=dict(
            title='JSON',
            serializer='cernopendata.modules.records.serializers.json',
        )
    ),
    datid=dict(
        json=dict(
            title='JSON',
            serializer='cernopendata.modules.records.serializers.json',
        )
    ),
    softid=dict(
        json=dict(
            title='JSON',
            serializer='cernopendata.modules.records.serializers.json',
        )
    )
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
    recid_preview=dict(
        pid_type='recid',
        route='/record/<pid_value>/preview/<path:filename>',
        view_imp='invenio_previewer.views:preview',
        record_class='invenio_records_files.api:Record',
    ),
    recid_export=dict(
        pid_type='recid',
        route='/record/<pid_value>/export/<format>',
        view_imp='invenio_records_ui.views.export',
        template='cernopendata_records_ui/default_export.html',
        record_class='invenio_records_files.api:Record',
    ),
    datid=dict(
        pid_type='datid',
        route='/datasets/<path:pid_value>',
        template='cernopendata_records_ui/records/dataset_detail.html',
        record_class='invenio_records_files.api:Record',
        permission_factory_imp=None,
    ),
    datid_files=dict(
        pid_type='datid',
        route='/datasets/<path:pid_value>/files/<path:filename>',
        view_imp='cernopendata.modules.records.utils:file_download_ui',
        record_class='invenio_records_files.api:Record',
    ),
    datid_export=dict(
        pid_type='datid',
        route='/datasets/<path:pid_value>/export/<format>',
        view_imp='invenio_records_ui.views.export',
        template='cernopendata_records_ui/default_export.html',
    ),
    softid=dict(
        pid_type='softid',
        route='/software/<pid_value>',
        template='cernopendata_records_ui/records/software_detail.html',
        record_class='invenio_records_files.api:Record',
        permission_factory_imp=None,
    ),
    softid_files=dict(
        pid_type='softid',
        route='/software/<pid_value>/files/<path:filename>',
        view_imp='cernopendata.modules.records.utils:file_download_ui',
        record_class='invenio_records_files.api:Record',
    ),
    softid_export=dict(
        pid_type='softid',
        route='/software/<pid_value>/export/<format>',
        view_imp='invenio_records_ui.views.export',
        template='cernopendata_records_ui/default_export.html',
        record_class='invenio_records_files.api:Record',
    ),
    termid=dict(
        pid_type='termid',
        route='/glossary/<pid_value>',
        template='cernopendata_records_ui/terms/detail.html',
        permission_factory_imp=None,
    ),
    artid=dict(
        pid_type='artid',
        route='/articles/<pid_value>',
        template='cernopendata_records_ui/articles/detail.html',
        permission_factory_imp=None,
        record_class='invenio_records_files.api:Record',
    ),
    artid_export=dict(
        pid_type='artid',
        route='/articles/<pid_value>/export/<format>',
        view_imp='invenio_records_ui.views.export',
        template='cernopendata_records_ui/default_export.html',
    ),
)

RECORDS_REST_ENDPOINTS['recid']['search_index'] = '_all'

RECORDS_REST_ENDPOINTS['recid'].update({
    'pid_minter': 'cernopendata_recid_minter',
    'pid_fetcher': 'cernopendata_recid_fetcher',
    'record_class': _Record,
    'links_factory_imp': 'cernopendata.modules.records.links:links_factory'
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
    },
    'search_index': 'records-glossary-term-v1.0.0',
    'search_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_search'),
    },
}

RECORDS_REST_ENDPOINTS['artid'] = {
    'pid_type': 'artid',
    'pid_minter': 'cernopendata_articleid_minter',
    'pid_fetcher': 'cernopendata_articleid_fetcher',
    'record_class': _Record,
    'links_factory_imp': 'cernopendata.modules.records.links:links_factory',
    'default_media_type': 'application/json',
    'max_result_window': 10000,
    'item_route': '/articles/<pid(artid):pid_value>',
    'list_route': '/articles',
    'record_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_response'),
    },
    'search_index': 'records-article-v1.0.0',
    'search_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_search'),
    },
}

RECORDS_REST_ENDPOINTS['datid'] = {
    'pid_type': 'datid',
    'pid_minter': 'cernopendata_datasetid_minter',
    'pid_fetcher': 'cernopendata_datasetid_fetcher',
    'record_class': _Record,
    'links_factory_imp': 'cernopendata.modules.records.links:links_factory',
    'default_media_type': 'application/json',
    'max_result_window': 10000,
    'item_route': '/datasets/<pidpath(datid):pid_value>',
    'list_route': '/datasets',
    'record_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_response'),
    },
    'search_index': 'records-datasets-v1.0.0',
    'search_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_search'),
    },
}

RECORDS_REST_ENDPOINTS['softid'] = {
    'pid_type': 'softid',
    'pid_minter': 'cernopendata_softid_minter',
    'pid_fetcher': 'cernopendata_softid_fetcher',
    'record_class': _Record,
    'links_factory_imp': 'cernopendata.modules.records.links:links_factory',
    'default_media_type': 'application/json',
    'max_result_window': 10000,
    'item_route': '/software/<pid(softid):pid_value>',
    'list_route': '/software',
    'record_serializers': {
        'application/json': ('invenio_records_rest.serializers'
                             ':json_v1_response'),
    },
    'search_index': 'records-software-v1.0.0',
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
        'title': dict(fields=['title'],
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
                field='experiment',
                min_doc_count=0,
                order=dict(_term='asc'))),
            type=dict(terms=dict(
                field='type.primary',
                min_doc_count=0,
                order=dict(_term='asc')),
                aggs=dict(subtype=dict(terms=dict(
                          field="type.secondary",
                          order=dict(_term='asc'))))),
            file_type=dict(terms=dict(
                field='distribution.formats',
                min_doc_count=0,
                order=dict(_term='asc'))),
            year=dict(terms=dict(
                field='date_created',
                min_doc_count=0,
                order=dict(_term='desc'))),
            keywords=dict(terms=dict(
                field='keywords',
                min_doc_count=0,
                order=dict(_term='asc'))),
            collision_type=dict(terms=dict(
                field='collision_information.type',
                min_doc_count=0,
                order=dict(_term='asc'))),
            collision_energy=dict(terms=dict(
                field='collision_information.energy',
                min_doc_count=0,
                order=dict(_term='asc'))),
            topic_category=dict(terms=dict(
                field='topic.category',
                min_doc_count=0,
                order=dict(_term='asc'))),
            run=dict(terms=dict(
                field='production_publication_distribution_manufacture_and_'
                      'copyright_notice.'
                      'date_of_production_publication_distribution_'
                      'manufacture_or_copyright_notice',
                min_doc_count=0,
                order=dict(_term='asc')
            )),
        ),
        'filters': dict(
            experiment=terms_filter('experiment'),
            type=terms_filter('type.primary'),
            subtype=terms_filter('type.secondary'),
            year=terms_filter('date_created'),
            tags=terms_filter('tags'),
            keywords=terms_filter('keywords'),
            collision_type=terms_filter('collision_information.type'),
            collision_energy=terms_filter('collision_information.energy'),
            topic_category=terms_filter('topic.category'),
            file_type=terms_filter('distribution.formats'),
            collections=terms_filter('collections'),
            run=terms_filter(
                'production_publication_distribution_manufacture_and_'
                'copyright_notice.'
                'date_of_production_publication_distribution_'
                'manufacture_or_copyright_notice'
            ),
        ),
        'post_filters': dict(
            experiment_post=terms_filter('experiment'),
            type_post=terms_filter('type.primary'),
            subtype_post=terms_filter('type.secondary'),
            year_post=terms_filter('date_created'),
            tags_post=terms_filter('tags'),
            keywords_post=terms_filter('keywords'),
            collision_type_post=terms_filter('collision_information.type'),
            collision_energy_post=terms_filter('collision_information.energy'),
            topic_category_post=terms_filter('topic.category'),
            file_type_post=terms_filter('distribution.formats'),
            run_post=terms_filter(
                'production_publication_distribution_manufacture_and_'
                'copyright_notice.'
                'date_of_production_publication_distribution_'
                'manufacture_or_copyright_notice'
            ),
        )
    },

}
"""Facets per index for the default facets factory."""

# Files
# ======
#: Permission factory to control the files access from the REST interface.
FILES_REST_PERMISSION_FACTORY = allow_all

# Search
# ======
#: Default API endpoint for search UI.
SEARCH_UI_SEARCH_API = "/api/records/"
#: Default template for search UI.
# SEARCH_UI_BASE_TEMPLATE = 'cernopendata/page.html'
#: Default template for search UI.
SEARCH_UI_SEARCH_TEMPLATE = 'cernopendata/search.html'
SEARCH_UI_JSTEMPLATE_FACETS = 'templates/cernopendata_search_ui/facets.html'
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
