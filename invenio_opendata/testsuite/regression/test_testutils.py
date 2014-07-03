# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2010, 2011 CERN.
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

"""TestUtils Regression Test Suite."""

__revision__ = "$Id$"

from invenio.testsuite import InvenioTestCase

from invenio.base.globals import cfg

from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content


class TestFunctionTestWebPageContent(InvenioTestCase):
    """Check browser test_web_page_content() function."""

    def test_twpc_username_arg(self):
        """testutils - test_web_page_content() and username arguments"""
        # should login as admin without password:
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'],
                                               username="admin",
                                               expected_text="</html>"))
        # should not login as admin with password:
        errmsgs = test_web_page_content(cfg['CFG_SITE_URL'],
                                        username="admin",
                                        password="foo",
                                        expected_text="</html>")
        if errmsgs[0].find("ERROR: Cannot login as admin.") > -1:
            pass
        else:
            self.fail("Should not be able to login as admin with foo password.")
        return

    def test_twpc_expected_text_arg(self):
        """testutils - test_web_page_content() and expected_text argument"""
        # should find HTML in an HTML page:
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + "/search?p=ellis",
                                               expected_text="</html>"))
        # should not find HTML tag in an XML page:
        errmsgs = test_web_page_content(cfg['CFG_SITE_URL'] + "/search?p=ellis&of=xm")
        if errmsgs[0].find(" does not contain </html>") > -1:
            pass
        else:
            self.fail("Should not find </html> in an XML page.")
        return

    def test_twpc_expected_link_arg(self):
        """testutils - test_web_page_content() and expected_link argument"""
        # should find link to ALEPH:
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'],
                                               expected_link_target=cfg['CFG_SITE_URL'] + "/collection/ALEPH?ln=" + cfg['CFG_SITE_LANG']))
        # should find link entitled ISOLDE:
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'],
                              expected_link_label="ISOLDE"))
        # should find link to ISOLDE entitled ISOLDE:
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'],
                              expected_link_target=cfg['CFG_SITE_URL'] + "/collection/ISOLDE?ln=" + cfg['CFG_SITE_LANG'],
                              expected_link_label="ISOLDE"))
        # should not find link to ALEPH entitled ISOLDE:
        errmsgs = test_web_page_content(cfg['CFG_SITE_URL'],
                              expected_link_target=cfg['CFG_SITE_URL'] + "/collection/ALEPH?ln=" + cfg['CFG_SITE_LANG'],
                              expected_link_label="ISOLDE")
        if errmsgs[0].find(" does not contain link to ") > -1:
            pass
        else:
            self.fail("Should not find link to ALEPH entitled ISOLDE.")
        return

TEST_SUITE = make_test_suite(TestFunctionTestWebPageContent)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
