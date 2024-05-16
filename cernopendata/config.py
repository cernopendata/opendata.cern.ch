# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017, 2018, 2020, 2022, 2023 CERN.
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
import warnings

from flask import request
from invenio_records_files.api import _Record
from invenio_records_rest.config import RECORDS_REST_ENDPOINTS
from invenio_records_rest.facets import nested_filter, range_filter, terms_filter
from invenio_records_rest.utils import allow_all
from invenio_search.engine import dsl
from urllib3.exceptions import InsecureRequestWarning

from cernopendata.modules.pages.config import *
from cernopendata.modules.search_ui.helpers import CODSearchAppInvenioRestConfigHelper
from cernopendata.modules.theme.config import *

from .views import search_legacy

# Disable opensearch warning of connecting without checking certificates
warnings.filterwarnings(action="ignore", category=UserWarning, module=r".*urllib3")
warnings.filterwarnings(
    action="ignore", category=InsecureRequestWarning, module=r".*urllib3"
)

# Debug
DEBUG = os.environ.get("DEBUG", False)
TEMPLATES_AUTO_RELOAD = DEBUG

# Mail debug
MAIL_DEBUG = 0

# Piwik tracking code: set None to disabled it
THEME_PIWIK_ID = os.environ.get("PIWIK_ID", None)
ACCOUNTS_SESSION_ACTIVITY_ENABLED = None
SITE_URL = os.environ.get("CERNOPENDATA_SITE_URL", "opendata.cern.ch")

# Logging - Set up Sentry for Invenio-Logging
SENTRY_DSN = os.environ.get("SENTRY_DSN", None)

LOGGING_SENTRY_CELERY = os.environ.get("LOGGING_SENTRY_CELERY", False)

# Security
# ========
#: Flask-Talisman secure headers
APP_DEFAULT_SECURE_HEADERS = {
    "force_https": False,
    "force_https_permanent": False,
    "force_file_save": False,
    "frame_options": "sameorigin",
    "frame_options_allow_from": None,
    "strict_transport_security": True,
    "strict_transport_security_preload": False,
    "strict_transport_security_max_age": 31556926,  # One year in seconds
    "strict_transport_security_include_subdomains": True,
    "content_security_policy": {
        "default-src": ["'self'"],
        "object-src": ["'none'"],
        "script-src": [
            "'self'",
            "'unsafe-eval'",
            "'unsafe-inline'",
            "https://cdnjs.cloudflare.com",
        ],
        "font-src": [
            "'self'",
            "data:",
            "https://cdnjs.cloudflare.com",
        ],
        "img-src": [
            "'self'",
            "cms-results.web.cern.ch",
            "raw.githubusercontent.com",
            "www.github.com",
            "github.com",
            "cms-docdb.cern.ch",
            "mybinder.org",
            "cms-results.web.cern.ch",
            "cds.cern.ch",
        ],
    },
    "content_security_policy_report_uri": None,
    "content_security_policy_report_only": False,
    "session_cookie_secure": True,
    "session_cookie_http_only": True,
}

SESSION_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SAMESITE = "Lax"

# Assets
# ======
#: Default application theme.
APP_THEME = ["semantic-ui"]
ACCOUNTS_REGISTER_BLUEPRINT = False

# Static file
COLLECT_STORAGE = (
    "flask_collect.storage.link" if DEBUG else "flask_collect.storage.file"
)

# Cache
CACHE_TYPE = "redis"

# Celery
CELERY_ACCEPT_CONTENT = ["json", "msgpack", "yaml"]

# JSONSchemas
JSONSCHEMAS_ENDPOINT = "/schema"
JSONSCHEMAS_HOST = "opendata.cern.ch"
JSONSCHEMAS_URL_SCHEME = "http"

# HOST_URI
HOST_URI = "{}://{}".format(JSONSCHEMAS_URL_SCHEME, JSONSCHEMAS_HOST)

# OAI Server
OAISERVER_RECORD_INDEX = "records"
OAISERVER_ID_PREFIX = "oai:cernopendata:recid/"

# Records
# Add tuple as array type on record validation
# http://python-jsonschema.readthedocs.org/en/latest/validate/#validating-types
RECORDS_VALIDATION_TYPES = {
    "array": (list, tuple),
}

