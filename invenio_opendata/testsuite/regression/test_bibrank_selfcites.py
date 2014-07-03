# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2011, 2012 CERN.
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

"""Unit tests for the search engine query parsers."""


from invenio.testsuite import InvenioTestCase
import sys
from StringIO import StringIO
from datetime import datetime, timedelta

from invenio.testsuite import make_test_suite, run_test_suite


class SelfCitesIndexerTests(InvenioTestCase):
    """Test utility functions for the summarizer components"""

    def setUp(self):
        from invenio.legacy.bibrank.selfcites_task import fill_self_cites_tables
        fill_self_cites_tables({'algorithm': 'simple'})

    def test_get_personids_from_record(self):
        from invenio.legacy.bibrank.selfcites_indexer import get_personids_from_record
        get_personids_from_record(1)

    def test_get_authors_tags(self):
        """test_get_authors_tags
        We don't care about the value since it's
        customizable but verify that it doesn't error
        """
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        tags = get_authors_tags()
        self.assertEqual(len(tags), 4)

    def test_get_authors_from_record(self):
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_from_record
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        from invenio.config import CFG_BIBRANK_SELFCITES_USE_BIBAUTHORID
        old_config = CFG_BIBRANK_SELFCITES_USE_BIBAUTHORID
        tags = get_authors_tags()
        CFG_BIBRANK_SELFCITES_USE_BIBAUTHORID = 0
        self.assert_(get_authors_from_record(1, tags))
        CFG_BIBRANK_SELFCITES_USE_BIBAUTHORID = 1
        get_authors_from_record(1, tags)
        CFG_BIBRANK_SELFCITES_USE_BIBAUTHORID = old_config

    def test_get_collaborations_from_record(self):
        from invenio.legacy.bibrank.selfcites_indexer import get_collaborations_from_record
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        tags = get_authors_tags()
        self.assert_(not get_collaborations_from_record(1, tags))

    def test_fetch_references(self):
        from invenio.legacy.bibrank.selfcites_indexer import fetch_references
        self.assertEqual(fetch_references(1), set())

    def test_get_precomputed_self_cites_list(self):
        from invenio.legacy.bibrank.selfcites_indexer import \
                                            get_precomputed_self_cites_list
        counts = get_precomputed_self_cites_list([1, 2, 3, 4])
        self.assertEqual(counts, ((1, 0), (2, 0), (3, 0), (4, 0)))

    def test_get_precomputed_self_cites(self):
        from invenio.legacy.bibrank.selfcites_indexer import \
                                                  get_precomputed_self_cites
        ret = get_precomputed_self_cites(1)
        self.assertEqual(ret, 0)

    def test_compute_simple_self_citations(self):
        from invenio.legacy.bibrank.selfcites_indexer import \
                                                compute_simple_self_citations
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        tags = get_authors_tags()
        ret = compute_simple_self_citations(1, tags)
        self.assertEqual(ret, set())

    def test_compute_friends_self_citations(self):
        from invenio.legacy.bibrank.selfcites_indexer import \
                                                compute_friends_self_citations
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        tags = get_authors_tags()
        ret = compute_friends_self_citations(1, tags)
        self.assertEqual(ret, set())

    def test_get_self_citations_count(self):
        from invenio.legacy.bibrank.selfcites_indexer import get_self_citations_count
        ret = get_self_citations_count([1, 2, 3, 4])
        self.assertEqual(ret, 0)

    def test_update_self_cites_tables(self):
        from invenio.legacy.bibrank.selfcites_indexer import update_self_cites_tables
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        tags = get_authors_tags()
        config = {}
        update_self_cites_tables(1, config, tags)

    def test_store_record(self):
        from invenio.legacy.bibrank.selfcites_indexer import store_record
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_from_record
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        from invenio.legacy.dbquery import run_sql
        tags = get_authors_tags()
        recid = 1
        authors = get_authors_from_record(recid, tags)
        sql = 'DELETE FROM rnkRECORDSCACHE WHERE id_bibrec = %s'
        run_sql(sql, (recid,))
        store_record(recid, authors)
        sql = 'SELECT count(*) FROM rnkRECORDSCACHE WHERE id_bibrec = %s'
        count = run_sql(sql, (recid,))[0][0]
        self.assert_(count)

    def test_get_author_coauthors_list(self):
        from invenio.legacy.bibrank.selfcites_indexer import get_author_coauthors_list
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_from_record
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        tags = get_authors_tags()
        config = {'friends_threshold': 3}
        authors = get_authors_from_record(1, tags)
        self.assert_(get_author_coauthors_list(authors, config))

    def test_store_record_coauthors_with_some_deleted(self):
        from invenio.legacy.bibrank.selfcites_indexer import store_record_coauthors
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_from_record
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        from invenio.legacy.dbquery import run_sql
        tags = get_authors_tags()
        config = {'friends_threshold': 3}
        recid = 1
        authors = get_authors_from_record(recid, tags)

        sql = 'DELETE FROM rnkEXTENDEDAUTHORS WHERE id = %s'
        run_sql(sql, (recid,))
        store_record_coauthors(recid, authors, [1], authors, config)
        sql = 'SELECT count(*) FROM rnkEXTENDEDAUTHORS WHERE id = %s'
        count = run_sql(sql, (recid,))[0][0]
        self.assert_(count)

    def test_store_record_coauthors_with_none_deleted(self):
        from invenio.legacy.bibrank.selfcites_indexer import store_record_coauthors
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_from_record
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        from invenio.legacy.dbquery import run_sql
        tags = get_authors_tags()
        recid = 1
        config = {'friends_threshold': 3}
        authors = get_authors_from_record(recid, tags)

        sql = 'DELETE FROM rnkEXTENDEDAUTHORS WHERE id = %s'
        run_sql(sql, (recid,))
        store_record_coauthors(recid, authors, [], authors, config)
        sql = 'SELECT count(*) FROM rnkEXTENDEDAUTHORS WHERE id = %s'
        count = run_sql(sql, (recid,))[0][0]
        self.assert_(count)

    def test_get_record_coauthors(self):
        from invenio.legacy.bibrank.selfcites_indexer import get_record_coauthors
        self.assert_(get_record_coauthors(1))


