# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017, 2018, 2020, 2022 CERN.
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

import os

from invenio_records_files.api import _Record
from invenio_records_rest.config import RECORDS_REST_ENDPOINTS
from invenio_records_rest.facets import terms_filter
from invenio_records_rest.utils import allow_all

from cernopendata.modules.pages.config import *
from cernopendata.modules.records.search.query import cernopendata_range_filter
from cernopendata.modules.search_ui.helpers import \
    CODSearchAppInvenioRestConfigHelper
from cernopendata.modules.theme.config import *

# Debug
DEBUG = os.environ.get(
    'DEBUG',
    False
)
TEMPLATES_AUTO_RELOAD = DEBUG

# Mail debug
MAIL_DEBUG = 0

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

# Security
# ========
#: Flask-Talisman secure headers
APP_DEFAULT_SECURE_HEADERS = {
    'force_https': False,
    'force_https_permanent': False,
    'force_file_save': False,
    'frame_options': 'sameorigin',
    'frame_options_allow_from': None,
    'strict_transport_security': True,
    'strict_transport_security_preload': False,
    'strict_transport_security_max_age': 31556926,  # One year in seconds
    'strict_transport_security_include_subdomains': True,
    'content_security_policy': {
        'default-src': ["'self'"],
        'object-src': ["'none'"],
        'script-src': [
            "'self'",
            "'unsafe-eval'",
            "'unsafe-inline'",
            "https://cdnjs.cloudflare.com",
        ],
        'font-src': [
            "'self'",
            "data:",
            "https://cdnjs.cloudflare.com",
        ],
    },
    'content_security_policy_report_uri': None,
    'content_security_policy_report_only': False,
    'session_cookie_secure': True,
    'session_cookie_http_only': True
}

SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SAMESITE = "Lax"

