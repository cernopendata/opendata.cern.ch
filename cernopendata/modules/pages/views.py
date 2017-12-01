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

import pkg_resources
from flask import Blueprint, abort, current_app, escape, jsonify, redirect, \
    render_template, request, url_for
from flask_babelex import lazy_gettext as _
from flask_breadcrumbs import default_breadcrumb_root, register_breadcrumb
from flask_menu import register_menu
from jinja2.exceptions import TemplateNotFound
from speaklater import make_lazy_string

from .utils import FeaturedArticlesSearch

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
    results = FeaturedArticlesSearch().sort('featured')[:6].execute()
    return render_template('cernopendata_pages/front/index.html',
                           featured_articles=results.hits.hits)


@blueprint.route('/md/debug', methods=['HEAD', 'GET'])
def md_debug():
    """Test Markdown rendering of a page.

    Route for quicker previewing markdown during development.
    During edit replace contents of `cernopendata/static/test_data/debug.md`
    and just refresh the view.
    I.e. there is no need to re-populate db every time a change is made.

    Command `cernopendata collect -v` has to be run everytime
    there is a change in static resources.

    """
    f = open('cernopendata/static/test_data/debug.md', 'r')
    # return render_template_string(
    #     u"{{ text|markdown }}", text=f.read().decode("utf-8"))
    return render_template('cernopendata_pages/md_template.html',
                           content=f.read().decode("utf-8"))


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
def visualise_events(experiment='cms', eventid=None):
    """Display visualisations."""
    try:
        return render_template(
            'cernopendata_pages/visualise_events_{}.html'.format(
                experiment),
            eventid=eventid,
            experiment=experiment,
        )
    except TemplateNotFound:
        return abort(404)


@blueprint.route('/visualise/histograms')
@blueprint.route('/visualise/histograms/<string:experiment>')
@register_breadcrumb(blueprint, '.visualise_histograms',
                     _('Visualise Histograms'))
def visualise_histograms(experiment='cms'):
    """Display histograms."""
    try:
        return render_template(
            'cernopendata_pages/visualise_histograms.html',
            experiment=experiment,
        )
    except TemplateNotFound:
        return abort(404)


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
def about():
    """Render view for general about page."""
    return redirect('/docs/cern-open-data-portal')


@blueprint.route('/about/<exp>')
def about_exp(exp):
    """Render about <experiment> pages."""
    return redirect('/docs/about-{}'.format(exp))


@blueprint.route('/about/cms-pileup-simulation')
def cms_pileup_simulation():
    """Render cms pileup simulation template."""
    return redirect('/docs/cms-pile-up-simulation')


@blueprint.route('/about/cms-simulated-dataset-names')
@register_breadcrumb(blueprint, '.about.about_cms.about_cms_dataset_names',
                     'Simulated Dataset Names')
def about_cms_dataset_names():
    """Render about CMS simulated dataset names template."""
    return render_template('cernopendata_pages/about/cms_dataset_names.html')


@blueprint.route('/getting-started/<exp>')
def getting_started_redirect(exp):
    """Redirects to associated experiment."""
    return redirect('/docs/getting-started-with-%s-open-data' % exp,
                    code=302)


@blueprint.route('/vm/<exp>/<year>')
def vm_redirect(exp, year):
    """Redirects to associated experiment."""
    if year:
        return redirect(
            '/docs/%s-%s-virtual-machines-how-to-install' % (exp, year),
            code=302)
    return redirect('/docs/%s-virtual-machines-how-to-install' % exp,
                    code=302)


@blueprint.route('/cms-physics-objects/')
@blueprint.route('/cms-physics-objects/<year>')
@blueprint.route('/about/cms-physics-objects/')
@blueprint.route('/about/cms-physics-objects/<year>')
def cms_physics_objects_redirect(year='2011'):
    """Redirects to CMS physics objects page of given year.

    If no year is given, redirects to latest available
    physics objects page (the default parameter).
    """
    return redirect('/docs/cms-physics-objects-{}'.format(year), code=302)


@blueprint.route('/terms-of-use')
@register_breadcrumb(blueprint, '.terms', _('Terms of Use'))
def terms():
    """Render terms of use."""
    return render_template('cernopendata_pages/terms_of_use.html')


@blueprint.route('/privacy-policy')
@register_breadcrumb(blueprint, '.about.privacy', _('Privacy Policy'))
def privacy():
    """Render privacy policy."""
    return render_template('cernopendata_pages/privacy_policy.html')


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


@blueprint.route('/collection/<string:collection>')
@blueprint.route('/<any("getting-started","vm","news",'
                 '"datasets","documentation","software"):page>')
@blueprint.route('/<any("getting-started","vm"):page>'
                 '/<any("cms","lhcb","opera","alice","atlas"):experiment>')
