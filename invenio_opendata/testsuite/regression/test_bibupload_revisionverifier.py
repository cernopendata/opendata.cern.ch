# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2013 CERN.
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

"""
Contains Test Cases for Revision Verifier module used along with BibUpload.
"""

from invenio.base.wrappers import lazy_import
from invenio.testsuite import make_test_suite, run_test_suite, nottest

get_record = lazy_import('invenio.legacy.search_engine:get_record')
print_record = lazy_import('invenio.legacy.search_engine:print_record')
bibupload = lazy_import('invenio.bibupload:bibupload')
xml_marc_to_records = lazy_import('invenio.bibupload:xml_marc_to_records')

run_sql = lazy_import('invenio.legacy.dbquery:run_sql')

record_get_field_value = lazy_import('invenio.legacy.bibrecord:record_get_field_value')
record_xml_output = lazy_import('invenio.legacy.bibrecord:record_xml_output')

RevisionVerifier = lazy_import('invenio.legacy.bibupload.revisionverifier:RevisionVerifier')
InvenioBibUploadConflictingRevisionsError = lazy_import('invenio.legacy.bibupload.revisionverifier:InvenioBibUploadConflictingRevisionsError')
InvenioBibUploadMissing005Error = lazy_import('invenio.legacy.bibupload.revisionverifier:InvenioBibUploadMissing005Error')
InvenioBibUploadUnchangedRecordError = lazy_import('invenio.legacy.bibupload.revisionverifier:InvenioBibUploadUnchangedRecordError')
InvenioBibUploadInvalidRevisionError = lazy_import('invenio.legacy.bibupload.revisionverifier:InvenioBibUploadInvalidRevisionError')

GenericBibUploadTest = lazy_import('invenio.legacy.bibupload.engine_regression_tests:GenericBibUploadTest')
compare_xmbuffers = lazy_import('invenio.legacy.bibupload.engine_regression_tests:compare_xmbuffers')


@nottest
def init_test_records():
    """
    Initializes test records for revision verifying scenarios

    Inserts 1st version and then appends new field every 1 sec
    to create 2nd and 3rd version of the record

    Returns a dict of following format :
                {'id':recid,
                 'rev1':(rev1_rec, rev1_005),
                 'rev2':(rev2_rec, rev2_005tag),
                 'rev3':(rev3_rec, rev3_005tag)}
    """

    # Rev 1 -- tag 100
    rev1 = """ <record>
    <controlfield tag="001">123456789</controlfield>
    <controlfield tag="005">20110101000000.0</controlfield>
    <datafield tag ="100" ind1=" " ind2=" ">
    <subfield code="a">Tester, T</subfield>
    <subfield code="u">DESY</subfield>
    </datafield>
    </record>"""
    # Append 970 to Rev1
    rev1_append = """<record>
    <controlfield tag="001">123456789</controlfield>
    <datafield tag ="970" ind1=" " ind2=" ">
    <subfield code="a">0003719PHOPHO</subfield>
    </datafield>
    </record>"""
    # Rev 2 -- Rev 1 + tag 970
    rev2 = """<record>
    <controlfield tag="001">123456789</controlfield>
    <controlfield tag="005">20110101000000.0</controlfield>
    <datafield tag ="100" ind1=" " ind2=" ">
    <subfield code="a">Tester, T</subfield>
    <subfield code="u">DESY</subfield>
    </datafield>
    <datafield tag ="970" ind1=" " ind2=" ">
    <subfield code="a">0003719PHOPHO</subfield>
    </datafield>
    </record>"""
    # Append 888 to Rev2
    rev2_append = """<record>
    <controlfield tag="001">123456789</controlfield>
    <datafield tag="888" ind1=" " ind2=" ">
    <subfield code="a">dumb text</subfield>
    </datafield>
    </record>"""
    # Rev 3 -- Rev 2 + tag 888
    rev3 = """<record>
    <controlfield tag="001">123456789</controlfield>
    <controlfield tag="005">20110101000000.0</controlfield>
    <datafield tag ="100" ind1=" " ind2=" ">
    <subfield code="a">Tester, T</subfield>
    <subfield code="u">DESY</subfield>
    </datafield>
    <datafield tag ="970" ind1=" " ind2=" ">
    <subfield code="a">0003719PHOPHO</subfield>
    </datafield>
    <datafield tag="888" ind1=" " ind2=" ">
    <subfield code="a">dumb text</subfield>
    </datafield>
    </record>"""

    init_details = {}
    insert_record = rev1.replace(
            '<controlfield tag="001">123456789</controlfield>', '')
    insert_record = insert_record.replace(
            '<controlfield tag="005">20110101000000.0</controlfield>', '')
    recs = xml_marc_to_records(insert_record)
    # --> Revision 1 submitted
    res = bibupload(recs[0], opt_mode='insert')
    recid = res[1]
    init_details['id'] = (str(recid), )

    rec = get_record(recid)
    rev_tag = record_get_field_value(rec, '005', '', '')
    # update the test data
    rev1 = rev1.replace('123456789', str(recid))
    rev1 = rev1.replace('20110101000000.0', rev_tag)
    rev1_append = rev1_append.replace('123456789', str(recid))

    rev2 = rev2.replace('123456789', str(recid))
    rev2 = rev2.replace('20110101000000.0', rev_tag)
    rev2_append = rev2_append.replace('123456789', str(recid))

    rev3 = rev3.replace('123456789', str(recid))

    init_details['rev1'] = (rev1, rev_tag)
    old_rev_tag = rev_tag

    # --> Revision 2 submitted
    recs = xml_marc_to_records(rev1_append)
    res = bibupload(recs[0], opt_mode='append')
    rec = get_record(recid)
    rev_tag = record_get_field_value(rec, '005')

    rev2 = rev2.replace(old_rev_tag, rev_tag)
    rev3 = rev3.replace('20110101000000.0', rev_tag)

    init_details['rev2'] = (rev2, rev_tag)
    old_rev_tag = rev_tag

    # --> Revision 3 submitted
    recs = xml_marc_to_records(rev2_append)
    res = bibupload(recs[0], opt_mode='append')
    rec = get_record(recid)
    rev_tag = record_get_field_value(rec, '005')

    rev3 = rev3.replace(old_rev_tag, rev_tag)
    init_details['rev3'] = (rev3, rev_tag)

    return init_details


