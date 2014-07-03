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

"""BibFormat module web tests."""

from invenio.config import CFG_SITE_SECURE_URL
from invenio.testsuite import make_test_suite, \
                              run_test_suite, \
                              InvenioWebTestCase


class InvenioBibFormatWebTest(InvenioWebTestCase):
    """BibFormat web tests."""

    def test_format_many_authors(self):
        """bibformat - web test format many authors"""

        self.browser.get(CFG_SITE_SECURE_URL)
        self.fill_textbox(textbox_name="p", text="recid:10")
        self.find_element_by_name_with_timeout("action_search")
        self.browser.find_element_by_name("action_search").click()
        self.handle_popup_dialog()
        self.page_source_test(expected_text='Bruneliere, R')
        self.find_element_by_link_text_with_timeout("Detailed record")
        self.browser.find_element_by_link_text("Detailed record").click()
        self.page_source_test(expected_text='Show all 315 authors')
        self.find_element_by_link_text_with_timeout("Show all 315 authors")
        self.browser.find_element_by_link_text("Show all 315 authors").click()
        self.page_source_test(expected_text=['Zobernig, G', 'Hide'])



TEST_SUITE = make_test_suite(InvenioBibFormatWebTest, )

if __name__ == '__main__':
    run_test_suite(TEST_SUITE, warn_user=True)
