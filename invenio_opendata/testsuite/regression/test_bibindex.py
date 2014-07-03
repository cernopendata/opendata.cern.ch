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
"""BibIndex Regression Test Suite."""

__revision__ = "$Id$"

from invenio.testsuite import InvenioTestCase
import os
from datetime import timedelta
from intbitset import intbitset

from invenio.testsuite import make_test_suite, run_test_suite, nottest
from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import

from invenio_demosite.testsuite.regression.test_bibupload import wipe_out_record_from_all_tables

WordTable = lazy_import('invenio.legacy.bibindex.engine:WordTable')
get_word_tables = lazy_import('invenio.legacy.bibindex.engine:get_word_tables')
find_affected_records_for_index = lazy_import('invenio.legacy.bibindex.engine:find_affected_records_for_index')
get_recIDs_by_date_authority = lazy_import('invenio.legacy.bibindex.engine:get_recIDs_by_date_authority')
get_recIDs_by_date_bibliographic = lazy_import('invenio.legacy.bibindex.engine:get_recIDs_by_date_bibliographic')
create_range_list = lazy_import('invenio.legacy.bibindex.engine:create_range_list')
beautify_range_list = lazy_import('invenio.legacy.bibindex.engine:beautify_range_list')
get_last_updated_all_indexes = lazy_import('invenio.legacy.bibindex.engine:get_last_updated_all_indexes')

get_index_id_from_index_name = lazy_import('invenio.legacy.bibindex.engine_utils:get_index_id_from_index_name')
get_index_tags = lazy_import('invenio.legacy.bibindex.engine_utils:get_index_tags')
get_tag_indexes = lazy_import('invenio.legacy.bibindex.engine_utils:get_tag_indexes')
get_all_indexes = lazy_import('invenio.legacy.bibindex.engine_utils:get_all_indexes')


CFG_BIBINDEX_INDEX_TABLE_TYPE = lazy_import('invenio.legacy.bibindex.engine_config:CFG_BIBINDEX_INDEX_TABLE_TYPE')
task_low_level_submission = lazy_import('invenio.legacy.bibsched.bibtask:task_low_level_submission')

run_sql = lazy_import('invenio.legacy.dbquery:run_sql')
deserialize_via_marshal = lazy_import('invenio.legacy.dbquery:deserialize_via_marshal')

get_record = lazy_import('invenio.legacy.search_engine:get_record')
get_fieldvalues = lazy_import('invenio.legacy.bibrecord:get_fieldvalues')

get_index_strings_by_control_no = lazy_import('invenio.legacy.bibauthority.engine:get_index_strings_by_control_no')
get_control_nos_from_recID = lazy_import('invenio.legacy.bibauthority.engine:get_control_nos_from_recID')

run_sql_drop_silently = lazy_import('invenio.legacy.bibindex.engine_utils:run_sql_drop_silently')
bibupload = lazy_import('invenio.legacy.bibupload.engine:bibupload')
xml_marc_to_records = lazy_import('invenio.legacy.bibupload.engine:xml_marc_to_records')
record_get_field_value = lazy_import('invenio.legacy.bibrecord:record_get_field_value')
get_max_recid = lazy_import('invenio.legacy.bibsort.engine:get_max_recid')


def reindex_for_type_with_bibsched(index_name, force_all=False, *other_options):
    """Runs bibindex for the specified index and returns the task_id.
       @param index_name: name of the index to reindex
       @param force_all: if it's True function will reindex all records
       not just affected ones
    """
    program = os.path.join(cfg['CFG_BINDIR'], 'bibindex')
    args = ['bibindex', 'bibindex_regression_tests', '-w', index_name, '-u', 'admin']
    args.extend(other_options)
    if force_all:
        args.append("--force")
    task_id = task_low_level_submission(*args)
    COMMAND = "%s %s > /dev/null 2> /dev/null" % (program, str(task_id))
    os.system(COMMAND)
    return task_id


def prepare_for_index_update(index_id, parameters={}):
    """ Prepares SQL query for an update of an index in the idxINDEX table.
        Takes into account remove_stopwords, remove_html_markup, remove_latex_markup,
        tokenizer and last_updated as parameters to change.
        remove_html_markup and remove_latex_markup accepts these values:
                                        '' to leave it unchanged
                                        'Yes' to change it to 'Yes'
                                        'No' to change it to 'No'.
        For remove_stopwords instead of 'Yes' one must give the name of the file (for example: 'stopwords.kb')
        from CFG_ETCDIR/bibrank/ directory pointing at stopwords knowledge base.
        For tokenizer please specify the name of the tokenizer.
        For last_updated provide a date in format: '2013-01-31 00:00:00'
        @param index_id: id of the index to change
        @param parameters: dict with names of parameters and their new values
    """
    if len(parameters) == 0:
        return ''

    parameter_set = False
    query_update = "UPDATE idxINDEX SET "
    for key in parameters:
        if parameters[key]:
            query_update += parameter_set and ", " or ""
            query_update += "%s='%s'" % (key, parameters[key])
            parameter_set = True
    query_update += " WHERE id=%s" % index_id
    return query_update


@nottest
def reindex_word_tables_into_testtables(index_name, recids = None, prefix = 'test', parameters={}, turn_off_virtual_indexes=True):
    """Function for setting up a test enviroment. Reindexes an index with a given name to a
       new temporary table with a given prefix. During the reindexing it changes some parameters
       of chosen index. It's useful for conducting tests concerning the reindexing process.
       Reindexes only idxWORDxxx tables.
       @param index_name: name of the index we want to reindex
       @param recids: None means reindexing all records, set ids of the records to update only part of them
       @param prefix: prefix for the new tabels, if it's set to boolean False function will reindex to original table
       @param parameters: dict with parameters and their new values; for more specific
       description take a look at  'prepare_for_index_update' function.
       @param turn_off_virtual_indexes: if True only specific index will be reindexed
       without connected virtual indexes
    """
    index_id = get_index_id_from_index_name(index_name)
    query_update = prepare_for_index_update(index_id, parameters)
    last_updated = run_sql("""SELECT last_updated FROM idxINDEX WHERE id=%s""" % index_id)[0][0]

    test_tablename = "%s_idxWORD%02d" % (prefix, index_id)
    query_drop_forward_index_table = """DROP TABLE IF EXISTS %sF""" % test_tablename
    query_drop_reversed_index_table = """DROP TABLE IF EXISTS %sR""" % test_tablename

    query_create_forward_index_table = """CREATE TABLE %sF (
                                          id mediumint(9) unsigned NOT NULL auto_increment,
                                          term varchar(50) default NULL,
                                          hitlist longblob,
                                          PRIMARY KEY  (id),
                                          UNIQUE KEY term (term)
                                          ) ENGINE=MyISAM""" % test_tablename
    query_create_reversed_index_table = """CREATE TABLE %sR (
                                           id_bibrec mediumint(9) unsigned NOT NULL,
                                           termlist longblob,
                                           type enum('CURRENT','FUTURE','TEMPORARY') NOT NULL default 'CURRENT',
                                           PRIMARY KEY (id_bibrec,type)
                                           ) ENGINE=MyISAM""" % test_tablename

    run_sql_drop_silently(query_drop_forward_index_table)
    run_sql_drop_silently(query_drop_reversed_index_table)
    run_sql(query_create_forward_index_table)
    run_sql(query_create_reversed_index_table)
    if query_update:
        run_sql(query_update)

    pattern = 'idxWORD'
    if prefix:
        pattern = '%s_idxWORD' % prefix
    wordTable = WordTable(index_name=index_name,
                          index_id=index_id,
                          fields_to_index=get_index_tags(index_name),
                          table_name_pattern= pattern + '%02dF',
                          wordtable_type = CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"],
                          tag_to_tokenizer_map={'8564_u': "BibIndexEmptyTokenizer"},
                          wash_index_terms=50)
    if turn_off_virtual_indexes:
        wordTable.turn_off_virtual_indexes()
    if recids:
        wordTable.add_recIDs(recids, 10000)
    else:
        recIDs_for_index = find_affected_records_for_index([index_name],
                                                 [[1, get_max_recid()]],
                                                                   True)
        bib_recIDs = get_recIDs_by_date_bibliographic([], index_name)
        auth_recIDs = get_recIDs_by_date_authority([], index_name)
        final_recIDs = bib_recIDs | auth_recIDs
        final_recIDs = set(final_recIDs) & set(recIDs_for_index[index_name])
        final_recIDs = beautify_range_list(create_range_list(list(final_recIDs)))
        wordTable.add_recIDs(final_recIDs, 10000)
    return last_updated


