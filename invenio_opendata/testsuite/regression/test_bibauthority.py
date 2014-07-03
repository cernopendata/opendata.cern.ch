# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2010, 2011, 2013 CERN.
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
"""BibAuthority Regression Test Suite."""

__revision__ = "$Id$"

from invenio.legacy.bibauthority.config import \
    CFG_BIBAUTHORITY_RECORD_CONTROL_NUMBER_FIELD, \
    CFG_BIBAUTHORITY_TYPE_NAMES, \
    CFG_BIBAUTHORITY_PREFIX_SEP

from invenio.testsuite import make_test_suite, run_test_suite, \
    InvenioTestCase
from invenio.base.wrappers import lazy_import
is_authority_record = lazy_import('invenio.legacy.bibauthority.engine:is_authority_record')
get_dependent_records_for_control_no = lazy_import('invenio.legacy.bibauthority.engine:get_dependent_records_for_control_no')
get_dependent_records_for_recID = lazy_import('invenio.legacy.bibauthority.engine:get_dependent_records_for_recID')
guess_authority_types = lazy_import('invenio.legacy.bibauthority.engine:guess_authority_types')
get_low_level_recIDs_from_control_no = lazy_import('invenio.legacy.bibauthority.engine:get_low_level_recIDs_from_control_no')
get_control_nos_from_recID = lazy_import('invenio.legacy.bibauthority.engine:get_control_nos_from_recID')
get_index_strings_by_control_no = lazy_import('invenio.legacy.bibauthority.engine:get_index_strings_by_control_no')
guess_main_name_from_authority_recID = lazy_import('invenio.legacy.bibauthority.engine:guess_main_name_from_authority_recID')
get_fieldvalues = lazy_import('invenio.legacy.bibrecord:get_fieldvalues')

class BibAuthorityEngineTest(InvenioTestCase):
    """Check BibEdit web pages whether they are up or not."""

    def test_bibauthority_is_authority_record(self):
        """bibauthority - test is_authority_record()"""
        self.assertFalse(is_authority_record(1))
        self.assertTrue(is_authority_record(118))

    def test_bibauthority_get_dependent_records_for_control_no(self):
        """bibauthority - test get_dependent_records_for_control_no()"""
        control_no_field = CFG_BIBAUTHORITY_RECORD_CONTROL_NUMBER_FIELD
        control_nos = get_fieldvalues(118, control_no_field)
        count = 0
        for control_no in control_nos:
            count += len(get_dependent_records_for_control_no(control_no))
        self.assertTrue(count)

    def test_bibauthority_get_dependent_records_for_recID(self):
        """bibauthority - test get_dependent_records_for_recID()"""
        self.assertTrue(len(get_dependent_records_for_recID(118)))

    def test_bibauthority_guess_authority_types(self):
        """bibauthority - test guess_authority_types()"""
        _type = CFG_BIBAUTHORITY_TYPE_NAMES['AUTHOR']
        self.assertEqual(guess_authority_types(118), [_type])

    def test_bibauthority_get_low_level_recIDs(self):
        """bibauthority - test get_low_level_recIDs_from_control_no()"""
        _type = CFG_BIBAUTHORITY_TYPE_NAMES['INSTITUTION']
        control_no = _type + CFG_BIBAUTHORITY_PREFIX_SEP + "(SzGeCERN)iii0002"
        recIDs = [121]
        self.assertEqual(get_low_level_recIDs_from_control_no(control_no),
                         recIDs)

    def test_bibauthority_get_control_nos_from_recID(self):
        """bibauthority - test get_control_nos_from_recID()"""
        self.assertTrue(len(get_control_nos_from_recID(118)))

    def test_bibauthority_guess_main_name(self):
        """bibauthority - test guess_main_name_from_authority_recID()"""
        recID = 118
        main_name = 'Ellis, John'
        self.assertEqual(guess_main_name_from_authority_recID(recID),
                         main_name)

    def test_authority_record_string_by_control_no(self):
        """bibauthority - simple test of get_index_strings_by_control_no()"""
        # vars
        _type = CFG_BIBAUTHORITY_TYPE_NAMES['AUTHOR']
        control_no = _type + CFG_BIBAUTHORITY_PREFIX_SEP + '(SzGeCERN)aaa0005'
        string = 'Ellis, Jonathan Richard'
        # run test
        self.assertTrue(string in get_index_strings_by_control_no(control_no))

TEST_SUITE = make_test_suite(
    BibAuthorityEngineTest,
)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
