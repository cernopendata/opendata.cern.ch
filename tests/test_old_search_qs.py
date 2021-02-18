# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2021 CERN.
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

import pytest

from cernopendata.config import RECORDS_REST_FACETS
from cernopendata.views import translate_search_url


@pytest.mark.parametrize(
    "old_qs_args,new_qs_args",
    [
        ({"type": ["Documentation"]}, {"f": ["type:Documentation"]}),
        (
            {"type": ["Environment"], "category": ["Exotica"]},
            {"f": ["type:Environment", "category:Exotica"]},
        ),
        (
            {"type": ["Dataset"], "subtype": ["Derived"]},
            {"f": ["type:Dataset+subtype:Derived"]},
        ),
        (
            {"type": ["Dataset", "Documentation"], "subtype": ["Simulated", "Guide"]},
            {
                "f": [
                    "type:Dataset+subtype:Simulated",
                    "type:Documentation+subtype:Guide",
                ]
            },
        ),
        (
            {
                "type": ["Dataset", "Documentation"],
                "subtype": ["Help", "Simulated", "Guide"],
            },
            {
                "f": [
                    "type:Dataset+subtype:Simulated",
                    "type:Documentation+subtype:Guide",
                    "type:Documentation+subtype:Help",
                ]
            },
        ),
        (
            {"type": ["Dataset", "Documentation"], "subtype": ["Help", "Guide"]},
            {
                "f": [
                    "type:Dataset",
                    "type:Documentation+subtype:Guide",
                    "type:Documentation+subtype:Help",
                ]
            },
        ),
        (
            {"type": ["Environment"], "subtype": ["VM"], "experiment": ["CMS"]},
            {"f": ["type:Environment+subtype:VM", "experiment:CMS"]},
        ),
        (
            {"experiment": ["CMS", "ATLAS"]},
            {"f": ["experiment:CMS", "experiment:ATLAS"]},
        ),
        ({"q": ["foo"]}, {"q": ["foo"], "f": []}),
        ({"foo": ["bar", "baz"]}, {"foo": ["bar", "baz"], "f": []}),
        ({"q": ["foo"], "type": ["Software"]}, {"q": ["foo"], "f": ["type:Software"]}),
    ],
)
def test_old_search_qs(old_qs_args, new_qs_args):
    """Test translation from old search querystring args to new ones."""
    translated_qs = translate_search_url(old_qs_args, RECORDS_REST_FACETS)
    # compare facets no matter the order
    assert set(translated_qs.pop('f')) == set(new_qs_args.pop('f'))
    # compare rest of query params
    assert translated_qs == new_qs_args
