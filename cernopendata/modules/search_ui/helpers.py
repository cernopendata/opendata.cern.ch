# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2021 CERN.
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

"""CERN Open Data Invenio-Search-UI helpers."""

from flask import current_app
from invenio_search_ui.views import SearchAppInvenioRestConfigHelper


class CODSearchAppInvenioRestConfigHelper(SearchAppInvenioRestConfigHelper):
    """Configuration generator for Invenio-Search-JS.

    Using the existing configuration from Invenio-Records-REST we can
    prefill most of the needed information required for the initialisation
    of SearchApp.
    """

    @property
    def aggs(self):
        """Format the aggs configuration to be used in React-SearchKit JS.

        Overridden to support multiple ES aggregation types.
        :returns: A list of dicts for React-SearchKit JS.
        """
        search_index = self._rest_config["search_index"]
        aggs = (
            current_app.config.get("RECORDS_REST_FACETS", {})
            .get(search_index, {})
            .get("aggs", {})
        )
        agg_list = []
        for agg_name, agg_definition in aggs.items():
            item = dict(title=None, agg=None)
            for k, v in agg_definition.items():
                # sub-aggs
                if k == "aggs":
                    name = list(v.keys())[0]
                    definition = list(v.values())[0]
                    field = list(definition.values())[0].get("field")
                    item["agg"]["childAgg"] = {"aggName": name, "field": field}
                else:
                    item.update(
                        {
                            "title": agg_name.capitalize().replace("_", " "),
                            "agg": {"aggName": agg_name, "field": v.get("field")},
                        }
                    )
            agg_list.append(item)
        return agg_list
