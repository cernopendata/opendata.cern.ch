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

"""Initialization of CernopendataMarkdown."""

from __future__ import absolute_import, print_function

from flaskext.markdown import Markdown

from mdx_gfm import GithubFlavoredMarkdownExtension

from pymdownx.github import GithubExtension


class CernopendataMarkdown(object):
    """CernopendataMarkdown. Wrapper for Flask-Markdown extension.

    Needed in order to add Flask-Markdown to Flask application
    created in Invenio-style (using entrypoints).
    """

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        # Follow the Flask guidelines on usage of app.extensions
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        if 'cod-markdown' in app.extensions:
            raise RuntimeError("Flask application already initialized")
        app.extensions['cod-markdown'] = self

        # Initialize Flask-Markdown extension
        md = Markdown(app)

        # Register Flask-Markdown extensions
        # TODO: Define and add config entries to app.config.
        # TODO: Init according options in app.config.

        # https://github.com/Zopieux/py-gfm
        # md.register_extension(GithubFlavoredMarkdownExtension)

        # Alternative GFM extension:
        # http://facelessuser.github.io/pymdown-extensions/extensions/github/
        md.register_extension(GithubExtension)
