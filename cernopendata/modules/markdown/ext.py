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

from flaskext.markdown import Markdown


class CernopendataMarkdown(object):
    r"""CernopendataMarkdown. Wrapper for Flask-Markdown extension.

    Needed in order to add Flask-Markdown to Flask application
    created in Invenio-style (using entrypoints).

    ### GitHub Flavored Markdown.
    Supports GitHub Flavored Markdown with PyMdown Extensions
    (https://facelessuser.github.io/pymdown-extensions/)

    ### TeX-support
    Supports math in TeX-syntax by utilizing python-markdown-math
    (https://github.com/mitya57/python-markdown-math)

    Produces TeX-syntax inside html script tags:
    ```
      '$$e^x$$'
        --> '<p>\n<script type="math/tex; mode=display">e^x</script>\n</p>'
    ```

    Supports at least following syntaxes:
    ```
      '$e^{i\pi}* = -1$'
      '$$e^{i\pi}* = -1$$'
      '\begin{equation*}e^{i\pi}* = -1\end{equation*}'
      '\[e^{i\pi}* = -1\]'
    ```

    Requires TeX-content to be rendered e.g. in client-side using MathJax.js.

    Example of suitable MathJax config:
        ```
        <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
          config: ["MMLorHTML.js"],
          jax: ["input/TeX", "output/HTML-CSS", "output/NativeMML"],
          extensions: ["MathMenu.js", "MathZoom.js"]
        });
        </script>
        ```
    """

    def __init__(self, app=None):
        """Extension initialization."""
        if app:
            self.md = None
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        # Follow the Flask guidelines on usage of app.extensions
        if not hasattr(app, "extensions"):
            app.extensions = {}
        if "cod-markdown" in app.extensions:
            raise RuntimeError("Flask application already initialized")
        app.extensions["cod-markdown"] = self

        # TODO: Define and add config entries to app.config.
        # TODO: Init according options in app.config.

        # Extension for Python-Markdown
        pymd_extensions = []

        # GitHub Flavored Markdown.
        # github extension is deprecated, workaround is to use other extensions
        # https://facelessuser.github.io/pymdown-extensions/faq/
        pymd_extensions.append("markdown.extensions.attr_list")
        pymd_extensions.append("markdown.extensions.tables")
        pymd_extensions.append("markdown.extensions.toc")
        pymd_extensions.append("pymdownx.magiclink")
        pymd_extensions.append("pymdownx.betterem")
        pymd_extensions.append("pymdownx.tilde")
        pymd_extensions.append("pymdownx.emoji")
        pymd_extensions.append("pymdownx.tasklist")
        pymd_extensions.append("pymdownx.superfences")

        # TeX-syntax math notation support.
        pymd_extensions.append("mdx_math")

        # Configuration for extensions.
        # For config format see:
        # https://pythonhosted.org/Markdown/reference.html#extension_configs
        pymd_extension_configs = {
            "markdown.extensions.toc.": {
                "anchorlink": True,
                "permalink": True,
                "toc_depth": 3,
            },
            "pymdownx.tilde": {"subscript": True},
            "mdx_math": {
                "enable_dollar_delimiter": "True",
                # 'add_preview': 'False',
            },
        }

        # Initialize Flask-Markdown Flask-extension
        # Pass list of Python-Markdown extensions and extension's config
        self.md = Markdown(
            app,
            extensions=pymd_extensions,
            extension_configs=pymd_extension_configs,
        )
