# -*- coding: utf-8 -*-

"""cernopendata base Invenio configuration."""

from __future__ import absolute_import, print_function


# Identity function for string extraction
def _(x):
    return x

# Default language and timezone
BABEL_DEFAULT_LANGUAGE = 'en'
BABEL_DEFAULT_TIMEZONE = 'Europe/Zurich'
I18N_LANGUAGES = [
    ('en', _('English')),
]

BASE_TEMPLATE = 'cernopendata/page.html'
COVER_TEMPLATE = 'invenio_theme/page_cover.html'
SETTINGS_TEMPLATE = 'invenio_theme/settings/content.html'

# WARNING: Do not share the secret key - especially do not commit it to
# version control.
SECRET_KEY = 'yG7PxDUon2NM8rhsXXyzd2dl3O6ce9NatOXBOs4bK6Fq1a8uQ9fgozNyaCs0r6SxjxQUCPhhJI3uYtDkZJa3qnTR38eCbEybEjNpdtPeUfQErxUlszcJbCrv7MrwQRszCeFkkqPWbG9zl8JX8NdL0O8RQEtLXcw6XHuVlE6dgyuq22PoP4FlJbxHn46yvHI8wsQ5E2uuQBjJNye2KsKl58TYbrJrwq21Ljcqx8tMvPvaSv0CWrp3IFlYcAUGzK9x'

# Theme
THEME_SITENAME = _('CERN Open Data Portal')
THEME_LOGO = 'img/home/opendata_logo.svg'

# JSONSchemas
JSONSCHEMAS_HOST = 'http://opendata.cern.ch'

# Records
RECORDS_UI_DEFAULT_PERMISSION_FACTORY = None
RECORDS_UI_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        route='/record/<pid_value>',
        template='invenio_records_ui/detail.html',
        permission_factory_imp=None,
    ),
)

RECORDS_REST_ENDPOINTS = dict(
    recid=dict(
        pid_type='recid',
        pid_minter='recid',
        pid_fetcher='recid',
        search_index='_all',
        search_type=None,
        record_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_response'),
        },
        search_serializers={
            'application/json': ('invenio_records_rest.serializers'
                                 ':json_v1_search'),
        },
        list_route='/records/',
        item_route='/records/<pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
    ),
)

from invenio_records_rest.facets import terms_filter
RECORDS_REST_FACETS = dict(
    _all=dict(
        aggs=dict(
            collections=dict(terms=dict(field='collections.primary'))
        ),
        post_filters=dict(
            collections=terms_filter('collections.primary'),
        )
    )
)
"""Facets per index for the default facets factory."""

# Search
# ======
#: Default API endpoint for search UI.
SEARCH_UI_SEARCH_API = "/api/records/"
#: Default template for search UI.
SEARCH_UI_BASE_TEMPLATE = 'cernopendata/page.html'
#: Default template for search UI.
SEARCH_UI_SEARCH_TEMPLATE = "cernopendata/search.html"
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

# Open Data Portal
# ================
#: Information on homepage.
OPENDATA_EXPERIMENTS = [
    'CMS', 'ALICE', 'ATLAS', 'LHCb',
]

OPENDATA_EDUCATION = [
    ('CMS',
     'The CMS (Compact Muon Solenoid) experiment is one of two large '
     'general-purpose particle physics detectors built on the Large Hadron '
     'Collider (LHC) at CERN in Switzerland and France. The goal of CMS is to '
     'investigate a wide range of physics, including properties of the recently '
     'discovered Higgs boson as well as searches for extra dimensions and '
     'particles that could make up dark matter.',
     True),
    ('ALICE',
     '<a href="http://aliceinfo.cern.ch/Public/Welcome.html">'
     '<span class="external-link-l"></span>ALICE</a> '
     '(A Large Ion Collider Experiment) is a heavy-ion '
     '<a href="http://home.web.cern.ch/about/how-detector-works">'
     '<span class="external-link-l"></span>detector</a> designed to study '
     'the physics of strongly interacting matter at extreme energy densities, '
     'where a phase of matter called <a href="http://home.web.cern.ch'
     '/about/physics/heavy-ions-and-quark-gluon-plasma">'
     '<span class="external-link-l"></span>quark-gluon plasma</a> forms.<br/>'
     'The ALICE collaboration uses the 10,000-tonne ALICE detector - 26 m long, '
     '16 m high, and 16 m wide - to study quark-gluon plasma. The detector sits '
     'in a vast cavern 56 m below ground close to the village of '
     'Saint Genis-Pouilly in France, receiving beams from the LHC. '
     'More than 1000 scientists are part of the collaboration.',
     True),
    ('ATLAS',
     '',
     True),
    ('LHCb',
     '',
     True),
]

OPENDATA_RESEARCH = [
    ('CMS',
     'The CMS (Compact Muon Solenoid) experiment is one of two large '
     'general-purpose particle physics detectors built on the Large Hadron '
     'Collider (LHC) at CERN in Switzerland and France. The goal of CMS is to '
     'investigate a wide range of physics, including properties of the recently '
     'discovered Higgs boson as well as searches for extra dimensions and '
     'particles that could make up dark matter.',
     True),
    ('ALICE',
     '',
     False),
    ('ATLAS',
     '',
     False),
    ('LHCb',
     '',
     False),
]
