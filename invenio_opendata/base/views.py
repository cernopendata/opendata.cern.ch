# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2013, 2014 CERN.
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

"""CERN Open Data Portal interface."""

from flask import Blueprint, render_template, \
    abort, request, current_app, g, url_for, redirect
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


def get_collections():
  experiments = Collection.query.filter(Collection.id == '1').first_or_404()
  exp_colls = []
  exp_names = []
  for exp in experiments.collection_children_v:
      exp_names.append(exp.name)
      exp_colls.append(Collection.query.filter(Collection.name == exp.name).first())

  return exp_colls, exp_names

def get_collection_names(without = []):
  experiments = Collection.query.filter(Collection.id == '1').first_or_404()
  exp_names = []
  for exp in experiments.collection_children_v:
    if exp.name not in without:
      exp_names.append(exp.name)

  return exp_names

def calculate_download_time(filesize, fileunits =1, transferunits=(1024*1024/8)):
  from math import floor,pow

  def _round(number, precision):
    if (precision>0):
        multiplier = pow(10,precision)
        return round(multiplier*number, precision)/multiplier
    else:
        return round(number, 0)

  seconds = (filesize*fileunits)/transferunits
  days_int = floor(seconds/86400)
  hours_int = floor(seconds/3600)
  minutes_int = floor((seconds - hours_int*3600)/60)
  seconds_float = seconds - minutes_int*60 - hours_int *3600
  seconds_float = _round(seconds_float,2)
  extra_mins = 1 if (minutes_int > 45)  else 0
  days_text = ' day ' if days_int == 1 else ' days '
  hoursText = ' hour ' if ( hours_int == 1 and extra_mins == 0 ) else ' hours '
  minutesText = ' minute ' if minutes_int == 1 else ' minutes '

  if (seconds < 60):
    return 'less than a minute'
  elif (seconds < 3600):
    return (str(int(minutes_int)) + minutesText)
  elif (seconds < 86400):
    return (str(int(hours_int)+extra_mins) + hoursText)
  else:
    return (str(int(days_int)) + days_text)

def splitting(value, delimiter='/', maxsplit=0):
    return value.split(delimiter, maxsplit)

@blueprint.route('')
def middle():
    import json, pkg_resources
    filepath = pkg_resources.resource_filename('invenio_opendata.base', 'templates/helpers/text/testimonials.json')
    with open(filepath,'r') as f:
        testimonials = json.load(f)

    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting

    exp_colls, exp_names = get_collections()

    try:
        return render_template('index_scrollspy.html', testimonials = testimonials, exp_colls = exp_colls, exp_names = exp_names)
    except TemplateNotFound:
        return abort(404)

@blueprint.route('education')
@blueprint.route('education/<string:exp>')
@register_breadcrumb(blueprint, '.educate', 'Education', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".educate","text":"Education"}
                        ]))
def educate(exp = None):
    import os.path, pkg_resources

    def file_exists(filename):
        filepath = pkg_resources.resource_filename('invenio_opendata.base', filename)
        return os.path.isfile(filepath)

    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting
    current_app.jinja_env.filters['file_exists'] = file_exists

    exp_colls, exp_names = get_collections()

    if exp not in exp_names:
        try:
            return render_template('index_scrollspy.html', entry = 'education', exp_colls = exp_colls, exp_names = exp_names)
        except TemplateNotFound:
            return abort(404)

    try:
        return render_template('educate.html',
                               exp=exp, exp_colls = exp_colls, exp_names = exp_names)
    except TemplateNotFound:
        return abort(404)



