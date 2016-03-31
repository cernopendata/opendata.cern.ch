# -*- coding: utf-8 -*-

"""cernopendata base Invenio configuration."""

from __future__ import absolute_import, print_function

import functools
import json
import pkg_resources

from flask import Blueprint, current_app, escape, render_template, request, url_for
from flask_babelex import lazy_gettext as _
from flask_breadcrumbs import default_breadcrumb_root, register_breadcrumb
from flask_menu import register_menu
from speaklater import make_lazy_string
from werkzeug import secure_filename


blueprint = Blueprint(
    'cernopendata',
    __name__,
    template_folder='templates',
    static_folder='static',
)

default_breadcrumb_root(blueprint, '.')


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
    return render_template('cernopendata/index.html')


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

    return render_template('cernopendata/education.html',
                           experiment=experiment)



@blueprint.route('/research')
@blueprint.route('/research/<string:experiment>')
@register_breadcrumb(blueprint, '.research.experiment',
                     lazy_title('%(experiment)s', 'experiment'),
                     endpoint_arguments_constructor=lambda: {
                         'experiment': request.view_args['experiment']})
def research(experiment=None):
    import os.path, pkg_resources

    def file_exists(filename):
        filepath = pkg_resources.resource_filename('cernopendata.base', filename)
        return os.path.isfile(filepath)

    def splitting(value, delimiter='/'):
        return value.split(delimiter)

    current_app.jinja_env.filters['splitthem'] = splitting
    current_app.jinja_env.filters['file_exists'] = file_exists

    exp_colls, exp_names = get_collections()

    if experiment not in exp_names :
        try:
            return render_template('index_scrollspy.html', entry = 'research', exp_colls = exp_colls, exp_names = exp_names)
        except TemplateNotFound:
            return abort(404)

    try:
        return render_template('research.html',
                               experiment=experiment, exp_colls = exp_colls, exp_names = exp_names)
    except TemplateNotFound:
        return abort(404)

@blueprint.route('/visualise/events/<string:experiment>')
def visualise_events(experiment = 'CMS'):

    exp_names = get_collection_names(['ALICE', 'LHCb', 'ATLAS'])

    breadcrumbs = [{},{'url':'.education','text':'Education'},\
                        {'url':'.education','text':'Visualise Events'}]
    try:
        return render_template('visualise_events.html', experiment = experiment, exp_names = exp_names, breadcrumbs = breadcrumbs)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('/visualise/histograms/<string:experiment>')
def visualise_histo(experiment='CMS'):
    exp_colls, exp_names = get_collections()

    breadcrumbs = [{}, {'url':'.education','text':'Education'},
                        {'url':'.education','text':'Visualise Histograms'}]

    try:
        return render_template('visualise_histograms.html', experiment = experiment, exp_names = exp_names, breadcrumbs = breadcrumbs)
    except TemplateNotFound:
        return abort(404)


@blueprint.route('/getstarted')
@blueprint.route('/<string:experiment>/getstarted')
@blueprint.route('/getstarted/<string:experiment>')
@blueprint.route('/getting-started')
@blueprint.route('/getting-started/<string:experiment>')
@blueprint.route('/getting-started/<string:experiment>/<string:year>')
@register_breadcrumb(blueprint, '.get_started', _('Get Started'))
def get_started(experiment=None, year=None):
    """Render getting started tutorials."""
    return render_template(
        'get_started.html', experiment=experiment, year=year
    )


@blueprint.route('/resources')
@register_breadcrumb(blueprint, '.education.resources',
                     _('Learning Resources'))
def resources():
    """Render index of resources."""
    return render_template('cernopendata/resources.html')


@blueprint.route('/VM', defaults={'experiment': None, 'year': None})
@blueprint.route('/VM/<string:experiment>', defaults={'year': None})
@blueprint.route('/VM/<string:experiment>/<string:year>')
@register_breadcrumb(blueprint, '.data_vms', 'Virtual Machines' , \
                        dynamic_list_constructor = (lambda :\
                        [{'url':'.data_vms','text':'Virtual Machines'}]) )
def data_vms(experiment, year):
    exp_names = get_collection_names(['ATLAS'])
    if experiment not in exp_names and experiment is not None:
        return render_template('404.html')

    def splitting(value, delimiter='/'):
        return value.split(delimiter)
    current_app.jinja_env.filters['splitthem'] = splitting

    try:
        return render_template('data_vms.html', experiment=experiment, exp_names=exp_names, year=year)
    except TemplateNotFound:
        return abort(404)

@blueprint.route('/VM/experiment/validation/report')
@register_breadcrumb(blueprint, '.val_report', 'VM', \
                        dynamic_list_constructor = (lambda :\
                        [{'url':'.data_vms','text':'Virtual Machines'},\
                        {'url':'.data_vms','text':'Validation Report'}]) )
def val_report(experiment):
    exp_names = get_collection_names()

    try:
        return render_template([experiment+'_VM_validation.html', 'data_vms.html'], experiment=experiment,exp_names=exp_names)
    except TemplateNotFound:
        return abort(404)


def about_menu(*args):
    """Generate menu decorator."""
    def decorator(f):
        for order, key in enumerate(args):
            def arguments(key):
                return lambda: {'page': key}
            f = register_menu(
                blueprint, 'main.about.{0}'.format(key),
                _('%(experiment)s Open Data', experiment=key), order=order+1,
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
@blueprint.route('/about/<page>')
@register_menu(blueprint, 'main.about', _('About'), order=1)
@register_menu(blueprint, 'main.about.this', _('This Portal'), order=0)
@about_menu('CMS', 'ALICE', 'ATLAS', 'LHCb')
@register_breadcrumb(blueprint, '.about', _('About'),
                     dynamic_list_constructor=about_breadcrumbs)
def about(page='index'):
    """Render about page."""
    return render_template([
        'cernopendata/about/{0}.html'.format(
            secure_filename(page.lower()).replace('/', '-')
        ),
        'cernopendata/about/index.html',
    ])


@blueprint.route('/terms-of-use')
@register_breadcrumb(blueprint, '.terms', _('Terms of Use'))
def terms():
    """Render terms of use."""
    return render_template('cernopendata/terms_of_use.html')


@blueprint.route('/privacy-policy')
@register_breadcrumb(blueprint, '.privacy', _('Privacy Policy'))
def privacy():
    """Render privacy policy."""
    return render_template('cernopendata/privacy_policy.html')


@blueprint.route('/experiments')
def collections():
    import json, pkg_resources
    filepath = pkg_resources.resource_filename('cernopendata.base', 'templates/helpers/text/testimonials.json')
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


@blueprint.route('/glossary', methods=['GET', 'POST'])
@register_menu(blueprint, 'main.about.glossary', _('Glossary'), order=90)
@register_breadcrumb(blueprint, '.education.glossary', _('Glossary'))
def glossary():
    """Display glossary."""
    filepath = pkg_resources.resource_filename(
        'cernopendata', 'static/json/glossary.json'
    )
    with open(filepath,'r') as f:
        glossary = json.load(f)

    return render_template('cernopendata/glossary.html', glossary=glossary)


@blueprint.route('/news')
@register_menu(blueprint, 'main.about.news', _('News'), order=91)
@register_breadcrumb(blueprint,'.news','News', dynamic_list_constructor=(
    lambda: [{'url':'.news','text':'News'}]
))
def news():
    """Render news."""
    return render_template('cernopendata/pages/news.html')
