# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2013, 2014 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Opendata Demosite interface."""

from flask import Blueprint, render_template, \
    abort, request, current_app, g, url_for
from flask.ext.login import current_user
from jinja2 import TemplateNotFound

from invenio.base.decorators import wash_arguments
from invenio.modules.search.signals import record_viewed
from invenio.modules.search.models import Collection
from invenio.modules.records.api import get_record
from invenio.modules.records.views import request_record
from flask.ext.breadcrumbs import \
    register_breadcrumb, current_breadcrumbs, default_breadcrumb_root
from flask.ext.menu import register_menu

blueprint = Blueprint('invenio_opendata', __name__, url_prefix='/',
                      template_folder='templates', static_folder='static')
default_breadcrumb_root(blueprint, '.')


@blueprint.route('')
def middle():
    import json, pkg_resources
    filepath = pkg_resources.resource_filename('invenio_opendata.base', 'templates/helpers/text/testimonials.json')
    with open(filepath,'r') as f:
        testimonials = json.load(f)

    try:
        return render_template('index_middle_with_design.html', testimonials = testimonials)
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


@blueprint.route('education', defaults={'exp': None})
@blueprint.route('education/<string:exp>')
@register_breadcrumb(blueprint, '.educate', 'For Education')
def educate(exp):
    experiments = Collection.query.filter(Collection.id == '1').first_or_404()
    cms_collection = Collection.query.filter(Collection.name == 'CMS').first_or_404()
    alice_collection = Collection.query.filter(Collection.name == 'ALICE').first_or_404()

    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting
    try:
        return render_template('educate.html', experiments=experiments,
                               exp=exp, cms_collection=cms_collection,
                               alice_collection=alice_collection)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('research', defaults={'exp': None})
@blueprint.route('research/<string:exp>')
@register_breadcrumb(blueprint, '.research', 'For Research')
def research(exp):
    experiments = Collection.query.filter(Collection.id == '1').first_or_404()
    cms_collection = Collection.query.filter(Collection.name == 'CMS').first_or_404()
    alice_collection = Collection.query.filter(Collection.name == 'ALICE').first_or_404()

    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting
    try:
        return render_template('research.html', experiments=experiments,
                               exp=exp, cms_collection=cms_collection,
                               alice_collection=alice_collection)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('news', defaults={'newsid': None})
@blueprint.route('news/<int:newsid>')
@register_breadcrumb(blueprint,'.news','News')
def news(newsid):
    if newsid is None:
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
@register_breadcrumb(blueprint, '.visualise_events', 'Visualise Histograms', \
                        dynamic_list_constructor = (lambda :\
                        [({"url":"education"},{"text":"For Education"}),\
                        ({"url":"education/CMS"},{"text":"CMS"}),\
                        ({"url":".visualise_events"},{"text":"Visualise Events"})]) )
def visualise_events():
    try:
        return render_template('visualise_events.html')
    except TemplateNotFound:
        return abort(404)


@blueprint.route('visualise/histograms')
@register_breadcrumb(blueprint, '.visualise_histo', 'Visualise Histograms', \
                        dynamic_list_constructor = (lambda :\
                        [({"url":"education"},{"text":"For Education"}),\
                        ({"url":"education/CMS"},{"text":"CMS"}),\
                        ({"url":".visualise_histo"},{"text":"Visualise Histograms"})]) )
def visualise_histo():
    try:
        return render_template('visualise_histograms.html')
    except TemplateNotFound:
        return abort(404)


@blueprint.route('getstarted', defaults={'exp': None})
@blueprint.route('<string:exp>/getstarted')
@blueprint.route('getstarted/<string:exp>')
@blueprint.route('getting-started', defaults={'exp': 'all'})
@blueprint.route('getting-started/<string:exp>')
@register_breadcrumb(blueprint, '.get_started', 'Get Started')
def get_started(exp):
    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting

    try:
        return render_template('get_started.html', exp=exp)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('resources')
@register_breadcrumb(blueprint, '.resources', 'External Resources', \
                        dynamic_list_constructor = (lambda :\
                        [({"url":"education"},{"text":"For Education"}),\
                        ({"url":"education/CMS"},{"text":"CMS"}),\
                        ({"url":"resources"},{"text":"External Resources"})]) )
