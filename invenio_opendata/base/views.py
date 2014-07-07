# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
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
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""
    invenio_demosite.views
    -------------------------------

    Demosite interface.
"""
from invenio.base.i18n import _

from flask import Blueprint, render_template, redirect, url_for
from jinja2 import TemplateNotFound
from flask.ext.breadcrumbs import register_breadcrumb

blueprint = Blueprint('invenio_opendata', __name__, url_prefix='',
                      template_folder='templates', static_folder='static')


@blueprint.route('/')
def index():
	try:
		return render_template('carousel.html')
	except TemplateNotFound:
		abort(404)

@blueprint.route('/carouselsearch')
def index_search():
	try:
		return render_template('carousel_search.html')
	except TemplateNotFound:
		abort(404)

@blueprint.route('/static')
def static_view():
	try:
		return render_template('index.html')
	except TemplateNotFound:
		abort(404)

@blueprint.route('/middle')
def middle():
	try:
		return render_template('middle.html')
	except TemplateNotFound:
		abort(404)