class SelfCitesTaskTests(InvenioTestCase):
    def test_check_options(self):
        from invenio.legacy.bibrank.selfcites_task import check_options
        old_stderr = sys.stderr
        sys.stderr = StringIO()
        try:
            self.assert_(not check_options())
        finally:
            sys.stderr = old_stderr

    def test_parse_option(self):
        from invenio.legacy.bibrank.selfcites_task import parse_option
        parse_option('-a', None, None, None)
        parse_option('-m', None, None, None)
        parse_option('-c', '1', None, None)
        parse_option('-r', '1', None, None)
        parse_option('--recids', '1-10', None, None)
        parse_option('-r', '1,2,3-6', None, None)
        parse_option('--rebuild', None, None, None)

    def test_compute_and_store_self_citations(self):
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        from invenio.legacy.bibrank.selfcites_task import compute_and_store_self_citations
        from invenio.legacy.bibrank.selfcites_task import get_citations_fun
        from invenio.legacy.bibrank.selfcites_indexer import ALL_ALGORITHMS

        tags = get_authors_tags()
        for algorithm in ALL_ALGORITHMS:
            citation_fun = get_citations_fun(algorithm=algorithm)
        compute_and_store_self_citations(1, tags, citation_fun)

    def test_rebuild_tables(self):
        from invenio.legacy.bibrank.selfcites_task import rebuild_tables
        from invenio.legacy.bibrank.selfcites_indexer import ALL_ALGORITHMS
        for algorithm in ALL_ALGORITHMS.iterkeys():
            config = {'algorithm': algorithm, 'friends_threshold': 3}
            assert rebuild_tables(config)

    def test_fetch_bibauthorid_last_update(self):
        from invenio.legacy.bibrank.selfcites_task import \
                                                fetch_bibauthorid_last_update
        self.assert_(fetch_bibauthorid_last_update())

    def test_fetch_index_update(self):
        from invenio.legacy.bibrank.selfcites_task import fetch_index_update
        self.assert_(fetch_index_update())

    def test_fetch_records(self):
        from invenio.legacy.bibrank.selfcites_task import fetch_records
        old_date = datetime(year=1900, month=1, day=1)
        future_date = datetime.now() + timedelta(days=1)
        self.assert_(fetch_records(old_date, future_date))
        self.assert_(not fetch_records(future_date, future_date))

    def test_fetch_concerned_records(self):
        from invenio.legacy.bibrank.selfcites_task import fetch_concerned_records, \
                                                   store_last_updated, \
                                                   get_bibrankmethod_lastupdate
        name = 'selfcites'
        old_date = datetime(year=1900, month=1, day=1).strftime("%Y-%m-%d %H:%M:%S")
        try:
            original_date = get_bibrankmethod_lastupdate(name)
        except IndexError:
            original_date = old_date
        store_last_updated(name, old_date)
        self.assert_(fetch_concerned_records('selfcites'))
        future_date = datetime.now() + timedelta(days=1)
        store_last_updated(name, future_date)
        self.assert_(not fetch_concerned_records('selfcites'))
        # Restore value in db
        store_last_updated(name, original_date)

    def test_process_updates(self):
        from invenio.legacy.bibrank.selfcites_task import process_updates
        process_updates('selfcites')

    def test_has_algorithms(self):
        from invenio.legacy.bibrank.selfcites_indexer import ALL_ALGORITHMS
        self.assert_(ALL_ALGORITHMS)

    def test_process_one(self):
        from invenio.legacy.bibrank.selfcites_indexer import get_authors_tags
        from invenio.legacy.bibrank.selfcites_task import process_one
        from invenio.legacy.bibrank.selfcites_task import get_citations_fun
        from invenio.legacy.bibrank.selfcites_indexer import ALL_ALGORITHMS

        tags = get_authors_tags()
        for algorithm in ALL_ALGORITHMS:
            citation_fun = get_citations_fun(algorithm=algorithm)
            process_one(1, tags, citation_fun)

    def test_empty_self_cites_tables(self):
        from invenio.legacy.bibrank.selfcites_task import empty_self_cites_tables
        from invenio.legacy.dbquery import run_sql
        empty_self_cites_tables()
        counts = [
            run_sql('SELECT count(*) from rnkRECORDSCACHE')[0][0],
            run_sql('SELECT count(*) from rnkEXTENDEDAUTHORS')[0][0],
            run_sql('SELECT count(*) from rnkSELFCITES')[0][0],
        ]
        self.assertEqual(counts, [0, 0, 0])

    def test_fill_self_cites_tables(self):
        from invenio.legacy.bibrank.selfcites_task import fill_self_cites_tables
        from invenio.legacy.dbquery import run_sql
        config = {'algorithm':'friends', 'friends_threshold': 3}
        fill_self_cites_tables(config)
        counts = [
            run_sql('SELECT count(*) from rnkRECORDSCACHE')[0][0],
            run_sql('SELECT count(*) from rnkEXTENDEDAUTHORS')[0][0],
            run_sql('SELECT count(*) from rnkSELFCITES')[0][0],
        ]
        self.assert_(counts[0] > 0)
        self.assert_(counts[1] > 0)
        self.assert_(counts[2] > 0)


TEST_SUITE = make_test_suite(SelfCitesIndexerTests,
                             SelfCitesTaskTests)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
