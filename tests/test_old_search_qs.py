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
        ({'type': ['foo']}, {'f': ['type:foo']}),
        (
            {'type': ['foo'], 'category': ['bar']},
            {'f': ['type:foo', 'category:bar']}
        ),
        (
            {'type': ['foo'], 'subtype': ['bar']},
            {'f': ['type:foo+subtype:bar']}
        ),
        (
            {'type': ['foo_a', 'foo_b'], 'subtype': ['bar_a', 'bar_b']},
            {'f': ['type:foo_a+subtype:bar_a', 'type:foo_b+subtype:bar_b' ]}
        ),
        (
            {'type': ['foo'], 'subtype': ['bar'], 'experiment': ['CMS']},
            {'f': ['type:foo+subtype:bar', 'experiment:CMS']}
        ),
        ({'q': ['foo']}, {'q': ['foo'], 'f': []}),
        ({'q': ['foo'], 'type': ['bar']}, {'q': ['foo'], 'f': ['type:bar']}),

    ]
)
def test_old_search_qs(old_qs_args, new_qs_args):
    """Test translation from old search querystring args to new ones."""
    assert translate_search_url(old_qs_args, RECORDS_REST_FACETS) == new_qs_args
