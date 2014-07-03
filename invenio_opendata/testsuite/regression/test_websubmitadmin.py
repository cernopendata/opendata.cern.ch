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

"""WebSubmit Admin Regression Test Suite."""

__revision__ = "$Id$"

from invenio.testsuite import InvenioTestCase

from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import

from invenio.testsuite import make_test_suite, run_test_suite, \
    test_web_page_content, merge_error_messages

dump_submission = lazy_import('invenio.legacy.websubmit.admincli:dump_submission')
load_submission = lazy_import('invenio.legacy.websubmit.admincli:load_submission')
remove_submission = lazy_import('invenio.legacy.websubmit.admincli:remove_submission')
diff_submission = lazy_import('invenio.legacy.websubmit.admincli:diff_submission')
run_sql = lazy_import('invenio.legacy.dbquery:run_sql')


class WebSubmitAdminWebPagesAvailabilityTest(InvenioTestCase):
    """Check WebSubmit Admin web pages whether they are up or not."""

    def test_websubmit_admin_interface_pages_availability(self):
        """websubmitadmin - availability of WebSubmit Admin interface pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/admin/websubmit/websubmitadmin.py/'

        _exports = ['', 'showall', 'doctypelist', 'doctypeadd',
                    'doctyperemove', 'actionlist', 'jschecklist',
                    'elementlist', 'functionlist']

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

    def test_websubmit_admin_guide_availability(self):
        """websubmitadmin - availability of WebSubmit Admin guide pages"""

        url = cfg['CFG_SITE_URL'] + '/help/admin/websubmit-admin-guide'
        error_messages = test_web_page_content(url,
                                               expected_text="WebSubmit Admin Guide")
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

class WebSubmitAdminCLITest(InvenioTestCase):
    """Test WebSubmit Admin CLI."""

    dummy_submission_dump_1 = r"""
