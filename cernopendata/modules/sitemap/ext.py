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

"""Sitemap generation for CERN Open Data Portal."""

from flask import current_app, render_template

from . import config
from .generators import urls_generator


class CERNOpenDataSitemap(object):
    """CERN Open Data sitemap extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        # Follow the Flask guidelines on usage of app.extensions
        if "cernopendata-sitemap" in app.extensions:
            raise RuntimeError("CERNOpenDataSitemap application already" "initialized")
        self.app = app
        self.init_config(app)
        self.urls_generator = urls_generator
        app.extensions["cernopendata-sitemap"] = self

    @staticmethod
    def init_config(app):
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("CERNOPENDATA_SITEMAP_"):
                app.config.setdefault(k, getattr(config, k))

    def _generate_all_urls(self):
        """Run all generators and yield the sitemap JSON entries."""
        for doc_type in current_app.config["CERNOPENDATA_SITEMAP_DOC_TYPES"]:
            for generated in urls_generator(doc_type):
                yield generated

    def get_populated_sitemap(self):
        """Populate sitemap template with current app urls."""
        site_url = current_app.config["SITE_URL"]
        with current_app.test_request_context(base_url=site_url):
            urls = iter(self._generate_all_urls())
            page = render_template("sitemap/sitemap.xml", urlset=filter(None, urls))
            return page