class RevisionVerifierForCorrectAddition(GenericBibUploadTest):
    """
    Test Cases for Patch generation when fields added in Upload Record.

    Scenarios:
        * Field added in Upload Record and not added in Original Record
        * Another instance of existing Field added in Upload Record and
          not added in Original Record
    """

    def setUp(self):
        """ Sets Up sample Records for Adding Field Scenario."""
        GenericBibUploadTest.setUp(self)
        self.data = init_test_records()

        # Rev 2 Update -- Rev2 + tag 300
        self.rev2_add_field = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHOPHO</subfield>
        </datafield>
        <datafield tag="300" ind1=" " ind2=" ">
        <subfield code="a">100P</subfield>
        </datafield>
        </record>"""
        #Rev 2 Update -- Rev2 + tag 100*
        self.rev2_add_sim_field = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="100" ind1="C" ind2="0">
        <subfield code="a">Devel, D</subfield>
        <subfield code="u">FUZZY</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHOPHO</subfield>
        </datafield>
        </record>"""
        # Record Patch -- Ouput For a New Field
        self.patch = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag="300" ind1=" " ind2=" ">
        <subfield code="a">100P</subfield>
        </datafield>
        </record>"""
        # Record Patch -- Outpute for a New Identical Field
        self.patch_identical_field = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="100" ind1="C" ind2="0">
        <subfield code="a">Devel, D</subfield>
        <subfield code="u">FUZZY</subfield>
        </datafield>
        </record>"""

        self.rev2_add_field = self.rev2_add_field.replace(
                '123456789', self.data['id'][0])
        self.rev2_add_field = self.rev2_add_field.replace(
                                                    '20110101000000.0', \
                                                    self.data['rev2'][1])

        self.rev2_add_sim_field = self.rev2_add_sim_field.replace(
                '123456789', self.data['id'][0])
        self.rev2_add_sim_field = self.rev2_add_sim_field.replace(
                                                    '20110101000000.0', \
                                                    self.data['rev2'][1])

        self.patch = self.patch.replace('123456789', self.data['id'][0])
        self.patch_identical_field = self.patch_identical_field.replace(
                                                        '123456789', \
                                                        self.data['id'][0])

    def test_add_new_field(self):
        """ BibUpload Revision Verifier - Rev3-100/970/888, Added 300 to Rev2(100/970), Patch Generated for 300"""
        upload_recs = xml_marc_to_records(self.rev2_add_field)
        orig_recs = xml_marc_to_records(self.data['rev3'][0])

        rev_verifier = RevisionVerifier()
        (opt_mode, patch, dummy_affected_tags) = rev_verifier.verify_revision(upload_recs[0], \
                                                               orig_recs[0], \
                                                               'replace')
        self.assertEqual('correct', opt_mode)
        self.assertEqual(compare_xmbuffers(record_xml_output(patch), self.patch), '')

    def test_add_identical_field(self):
        """ BibUpload Revision Verifier - Rev3-100/970/888, Added 100 to Rev2(100/970), Patch Generated for 100"""
        upload_identical_rec = xml_marc_to_records(self.rev2_add_sim_field)
        orig_recs = xml_marc_to_records(self.data['rev3'][0])

        rev_verifier = RevisionVerifier()
        (opt_mode, patch, dummy_affected_tags) = rev_verifier.verify_revision(upload_identical_rec[0], \
                                           orig_recs[0], \
                                           'replace')
        self.assertEqual('correct', opt_mode)
        self.assertEqual(compare_xmbuffers(record_xml_output(patch), self.patch_identical_field), '')