RECORDS_UI_EXPORT_FORMATS = dict(
    docid=dict(
        json=dict(
            title="JSON",
            serializer="cernopendata.modules.records.serializers.json",
        ),
        jsonld=dict(
            title="JSON-LD",
            serializer="cernopendata.modules.records.serializers." "schemaorg_jsonld",
        ),
    ),
    recid=dict(
        json=dict(
            title="JSON",
            serializer="cernopendata.modules.records.serializers.json",
        ),
        jsonld=dict(
            title="JSON-LD",
            serializer="cernopendata.modules.records.serializers." "schemaorg_jsonld",
        ),
    ),
)

RECORDS_UI_ENDPOINTS = dict(
    recid=dict(
        pid_type="recid",
        route="/record/<pid_value>",
        permission_factory_imp=None,
        record_class="invenio_records_files.api:Record",
        view_imp="cernopendata.modules.records.utils:record_metadata_view",
    ),
    recid_files=dict(
        pid_type="recid",
        route="/record/<pid_value>/files/<path:filename>",
        view_imp="cernopendata.modules.records.utils:file_download_ui",
        record_class="invenio_records_files.api:Record",
    ),
    recid_files_assets=dict(
        pid_type="recid",
        route="/record/<pid_value>/files/assets/<path:filepath>",
        view_imp="cernopendata.modules.records.utils:eos_file_download_ui",
        record_class="invenio_records_files.api:Record",
    ),
    recid_files_page=dict(
        pid_type="recid",
        route="/record/<pid_value>/filepage/<int:page>",
        view_imp="cernopendata.modules.records.utils:record_file_page",
        record_class="invenio_records_files.api:Record",
    ),
    recid_export=dict(
        pid_type="recid",
        route="/record/<pid_value>/export/<format>",
        view_imp="cernopendata.modules.records.utils:export_json_view",
        record_class="invenio_records_files.api:Record",
    ),
    termid=dict(
        pid_type="termid",
        route="/glossary/<pid_value>",
        permission_factory_imp=None,
        view_imp="cernopendata.modules.records.utils:term_metadata_view",
    ),
    docid=dict(
        pid_type="docid",
        route="/docs/<pid_value>",
        permission_factory_imp=None,
        record_class="invenio_records_files.api:Record",
        view_imp="cernopendata.modules.records.utils:doc_metadata_view",
    ),
    docid_export=dict(
        pid_type="docid",
        route="/docs/<pid_value>/export/<format>",
        view_imp="invenio_records_ui.views.export",
        template="cernopendata_records_ui/default_export.html",
    ),
)

RECORDS_REST_ENDPOINTS["recid"]["search_index"] = "records"


def _query_parser_and(qstr=None):
    """Parser that uses the Q() with AND from search engine dsl."""
    if qstr:
        _query = dsl.Q(
            "query_string",
            query=qstr.replace("/", "\\/"),
            default_operator="AND",
            fields=["title.tokens^2", "*"],
        )
    else:
        _query = dsl.Q()
    if (
        request.values.get("ondemand") != "true"
        and request.values.get("ondemand") != "ondemand"
    ):
        _query = _query & ~dsl.Q("match", **{"distribution.availability": "ondemand"})
    return _query


RECORDS_REST_ENDPOINTS["recid"].update(
    {
        "search_query_parser": _query_parser_and,
        "pid_minter": "cernopendata_recid_minter",
        "pid_fetcher": "cernopendata_recid_fetcher",
        "record_class": _Record,
        "links_factory_imp": "cernopendata.modules.records.links:links_factory",
        "record_serializers": {
            "application/json": (
                "invenio_records_rest.serializers" ":json_v1_response"
            ),
            "application/ld+json": (
                "cernopendata.modules.records.serializers" ":schemaorg_jsonld_response"
            ),
        },
        "search_serializers": {
            "application/json": (
                "cernopendata.modules.records.serializers" ":json_v1_search"
            ),
        },
    }
)

RECORDS_REST_ENDPOINTS["termid"] = {
    "pid_type": "termid",
    "pid_minter": "cernopendata_termid_minter",
    "pid_fetcher": "cernopendata_termid_fetcher",
    "record_class": _Record,
    "links_factory_imp": "cernopendata.modules.records.links:links_factory",
    "default_media_type": "application/json",
    "max_result_window": 10000,
    "item_route": "/glossary/<pid(termid):pid_value>",
    "list_route": "/glossary",
    "record_serializers": {
        "application/json": ("invenio_records_rest.serializers" ":json_v1_response"),
        "application/ld+json": (
            "cernopendata.modules.records.serializers" ":schemaorg_jsonld_response"
        ),
    },
    "search_index": "records-glossary-term-v1.0.0",
    "search_serializers": {
        "application/json": ("invenio_records_rest.serializers" ":json_v1_search"),
    },
}

