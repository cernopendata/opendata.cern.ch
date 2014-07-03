# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2009, 2010, 2011, 2012 CERN.
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

"""OAIArchive Admin Regression Test Suite."""

__revision__ = "$Id$"

from invenio.testsuite import InvenioTestCase

from invenio.base.globals import cfg
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages


class OAIRepositoryAdminWebPagesAvailabilityTest(InvenioTestCase):
    """Check OAI Repository Admin web pages whether they are up or not."""

    def test_oairepositoryadmin_interface_pages_availability(self):
        """oairepositoryadmin - availability of OAI Repository Admin interface pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/admin/oairepository/oairepositoryadmin.py/'

        _exports = ['', 'delset', 'editset', 'addset']

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

    def test_oairepositoryadmin_edit_set(self):
        """oairepositoryadmin - edit set page"""
        test_edit_url = cfg['CFG_SITE_URL'] + \
               "/admin/oairepository/oairepositoryadmin.py/editset?oai_set_id=2"
        error_messages = test_web_page_content(test_edit_url,
                                               username='admin')
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_oairepositoryadmin_delete_set(self):
        """oairepositoryadmin - delete set page"""
        test_edit_url = cfg['CFG_SITE_URL'] + \
               "/admin/oairepository/oairepositoryadmin.py/delset?oai_set_id=2"
        error_messages = test_web_page_content(test_edit_url,
                                               username='admin')
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

TEST_SUITE = make_test_suite(OAIRepositoryAdminWebPagesAvailabilityTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