class RevisionVerifierForConflictingAddition(GenericBibUploadTest):
    """
    Test Cases for Conflicts when fields added in Upload Record.

    Scenarios:
        * Field added in Upload Record but also added in Original Record
        * Field added in Upload Record but similar field modified in Original
    """

    def setUp(self):
        """ Sets Up sample Records for Adding Field Scenario."""
        GenericBibUploadTest.setUp(self)
        self.data = init_test_records()
        # Rev 2 Update -- Rev2 + tag 888
        self.rev2_add_conf_field = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
        <subfield code="a">dumb text</subfield>
        </datafield>
        </record>"""
        #Rev 2 Update -- Rev2 + tag 100*
        self.rev2_add_sim_field = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="100" ind1="C" ind2="0">
        <subfield code="a">Devel, D</subfield>
        <subfield code="u">FUZZY</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHOPHO</subfield>
        </datafield>
        </record>"""
        #Rev 3 -- Rev2 + tag 100* +tag 888
        self.rev3_add_sim_field = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="100" ind1="C" ind2="1">
        <subfield code="a">Devel, D</subfield>
        <subfield code="z">FUZZY</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHOPHO</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
        <subfield code="a">dumb text</subfield>
        </datafield>
        </record>"""
        # Rev 3 -- tag 100 updated from Rev 2 + Tag 888
        self.rev3_mod = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="z">DEVEL, U</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHOPHO</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
        <subfield code="a">dumb text</subfield>
        </datafield>
        </record>"""

        self.rev2_add_conf_field = self.rev2_add_conf_field.replace(
                '123456789', self.data['id'][0])
        self.rev2_add_conf_field = self.rev2_add_conf_field.replace(
                                                        '20110101000000.0', \
                                                        self.data['rev2'][1])

        self.rev2_add_sim_field = self.rev2_add_sim_field.replace(
                '123456789', self.data['id'][0])
        self.rev2_add_sim_field = self.rev2_add_sim_field.replace(
                                                        '20110101000000.0', \
                                                        self.data['rev2'][1])

        self.rev3_mod = self.rev3_mod.replace('123456789', self.data['id'][0])
        self.rev3_mod = self.rev3_mod.replace('20110101000000.0', \
                                              self.data['rev3'][1])

        self.rev3_add_sim_field = self.rev3_add_sim_field.replace(
                                                            '123456789', \
                                                            self.data['id'][0])
        self.rev3_add_sim_field = self.rev3_add_sim_field.replace(
                                                        '20110101000000.0', \
                                                        self.data['rev3'][1])

    def test_add_conflict_field(self):
        """ BibUpload Revision Verifier - Rev3-100/970/888, Added 888 to Rev2(100/970), Conflict Expected"""
        upload_conf_rec = xml_marc_to_records(self.rev2_add_conf_field)
        orig_recs = xml_marc_to_records(self.data['rev3'][0])

        rev_verifier = RevisionVerifier()
        self.assertRaises(InvenioBibUploadConflictingRevisionsError, \
                          rev_verifier.verify_revision, \
                          upload_conf_rec[0], \
                          orig_recs[0], \
                          'replace')

    def test_conflicting_similarfield(self):
        """ BibUpload Revision Verifier - Rev3-100/970/888, Added 100 to Rev2(100/970), 100 added to Rev3, Conflict Expected"""
        upload_identical_rec = xml_marc_to_records(self.rev2_add_sim_field)
        orig_recs = xml_marc_to_records(self.rev3_add_sim_field)

        rev_verifier = RevisionVerifier()
        self.assertRaises(InvenioBibUploadConflictingRevisionsError, \
                          rev_verifier.verify_revision, \
                          upload_identical_rec[0], \
                          orig_recs[0], \
                          'replace')

    def test_conflicting_modfield(self):
        """ BibUpload Revision Verifier - Rev3-100/970/888, Added 100 to Rev2(100/970), Rev3 100 modified, Conflict Expected"""
        upload_identical_rec = xml_marc_to_records(self.rev2_add_sim_field)
        orig_recs = xml_marc_to_records(self.rev3_mod)

        rev_verifier = RevisionVerifier()
        self.assertRaises(InvenioBibUploadConflictingRevisionsError, \
                          rev_verifier.verify_revision, \
                          upload_identical_rec[0], \
                          orig_recs[0], \
                          'replace')


