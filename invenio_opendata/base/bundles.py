# -*- coding: utf-8 -*-
#
## This file is part of Invenio.
## Copyright (C) 2014 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02D111-1307, USA.

"""CDS bundles."""

from invenio.ext.assets import Bundle

from invenio.base.bundles import styles as _styles

_styles.contents.remove("less/base.less")
_styles.contents += ("less/cds.less",)


css = Bundle(
    "css/style.css",
    "css/carousel.css",
    "css/collection.css",
    "css/testimonials.css",
    "css/search.css",
    "css/educate.css",
    "css/news.css",
    output="opendata.css",
    weight=1,
)

js = Bundle(
    "js/main.js",
    output="cds.js",
    weight=91,
    filters="requirejs",
    bower={
        "backbone": "latest",
        "backbone.localstorage": "latest",
        "jsx-requirejs-plugin": "latest",
        "requirejs-plugins": "latest",
        "es5-shim": "latest"
    }
)
