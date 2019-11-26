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
    'node_modules/angular-ui-bootstrap/dist/ui-bootstrap-tpls.js',
    output='gen/cernopendata.theme.%(version)s.js',
    npm={
        'angular': '~1.4.9',
        'jquery': '~1.9.1',
        'popper.js': '~1.11.0',
        'bootstrap': '~4.0.0-beta',
        'angular-ui-bootstrap': '~2.2.0',
    },
)

css = NpmBundle(
    Bundle(
        'node_modules/bootstrap/dist/css/bootstrap.min.css',
        'node_modules/angular-loading-bar/build/loading-bar.css',
        filters='cleancssurl',
    ),
    Bundle(
        'scss/styles.scss',
        filters='node-scss, cleancssurl',
    ),
    depends=('scss/*.scss',),
    output='gen/cernopendata.%(version)s.css',
    npm={
        'angular-loading-bar': '~0.9.0',
        'bootstrap-sass': '~3.3.5',
        'open-iconic': '~1.1.1',
        'typeahead.js-bootstrap-css': '~1.2.1',
    }
)

front_js = NpmBundle(
    'node_modules/fullpage.js/dist/jquery.fullpage.js',
    output='gen/cernopendata.front.%(version)s.js',
    npm={
        'fullpage.js': '~2.9.5',
    },
)

search_js = NpmBundle(
    'node_modules/angular-sanitize/angular-sanitize.js',
    'node_modules/angular-loading-bar/build/loading-bar.js',
    'node_modules/invenio-search-js/dist/invenio-search-js.js',
    'js/components/resultsBrief.js',
    'js/controllers/facetCtrl.js',
    output='gen/codp_search.%(version)s.js',
    npm={
        'angular': '~1.4.10',
        'angular-loading-bar': '~0.9.0',
        'angular-sanitize': '~1.4.14',
        'invenio-search-js': '^1.3.1',
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
    'node_modules/demobbed-viewer/js/lib/d3.min.js',
    'node_modules/demobbed-viewer/js/lib/jquery.min.js',
    'node_modules/demobbed-viewer/js/lib/bootstrap.min.js',
    'node_modules/demobbed-viewer/js/lib/three.min.js',
    'node_modules/demobbed-viewer/js/lib/three3DExtras.min.js',
    'node_modules/demobbed-viewer/js/lib/TrackballControls.js',
    'node_modules/demobbed-viewer/js/DetCfg-def.js',
    'node_modules/demobbed-viewer/js/Utils-def.js',
    'node_modules/demobbed-viewer/js/Hits-defs.js',
    'node_modules/demobbed-viewer/js/Vertex-def.js',
    'node_modules/demobbed-viewer/js/TrackECC-def.js',
    'node_modules/demobbed-viewer/js/Event-def.js',
    'node_modules/demobbed-viewer/js/loadUserSpecifiedEvent.js',
    'node_modules/demobbed-viewer/js/changeEventSample.js',
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
        "demobbed-viewer-dev-js":
            "git+https://git@github.com/cernopendata/demobbed-viewer.git"
    },
)

opera_css = NpmBundle(
    'node_modules/demobbed-viewer/css/demobbed.css',
    filters='node-scss, cleancss',
    output='gen/cernopendata.opera.%(version)s.css',
    npm={
        "demobbed-viewer-dev-css":
            "git+https://git@github.com/cernopendata/demobbed-viewer.git"
    }
)

ispy_js = NpmBundle(
    # "node_modules/ispy-webgl/js/lib/jquery-1.11.1.min.js",
    "node_modules/ispy-webgl/js/lib/jquery.scrollintoview.min.js",
    "node_modules/ispy-webgl/js/lib/stupidtable.min.js",
    # 'node_modules/bootstrap/dist/js/bootstrap.js',
    # "node_modules/ispy-webgl/js/lib/bootstrap.min.js",
    "node_modules/ispy-webgl/js/lib/stats.min.js",
    "node_modules/ispy-webgl/js/lib/three.min.js",
    "node_modules/ispy-webgl/js/lib/tween.min.js",
    "node_modules/ispy-webgl/js/lib/CombinedCamera.js",
    "node_modules/ispy-webgl/js/lib/TrackballControls.js",
    "node_modules/ispy-webgl/js/lib/Projector.js",
    "node_modules/ispy-webgl/js/lib/CanvasRenderer.js",
    "node_modules/ispy-webgl/js/lib/SVGRenderer.js",
    "node_modules/ispy-webgl/js/lib/MTLLoader.js",
    "node_modules/ispy-webgl/js/lib/OBJLoader.js",
    "node_modules/ispy-webgl/js/lib/OBJExporter.js",
    "node_modules/ispy-webgl/js/lib/STLExporter.js",
    "node_modules/ispy-webgl/js/lib/GLTFExporter.js",
    "node_modules/ispy-webgl/js/lib/jszip.min.js",
    "node_modules/ispy-webgl/js/lib/DeviceOrientationControls.js",
    "node_modules/ispy-webgl/js/lib/StereoEffect.js",
    "node_modules/ispy-webgl/js/lib/StereoCamera.js",
    "node_modules/ispy-webgl/js/config.js",
    "node_modules/ispy-webgl/js/setup.js",
    "node_modules/ispy-webgl/js/animate.js",
    "node_modules/ispy-webgl/js/files-load.js",
    "node_modules/ispy-webgl/js/objects-draw.js",
    "node_modules/ispy-webgl/js/objects-add.js",
    "node_modules/ispy-webgl/js/objects-config.js",
    # <!-- These geometries are loaded regardless of the renderer used -->
    "node_modules/ispy-webgl/geometry/dt.js",
    "node_modules/ispy-webgl/geometry/csc.js",
    "node_modules/ispy-webgl/geometry/rpc.js",
    # <!-- Don't load this anymore as we don't use the models for WebGL
    # "node_modules/ispy-webgl/geometry/ecal.js",
    "node_modules/ispy-webgl/js/controls.js",
    "node_modules/ispy-webgl/js/tree-view.js",
    "node_modules/ispy-webgl/js/display.js",
    "node_modules/ispy-webgl/js/ispy.js",
    output='gen/cernopendata.ispy.%(version)s.js',
    npm={
        "ispy-webgl": "0.9.8-COD3.11"
    },
)

ispy_css = NpmBundle(
    "node_modules/ispy-webgl/css/font-awesome.min.css",
    "node_modules/ispy-webgl/css/ispy.css",
    filters='node-scss, cleancss',
    output='gen/cernopendata.ispy.%(version)s.css',
    npm={
        "ispy-webgl": "0.9.8-COD3.11"
    }
)


codemirror_js = NpmBundle(
    'node_modules/codemirror/lib/codemirror.js',
    'node_modules/codemirror/mode/scheme/scheme.js',
    'node_modules/codemirror/mode/javascript/javascript.js',
    'node_modules/codemirror/mode/xml/xml.js',
    'node_modules/angular-ui-codemirror/src/ui-codemirror.js',
    'node_modules/angular-clipboard/angular-clipboard.js',
    output='gen/cernopendata.codemirror.%(version)s.js',
    npm={
        "angular-ui-codemirror": "0.3.0",
        "codemirror": "*",
        "angular-clipboard": "1.6.2",
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