class RevisionVerifierForCorrectModification(GenericBibUploadTest):
    """
    Test Cases for Patch generation when fields are modified.

    Scenarios:
        * Fields modified in Upload Record but not modified in Original Record
    """

    def setUp(self):
        """ Sets up sample records for Modified Fields Scenarios."""
        GenericBibUploadTest.setUp(self)
        self.data = init_test_records()
        # Rev 2 Update -- Rev2 ~ tag 970 Modified
        self.rev2_mod_field = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PZOOPZOO</subfield>
        </datafield>
        </record>"""
        # Modify Record Patch Output
        self.patch = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PZOOPZOO</subfield>
        </datafield>
        </record>"""

        # Scenario 2 - 970CP added to existing record
        # Rev 2 Update -- Rev2 ~ tag 970CP Added
        self.rev2_mod_field_diff_ind = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHOPHO</subfield>
        </datafield>
        <datafield tag ="970" ind1="C" ind2="P">
        <subfield code="a">0003719XYZOXYZO</subfield>
        </datafield>
        </record>"""
        # Modify Record Patch Output
        self.patch_diff_ind = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="970" ind1="C" ind2="P">
        <subfield code="a">0003719XYZOXYZO</subfield>
        </datafield>
        </record>"""

        # Scenario 3 - 970__ deleted and 970CP added to existing record
        # Rev 2 Update -- Rev2 ~ tag 970CP Added
        self.rev2_mod_del_one_add_one = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="970" ind1="C" ind2="P">
        <subfield code="a">0003719XYZOXYZO</subfield>
        </datafield>
        </record>"""
        # Modify Record Patch Output - 1st possibility
        self.patch_del_one_add_one = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="0">__DELETED_FIELDS__</subfield>
        </datafield>
        <datafield tag ="970" ind1="C" ind2="P">
        <subfield code="a">0003719XYZOXYZO</subfield>
        </datafield>
        </record>"""
        # Modify Record Patch Output - 2nd possibility
        self.patch_del_one_add_one_2 = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="970" ind1="C" ind2="P">
        <subfield code="a">0003719XYZOXYZO</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="0">__DELETED_FIELDS__</subfield>
        </datafield>
        </record>"""

        self.rev2_mod_field = self.rev2_mod_field.replace(
                                                    '123456789', \
                                                    self.data['id'][0])
        self.rev2_mod_field = self.rev2_mod_field.replace(
                                                    '20110101000000.0', \
                                                    self.data['rev2'][1])

        self.patch = self.patch.replace('123456789', self.data['id'][0])

        self.rev2_mod_field_diff_ind = self.rev2_mod_field_diff_ind.replace(
                                                    '123456789', \
                                                    self.data['id'][0])
        self.rev2_mod_field_diff_ind = self.rev2_mod_field_diff_ind.replace(
                                                    '20110101000000.0', \
                                                    self.data['rev2'][1])

        self.patch_diff_ind = self.patch_diff_ind.replace('123456789', self.data['id'][0])

        self.rev2_mod_del_one_add_one = self.rev2_mod_del_one_add_one.replace(
                                                    '123456789', \
                                                    self.data['id'][0])
        self.rev2_mod_del_one_add_one = self.rev2_mod_del_one_add_one.replace(
                                                    '20110101000000.0', \
                                                    self.data['rev2'][1])

        self.patch_del_one_add_one = self.patch_del_one_add_one.replace('123456789', self.data['id'][0])
        self.patch_del_one_add_one_2 = self.patch_del_one_add_one_2.replace('123456789', self.data['id'][0])

    def test_modified_fields(self):
        """ BibUpload Revision Verifier - Rev3-100/970/888, Modified 970 in Rev2(100/970), Patch Generated for 970"""
        upload_recs = xml_marc_to_records(self.rev2_mod_field)
        orig_recs = xml_marc_to_records(self.data['rev3'][0])

        rev_verifier = RevisionVerifier()
        (opt_mode, patch, dummy_affected_tags) = rev_verifier.verify_revision(
                                        upload_recs[0], \
                                        orig_recs[0], \
                                        'replace')
        self.assertEqual('correct', opt_mode)
        self.assertEqual(compare_xmbuffers(record_xml_output(patch), self.patch), '')

    def test_correcting_added_field_with_diff_ind(self):
        """ BibUpload Revision Verifier - Rev3-100/970__/888, Added 970CP in Rev2(100/970__), Patch Generated for 970CP"""
        upload_recs = xml_marc_to_records(self.rev2_mod_field_diff_ind)
        orig_recs = xml_marc_to_records(self.data['rev3'][0])

        rev_verifier = RevisionVerifier()
        (opt_mode, patch, dummy_affected_tags) = rev_verifier.verify_revision(
                                        upload_recs[0], \
                                        orig_recs[0], \
                                        'replace')
        self.assertEqual('correct', opt_mode)
        self.assertEqual(compare_xmbuffers(record_xml_output(patch), self.patch_diff_ind), '')

    def test_correcting_del_field_add_field_diff_ind(self):
        """ BibUpload Revision Verifier - Rev3-100/970__/888, Deleted 970__ and Added 970CP in Rev2(100/970__), Patch Generated for 970__/970CP"""
        upload_recs = xml_marc_to_records(self.rev2_mod_del_one_add_one)
        orig_recs = xml_marc_to_records(self.data['rev3'][0])

        rev_verifier = RevisionVerifier()
        (opt_mode, patch, dummy_affected_tags) = rev_verifier.verify_revision(
                                        upload_recs[0], \
                                        orig_recs[0], \
                                        'replace')
        self.assertEqual('correct', opt_mode)
        #NOTE:for multiple fields in patch it is better to compare with different possible patch strings
        #This is due to unsorted key-value pairs of generated patch dictionary
        #self.assertEqual(compare_xmbuffers(record_xml_output(patch), self.patch_del_one_add_one), '')
        self.failUnless((compare_xmbuffers(record_xml_output(patch), self.patch_del_one_add_one)!='') \
                or (compare_xmbuffers(record_xml_output(patch), self.patch_del_one_add_one_2)!=''))

class RevisionVerifierForConflictingModification(GenericBibUploadTest):
    """
    Test Cases for Revision Verifier when fields modified are conflicting.

    Scenarios:
        * Fields modified in both Upload Record and Original Record
        * Fields modified in Upload record but deleted from Original Record
    """

    def setUp(self):
        """ Sets up sample records for Modified Fields Scenarios."""
        GenericBibUploadTest.setUp(self)
        self.data = init_test_records()

        # Rev 2 Update -- Rev2 ~ tag 970 Modified
        self.rev2_mod_field = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PZOOPZOO</subfield>
        </datafield>
        </record>"""
        # Rev 3 MOdified = Rev3 ~ Tag 970 modified - Conflict with Rev2-Update
        self.rev3_mod = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHYPHY</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
        <subfield code="a">dumb text</subfield>
        </datafield>
        </record>"""
        # Rev 3 MOdified = Rev3 ~ Tag 970 Deleted - Conflict with Rev2-Update
        self.rev3_deleted = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
        <subfield code="a">dumb text</subfield>
        </datafield>
        </record>"""

        self.rev2_mod_field = self.rev2_mod_field.replace('123456789', \
                                                          self.data['id'][0])
        self.rev2_mod_field = self.rev2_mod_field.replace('20110101000000.0', \
                                                         self.data['rev2'][1])

        self.rev3_mod = self.rev3_mod.replace('123456789', self.data['id'][0])
        self.rev3_mod = self.rev3_mod.replace('20110101000000.0', \
                                               self.data['rev3'][1])

        self.rev3_deleted = self.rev3_deleted.replace('123456789', \
                                                self.data['id'][0])
        self.rev3_deleted = self.rev3_deleted.replace('20110101000000.0', \
                                                       self.data['rev3'][1])

    def test_conflicting_modified_field(self):
        """ BibUpload Revision Verifier - Rev3-100/970/888, Modified 970 in Rev2(100/970), 970 modified in Rev3, Conflict Expected"""
        upload_conf_recs = xml_marc_to_records(self.rev2_mod_field)
        orig_recs = xml_marc_to_records(self.rev3_mod)

        rev_verifier = RevisionVerifier()
        self.assertRaises(
                InvenioBibUploadConflictingRevisionsError, \
                rev_verifier.verify_revision, \
                upload_conf_recs[0], \
                orig_recs[0], \
                'replace')

    def test_conflicting_deleted_field(self):
        """ BibUpload Revision Verifier - Rev3-100/970/888, Modified 970 in Rev2(100/970), 970 removed in Rev3, Conflict Expected"""
        upload_conf_recs = xml_marc_to_records(self.rev2_mod_field)
        orig_recs = xml_marc_to_records(self.rev3_deleted)

        rev_verifier = RevisionVerifier()
        self.assertRaises(
                InvenioBibUploadConflictingRevisionsError, \
                rev_verifier.verify_revision, \
                upload_conf_recs[0], \
                orig_recs[0], \
                'replace')

