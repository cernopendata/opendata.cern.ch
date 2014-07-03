# -*- coding: utf-8 -*-

## This file is part of Invenio.
## Copyright (C) 2011, 2012, 2013 CERN.
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

"""dbquery Regression Test Suite."""

__revision__ = "$Id$"

from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.testsuite import InvenioTestCase, make_test_suite, run_test_suite

dbquery = lazy_import('invenio.legacy:dbquery')


class RunSqlReturnListOfDictionaries(InvenioTestCase):
    """Test run_sql behavior when with_dict parameter is provided"""

    def test_select_simple_columns_query(self):
        """dbquery - select simple columns query"""
        res = dbquery.run_sql("SELECT id,name,dbquery FROM collection WHERE id<3", with_dict=True)
        self.assertEqual(res, ([{'dbquery': None, 'id': 1, 'name': cfg['CFG_SITE_NAME']},
                                {'dbquery': '980:"PREPRINT"', 'id': 2, 'name': 'Preprints'}]))

    def test_select_date_format_column_query(self):
        """dbquery - select date format column query"""
        import time
        year = time.localtime().tm_year
        res = dbquery.run_sql("SELECT DATE_FORMAT(creation_date, '%Y') FROM bibrec WHERE id<3", with_dict=True)
        self.assertEqual(res, ([{"DATE_FORMAT(creation_date, '%Y')": str(year)},
                                {"DATE_FORMAT(creation_date, '%Y')": str(year)}]))

    def test_select_sum_columns_query(self):
        """dbquery - select sum columns query"""
        res = dbquery.run_sql("SELECT id+nbrecs,name FROM collection WHERE id>1 AND id<5", with_dict=True)
        self.assertEqual(res, ([{'id+nbrecs': 39L, 'name': 'Preprints'},
                                {'id+nbrecs': 17L, 'name': 'Books'},
                                {'id+nbrecs': 13L, 'name': 'Theses'}]))

    def test_select_all_columns_query(self):
        """dbquery - select all columns query"""
        res = dbquery.run_sql("SELECT * FROM collection WHERE id=2", with_dict=True) # kwalitee: disable=sql
        self.assertEqual(res, ([{'dbquery': '980:"PREPRINT"',
                                  'id': 2,
                                  'name': 'Preprints',
                                  'nbrecs': 37L,
                                  'reclist': 'x\x9cc\xf8\xcf\xc8\xc0\xf0\xe3\xff\x7ff\x066E\x16\x06\x04\x00\x00N\xbd\x04%'}]))

TEST_SUITE = make_test_suite(RunSqlReturnListOfDictionaries,)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