@blueprint.route('research')
@blueprint.route('research/<string:exp>')
@register_breadcrumb(blueprint, '.research', 'Research', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".research","text":"Research"}]))
def research(exp = None):
    import os.path, pkg_resources

    def file_exists(filename):
        filepath = pkg_resources.resource_filename('invenio_opendata.base', filename)
        return os.path.isfile(filepath)

    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting
    current_app.jinja_env.filters['file_exists'] = file_exists

    exp_colls, exp_names = get_collections()

    if exp not in exp_names :
        try:
            return render_template('index_scrollspy.html', entry = 'research', exp_colls = exp_colls, exp_names = exp_names)
        except TemplateNotFound:
            return abort(404)

    try:
        return render_template('research.html',
                               exp=exp, exp_colls = exp_colls, exp_names = exp_names)
    except TemplateNotFound:
        return abort(404)

@blueprint.route('visualise/events/<string:exp>')
def visualise_events(exp = 'CMS'):

    exp_names = get_collection_names(['ALICE', 'LHCb', 'ATLAS'])

    breadcrumbs = [{},{"url":".educate","text":"Education"},\
                        {"url":".educate","text":"Visualise Events"}]
    try:
        return render_template('visualise_events.html', exp = exp, exp_names = exp_names, breadcrumbs = breadcrumbs)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('visualise/histograms/<string:exp>')
def visualise_histo(exp = 'CMS'):
    exp_colls, exp_names = get_collections()

    breadcrumbs = [{},{"url":".educate","text":"Education"},\
                        {"url":".educate","text":"Visualise Histograms"}]

    try:
        return render_template('visualise_histograms.html', exp = exp, exp_names = exp_names, breadcrumbs = breadcrumbs)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('getstarted', defaults={'exp': None})
@blueprint.route('<string:exp>/getstarted')
@blueprint.route('getstarted/<string:exp>')
@blueprint.route('getting-started', defaults={'exp': None, 'year': None})
@blueprint.route('getting-started/<string:exp>',defaults={'year': None})
@blueprint.route('getting-started/<string:exp>/<string:year>')
@register_breadcrumb(blueprint, '.get_started', 'Get Started', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".get_started","text":"Getting started"}]))
def get_started(exp, year):
    def splitting(value, delimiter='/'):
        return value.split(delimiter)
    exp_names = get_collection_names()
    current_app.jinja_env.filters['splitthem'] = splitting

    try:
        return render_template('get_started.html', exp=exp,exp_names=exp_names, year=year)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('resources/<string:exp>')
@blueprint.route('resources', defaults={'exp': None})
@register_breadcrumb(blueprint, '.resources', 'Learning Resources', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".educate","text":"Education"},\
                        {"url":".resources","text":"Learning Resources"}]) )
def resources(exp):
    exp_names = get_collection_names()

    try:
        return render_template('resources.html', exp=exp, exp_names=exp_names)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('VM', defaults={'exp': None, 'year': None})
@blueprint.route('VM/<string:exp>', defaults={'year': None})
@blueprint.route('VM/<string:exp>/<string:year>')
@register_breadcrumb(blueprint, '.data_vms', 'Virtual Machines' , \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".data_vms","text":"Virtual Machines"}]) )
def data_vms(exp, year):
    exp_names = get_collection_names(['ATLAS'])
    if exp not in exp_names and exp is not None:
        return render_template("404.html")

    def splitting(value, delimiter='/'):
        return value.split(delimiter)
    current_app.jinja_env.filters['splitthem'] = splitting

    try:
        return render_template('data_vms.html', exp=exp, exp_names=exp_names, year=year)
    except TemplateNotFound:
        return abort(404)

@blueprint.route('VM/<exp>/validation/report')
@register_breadcrumb(blueprint, '.val_report', 'VM', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".data_vms","text":"Virtual Machines"},\
                        {"url":".data_vms","text":"Validation Report"}]) )
def val_report(exp):
    exp_names = get_collection_names()

    try:
        return render_template([exp+'_VM_validation.html', 'data_vms.html'], exp=exp,exp_names=exp_names)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('about')
@register_breadcrumb(blueprint, '.about', 'About', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".about","text":"About"}]))
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        return abort(404)


