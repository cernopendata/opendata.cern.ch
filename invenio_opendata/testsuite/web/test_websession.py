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


class InvenioWebSessionWebTest(InvenioWebTestCase):
    """WebSession web tests."""

    def _delete_messages(self):
        """Delete all messages from users inbox"""

        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_xpath_with_timeout("//input[@name='del_all' and @value='Delete All']")
        self.browser.find_element_by_xpath("//input[@name='del_all' and @value='Delete All']").click()
        self.handle_popup_dialog()
        self.find_element_by_xpath_with_timeout("//input[@value='Yes']")
        self.browser.find_element_by_xpath("//input[@value='Yes']").click()

    def test_create_group(self):
        """websession - web test create a group"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Groups")
        self.browser.find_element_by_link_text("Your Groups").click()
        self.find_element_by_name_with_timeout("create_group")
        self.browser.find_element_by_name("create_group").click()
        self.fill_textbox(textbox_name="group_name", text="group test")
        self.fill_textbox(textbox_name="group_description", text="test")
        self.choose_selectbox_option_by_label(selectbox_name="join_policy", label="Visible and open for new members")
        self.find_element_by_name_with_timeout("create_button")
        self.browser.find_element_by_name("create_button").click()
        self.handle_popup_dialog()
        self.page_source_test(expected_text='You have successfully created a new group.')
        self.find_element_by_xpath_with_timeout("//small")
        self.browser.find_element_by_xpath("//small").click()
        self.find_element_by_name_with_timeout("delete")
        self.browser.find_element_by_name("delete").click()
        self.find_element_by_name_with_timeout("delete")
        self.browser.find_element_by_name("delete").click()
        self.page_source_test(expected_text='You have successfully deleted a group.')
        self._delete_messages()
        self.logout()

    def test_message_group(self):
        """websession - web test send a message to any group"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_name_with_timeout("del_all")
        self.browser.find_element_by_name("del_all").click()
        self.handle_popup_dialog()
        self.fill_textbox(textbox_name="search_pattern", text="montague-family")
        self.find_element_by_name_with_timeout("search_group")
        self.browser.find_element_by_name("search_group").click()
        self.choose_selectbox_option_by_label(selectbox_name="names_selected", label="montague-family")
        self.find_element_by_name_with_timeout("add_group")
        self.browser.find_element_by_name("add_group").click()
        self.fill_textbox(textbox_name="msg_subject", text="hello everybody")
        self.fill_textbox(textbox_name="msg_body", text="hello")
        self.find_element_by_name_with_timeout("send_button")
        self.browser.find_element_by_name("send_button").click()
        self._delete_messages()
        self.logout()
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_link_text_with_timeout("hello everybody")
        self.browser.find_element_by_link_text("hello everybody").click()
        self.page_source_test(expected_text='hello')
        self.find_element_by_name_with_timeout("delete")
        self.browser.find_element_by_name("delete").click()
        self.logout()

    def test_create_open_group(self):
        """websession - web test create an open group and join it"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Groups")
        self.browser.find_element_by_link_text("Your Groups").click()
        self.find_element_by_name_with_timeout("create_group")
        self.browser.find_element_by_name("create_group").click()
        self.fill_textbox(textbox_name="group_name", text="my_friends")
        self.fill_textbox(textbox_name="group_description", text="all my friends")
        self.choose_selectbox_option_by_label(selectbox_name="join_policy", label="Visible and open for new members")
        self.find_element_by_name_with_timeout("create_button")
        self.browser.find_element_by_name("create_button").click()
        self.handle_popup_dialog()
        self.logout()
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.find_element_by_link_text_with_timeout("Your Groups")
        self.browser.find_element_by_link_text("Your Groups").click()
        self.find_element_by_name_with_timeout("join_group")
        self.browser.find_element_by_name("join_group").click()
        self.choose_selectbox_option_by_label(selectbox_name="grpID", label="my_friends")
        self.find_element_by_name_with_timeout("join_button")
        self.browser.find_element_by_name("join_button").click()
        self.handle_popup_dialog()
        self.logout()
        # login as hyde
        self.login(username="hyde", password="h123yde")
        self.find_element_by_link_text_with_timeout("Your Groups")
        self.browser.find_element_by_link_text("Your Groups").click()
        self.find_element_by_name_with_timeout("join_group")
        self.browser.find_element_by_name("join_group").click()
        self.choose_selectbox_option_by_label(selectbox_name="grpID", label="my_friends")
        self.find_element_by_name_with_timeout("join_button")
        self.browser.find_element_by_name("join_button").click()
        self.handle_popup_dialog()
        self.logout()
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.find_element_by_link_text_with_timeout("Your Groups")
        self.browser.find_element_by_link_text("Your Groups").click()
        self.find_element_by_name_with_timeout("leave")
        self.browser.find_element_by_name("leave").click()
        self.choose_selectbox_option_by_label(selectbox_name="grpID", label="my_friends")
        self.find_element_by_name_with_timeout("leave_button")
        self.browser.find_element_by_name("leave_button").click()
        self.handle_popup_dialog()
        self.find_element_by_name_with_timeout("leave_button")
        self.browser.find_element_by_name("leave_button").click()
        self.logout()
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        self.find_element_by_link_text_with_timeout("Your Groups")
        self.browser.find_element_by_link_text("Your Groups").click()
        self.find_element_by_xpath_with_timeout("//small")
        self.browser.find_element_by_xpath("//small").click()
        self.find_element_by_name_with_timeout("delete")
        self.browser.find_element_by_name("delete").click()
        self.find_element_by_name_with_timeout("delete")
        self.browser.find_element_by_name("delete").click()
        self._delete_messages()
        self.logout()
        # login as hyde
        self.login(username="hyde", password="h123yde")
        self._delete_messages()
        self.logout()

    def test_set_group(self):
        """websession - web test set group"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        self.find_element_by_link_text_with_timeout("Personalize")
        self.browser.find_element_by_link_text("Personalize").click()
        self.find_element_by_link_text_with_timeout("Your Groups")
        self.browser.find_element_by_link_text("Your Groups").click()
        self.find_element_by_name_with_timeout("create_group")
        self.browser.find_element_by_name("create_group").click()
        self.fill_textbox(textbox_name="group_name", text="my_friends")
        self.fill_textbox(textbox_name="group_description", text="all my friends")
        self.choose_selectbox_option_by_label(selectbox_name="join_policy", label="Visible but new members need approval")
        self.find_element_by_name_with_timeout("create_button")
        self.browser.find_element_by_name("create_button").click()
        self.handle_popup_dialog()
        self.logout()
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.find_element_by_link_text_with_timeout("Your Groups")
        self.browser.find_element_by_link_text("Your Groups").click()
        self.find_element_by_name_with_timeout("join_group")
        self.browser.find_element_by_name("join_group").click()
        self.fill_textbox(textbox_name="group_name", text="my_friends")
        self.find_element_by_name_with_timeout("join_button")
        self.browser.find_element_by_name("join_button").click()
        self.handle_popup_dialog()
        self.choose_selectbox_option_by_label(selectbox_name="grpID", label="my_friends")
        self.find_element_by_name_with_timeout("join_button")
        self.browser.find_element_by_name("join_button").click()
        self.logout()
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        self.find_element_by_link_text_with_timeout("Your Messages")
        self.browser.find_element_by_link_text("Your Messages").click()
        self.find_element_by_link_text_with_timeout("Group my_friends: New membership request")
        self.browser.find_element_by_link_text("Group my_friends: New membership request").click()
        self.find_element_by_link_text_with_timeout("accept or reject")
        self.browser.find_element_by_link_text("accept or reject").click()
        self.choose_selectbox_option_by_label(selectbox_name="pending_member_id", label="romeo")
        self.find_element_by_name_with_timeout("add_member")
        self.browser.find_element_by_name("add_member").click()
        self.find_element_by_link_text_with_timeout("Your Groups")
        self.browser.find_element_by_link_text("Your Groups").click()
        self.find_element_by_xpath_with_timeout("//small")
        self.browser.find_element_by_xpath("//small").click()
        self.find_element_by_name_with_timeout("delete")
        self.browser.find_element_by_name("delete").click()
        self.find_element_by_name_with_timeout("delete")
        self.browser.find_element_by_name("delete").click()
        self._delete_messages()
        self.logout()
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self._delete_messages()
        self.logout()

TEST_SUITE = make_test_suite(InvenioWebSessionWebTest, )

if __name__ == '__main__':
    run_test_suite(TEST_SUITE, warn_user=True)
