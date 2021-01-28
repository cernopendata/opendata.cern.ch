# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2020 CERN.
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

"""JS/CSS webpack bundles for theme."""

from invenio_assets.webpack import WebpackThemeBundle


theme = WebpackThemeBundle(
    __name__,
    'assets',
    default='semantic-ui',
    themes={
        'semantic-ui': dict(
            entry={
                'cernopendata_css': './scss/styles.scss',
                'cernopendata_js': './js/app.js'
            },
            dependencies={
                'open-iconic': '~1.1.1',
                'popper.js': '~1.11.0',
            },
            aliases={
                '../../theme.config$': 'less/cernopendata/theme.config',
            },
        ),
    }
)


glossary = WebpackThemeBundle(
    __name__,
    'assets',
    default='semantic-ui',
    themes={
        'semantic-ui': dict(
            entry={
                'glossary_js': './js/glossary/jquery.zglossary.js',
                'glossary_css': './js/glossary/jquery.zglossary.css',
            },
        )
    }
)

search_ui = WebpackThemeBundle(
    __name__,
    "assets",
    default="semantic-ui",
    themes={
        "semantic-ui": dict(
            entry={
                "cernopendata_search_app": "./js/search/app.js",
            },
            aliases={
                '@js/cernopendata_search_ui': 'js/search',
            }
        ),
    },
)