class RevisionVerifierForDeletingFields(GenericBibUploadTest):
    """
    Test Cases for Revision Verifier when fields are to be deleted from upload record.

    Scenarios:
        * Fields modified in both Upload Record and Original Record
        * Fields modified in Upload record but deleted from Original Record
    """

    def setUp(self):
        """ Sets up sample records for Modified Fields Scenarios."""
        GenericBibUploadTest.setUp(self)

        # Rev 1
        self.rev1 = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="300" ind1=" " ind2=" ">
        <subfield code="a">Test, Field-1</subfield>
        </datafield>
        <datafield tag ="300" ind1=" " ind2=" ">
        <subfield code="a">Test, Field-2</subfield>
        </datafield>
        <datafield tag ="300" ind1="C" ind2="P">
        <subfield code="a">Test, Field-3</subfield>
        </datafield>
        </record>"""

        # Rev 1 -- To Replace
        self.rev1_mod = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        </record>"""

        # Patch with SPECIAL DELETE FIELD-1
        self.patch_1 = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="300" ind1=" " ind2=" ">
        <subfield code="0">__DELETE_FIELDS__</subfield>
        </datafield>
        <datafield tag ="300" ind1="C" ind2="P">
        <subfield code="0">__DELETE_FIELDS__</subfield>
        </datafield>
        </record>"""

        # Patch with SPECIAL DELETE FIELD-2
        self.patch_2 = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="300" ind1="C" ind2="P">
        <subfield code="0">__DELETE_FIELDS__</subfield>
        </datafield>
        <datafield tag ="300" ind1=" " ind2=" ">
        <subfield code="0">__DELETE_FIELDS__</subfield>
        </datafield>
        </record>"""

        self.rev_to_insert = self.rev1.replace('<controlfield tag="001">123456789</controlfield>', '')
        self.rev_to_insert = self.rev_to_insert.replace('<controlfield tag="005">20110101000000.0</controlfield>','')
        rec = xml_marc_to_records(self.rev_to_insert)
        dummy_error, self.recid, dummy_msg = bibupload(rec[0], opt_mode='insert')
        self.check_record_consistency(self.recid)

        self.rev1 = self.rev1.replace('123456789', str(self.recid))
        self.rev1_mod = self.rev1_mod.replace('123456789', str(self.recid))
        self.patch_1 = self.patch_1.replace('123456789', str(self.recid))
        self.patch_2 = self.patch_2.replace('123456789', str(self.recid))

        record = get_record(self.recid)
        rev = record_get_field_value(record, '005')

        self.rev1 = self.rev1.replace('20110101000000.0', rev)
        self.rev1_mod = self.rev1_mod.replace('20110101000000.0', rev)

    def test_for_special_delete_field(self):
        """ BibUpload Revision Verifier - Rev1-100/300, Modified 100 in Rev1-Mod, Deleted 300 in Rev1-Mod (100/300), Patch for DELETE generated"""
        upload_rec = xml_marc_to_records(self.rev1_mod)
        orig_rec = xml_marc_to_records(self.rev1)

        rev_verifier = RevisionVerifier()
        (opt_mode, final_patch, dummy_affected_tags) = rev_verifier.verify_revision(upload_rec[0], \
                                                         orig_rec[0], \
                                                         'replace')
        self.assertEqual('correct', opt_mode)
        self.failUnless((compare_xmbuffers(self.patch_1, record_xml_output(final_patch))!='') or \
                        (compare_xmbuffers(self.patch_2, record_xml_output(final_patch))!=''))
