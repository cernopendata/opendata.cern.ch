# -*- coding: utf-8 -*-

## This file is part of Invenio.
## Copyright (C) 2011 CERN.
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

"""WebAlert module web tests."""

from invenio.config import CFG_SITE_SECURE_URL
from invenio.testsuite import make_test_suite, \
                              run_test_suite, \
                              InvenioWebTestCase


class InvenioWebAlertWebTest(InvenioWebTestCase):
    """WebAlert web tests."""

    def test_add_alert(self):
        """webalert - web test set a new alert"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.find_element_by_link_text_with_timeout("Search")
        self.browser.find_element_by_link_text("Search").click()
        self.fill_textbox(textbox_name="p", text="physics")
        self.find_element_by_name_with_timeout("action_search")
        self.browser.find_element_by_name("action_search").click()
        self.find_element_by_link_text_with_timeout("email alert")
        self.browser.find_element_by_link_text("email alert").click()
        self.fill_textbox(textbox_name="name", text="news")
        self.choose_selectbox_option_by_label(selectbox_name="freq", label="daily")
        self.find_element_by_name_with_timeout("action")
        self.browser.find_element_by_name("action").click()
        self.page_source_test(expected_text='The alert <b>news</b> has been added to your profile.')
        self.find_element_by_link_text_with_timeout("Remove")
        self.browser.find_element_by_link_text("Remove").click()
        self.page_source_test(expected_text='The alert <b>news</b> has been removed from your profile.')
        self.logout()

    def test_alert_addbasket(self):
        """webalert - web test set an alert and store results in a basket"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Baskets")
        self.browser.find_element_by_link_text("Your Baskets").click()
        self.find_element_by_link_text_with_timeout("creating a new basket")
        self.browser.find_element_by_link_text("creating a new basket").click()
        self.fill_textbox(textbox_name="new_topic_name", text="alerts")
        self.fill_textbox(textbox_name="new_basket_name", text="news physics")
        self.find_element_by_xpath_with_timeout("//input[@value='Create new basket']")
        self.browser.find_element_by_xpath("//input[@value='Create new basket']").click()
        self.page_source_test(expected_text='news physics')
        self.find_element_by_link_text_with_timeout("Search")
        self.browser.find_element_by_link_text("Search").click()
        self.fill_textbox(textbox_name="p", text="physics")
        self.find_element_by_name_with_timeout("action_search")
        self.browser.find_element_by_name("action_search").click()
        self.find_element_by_link_text_with_timeout("email alert")
        self.browser.find_element_by_link_text("email alert").click()
        self.fill_textbox(textbox_name="name", text="news")
        self.choose_selectbox_option_by_label(selectbox_name="freq", label="daily")
        self.choose_selectbox_option_by_label(selectbox_name="idb", label="alerts > news physics")
        self.find_element_by_name_with_timeout("action")
        self.browser.find_element_by_name("action").click()
        self.page_source_test(expected_text='The alert <b>news</b> has been added to your profile.')
        self.find_element_by_link_text_with_timeout("Remove")
        self.browser.find_element_by_link_text("Remove").click()
        self.page_source_test(expected_text='The alert <b>news</b> has been removed from your profile')
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Baskets")
        self.browser.find_element_by_link_text("Your Baskets").click()
        self.find_element_by_link_text_with_timeout("news physics")
        self.browser.find_element_by_link_text("news physics").click()
        self.find_element_by_link_text_with_timeout("Delete basket")
        self.browser.find_element_by_link_text("Delete basket").click()
        self.find_element_by_xpath_with_timeout("//input[@value='Yes']")
        self.browser.find_element_by_xpath("//input[@value='Yes']").click()
        self.logout()

    def test_alert_yoursearches(self):
        """webalert - web test presence of your searches in 'Alerts'"""
    
        self.browser.get(CFG_SITE_SECURE_URL)
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.fill_textbox(textbox_name="p", text="physics")
        self.find_element_by_name_with_timeout("action_search")
        self.browser.find_element_by_name("action_search").click()
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Alert Searches")
        self.browser.find_element_by_link_text("Your Alert Searches").click()
        self.find_element_by_link_text_with_timeout("your searches")
        self.browser.find_element_by_link_text("your searches").click()
        self.page_source_test(expected_text='<strong>Pattern:</strong> physics')
        self.logout()

TEST_SUITE = make_test_suite(InvenioWebAlertWebTest, )

if __name__ == '__main__':
    run_test_suite(TEST_SUITE, warn_user=True)