def resources():
    try:
        return render_template('resources.html')
    except TemplateNotFound:
        return abort(404)


@blueprint.route('VM', defaults={'exp': None})
@blueprint.route('VM/<string:exp>')
@register_breadcrumb(blueprint, '.data_vms', 'Virtual Machines' )
def data_vms(exp):
    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting

    try:
        return render_template('data_vms.html', exp=exp)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('data')
def data():
    try:
        return render_template('data.html')
    except TemplateNotFound:
        return abort(404)


@blueprint.route('about')
@register_breadcrumb(blueprint, '.about', 'About')
def about():
    try:    
        return render_template('about.html')
    except TemplateNotFound:
        return abort(404)


@blueprint.route('about/cms')
@blueprint.route('about/CMS')
@register_breadcrumb(blueprint, '.about_cms', 'CMS', \
                        dynamic_list_constructor = (lambda :\
                        [({"url":".about"},{"text":"About"}),\
                        ({"url":".about_cms"},{"text":"CMS OpenData"})]) )
def about_cms():
    try:
        return render_template('about_cms.html')
    except TemplateNotFound:
        return abort(404)

def about_cms_bread():
    return ()

@blueprint.route('about/alice')
@blueprint.route('about/ALICE')
@register_breadcrumb(blueprint, '.about_alice', 'ALICE', \
                        dynamic_list_constructor = (lambda :\
                        [({"url":".about"},{"text":"About"}),\
                        ({"url":".about_alice"},{"text":"ALICE OpenData"})]) )
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
    experiments = base_collection.collection_children_v
    try:
        return render_template('collections_overview.html',
                               experiments=experiments)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('collection/<name>', methods=['GET', 'POST'])
def collection(name):
    """
    Render the collection page.

    It renders it either with a collection specific template (aka
    collection_{collection_name}.html) or with the default collection
    template (collection.html)
    """
    from invenio.utils.text import slugify
    from invenio.modules.formatter import format_record
    from invenio.modules.search.forms import EasySearchForm
    from invenio.ext.template.context_processor import \
    register_template_context_processor
    from flask.ext.breadcrumbs import current_breadcrumbs

    collection = Collection.query.filter(Collection.name == name) \
                                 .first_or_404()
    coll_reclist = collection.reclist
    coll_records = []
    for rec in coll_reclist:
        coll_records.append(get_record(rec))
    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting
    
    @register_template_context_processor
    def index_context():
        breadcrumbs = current_breadcrumbs + collection.breadcrumbs(ln=g.ln)[1:]
        return dict(
            of=request.values.get('of', collection.formatoptions[0]['code']),
            format_record=format_record,
            easy_search_form=EasySearchForm(csrf_enabled=False),
            breadcrumbs=breadcrumbs)

    return render_template(['search/collection_{0}.html'.format(collection.id),
                            'search/collection_{0}.html'.format(slugify(name,
                                                                        '_')),
                            'search/collection.html'],
                           collection=collection, coll_records=coll_records)


# Routing for "record" module
@blueprint.route('record/<int:recid>/files', methods=['GET', 'POST'])
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
        return render_template(['records/'+record_collection+'_record.html',
                                'records/metadata_base.html'])
    except TemplateNotFound:
        return abort(404)  # FIX


@blueprint.route('youraccount/login', methods=['GET', 'POST'])
@blueprint.route('youraccount/register', methods=['GET', 'POST'])
@blueprint.route('youraccount/logout', methods=['GET', 'POST'])
@blueprint.route('youraccount/', methods=['GET', 'POST'])
@blueprint.route('youraccount/display', methods=['GET', 'POST'])
@blueprint.route('youraccount/edit/<name>', methods=['GET', 'POST'])
@blueprint.route('youraccount/view', methods=['GET', 'POST'])
@blueprint.route('youraccount/lost', methods=['GET', 'POST'])
@blueprint.route('youraccount/access', methods=['GET', 'POST'])
def no_accounts():
    try:
        return render_template('404.html')
    except TemplateNotFound:
        return abort('404')
