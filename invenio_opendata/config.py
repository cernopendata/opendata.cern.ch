# -*- coding: utf-8 -*-
#
## This file is part of CERN Open Data Portal.
## Copyright (C) 2014 CERN.
##
## CERN Open Data Portal is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## CERN Open Data Portal is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02D111-1307, USA.

from __future__ import unicode_literals
from invenio.base.config import PACKAGES as _PACKAGES

PACKAGES = [
    "invenio_opendata.base",
    "invenio_opendata.modules.*",
    "invenio_previewer_ispy"
] + _PACKAGES

PACKAGES_EXCLUDE = [
    "invenio.modules.annotations",
    "invenio.modules.communities",
    "invenio.modules.pages",
]

DEPOSIT_TYPES = [
#    'invenio_opendata.modules.deposit.workflows.article.article',
]

CFG_SITE_URL = 'http://opendata.cern.ch'
#CFG_SITE_SECURE_URL = 'https://opendata.cern.ch'
CFG_SITE_SECURE_URL = 'http://opendata.cern.ch'

CFG_SITE_NAME = 'CERN Open Data Portal'
CFG_SITE_LANGS = {'en'}
CFG_SITE_NAME_INTL = {}
CFG_SITE_NAME_INTL['en'] = 'CERN Open Data Portal'

CFG_WEBCOMMENT_ALLOW_REVIEWS = 0

CFG_WEBSEARCH_DISPLAY_NEAREST_TERMS = 0

try:
    from invenio_opendata.instance_config import *  # noqa
except ImportError:
    pass
