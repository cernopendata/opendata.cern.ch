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

from __future__ import absolute_import, print_function

from flask_assets import Bundle
from invenio_assets import NpmBundle

js = NpmBundle(
    'node_modules/angular/angular.js',
    'node_modules/jquery/jquery.js',
    'node_modules/popper.js/dist/umd/popper.js',
    'node_modules/bootstrap/dist/js/bootstrap.js',
    output='gen/cernopendata.theme.%(version)s.js',
    npm={
        'angular': '~1.4.9',
        'jquery': '~1.9.1',
        'popper.js': '~1.11.0',
        'bootstrap': '~4.0.0-beta',
    },
)

css = NpmBundle(
    Bundle(
        'scss/styles.scss',
        filters='node-scss, cleancssurl',
    ),
    Bundle(
        'node_modules/angular-loading-bar/build/loading-bar.css',
        'node_modules/typeahead.js-bootstrap-css/typeaheadjs.css',
        # 'node_modules/bootstrap-switch/dist/css/bootstrap3'
        # '/bootstrap-switch.css',
        filters='cleancssurl',
    ),
    depends=('scss/*.scss',),
    output='gen/cernopendata.%(version)s.css',
    npm={
        'angular-loading-bar': '~0.9.0',
        'bootstrap-sass': '~3.3.5',
        # 'bootstrap-switch': '~3.0.2',
        'font-awesome': '~4.4.0',
        'typeahead.js-bootstrap-css': '~1.2.1',
    }
)
"""Default CSS bundle."""

search_js = NpmBundle(
    'node_modules/angular-sanitize/angular-sanitize.js',
    'js/components/resultsBrief.js',
    output='gen/codp_search.%(version)s.js',
    npm={
        'angular': '~1.4.10',
        'angular-sanitize': '~1.4.14'
    },
)

visualise_js = NpmBundle(
    'node_modules/d3/d3.min.js',
    'node_modules/flot/jquery.flot.js',
    'node_modules/flot/jquery.flot.selection.js',
    'js/visualise/visualise_histograms.js',
    output='gen/cernopendata.%(version)s.js',
    npm={
        'd3': '^3.3.13',
        'flot': '~0.8.0-alpha',
    },
)

visualise_css = NpmBundle(
    'scss/visualise.scss',
    filters='node-scss, cleancss',
    output='gen/cernopendata.vis.%(version)s.css',
    npm={
        "bootstrap-sass": "~3.3.5",
    }
)

glossary_js = NpmBundle(
    'js/glossary/jquery.zglossary.js',
    output='gen/glossary.%(version)s.js',
    npm={},
)

glossary_css = NpmBundle(
    'js/glossary/jquery.zglossary.css',
    filters='node-scss, cleancss',
    output='gen/cernopendata.glossary.%(version)s.css',
    npm={
        "bootstrap-sass": "~3.3.5",
    }
)

opera_js = NpmBundle(
    'node_modules/demobbed-viewer/js/lib/d3.js',
    'node_modules/demobbed-viewer/js/lib/jquery.js',
    'node_modules/demobbed-viewer/js/lib/three.js',
    'node_modules/demobbed-viewer/js/lib/three3DExtras.min.js',
    'node_modules/demobbed-viewer/js/DetCfg-def.js',
    'node_modules/demobbed-viewer/js/Utils-def.js',
    'node_modules/demobbed-viewer/js/Hits-defs.js',
    'node_modules/demobbed-viewer/js/Vertex-def.js',
    'node_modules/demobbed-viewer/js/TrackECC-def.js',
    'node_modules/demobbed-viewer/js/Event-def.js',
    'node_modules/demobbed-viewer/js/loadEvent.js',
    'node_modules/demobbed-viewer/js/DetElems-defs.js',
    'node_modules/demobbed-viewer/js/MgrGeomED-def.js',
    'node_modules/demobbed-viewer/js/MgrDrawED-def.js',
    'node_modules/demobbed-viewer/js/MgrDrawECC-def.js',
    'node_modules/demobbed-viewer/js/Demobbed-def.js',
    'node_modules/demobbed-viewer/js/init.js',
    'node_modules/demobbed-viewer/js/Demobbed-fills.js',
    'node_modules/demobbed-viewer/js/MgrGeomED-fills.js',
    'node_modules/demobbed-viewer/js/MgrGeomED-funcAdd.js',
    'node_modules/demobbed-viewer/js/MgrDrawED-funcAdd.js',
    'node_modules/demobbed-viewer/js/MgrDrawECC-funcAdd.js',
    output='gen/cernopendata.opera.%(version)s.js',
    npm={
        "demobbed-viewer": "~1.0.2"
    },
)

opera_css = NpmBundle(
    'node_modules/demobbed-viewer/css/demobbed.css',
    filters='node-scss, cleancss',
    output='gen/cernopendata.opera.%(version)s.css',
    npm={
        "demobbed-viewer": "~1.0.2"
    }
)