@nottest
def remove_reindexed_word_testtables(index_name, prefix = 'test'):
    """
        Removes prefix_idxWORDxxx tables created during tests.
        @param index_name: name of the index
        @param prefix: prefix for the tables
    """
    index_id = get_index_id_from_index_name(index_name)
    test_tablename = "%s_idxWORD%02d" % (prefix, index_id)
    query_drop_forward_index_table = """DROP TABLE IF EXISTS %sF""" % test_tablename
    query_drop_reversed_index_table = """DROP TABLE IF EXISTS %sR""" % test_tablename
    run_sql(query_drop_forward_index_table)
    run_sql(query_drop_reversed_index_table)


class BibIndexRemoveStopwordsTest(InvenioTestCase):
    """Tests remove_stopwords parameter of an index. Changes it in the database
       and reindexes from scratch into a new table to see the diffrence which is brought
       by change. Uses 'title' index.
    """

    test_counter = 0
    reindexed = False

    @classmethod
    def setUp(self):
        """reindexation to new table"""
        if not self.reindexed:
            self.last_updated = reindex_word_tables_into_testtables(
                'title',
                parameters = {'remove_stopwords':'stopwords.kb',
                              'last_updated':'0000-00-00 00:00:00'})
            self.reindexed = True

    @classmethod
    def tearDown(self):
        """cleaning up"""
        self.test_counter += 1
        if self.test_counter == 4:
            remove_reindexed_word_testtables('title')
            reverse_changes = prepare_for_index_update(
                get_index_id_from_index_name('title'),
                parameters = {'remove_stopwords':'No',
                              'last_updated':self.last_updated})
            run_sql(reverse_changes)

    def test_check_occurrences_of_stopwords_in_testable_word_of(self):
        """Tests if term 'of' is in the new reindexed table"""

        query = "SELECT hitlist FROM test_idxWORD08F WHERE term='of'"
        res = run_sql(query)
        self.assertEqual(0, len(res))

    def test_check_occurrences_of_stopwords_in_testable_word_everything(self):
        """Tests if term 'everything' is in the new reindexed table"""

        query = "SELECT hitlist FROM test_idxWORD08F WHERE term='everything'"
        res = run_sql(query)
        self.assertEqual(0, len(res))

    def test_compare_non_stopwords_occurrences_in_original_and_test_tables_word_theory(self):
        """Checks if stopwords removing has no influence on indexation of word 'theory' """

        word = "theori" #theori not theory, because of default stemming for title index
        query = "SELECT hitlist FROM test_idxWORD08F WHERE term='%s'" % word
        iset_removed = "iset_removed"
        iset_original = "iset_original"
        res = run_sql(query)
        if res:
            iset_removed = intbitset(res[0][0])
        query = "SELECT hitlist FROM idxWORD08F WHERE term='%s'" % word
        res = run_sql(query)
        if res:
            iset_original = intbitset(res[0][0])
        self.assertEqual(len(iset_removed), len(iset_original))

    def test_compare_non_stopwords_occurrences_in_original_and_test_tables_word_on(self):
        """Checks if stopwords removing has no influence on indexation of word 'o(n)' """

        word = "o(n)"
        query = "SELECT hitlist FROM test_idxWORD08F WHERE term='%s'" % word
        iset_removed = "iset_removed"
        iset_original = "iset_original"
        res = run_sql(query)
        if res:
            iset_removed = intbitset(res[0][0])
        query = "SELECT hitlist FROM idxWORD08F WHERE term='%s'" % word
        res = run_sql(query)
        if res:
            iset_original = intbitset(res[0][0])
        self.assertEqual(len(iset_removed), len(iset_original))


class BibIndexRemoveLatexTest(InvenioTestCase):
    """Tests remove_latex_markup parameter of an index. Changes it in the database
       and reindexes from scratch into a new table to see the diffrence which is brought
       by change. Uses 'abstract' index.
    """

    test_counter = 0
    reindexed = False

    @classmethod
    def setUp(self):
        """reindexation to new table"""
        if not self.reindexed:
            self.last_updated = reindex_word_tables_into_testtables(
                'abstract',
                parameters = {'remove_latex_markup':'Yes',
                              'last_updated':'0000-00-00 00:00:00'})
            self.reindexed = True

    @classmethod
    def tearDown(self):
        """cleaning up"""
        self.test_counter += 1
        if self.test_counter == 4:
            remove_reindexed_word_testtables('abstract')
            reverse_changes = prepare_for_index_update(
                get_index_id_from_index_name('abstract'),
                parameters = {'remove_latex_markup':'No',
                              'last_updated':self.last_updated})
            run_sql(reverse_changes)


    def test_check_occurrences_after_latex_removal_word_u1(self):
        """Tests how many times experssion 'u(1)' occures"""

        word = "u(1)"
        query = "SELECT hitlist FROM test_idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('abstract'), word)
        res = run_sql(query)
        iset = "iset_change"
        if res:
            iset = intbitset(res[0][0])
        self.assertEqual(3, len(iset))

    def test_check_exact_occurrences_after_latex_removal_word_theta(self):
        """Tests where experssion 'theta' occures"""

        word = "theta"
        query = "SELECT hitlist FROM test_idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('abstract'), word)
        res = run_sql(query)
        ilist = []
        if res:
            iset = intbitset(res[0][0])
            ilist = iset.tolist()
        self.assertEqual([12], ilist)

    def test_compare_occurrences_after_and_before_latex_removal_math_expression(self):
        """Checks if latex removal has no influence on indexation of expression 's(u(n_1)*u(n_2))' """

        word = 's(u(n_1)*u(n_2))'
        query = "SELECT hitlist FROM test_idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('abstract'), word)
        res = run_sql(query)
        ilist_test = []
        if res:
            iset = intbitset(res[0][0])
            ilist_test = iset.tolist()
        word = 's(u(n_1)*u(n_2))'
        query = "SELECT hitlist FROM idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('abstract'), word)
        res = run_sql(query)
        ilist = ["default_not_equal"]
        if res:
            iset = intbitset(res[0][0])
            ilist = iset.tolist()
        self.assertEqual(ilist, ilist_test)

    def test_check_occurrences_latex_expression_with_u1(self):
        """Tests influence of latex removal on record 80"""

        word = '%over u(1)%'
        query = "SELECT hitlist FROM test_idxWORD%02dF WHERE term LIKE '%s'" % (get_index_id_from_index_name('abstract'), word)
        res = run_sql(query)
        ilist = []
        if res:
            iset = intbitset(res[0][0])
            ilist = iset.tolist()
        self.assertEqual([80], ilist)


