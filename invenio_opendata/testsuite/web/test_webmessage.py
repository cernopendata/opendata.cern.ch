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

"""WebMessage module web tests."""

from invenio.config import CFG_SITE_SECURE_URL
from invenio.testsuite import make_test_suite, \
                              run_test_suite, \
                              InvenioWebTestCase


class InvenioWebMessageWebTest(InvenioWebTestCase):
    """WebMessage web tests."""

    def _compose_message(self, users="", groups="", subject="", body=""):
        """ Compose a message with the given values
        @param users: comma separated usernames
        @type users: string
        @param groups: comma separated groupnames
        @type groups: string
        @param subject: message subject
        @type subject: string
        @param body: message body
        @type body: string
        """
        if users:
            self.fill_textbox(textbox_name="msg_to_user", text=users)
        if groups:
            self.fill_textbox(textbox_name="msg_to_group", text=groups)
        if subject:
            self.fill_textbox(textbox_name="msg_subject", text=subject)
        if body:
            self.fill_textbox(textbox_name="msg_body", text=body)

    def test_send_message(self):
        """webmessage - web test send a message"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as romeo
        self.login(username="romeo", password="r123omeo")

        # let's go to "Your Messages"
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_name_with_timeout("del_all")
        self.browser.find_element_by_name("del_all").click()
        self.handle_popup_dialog()
        self.fill_textbox(textbox_name="search_pattern", text="juliet")
        self.find_element_by_name_with_timeout("search_user")
        self.browser.find_element_by_name("search_user").click()
        self.choose_selectbox_option_by_label(selectbox_name="names_selected", label="juliet")
        self.find_element_by_name_with_timeout("add_user")
        self.browser.find_element_by_name("add_user").click()
        self.element_value_test("msg_to_user", \
                                expected_element_value='juliet')
        self._compose_message(subject="dear Juliet", body= "I love you")
        self.find_element_by_name_with_timeout("send_button")
        self.browser.find_element_by_name("send_button").click()
        self.logout()
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        # let's go to "Your Messages"
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_link_text_with_timeout("dear Juliet")
        self.browser.find_element_by_link_text("dear Juliet").click()
        self.find_element_by_name_with_timeout("delete")
        self.browser.find_element_by_name("delete").click()
        self.logout()

    def test_delete_all_messages(self):
        """webmessage - web test delete all messages"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        # let's go to "Your Messages"
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_name_with_timeout("del_all")
        self.browser.find_element_by_name("del_all").click()
        self.handle_popup_dialog()
        self._compose_message(users="juliet", subject="Dear juliet")
        self.find_element_by_name_with_timeout("send_button")
        self.browser.find_element_by_name("send_button").click()
        self.find_element_by_name_with_timeout("del_all", timeout=60)
        self.browser.find_element_by_name("del_all").click()
        self._compose_message(users="juliet", subject="Dear juliet 2")
        self.find_element_by_name_with_timeout("send_button")
        self.browser.find_element_by_name("send_button").click()
        self.logout()
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        # let's go to "Your Messages"
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_xpath_with_timeout("//input[@name='del_all' and @value='Delete All']")
        self.browser.find_element_by_xpath("//input[@name='del_all' and @value='Delete All']").click()
        self.handle_popup_dialog()
        self.find_element_by_xpath_with_timeout("//input[@value='Yes']", timeout=60)
        self.browser.find_element_by_xpath("//input[@value='Yes']").click()
        self.page_source_test(expected_text='No messages')
        self.logout()

    def test_reply_message(self):
        """webmessage - web test reply a message"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        # let's go to "Your Messages"
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_name_with_timeout("del_all")
        self.browser.find_element_by_name("del_all").click()
        self.handle_popup_dialog()
        self.fill_textbox(textbox_name="search_pattern", text="juliet")
        self.find_element_by_name_with_timeout("search_user")
        self.browser.find_element_by_name("search_user").click()
        self.choose_selectbox_option_by_label(selectbox_name="names_selected", label="juliet")
        self.find_element_by_name_with_timeout("add_user")
        self.browser.find_element_by_name("add_user").click()
        self.element_value_test("msg_to_user", \
                                expected_element_value='juliet')
        self._compose_message(subject="dear Juliet", body="I love you")
        self.find_element_by_name_with_timeout("send_button")
        self.browser.find_element_by_name("send_button").click()
        self.logout()
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        # let's go to "Your Messages"
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_link_text_with_timeout("Reply")
        self.browser.find_element_by_link_text("Reply").click()
        self._compose_message(body="\n\nme too")
        self.find_element_by_name_with_timeout("send_button")
        self.browser.find_element_by_name("send_button").click()
        self.logout()
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        # let's go to "Your Messages"
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_link_text_with_timeout("Re: dear Juliet")
        self.browser.find_element_by_link_text("Re: dear Juliet").click()
        self.find_element_by_name_with_timeout("delete")
        self.browser.find_element_by_name("delete").click()
        self.logout()
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        # let's go to "Your Messages"
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_link_text_with_timeout("dear Juliet")
        self.browser.find_element_by_link_text("dear Juliet").click()
        self.find_element_by_name_with_timeout("delete")
        self.browser.find_element_by_name("delete").click()
        self.logout()

    def test_send_message_later(self):
        """webmessage - web test send a message later"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        # let's go to "Your Messages"
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_name_with_timeout("del_all")
        self.browser.find_element_by_name("del_all").click()
        self.handle_popup_dialog()
        self._compose_message(users="juliet", subject="dear juliet", body= "i love you")
        self.choose_selectbox_option_by_label(selectbox_name="msg_send_day",label= "4")
        self.choose_selectbox_option_by_label(selectbox_name="msg_send_month", label="July")
        self.find_element_by_name_with_timeout("send_button")
        self.browser.find_element_by_name("send_button").click()
        self.page_source_test(expected_text='The chosen date (0/7/4) is invalid')
        self.choose_selectbox_option_by_label(selectbox_name="msg_send_year", label="2019")
        self.find_element_by_name_with_timeout("send_button")
        self.browser.find_element_by_name("send_button").click()
        self.page_source_test(expected_text='Your message has been sent')
        self.logout()

TEST_SUITE = make_test_suite(InvenioWebMessageWebTest, )

if __name__ == '__main__':
    run_test_suite(TEST_SUITE, warn_user=True)
