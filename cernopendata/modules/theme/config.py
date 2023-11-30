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

"""Default configuration for CERN Open Data theme."""


def _(x):
    """Identity function for string extraction."""
    return x


# Default language and timezone
BABEL_DEFAULT_LANGUAGE = "en"
BABEL_DEFAULT_TIMEZONE = "Europe/Zurich"
I18N_LANGUAGES = [
    ("en", _("English")),
]

BASE_TEMPLATE = "cernopendata_theme/page.html"
HEADER_TEMPLATE = "cernopendata_theme/header.html"
COVER_TEMPLATE = "invenio_theme/page_cover.html"
SETTINGS_TEMPLATE = "invenio_theme/settings/content.html"

# Theme
THEME_SITENAME = _("CERN Open Data Portal")
THEME_LOGO = "img/cernopendata.svg"
