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

"""JS/CSS bundles for theme."""

from flask_assets import Bundle
from invenio_assets import NpmBundle



codemirror_js = NpmBundle(
    'node_modules/codemirror/lib/codemirror.js',
    'node_modules/codemirror/mode/scheme/scheme.js',
    'node_modules/codemirror/mode/javascript/javascript.js',
    'node_modules/codemirror/mode/xml/xml.js',
    # 'node_modules/angular-ui-codemirror/src/ui-codemirror.js',
    # 'node_modules/angular-clipboard/angular-clipboard.js',
    output='gen/cernopendata.codemirror.%(version)s.js',
    npm={
        # "angular-ui-codemirror": "0.3.0",
        "codemirror": "*",
        # "angular-clipboard": "1.6.2",
    },
)

codemirror_css = NpmBundle(
    Bundle(
        'node_modules/codemirror/lib/codemirror.css',
        filters='cleancssurl',
    ),
    depends=('scss/*.scss',),
    output='gen/cernopendata.codemirror.%(version)s.css',
    npm={
    }
)
