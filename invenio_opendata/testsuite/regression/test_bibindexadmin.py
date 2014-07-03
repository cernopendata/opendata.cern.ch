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

"""BibIndex Admin Regression Test Suite."""

__revision__ = "$Id$"

import re

from invenio.base.globals import cfg
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages, \
                              get_authenticated_mechanize_browser, make_url, \
                              InvenioTestCase


class BibIndexAdminWebPagesAvailabilityTest(InvenioTestCase):
    """Check BibIndex Admin web pages whether they are up or not."""

    def test_bibindex_admin_interface_pages_availability(self):
        """bibindexadmin - availability of BibIndex Admin interface pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/admin/bibindex/bibindexadmin.py/'

        _exports = ['',
                    'index',
                    'index?mtype=perform_showindexoverview',
                    'index?mtype=perform_showvirtualindexoverview',
                    'index?mtype=perform_editindexes',
                    'index?mtype=perform_addindex',
                    'index?mtype=perform_editvirtualindex',
                    'index?mtype=perform_addvirtualindex',
                    'field',
                    'field?mtype=perform_showfieldoverview',
                    'field?mtype=perform_editfields',
                    'field?mtype=perform_addfield',
                    'editindex?mtype=perform_modifysynonymkb',
                    'editindex?mtype=perform_modifystopwords',
                    'editindex?mtype=perform_modifyremovehtml',
                    'editindex?mtype=perform_modifyremovelatex',
                    'editindex?mtype=perform_modifytokenizer'
                    ]

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            # first try as guest:
            error_messages.extend(test_web_page_content(url,
                                                        username='guest',
                                                        expected_text=
                                                        'Authorization failure'))
            # then try as admin:
            error_messages.extend(test_web_page_content(url,
                                                        username='admin'))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_bibindex_admin_guide_availability(self):
        """bibindexadmin - availability of BibIndex Admin guide pages"""

        url = cfg['CFG_SITE_URL'] + '/help/admin/bibindex-admin-guide'
        error_messages = test_web_page_content(url,
                                               expected_text="BibIndex Admin Guide")
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return


def check_admin_forms_with_dropdown_list(url, fields):
    """Logs in as 'admin' and checks given url for
       dropdown lists in forms available in the given page.
       Fills them with given fields and returns html body response.
       @param url: url of the forms to test
       @param fields: a dict of the form fields and their values (only dropdown lists)
       @return: html body
    """
    browser = get_authenticated_mechanize_browser("admin","")
    browser.open(url)
    browser.select_form(nr=0)
    form = browser.form
    for key in fields:
        form[key] = [fields[key]]
    resp = browser.submit()
    #second page - confirmation
    browser.select_form(nr=1)
    resp = browser.submit()
    return resp.read()

def check_admin_forms_with_input_text(url, fields):
    """Logs in as 'admin' and checks given url for
       input texts in forms available in the given page.
       Fills them with given fields and returns html body response.
       @param url: url of the forms to test
       @param fields: a dict of the form fields and their values
       @return: html body
    """
    browser = get_authenticated_mechanize_browser("admin","")
    browser.open(url)
    browser.select_form(nr=0)
    form = browser.form
    for key in fields:
        form[key] = fields[key]
    resp = browser.submit()
    #second page - confirmation
    browser.select_form(nr=1)
    resp = browser.submit()
    return resp.read()

class BibIndexAdminSynonymKnowledgeBaseTest(InvenioTestCase):
    """Tests BibIndexAdmin's ability to change knowledge base details for indexes"""

    def setUp(self):
        self.re_operation_successfull = re.compile(r"Operation successfully completed")

    def test_change_title_index_knowledge_base(self):
        """tests if information about title index's knowledge base can be changed properly"""

        base = "/admin/bibindex/bibindexadmin.py/editindex"
        parameters = {'idxID':'8', 'ln':'en', 'mtype':'perform_modifysynonymkb'}
        url = make_url(base,**parameters)

        html_response = check_admin_forms_with_dropdown_list(url, {"idxKB":"INDEX-SYNONYM-TITLE",
                                                                   "idxMATCH":"leading_to_comma"})
        success = self.re_operation_successfull.search(html_response)
        if not success:
            error_messages = """There is no "Operation successfully completed" in html response."""
            self.fail(merge_error_messages(error_messages))

    def test_change_title_index_knowledge_base_back(self):
        """tests if information about title index's knowledge base can be changed back"""

        base = "/admin/bibindex/bibindexadmin.py/editindex"
        parameters = {'idxID':'8', 'ln':'en', 'mtype':'perform_modifysynonymkb'}
        url = make_url(base, **parameters)

        html_response = check_admin_forms_with_dropdown_list(url, {"idxKB":"INDEX-SYNONYM-TITLE",
                                                                   "idxMATCH":"exact"})
        success = self.re_operation_successfull.search(html_response)
        if not success:
            error_messages = """There is no "Operation successfully completed." in html response."""
            self.fail(merge_error_messages(error_messages))


