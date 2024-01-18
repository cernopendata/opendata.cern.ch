# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017, 2018 CERN.
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

import json

import pkg_resources
from flask import (
    Blueprint,
    Response,
    abort,
    current_app,
    escape,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_breadcrumbs import default_breadcrumb_root
from invenio_i18n import lazy_gettext as _
from jinja2.exceptions import TemplateNotFound
from speaklater import make_lazy_string

from .utils import FeaturedArticlesSearch

blueprint = Blueprint(
    "cernopendata_pages",
    __name__,
    template_folder="templates",
    static_folder="static",
)

default_breadcrumb_root(blueprint, ".")


@blueprint.errorhandler(TemplateNotFound)
def template_not_found(err):
    """Log missing template."""
    current_app.logger.exception("Please check missing template.")
    abort(404)
    # return 'Template not found!', 404


def lazy_title(text, *args):
    """Make tranlated string with escaped values from request view args."""
    return _(
        text,
        **{
            key: make_lazy_string(lambda: escape(request.view_args.get(key, "")))
            for key in args
        }
    )


@blueprint.route("/")
def index():
    """Home Page."""
    results = []
    try:
        results = FeaturedArticlesSearch().sort("featured")[:6].execute().hits.hits
    except Exception:
        pass
    return render_template(
        "cernopendata_pages/front/index.html", featured_articles=results
    )


@blueprint.route("/robots.txt")
def robots():
    """Render robots page."""
    with open("cernopendata/templates/cernopendata_pages/robots.txt") as f:
        return Response(f.read(), mimetype="text/plain")


@blueprint.route("/md/debug", methods=["HEAD", "GET"])
def md_debug():
    """Test Markdown rendering of a page.

    Route for quicker previewing markdown during development.
    During edit replace contents of `cernopendata/static/test_data/debug.md`
    and just refresh the view.
    I.e. there is no need to re-populate db every time a change is made.

    If DEBUG is not set this will redirect to homepage.

    Command `cernopendata collect -v` has to be run everytime
    there is a change in static resources.

    """
    if current_app.config.get("DEBUG"):
        f = open("cernopendata/static/test_data/debug.md", "r")
        # return render_template_string(
        #     u"{{ text|markdown }}", text=f.read().decode("utf-8"))
        return render_template(
            "cernopendata_pages/md_template.html", content=f.read().decode("utf-8")
        )
    else:
        return redirect("/")


@blueprint.route("/visualise/events")
# @register_breadcrumb(blueprint, '.visualise_events', _('Visualise Events'))
def visualise_events_landing():
    """Display landing page."""
    try:
        return render_template("cernopendata_pages/visualise_events.html")
    except TemplateNotFound:
        return abort(404)


@blueprint.route("/visualise/events/<string:experiment>")
@blueprint.route("/visualise/events/<string:experiment>/<int:eventid>")
# @register_breadcrumb(blueprint, '.visualise_events', _('Visualise Events'))
def visualise_events(experiment="cms", eventid=None):
    """Display visualisations."""
    # if experiment == 'opera':
    #     abort(404)
    try:
        return render_template(
            "cernopendata_pages/visualise_events_{}.html".format(experiment),
            eventid=eventid,
            experiment=experiment,
        )
    except TemplateNotFound:
        return abort(404)


@blueprint.route("/visualise/histograms")
@blueprint.route("/visualise/histograms/<string:experiment>")
# @register_breadcrumb(blueprint, '.visualise_histograms',
#                      _('Visualise Histograms'))
def visualise_histograms(experiment="cms"):
    """Display histograms."""
    try:
        return render_template(
            "cernopendata_pages/visualise_histograms.html",
            experiment=experiment,
        )
    except TemplateNotFound:
        return abort(404)


# FIXME quick fix
@blueprint.route("/record/<recid>/")
def record_redirect(recid):
    """Redirect to deal with trailing slash."""
    return redirect("/record/{}".format(recid))


@blueprint.route("/glossary")
def glossary():
    """Display glossary terms."""
    return redirect("/search?f=type%3AGlossary&sort=title")


@blueprint.route("/glossary/json")
def glossary_json():
    """Fetch glossary json."""
    filepath = pkg_resources.resource_filename(
        "cernopendata.modules.fixtures", "data/terms/terms.json"
    )
    with open(filepath, "r") as f:
        glossary = json.load(f)
    return jsonify(glossary)


@blueprint.route("/experiments")
@blueprint.route("/resources")
@blueprint.route("/research")
@blueprint.route("/research" '/<any("lhcb","alice","atlas"):experiment>')
@blueprint.route("/resources" '/<any("cms","lhcb","alice","atlas"):experiment>')
@blueprint.route("/collection/<string:collection>")
@blueprint.route(
    '/<any("getting-started","getstarted", "vm","news",'
    '"datasets","documentation","software"):page>'
)
@blueprint.route(
    '/<any("getting-started","getstarted","vm"):page>'
    '/<any("opera", "atlas"):experiment>'
)
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
        "documentation": ("type", "Documentation"),
        "software": ("type", "Software"),
        "datasets": ("type", "Dataset"),
        "getting-started": ("tags", "Getting Started"),
        "getstarted": ("tags", "Getting Started"),
        "news": ("type", "News"),
        "vm": ("tags", "VM"),
        "cms": ("experiment", "CMS"),
        "alice": ("experiment", "ALICE"),
        "atlas": ("experiment", "ATLAS"),
        "lhcb": ("experiment", "LHCb"),
        "opera": ("experiment", "OPERA"),
        "data-policies": ("collections", "Data-Policies"),
        "alice-derived-datasets": ("collections", "ALICE-Derived-Datasets"),
        "alice-reconstructed-data": ("collections", "ALICE-Reconstructed-Data"),
        "alice-learning-resources": ("collections", "ALICE-Learning-Resources"),
        "alice-tools": ("collections", "ALICE-Tools"),
        "atlas-derived-datasets": ("collections", "ATLAS-Derived-Datasets"),
        "atlas-higgs-challenge-2014": ("collections", "ATLAS-Higgs-Challenge-2014"),
        "atlas-simulated-datasets": ("collections", "ATLAS-Simulated-Datasets"),
        "atlas-learning-resources": ("collections", "ATLAS-Learning-Resources"),
        "atlas-tools": ("collections", "ATLAS-Tools"),
        "author-lists": ("collections", "Author-Lists"),
        "cms-condition-data": ("collections", "CMS-Condition-Data"),
        "cms-configuration-files": ("collections", "CMS-Configuration-Files"),
        "cms-derived-datasets": ("collections", "CMS-Derived-Datasets"),
        "cms-luminosity-information": ("collections", "CMS-Luminosity-Information"),
        "cms-open-data-instructions": ("collections", "CMS-Open-Data-Instructions"),
        "cms-learning-resources": ("collections", "CMS-Learning-Resources"),
        "cms-primary-datasets": ("collections", "CMS-Primary-Datasets"),
        "cms-simulated-datasets": ("collections", "CMS-Simulated-Datasets"),
        "cms-tools": ("collections", "CMS-Tools"),
        "cms-trigger-information": ("collections", "CMS-Trigger-Information"),
        "cms-validated-runs": ("collections", "CMS-Validated-Runs"),
        "cms-validation-utilities": ("collections", "CMS-Validation-Utilities"),
        "lhcb-derived-datasets": ("collections", "LHCb-Derived-Datasets"),
        "lhcb-learning-resources": ("collections", "LHCb-Learning-Resources"),
        "lhcb-tools": ("collections", "LHCb-Tools"),
        "opera-detector-events": ("collections", "OPERA-Detector-Events"),
        "opera-electronic-detector-datasets": (
            "collections",
            "OPERA-Electronic-Detector-Datasets",
        ),
        "opera-emulsion-detector-datasets": (
            "collections",
            "OPERA-Emulsion-Detector-Datasets",
        ),
    }

    for facet in facets:
        _filter = filter_map.get(facet) or abort(404)
        filters[_filter[0]] = _filter[1]

    return redirect(url_for("invenio_search_ui.search", **filters))


