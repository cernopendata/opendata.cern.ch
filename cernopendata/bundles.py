"""JS/CSS bundles for theme."""

from __future__ import absolute_import, print_function

from flask_assets import Bundle
from invenio_assets import NpmBundle

css = NpmBundle(
    'scss/styles.scss',
    filters='node-scss, cleancss',
    depends=('scss/*.scss', ),
    output='gen/cernopendata.%(version)s.css',
    npm={
        "almond": "~0.3.1",
        "bootstrap-sass": "~3.3.5",
        "font-awesome": "~4.4.0"
    }
)
"""Default CSS bundle."""
