# -*- coding: utf-8 -*-

## This file is part of Invenio.
## Copyright (C) 2012 CERN.
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

"""BibEdit module web tests."""

from invenio.config import CFG_SITE_SECURE_URL
from invenio.testsuite import make_test_suite, \
                              run_test_suite, \
                              InvenioWebTestCase

try:
    from selenium.webdriver.common.keys import Keys
except ImportError:
    pass

class InvenioBibEditWebTest(InvenioWebTestCase):
    """BibEdit web tests."""

    def test_bibedit_access_curator_all(self):
        """bibedit - web test access curator all"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as balthasar
        self.login(username="balthasar", password="b123althasar")
        self.browser.get(CFG_SITE_SECURE_URL + "/record/edit/?ln=en")
        self.fill_textbox(textbox_id="txtSearchPattern", text="36")
        self.find_element_by_id_with_timeout("btnSearch")
        self.browser.find_element_by_id("btnSearch").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Record loaded")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.find_element_by_id_with_timeout("content_001_0", text="36")
        self.find_element_by_id_with_timeout("btnCancel")
        self.browser.find_element_by_id("btnCancel").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Cancelled")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.fill_textbox(textbox_id="txtSearchPattern", text="12")
        self.find_element_by_id_with_timeout("btnSearch")
        self.browser.find_element_by_id("btnSearch").click()
        self.find_element_by_id_with_timeout("cellStatus")
        self.find_element_by_id_with_timeout("cellStatus", text="Record loaded")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.find_element_by_id_with_timeout("content_001_0", text="12")
        self.find_element_by_id_with_timeout("btnCancel")
        self.browser.find_element_by_id("btnCancel").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Cancelled")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.logout()

    def test_bibedit_access_curator_coll(self):
        """bibedit - web test access curator coll"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.browser.get(CFG_SITE_SECURE_URL + "/record/edit/?ln=en")
        self.fill_textbox(textbox_id="txtSearchPattern", text="36")
        self.find_element_by_id_with_timeout("btnSearch")
        self.browser.find_element_by_id("btnSearch").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Record loaded")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.find_element_by_id_with_timeout("content_001_0", text="36")
        self.find_element_by_id_with_timeout("btnCancel")
        self.browser.find_element_by_id("btnCancel").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Cancelled")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.fill_textbox(textbox_id="txtSearchPattern", text="70")
        self.find_element_by_id_with_timeout("btnSearch")
        self.browser.find_element_by_id("btnSearch").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Error: Permission denied")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.element_value_test(element_id="bibEditMessage", expected_element_value="Could not access record. Permission denied.", in_form=False)
        self.logout()

    def test_bibedit_access_curator_none(self):
        """bibedit - web test access curator none"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as jekyll
        self.login(username="jekyll", password="j123ekyll")
        self.browser.get(CFG_SITE_SECURE_URL + "/record/edit/?ln=en")
        self.fill_textbox(textbox_id="txtSearchPattern", text="1")
        self.find_element_by_id_with_timeout("btnSearch")
        self.browser.find_element_by_id("btnSearch").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Error: Permission denied")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.element_value_test(element_id="bibEditMessage", expected_element_value="Could not access record. Permission denied.", in_form=False)
        self.browser.find_element_by_id("txtSearchPattern").clear()
        self.fill_textbox(textbox_id="txtSearchPattern", text="70")
        self.find_element_by_id_with_timeout("btnSearch")
        self.browser.find_element_by_id("btnSearch").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Error: Permission denied")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.element_value_test(element_id="bibEditMessage", expected_element_value="Could not access record. Permission denied.", in_form=False)
        self.logout()

    def test_bibedit_basic_record_locking(self):
        """bibedit - web test basic record locking"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as balthasar
        self.login(username="balthasar", password="b123althasar")
        self.browser.get(CFG_SITE_SECURE_URL + "/record/edit/?ln=en")
        self.fill_textbox(textbox_id="txtSearchPattern", text="40")
        self.find_element_by_id_with_timeout("btnSearch")
        self.browser.find_element_by_id("btnSearch").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Record loaded")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.find_element_by_id_with_timeout("content_001_0", text="40")
        self.browser.find_element_by_id("content_088_0_0").click()
        self.browser.find_element_by_css_selector("textarea").clear()
        self.browser.find_element_by_css_selector("textarea").send_keys("Testing!")
        self.browser.find_element_by_css_selector("textarea").send_keys(Keys.RETURN)

        self.logout()
        self.handle_popup_dialog()
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.browser.get(CFG_SITE_SECURE_URL + "/record/edit/?ln=en")
        self.fill_textbox(textbox_id="txtSearchPattern", text="40")
        self.find_element_by_id_with_timeout("btnSearch")
        self.browser.find_element_by_id("btnSearch").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Error: Record locked by user")
        self.element_value_test(element_id="bibEditMessage", expected_element_value="This record is being edited by user balthasar (balthasar.montague@cds.cern.ch) since . Please try again later.", in_form=False)
        self.logout()
        # login as balthasar
        self.login(username="balthasar", password="b123althasar")
        self.browser.get(CFG_SITE_SECURE_URL + "/record/edit/?ln=en")
        self.fill_textbox(textbox_id="txtSearchPattern", text="40")
        self.find_element_by_id_with_timeout("btnSearch")
        self.browser.find_element_by_id("btnSearch").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Record loaded")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.find_element_by_id_with_timeout("content_001_0", text="40")
        self.find_element_by_id_with_timeout("btnCancel")
        self.browser.find_element_by_id("btnCancel").click()
        self.find_element_by_id_with_timeout("cellStatus", text="Cancelled")
        self.find_element_by_id_with_timeout("cellStatus", text="Ready")
        self.logout()

TEST_SUITE = make_test_suite(InvenioBibEditWebTest, )

if __name__ == '__main__':
    run_test_suite(TEST_SUITE, warn_user=True)