class BibIndexRemoveHtmlTest(InvenioTestCase):
    """Tests remove_html_markup parameter of an index. Changes it in the database
       and reindexes from scratch into a new table to see the diffrence which is brought
       by change. Uses 'abstract' index.
    """

    test_counter = 0
    reindexed = False

    @classmethod
    def setUp(self):
        """reindexation to new table"""
        if not self.reindexed:
            self.last_updated = reindex_word_tables_into_testtables(
                'abstract',
                parameters = {'remove_html_markup':'Yes',
                              'last_updated':'0000-00-00 00:00:00'})
            self.reindexed = True

    @classmethod
    def tearDown(self):
        """cleaning up"""
        self.test_counter += 1
        if self.test_counter == 2:
            remove_reindexed_word_testtables('abstract')
            reverse_changes = prepare_for_index_update(
                get_index_id_from_index_name('abstract'),
                parameters = {'remove_html_markup':'No',
                              'last_updated':self.last_updated})
            run_sql(reverse_changes)


    def test_check_occurrences_after_html_removal_tag_p(self):
        """Tests if expression 'water-hog</p>' is not indexed after html markup removal"""

        word = 'water-hog</p>'
        query = "SELECT hitlist FROM test_idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('abstract'), word)
        res = run_sql(query)
        ilist = []
        if res:
            iset = intbitset(res[0][0])
            ilist = iset.tolist()
        self.assertEqual(0, len(ilist))


    def test_check_occurrences_after_and_before_html_removal_word_style(self):
        """Tests html markup removal influence on expression 'style="width' """

        word = 'style="width'
        query = "SELECT hitlist FROM test_idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('abstract'), word)
        res = run_sql(query)
        ilist_test = []
        if res:
            iset = intbitset(res[0][0])
            ilist_test = iset.tolist()
        query = "SELECT hitlist FROM idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('abstract'), word)
        res = run_sql(query)
        ilist = []
        if res:
            iset = intbitset(res[0][0])
            ilist = iset.tolist()
        self.assertNotEqual(ilist, ilist_test)


class BibIndexYearIndexTest(InvenioTestCase):
    """
        Checks year index. Tests are diffrent than those inside WebSearch module because
        they only test content and reindexation and not the search itself.
    """

    test_counter = 0
    reindexed = False

    @classmethod
    def setUp(self):
        """reindexation to new table"""
        if not self.reindexed:
            self.last_updated = reindex_word_tables_into_testtables(
                'year',
                parameters = {'last_updated':'0000-00-00 00:00:00'})
            self.reindexed = True


    @classmethod
    def tearDown(self):
        """cleaning up"""
        self.test_counter += 1
        if self.test_counter == 3:
            remove_reindexed_word_testtables('year')
            reverse_changes = prepare_for_index_update(
                get_index_id_from_index_name('year'),
                parameters = {'last_updated':self.last_updated})
            run_sql(reverse_changes)


    def test_occurrences_in_year_index_1973(self):
        """checks content of year index for year 1973"""
        word = '1973'
        query = "SELECT hitlist FROM test_idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('year'), word)
        res = run_sql(query)
        ilist = []
        if res:
            iset = intbitset(res[0][0])
            ilist = iset.tolist()
        self.assertEqual([34], ilist)


    def test_occurrences_in_year_index_2001(self):
        """checks content of year index for year 2001"""
        word = '2001'
        query = "SELECT hitlist FROM test_idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('year'), word)
        res = run_sql(query)
        ilist = []
        if res:
            iset = intbitset(res[0][0])
            ilist = iset.tolist()
        self.assertEqual([2, 11, 12, 15], ilist)


    def test_comparison_for_number_of_items(self):
        """checks the reindexation of year index"""
        query_test = "SELECT count(*) FROM test_idxWORD%02dF" % get_index_id_from_index_name('year')
        query_orig = "SELECT count(*) FROM idxWORD%02dF" % get_index_id_from_index_name('year')
        num_orig = 0
        num_test = 1
        res = run_sql(query_test)
        if res:
            num_test = res[0][0]
        res = run_sql(query_orig)
        if res:
            num_orig = res[0][0]
        self.assertEqual(num_orig, num_test)



class BibIndexAuthorCountIndexTest(InvenioTestCase):
    """
       Checks author count index. Tests are diffrent than those inside WebSearch module because
       they only test content and reindexation and not the search itself.
    """

    test_counter = 0
    reindexed = False

    @classmethod
    def setUp(self):
        """reindexation to new table"""
        if not self.reindexed:
            self.last_updated = reindex_word_tables_into_testtables(
                'authorcount',
                parameters = {'last_updated':'0000-00-00 00:00:00'})
            self.reindexed = True

    @classmethod
    def tearDown(self):
        """cleaning up"""
        self.test_counter += 1
        if self.test_counter == 2:
            remove_reindexed_word_testtables('authorcount')
            reverse_changes = prepare_for_index_update(
                get_index_id_from_index_name('authorcount'),
                parameters = {'last_updated':self.last_updated})
            run_sql(reverse_changes)


    def test_occurrences_in_authorcount_index(self):
        """checks content of authorcount index for papers with 4 authors"""
        word = '4'
        query = "SELECT hitlist FROM test_idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('authorcount'), word)
        res = run_sql(query)
        ilist = []
        if res:
            iset = intbitset(res[0][0])
            ilist = iset.tolist()
        self.assertEqual([51, 54, 59, 66, 92, 96], ilist)


    def test_comparison_for_number_of_items(self):
        """checks the reindexation of authorcount index"""
        query_test = "SELECT count(*) FROM test_idxWORD%02dF" % get_index_id_from_index_name('authorcount')
        query_orig = "SELECT count(*) FROM idxWORD%02dF" % get_index_id_from_index_name('authorcount')
        num_orig = 0
        num_test = 1
        res = run_sql(query_test)
        if res:
            num_test = res[0][0]
        res = run_sql(query_orig)
        if res:
            num_orig = res[0][0]
        self.assertEqual(num_orig, num_test)


class BibIndexItemCountIndexTest(InvenioTestCase):
    """
       Checks item count index. Checks a number of copies of books for records
       as well as occurrences of particular number of copies in test data.
    """

    def setUp(self):
        index_name = 'itemcount'
        index_id = get_index_id_from_index_name(index_name)
        index_tags = get_word_tables([index_name])[0][2]

        query = """SELECT termlist FROM idxWORD%02dR
                   WHERE id_bibrec=21""" % index_id
        count = int(deserialize_via_marshal(run_sql(query)[0][0])[0])
        # crcITEM table wasn't updated before initial indexing
        # we need to update ItemCount index if count == 0
        if count == 0:
            wt = WordTable(index_name=index_name,
                           index_id=index_id,
                           fields_to_index=index_tags,
                           table_name_pattern='idxWORD%02dF',
                           wordtable_type = CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"],
                           tag_to_tokenizer_map={})
            wt.add_recIDs([[1, 100]], 10000)

    def test_occurrences_in_itemcount_index_two_copies(self):
        """checks content of itemcount index for records with two copies of a book"""
        word = '2'
        query = "SELECT hitlist FROM idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('itemcount'), word)
        res = run_sql(query)
        ilist = []
        if res:
            iset = intbitset(res[0][0])
            ilist = iset.tolist()
        self.assertEqual([31, 34], ilist)

    def test_records_for_number_of_copies_record1(self):
        """checks content of itemcount index for record: 1"""
        query = "SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=1" \
                 % get_index_id_from_index_name('itemcount')
        res = run_sql(query)
        self.assertEqual(deserialize_via_marshal(res[0][0]),['0'])

    def test_records_for_number_of_copies_record30(self):
        """checks content of itemcount index for record: 30"""
        query = "SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=30" \
                 % get_index_id_from_index_name('itemcount')
        res = run_sql(query)
        self.assertEqual(deserialize_via_marshal(res[0][0]),['1'])

    def test_records_for_number_of_copies_record32(self):
        """checks content of itemcount index for record: 32"""
        query = "SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=32" \
                 % get_index_id_from_index_name('itemcount')
        res = run_sql(query)
        self.assertEqual(deserialize_via_marshal(res[0][0]),['3'])


