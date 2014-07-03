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
from invenio.legacy.dbquery import run_sql


class InvenioWebCommentWebTest(InvenioWebTestCase):
    """WebComment web tests."""

    def _delete_comments_and_reviews(self, recID, text="%This is a test%"):
        run_sql("delete from cmtRECORDCOMMENT where id_bibrec=%s and body like %s", (recID, text))

    def _delete_comments_and_reviews_history(self, recID):
        run_sql("delete from cmtACTIONHISTORY where id_bibrec=%s", (recID,))

    def test_add_comment(self):
        """webcomment - web test add a new comment"""

        self.browser.get(CFG_SITE_SECURE_URL + "/record/1")
        self.find_element_by_partial_link_text_with_timeout("Discussion")
        self.browser.find_element_by_partial_link_text("Discussion").click()
        self.fill_textbox(textbox_name="msg", text="This is a test comment.")
        self.find_element_by_xpath_with_timeout("//input[@value='Add comment']")
        self.browser.find_element_by_xpath("//input[@value='Add comment']").click()
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.page_source_test(expected_text='Your comment was successfully added')
        self.browser.get(CFG_SITE_SECURE_URL + "/record/1")
        self.find_element_by_partial_link_text_with_timeout("Discussion")
        self.browser.find_element_by_partial_link_text("Discussion").click()
        self.page_source_test(expected_text=['romeo', 'Your nickname, <i>romeo</i>, will be displayed as author of this comment'])
        self.logout()
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        self.browser.get(CFG_SITE_SECURE_URL+"/record/1")
        self.find_element_by_partial_link_text_with_timeout("Discussion")
        self.browser.find_element_by_partial_link_text("Discussion").click()
        self.find_element_by_link_text_with_timeout("Reply")
        self.browser.find_element_by_link_text("Reply").click()
        self.fill_textbox(textbox_name="msg", text="This is a test reply.")
        self.page_source_test(expected_text='Your nickname, <i>juliet</i>, will be displayed as author of this comment')
        self.find_element_by_xpath_with_timeout("//input[@value='Add comment']")
        self.browser.find_element_by_xpath("//input[@value='Add comment']").click()
        self.find_element_by_link_text_with_timeout("Back to record")
        self.browser.find_element_by_link_text("Back to record").click()
        self.page_source_test(expected_text=['juliet', 'This is a test reply.'])
        self.logout()
        self._delete_comments_and_reviews(recID=1)

    def test_add_review(self):
        """webcomment - web test add a new review"""

        self.browser.get(CFG_SITE_SECURE_URL + "/record/1")
        self.find_element_by_partial_link_text_with_timeout("Discussion")
        self.browser.find_element_by_partial_link_text("Discussion").click()
        self.find_element_by_link_text_with_timeout("Reviews")
        self.browser.find_element_by_link_text("Reviews").click()
        self._delete_comments_and_reviews_history(recID=1)
        self.choose_selectbox_option_by_value(selectbox_name="score", value="4")
        self.fill_textbox(textbox_name="note", text="This is a test review title")
        self.fill_textbox(textbox_name="msg", text="This is a test review body.")
        self.find_element_by_xpath_with_timeout("//input[@value='Add Review']")
        self.browser.find_element_by_xpath("//input[@value='Add Review']").click()
        # login as jekyll
        self.login(username="jekyll", password="j123ekyll")
        self.page_source_test(expected_text='review')
        self.browser.get(CFG_SITE_SECURE_URL + "/record/1")
        self.find_element_by_partial_link_text_with_timeout("Discussion")
        self.browser.find_element_by_partial_link_text("Discussion").click()
        self.find_element_by_link_text_with_timeout("Reviews")
        self.browser.find_element_by_link_text("Reviews").click()
        self.page_source_test(expected_text=['This is a test review title', \
                                             'Reviewed by', 'jekyll', \
                                             'This is a test review body.'])
        self.logout()
        self._delete_comments_and_reviews(recID=1)

    def test_delete_report(self):
        """webcomment - web test delete a report"""

        self.browser.get(CFG_SITE_SECURE_URL)
        # login as romeo
        self.login(username="romeo", password="r123omeo")
        self.browser.get(CFG_SITE_SECURE_URL + "/record/2")
        self.find_element_by_partial_link_text_with_timeout("Discussion")
        self.browser.find_element_by_partial_link_text("Discussion").click()
        self.fill_textbox(textbox_name="msg", text="This is a test comment.")
        self.find_element_by_xpath_with_timeout("//input[@value='Add comment']")
        self.browser.find_element_by_xpath("//input[@value='Add comment']").click()
        self.page_source_test(expected_text='Your comment was successfully added.')
        self.find_element_by_link_text_with_timeout("Back to record")
        self.browser.find_element_by_link_text("Back to record").click()
        self.page_source_test(expected_text=['romeo', 'This is a test comment.'])
        self.logout()
        self.browser.get(CFG_SITE_SECURE_URL)
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        self.browser.get(CFG_SITE_SECURE_URL + "/record/2")
        self.find_element_by_partial_link_text_with_timeout("Discussion")
        self.browser.find_element_by_partial_link_text("Discussion").click()
        self.fill_textbox(textbox_name="msg", text="'This is a test for another comment.")
        self.find_element_by_xpath_with_timeout("//input[@value='Add comment']")
        self.browser.find_element_by_xpath("//input[@value='Add comment']").click()
        self.find_element_by_link_text_with_timeout("Back to record")
        self.browser.find_element_by_link_text("Back to record").click()
        self.find_element_by_link_text_with_timeout("Delete comment")
        self.browser.find_element_by_link_text("Delete comment").click()
        self.page_source_test(expected_text='Comment deleted by the author')
        self.browser.get(CFG_SITE_SECURE_URL + "/admin/webcomment/webcommentadmin.py/del_single_com_auth?ln=en&id=1")
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + "/record/2/comments/display?ln=en&do=od")
        self.find_element_by_link_text_with_timeout("Report abuse")
        self.browser.find_element_by_link_text("Report abuse").click()
        self.page_source_test(expected_text='Your feedback has been recorded, many thanks')
        self.logout()
        self.browser.get(CFG_SITE_SECURE_URL + "/record/2")
        self.find_element_by_partial_link_text_with_timeout("Discussion")
        self.browser.find_element_by_partial_link_text("Discussion").click()
        self.find_element_by_link_text_with_timeout("Report abuse")
        self.browser.find_element_by_link_text("Report abuse").click()
        self.page_source_test(expected_text='please login')
        self._delete_comments_and_reviews(recID=2)

TEST_SUITE = make_test_suite(InvenioWebCommentWebTest, )

if __name__ == '__main__':
    run_test_suite(TEST_SUITE, warn_user=True)