@blueprint.route('about/cms')
@blueprint.route('about/CMS')
@register_breadcrumb(blueprint, '.about_cms', 'CMS', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".about", "text":"About"},\
                        {"url":".about_cms","text":"CMS Open Data"}]) )
def about_cms():
    try:
        return render_template('about_cms.html')
    except TemplateNotFound:
        return abort(404)

@blueprint.route('about/alice')
@blueprint.route('about/ALICE')
@register_breadcrumb(blueprint, '.about_alice', 'ALICE', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".about", "text":"About"},\
                        {"url":".about_alice","text":"ALICE Open Data"}]) )
def about_alice():
    try:
        return render_template('about_alice.html')
    except TemplateNotFound:
        return abort(404)

@blueprint.route('about/atlas')
@blueprint.route('about/ATLAS')
@register_breadcrumb(blueprint, '.about_atlas', 'ATLAS', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".about", "text":"About"},\
                        {"url":".about_atlas","text":"ATLAS Open Data"}]) )
def about_atlas():
    try:
        return render_template('about_atlas.html')
    except TemplateNotFound:
        return abort(404)

@blueprint.route('about/lhcb')
@blueprint.route('about/LHCb')
@register_breadcrumb(blueprint, '.about_lhcb', 'LHCb', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".about", "text":"About"},\
                        {"url":".about_lhcb","text":"LHCb Open Data"}]) )
def about_lhcb():
    try:
        return render_template('about_lhcb.html')
    except TemplateNotFound:
        return abort(404)

@blueprint.route('about/CMS-Physics-Objects', defaults={'year': None})
@blueprint.route('about/CMS-Physics-Objects/<string:year>')
@register_breadcrumb(blueprint, '.about_physics', 'CMSS', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".about", "text":"About"},\
                        {"url":".about_cms", "text":"CMS"},\
                        {"url":".about_physics","text":"Physics Objects"}]) )
def about_physics(year):
    try:
        return render_template('about_physics_objects_overview.html', year = year)
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
    import json, pkg_resources
    filepath = pkg_resources.resource_filename('invenio_opendata.base', 'templates/helpers/text/testimonials.json')
    with open(filepath,'r') as f:
        testimonials = json.load(f)

    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting

    exp_colls, exp_names = get_collections()

    try:
        return render_template('index_scrollspy.html', testimonials = testimonials, exp_colls = exp_colls, exp_names = exp_names)
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
    collection = Collection.query.filter(Collection.name == name).first()

    if collection == None:
        return render_template('404.html')

    parent_collection = collection.most_specific_dad \
                        if (collection.most_specific_dad and \
                            collection.most_specific_dad.id != 1) else None

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

    breadcrumbs = [{}]
    if parent_collection:
        breadcrumbs.append({ "url":".collection", "text": parent_collection.name_ln, "param":"name", "value": parent_collection.name })
        exp = parent_collection.name_ln
    else:
        exp = collection.name_ln

    breadcrumbs.append({ "url":".collection", "text": collection.name_ln, "param":"name", "value": collection.name })

    return render_template(['search/collection_{0}.html'.format(collection.id),
                            'search/collection_{0}.html'.format(slugify(name,
                                                                        '_')),
                            'search/collection.html'],
                           collection=collection, coll_records=coll_records, breadcrumbs = breadcrumbs, exp = exp)