class BibIndexFiletypeIndexTest(InvenioTestCase):
    """
       Checks filetype index. Tests are diffrent than those inside WebSearch module because
       they only test content and indexation and not the search itself.
    """

    def test_occurances_of_tif_filetype(self):
        """tests which records has file with 'tif' extension"""
        query = "SELECT hitlist FROM idxWORD%02dF where term='tif'" \
                % get_index_id_from_index_name('filetype')
        res = run_sql(query)
        value = []
        if res:
            iset = intbitset(res[0][0])
            value = iset.tolist()
        self.assertEqual(sorted(value), [66, 71])

    def test_filetypes_of_records(self):
        """tests files extensions of record 1 and 77"""
        query1 = "SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=1" \
                 % get_index_id_from_index_name('filetype')
        query2 = "SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=77" \
                 % get_index_id_from_index_name('filetype')
        res1 = run_sql(query1)
        res2 = run_sql(query2)
        set1 = deserialize_via_marshal(res1[0][0])
        set2 = deserialize_via_marshal(res2[0][0])
        self.assertEqual(set1, ['gif', 'jpg'])
        self.assertEqual(set2, ['pdf', 'ps.gz'])


class BibIndexJournalIndexTest(InvenioTestCase):
    """
        Checks journal index. Tests are diffrent than those inside WebSearch module because
        they only test content and reindexation and not the search itself.
    """
    test_counter = 0
    reindexed = False

    @classmethod
    def setUp(self):
        """reindexation to new table"""
        if not self.reindexed:
            self.last_updated = reindex_word_tables_into_testtables(
                'journal',
                parameters = {'last_updated':'0000-00-00 00:00:00'})
            self.reindexed = True

    @classmethod
    def tearDown(self):
        """cleaning up"""
        self.test_counter += 1
        if self.test_counter == 2:
            remove_reindexed_word_testtables('journal')
            reverse_changes = prepare_for_index_update(
                get_index_id_from_index_name('journal'),
                parameters = {'last_updated':self.last_updated})
            run_sql(reverse_changes)


    def test_occurrences_in_journal_index(self):
        """checks content of journal index for phrase: 'prog. theor. phys.' """
        word = 'prog. theor. phys.'
        query = "SELECT hitlist FROM test_idxWORD%02dF WHERE term='%s'" % (get_index_id_from_index_name('journal'), word)
        res = run_sql(query)
        ilist = []
        if res:
            iset = intbitset(res[0][0])
            ilist = iset.tolist()
        self.assertEqual([86], ilist)


    def test_comparison_for_number_of_items(self):
        """checks the reindexation of journal index"""
        query_test = "SELECT count(*) FROM test_idxWORD%02dF" % get_index_id_from_index_name('journal')
        query_orig = "SELECT count(*) FROM idxWORD%02dF" % get_index_id_from_index_name('journal')
        num_orig = 0
        num_test = 1
        res = run_sql(query_test)
        if res:
            num_test = res[0][0]
        res = run_sql(query_orig)
        if res:
            num_orig = res[0][0]
        self.assertEqual(num_orig, num_test)


class BibIndexCJKTokenizerTitleIndexTest(InvenioTestCase):
    """
       Checks CJK tokenization on title index.
    """
    test_counter = 0
    reindexed = False

    @classmethod
    def setUp(self):
        """reindexation to new table"""
        if not self.reindexed:
            self.last_updated = reindex_word_tables_into_testtables(
                'title',
                parameters = {'tokenizer':'BibIndexCJKTokenizer',
                              'last_updated':'0000-00-00 00:00:00'})
            self.reindexed = True

    @classmethod
    def tearDown(self):
        """cleaning up"""
        self.test_counter += 1
        if self.test_counter == 2:
            remove_reindexed_word_testtables('title')
            reverse_changes = prepare_for_index_update(
                get_index_id_from_index_name('title'),
                parameters = {'tokenizer':'BibIndexDefaultTokenizer',
                              'last_updated':self.last_updated})
            run_sql(reverse_changes)


    def test_splliting_and_indexing_CJK_characters_forward_table(self):
        """CJK Tokenizer - searching for a CJK term in title index, forward table"""
        query = "SELECT * from test_idxWORD%02dF where term='\xe6\x95\xac'" % get_index_id_from_index_name('title')
        res = run_sql(query)
        iset = []
        if res:
            iset = intbitset(res[0][2])
            iset = iset.tolist()
        self.assertEqual(iset, [104])

    def test_splliting_and_indexing_CJK_characters_reversed_table(self):
        """CJK Tokenizer - comparing terms for record with chinese poetry in title index, reverse table"""
        query = "SELECT * from test_idxWORD%02dR where id_bibrec='104'" % get_index_id_from_index_name('title')
        res = run_sql(query)
        iset = []
        if res:
            iset = deserialize_via_marshal(res[0][1])
        self.assertEqual(iset, ['\xe6\x95\xac', '\xe7\x8d\xa8', '\xe4\xba\xad', '\xe5\x9d\x90'])


class BibIndexAuthorityRecordTest(InvenioTestCase):
    """Test if BibIndex correctly knows when to update the index for a
    bibliographic record if it is dependent upon an authority record changed
    within the given date range"""

    def test_authority_record_recently_updated(self):
        """bibindex - reindexing after recently changed authority record"""
        from invenio.legacy.bibindex.engine_config import (
            CFG_BIBINDEX_ADDING_RECORDS_STARTED_STR,
            CFG_BIBINDEX_UPDATE_MESSAGE)

        authRecID = 118
        bibRecID = 9
        index_name = 'author'
        table = "idxWORD%02dF" % get_index_id_from_index_name(index_name)
        reindex_for_type_with_bibsched(index_name)
        run_sql("UPDATE bibrec SET modification_date = now() WHERE id = %s", (authRecID,))
        # run bibindex again
        task_id = reindex_for_type_with_bibsched(index_name, force_all=True)
        filename = os.path.join(cfg['CFG_LOGDIR'], 'bibsched_task_' + str(task_id) + '.log')
        _file = open(filename)
        text = _file.read() # small file
        _file.close()
        self.assertTrue(text.find(CFG_BIBINDEX_UPDATE_MESSAGE) >= 0)
        self.assertTrue(text.find(CFG_BIBINDEX_ADDING_RECORDS_STARTED_STR % (table, 1, get_max_recid())) >= 0)

    def test_authority_record_enriched_index(self):
        """bibindex - test whether reverse index for bibliographic record
        contains words from referenced authority records"""
        bibRecID = 9
        authority_string = 'jonathan'
        index_name = 'author'
        table = "idxWORD%02dR" % get_index_id_from_index_name(index_name)

        reindex_for_type_with_bibsched(index_name, force_all=True)
        self.assertTrue(
            authority_string in deserialize_via_marshal(
                run_sql("SELECT termlist FROM %s WHERE id_bibrec = %s" % (table, bibRecID))[0][0]
            )
        )

    def test_indexing_of_deleted_authority_record(self):
        """bibindex - no info for indexing from deleted authority record"""
        recID = 119 # deleted record
        control_nos = get_control_nos_from_recID(recID)
        info = get_index_strings_by_control_no(control_nos[0])
        self.assertEqual([], info)

    def test_authority_record_get_values_by_bibrecID_from_tag(self):
        """bibindex - find authors in authority records for given bibrecID"""
        tags = ['100__a']
        bibRecID = 9
        values = []
        for tag in tags:
            authority_tag = tag[0:3] + "__0"
            control_nos = get_fieldvalues(bibRecID, authority_tag)
            for control_no in control_nos:
                new_strings = get_index_strings_by_control_no(control_no)
                values.extend(new_strings)
        self.assertTrue('Ellis, Jonathan Richard' in values)