def faceted_search(page=None, experiment=None, collection=None):
    """Faceted search view.

    To add a new page:
        add url to blueprint.route
        add mapping, which (filter,val,search_endpoint)
            should be used to filter records

    """
    facets = [x for x in locals().values() if x]
    filters = {}

    filter_map = {
        'documentation': ('type', 'Documentation'),
        'software': ('type', 'Software'),
        'datasets': ('type', 'Dataset'),
        'getting-started': ('tags', 'Getting Started'),
        'news': ('type', 'News'),
        'vm': ('tags', 'VM'),
        'cms': ('experiment', 'CMS'),
        'alice': ('experiment', 'ALICE'),
        'atlas': ('experiment', 'ATLAS'),
        'lhcb': ('experiment', 'LHCb'),
        'opera': ('experiment', 'OPERA'),
        'data-policies': ('collections', 'Data-Policies'),
        'alice-derived-datasets': ('collections',
                                   'ALICE-Derived-Datasets'),
        'alice-reconstructed-data': ('collections',
                                     'ALICE-Reconstructed-Data'),
        'alice-learning-resources': ('collections',
                                     'ALICE-Learning-Resources'),
        'alice-tools': ('collections', 'ALICE-Tools'),
        'atlas-derived-datasets': ('collections',
                                   'ATLAS-Derived-Datasets'),
        'atlas-higgs-challenge-2014': ('collections',
                                       'ATLAS-Higgs-Challenge-2014'),
        'atlas-simulated-datasets': ('collections',
                                     'ATLAS-Simulated-Datasets'),
        'atlas-learning-resources': ('collections',
                                     'ATLAS-Learning-Resources'),
        'atlas-tools': ('collections', 'ATLAS-Tools'),
        'author-lists': ('collections', 'Author-Lists'),
        'cms-condition-data': ('collections', 'CMS-Condition-Data'),
        'cms-configuration-files': ('collections',
                                    'CMS-Configuration-Files'),
        'cms-derived-datasets': ('collections', 'CMS-Derived-Datasets'),
        'cms-luminosity-information': ('collections',
                                       'CMS-Luminosity-Information'),
        'cms-open-data-instructions': ('collections',
                                       'CMS-Open-Data-Instructions'),
        'cms-learning-resources': ('collections', 'CMS-Learning-Resources'),
        'cms-primary-datasets': ('collections', 'CMS-Primary-Datasets'),
        'cms-simulated-datasets': ('collections',
                                   'CMS-Simulated-Datasets'),
        'cms-tools': ('collections', 'CMS-Tools'),
        'cms-trigger-information': ('collections', 'CMS-Trigger-Information'),
        'cms-validated-runs': ('collections', 'CMS-Validated-Runs'),
        'cms-validation-utilities': ('collections',
                                     'CMS-Validation-Utilities'),
        'lhcb-derived-datasets': ('collections', 'LHCb-Derived-Datasets'),
        'lhcb-learning-resources': ('collections',
                                    'LHCb-Learning-Resources'),
        'lhcb-tools': ('collections', 'LHCb-Tools'),
        'opera-detector-events': ('collections', 'OPERA-Detector-Events'),
        'opera-electronic-detector-datasets': (
            'collections',
            'OPERA-Electronic-Detector-Datasets'),
        'opera-emulsion-detector-datasets': (
            'collections',
            'OPERA-Emulsion-Detector-Datasets')
    }

    for facet in facets:
        _filter = filter_map.get(facet) or abort(404)
        filters[_filter[0]] = _filter[1]

    return redirect(url_for('invenio_search_ui.search', **filters))


@blueprint.route('/<any("research","education"):page>')
@blueprint.route('/<any("research","education"):page>'
                 '/<any("cms","lhcb","opera","alice","atlas"):experiment>')
def education_research_pages(page, experiment=None):
    """Research and education pages."""
    collections = {
        'research': {'cms': ['CMS-Primary-Datasets',
                             'CMS-Simulated-Datasets',
                             'CMS-Derived-Datasets',
                             'CMS-Tools',
                             'CMS-Validation-Utilities',
                             'CMS-Learning-Resources',
                             'CMS-Simulated-Datasets',
                             'CMS-Open-Data-Instructions',
                             'CMS-Trigger-Information',
                             'CMS-Condition-Data',
                             'CMS-Configuration-Files',
                             'CMS-Luminosity-Information'
                             ]
                     },
        'education': {'cms': ['CMS-Derived-Datasets',
                              'CMS-Tools',
                              'CMS-Learning-Resources',
                              'CMS-Open-Data-Instructions'
                              ],
                      'alice': ['ALICE-Derived-Datasets',
                                'ALICE-Reconstructed-Data',
                                'ALICE-Tools',
                                'ALICE-Learning-Resources'
                                ],
                      'atlas': ['ATLAS-Derived-Datasets',
                                'ATLAS-Learning-Resources',
                                'ATLAS-Tools',
                                'ATLAS-Higgs-Challenge-2014',
                                'ATLAS-Simulated-Datasets'
                                ],
                      'lhcb': ['LHCb-Derived-Datasets',
                               'LHCb-Tools',
                               'LHCb-Learning-Resources'
                               ],
                      'opera': [
                          'OPERA-Detector-Events',
                          'OPERA-Electronic-Detector-Datasets',
                          'OPERA-Emulsion-Detector-Datasets'
        ]
        }
    }

    collections = collections.get(page)

    if not experiment:
        # use collections defined for all experiments
        filters = {'collections': sum([v for k, v in collections.items()], [])}
    else:
        filters = {'collections': collections.get(experiment) or abort(404)}

    return redirect(url_for('invenio_search_ui.search', **filters))
