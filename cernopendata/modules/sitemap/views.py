# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2018 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Sitemap views for CERN Open Data Portal."""

from flask import Blueprint, current_app, make_response

static_folder = "static"

blueprint = Blueprint(
    "cernopendata_sitemap",
    __name__,
    url_prefix="",
    template_folder="templates",
    static_folder=static_folder,
)


@blueprint.route(
    "/sitemap.xml",
    methods=[
        "GET",
    ],
)
def sitemappage():
    """Get the sitemap."""
    sitemap = current_app.extensions["cernopendata-sitemap"]
    sitemap_xml = sitemap.get_populated_sitemap()
    response = make_response(sitemap_xml)
    response.headers["Content-Type"] = "application/xml"
    return response