def insert_record_one_and_second_revision():
    """Inserts test record no. 1 and a second revision for that record"""

    rev1 = """<record>
              <controlfield tag="001">123456789</controlfield>
              <controlfield tag="005">20110101000000.0</controlfield>
              <datafield tag ="100" ind1=" " ind2=" ">
                <subfield code="a">Close, John</subfield>
                <subfield code="u">DESY</subfield>
              </datafield>
              <datafield tag="245" ind1=" " ind2=" ">
                <subfield code="a">Particles world</subfield>
              </datafield>
            </record>"""
    rev1_final = rev1.replace('<controlfield tag="001">123456789</controlfield>','')
    rev1_final = rev1_final.replace('<controlfield tag="005">20110101000000.0</controlfield>','')

    rev2 = rev1.replace('<subfield code="a">Close, John</subfield>', '<subfield code="a">Dawkins, Richard</subfield>')
    rev2 = rev2.replace('Particles world', 'Particles universe')

    rec1 = xml_marc_to_records(rev1_final)
    res = bibupload(rec1[0], opt_mode='insert')
    _id = res[1]
    rec = get_record(_id)
    _rev = record_get_field_value(rec, '005', '', '')

    #need to index for the first time
    indexes = get_all_indexes(virtual=False)
    wtabs = get_word_tables(indexes)
    for index_id, index_name, index_tags in wtabs:
        wordTable = WordTable(index_name=index_name,
                              index_id=index_id,
                              fields_to_index=index_tags,
                              table_name_pattern='idxWORD%02dF',
                              wordtable_type = CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"],
                              tag_to_tokenizer_map={'8564_u': "BibIndexEmptyTokenizer"},
                              wash_index_terms=50)
        wordTable.add_recIDs([[_id, _id]], 10000)

    #upload the second revision, but don't index
    rev2_final = rev2.replace('123456789', str(_id))
    rev2_final = rev2_final.replace('20110101000000.0', _rev)
    rec2 = xml_marc_to_records(rev2_final)
    res = bibupload(rec2[0], opt_mode='correct')

    return _id


def insert_record_two_and_second_revision():
    """Inserts test record no. 2 and a revision for that record"""

    rev1 = """<record>
              <controlfield tag="001">123456789</controlfield>
              <controlfield tag="005">20110101000000.0</controlfield>
              <datafield tag ="100" ind1=" " ind2=" ">
                <subfield code="a">Locke, John</subfield>
                <subfield code="u">UNITRA</subfield>
              </datafield>
              <datafield tag="245" ind1=" " ind2=" ">
                <subfield code="a">Collision course</subfield>
              </datafield>
            </record>"""
    rev1_final = rev1.replace('<controlfield tag="001">123456789</controlfield>','')
    rev1_final = rev1_final.replace('<controlfield tag="005">20110101000000.0</controlfield>','')

    rev2 = rev1.replace('Collision course', 'Course of collision')

    rec1 = xml_marc_to_records(rev1_final)
    res = bibupload(rec1[0], opt_mode='insert')
    id_bibrec = res[1]
    rec = get_record(id_bibrec)
    _rev = record_get_field_value(rec, '005', '', '')

    #need to index for the first time
    indexes = get_all_indexes(virtual=False)
    wtabs = get_word_tables(indexes)
    for index_id, index_name, index_tags in wtabs:
        wordTable = WordTable(index_name=index_name,
                              index_id=index_id,
                              fields_to_index=index_tags,
                              table_name_pattern='idxWORD%02dF',
                              wordtable_type = CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"],
                              tag_to_tokenizer_map={'8564_u': "BibIndexEmptyTokenizer"},
                              wash_index_terms=50)
        wordTable.add_recIDs([[id_bibrec, id_bibrec]], 10000)

    #upload the second revision, but don't index
    rev2_final = rev2.replace('123456789', str(id_bibrec))
    rev2_final = rev2_final.replace('20110101000000.0', _rev)
    rec2 = xml_marc_to_records(rev2_final)
    res = bibupload(rec2[0], opt_mode='correct')

    return id_bibrec


def create_index_tables(index_id):
    query_create = """CREATE TABLE IF NOT EXISTS idxWORD%02dF (
                      id mediumint(9) unsigned NOT NULL auto_increment,
                      term varchar(50) default NULL,
                      hitlist longblob,
                      PRIMARY KEY  (id),
                      UNIQUE KEY term (term)
                    ) ENGINE=MyISAM"""

    query_create_r = """CREATE TABLE IF NOT EXISTS idxWORD%02dR (
                        id_bibrec mediumint(9) unsigned NOT NULL,
                        termlist longblob,
                        type enum('CURRENT','FUTURE','TEMPORARY') NOT NULL default 'CURRENT',
                        PRIMARY KEY (id_bibrec,type)
                      ) ENGINE=MyISAM"""
    run_sql(query_create % index_id)
    run_sql(query_create_r % index_id)


def drop_index_tables(index_id):
    query_drop = """DROP TABLE IF EXISTS idxWORD%02d%s"""
    run_sql(query_drop % (index_id, "F"))
    run_sql(query_drop % (index_id, "R"))


def create_virtual_index(index_id, dependent_indexes):
    """creates new virtual index and binds it to specific dependent indexes"""
    query = """INSERT INTO idxINDEX (id, name, tokenizer) VALUES (%s, 'testindex', 'BibIndexDefaultTokenizer')"""
    run_sql(query % index_id)
    query = """INSERT INTO idxINDEX_idxINDEX VALUES (%s, %s)"""
    for index in dependent_indexes:
        run_sql(query % (index_id, get_index_id_from_index_name(index)))
    create_index_tables(index_id)


def remove_virtual_index(index_id):
    """removes tables and other traces after virtual index"""
    drop_index_tables(index_id)
    query = """DELETE FROM idxINDEX WHERE id=%s""" % index_id
    run_sql(query)
    query = """DELETE FROM idxINDEX_idxINDEX WHERE id_virtual=%s"""
    run_sql(query % index_id)


