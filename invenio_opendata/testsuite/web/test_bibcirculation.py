# -*- coding: utf-8 -*-

## This file is part of Invenio.
## Copyright (C) 2011, 2013 CERN.
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

"""Bibcirculation module web tests.
   These tests are designed to pass if the pre-existing data in the database
   tables is not modified. Additional data could have been added/modified/deleted.
   These are sample tests for a few control flows. More tests must be added to the
   relevant classes for exhaustive testing.

   Set the user names and passwords correctly.
"""

from invenio.config import CFG_SITE_SECURE_URL
from invenio.testsuite import make_test_suite, \
                              run_test_suite, \
                              InvenioWebTestCase, \
                              test_web_page_content


class BibcirculationLoanRequestReturnWebTest(InvenioWebTestCase):
    """
    Web tests for different scenarios involving different control flows
    with loans, requests and returns go into this class.
    """

    user1 = "jekyll"
    pass1 = ""
    admin = "admin"
    pass_admin = ""

    def test_loan_and_return_book(self):
        print "Starting test_loan_and_return_book..."
        self.browser.get(CFG_SITE_SECURE_URL)
        self.login(username=self.admin, password=self.pass_admin)
        print "Logged in as admin."

        self.find_element_by_link_text_with_timeout("Administration")
        self.browser.find_element_by_link_text("Administration").click()

        self.find_element_by_link_text_with_timeout("Run BibCirculation")
        self.browser.find_element_by_link_text("Run BibCirculation").click()
        print "In Bibcirculation admin page."

        #Click on the 'Loan' tab and search for the borrower 'user1'
        self.find_element_by_link_text_with_timeout("Loan")
        self.browser.find_element_by_link_text("Loan").click()
        print "In 'Loan' tab, searching for the borrower."

        self.fill_textbox("string", self.user1)
        self.find_element_by_id_with_timeout("bor_search")
        self.browser.find_element_by_id("bor_search").click()
        self.page_source_test(expected_text=['User information',
                                             'Enter the barcode'])
        print "Found the borrower! Entering the barcode."

        #Try checking out a book on which another user is waiting.
        #Continue in spite of the prompting.
        self.fill_textbox("barcode", "bc-34001")
        self.find_element_by_id_with_timeout("submit_barcode")
        self.browser.find_element_by_id("submit_barcode").click()
        self.page_source_test(expected_text=['Another user is waiting'])

        self.find_element_by_id_with_timeout("submit_barcode")
        self.browser.find_element_by_id("submit_barcode").click()
        self.page_source_test(expected_text=['registered with success',
                                             'Enter the barcode'])
        print "Registered the loan with success, in spite of another user waiting."
        print "Trying to register a loan on the same book again!"

        #Try checking out the same book for the second time.
        #Error msg. shd be displayed.
        self.fill_textbox("barcode", "bc-34001")
        self.find_element_by_id_with_timeout("submit_barcode")
        self.browser.find_element_by_id("submit_barcode").click()
        self.page_source_test(expected_text=['is on a loan. Cannot be checked out.',
                                             'Enter the barcode'])
        print "Can't register."

        #The recently checked out book should appear in the 'Last loans' list.
        assert test_web_page_content(CFG_SITE_SECURE_URL +
            '/admin2/bibcirculation/all_loans', username='admin', \
             expected_text='bc-34001') == [], \
             "User's loan doesn't appear in the 'Last loans' list"

        #Click on the 'Return' tab and enter the barcode in order to
        #return the book.
        print "Returning the book."
        self.find_element_by_link_text_with_timeout("Return")
        self.browser.find_element_by_link_text("Return").click()
        self.fill_textbox("barcode", "bc-34001")
        self.find_element_by_name_with_timeout("ok_button")
        self.browser.find_element_by_name("ok_button").click()
        self.page_source_test(expected_text=['returned with success'])
        print "Returned it with success."

        #The returned book no longer appears in the 'Last loans' list.
        assert test_web_page_content(CFG_SITE_SECURE_URL +
            '/admin2/bibcirculation/all_loans', username='admin', \
             unexpected_text='bc-34001') == [], \
             "The returned book still appears in the 'Last loans' list"

        print "Trying to return the same book again."
        self.find_element_by_link_text_with_timeout("Return")
        self.browser.find_element_by_link_text("Return").click()
        self.fill_textbox("barcode", "bc-34001")
        self.find_element_by_name_with_timeout("ok_button")
        self.browser.find_element_by_name("ok_button").click()
        self.page_source_test(expected_text=['is not on loan', 'Barcode'])
        print "Can't return an already returned book."

        self.logout()
        print "Logged out."