@blueprint.route("/education")
@blueprint.route("/education" '/<any("lhcb","opera","alice","atlas"):experiment>')
def education_pages(experiment=None):
    """Education pages."""
    collections = {
        "education": {
            "alice": [
                "ALICE-Derived-Datasets",
                "ALICE-Reconstructed-Data",
                "ALICE-Tools",
                "ALICE-Learning-Resources",
            ],
            "atlas": [
                "ATLAS-Derived-Datasets",
                "ATLAS-Learning-Resources",
                "ATLAS-Tools",
                "ATLAS-Higgs-Challenge-2014",
                "ATLAS-Simulated-Datasets",
            ],
            "lhcb": ["LHCb-Derived-Datasets", "LHCb-Tools", "LHCb-Learning-Resources"],
            "opera": [
                "OPERA-Detector-Events",
                "OPERA-Electronic-Detector-Datasets",
                "OPERA-Emulsion-Detector-Datasets",
            ],
        }
    }

    collections = collections.get("education")

    if not experiment:
        # use collections defined for all experiments
        filters = {"collections": sum([v for k, v in collections.items()], [])}
    else:
        filters = {"collections": collections.get(experiment) or abort(404)}

    return redirect(url_for("invenio_search_ui.search", **filters))


@blueprint.route("/<path:path>/<int(fixed_digits=4):year>")
@blueprint.route("/<path:path>")
def redirect_old_urls(path, year=None):
    """Redirect old urls."""
    old_to_new_url_map = {
        "about": "docs/about",
        "about/cms": "/docs/about-cms",
        "about/cms-pileup-simulation": "/docs/cms-guide-pileup-simulation",
        "about/cms-simulated-dataset-names": "/docs/cms-simulated-dataset-names",
        "about/cms-physics-objects": "/docs/cms-physics-objects-{}".format(
            year or 2011
        ),
        "about/lhcb": "/docs/about-lhcb",
        "about/atlas": "/docs/about-atlas",
        "about/alice": "/docs/about-alice",
        "about/opera": "/docs/about-opera",
        "alice/getstarted": "/docs/alice-getting-started",
        "cms/getstarted": "/docs/cms-getting-started-{}".format(year or 2011),
        "cms-physics-objects": "/docs/cms-physics-objects-{}".format(year or 2011),
        "education/cms": "/docs/about-cms",
        "getstarted/cms": "/docs/cms-getting-started-{}".format(year or 2011),
        "getting-started/alice": "/docs/alice-getting-started",
        "getting-started/cms": "/docs/cms-getting-started-{}".format(year or 2011),
        "getting-started/lhcb": "/docs/lhcb-getting-started",
        "lhcb/getstarted": "/docs/lhcb-getting-started",
        "privacy-policy": "/docs/privacy-policy",
        "research/cms": "/docs/about-cms",
        "terms-of-use": "/docs/terms-of-use",
        "vm/alice": "/docs/alice-virtual-machine",
        "vm/cms": "/docs/cms-virtual-machine-{}".format(year or 2011),
        "vm/lhcb": "/docs/lhcb-virtual-machine",
        "vm/validation/report": "/docs/cms-vm-validation-2010",
        "vm/cms/validation/report": "/docs/cms-vm-validation-2010",
    }

    new_url = old_to_new_url_map.get(path) or abort(404)

    return redirect(new_url)