# Assets
# ======
#: Default application theme.
APP_THEME = ['semantic-ui']

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
    'search_serializers': {
        'application/json': ('cernopendata.modules.records.serializers'
                             ':json_v1_search'),
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
            fields=['recid'],
            title='Most recent',
            default_order='desc',
            order=1,
        ),
        'title': dict(fields=['title.exact'],
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

# FIXME: KeyError: 'query'
# RECORDS_REST_DEFAULT_SORT = {
#     'records-glossary-term-v1.0.0': {
#         'noquery': 'anchor'
#     }
# }

# TODO: based on invenio-records-rest default config
RECORDS_REST_DEFAULT_SORT = dict(
    _all=dict(
        query='bestmatch',
        noquery='mostrecent',
    )
)

RECORDS_REST_FACETS = {
    '_all': {
        'aggs': dict(
            type=dict(terms=dict(
                field='type.primary.keyword',
                order=dict(_key='asc')),
                aggs=dict(subtype=dict(terms=dict(
                          field="type.secondary.keyword",
                          order=dict(_key='asc'))))),
            experiment=dict(terms=dict(
                field='experiment.keyword',
                order=dict(_key='asc'))),
            year=dict(terms=dict(
                field='date_created.keyword',
                order=dict(_key='asc'))),
            file_type=dict(terms=dict(
                field='distribution.formats.keyword',
                size=50,
                order=dict(_key='asc'))),
            collision_type=dict(terms=dict(
                field='collision_information.type.keyword',
                order=dict(_key='asc'))),
            collision_energy=dict(terms=dict(
                field='collision_information.energy.keyword',
                order=dict(_key='asc'))),
            category=dict(terms=dict(
                field='categories.primary.keyword',
                order=dict(_key='asc')),
                aggs=dict(subcategory=dict(terms=dict(
                          field="categories.secondary.keyword",
                          order=dict(_key='asc'))))),
            magnet_polarity=dict(terms=dict(
                field='magnet_polarity.keyword',
                order=dict(_term='asc'))),
            stripping_stream=dict(terms=dict(
                field='stripping.stream.keyword',
                order=dict(_term='asc'))),
            stripping_version=dict(terms=dict(
                field='stripping.version.keyword',
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
            },
            signature=dict(terms=dict(
                field='signature.keyword',
                order=dict(_key='asc'))),
            keywords=dict(terms=dict(
                field='keywords.keyword',
                order=dict(_key='asc'))),
        ),
        'post_filters': dict(
            type=terms_filter('type.primary.keyword'),
            subtype=terms_filter('type.secondary.keyword'),
            experiment=terms_filter('experiment.keyword'),
            year=terms_filter('date_created.keyword'),
            file_type=terms_filter('distribution.formats.keyword'),
            tags=terms_filter('tags.keyword'),
            collision_type=terms_filter('collision_information.type.keyword'),
            collision_energy=terms_filter('collision_information.energy'
                                          '.keyword'),
            category=terms_filter('categories.primary.keyword'),
            subcategory=terms_filter('categories.secondary.keyword'),
            magnet_polarity=terms_filter('magnet_polarity.keyword'),
            stripping_stream=terms_filter('stripping.stream.keyword'),
            stripping_version=terms_filter('stripping.version.keyword'),
            event_number=cernopendata_range_filter(
                            'distribution.number_events'),
            collections=terms_filter('collections.keyword'),
            signature=terms_filter('signature.keyword'),
            keywords=terms_filter('keywords.keyword'),
        )
    }
}

"""Facets per index for the default facets factory."""

# Generated by scripts/get_facet_hierarchy.py
FACET_HIERARCHY = {
    "category": {
        "B physics and Quarkonia": {"subcategory": set()},
        "Exotica": {"subcategory": {"Miscellaneous", "Gravitons"}},
        "Higgs Physics": {
            "subcategory": {
                "Beyond Standard Model",
                "Standard Model"
            }
        },
        "Physics Modelling": {"subcategory": set()},
        "Standard Model Physics": {
            "subcategory": {
                "Drell-Yan",
                "ElectroWeak",
                "Forward and Small-x " "QCD Physics",
                "Minimum Bias",
                "QCD",
                "Top physics",
            }
        },
        "Supersymmetry": {"subcategory": set()},
    },
    "collision_energy": {
        "0.9TeV": {},
        "0TeV": {},
        "13TeV": {},
        "2.76TeV": {},
        "7TeV": {},
        "8TeV": {},
    },
    "collision_type": {"Interfill": {}, "PbPb": {}, "pp": {}},
    "event_number": {
        "0--999": {},
        "1000--9999": {},
        "10000--99999": {},
        "100000--999999": {},
        "1000000--9999999": {},
        "10000000--": {},
    },
    "experiment": {
        "ALICE": {},
        "ATLAS": {},
        "CMS": {},
        "LHCb": {},
        "OPERA": {}
    },
    "file_type": {
        "C": {},
        "aod": {},
        "aodsim": {},
        "cc": {},
        "csv": {},
        "docx": {},
        "fevtdebughlt": {},
        "gen-sim": {},
        "gen-sim-digi-raw": {},
        "gen-sim-reco": {},
        "gz": {},
        "h5": {},
        "html": {},
        "ig": {},
        "ipynb": {},
        "jpg": {},
        "json": {},
        "m4v": {},
        "miniaodsim": {},
        "nanoaod": {},
        "ova": {},
        "pdf": {},
        "png": {},
        "py": {},
        "raw": {},
        "reco": {},
        "root": {},
        "tar": {},
        "tar.gz": {},
        "txt": {},
        "xls": {},
        "xml": {},
        "zip": {},
    },
    "keywords": {
        "datascience": {},
        "education": {},
        "external resource": {},
        "heavy-ion physics": {},
        "masterclass": {},
        "teaching": {},
    },
    "signature": {
        "H": {},
        "Jpsi": {},
        "W": {},
        "Y": {},
        "Z": {},
        "electron": {},
        "missing transverse energy": {},
        "muon": {},
        "photon": {},
    },
    "type": {
        "Dataset": {"subtype": {"Simulated", "Derived", "Collision"}},
        "Documentation": {
            "subtype": {
                "About",
                "Activities",
                "Authors",
                "Guide",
                "Help",
                "Policy",
                "Report",
            }
        },
        "Environment": {"subtype": {"VM", "Condition", "Validation"}},
        "Glossary": {"subtype": set()},
        "News": {"subtype": set()},
        "Software": {
            "subtype": {
                "Analysis",
                "Framework",
                "Tool",
                "Validation",
                "Workflow"
            }
        },
        "Supplementaries": {
            "subtype": {
                "Configuration",
                "Configuration HLT",
                "Configuration LHE",
                "Configuration RECO",
                "Configuration SIM",
                "Luminosity",
                "Trigger",
            }
        },
    },
    "year": {
        "2008": {},
        "2009": {},
        "2010": {},
        "2011": {},
        "2012": {},
        "2016": {},
        "2018": {},
        "2019": {},
    },
}

"""Hierarchy of facets containing subfacets."""

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
#: Default Elasticsearch document type.
SEARCH_DOC_TYPE_DEFAULT = None
#: Do not map any keywords.
SEARCH_ELASTIC_KEYWORD_MAPPING = {}

#: Configure the search page template.
SEARCH_UI_SEARCH_TEMPLATE = 'cernopendata_search_ui/search.html'
SEARCH_UI_SEARCH_INDEX = '_all'
#: Override the React-SearchKit config generator to support range aggs.
SEARCH_UI_SEARCH_CONFIG_GEN = {
    'invenio_records_rest': CODSearchAppInvenioRestConfigHelper,
}

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

ANNOUNCEMENT_BANNER_MESSAGE = os.getenv('ANNOUNCEMENT_BANNER_MESSAGE', '')
"""Message to display in all pages as a banner (HTML allowed)."""