class BibIndexFindingAffectedIndexes(InvenioTestCase):
    """
    Checks if function 'find_affected_records_for_index'
    works correctly.
    """

    counter = 0
    indexes = ['global', 'fulltext', 'caption', 'journal', 'miscellaneous', 'reportnumber', 'year']

    @classmethod
    def setUp(self):
        if self.counter == 0:
            self.last_updated = dict(get_last_updated_all_indexes())
            res = run_sql("SELECT job_date FROM hstRECORD WHERE id_bibrec=10 AND affected_fields<>''")
            self.hst_date = res[0][0]
            date_to_set = self.hst_date - timedelta(seconds=1)
            for index in self.indexes:
                run_sql("""UPDATE idxINDEX SET last_updated=%s
                           WHERE name=%s""", (str(date_to_set), index))

    @classmethod
    def tearDown(self):
        self.counter += 1
        if self.counter >= 8:
            for index in self.indexes:
                run_sql("""UPDATE idxINDEX SET last_updated=%s
                           WHERE name=%s""", (self.last_updated[index], index))

    def test_find_proper_indexes(self):
        """bibindex - checks if affected indexes are found correctly"""
        records_for_indexes = find_affected_records_for_index(get_all_indexes(virtual=False),
                                                              [[1,20]])
        self.assertEqual(sorted(['miscellaneous', 'fulltext', 'caption', 'journal', 'reportnumber', 'year']),
                         sorted(records_for_indexes.keys()))

    def test_find_proper_recrods_for_miscellaneous_index(self):
        """bibindex - checks if affected recids are found correctly for miscellaneous index"""
        records_for_indexes = find_affected_records_for_index(get_all_indexes(virtual=False),
                                                              [[1,20]])
        self.assertEqual(records_for_indexes['miscellaneous'],
                         [1, 2, 3, 4, 5, 6, 7, 10, 12, 14, 17, 18])

    def test_find_proper_records_for_year_index(self):
        """bibindex - checks if affected recids are found correctly for year index"""
        records_for_indexes = find_affected_records_for_index(get_all_indexes(virtual=False),
                                                              [[1,20]])
        self.assertEqual(records_for_indexes['year'],
                         [1, 2, 3, 4, 5, 6, 7, 10, 12, 14, 17, 18])

    def test_find_proper_records_for_caption_index(self):
        """bibindex - checks if affected recids are found correctly for caption index"""
        records_for_indexes = find_affected_records_for_index(get_all_indexes(virtual=False),
                                                              [[1,100]])
        self.assertEqual(records_for_indexes['caption'],
                         [1, 2, 3, 4, 5, 6, 7, 10, 12, 55, 98])

    def test_find_proper_records_for_journal_index(self):
        """bibindex - checks if affected recids are found correctly for journal index"""
        records_for_indexes = find_affected_records_for_index(get_all_indexes(virtual=False),
                                                              [[1,100]])
        self.assertEqual(records_for_indexes['journal'],
                         [6, 7, 10, 17, 18])

    def test_find_proper_records_specified_only_year(self):
        """bibindex - checks if affected recids are found correctly for year index if we specify only year index as input"""
        records_for_indexes = find_affected_records_for_index(["year"], [[1, 100]])
        self.assertEqual(records_for_indexes["year"],
                         [1, 2, 3, 4, 5, 6, 7, 10, 12, 14, 17, 18, 55])

    def test_find_proper_records_force_all(self):
        """bibindex - checks if all recids will be assigned to all specified indexes"""
        records_for_indexes = find_affected_records_for_index(["year", "title"], [[10, 15]], True)
        self.assertEqual(records_for_indexes["year"], records_for_indexes["title"])
        self.assertEqual(records_for_indexes["year"], [10, 11, 12, 13, 14, 15])

    def test_find_proper_records_nothing_for_title_index(self):
        """bibindex - checks if nothing was found for title index in range of records: 1 - 20"""
        records_for_indexes = find_affected_records_for_index(["title"], [[1, 20]])
        self.assertRaises(KeyError, lambda :records_for_indexes["title"])