class BibcirculationILLWebTest(InvenioWebTestCase):
    """
    Web tests with typical ILL control flows both on the user as well as
    on the admin side, reflecting the change of statuses and other attributes
    of the ILL(library, request date, cost...) and appearance in the appropriate
    ILL lists.
    """
    def test_ill_book_request(self):
        pass

    def test_ill_article_request(self):
        pass

class BibcirculationBookProposalWebTest(InvenioWebTestCase):
    """
    Web tests for book proposal control flows.
    """
    def test_propose_book_by_user(self):
        pass

class BibcirculationBookPurchaseWebTest(InvenioWebTestCase):
    """
    Web tests for book purchase control flows.
    """
    user1 = "jekyll"
    pass1 = ""
    admin = "admin"
    pass_admin = ""

    def test_purchase_book_request_with_recid(self):
        print "Starting test_purchase_book_request_with_recid..."
        self.browser.get(CFG_SITE_SECURE_URL)
        self.find_element_by_link_text_with_timeout("Books")
        self.browser.find_element_by_link_text("Books").click()

        self.find_element_by_link_text_with_timeout("Detailed record")
        self.browser.find_element_by_link_text("Detailed record").click()

        print "Reached a detailed record, clicking on purchase link."
        self.find_element_by_link_text_with_timeout("Purchase it for me!")
        self.browser.find_element_by_link_text("Purchase it for me!").click()
        self.login(username=self.user1, password=self.pass1)

        print "Logged in as user1, filling the form."
        self.page_source_test(expected_text=['Purchase request'],
                              unexpected_text=['Borrowers'])
        self.find_element_by_name_with_timeout("budget_code")
        self.fill_textbox("budget_code", "budget_code_test")
        self.find_element_by_name_with_timeout("additional_comments")
        self.fill_textbox("additional_comments", "additional_comments_test")
        self.find_element_by_id_with_timeout("submit_request")
        self.browser.find_element_by_id("submit_request").click()
        self.page_source_test(expected_text=['request has been registered'])
        print "Request registered!"
        self.logout()
        print "Logged out as user1"

        print "Logging in as admin"
        self.login(username=self.admin, password=self.pass_admin)

        self.find_element_by_link_text_with_timeout("Search")
        self.browser.find_element_by_link_text("Search").click()
        self.find_element_by_link_text_with_timeout("Books")
        self.browser.find_element_by_link_text("Books").click()

        self.find_element_by_link_text_with_timeout("Detailed record")
        self.browser.find_element_by_link_text("Detailed record").click()

        print "Reached a detailed record, clicking on purchase link."
        self.find_element_by_link_text_with_timeout("Purchase it for me!")
        self.browser.find_element_by_link_text("Purchase it for me!").click()
        self.page_source_test(expected_text=['Purchase request', 'Borrowers',
                                             'Document details'])

        print "Step1-Filling the purchase form..."
        self.find_element_by_name_with_timeout("budget_code")
        self.fill_textbox("budget_code", "budget_code_test")
        self.find_element_by_name_with_timeout("additional_comments")
        self.fill_textbox("additional_comments", "additional_comments_test")

        print "Submitting the form."
        self.find_element_by_id_with_timeout("submit_request")
        self.browser.find_element_by_id("submit_request").click()
        self.page_source_test(expected_text=['Item details', 'Request details',
                                             'Search borrower by'])
        print "Step2-Selecting the borrower..."
        self.find_element_by_name_with_timeout("p")
        self.fill_textbox("p", self.user1)
        self.find_element_by_id_with_timeout("search_user")
        self.browser.find_element_by_id("search_user").click()
        self.find_element_by_name_with_timeout("borrower_id")
        self.choose_selectbox_option_by_label("borrower_id", self.user1)
        self.find_element_by_id_with_timeout("select_user")
        self.browser.find_element_by_id("select_user").click()
        self.find_element_by_id_with_timeout("table_ill")
        self.page_source_test(expected_text=['List of purchase requests'])
        print "Submitted the purchase request."
        self.find_element_by_id_with_timeout("select_purchase")
        self.browser.find_element_by_id("select_purchase").click()
        self.find_element_by_name_with_timeout("ill_req_form")
        self.page_source_test(expected_text=['Purchase details',
                                             'Request details'])
        self.logout()

    #def test_purchase_book_request_without_recid(self):
    #    pass

TEST_SUITE = make_test_suite(BibcirculationLoanRequestReturnWebTest,
                             BibcirculationBookPurchaseWebTest, )

if __name__ == '__main__':
    run_test_suite(TEST_SUITE, warn_user=True)