class RevisionVerifierForInterchangedFields(GenericBibUploadTest):
    """
    Contains Test Cases for Re-ordered Fields.

    Scenarios include:
            * Same set of fields but in different order
    """

    def setUp(self):
        """ Sets up sample records for Modified Fields Scenarios."""
        GenericBibUploadTest.setUp(self)

        # Rev 1 -- 100-1/100-2/100-3
        self.rev1 = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester1, T</subfield>
        <subfield code="u">DESY1</subfield>
        </datafield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester2, T</subfield>
        <subfield code="u">DESY2</subfield>
        </datafield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester3, T</subfield>
        <subfield code="u">DESY3</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHYPHY</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
        <subfield code="a">dumb text</subfield>
        </datafield>
        </record>"""

        # Rev 1 Modified -- 100-2/100-3/100-1
        self.rev1_mod = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester2, T</subfield>
        <subfield code="u">DESY2</subfield>
        </datafield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester3, T</subfield>
        <subfield code="u">DESY3</subfield>
        </datafield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester1, T</subfield>
        <subfield code="u">DESY1</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHYPHY</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
        <subfield code="a">dumb text</subfield>
        </datafield>
        </record>"""

        self.patch = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester2, T</subfield>
        <subfield code="u">DESY2</subfield>
        </datafield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester3, T</subfield>
        <subfield code="u">DESY3</subfield>
        </datafield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester1, T</subfield>
        <subfield code="u">DESY1</subfield>
        </datafield>
        </record>"""

        insert_record = self.rev1.replace(
            '<controlfield tag="001">123456789</controlfield>', '')
        insert_record = insert_record.replace(
            '<controlfield tag="005">20110101000000.0</controlfield>', '')
        recs = xml_marc_to_records(insert_record)
        # --> Revision 1 submitted
        res = bibupload(recs[0], opt_mode='insert')
        self.recid = res[1]
        self.check_record_consistency(self.recid)

        rec = get_record(self.recid)
        rev_tag = record_get_field_value(rec, '005', '', '')
        # update the test data
        self.rev1 = self.rev1.replace('123456789', str(self.recid))
        self.rev1 = self.rev1.replace('20110101000000.0', rev_tag)

        self.rev1_mod = self.rev1_mod.replace('123456789', str(self.recid))
        self.rev1_mod = self.rev1_mod.replace('20110101000000.0', rev_tag)

        self.patch = self.patch.replace('123456789', str(self.recid))

    def test_interchanged_fields(self):
        """ BibUpload Revision Verifier - Rev1--100-1/100-2/100-3/970/888, Rev1-Up--100-2/100-3/100-1/970/888, Patch Generated for 100"""

        upload_recs = xml_marc_to_records(self.rev1_mod)
        orig_recs = xml_marc_to_records(self.rev1)

        rev_verifier = RevisionVerifier()
        (opt_mode, patch, dummy_affected_tags) = rev_verifier.verify_revision(
                                        upload_recs[0], \
                                        orig_recs[0], \
                                        'replace')
        self.assertEqual('correct', opt_mode)
        self.assertEqual(compare_xmbuffers(record_xml_output(patch), self.patch), '')


class RevisionVerifierForCommonCases(GenericBibUploadTest):
    """
    Contains Test Cases for Common Scenarios.

    Scenarios include :
            * Invalid Revision
            * Invalide Opt_Mode value
            * Missing Revision in Upload Record
    """

    def setUp(self):
        """ Set up all the sample records required for Test Cases."""
        GenericBibUploadTest.setUp(self)
        self.data = init_test_records()

        # Rev 2 Update -- Rev2 ~ tag 970 Modified
        self.rev2_modified = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PZOOPZOO</subfield>
        </datafield>
        </record>"""

        self.rev2_modified = self.rev2_modified.replace('123456789', \
                                                        self.data['id'][0])

    def test_unchanged_record_upload(self):
        """ BibUpload Revision Verifier - Uploading Unchanged Record, Raise UnchangedRecordError"""

        upload_recs = xml_marc_to_records(self.data['rev3'][0])
        orig_recs = xml_marc_to_records(self.data['rev3'][0])
        rev_verifier = RevisionVerifier()

        self.assertRaises(InvenioBibUploadUnchangedRecordError, \
                        rev_verifier.verify_revision, \
                        upload_recs[0], \
                        orig_recs[0], \
                        'replace')

    def test_missing_revision(self):
        """ BibUpload Revision Verifier - Missing 005 Tag scenario, Raise Missing005Error."""

        self.rev2_modified = self.rev2_modified.replace(
                '<controlfield tag="005">20110101000000.0</controlfield>', \
                '')

        upload_recs = xml_marc_to_records(self.rev2_modified)
        orig_recs = xml_marc_to_records(self.data['rev3'][0])
        rev_verifier = RevisionVerifier()

        self.assertRaises(InvenioBibUploadMissing005Error, \
                        rev_verifier.verify_revision, \
                        upload_recs[0], \
                        orig_recs[0], \
                        'replace')

    def test_invalid_operation(self):
        """ BibUpload Revision Verifier - Incorrect opt_mode parameter."""

        upload_recs = xml_marc_to_records(self.rev2_modified)
        orig_recs = xml_marc_to_records(self.data['rev3'][0])
        rev_verifier = RevisionVerifier()

        for item in ['append', 'format', 'insert', 'delete', 'reference']:
            self.assertEqual(rev_verifier.verify_revision(
                                                upload_recs[0], \
                                                orig_recs[0], \
                                                item), None)

    def test_invalid_revision(self):
        """ BibUpload Revision Verifier - Wrong Revision in the Upload Record, Raise InvalidRevisionError"""

        self.rev2_modified = self.rev2_modified.replace(
                '<controlfield tag="005">20110101000000.0</controlfield>', \
                '<controlfield tag="005">20110101020304.0</controlfield>')
        rev_verifier = RevisionVerifier()
        upload_recs = xml_marc_to_records(self.rev2_modified)
        orig_recs = xml_marc_to_records(self.data['rev3'][0])

        self.assertRaises(InvenioBibUploadInvalidRevisionError, \
                            rev_verifier.verify_revision, \
                            upload_recs[0], \
                            orig_recs[0], \
                            'replace')