DELETE FROM sbmFUNDESC WHERE function LIKE 'DUMMY1%';
DELETE FROM sbmFIELD WHERE subname LIKE '%DUMMY1';
DELETE FROM sbmFIELDDESC WHERE name LIKE 'DUMMY1%';
DELETE FROM sbmALLFUNCDESCR WHERE function LIKE 'DUMMY1%';
DELETE FROM sbmDOCTYPE WHERE sdocname='DUMMY1';
DELETE FROM sbmCATEGORIES WHERE doctype ='DUMMY1';
DELETE FROM sbmFUNCTIONS WHERE doctype='DUMMY1';
DELETE FROM sbmIMPLEMENT WHERE docname='DUMMY1';
DELETE FROM sbmPARAMETERS WHERE doctype='DUMMY1';
INSERT INTO sbmCATEGORIES VALUES ('DUMMY1','ARTICLE','Article',1);
INSERT INTO sbmDOCTYPE VALUES ('Dummy test submission 1','DUMMY1','2008-03-06','2008-03-06','Dummy submission 1 for tests');
INSERT INTO sbmFIELD VALUES ('SBIDUMMY1',1,1,'DUMMY1_AU','<br /><br /><table width=\"100%\"><tr><td valign=\"top\"><span style=\"color: red;\">*</span>Author of the Document: <i>(one per line)</i><br />','M','Author(s)','','2008-03-07','2008-03-07',NULL,NULL);
INSERT INTO sbmFIELD VALUES ('SBIDUMMY1',1,2,'DUMMY1_ABS','</td></tr></table><br /><span style=\"color: red;\">*</span>Abstract:<br />','M','Abstract','','2008-03-07','2008-03-07',NULL,NULL);
INSERT INTO sbmFIELDDESC VALUES ('DUMMY1_ABS',NULL,'520__a','T',NULL,12,80,NULL,NULL,NULL,'2008-03-07','2008-03-07','<br />Abstract:<br />',NULL,0);
INSERT INTO sbmFIELDDESC VALUES ('DUMMY1_AU',NULL,'100__a','T',NULL,6,60,NULL,NULL,NULL,'2008-03-07','2008-03-07','<br />Authors: <i>(one per line)</i><br />',NULL,0);
INSERT INTO sbmFUNCTIONS VALUES ('SBI','DUMMY1','Create_Recid',10,1);
INSERT INTO sbmFUNCTIONS VALUES ('SBI','DUMMY1','Insert_Record',40,1);
INSERT INTO sbmFUNCTIONS VALUES ('SBI','DUMMY1','Mail_Submitter',60,1);
INSERT INTO sbmFUNCTIONS VALUES ('SBI','DUMMY1','Make_Record',30,1);
INSERT INTO sbmFUNCTIONS VALUES ('SBI','DUMMY1','Print_Success',50,1);
INSERT INTO sbmFUNCTIONS VALUES ('SBI','DUMMY1','Report_Number_Generation',20,1);
INSERT INTO sbmIMPLEMENT VALUES ('DUMMY1','SBI','Y','SBIDUMMY1',1,'2008-03-06','2008-03-07',1,'','',0,0,'');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','authorfile','DUMMY1_AU');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','autorngen','Y');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','counterpath','lastid_DUMMY1_<PA>categ</PA>_<PA>yy</PA>');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','createTemplate','DUMMY1create.tpl');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','documenttype','fulltext');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','edsrn','DUMMY1_RN');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','emailFile','SuE');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','fieldnameMBI','DUMMY1_CHANGE');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','iconsize','180');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','modifyTemplate','DUMMY1modify.tpl');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','newrnin','');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','paths_and_suffixes','{\"DUMMY1_FILE\":\"\"}');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','rename','<PA>file:DUMMY1_RN</PA>');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','rnformat','DEMO-<PA>categ</PA>-<PA>yy</PA>');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','rnin','comboDUMMY1');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','sourceDoc','Textual Document');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','sourceTemplate','DUMMY1.tpl');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','status','ADDED');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','titleFile','DUMMY1_TITLE');
INSERT INTO sbmPARAMETERS VALUES ('DUMMY1','yeargen','AUTO');"""

    def test_load_submission(self):
        """websubmitadmin - test loading submission dump"""
        #FIXME
        load_submission('DUMMY1', self.dummy_submission_dump_1, method="NAMES")
        dumped_submission = dump_submission("DUMMY1", 'NAMES', True)

        dummy_submission_dump_1_and_header = '-- Extra:NAMES (the following dump contains rows in sbmALLFUNCDESCR, sbmFUNDESC, sbmFIELD and sbmFIELDDESC tables which are not specific to this submission, but that include keyword DUMMY1)' + \
                                             self.dummy_submission_dump_1
        diffed_submission = diff_submission(dumped_submission, dummy_submission_dump_1_and_header, verbose=2,
                                            ignore_dates=False, ignore_positions=False, ignore_pages=False)
        # Only the header should differ
        self.assertEqual('\n'.join(diffed_submission.splitlines()[1:]), "")

    def test_diff_submission(self):
        """websubmitadmin - test diffing submissions """
        insert_submission_dump(self.dummy_submission_dump_1)
        dumped_submission = dump_submission("DUMMY1", 'NAMES', True)

        dummy_submission_dump_1_and_header = '-- Extra:NAMES (the following dump contains rows in sbmALLFUNCDESCR, sbmFUNDESC, sbmFIELD and sbmFIELDDESC tables which are not specific to this submission, but that include keyword DUMMY1)' + \
                                             self.dummy_submission_dump_1
        diffed_submission = diff_submission(dumped_submission, dummy_submission_dump_1_and_header, verbose=2,
                                            ignore_dates=False, ignore_positions=False, ignore_pages=False)
        # Only the header should differ
        self.assertEqual('\n'.join(diffed_submission.splitlines()[1:]), "")

    def test_dump_submission_method_names(self):
        """websubmitadmin - test dumping submissions with --method=NAMES"""
        insert_submission_dump(self.dummy_submission_dump_1)
        dumped_submission = dump_submission("DUMMY1", 'NAMES', True)

        self.assert_(dumped_submission.startswith('-- DUMMY1 dump '))

        # Submission will contain date/timestamps that we don't want to consider
        dumped_submission = '\n'.join(dumped_submission.splitlines()[1:])

        expected_dump = """-- Extra:NAMES (the following dump contains rows in sbmALLFUNCDESCR, sbmFUNDESC, sbmFIELD and sbmFIELDDESC tables which are not specific to this submission, but that include keyword DUMMY1)
