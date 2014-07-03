# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2010, 2011, 2013 CERN.
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

# pylint: disable=E1102

"""WebSession Regression Test Suite."""

__revision__ = \
    "$Id$"

from mechanize import Browser
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages, \
                              InvenioTestCase
from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import

run_sql = lazy_import('invenio.legacy.dbquery:run_sql')

class WebSessionWebPagesAvailabilityTest(InvenioTestCase):
    """Check WebSession web pages whether they are up or not."""

    def test_your_account_pages_availability(self):
        """websession - availability of Your Account pages"""

        baseurl = cfg['CFG_SITE_SECURE_URL'] + '/youraccount/'

        _exports = ['', 'edit', 'change', 'lost', 'display',
                    'send_email', 'youradminactivities',
                    'delete', 'logout', 'login', 'register']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url, username='admin',
                                                        expected_text=[]))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_your_groups_pages_availability(self):
        """websession - availability of Your Groups pages"""

        baseurl = cfg['CFG_SITE_SECURE_URL'] + '/yourgroups/'

        _exports = ['', 'display', 'create', 'join', 'leave', 'edit', 'members']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url, username='admin',
                                                        expected_text=[]))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

class WebSessionLostYourPasswordTest(InvenioTestCase):
    """Test Lost Your Passwords functionality."""

    def test_lost_your_password_for_internal_accounts(self):
        """websession - sending lost password for internal admin account"""

        try_with_account = cfg['CFG_SITE_ADMIN_EMAIL'].encode('utf8')

        # click on "send lost password" for cfg['CFG_SITE_ADMIN_EMAIL'] internal account
        browser = Browser()
        browser.open(cfg['CFG_SITE_SECURE_URL'] + "/youraccount/lost")
        browser.select_form(nr=0)
        browser['email'] = try_with_account
        try:
            browser.submit()
        except Exception, e:
            # Restore the admin password (send_email set it to random number)
            run_sql("UPDATE user SET password=AES_ENCRYPT(email, '')"
                "WHERE id=1")
            self.fail("Obtained %s: probably the email server is not installed "
                "correctly." % e)



        # verify the response:
        expected_response = "A password reset link has been sent to " + \
                            try_with_account
        lost_password_response_body = browser.response().read()
        try:
            lost_password_response_body.index(expected_response)
        except ValueError:
            # Restore the admin password (send_email set it to random number)
            run_sql("UPDATE user SET password=AES_ENCRYPT(email, '')"
                "WHERE id=1")
            self.fail("Expected to see %s, got %s." % \
                      (expected_response, lost_password_response_body))

    def tearDown(self):
        # Restore the admin password (send_email set it to random number)
        run_sql("UPDATE user SET password=AES_ENCRYPT(email, '')"
            "WHERE id=1")

TEST_SUITE = make_test_suite(WebSessionWebPagesAvailabilityTest,
                             WebSessionLostYourPasswordTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
