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

"""WebJournal module web tests."""

from invenio.config import CFG_SITE_SECURE_URL
from invenio.testsuite import make_test_suite, \
                              run_test_suite, \
                              InvenioWebTestCase


class InvenioWebJournalWebTest(InvenioWebTestCase):
    """WebJournal web tests."""

    def test_admin_restrictions(self):
        """webjournal - web test admin restrictions"""

        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py?ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/administrate?journal_name=AtlantisTimes&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/configure?action=add&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/index?journal_name=AtlantisTimes&action=askDelete&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/index?journal_name=AtlantisTimes&action=delete&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/configure?action=edit&journal_name=AtlantisTimes&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/feature_record?journal_name=AtlantisTimes&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/feature_record?journal_name=AtlantisTimes&action=askremove&recid=7&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/feature_record?ln=en')
        self.page_source_test(expected_text='Authorization failure')
        # Access WebJournal URLs in read-only mode
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py?ln=en')
        self.page_source_test(expected_text='Authorization failure')
        # login as juliet
        self.login(username="juliet", password="j123uliet")
        self.page_source_test(unexpected_text='delete')
        self.find_element_by_link_text_with_timeout("AtlantisTimes")
        self.browser.find_element_by_link_text("AtlantisTimes").click()
        self.page_source_test(expected_text='regenerate',
                              unexpected_text=['Feature a Record', 'Edit Configuration', 'release now', 'announce now'])
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/configure?action=add&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/index?journal_name=AtlantisTimes&action=askDelete&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/index?journal_name=AtlantisTimes&action=delete&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/configure?action=edit&journal_name=AtlantisTimes&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/feature_record?journal_name=AtlantisTimes&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/feature_record?journal_name=AtlantisTimes&action=askremove&recid=7&ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/feature_record?ln=en')
        self.page_source_test(expected_text='Authorization failure')
        self.logout()
        # Access WebJournal URLs as fully authorized editor
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py?ln=en')
        # login as balthasar
        self.login(username="balthasar", password="b123althasar")
        self.page_source_test(expected_text='delete')
        self.find_element_by_link_text_with_timeout("AtlantisTimes")
        self.browser.find_element_by_link_text("AtlantisTimes").click()
        self.page_source_test(expected_text=['Feature a Record', 'Edit Configuration',
                                             'regenerate', 'release now', 'announce now'])
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/configure?action=add&ln=en')
        self.page_source_test(unexpected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/index?journal_name=AtlantisTimes&action=askDelete&ln=en')
        self.page_source_test(unexpected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/configure?action=edit&journal_name=AtlantisTimes&ln=en')
        self.page_source_test(unexpected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/feature_record?journal_name=AtlantisTimes&ln=en')
        self.page_source_test(unexpected_text='Authorization failure')
        self.browser.get(CFG_SITE_SECURE_URL + '/admin/webjournal/webjournaladmin.py/feature_record?ln=en')
        self.page_source_test(unexpected_text='Authorization failure')
        self.logout()

TEST_SUITE = make_test_suite(InvenioWebJournalWebTest, )

if __name__ == '__main__':
    run_test_suite(TEST_SUITE, warn_user=True)
