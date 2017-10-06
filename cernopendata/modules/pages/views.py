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

"""Pages for CERN Open Data Portal."""

from __future__ import absolute_import, print_function

import json
import urllib

import pkg_resources
from flask import Blueprint, abort, current_app, escape, jsonify, \
    render_template, request, url_for
from flask_babelex import lazy_gettext as _
from flask_breadcrumbs import default_breadcrumb_root, register_breadcrumb
from flask_menu import register_menu
from jinja2.exceptions import TemplateNotFound
from speaklater import make_lazy_string

from cernopendata.modules.collections.descriptions import descriptions

from .utils import FrontpageRecordsSearch

blueprint = Blueprint(
    'cernopendata_pages',
    __name__,
    template_folder='templates',
    static_folder='static',
)

default_breadcrumb_root(blueprint, '.')


@blueprint.errorhandler(TemplateNotFound)
def template_not_found(err):
    """Log missing template."""
    current_app.logger.exception('Please check missing template.')
    abort(404)
    # return 'Template not found!', 404


def lazy_title(text, *args):
    """Make tranlated string with escaped values from request view args."""
    return _(text, **{key: make_lazy_string(
        lambda: escape(request.view_args.get(key, ''))
    ) for key in args})


@blueprint.route('/')
@register_menu(blueprint, 'main.education', _('Education'), order=2,
               active_when=lambda: False,
               endpoint_arguments_constructor=lambda: {'_anchor': 'education'})
@register_menu(blueprint, 'main.research', _('Research'), order=3,
               active_when=lambda: False,
               endpoint_arguments_constructor=lambda: {'_anchor': 'research'})
@register_breadcrumb(blueprint, '.', _('Home'))
@register_breadcrumb(blueprint, '.education', _('Education'),
                     endpoint_arguments_constructor=lambda: {
                         '_anchor': 'education'})
@register_breadcrumb(blueprint, '.research', _('Research'),
                     endpoint_arguments_constructor=lambda: {
                         '_anchor': 'education'})
def index():
    """Home Page."""
    results = FrontpageRecordsSearch()[:6].execute()
    return render_template('cernopendata_pages/index.html',
                           records=results.hits.hits)


@blueprint.route('/education')
@blueprint.route('/education/<string:experiment>')
@register_breadcrumb(blueprint, '.education.experiment',
                     lazy_title('%(experiment)s', 'experiment'),
                     endpoint_arguments_constructor=lambda: {
                         'experiment': request.view_args['experiment']})
def education(experiment=None):
    """Display education pages."""
    if experiment not in current_app.config['OPENDATA_EXPERIMENTS']:
        abort(404)

    return render_template('cernopendata_pages/education.html',
                           experiment=experiment)


@blueprint.route('/research')
@blueprint.route('/research/<string:experiment>')
@register_breadcrumb(blueprint, '.research.experiment',
                     lazy_title('%(experiment)s', 'experiment'),
                     endpoint_arguments_constructor=lambda: {
                         'experiment': request.view_args['experiment']})
def research(experiment=None):
    """Display research pages."""
    import os.path
    import pkg_resources

    def file_exists(filename):
        filepath = pkg_resources.resource_filename(
            'cernopendata.base', filename)
        return os.path.isfile(filepath)

    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting
    current_app.jinja_env.filters['file_exists'] = file_exists

    exp_colls, exp_names = get_collections()

    if experiment not in exp_names:
        return render_template(
            'index_scrollspy.html',
            entry='research',
            exp_colls=exp_colls,
            exp_names=exp_names)

    return render_template(
        'research.html',
        experiment=experiment,
        exp_colls=exp_colls,
        exp_names=exp_names)


@blueprint.route('/visualise/events')
@register_breadcrumb(blueprint, '.visualise_events', _('Visualise Events'))
def visualise_events_landing():
    """Display landing page."""
    try:
        return render_template(
            'cernopendata_pages/visualise_events.html')
    except TemplateNotFound:
        return abort(404)


