# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2011, 2012, 2013 CERN.
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

"""Regression tests for the search engine summarizer."""

from invenio.testsuite import make_test_suite, run_test_suite, InvenioTestCase
from intbitset import intbitset
from invenio.base.wrappers import lazy_import


class WebSearchSummarizerTests(InvenioTestCase):
    """Test utility functions for search engine summarizer."""

    def test_basic(self):
        summarize_records = lazy_import('invenio.legacy.search_engine.summarizer:summarize_records')
        #FIXME
        summarize_records(intbitset(range(1, 100)), 'hcs', 'en')

    def test_xml(self):
        summarize_records = lazy_import('invenio.legacy.search_engine.summarizer:summarize_records')
        summarize_records(intbitset(range(1, 100)), 'xcs', 'en')


TEST_SUITE = make_test_suite(WebSearchSummarizerTests)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
