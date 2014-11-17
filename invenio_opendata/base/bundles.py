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

css = Bundle(
    "css/style.css",
    "css/carousel.css",
    "css/collection.css",
    "css/testimonials.css",
    "css/search.css",
    "css/educate.css",
    "css/news.css",
    "css/records.css",
    "css/middle.css",
    "css/record.css",
    "css/general.css",
    output="opendata.css",
    weight=1,
)

ie_bundle = Bundle(
    "vendors/respond/src/respond.js",
    output="respond.js", 
    weight=200,
)

od_records_js = Bundle(
    "vendors/readmore/readmore.min.js",
    "js/records_base.js",
    output = "od_records.js",
    weight=20,
    bower = {
    "readmore": "latest",
    }
)

od_records_utils_js = Bundle(
    "vendors/listjs/dist/list.min.js",
    output = "od_records_utils.js",
    weight=40,
    filters="requirejs",
    bower = {
        "readmore": "latest",
        "listjs": "latest",
    }
)

od_d3_js = Bundle(
    "vendors/d3/d3.min.js",
    "vendors/flot/jquery.flot.js",
    "vendors/flot/jquery.flot.selection.js",
    output = "d3.js",
    bower = {
       "d3": "3.3.13"
    }
)
