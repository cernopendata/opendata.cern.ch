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

"""WebBasket Regression Test Suite."""

__revision__ = "$Id$"

from invenio.testsuite import InvenioTestCase
import mechanize
import re
from invenio.base.globals import cfg
from invenio.testsuite import make_test_suite, run_test_suite, InvenioTestCase, \
                              test_web_page_content, make_url, make_surl, merge_error_messages


class WebBasketWebPagesAvailabilityTest(InvenioTestCase):
    """Check WebBasket web pages whether they are up or not."""

    def test_your_baskets_pages_availability(self):
        """webbasket - availability of Your Baskets pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/yourbaskets/'

        _exports = ['', 'display_item', 'display', 'search', 'write_note',
                    'save_note', 'delete_note', 'add', 'delete', 'modify',
                    'edit', 'edit_topic', 'create_basket', 'display_public',
                    'list_public_baskets', 'subscribe', 'unsubscribe',
                    'write_public_note', 'save_public_note',]

        error_messages = []
        if cfg['CFG_WEBSESSION_DIFFERENTIATE_BETWEEN_GUESTS']:
            for url in [baseurl + page for page in _exports]:
                error_messages.extend(test_web_page_content(url))
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url, username='jekyll', password='j123ekyll'))
        for url in [baseurl + page for page in ['list_public_baskets', 'display_public']]:
            error_messages.extend(test_web_page_content(url))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

class WebBasketRecordsAdditionTest(InvenioTestCase):
    """Test addition of records to webbasket"""

    def _login(self, browser, user, password):
        """Log the user in an existing browser using his password"""

        browser.open(make_surl('/youraccount/login'))
        browser.select_form(nr=0)
        browser['nickname'] = user
        browser['password'] = password
        browser.submit()

    def _perform_search(self, browser, search_criteria):
        """Perform search in an existing browser using the specified criteria.
        Calling the method is equal of typing the criteria in the search box
        and pressing the 'search' button."""

        # open the search page that in our case is the default page
        browser.open(make_url('/'))

        # perform search
        browser.select_form(name = 'search')
        browser['p'] = search_criteria
        browser.submit(name = 'action_search')

    def _select_records_for_adding_to_basket(self, browser, records):
        """Calling this method is is equal of selecting records from
        the search results and pressing 'ADD TO BASKET' button.

        browser - the browser object where the selection takes place.
        It is supposed that the browser contains form with search results.

        records - list of numbers (first record is 0) indicating
        whisch records to be selected from the search results.  """

        # select the proper form containing the check boxes for marking the records
        browser.select_form(nr = 2)

        # select the records
        control = browser.find_control('recid')

        for current_record in records:
            control.items[current_record].selected = True

        # press 'ADD TO BASKET' button
        browser.submit();

    def _create_new_basket_and_add_records(self, browser, basket_name, topic_name):
        """creates a new basket. After submiting the form for basket creation
        the records will be automaticaly added to the basket. """

        browser.select_form(name = 'add_to_basket')
        browser['new_basket_name'] = basket_name
        browser['new_topic_name'] = topic_name
        browser.submit()

    def _delete_basket(self, browser):
        """deletes the first basket in the list of baskets on Display baskets page"""

        # go to Display baskets page
        browser.open(make_surl('/yourbaskets/display?ln=en'))

        # click Edit basket link
        browser.follow_link(text_regex=re.compile('.*Edit basket', re.I))

        # click Delete basket button on the page
        browser.select_form(name = 'edit')
        browser.submit(name = 'delete')

        # answer yes to the question "Are you sure..."
        browser.select_form(name = 'validate')
        browser.submit()

    def _check_basket_content(self, browser, expected_texts):
        """goes to the baskets page and checks the content for a specified text.

        expected_texts is a list of strings containing text that is we expect
        to be shown on the page."""

        browser.open(make_surl('/yourbaskets/display?ln=en'))
        url_body = browser.response().read()

        for current_expected_text in expected_texts:
            if current_expected_text not in url_body:
                self.fail('Expects to find ' + current_expected_text + ' in the basket')

    def _add_records_into_new_basket(self, browser, basket_name, topic_name):
        """perform a search and add records into new basket"""

        self._perform_search(browser, 'ellis')
        self._select_records_for_adding_to_basket(browser, [0, 6])
        self._create_new_basket_and_add_records(browser, basket_name, topic_name)


    def _add_records_to_basket_and_check_content(self, browser):
        """add records to basket and check content of baskets page for
        expexted strings """

        self._add_records_into_new_basket(browser, basket_name = 'Test Basket', topic_name = 'Test Topic')

        expected_texts = ['Test Topic', 'Test Basket', '2 records',
                          'Thermal conductivity of dense quark matter and cooling of stars',
                          'The total cross section for the production of heavy quarks in hadronic collisions']
        self._check_basket_content(browser, expected_texts)

    def xtest_records_addition_as_guest_user(self):
        """webbasket - addition of records as guest"""
        # FIXME: needs updating as per the new WebBasket UI

        if not cfg['CFG_WEBSESSION_DIFFERENTIATE_BETWEEN_GUESTS']:
            self.fail('SKIPPED: guests users are not differentiated')
        browser = mechanize.Browser()
        self._add_records_to_basket_and_check_content(browser)

    def xtest_records_addition_as_registered_user(self):
        """webbasket - addition of records as registered user"""
        # FIXME: needs updating as per the new WebBasket UI

        browser = mechanize.Browser()
        self._login(browser, 'jekyll', 'j123ekyll')

        self._add_records_to_basket_and_check_content(browser)

        self._delete_basket(browser)

    def xtest_adding_records_into_new_basket_twice(self):
        """webbasket - test adding records in new basket after second addition """
        # FIXME: needs updating as per the new WebBasket UI

        browser = mechanize.Browser()
        self._login(browser, 'jekyll', 'j123ekyll')

        # add twice records into the same basket, creating the basket every time
        self._add_records_into_new_basket(browser, basket_name = 'New Basket', topic_name = 'New Topic')
        self._add_records_into_new_basket(browser, basket_name = 'New Basket2', topic_name = 'New Topic2')

        url_body = browser.response().read()

        error_message = "Error: Sorry, you don't have sufficient rights on this basket"

        if(error_message in url_body):
            self._delete_basket(browser)
            self._delete_basket(browser)
            self.fail('Does not expect to find message "' + error_message + ' after creating twice the same basket.')

        self._delete_basket(browser)
        self._delete_basket(browser)


TEST_SUITE = make_test_suite(WebBasketWebPagesAvailabilityTest, WebBasketRecordsAdditionTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
