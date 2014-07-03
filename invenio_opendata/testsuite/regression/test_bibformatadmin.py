# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011 CERN.
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

"""BibFormat Admin Regression Test Suite."""

__revision__ = "$Id$"

from invenio.testsuite import InvenioTestCase

from invenio.base.globals import cfg
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages


class BibFormatAdminWebPagesAvailabilityTest(InvenioTestCase):
    """Check BibFormat Admin web pages whether they are up or not."""

    def test_bibformat_admin_interface_availability(self):
        """bibformatadmin - availability of BibFormat Admin interface pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/admin/bibformat/'

        _exports = ['bibformatadmin.py/format_templates_manage',
                    'bibformatadmin.py/output_formats_manage',
                    'bibformatadmin.py/format_elements_doc']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            # first try as guest:
            error_messages.extend(test_web_page_content(url,
                                                        username='guest',
                                                        expected_text=
                                                        'Authorization failure'))
            # then try as admin:
            error_messages.extend(test_web_page_content(url,
                                                        username='admin'))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_bibformat_admin_guide_availability(self):
        """bibformatadmin - availability of BibFormat Admin guide pages"""

        url = cfg['CFG_SITE_URL'] + '/help/admin/bibformat-admin-guide'
        error_messages = test_web_page_content(url,
                                               expected_text="BibFormat Admin Guide")
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

TEST_SUITE = make_test_suite(BibFormatAdminWebPagesAvailabilityTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
