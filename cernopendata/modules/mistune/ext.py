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

"""Initialization of CernopendataMistune."""

from __future__ import absolute_import, print_function

from flask.ext.mistune import Mistune

import mistune

from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments import highlight
import pygments.util


class CodeHtmlFormatter(HtmlFormatter):
    """Pygments formatter that adds HTML5 <code>-tag to generated html.

    Add the <code>-tag after Pygments usual <div class="highlight">
    and <pre> classes.
    Based on example from http://pygments.org/docs/formatters/
    """

    def __init__(self, lang=False, **options):
        """."""
        self.lang = lang
        super(CodeHtmlFormatter, self).__init__(**options)

    def wrap(self, source, outfile):
        """."""
        return self._wrap_code(source)

    def _wrap_code(self, source):
        if self.lang:
            yield 0, '<div class="highlight"><pre><code class="lang-{}">'.\
                format(self.lang)
        else:
            yield 0, '<div class="highlight"><pre><code>'
        for i, t in source:

            yield i, t
        yield 0, '</code></pre></div>'


class CodeRenderer(mistune.Renderer):
    """Renderer to support standard pygments-themes (adds highlight-class).

    Based on https://github.com/asottile/markdown-code-blocks and on
    https://github.com/lepture/mistune-contrib/blob/master/mistune_contrib/highlight.py
    """

    def block_code(self,
                   code,
                   lang,
                   code_tag=True,
                   inlinestyles=False,
                   linenos=False):
        """.

        :param code_tag: If True html will contain <code>-tag.
        :param inlinestyles: If True html contains inline styles.
        :param linenos: If True html contains line numbers
        :return:
        """
        try:
            lexer = get_lexer_by_name(lang, stripnl=False)
        except pygments.util.ClassNotFound:
            lexer = get_lexer_by_name('text', stripnl=False)

        if code_tag:
            formatter = CodeHtmlFormatter(lang,
                                          noclasses=inlinestyles,
                                          linenos=linenos)
        else:
            formatter = HtmlFormatter(noclasses=inlinestyles, linenos=linenos)

        return highlight(code, lexer=lexer, formatter=formatter)


class CernopendataMistune(object):
    """CernopendataMistune. Wrapper for Flask-Mistune extension.

    Needed in order to properly add Flask-Mistune to Flask application
    created in Invenio-style (using entrypoints).
    """

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        if 'cod-mistune' in app.extensions:
            raise RuntimeError("Flask application already initialized")
        app.extensions['cod-mistune'] = self

        # Initialize Flask-Mistune extension.
        # TODO: Define and add config entries to app.config.
        # TODO: Init according options in app.config.

        # Mistune with only HTML5 <code>-tag highlighting.
        # Support for language specific highlight styles, with
        # <code class="lang-XXX">.
        # mistune = Mistune(app, escape=False, hard_wrap=True)

        # Mistune with HTML5 <code>-tag highlight wrapped inside
        # Pygments style <div class="highlight"><pre> highlight
        # Provides support for Pygments and language specific highlight styles
        mistune = Mistune(app,
                          renderer=CodeRenderer(escape=False, hard_wrap=True))
