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

"""CDS Demosite interface."""

from invenio.base.i18n import _

from flask import Blueprint, render_template, redirect, url_for, abort
from jinja2 import TemplateNotFound


blueprint = Blueprint('cds', __name__, url_prefix='/',
                      template_folder='templates', static_folder='static')


@blueprint.route('/')
def index():
	try:
		return render_template('index.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('index2')
def index2():
	try:
		return render_template('index2.html')
	except TemplateNotFound:
		return abort(405)

@blueprint.route('educate')
def educate():
	try:
		return render_template('educate.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('research')
def research():
	try:
		return render_template('research.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('news')
def news():
	try:
		return render_template('news.html')
	except TemplateNotFound:
		return abort(404)