RECORDS_REST_ENDPOINTS["docid"] = {
    "pid_type": "docid",
    "pid_minter": "cernopendata_docid_minter",
    "pid_fetcher": "cernopendata_docid_fetcher",
    "record_class": _Record,
    "links_factory_imp": "cernopendata.modules.records.links:links_factory",
    "default_media_type": "application/json",
    "max_result_window": 10000,
    "item_route": "/docs/<pid(docid):pid_value>",
    "list_route": "/docs",
    "record_serializers": {
        "application/json": ("invenio_records_rest.serializers" ":json_v1_response"),
        "application/ld+json": (
            "cernopendata.modules.records.serializers" ":schemaorg_jsonld_response"
        ),
    },
    "search_index": "records-docs-v1.0.0",
    "search_serializers": {
        "application/json": ("invenio_records_rest.serializers" ":json_v1_search"),
    },
}

RECORDS_REST_SORT_OPTIONS = {
    "records": {
        "bestmatch": dict(
            fields=["-_score"],
            title="Best match",
            default_order="asc",
            order=1,
        ),
        "mostrecent": dict(
            fields=["date_published", "recid"],
            title="Most recent",
            default_order="desc",
            order=1,
        ),
        "title": dict(
            fields=["title"], title="Title A-Z", default_order="asc", order=1
        ),
        "title_desc": dict(
            fields=["title"], title="Title Z-A", default_order="desc", order=1
        ),
    }
}

# TODO: based on invenio-records-rest default config
RECORDS_REST_DEFAULT_SORT = dict(
    records=dict(
        query="bestmatch",
        noquery="mostrecent",
    )
)
# This parameter ensures that the numbers that appear in the facets get updated after the user
# selects some filters. Note that the filters apply to other areas. For example, imagine that the user selects
# in the area of `experiment` the value 'A'. All the other `experiments` will still appear, and, for the area of
# `year` for instance, it will be filtered to show only where `experiment==A`
RECORDS_REST_FACETS_POST_FILTERS_PROPAGATE = True

RECORDS_REST_FACETS = {
    "records": {
        "aggs": dict(
            type=dict(
                terms=dict(field="type.primary", order=dict(_key="asc")),
                aggs=dict(
                    subtype=dict(
                        terms=dict(field="type.secondary", order=dict(_key="asc"))
                    )
                ),
            ),
            experiment=dict(terms=dict(field="experiment", order=dict(_key="asc"))),
            year=dict(
                terms=dict(field="date_created", size=70, order=dict(_key="asc"))
            ),
            file_type=dict(
                terms=dict(
                    field="distribution.formats", size=50, order=dict(_key="asc")
                )
            ),
            collision_type=dict(
                terms=dict(field="collision_information.type", order=dict(_key="asc"))
            ),
            collision_energy=dict(
                terms=dict(field="collision_information.energy", order=dict(_key="asc"))
            ),
            category=dict(
                terms=dict(field="categories.primary", order=dict(_key="asc")),
                aggs=dict(
                    subcategory=dict(
                        terms=dict(field="categories.secondary", order=dict(_key="asc"))
                    )
                ),
            ),
            magnet_polarity=dict(
                terms=dict(field="magnet_polarity", order=dict(_term="asc"))
            ),
            stripping_stream=dict(
                terms=dict(field="stripping.stream", order=dict(_term="asc"))
            ),
            stripping_version=dict(
                terms=dict(field="stripping.version", order=dict(_term="asc"))
            ),
            number_of_events={
                "range": {
                    "field": "distribution.number_events",
                    "ranges": [
                        {"key": "0 -- 999 ", "from": 0, "to": 1000},
                        {"key": "1000 -- 9999", "from": 1000, "to": 10000},
                        {"key": "10000 -- 99999", "from": 10000, "to": 100000},
                        {"key": "100000 -- 999999", "from": 100000, "to": 1000000},
                        {"key": "1000000 -- 9999999", "from": 1000000, "to": 10000000},
                        {"key": " 10000000 --", "from": 10000000},
                    ],
                }
            },
            signature=dict(terms=dict(field="signature", order=dict(_key="asc"))),
            keywords=dict(terms=dict(field="keywords", order=dict(_key="asc"))),
        ),
        "post_filters": dict(
            type=nested_filter("type.primary", "type.secondary"),
            experiment=terms_filter("experiment"),
            year=terms_filter("date_created"),
            file_type=terms_filter("distribution.formats"),
            tags=terms_filter("tags"),
            collision_type=terms_filter("collision_information.type"),
            collision_energy=terms_filter("collision_information.energy"),
            category=nested_filter("categories.primary", "categories.secondary"),
            magnet_polarity=terms_filter("magnet_polarity"),
            stripping_stream=terms_filter("stripping.stream"),
            stripping_version=terms_filter("stripping.version"),
            number_of_events=range_filter("distribution.number_events"),
            collections=terms_filter("collections"),
            signature=terms_filter("signature"),
            keywords=terms_filter("keywords"),
        ),
    }
}

