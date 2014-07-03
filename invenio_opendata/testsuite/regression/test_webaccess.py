# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2013 CERN.
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

"""WebAccess Regression Test Suite."""

__revision__ = "$Id$"

import socket
import time
import cgi

from urlparse import urlparse, urlunparse
from urllib import urlopen, urlencode

from invenio.base.globals import cfg
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages, \
                              get_authenticated_mechanize_browser, \
                              InvenioTestCase
from invenio.base.wrappers import lazy_import
run_sql = lazy_import('invenio.legacy.dbquery:run_sql')


class WebAccessWebPagesAvailabilityTest(InvenioTestCase):
    """Check WebAccess web pages whether they are up or not."""

    def test_webaccess_admin_interface_availability(self):
        """webaccess - availability of WebAccess Admin interface pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/admin/webaccess/webaccessadmin.py/'

        _exports = ['', 'delegate_startarea', 'manageaccounts', 'rolearea',
                    'actionarea', 'userarea', 'managerobotlogin', 'listgroups',
                    'resetarea', '']

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

    def test_webaccess_admin_guide_availability(self):
        """webaccess - availability of WebAccess Admin guide pages"""

        url = cfg['CFG_SITE_URL'] + '/help/admin/webaccess-admin-guide'
        error_messages = test_web_page_content(url,
                                               expected_text="WebAccess Admin Guide")
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_webaccess_becomeuser(self):
        """webaccess - becomeuser functionality"""
        browser = get_authenticated_mechanize_browser("admin")
        browser.open(cfg['CFG_SITE_SECURE_URL'] + '/admin/webaccess/webaccessadmin.py/manageaccounts?mtype=perform_modifyaccounts')
        browser.select_form(nr=0)
        browser['email_user_pattern'] = 'romeo'
        browser.submit()
        browser.open(browser.find_link(text="Become user").absolute_url)
        self.failUnless('romeo' in browser.response().read())

class WebAccessFireRoleTest(InvenioTestCase):
    """Check WebAccess behaviour WRT FireRole."""

    def setUp(self):
        """Create a fake role."""
        from invenio.modules.access.control import acc_add_role
        from invenio.modules.access.firerole import compile_role_definition, \
            serialize
        self.role_name = 'test'
        self.role_description = 'test role'
        self.role_definition = 'allow email /.*@cern.ch/'
        self.role_id, dummy, dummy, dummy = acc_add_role(self.role_name,
            self.role_description,
            serialize(compile_role_definition(self.role_definition)),
            self.role_definition)

    def tearDown(self):
        """Drop the fake role."""
        from invenio.modules.access.control import acc_delete_role
        acc_delete_role(self.role_id)

    def test_webaccess_firerole_serialization(self):
        """webaccess - firerole role definition correctly serialized"""
        from invenio.modules.access.control import acc_get_role_definition
        from invenio.modules.access.firerole import compile_role_definition, \
            deserialize
        def_ser = compile_role_definition(self.role_definition)
        tmp_def_ser = acc_get_role_definition(self.role_id)
        self.assertEqual(def_ser, deserialize(tmp_def_ser))

class WebAccessUseBasketsTest(InvenioTestCase):
    """
    Check WebAccess behaviour WRT enabling/disabling web modules such
    as baskets.
    """

    def test_precached_area_authorization(self):
        """webaccess - login-time precached authorizations for usebaskets"""
        error_messages = test_web_page_content(cfg['CFG_SITE_SECURE_URL'] + '/youraccount/display?ln=en', username='jekyll', password='j123ekyll', expected_text='Your Baskets')
        error_messages.extend(test_web_page_content(cfg['CFG_SITE_SECURE_URL'] + '/youraccount/display?ln=en', username='hyde', password='h123yde', unexpected_text='Your Baskets'))

        if error_messages:
            self.fail(merge_error_messages(error_messages))

if False: #FIXME cfg['CFG_DEVEL_SITE']:
    class WebAccessRobotLoginTest(InvenioTestCase):
        """
        Check whether robot login functionality is OK.
        """
        def _erase_example_user_and_groups(self):
            for email in (self.a_email, self.another_email):
                uid = run_sql("SELECT id FROM user WHERE email=%s", (email, ))
                if uid:
                    run_sql("DELETE FROM user WHERE id=%s", (uid[0][0], ))
                    run_sql("DELETE FROM user_usergroup WHERE id_user=%s", (uid[0][0], ))
                    run_sql("DELETE FROM userEXT WHERE id_user=%s", (uid[0][0], ))
                for method_name in self.robot_login_methods:
                    for group in self.some_groups:
                        run_sql("DELETE FROM usergroup WHERE name=%s", ("%s [%s]" % (group, method_name), ))
            for nickname in (self.a_nickname, self.another_nickname):
                run_sql("DELETE FROM userEXT WHERE id=%s", (nickname, ))

        def setUp(self):
            from invenio.modules.access.local_config import CFG_EXTERNAL_AUTHENTICATION
            self.robot_login_methods = dict([(method_name, CFG_EXTERNAL_AUTHENTICATION[method_name]) for method_name in CFG_EXTERNAL_AUTHENTICATION if CFG_EXTERNAL_AUTHENTICATION[method_name] and CFG_EXTERNAL_AUTHENTICATION[method_name].robot_login_method_p()])
            self.a_robot = "regression-test"
            self.a_password = "123"
            self.a_email = "foo.bar@example.org"
            self.another_email = "baz@example.org"
            self.a_nickname = "foo-bar"
            self.another_nickname = "baz"
            self.some_groups = ["a group for regression test", "another group for regression test"]
            self.myip = urlopen(cfg['CFG_SITE_URL'] + "/httptest/whatismyip").read()
            from invenio.legacy.external_authentication.robot import update_robot_key
            for method_name in self.robot_login_methods:
                update_robot_key(method_name, self.a_robot, self.a_password)
            from invenio.legacy.external_authentication.robot import load_robot_keys

        def tearDown(self):
            from invenio.legacy.external_authentication.robot import update_robot_key
            #for method_name in self.robot_login_methods:
                #update_robot_key(method_name, self.a_robot)
            from invenio.legacy.external_authentication.robot import load_robot_keys
            self._erase_example_user_and_groups()

        def test_normal_robot_login_method(self):
            """webaccess - robot login method"""
            for method_name, method in self.robot_login_methods.iteritems():
                url = method.test_create_example_url(self.a_email, method_name, self.a_robot, self.myip)
                try:
                    error_messages = test_web_page_content(url, expected_text=self.a_email)
                    if error_messages:
                        self.fail(merge_error_messages(error_messages))
                finally:
                    self._erase_example_user_and_groups()

        def test_robot_login_method_with_nickname(self):
            """webaccess - robot login method with nickname"""
            for method_name, method in self.robot_login_methods.iteritems():
                if method.enforce_external_nicknames:
                    url = method.test_create_example_url(self.a_email, method_name, self.a_robot, self.myip, nickname=self.a_nickname)
                    try:
                        error_messages = test_web_page_content(url, expected_text=self.a_nickname)
                        if error_messages:
                            self.fail(merge_error_messages(error_messages))
                    finally:
                        self._erase_example_user_and_groups()

        def test_robot_login_method_with_groups(self):
            """webaccess - robot login method with groups"""
            for method_name, method in self.robot_login_methods.iteritems():
                url = method.test_create_example_url(self.a_email, method_name, self.a_robot, self.myip, groups=self.some_groups, referer=cfg['CFG_SITE_SECURE_URL'] + "/yourgroups/display")
                try:
                    for group in self.some_groups:
                        error_messages = test_web_page_content(url, expected_text="%s [%s]" % (group, method_name))
                    if error_messages:
                        self.fail(merge_error_messages(error_messages))
                finally:
                    self._erase_example_user_and_groups()

        def test_robot_login_method_wrong_ip(self):
            """webaccess - robot login method wrong IP"""
            for method_name, method in self.robot_login_methods.iteritems():
                url = method.test_create_example_url(self.a_email, method_name, self.a_robot, '123.123.123.123')
                try:
                    error_messages = test_web_page_content(url, expected_text="The provided assertion has been issued for a different IP address")
                    if error_messages:
                        self.fail(merge_error_messages(error_messages))
                finally:
                    self._erase_example_user_and_groups()

        def test_robot_login_method_expired_assertion(self):
            """webaccess - robot login method with expired assertion"""
            for method_name, method in self.robot_login_methods.iteritems():
                url = method.test_create_example_url(self.a_email, method_name, self.a_robot, self.myip, timeout=time.time())
                time.sleep(1)
                try:
                    error_messages = test_web_page_content(url, expected_text="The provided assertion is expired")
                    if error_messages:
                        self.fail(merge_error_messages(error_messages))
                finally:
                    self._erase_example_user_and_groups()

        def test_robot_login_method_with_invalid_signature(self):
            """webaccess - robot login method with invalid signature"""
            for method_name, method in self.robot_login_methods.iteritems():
                url = method.test_create_example_url(self.a_email, method_name, self.a_robot, self.myip)
                url = list(urlparse(url))
                query = cgi.parse_qs(url[4])
                for key, value in query.items():
                    query[key] = value[0]
                digest = query['digest']
                digest0 = digest[0]
                if digest0 == '0':
                    digest0 = '1'
                else:
                    digest0 = '0'
                digest = digest0 + digest[1:]
                query['digest'] = digest
                url[4] = urlencode(query)
                url = urlunparse(url)
                try:
                    error_messages = test_web_page_content(url, expected_text="does not validate against the digest")
                    if error_messages:
                        self.fail(merge_error_messages(error_messages))
                finally:
                    self._erase_example_user_and_groups()

        def test_robot_login_method_changed_email(self):
            """webaccess - robot login method changed email"""
            for method_name, method in self.robot_login_methods.iteritems():
                url = method.test_create_example_url(self.a_email, method_name, self.a_robot, self.myip, nickname=self.a_nickname)
                url2 = method.test_create_example_url(self.another_email, method_name, self.a_robot, self.myip, nickname=self.a_nickname)
                try:
                    error_messages = test_web_page_content(url, expected_text=self.a_nickname)
                    if error_messages:
                        self.fail(merge_error_messages(error_messages))
                    id_user = run_sql("SELECT id FROM user WHERE email=%s", (self.a_email, ))[0][0]
                    self.failUnless(run_sql("SELECT * FROM userEXT WHERE id=%s AND id_user=%s AND method=%s", (self.a_nickname, id_user, method_name)), "Can't find id %s for user %s with metod %s. userEXT contains: %s" % (self.a_nickname, id_user, method_name, run_sql("SELECT * FROM userEXT")))
                    error_messages = test_web_page_content(url2, expected_text=self.a_nickname)
                    if error_messages:
                        self.fail(merge_error_messages(error_messages))
                    id_user2 = run_sql("SELECT id FROM user WHERE email=%s", (self.another_email, ))[0][0]
                    self.assertEqual(id_user, id_user2)
                    self.failUnless(run_sql("SELECT * FROM userEXT WHERE id=%s AND id_user=%s AND method=%s", (self.a_nickname, id_user2, method_name)))
                    ## The old email should not exist any longer.
                    self.failIf(run_sql("SELECT * FROM user WHERE email=%s", (self.a_email, )))
                finally:
                    self._erase_example_user_and_groups()

        def test_robot_login_method_merging_accounts(self):
            """webaccess - robot login method merging accounts"""
            for method_name, method in self.robot_login_methods.iteritems():
                url = method.test_create_example_url(self.a_email, method_name, self.a_robot, self.myip, nickname=self.a_nickname)
                url2 = method.test_create_example_url(self.another_email, method_name, self.a_robot, self.myip, nickname=self.another_nickname)
                url3 = method.test_create_example_url(self.a_email, method_name, self.a_robot, self.myip, nickname=self.another_nickname)
                try:
                    error_messages = test_web_page_content(url, expected_text=self.a_nickname)
                    if error_messages:
                        self.fail(merge_error_messages(error_messages))
                    id_user = run_sql("SELECT id FROM user WHERE email=%s", (self.a_email, ))[0][0]
                    self.failUnless(run_sql("SELECT * FROM userEXT WHERE id=%s AND id_user=%s AND method=%s", (self.a_nickname, id_user, method_name)))
                    error_messages = test_web_page_content(url2, expected_text=self.another_nickname)
                    if error_messages:
                        self.fail(merge_error_messages(error_messages))
                    id_user2 = run_sql("SELECT id FROM user WHERE email=%s", (self.another_email, ))[0][0]
                    self.failIfEqual(id_user, id_user2)
                    self.failUnless(run_sql("SELECT * FROM userEXT WHERE id=%s AND id_user=%s AND method=%s", (self.another_nickname, id_user2, method_name)), "Can't find id %s for user %s with metod %s. userEXT contains: %s" % (self.another_nickname, id_user2, method_name, run_sql("SELECT * FROM userEXT")))
                    ## The first email should still exists
                    self.failUnless(run_sql("SELECT * FROM user WHERE email=%s", (self.a_email, )))
                    ## We log in with the 1st email but with the second nickname.
                    ## That means the 1st user should be merged into the second.
                    error_messages = test_web_page_content(url3, expected_text=self.another_nickname)
                    if error_messages:
                        self.fail(merge_error_messages(error_messages))
                    ## The another_email should not exist any longer.
                    self.failIf(run_sql("SELECT * FROM user WHERE email=%s", (self.another_email, )), "%s still exists! while it should have been merged into %s: %s, userEXT contains: %s" % (self.another_email, self.a_email, run_sql("SELECT * FROM user WHERE email=%s", (self.another_email, )), run_sql("SELECT * FROM userEXT")))
                    ## And the corresponding user should not exist anymore as it has been
                    ## merged into id_user
                    self.failIf(run_sql("SELECT * FROM user WHERE id=%s", (id_user2, )))
                    self.failUnless(run_sql("SELECT * FROM user WHERE id=%s AND email=%s", (id_user, self.a_email)))
                finally:
                    self._erase_example_user_and_groups()


    TEST_SUITE = make_test_suite(WebAccessWebPagesAvailabilityTest,
                                WebAccessFireRoleTest,
                                WebAccessUseBasketsTest,
                                WebAccessRobotLoginTest)
else:
    TEST_SUITE = make_test_suite(WebAccessWebPagesAvailabilityTest,
                                WebAccessFireRoleTest,
                                WebAccessUseBasketsTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