class BibIndexAdminRemoveStopwordsTest(InvenioTestCase):
    """Tests BibIndexAdmin's ability to change stopwords configuration details for indexes.
       Tests change the databse entries in idxINDEX table, but don't reindex information contained in idxWORDXXF/R.
    """

    def setUp(self):
        self.re_operation_successfull = re.compile(r"Operation successfully completed")
        self.re_stopwords_not_changed = re.compile(r"Stopwords have not been changed")

    def test_change_title_index_remove_stopword_configuration(self):
        """tests if index's remove stopwords configuration can be changed"""

        base = "/admin/bibindex/bibindexadmin.py/editindex"
        parameters = {'idxID':'8', 'ln':'en', 'mtype':'perform_modifystopwords'}
        url = make_url(base, **parameters)

        html_response = check_admin_forms_with_input_text(url, {"idxSTOPWORDS":"stopwords.kb"})

        success = self.re_operation_successfull.search(html_response)
        if not success:
            error_messages = """There is no "Operation successfully completed" in html response."""
            self.fail(merge_error_messages(error_messages))


    def test_change_title_index_remove_stopword_configuration_back(self):
        """tests if index's remove stopwords configuration can be changed back"""

        base = "/admin/bibindex/bibindexadmin.py/editindex"
        parameters = {'idxID':'8', 'ln':'en', 'mtype':'perform_modifystopwords'}
        url = make_url(base, **parameters)

        html_response = check_admin_forms_with_input_text(url, {"idxSTOPWORDS":"No"})

        success = self.re_operation_successfull.search(html_response)
        if not success:
            error_messages = """There is no "Operation successfully completed" in html response."""
            self.fail(merge_error_messages(error_messages))


class BibIndexAdminRemoveHTMLTest(InvenioTestCase):
    """Tests BibIndexAdmin's ability to change 'remove html' configuration details for indexes.
       Tests change the databse entries in idxINDEX table, but don't reindex information contained in idxWORDXXF/R.
    """

    def setUp(self):
        self.re_operation_successfull = re.compile(r"Operation successfully completed")
        self.re_removehtml_not_changed = re.compile(r"Remove HTML markup parameter has not been changed")

    def test_change_title_index_remove_html_configuration(self):
        """tests if index's 'remove html' configuration can be changed"""

        base = "/admin/bibindex/bibindexadmin.py/editindex"
        parameters = {'idxID':'8', 'ln':'en', 'mtype':'perform_modifyremovehtml'}
        url = make_url(base, **parameters)

        html_response = check_admin_forms_with_dropdown_list(url, {"idxHTML":"Yes"})
        success = self.re_operation_successfull.search(html_response)
        if not success:
            error_messages = """There is no "Operation successfully completed" in html response."""
            self.fail(merge_error_messages(error_messages))


    def test_change_title_index_remove_html_configuration_back(self):
        """tests if index's 'remove html' configuration can be changed back"""

        base = "/admin/bibindex/bibindexadmin.py/editindex"
        parameters = {'idxID':'8', 'ln':'en', 'mtype':'perform_modifyremovehtml'}
        url = make_url(base, **parameters)

        html_response = check_admin_forms_with_dropdown_list(url, {"idxHTML":"No"})
        success = self.re_operation_successfull.search(html_response)
        if not success:
            error_messages = """There is no "Operation successfully completed" in html response."""
            self.fail(merge_error_messages(error_messages))