# Routing for "record" module
@blueprint.route('record/<int:recid>/files', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/metadata', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/export', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/export/<of>', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/usage', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/references', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/keywords', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/citations', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>', methods=['GET', 'POST'])
@wash_arguments({'of': (unicode, 'hd')})
@request_record
def metadata(recid, of='hd'):
    from invenio.legacy.bibrank.downloads_similarity import register_page_view_event
    from invenio.modules.formatter import get_output_format_content_type
    register_page_view_event(recid, current_user.get_id(), str(request.remote_addr))
    if get_output_format_content_type(of) != 'text/html':
        from invenio.modules.search.views.search import response_formated_records
        return response_formated_records([recid], g.collection, of, qid=None)


    # Send the signal 'document viewed'
    record_viewed.send(
        current_app._get_current_object(),
        recid=recid,
        id_user=current_user.get_id(),
        request=request)


    def get_record_name(recid):
        tmp_rec = get_record(recid)
        if tmp_rec is None:
            return 'Can\'t link to record ( WRONG recid )'

        if 'title_additional' in tmp_rec :
            return tmp_rec.get('title_additional', '').get('title', '')
        elif tmp_rec.get('title',{}).get('title',''):
            return tmp_rec.get('title',{}).get('title','')

    def get_record_author_list(recid):
        tmp_rec = get_record(recid)
        if tmp_rec is None:
            return None

        return tmp_rec.get('authors','')


    current_app.jinja_env.filters['splitthem'] = splitting
    current_app.jinja_env.filters['get_record_name'] = get_record_name
    current_app.jinja_env.filters['get_record_author_list'] = get_record_author_list
    current_app.jinja_env.filters['get_download_time'] = calculate_download_time


    record_collection = get_record(recid)['collections'][0]['primary']
    rec_col = Collection.query.filter(Collection.name == record_collection).first_or_404()
    parent_collection = rec_col.most_specific_dad \
                        if (rec_col.most_specific_dad and \
                            rec_col.most_specific_dad.id != 1) else None

    breadcrumbs = [{}]

    if parent_collection:
        breadcrumbs.append({ "url":".collection", "text": parent_collection.name_ln, "param":"name", "value": parent_collection.name })

    breadcrumbs.append({"url":".collection", "text": rec_col.name_ln, "param":"name", "value":rec_col.name })

    try:
        return render_template(['records/'+record_collection+'_base.html','records/base_base.html'], breadcrumbs = breadcrumbs )
    except TemplateNotFound:
        return abort(404)  # FIX

@blueprint.route('record/<int:recid>/load/authors/<int:start>/to/<int:end>', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/load/authors/', methods=['GET', 'POST'], defaults={'start': '0', 'end':'100'})
def load_authors(recid, start = 0, end = 100):
  from invenio.modules.records.models import Record

  record = Record.query.filter(Record.id == recid).first_or_404()
  data = record.record_json[0].json['authors'][start:end]

  try:
    return render_template('records/load_authors_base.html', data = data, start = start, end = end)
  except TemplateNotFound:
    return render_template('404.html')

@blueprint.route('record/<int:recid>/load/files/<int:start>/to/<int:end>', methods=['GET', 'POST'])
@blueprint.route('record/<int:recid>/load/files/', methods=['GET', 'POST'], defaults={'start': '0', 'end':'5'})
def load_files(recid, start = 0, end = 5):
  from invenio.modules.records.models import Record

  record = Record.query.filter(Record.id == recid).first_or_404()
  data = record.record_json[0].json['electronic_location'][start:end]

  current_app.jinja_env.filters['get_download_time'] = calculate_download_time
  current_app.jinja_env.filters['splitthem'] = splitting

  try:
    return render_template('records/load_files_base.html', data = data, start = start, end = end)
  except TemplateNotFound:
    return render_template('404.html')

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


@blueprint.route('glossary', methods=['GET', 'POST'])
@register_breadcrumb(blueprint, '.glossary', 'Glossary', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".educate", "text":"Education"},\
                        {"url":".glossary","text":"Glossary"}]) )
def glossary():
    import json, pkg_resources
    filepath = pkg_resources.resource_filename('invenio_opendata.base', 'static/json/glossary.json')
    with open(filepath,'r') as f:
        glossary = json.load(f)

    try:
        return render_template('glossary.html', glossary = glossary)
    except TemplateNotFound:
        return abort('404')

@blueprint.route('news')
@register_breadcrumb(blueprint,'.news','News', \
                        dynamic_list_constructor = (lambda :\
                        [{"url":".news","text":"News"}]))
def news():
    try:
        return render_template('news.html')
    except TemplateNotFound:
        return abort(404)