@blueprint.route('/visualise/events/<string:experiment>')
@blueprint.route('/visualise/events/<string:experiment>/<int:eventid>')
@register_breadcrumb(blueprint, '.visualise_events', _('Visualise Events'))
def visualise_events(experiment='CMS', eventid=None):
    """Display visualisations."""
    try:
        return render_template(
            'cernopendata_pages/visualise_events_{}.html'.format(
                experiment.lower()),
            eventid=eventid,
            experiment=experiment,
        )
    except TemplateNotFound:
        return abort(404)


@blueprint.route('/visualise/histograms/<string:experiment>')
@register_breadcrumb(blueprint, '.visualise_histograms',
                     _('Visualise Histograms'))
def visualise_histograms(experiment='CMS'):
    """Display histograms."""
    try:
        return render_template(
            'cernopendata_pages/visualise_histograms.html',
            experiment=experiment,
        )
    except TemplateNotFound:
        return abort(404)


@blueprint.route('/resources/articles')
@register_breadcrumb(blueprint, '.index', _('Learning Resources'))
def resources_articles():
    """Render index of articles resources."""
    url = '/api/articles'

    return render_template('cernopendata_pages/faceted_page.html',
                           search_endpoint=url)


# @blueprint.route('/VM')
# @blueprint.route('/VM/')
# @register_breadcrumb(blueprint, '.vm', _('Virtual Machines'))
# def vm():
#     """Display experiment VMs."""
#     return render_template('cernopendata_pages/vm/index.html')
#
#
# @blueprint.route('/VM/<string:experiment>', defaults={'year': None})
# @blueprint.route('/VM/<string:experiment>/<string:year>')
# @register_breadcrumb(blueprint, '.vm.experiment',
#                      lazy_title('%(experiment)s', 'experiment'),
#                      endpoint_arguments_constructor=lambda: {
#                          'experiment': request.view_args['experiment']})
# def vm_experiment(experiment, year):
#     """Display details about experiment VMs."""
#     return render_template(
#         'cernopendata/vm/experiment_{0}.html'.format(experiment.lower()),
#         year=year,
#     )
#
#
# @blueprint.route('/VM/<string:experiment>/validation/report')
# @register_breadcrumb(blueprint, '.vm.validation_report',
#                      lazy_title('%(experiment)s Validation Report',
#                                 'experiment'),
#                      endpoint_arguments_constructor=lambda: {
#                          'experiment': request.view_args['experiment']})
# def validation_report(experiment):
#     """Display default abourt experiment validation report."""
#     return render_template([
#         'cernopendata/vm/validation_{0}.html'.format(experiment.lower()),
#         'cernopendata/vm/validation.html',
#     ], experiment=experiment)


def about_menu(*args):
    """Generate menu decorator."""
    def decorator(f):
        """Menu decorator."""
        for order, key in enumerate(args):
            def arguments(key):
                return lambda: {'page': key}

            f = register_menu(
                blueprint, 'main.about.{0}'.format(key),
                _('%(experiment)s Open Data', experiment=key), order=order + 1,
                endpoint_arguments_constructor=arguments(key)
            )(f)
        return f

    return decorator


def about_breadcrumbs():
    """Generate breadcrumbs for about pages."""
    key = request.view_args.get('page')
    breadcrumbs = [{'url': url_for('cernopendata.about'), 'text': _('About')}]
    if key:
        breadcrumbs.append({
            'url': url_for('cernopendata.about', experiment=key),
            'text': _('%(experiment)s Open Data', experiment=key),
        })
    return breadcrumbs


@blueprint.route('/about')
@register_breadcrumb(blueprint, '.about', _('About'))
def about():
    """Render view for general about page."""
    return render_template('cernopendata_pages/about/index.html')


@blueprint.route('/about/alice')
@register_breadcrumb(blueprint, '.about.about_alice', _('ALICE'))
def about_alice():
    """Render about ALICE template."""
    return render_template('cernopendata_pages/about/about_alice.html')


@blueprint.route('/about/atlas')
@register_breadcrumb(blueprint, '.about.about_atlas', _('ATLAS'))
def about_atlas():
    """Render about atlas template."""
    return render_template('cernopendata_pages/about/about_atlas.html')


@blueprint.route('/about/cms')
@register_breadcrumb(blueprint, '.about.about_cms', 'CMS')
def about_cms():
    """Render about cms template."""
    return render_template('cernopendata_pages/about/about_cms.html')


