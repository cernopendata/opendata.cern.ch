"""JS/CSS bundles for theme."""

from __future__ import absolute_import, print_function

from flask_assets import Bundle
from invenio_assets import NpmBundle

css = NpmBundle(
    Bundle(
        'scss/styles.scss',
        filters='node-scss, cleancss',
    ),
    Bundle(
        'node_modules/angular-loading-bar/build/loading-bar.css',
        'node_modules/typeahead.js-bootstrap-css/typeaheadjs.css',
        # 'node_modules/bootstrap-switch/dist/css/bootstrap3'
        # '/bootstrap-switch.css',
        filters='cleancss',
    ),
    depends=('scss/*.scss', ),
    output='gen/cernopendata.%(version)s.css',
    npm={
        'bootstrap-sass': '~3.3.5',
        # 'bootstrap-switch': '~3.0.2',
        'font-awesome': '~4.4.0',
        'typeahead.js-bootstrap-css': '~1.2.1',
    }
)
"""Default CSS bundle."""
