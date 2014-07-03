# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2010, 2011, 2013 CERN.
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

"""Unit tests for the invenio_connector script."""

__revision__ = "$Id$"

import os

from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.testsuite import InvenioTestCase, make_test_suite, run_test_suite

InvenioConnector = lazy_import('invenio.utils.connector:InvenioConnector')


class InvenioConnectorTest(InvenioTestCase):
    """Test function to get default values."""

    def test_local_search(self):
        """InvenioConnector - local search"""
        server = InvenioConnector(cfg['CFG_SITE_URL'])
        result = server.search(p='ellis', of='id')
        self.assertTrue(len(result) > 0, \
                        'did not get local search results.')

    def test_remote_search(self):
        """InvenioConnector - remote search"""
        server = InvenioConnector("http://invenio-demo.cern.ch")
        result = server.search(p='ellis', of='id')
        self.assertTrue(len(result) > 0, \
                        'did not get remote search results from http://invenio-demo.cern.ch')

    def test_search_collections(self):
        """InvenioConnector - collection search"""
        server = InvenioConnector(cfg['CFG_SITE_URL'])
        result = server.search(p='', c=['Books'], of='id')
        self.assertTrue(len(result) > 0, \
                        'did not get collection search results.')

    def test_search_local_restricted_collections(self):
        """InvenioConnector - local restricted collection search"""
        from invenio.utils.connector import InvenioConnectorAuthError
        server = InvenioConnector(cfg['CFG_SITE_URL'])
        search_params = dict(p='LBL-28106', c=['Theses'], of='id')
        self.assertRaises(InvenioConnectorAuthError, server.search, **search_params)
        #FIXME InvenioConnectorAuthError: You have to use a secure URL (HTTPS) to login
        server = InvenioConnector(cfg['CFG_SITE_SECURE_URL'], user='admin', password='')
        result = server.search(p='LBL-28106', c=['Theses'], of='id')
        self.assertTrue(len(result) > 0, \
                        'did not get restricted collection search results.')

    def test_search_remote_restricted_collections(self):
        """InvenioConnector - remote restricted collection search"""
        from invenio.utils.connector import InvenioConnectorAuthError
        server = InvenioConnector("http://invenio-demo.cern.ch")
        search_params = dict(p='LBL-28106', c=['Theses'], of='id')
        self.assertRaises(InvenioConnectorAuthError, server.search, **search_params)

        server = InvenioConnector("https://invenio-demo.cern.ch", user='jekyll', password='j123ekyll')
        result = server.search(p='LBL-28106', c=['Theses'], of='id')
        self.assertTrue(len(result) > 0, \
                        'did not get restricted collection search results.')

TEST_SUITE = make_test_suite(InvenioConnectorTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