""" + self.dummy_submission_dump_1

        self.assertEqual(dumped_submission, expected_dump)

        # Dump without delete statements
        dumped_submission = dump_submission("DUMMY1", 'NAMES', False)
        self.assert_("DELETE" not in dumped_submission.upper())

        # Dump without "IGNORE" for duplicate insertions
        dumped_submission = dump_submission("DUMMY1", 'NAMES', False, True)
        self.assert_("IGNORE" in dumped_submission.upper())

        # Test dumping demo submission
        dumped_submission = dump_submission("DEMOART", 'NAMES', True)
        self.assert_(dumped_submission.startswith('-- DEMOART dump '))

    def test_dump_submission_method_relations(self):
        """websubmitadmin - test dumping submissions with --method=RELATIONS"""
        insert_submission_dump(self.dummy_submission_dump_1)
        dumped_submission = dump_submission("DUMMY1", 'RELATIONS', True)

        self.assert_(dumped_submission.startswith('-- DUMMY1 dump '))

        # Submission will contain date/timestamps that we don't want to consider
        dumped_submission = '\n'.join(dumped_submission.splitlines()[1:])

        self.assert_(dumped_submission.startswith("-- Extra:RELATIONS (the following dump contains rows in sbmALLFUNCDESCR, sbmFUNDESC, sbmFIELD and sbmFIELDDESC tables that are not specific to doctype DUMMY1"))

    def test_remove_submission(self):
        """websubmitadmin - test removing submissions """
        insert_submission_dump(self.dummy_submission_dump_1)
        remove_submission(doctype="DUMMY1", method="NAMES")

        self.assert_(len(run_sql('SELECT * FROM sbmDOCTYPE WHERE sdocname="DUMMY1"')) == 0)
        self.assert_(len(run_sql('SELECT * FROM sbmCATEGORIES WHERE doctype="DUMMY1"')) == 0)
        self.assert_(len(run_sql('SELECT * FROM sbmFUNCTIONS WHERE doctype="DUMMY1"')) == 0)
        self.assert_(len(run_sql('SELECT * FROM sbmIMPLEMENT WHERE docname="DUMMY1"')) == 0)
        self.assert_(len(run_sql('SELECT * FROM sbmPARAMETERS WHERE doctype="DUMMY1"')) == 0)

        self.assert_(len(run_sql('SELECT * FROM sbmFUNDESC WHERE function LIKE "DUMMY1%"')) == 0)
        self.assert_(len(run_sql('SELECT * FROM sbmFIELD WHERE subname LIKE "DUMMY1%"')) == 0)
        self.assert_(len(run_sql('SELECT * FROM sbmFIELDDESC WHERE name LIKE "DUMMY1%"')) == 0)
        self.assert_(len(run_sql('SELECT * FROM sbmALLFUNCDESCR WHERE function LIKE "DUMMY1%"')) == 0)

    def tearDown(self):
        insert_submission_dump('\n'.join([line for line in self.dummy_submission_dump_1.splitlines() if line.startswith('DELETE')]))

def insert_submission_dump(dump):
    """Helper function to insert submisson dump via run_sql()"""
    for sql_statement in dump.replace(r'\"', '"').splitlines():
        if sql_statement:
            run_sql(sql_statement)

TEST_SUITE = make_test_suite(WebSubmitAdminWebPagesAvailabilityTest,
                             WebSubmitAdminCLITest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