class BibIndexIndexingAffectedIndexes(InvenioTestCase):

    started = False
    records = []
    counter = 0

    @classmethod
    def setUp(self):
        self.counter += 1
        if not self.started:
            self.records.append(insert_record_one_and_second_revision())
            self.records.append(insert_record_two_and_second_revision())
            records_for_indexes = find_affected_records_for_index(get_all_indexes(virtual=False),
                                                                  [self.records])
            wtabs = get_word_tables(records_for_indexes.keys())
            for index_id, index_name, index_tags in wtabs:
                wordTable = WordTable(index_name=index_name,
                                      index_id=index_id,
                                      fields_to_index=index_tags,
                                      table_name_pattern='idxWORD%02dF',
                                      wordtable_type = CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"],
                                      tag_to_tokenizer_map={'8564_u': "BibIndexEmptyTokenizer"},
                                      wash_index_terms=50)
                wordTable.add_recIDs([self.records], 10000)
            self.started = True

    @classmethod
    def tearDown(self):
        if self.counter == 3:
            for rec in self.records:
                wipe_out_record_from_all_tables(rec)
            indexes = get_all_indexes(virtual=False)
            wtabs = get_word_tables(indexes)
            for index_id, index_name, index_tags in wtabs:
                wordTable = WordTable(index_name=index_name,
                                      index_id=index_id,
                                      fields_to_index=index_tags,
                                      table_name_pattern='idxWORD%02dF',
                                      wordtable_type = CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"],
                                      tag_to_tokenizer_map={'8564_u': "BibIndexEmptyTokenizer"},
                                      wash_index_terms=50)
                wordTable.del_recIDs([self.records])


    def test_proper_content_in_title_index(self):
        """bibindex - checks reindexation of title index for test records.."""
        index_id = get_index_id_from_index_name('title')
        query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec IN (""" % (index_id,)
        query = query + ", ".join(map(str, self.records)) + ")"
        resp = run_sql(query)
        affiliation_rec1 = deserialize_via_marshal(resp[0][0])
        affiliation_rec2 = deserialize_via_marshal(resp[1][0])
        self.assertEqual(['univers', 'particl'], affiliation_rec1)
        self.assertEqual(['of', 'cours', 'collis'], affiliation_rec2)


    def test_proper_content_in_author_index(self):
        """bibindex - checks reindexation of author index for test records.."""
        index_id = get_index_id_from_index_name('author')
        query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec IN (""" % (index_id,)
        query = query + ", ".join(map(str, self.records)) + ")"
        resp = run_sql(query)
        author_rec1 = deserialize_via_marshal(resp[0][0])
        author_rec2 = deserialize_via_marshal(resp[1][0])
        self.assertEqual(['dawkins', 'richard', ], author_rec1)
        self.assertEqual(['john', 'locke'], author_rec2)


    def test_proper_content_in_global_index(self):
        """bibindex - checks reindexation of global index for test records.."""
        index_id = get_index_id_from_index_name('global')
        query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec IN (""" % (index_id,)
        query = query + ", ".join(map(str, self.records)) + ")"
        resp = run_sql(query)
        global_rec1 = deserialize_via_marshal(resp[0][0])
        global_rec2 = deserialize_via_marshal(resp[1][0])
        self.assertEqual(True, 'dawkin' in global_rec1)
        self.assertEqual(False, 'close' in global_rec1)
        self.assertEqual(True, 'univers' in global_rec1)
        self.assertEqual(True, 'john' in global_rec2)
        self.assertEqual(False, 'john' in global_rec1)


class BibIndexFindingIndexesForTags(InvenioTestCase):
    """ Tests function 'get_tag_indexes' """

    def test_fulltext_tag_virtual_indexes_on(self):
        """bibindex - checks if 'get_tag_indexes' for tag 8564_u will find only 'fulltext' index"""
        self.assertEqual(('fulltext',), zip(*get_tag_indexes('8564_u'))[1])

    def test_title_tag_virtual_indexes_on(self):
        """bibindex - checks if 'get_tag_indexes' for tag 245__% will find also 'global' index"""
        self.assertEqual(('title', 'exacttitle', 'global'), zip(*get_tag_indexes('245__%'))[1])

    def test_title_tag_virtual_indexes_off(self):
        """bibindex - checks if 'get_tag_indexes' for tag 245__% wont find 'global' index (with virtual=False)"""
        self.assertEqual(('title', 'exacttitle'), zip(*get_tag_indexes('245__%', virtual=False))[1])

    def test_author_tag_virtual_indexes_on(self):
        """bibindex - checks 'get_tag_indexes' for tag '100'"""
        self.assertEqual(('author', 'affiliation', 'exactauthor', 'firstauthor',
                          'exactfirstauthor', 'authorcount', 'authorityauthor',
                          'miscellaneous', 'global'),
                         zip(*get_tag_indexes('100'))[1])

    def test_author_exact_tag_virtual_indexes_off(self):
        """bibindex - checks 'get_tag_indexes' for tag '100__a'"""
        self.assertEqual(('author', 'exactauthor', 'firstauthor',
                          'exactfirstauthor', 'authorcount',
                          'authorityauthor', 'miscellaneous'),
                         zip(*get_tag_indexes('100__a', virtual=False))[1])

    def test_wide_tag_virtual_indexes_off(self):
        """bibindex - checks 'get_tag_indexes' for tag like '86%'"""
        self.assertEqual(('miscellaneous',), zip(*get_tag_indexes('86%', virtual=False))[1])

    def test_909_tags_in_misc_index(self):
        """bibindex - checks connection between misc index and tags: 909C1%, 909C4%"""
        self.assertEqual(('miscellaneous',), zip(*get_tag_indexes('909C1%', virtual=False))[1])
        self.assertEqual('miscellaneous' in zip(*get_tag_indexes('909C4%', virtual=False))[1], False)

    def test_year_tag_virtual_indexes_on(self):
        """bibindex - checks 'get_tag_indexes' for tag 909C0y"""
        self.assertEqual(('year', 'global'), zip(*get_tag_indexes('909C0y'))[1])

    def test_wide_tag_authority_index_virtual_indexes_off(self):
        """bibindex - checks 'get_tag_indexes' for tag like '15%'"""
        self.assertEqual(('authoritysubject', 'miscellaneous'), zip(*get_tag_indexes('15%',virtual=False))[1])


class BibIndexFindingTagsForIndexes(InvenioTestCase):
    """ Tests function 'get_index_tags' """


    def test_tags_for_author_index(self):
        """bibindex - checks if 'get_index_tags' find proper tags for 'author' index """
        self.assertEqual(get_index_tags('author'), ['100__a', '700__a'])

    def test_tags_for_global_index_virtual_indexes_off(self):
        """bibindex - checks if 'get_index_tags' find proper tags for 'global' index """
        self.assertEqual(get_index_tags('global', virtual=False),[])

    def test_tags_for_global_index_virtual_indexes_on(self):
        """bibindex - checks if 'get_index_tags' find proper tags for 'global' index """
        tags = get_index_tags('global')
        self.assertEqual('86%' in tags, True)
        self.assertEqual('100__a' in tags, True)
        self.assertEqual('245__%' in tags, True)


class BibIndexGlobalIndexContentTest(InvenioTestCase):
    """ Tests if virtual global index is correctly indexed"""

    def is_part_of(self, container, content):
        """checks if content is a part of container"""
        ctr = set(container)
        cont = set(content)
        return cont.issubset(ctr)

    def test_title_index_compatibility_reversed_table(self):
        """bibindex - checks if the same words are in title and global index, reversed table"""
        global_id = get_index_id_from_index_name('global')
        title_id = get_index_id_from_index_name('title')
        for rec in range(1, 4):
            query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=%s""" % (title_id, rec)
            res = run_sql(query)
            termlist_title = deserialize_via_marshal(res[0][0])
            query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=%s""" % (global_id, rec)
            glob = run_sql(query)
            termlist_global = deserialize_via_marshal(glob[0][0])
            self.assertEqual(self.is_part_of(termlist_global, termlist_title), True)

    def test_abstract_index_compatibility_reversed_table(self):
        """bibindex - checks if the same words are in abstract and global index, reversed table"""
        global_id = get_index_id_from_index_name('global')
        abstract_id = get_index_id_from_index_name('abstract')
        for rec in range(6, 9):
            query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=%s""" % (abstract_id, rec)
            res = run_sql(query)
            termlist_abstract = deserialize_via_marshal(res[0][0])
            query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=%s""" % (global_id, rec)
            glob = run_sql(query)
            termlist_global = deserialize_via_marshal(glob[0][0])
            self.assertEqual(self.is_part_of(termlist_global, termlist_abstract), True)

    def test_misc_index_compatibility_reversed_table(self):
        """bibindex - checks if the same words are in misc and global index, reversed table"""
        global_id = get_index_id_from_index_name('global')
        misc_id = get_index_id_from_index_name('miscellaneous')
        for rec in range(10, 14):
            query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=%s""" % (misc_id, rec)
            res = run_sql(query)
            termlist_misc = deserialize_via_marshal(res[0][0])
            query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=%s""" % (global_id, rec)
            glob = run_sql(query)
            termlist_global = deserialize_via_marshal(glob[0][0])
            self.assertEqual(self.is_part_of(termlist_global, termlist_misc), True)

    def test_journal_index_compatibility_forward_table(self):
        """bibindex - checks if the same words are in journal and global index, forward table"""
        global_id = get_index_id_from_index_name('global')
        journal_id = get_index_id_from_index_name('journal')
        query = """SELECT term FROM idxWORD%02dF""" % journal_id
        res = zip(*run_sql(query))[0]
        query = """SELECT term FROM idxWORD%02dF""" % global_id
        glob = zip(*run_sql(query))[0]
        self.assertEqual(self.is_part_of(glob, res), True)

    def test_keyword_index_compatibility_forward_table(self):
        """bibindex - checks if the same pairs are in keyword and global index, forward table"""
        global_id = get_index_id_from_index_name('global')
        keyword_id = get_index_id_from_index_name('keyword')
        query = """SELECT term FROM idxPAIR%02dF""" % keyword_id
        res = zip(*run_sql(query))[0]
        query = """SELECT term FROM idxPAIR%02dF""" % global_id
        glob = zip(*run_sql(query))[0]
        self.assertEqual(self.is_part_of(glob, res), True)

    def test_affiliation_index_compatibility_forward_table(self):
        """bibindex - checks if the same phrases are in affiliation and global index, forward table"""
        global_id = get_index_id_from_index_name('global')
        affiliation_id = get_index_id_from_index_name('affiliation')
        query = """SELECT term FROM idxPHRASE%02dF""" % affiliation_id
        res = zip(*run_sql(query))[0]
        query = """SELECT term FROM idxPHRASE%02dF""" % global_id
        glob = zip(*run_sql(query))[0]
        self.assertEqual(self.is_part_of(glob, res), True)


class BibIndexVirtualIndexAlsoChangesTest(InvenioTestCase):
    """ Tests if virtual index changes after changes in dependent index"""

    counter = 0
    indexes = ["title"]
    _id = 39

    @classmethod
    def prepare_virtual_index(self):
        """creates new virtual index and binds it to specific normal index"""
        create_virtual_index(self._id, self.indexes)
        wtabs = get_word_tables(self.indexes)
        for index_id, index_name, index_tags in wtabs:
            wordTable = WordTable(index_name=index_name,
                                  index_id=index_id,
                                  fields_to_index=index_tags,
                                  table_name_pattern='idxWORD%02dF',
                                  wordtable_type=CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"],
                                  tag_to_tokenizer_map={'8564_u': "BibIndexEmptyTokenizer"},
                                  wash_index_terms=50)
            wordTable.add_recIDs([[1, 10]], 1000)

    @classmethod
    def reindex_virtual_index(self, special_tokenizer=False):
        """reindexes virtual and dependent indexes with different tokenizer"""
        def tokenize_for_words(phrase):
            return phrase.split(" ")

        wtabs = get_word_tables(self.indexes)
        for index_id, index_name, index_tags in wtabs:
            wordTable = WordTable(index_name=index_name,
                                  index_id=index_id,
                                  fields_to_index=index_tags,
                                  table_name_pattern='idxWORD%02dF',
                                  wordtable_type=CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"],
                                  tag_to_tokenizer_map={'8564_u': "BibIndexEmptyTokenizer"},
                                  wash_index_terms=50)
            if special_tokenizer == True:
                wordTable.default_tokenizer_function = tokenize_for_words
            wordTable.add_recIDs([[1, 10]], 1000)

    @classmethod
    def setUp(self):
        self.counter += 1
        if self.counter == 1:
            self.prepare_virtual_index()
        elif self.counter == 2:
            self.reindex_virtual_index(special_tokenizer=True)

    @classmethod
    def tearDown(self):
        if self.counter == 3:
            self.reindex_virtual_index()
        elif self.counter == 4:
            remove_virtual_index(self._id)

    def test_virtual_index_1_has_10_records(self):
        """bibindex - checks if virtual index was filled with only ten records from title index"""
        query = "SELECT count(*) FROM idxWORD%02dR" % self._id
        self.assertEqual(10, run_sql(query)[0][0])

    def test_virtual_index_2_correct_content_record_1(self):
        """bibindex - after reindexing with different tokenizer virtual index also changes - record 1"""
        query = "SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=%s" % (self._id, 1)
        self.assertEqual('Higgs' in deserialize_via_marshal(run_sql(query)[0][0]), True)

    def test_virtual_index_3_correct_content_record_3(self):
        """bibindex - after reindexing with different tokenizer virtual index also changes - record 3"""
        query = "SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=%s" % (self._id, 3)
        self.assertEqual(['Conference', 'Biology', 'Molecular', 'European'],
                         deserialize_via_marshal(run_sql(query)[0][0]))

    def test_virtual_index_4_cleaned_up(self):
        """bibindex - after reindexing with normal title tokenizer everything is back to normal"""
        #this is version of test for installation with PyStemmer package
        #without this package word 'biology' is stemmed differently
        query = "SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=%s" % (self._id, 3)
        self.assertEqual(['biolog', 'molecular', 'confer', 'european'],
                         deserialize_via_marshal(run_sql(query)[0][0]))


class BibIndexVirtualIndexRemovalTest(InvenioTestCase):

    counter = 0
    indexes = ["authorcount", "journal", "year"]
    _id = 40

    @classmethod
    def setUp(self):
        self.counter += 1
        if self.counter == 1:
            create_virtual_index(self._id, self.indexes)
            wtabs = get_word_tables(self.indexes)
            for index_id, index_name, index_tags in wtabs:
                wordTable = WordTable(index_name=index_name,
                                      index_id=index_id,
                                      fields_to_index=index_tags,
                                      table_name_pattern='idxWORD%02dF',
                                      wordtable_type=CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"],
                                      tag_to_tokenizer_map={'8564_u': "BibIndexFulltextTokenizer"},
                                      wash_index_terms=50)
                wordTable.add_recIDs([[1, 113]], 1000)
            #removal part
            w = WordTable("testindex", self._id, [], "idxWORD%02dF", CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"], {}, 50)
            w.remove_dependent_index(int(get_index_id_from_index_name("authorcount")))


    @classmethod
    def tearDown(self):
        if self.counter == 9:
            remove_virtual_index(self._id)


    def test_authorcount_removal_number_of_items(self):
        """bibindex - checks virtual index after authorcount index removal - number of items"""
        query = """SELECT count(*) FROM idxWORD%02dF"""
        res = run_sql(query % self._id)
        self.assertEqual(157, res[0][0])

    def test_authorcount_removal_common_terms_intact(self):
        """bibindex - checks virtual index after authorcount index removal - common terms"""
        query = """SELECT term FROM idxWORD%02dF WHERE term IN ('10', '2', '4', '7')"""
        res = run_sql(query % self._id)
        self.assertEqual(4, len(res))

    def test_authorcount_removal_no_315_term(self):
        """bibindex - checks virtual index after authorcount index removal - no '315' term in virtual index"""
        query = """SELECT term FROM idxWORD%02dF WHERE term='315'"""
        res = run_sql(query % self._id)
        self.assertEqual(0, len(res))

    def test_authorcount_removal_term_10_hitlist(self):
        """bibindex - checks virtual index after authorcount index removal - hitlist for '10' term"""
        query = """SELECT hitlist FROM idxWORD%02dF WHERE term='10'"""
        res = run_sql(query % self._id)
        self.assertEqual([80, 92], intbitset(res[0][0]).tolist())

    def test_authorcount_removal_term_1985_hitlist(self):
        """bibindex - checks virtual index after authorcount index removal - hitlist for '1985' term"""
        query = """SELECT hitlist FROM idxWORD%02dF WHERE term='1985'"""
        res = run_sql(query % self._id)
        self.assertEqual([16, 18], intbitset(res[0][0]).tolist())

    def test_authorcount_removal_record_16_hitlist(self):
        """bibindex - checks virtual index after authorcount index removal - termlist for record 16"""
        query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=16"""
        res = run_sql(query % self._id)
        self.assertEqual(['1985'], deserialize_via_marshal(res[0][0]))

    def test_authorcount_removal_record_10_hitlist(self):
        """bibindex - checks virtual index after authorcount index removal - termlist for record 10"""
        query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=10"""
        res = run_sql(query % self._id)
        self.assertEqual(['2002', 'Eur. Phys. J., C'], deserialize_via_marshal(res[0][0]))

    def test_year_removal_number_of_items(self):
        """bibindex - checks virtual index after year removal - number of items"""
        #must be run after: tearDown
        w = WordTable("testindex", self._id, [], "idxWORD%02dF", CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"], {}, 50)
        w.remove_dependent_index(int(get_index_id_from_index_name("year")))
        query = """SELECT count(*) FROM idxWORD%02dF"""
        res = run_sql(query % self._id)
        self.assertEqual(134, res[0][0])

    def test_year_removal_record_18_hitlist(self):
        """bibindex - checks virtual index after year removal - termlist for record 18"""
        #must be run after: tearDown, test_year_removal_number_of_items
        query = """SELECT termlist FROM idxWORD%02dR WHERE id_bibrec=18"""
        res = run_sql(query % self._id)
        self.assertEqual(['151', '357','1985', 'Phys. Lett., B 151 (1985) 357', 'Phys. Lett., B'],
                         deserialize_via_marshal(res[0][0]))

class BibIndexCLICallTest(InvenioTestCase):
    """Tests if calls to bibindex from CLI (bibsched deamon) are run correctly"""

    def test_correct_message_for_wrong_index_names(self):
        """bibindex - checks if correct message for wrong index appears"""
        index_name = "titlexrg"
        task_id = reindex_for_type_with_bibsched(index_name, force_all=True)
        filename = os.path.join(cfg['CFG_LOGDIR'], 'bibsched_task_' + str(task_id) + '.log')
        fl = open(filename)
        text = fl.read() # small file
        fl.close()
        self.assertTrue(text.find("Specified indexes can't be found.") >= 0)

    def test_correct_message_for_up_to_date_indexes(self):
        """bibindex - checks if correct message for index up to date appears"""
        index_name = "abstract"
        task_id = reindex_for_type_with_bibsched(index_name)
        filename = os.path.join(cfg['CFG_LOGDIR'], 'bibsched_task_' + str(task_id) + '.log')
        fl = open(filename)
        text = fl.read() # small file
        fl.close()
        self.assertTrue(text.find("Selected indexes/recIDs are up to date.") >= 0)



TEST_SUITE = make_test_suite(BibIndexRemoveStopwordsTest,
                             BibIndexRemoveLatexTest,
                             BibIndexRemoveHtmlTest,
                             BibIndexYearIndexTest,
                             BibIndexAuthorCountIndexTest,
                             BibIndexItemCountIndexTest,
                             BibIndexFiletypeIndexTest,
                             BibIndexJournalIndexTest,
                             BibIndexCJKTokenizerTitleIndexTest,
                             BibIndexAuthorityRecordTest,
                             BibIndexFindingAffectedIndexes,
                             BibIndexIndexingAffectedIndexes,
                             BibIndexFindingIndexesForTags,
                             BibIndexFindingTagsForIndexes,
                             BibIndexGlobalIndexContentTest,
                             BibIndexVirtualIndexAlsoChangesTest,
                             BibIndexVirtualIndexRemovalTest,
                             BibIndexCLICallTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
