# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2009, 2010, 2011, 2013 CERN.
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

"""BibCirculation Regression Test Suite."""

__revision__ = "$Id$"

from invenio.base.globals import cfg
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages, \
                              InvenioTestCase


class BibCirculationUsersWebPagesAvailabilityTest(InvenioTestCase):
    """Check BibCirculation web pages whether they are up or not."""

    def test_your_loans_page_availability(self):
        """bibcirculation - availability of your loans page"""

        baseurl = cfg['CFG_SITE_URL'] + '/yourloans/'

        _exports = ['', 'display', 'loanshistoricaloverview']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return


class BibCirculationAdminsWebPagesAvailabilityTest(InvenioTestCase):
    """Check BibCirculation web pages whether they are up or not for Admins."""

    def test_admin_pages_availability(self):
        """bibcirculation - availability of main admin page"""

        baseurl = cfg['CFG_SITE_URL'] + '/admin2/bibcirculation'

        self.assertEqual([], test_web_page_content(baseurl,
                                        expected_text="BibCirculation Admin"))

        return

    def test_borrower_search_availability(self):
        """bibcirculation - availability of borrower search"""

        baseurl = cfg['CFG_SITE_SECURE_URL'] + '/admin2/bibcirculation/' \
                              + 'borrower_search_result?column=name&string=john'

        self.assertEqual([], test_web_page_content(baseurl, username='admin',
                                        expected_text='Borrower search result'))

        return

    def test_item_search_availability(self):
        """bibcirculation - availability of item search"""

        baseurl = cfg['CFG_SITE_SECURE_URL'] + '/admin2/bibcirculation/' \
                              + 'item_search_result?f=barcode&p=bc-34001'

        self.assertEqual([], test_web_page_content(baseurl, username='admin',
                                        expected_text='Item details'))

        return

TEST_SUITE = make_test_suite(BibCirculationUsersWebPagesAvailabilityTest,
                             BibCirculationAdminsWebPagesAvailabilityTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