"""Facets per index for the default facets factory."""

# Files
# ======
#: Permission factory to control the files access from the REST interface.
FILES_REST_PERMISSION_FACTORY = allow_all
#: Allow URI's longer than 255 chars.
FILES_REST_FILE_URI_MAX_LEN = os.environ.get("FILES_REST_FILE_URI_MAX_LEN", 512)
#: Files max size threshold(bytes)
CERNOPENDATA_MAX_DOWNLOAD_SIZE = os.environ.get(
    "CERNOPENDATA_MAX_DOWNLOAD_SIZE", 200000000
)
#: Make download availalbe for Root files
CERNOPENDATA_DISABLE_DOWNLOADS = os.environ.get("CERNOPENDATA_DISABLE_DOWNLOADS", False)
# Search
# ======
#: Default OpenSearch document type.
SEARCH_DOC_TYPE_DEFAULT = None

# This one can be used to have multiple instances on the same cluster
# SEARCH_INDEX_PREFIX = "opendata-dev-"

#: Configure the search page template.
SEARCH_UI_SEARCH_TEMPLATE = "cernopendata_search_ui/search.html"
SEARCH_UI_SEARCH_INDEX = "records"
#: Override the React-SearchKit config generator to support range aggs.
SEARCH_UI_SEARCH_CONFIG_GEN = {
    "invenio_records_rest": CODSearchAppInvenioRestConfigHelper,
}


SEARCH_UI_SEARCH_VIEW = search_legacy
# OAI-PMH
# =======
#: Default OpenSearch index.
OAISERVER_RECORD_INDEX = "records"
#: OAI ID prefix.
OAISERVER_ID_PREFIX = "oai:opendata.cern.ch:recid/"

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "APP_SQLALCHEMY_DATABASE_URI", "postgresql+psycopg2://localhost/cernopendata"
)

# DataCite
# ========
#: DataCite API - URL endpoint.
PIDSTORE_DATACITE_URL = "https://mds.datacite.org"

#: DataCite API - Disable test mode (we however use the test prefix).
PIDSTORE_DATACITE_TESTMODE = os.environ.get("APP_PIDSTORE_DATACITE_TESTMODE", False)

#: DataCite API - Prefix for minting DOIs in (10.5072 is a test prefix).
PIDSTORE_DATACITE_DOI_PREFIX = os.environ.get(
    "APP_PIDSTORE_DATACITE_DOI_PREFIX", "10.5072"
)

#: DataCite MDS username.
PIDSTORE_DATACITE_USERNAME = os.environ.get(
    "APP_PIDSTORE_DATACITE_USERNAME", "CERN.OPENDATA"
)

#: DataCite MDS password.
PIDSTORE_DATACITE_PASSWORD = os.environ.get(
    "APP_PIDSTORE_DATACITE_PASSWORD", "CHANGE_ME"
)

#: Base URL for landing page
PIDSTORE_LANDING_BASE_URL = os.environ.get(
    "APP_PIDSTORE_LANDING_BASE_URL", "http://opendata.cern.ch/record"
)

ANNOUNCEMENT_BANNER_MESSAGE = os.getenv("ANNOUNCEMENT_BANNER_MESSAGE", "")
"""Message to display in all pages as a banner (HTML allowed)."""

# THIS ONE IS ONLY FOR THE DEVELOPMENT
RATELIMIT_PER_ENDPOINT = {"static": "600 per minute"}