@blueprint.route('/about/cms-pileup-simulation')
@register_breadcrumb(blueprint, '.about.about_cms.about_cms_pileup',
                     'Pileup Simulation')
def cms_pileup_simulation():
    """Render cms pileup simulation template."""
    return render_template(
        'cernopendata_pages/about/cms_pileup_simulation.html')


@blueprint.route('/about/cms-simulated-dataset-names')
@register_breadcrumb(blueprint, '.about.about_cms.about_cms_dataset_names',
                     'Simulated Dataset Names')
def about_cms_dataset_names():
    """Render about CMS simulated dataset names template."""
    return render_template('cernopendata_pages/about/cms_dataset_names.html')


@blueprint.route('/about/lhcb')
@register_breadcrumb(blueprint, '.about.about_lhcb', _('LHCb'))
def about_lhcb():
    """Render about lhcb template."""
    return render_template('cernopendata_pages/about/about_lhcb.html')


@blueprint.route('/about/opera')
@register_breadcrumb(blueprint, '.about.about_opera', _('OPERA'))
def about_opera():
    """Render about opera template."""
    return render_template('cernopendata_pages/about/about_opera.html')


@blueprint.route('/terms-of-use')
@register_breadcrumb(blueprint, '.terms', _('Terms of Use'))
def terms():
    """Render terms of use."""
    return render_template('cernopendata_pages/terms_of_use.html')


@blueprint.route('/privacy-policy')
@register_breadcrumb(blueprint, '.privacy', _('Privacy Policy'))
def privacy():
    """Render privacy policy."""
    return render_template('cernopendata_pages/privacy_policy.html')


@blueprint.route('/experiments')
def collections():
    """Display experiments."""
    import json
    import pkg_resources
    filepath = pkg_resources.resource_filename(
        'cernopendata.base', 'templates/helpers/text/testimonials.json')
    with open(filepath, 'r') as f:
        testimonials = json.load(f)

    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting

    exp_colls, exp_names = get_collections()

    return render_template(
        'index_scrollspy.html',
        testimonials=testimonials,
        exp_colls=exp_colls,
        exp_names=exp_names)


@blueprint.route('/glossary')
@register_breadcrumb(blueprint, '.about.glossary', _('Glossary'))
def glossary():
    """Display glossary terms."""
    return render_template('cernopendata/glossary_terms.html')


@blueprint.route('/glossary/json')
def glossary_json():
    """Fetch glossary json."""
    filepath = pkg_resources.resource_filename(
        'cernopendata.modules.fixtures', 'data/terms/terms.json')
    with open(filepath, 'r') as f:
        glossary = json.load(f)
    return jsonify(glossary)


@blueprint.route('/collection'
                 '/<any("cms","lhcb","opera","alice","atlas","data-policies")'
                 ':collection>')
@blueprint.route('/<any("getting-started","vm","news"):page>')
@blueprint.route('/<any("getting-started"):page>'
                 '/<any("cms","lhcb","opera","alice","atlas"):experiment>')
def faceted_search(page=None, experiment=None, collection=None):
    """Faceted search view.

    To add a new page:
        add url to blueprint.route
        add mapping, which (filter,val) should be use to filter record
    """
    facets = [x for x in locals().values() if x]

    filter_map = {
        'getting-started': ('tags_pre', 'Getting Started'),
        'news': ('type_pre', 'News'),
        'vm': ('tags_pre', 'VM'),
        'data-policies': ('subtype_pre', 'Data policy'),
        'cms': ('experiment_pre', 'CMS'),
        'alice': ('experiment_pre', 'ALICE'),
        'atlas': ('experiment_pre', 'ATLAS'),
        'lhcb': ('experiment_pre', 'LHCb'),
    }

    filters = {}
    for facet in facets:
        _filter = filter_map.get(facet) or abort(404)
        filters[_filter[0]] = _filter[1]

    description = descriptions.get(collection, None)
    url = '/api/records?' + urllib.urlencode(filters)

    return render_template('cernopendata_pages/faceted_page.html',
                           search_endpoint=url,
                           description=description)
