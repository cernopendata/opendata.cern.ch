# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2005, 2006, 2007, 2008, 2010, 2011, 2012, 2013 CERN.
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

"""Regression tests for the citation indexer."""

import ConfigParser

from invenio.testsuite import make_test_suite, run_test_suite, InvenioTestCase
from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import

run_sql = lazy_import('invenio.legacy.dbquery:run_sql')


def load_config():
    config_path = cfg['CFG_ETCDIR'] + "/bibrank/citation.cfg"
    config = ConfigParser.ConfigParser()
    config.readfp(open(config_path))
    return config

#FIXME
CONFIG = load_config()

EXPECTED_DICTS = {
    'refs': {
        77: [95],
        79: [78],
        80: [94],
        82: [81],
        83: [81],
        85: [77, 84],
        86: [77, 95],
        87: [81],
        88: [84],
        89: [81],
        91: [78, 79, 84],
        92: [74, 91],
        96: [18]},
    'selfcites': {},
    'selfrefs': {},
    'authorcites': {},
    'cites': {
        18: [96],
        74: [92],
        77: [85, 86],
        78: [79, 91],
        79: [91],
        81: [82, 83, 87, 89],
        84: [85, 88, 91],
        91: [92],
        94: [80],
        95: [77, 86]},
    'cites_weight': {
        18: 1,
        74: 1,
        77: 2,
        78: 2,
        79: 1,
        81: 4,
        84: 3,
        91: 1,
        94: 1,
        95: 2}
}


def compare_dicts(tester, dicts):
    for k, v in EXPECTED_DICTS.iteritems():
        if False:
            print 'expected', repr(v)
            print 'found', repr(dicts[k])
        for item in dicts[k].values():
            if isinstance(item, list):
                item.sort()
        tester.assertEqual(v, dicts[k], 'checking %s' % k)


def remove_from_dicts(dicts, recid):
    for recid in dicts['cites'].keys():
        try:
            dicts['cites'][recid].remove(recid)
            dicts['cites_weight'] -= 1
        except ValueError:
            pass
        else:
            if not dicts['cites'][recid]:
                del dicts['cites'][recid]
                del dicts['cites_weight'][recid]

    for recid in dicts['refs'].keys():
        try:
            dicts['refs'][recid].remove(recid)
        except ValueError:
            pass
        else:
            if not dicts['refs'][recid]:
                del dicts['refs'][recid]


class TestCitationIndexer(InvenioTestCase):
    """Testing citation indexer."""
    def test_basic(self):
        from invenio.legacy.bibrank.citation_indexer import process_chunk
        dicts = {
            'cites_weight': {},
            'cites': {},
            'refs': {},
            'selfcites': {},
            'selfrefs': {},
            'authorcites': {},
        }

        process_chunk(range(1, 100), CONFIG, dicts)
        compare_dicts(self, dicts)

    def test_adding_record(self):
        "tests adding a record"
        from invenio.legacy.bibrank.citation_indexer import process_chunk
        dicts = EXPECTED_DICTS.copy()
        remove_from_dicts(dicts, 92)
        process_chunk([92], CONFIG, dicts)
        compare_dicts(self, dicts)

    def test_catchup(self):
        "tests adding a record"
        from invenio.legacy.bibrank.citation_indexer import process_chunk
        dicts = EXPECTED_DICTS.copy()
        dicts['cites'][95].remove(77)
        dicts['refs'][77].remove(95)
        process_chunk([95], CONFIG, dicts)
        compare_dicts(self, dicts)

    def test_removed_refs(self):
        "test the cascading of removed refs"
        from invenio.legacy.bibrank.citation_indexer import process_chunk
        dicts = EXPECTED_DICTS.copy()
        dicts['cites'].setdefault(1, []).append(3)
        dicts['cites'].setdefault(2, []).append(3)
        dicts['refs'].setdefault(3, []).extend([1, 2])
        process_chunk([3], CONFIG, dicts)
        compare_dicts(self, dicts)

    def test_removed_cites(self):
        "test the cascading of removed cites"
        from invenio.legacy.bibrank.citation_indexer import process_chunk
        dicts = EXPECTED_DICTS.copy()
        dicts['cites'].setdefault(1, []).append(3)
        dicts['cites'].setdefault(2, []).append(3)
        dicts['refs'].setdefault(3, []).extend([1, 2])
        process_chunk([1, 2], CONFIG, dicts)
        compare_dicts(self, dicts)


class TestCitationIndexerWarnings(InvenioTestCase):
    def cleanup(self):
        run_sql("""DELETE FROM rnkCITATIONDATAERR
                   WHERE citinfo LIKE 'Test Ref %'""")

    def count(self):
        return run_sql("SELECT COUNT(*) FROM rnkCITATIONDATAERR")[0][0]

    def test_insert(self):
        from invenio.legacy.bibrank.citation_indexer import store_citation_warning
        self.cleanup()
        before = self.count()
        store_citation_warning('multiple-matches', 'Test Ref 1')
        store_citation_warning('not-well-formed', 'Test Ref 2')
        after = self.count()
        self.assertEqual(after - before, 2)
        store_citation_warning('not-well-formed', 'Test Ref 2')
        after2 = self.count()
        self.assertEqual(after2 - before, 2)
        self.cleanup()

TEST_SUITE = make_test_suite(TestCitationIndexer, TestCitationIndexerWarnings)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