class RevisionVerifierFromBibUpload(GenericBibUploadTest):
    """ Test Case for End-to-End Bibupload with Revision Verifier module Enabled """

    def setUp(self):
        """ Set up all the sample records required for Test Cases."""
        GenericBibUploadTest.setUp(self)

        # Rev 1 -- To Insert
        self.rev1 = """<record>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="870" ind1=" " ind2=" ">
        <subfield code="a">3719PZOOPZOO</subfield>
        </datafield>
        </record>"""

        # Rev 1 Modified -- To Replace
        self.rev1_modified = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="870" ind1=" " ind2=" ">
            <subfield code="a">3719PZOOPZOO_modified</subfield>
        </datafield>
        </record>"""

        # Rev 2 Update -- Rev2
        self.rev2 = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="870" ind1=" " ind2=" ">
        <subfield code="a">3719PZOOPZOO</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
        <subfield code="a">dumb text</subfield>
        </datafield>
        </record>"""

        # Rev 2 MOdified -- Rev2 - 870 modified
        self.rev2_modified = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="870" ind1=" " ind2=" ">
        <subfield code="a">3719PZOOPZOO_another modification</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
        <subfield code="a">dumb text</subfield>
        </datafield>
        </record>"""

        self.final_xm = """<record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="005">20110101000000.0</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="870" ind1=" " ind2=" ">
        <subfield code="a">3719PZOOPZOO_modified</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
        <subfield code="a">dumb text</subfield>
        </datafield>
        </record>"""

    def test_BibUpload_revision_verifier(self):
        """ BibUpload Revision Verifier - Called from BibUpload Operation - Patch & Conflict Scenarios"""

        recs = xml_marc_to_records(self.rev1)
        # --> Revision 1 submitted
        error, self.recid, dummy_msg = bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(self.recid)
        record = get_record(self.recid)
        rev = record_get_field_value(record, '005', '', '')
        recs = xml_marc_to_records(self.rev1)
        self.rev2 = self.rev2.replace('123456789', str(self.recid))
        self.rev2 = self.rev2.replace('20110101000000.0', rev)
        self.rev1_modified = self.rev1_modified.replace('123456789', str(self.recid))
        self.rev1_modified = self.rev1_modified.replace('20110101000000.0', rev)
        self.final_xm = self.final_xm.replace('123456789', str(self.recid))

        recs = xml_marc_to_records(self.rev1)
        recs = xml_marc_to_records(self.rev2)
        # --> Revision 2 submitted
        error, self.recid, dummy_msg = bibupload(recs[0], opt_mode='replace')
        self.check_record_consistency(self.recid)
        record = get_record(self.recid)
        self.rev2 = self.rev2.replace(rev, record_get_field_value(record, '005', '', ''))
        self.rev2_modified = self.rev2_modified.replace('123456789', str(self.recid))
        self.rev2_modified = self.rev2_modified.replace('20110101000000.0', record_get_field_value(record, '005', '', ''))
        # --> Revision 1 modified submitted
        recs = xml_marc_to_records(self.rev1_modified)
        error, self.recid, dummy_msg = bibupload(recs[0], opt_mode='replace')
        self.check_record_consistency(self.recid)
        record = get_record(self.recid)
        rev = record_get_field_value(record, '005', '', '')
        self.final_xm = self.final_xm.replace('20110101000000.0', rev)
        self.assertEqual(compare_xmbuffers(self.final_xm, print_record(self.recid, 'xm')), '')
        # --> Revision 2 modified submitted
        recs = xml_marc_to_records(self.rev2_modified)
        error, self.recid, dummy_msg = bibupload(recs[0], opt_mode='replace')
        self.check_record_consistency(self.recid)
        self.assertEquals(error, 2)



class RevisionVerifierHistoryOfAffectedFields(GenericBibUploadTest):
    """Checks if column 'affected fields' from hstRECORD table
       is filled correctly"""

    def setUp(self):
        GenericBibUploadTest.setUp(self)
        self.data = init_test_records()

    def test_inserted_record_with_no_affected_tags_in_hst(self):
        """Checks if inserted record has affected fields in hstRECORD table"""
        query = "SELECT affected_fields from hstRECORD where id_bibrec=5 ORDER BY job_date DESC"
        res = run_sql(query)
        self.assertEqual(res[0][0], "")

    def test_corrected_record_affected_tags(self):
        """Checks if corrected record has affected fields in hstRECORD table"""
        query = "SELECT affected_fields from hstRECORD where id_bibrec=12 ORDER BY job_date DESC"
        res = run_sql(query)
        self.assertEqual(res[0][0], "005__%,8564_%,909C0%,909C1%,909C5%,909CO%,909CS%")


    def test_append_to_record_affected_tags(self):
        """Checks if record with appended parts has proper affected fields in hstRECORD table"""
        query = """SELECT affected_fields from hstRECORD where id_bibrec=%s
                   ORDER BY job_date DESC""" % self.data["id"][0]
        res = run_sql(query)
        self.assertEqual(res[0][0], '005__%,888__%')
        self.assertEqual(res[1][0], '005__%,970__%')
        self.assertEqual(res[2][0], '')


TEST_SUITE = make_test_suite(RevisionVerifierForCorrectAddition,
                            RevisionVerifierForCorrectModification,
                            RevisionVerifierForInterchangedFields,
                            RevisionVerifierForDeletingFields,
                            RevisionVerifierForConflictingAddition,
                            RevisionVerifierForConflictingModification,
                            RevisionVerifierForCommonCases,
                            RevisionVerifierHistoryOfAffectedFields)


if __name__ == '__main__':
    run_test_suite(TEST_SUITE, warn_user=True)