class BibIndexAdminRemoveLatexTest(InvenioTestCase):
    """Tests BibIndexAdmin's ability to change 'remove latex' configuration details for indexes.
       Tests change the databse entries in idxINDEX table, but don't reindex information contained in idxWORDXXF/R.
    """

    def setUp(self):
        self.re_operation_successfull = re.compile(r"Operation successfully completed")
        self.re_removehtml_not_changed = re.compile(r"Remove latex markup parameter has not been changed")

    def test_change_title_index_remove_html_configuration(self):
        """tests if index's 'remove latex' configuration can be changed"""

        base = "/admin/bibindex/bibindexadmin.py/editindex"
        parameters = {'idxID':'8', 'ln':'en', 'mtype':'perform_modifyremovelatex'}
        url = make_url(base, **parameters)

        html_response = check_admin_forms_with_dropdown_list(url, {"idxLATEX":"Yes"})
        success = self.re_operation_successfull.search(html_response)
        if not success:
            error_messages = """There is no "Operation successfully completed" in html response."""
            self.fail(merge_error_messages(error_messages))


    def test_change_title_index_remove_html_configuration_back(self):
        """tests if index's 'remove latex' configuration can be changed back"""

        base = "/admin/bibindex/bibindexadmin.py/editindex"
        parameters = {'idxID':'8', 'ln':'en', 'mtype':'perform_modifyremovelatex'}
        url = make_url(base, **parameters)

        html_response = check_admin_forms_with_dropdown_list(url, {"idxLATEX":"No"})
        success = self.re_operation_successfull.search(html_response)
        if not success:
            error_messages = """There is no "Operation successfully completed" in html response."""
            self.fail(merge_error_messages(error_messages))


class BibIndexAdminTokenizerTest(InvenioTestCase):
    """Tests BibIndexAdmin's ability to change tokenizer configuration details for indexes.
       Tests change the databse entries in idxINDEX table, but don't reindex information contained in idxWORDXXF/R.
    """

    def setUp(self):
        self.re_operation_successfull = re.compile(r"Operation successfully completed")


    def test_change_title_index_tokenizer_configuration(self):
        """tests if index's tokenizer configuration can be changed"""

        base = "/admin/bibindex/bibindexadmin.py/editindex"
        parameters = {'idxID':'8', 'ln':'en', 'mtype':'perform_modifytokenizer'}
        url = make_url(base, **parameters)

        html_response = check_admin_forms_with_dropdown_list(url, {"idxTOK":"BibIndexEmptyTokenizer"})
        success = self.re_operation_successfull.search(html_response)
        if not success:
            error_messages = """There is no "Operation successfully completed" in html response."""
            self.fail(merge_error_messages(error_messages))


    def test_change_title_index_tokenizer_configuration_back(self):
        """tests if index's tokenizer configuration can be changed back"""

        base = "/admin/bibindex/bibindexadmin.py/editindex"
        parameters = {'idxID':'8', 'ln':'en', 'mtype':'perform_modifytokenizer'}
        url = make_url(base, **parameters)

        html_response = check_admin_forms_with_dropdown_list(url, {"idxTOK":"BibIndexDefaultTokenizer"})
        success = self.re_operation_successfull.search(html_response)
        if not success:
            error_messages = """There is no "Operation successfully completed" in html response."""
            self.fail(merge_error_messages(error_messages))



TEST_SUITE = make_test_suite(BibIndexAdminWebPagesAvailabilityTest,
                             BibIndexAdminSynonymKnowledgeBaseTest,
                             BibIndexAdminRemoveStopwordsTest,
                             BibIndexAdminRemoveHTMLTest,
                             BibIndexAdminRemoveLatexTest,
                             BibIndexAdminTokenizerTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
