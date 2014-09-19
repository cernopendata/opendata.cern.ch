# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013, 2014 CERN.
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

"""Opendata Demosite interface."""

from invenio.base.i18n import _

from flask import Blueprint, render_template, redirect, url_for, abort, request, current_app
from flask.ext.login import current_user
from jinja2 import TemplateNotFound

from invenio.base.decorators import wash_arguments
from invenio.modules.search.signals import record_viewed
from invenio.modules.search.models import Collection
from invenio.modules.records.models import Record
from invenio.modules.records.api import get_record
from random import sample as randomise
from invenio.modules.records.views import request_record

blueprint = Blueprint('invenio_opendata', __name__, url_prefix='/',
                      template_folder='templates', static_folder='static')


@blueprint.route('')
def middle():
	try:
		return render_template('index_middle_with_design.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('middle')
def middle_des():
	try:
		return render_template('index_middle.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('index')
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
		return abort(404)

@blueprint.route('education', defaults={'exp':'all'})
@blueprint.route('education/<string:exp>')
def educate(exp):
	experiments = Collection.query.filter(Collection.id == '1' ).first_or_404()
	cms_collection = Collection.query.filter(Collection.name == 'CMS').first_or_404()
	alice_collection = Collection.query.filter(Collection.name == 'ALICE').first_or_404()
	def splitting(value, delimiter='/'):
		return value.split(delimiter)

	current_app.jinja_env.filters['splitthem'] = splitting
	try:
		return render_template('educate.html', experiments = experiments, exp = exp, cms_collection = cms_collection, alice_collection=alice_collection)
	except TemplateNotFound:
		return abort(404)

@blueprint.route('research', defaults={'exp':'all'})
@blueprint.route('research/<string:exp>')
def research(exp):
	cms_reclist = Collection.query.filter(Collection.name == 'CMS-Primary-Datasets').first_or_404().reclist
	cms = []
	for rec in cms_reclist[:6]:
		cms.append(get_record(rec))

	cmstools_reclist = Collection.query.filter(Collection.name == 'CMS-Tools').first_or_404().reclist
	cmstools = []
	for tool in cmstools_reclist[:3]:
		cmstools.append(get_record(tool))

	alice_reclist = Collection.query.filter(Collection.name == 'ALICE-Analyses').first_or_404().reclist
	alice = []
	for rec in alice_reclist[:6]:
		alice.append(get_record(rec))

	try:
		return render_template('research.html', cms = cms, alice = alice, cmstools = cmstools, exp = exp)
	except TemplateNotFound:
		return abort(404)

@blueprint.route('news', defaults={ 'newsid': None })
@blueprint.route('news/<int:newsid>')
def news(newsid):
	if newsid == None:
		try:
			return render_template('news.html')
		except TemplateNotFound:
			return abort(404)
	else:
		try:
			return render_template('news_page.html', news_id=newsid)
		except TemplateNotFound:
			return abort(404)

@blueprint.route('visualise/events')
def visualise_events():
	try:
		return render_template('visualise_events.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('visualise/histograms')
def visualise_histo():
	try:
		return render_template('visualise_histograms.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('getstarted', defaults={'exp':'all'})
@blueprint.route('<string:exp>/getstarted')
@blueprint.route('getstarted/<string:exp>')
@blueprint.route('getting-started', defaults={'exp':'all'})
@blueprint.route('getting-started/<string:exp>')
def get_started(exp):
	def splitting(value, delimiter='/'):
		return value.split(delimiter)

	current_app.jinja_env.filters['splitthem'] = splitting
	
	try:
		return render_template('get_started.html', exp = exp)
	except TemplateNotFound:
		return abort(404)

@blueprint.route('resources')
def visualise():
	try:
		return render_template('resources.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('VM', defaults={'exp':None})
@blueprint.route('VM/<string:exp>')
def data_vms(exp):
	def splitting(value, delimiter='/'):
		return value.split(delimiter)

	current_app.jinja_env.filters['splitthem'] = splitting

	try:
		return render_template('data_vms.html', exp = exp)
	except TemplateNotFound:
		return abort(404)

@blueprint.route('data')
def data():
	try:
		return render_template('data.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('about')
def about():
	try:
		return render_template('about.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('about/CMS')
@blueprint.route('about/cms')
def about_cms():
	try:
		return render_template('about_cms.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('about/ALICE')
@blueprint.route('about/alice')
def about_alice():
	try:
		return render_template('about_alice.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('about/CMS-Physics-Objects')
def about_physics():
	try:
		return render_template('about_physics_objects.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('terms-of-use')
def terms():
	try:
		return render_template('termsofuse.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('privacy-policy')
def privacy():
	try:
		return render_template('privacy.html')
	except TemplateNotFound:
		return abort(404)

@blueprint.route('experiments')
@blueprint.route('collections')
@blueprint.route('collection')
def collections():
	base_collection = Collection.query.filter(Collection.id == '1').first_or_404()
	experiments = base_collection.collection_children
	try:
		return render_template('collections_overview.html', experiments = experiments )
	except TemplateNotFound:
		return abort(404)

# Routing for "record" module

@blueprint.route('record/<int:recid>/files', methods=['GET','POST'])
@blueprint.route('record/<int:recid>/metadata', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/export/<of>', methods=['GET', 'POST'])
@wash_arguments({'of': (unicode, 'hd')})
@request_record
def metadata(recid, of='hd'):
	# Send the signal 'document viewed'
	record_viewed.send(
    	current_app._get_current_object(),
        recid=recid,
        id_user=current_user.get_id(),
        request=request)

	record_collection = get_record(recid)['collections'][0]['primary']
	try:
		return render_template(['records/'+record_collection+'_record.html', 'records/metadata_base.html'])
	except TemplateNotFound:
		return abort(404) #FIX


@blueprint.route('youraccount/login', methods=['GET', 'POST'])
@blueprint.route('youraccount/register', methods=['GET', 'POST'])
@blueprint.route('youraccount/logout', methods=['GET', 'POST'])
@blueprint.route('youraccount/', methods=['GET', 'POST'])
@blueprint.route('youraccount/display', methods=['GET', 'POST'])
@blueprint.route('youraccount/edit/<name>', methods=['GET', 'POST'])
@blueprint.route('youraccount/view', methods=['GET','POST'])
@blueprint.route('youraccount/lost', methods=['GET', 'POST'])
@blueprint.route('youraccount/access', methods=['GET', 'POST'])
def no_accounts():
	try:
		return render_template('404.html')
	except TemplateNotFound:
		return abort('404')
