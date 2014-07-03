## This file is part of Invenio.
## Copyright (C) 2010, 2011, 2013 CERN.
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

from invenio.testsuite import InvenioTestCase
from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.testsuite import make_test_suite, \
                              run_test_suite, \
                              test_web_page_content, \
                              nottest
import intbitset

solr_get_ranked = lazy_import('invenio.legacy.miscutil.solrutils_bibrank_searcher:solr_get_ranked')
solr_get_similar_ranked = lazy_import('invenio.legacy.miscutil.solrutils_bibrank_searcher:solr_get_similar_ranked')
solr_get_bitset = lazy_import('invenio.legacy.miscutil.solrutils_bibindex_searcher:solr_get_bitset')
get_collection_reclist = lazy_import('invenio.legacy.search_engine:get_collection_reclist')
get_external_word_similarity_ranker = lazy_import('invenio.legacy.bibrank.bridge_utils:get_external_word_similarity_ranker')
get_logical_fields = lazy_import('invenio.legacy.bibrank.bridge_utils:get_logical_fields')
get_tags = lazy_import('invenio.legacy.bibrank.bridge_utils:get_tags')
get_field_content_in_utf8 = lazy_import('invenio.legacy.bibrank.bridge_utils:get_field_content_in_utf8')


ROWS = 100


HITSETS = {
    'Willnotfind': intbitset.intbitset([]),
    'higgs': intbitset.intbitset([47, 48, 51, 52, 55, 56, 58, 68, 79, 85, 89, 96]),
    'of': intbitset.intbitset([8, 10, 11, 12, 15, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                               52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 68, 74,
                               77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
                               91, 92, 93, 94, 95, 96, 97]),
    '"higgs boson"': intbitset.intbitset([55, 56]),
}

def get_topN(n, data):
    res = dict()
    for key, value in data.iteritems():
        res[key] = value[-n:]
    return res


class TestSolrSearch(InvenioTestCase):
    """Test for Solr search. Requires:
    make install-solrutils
    cfg['CFG_SOLR_URL'] set
    fulltext index in idxINDEX containing 'SOLR' in indexer column
    AND EITHER
      Solr index built: ./bibindex -w fulltext for all records
     OR
      WRD method referring to Solr: <invenio installation>/etc/bibrank$ cp template_word_similarity_solr.cfg wrd.cfg
      and ./bibrank -w wrd for all records
    """

    def _get_result(self, query, index='fulltext'):
        return solr_get_bitset(index, query)

    @nottest
    def test_get_bitset(self):
        """solrutils - search results"""
        self.assertEqual(HITSETS['Willnotfind'], self._get_result('Willnotfind'))
        self.assertEqual(HITSETS['higgs'], self._get_result('higgs'))
        self.assertEqual(HITSETS['of'], self._get_result('of'))
        self.assertEqual(HITSETS['"higgs boson"'], self._get_result('"higgs boson"'))


class TestSolrRanking(InvenioTestCase):
    """Test for Solr ranking. Requires:
    make install-solrutils
    cfg['CFG_SOLR_URL'] set
    fulltext index in idxINDEX containing 'SOLR' in indexer column
    AND EITHER
      Solr index built: ./bibindex -w fulltext for all records
     OR
      WRD method referring to Solr: <invenio installation>/etc/bibrank$ cp template_word_similarity_solr.cfg wrd.cfg
      and ./bibrank -w wrd for all records
    """

    def _get_ranked_result_sequence(self, query, index='fulltext', rows=ROWS, hitset=None):
        if hitset is None:
            hitset=HITSETS[query]
        ranked_result = solr_get_ranked('%s:%s' % (index, query), hitset, self._get_ranking_params(), rows)
        return tuple([pair[0] for pair in ranked_result[0]])

    def _get_ranked_topN(self, n):
        return get_topN(n, self._RANKED)

    _RANKED = {
        'Willnotfind': tuple(),
        'higgs': (79, 51, 55, 47, 56, 96, 58, 68, 52, 48, 89, 85),
        'of': (50, 61, 60, 54, 56, 53, 10, 68, 44, 57, 83, 95, 92, 91, 74, 45, 48, 62, 82,
               49, 51, 89, 90, 96, 43, 8, 64, 97, 15, 85, 78, 46, 55, 79, 84, 88, 81, 52,
               58, 86, 11, 80, 93, 77, 12, 59, 87, 47, 94),
        '"higgs boson"': (55, 56),
    }

    def _get_ranking_params(self, cutoff_amount=10000, cutoff_time=2000):
        """
        Default values from template_word_similarity_solr.cfg
        """
        return {
            'cutoff_amount': cutoff_amount,
            'cutoff_time_ms': cutoff_time
        }

    @nottest
    def test_get_ranked(self):
        """solrutils - ranking results"""
        all_ranked = 0
        ranked_top = self._get_ranked_topN(all_ranked)
        self.assertEqual(ranked_top['Willnotfind'], self._get_ranked_result_sequence(query='Willnotfind'))
        self.assertEqual(ranked_top['higgs'], self._get_ranked_result_sequence(query='higgs'))
        self.assertEqual(ranked_top['of'], self._get_ranked_result_sequence(query='of'))
        self.assertEqual(ranked_top['"higgs boson"'], self._get_ranked_result_sequence(query='"higgs boson"'))

    @nottest
    def test_get_ranked_top(self):
        """solrutils - ranking top results"""
        top_n = 0
        self.assertEqual(tuple(), self._get_ranked_result_sequence(query='Willnotfind', rows=top_n))
        self.assertEqual(tuple(), self._get_ranked_result_sequence(query='higgs', rows=top_n))
        self.assertEqual(tuple(), self._get_ranked_result_sequence(query='of', rows=top_n))
        self.assertEqual(tuple(), self._get_ranked_result_sequence(query='"higgs boson"', rows=top_n))

        top_n = 2
        ranked_top = self._get_ranked_topN(top_n)
        self.assertEqual(ranked_top['Willnotfind'], self._get_ranked_result_sequence(query='Willnotfind', rows=top_n))
        self.assertEqual(ranked_top['higgs'], self._get_ranked_result_sequence(query='higgs', rows=top_n))
        self.assertEqual(ranked_top['of'], self._get_ranked_result_sequence(query='of', rows=top_n))
        self.assertEqual(ranked_top['"higgs boson"'], self._get_ranked_result_sequence(query='"higgs boson"', rows=top_n))

        top_n = 10
        ranked_top = self._get_ranked_topN(top_n)
        self.assertEqual(ranked_top['Willnotfind'], self._get_ranked_result_sequence(query='Willnotfind', rows=top_n))
        self.assertEqual(ranked_top['higgs'], self._get_ranked_result_sequence(query='higgs', rows=top_n))
        self.assertEqual(ranked_top['of'], self._get_ranked_result_sequence(query='of', rows=top_n))
        self.assertEqual(ranked_top['"higgs boson"'], self._get_ranked_result_sequence(query='"higgs boson"', rows=top_n))

    @nottest
    def test_get_ranked_smaller_hitset(self):
        """solrutils - ranking smaller hitset"""
        hitset = intbitset.intbitset([47, 56, 58, 68, 85, 89])
        self.assertEqual((47, 56, 58, 68, 89, 85), self._get_ranked_result_sequence(query='higgs', hitset=hitset))

        hitset = intbitset.intbitset([45, 50, 61, 74, 94])
        self.assertEqual((50, 61, 74, 45, 94), self._get_ranked_result_sequence(query='of', hitset=hitset))
        self.assertEqual((74, 45, 94), self._get_ranked_result_sequence(query='of', hitset=hitset, rows=3))

    @nottest
    def test_get_ranked_larger_hitset(self):
        """solrutils - ranking larger hitset"""
        hitset = intbitset.intbitset([47, 56, 58, 68, 85, 89])
        self.assertEqual(tuple(), self._get_ranked_result_sequence(query='Willnotfind', hitset=hitset))

        hitset = intbitset.intbitset([47, 56, 55, 56, 58, 68, 85, 89])
        self.assertEqual((55, 56), self._get_ranked_result_sequence(query='"higgs boson"', hitset=hitset))


class TestSolrSimilarToRecid(InvenioTestCase):
    """Test for Solr similar ranking. Requires:
    make install-solrutils
    cfg['CFG_SOLR_URL'] set
    fulltext index in idxINDEX containing 'SOLR' in indexer column
    WRD method referring to Solr: <invenio installation>/etc/bibrank$ cp template_word_similarity_solr.cfg wrd.cfg
    ./bibrank -w wrd for all records
    """

    def _get_similar_result_sequence(self, recid, rows=ROWS):
        similar_result = solr_get_similar_ranked(recid, self._all_records, self._get_similar_ranking_params(), rows)
        return tuple([pair[0] for pair in similar_result[0]])[-rows:]

    def _get_similar_topN(self, n):
        return get_topN(n, self._SIMILAR)

    _SIMILAR = {
        30: (12, 95, 85, 82, 44, 1, 89, 64, 58, 15, 96, 61, 50, 86, 78, 77, 65, 62, 60,
             47, 46, 100, 99, 102, 91, 80, 7, 5, 92, 88, 74, 57, 55, 108, 84, 81, 79, 54,
             101, 11, 103, 94, 48, 83, 72, 63, 2, 68, 51, 53, 97, 93, 70, 45, 52, 14,
             59, 6, 10, 32, 33, 29, 30),
        59: (17, 69, 3, 20, 109, 14, 22, 33, 28, 24, 60, 6, 73, 113, 5, 107, 78, 4, 13,
             8, 45, 72, 74, 46, 104, 63, 71, 44, 87, 70, 103, 92, 57, 49, 7, 88, 68, 77,
             62, 10, 93, 2, 65, 55, 43, 94, 96, 1, 11, 99, 91, 61, 51, 15, 64, 97, 89, 101,
             108, 80, 86, 90, 54, 95, 102, 47, 100, 79, 83, 48, 12, 81, 82, 58, 50, 56, 84,
             85, 53, 52, 59)
    }

    def _get_similar_ranking_params(self, cutoff_amount=10000, cutoff_time=2000):
        """
        Default values from template_word_similarity_solr.cfg
        """
        return {
            'cutoff_amount': cutoff_amount,
            'cutoff_time_ms': cutoff_time,
            'find_similar_to_recid': {
                'more_results_factor': 5,
                'mlt_fl': 'mlt',
                'mlt_mintf': 0,
                'mlt_mindf': 0,
                'mlt_minwl': 0,
                'mlt_maxwl': 0,
                'mlt_maxqt': 25,
                'mlt_maxntp': 1000,
                'mlt_boost': 'false'
                }
            }
      #FIXME
    _all_records = get_collection_reclist(cfg['CFG_SITE_NAME'])

    @nottest
    def test_get_similar_ranked(self):
        """solrutils - similar results"""
        all_ranked = 0
        similar_top = self._get_similar_topN(all_ranked)
        recid = 30
        self.assertEqual(similar_top[recid], self._get_similar_result_sequence(recid=recid))
        recid = 59
        self.assertEqual(similar_top[recid], self._get_similar_result_sequence(recid=recid))

    @nottest
    def test_get_similar_ranked_top(self):
        """solrutils - similar top results"""
        top_n = 5
        similar_top = self._get_similar_topN(top_n)
        recid = 30
        self.assertEqual(similar_top[recid], self._get_similar_result_sequence(recid=recid, rows=top_n))
        recid = 59
        self.assertEqual(similar_top[recid], self._get_similar_result_sequence(recid=recid, rows=top_n))


class TestSolrWebSearch(InvenioTestCase):
    """Test for webbased Solr search. Requires:
    make install-solrutils
    cfg['CFG_SOLR_URL'] set
    fulltext index in idxINDEX containing 'SOLR' in indexer column
    AND EITHER
      Solr index built: ./bibindex -w fulltext for all records
     OR
      WRD method referring to Solr: <invenio installation>/etc/bibrank$ cp template_word_similarity_solr.cfg wrd.cfg
      and ./bibrank -w wrd for all records
    """

    @nottest
    def test_get_result(self):
        """solrutils - web search results"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=fulltext%3AWillnotfind&rg=100',
                                               expected_text="[]"))

        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=fulltext%3Ahiggs&rg=100',
                                               expected_text="[12, 47, 48, 51, 52, 55, 56, 58, 68, 79, 80, 81, 85, 89, 96]"))

        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=fulltext%3Aof&rg=100',
                                               expected_text="[8, 10, 11, 12, 15, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 68, 74, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]"))

        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=fulltext%3A%22higgs+boson%22&rg=100',
                                               expected_text="[12, 47, 51, 55, 56, 68, 81, 85]"))


class TestSolrWebRanking(InvenioTestCase):
    """Test for webbased Solr ranking. Requires:
    make install-solrutils
    cfg['CFG_SOLR_URL'] set
    fulltext index in idxINDEX containing 'SOLR' in indexer column
    AND EITHER
      Solr index built: ./bibindex -w fulltext for all records
     OR
      WRD method referring to Solr: <invenio installation>/etc/bibrank$ cp template_word_similarity_solr.cfg wrd.cfg
      and ./bibrank -w wrd for all records
    """

    @nottest
    def test_get_ranked(self):
        """solrutils - web ranking results"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=fulltext%3AWillnotfind&rg=100&rm=wrd',
                                               expected_text="[]"))

        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=fulltext%3Ahiggs&rm=wrd',
                                               expected_text="[12, 51, 79, 80, 81, 55, 47, 56, 96, 58, 68, 52, 48, 89, 85]"))

        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=fulltext%3Ahiggs&rg=100&rm=wrd',
                                               expected_text="[12, 80, 81, 79, 51, 55, 47, 56, 96, 58, 68, 52, 48, 89, 85]"))

        # Record 77 is restricted
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=fulltext%3Aof&rm=wrd',
                                               expected_text="[8, 10, 15, 43, 44, 45, 46, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 64, 68, 74, 78, 79, 81, 82, 83, 84, 85, 88, 89, 90, 91, 92, 95, 96, 97, 86, 11, 80, 93, 77, 12, 59, 87, 47, 94]",
                                               username='admin'))

        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=fulltext%3Aof&rg=100&rm=wrd',
                                               expected_text="[61, 60, 54, 56, 53, 10, 68, 44, 57, 83, 95, 92, 91, 74, 45, 48, 62, 82, 49, 51, 89, 90, 96, 43, 8, 64, 97, 15, 85, 78, 46, 55, 79, 84, 88, 81, 52, 58, 86, 11, 80, 93, 77, 12, 59, 87, 47, 94]",
                                               username='admin'))

        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=fulltext%3A%22higgs+boson%22&rg=100&rm=wrd',
                                               expected_text="[12, 47, 51, 68, 81, 85, 55, 56]"))


class TestSolrWebSimilarToRecid(InvenioTestCase):
    """Test for webbased Solr similar ranking. Requires:
    make install-solrutils
    cfg['CFG_SOLR_URL'] set
    fulltext index in idxINDEX containing 'SOLR' in indexer column
    WRD method referring to Solr: <invenio installation>/etc/bibrank$ cp template_word_similarity_solr.cfg wrd.cfg
    ./bibrank -w wrd for all records
    """

    @nottest
    def test_get_similar_ranked(self):
        """solrutils - web similar results"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=recid%3A30&rm=wrd',
                                               expected_text="[1, 3, 4, 8, 9, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 34, 43, 44, 49, 50, 56, 58, 61, 64, 66, 67, 69, 71, 73, 75, 76, 77, 78, 82, 85, 86, 87, 89, 90, 95, 96, 98, 104, 107, 109, 113, 65, 62, 60, 47, 46, 100, 99, 102, 91, 80, 7, 5, 92, 88, 74, 57, 55, 108, 84, 81, 79, 54, 101, 11, 103, 94, 48, 83, 72, 63, 2, 68, 51, 53, 97, 93, 70, 45, 52, 14, 59, 6, 10, 32, 33, 29, 30]"))

        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/search?of=id&p=recid%3A30&rg=100&rm=wrd',
                                               expected_text="[3, 4, 8, 9, 13, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 34, 43, 49, 56, 66, 67, 69, 71, 73, 75, 76, 87, 90, 98, 104, 107, 109, 113, 12, 95, 85, 82, 44, 1, 89, 64, 58, 15, 96, 61, 50, 86, 78, 77, 65, 62, 60, 47, 46, 100, 99, 102, 91, 80, 7, 5, 92, 88, 74, 57, 55, 108, 84, 81, 79, 54, 101, 11, 103, 94, 48, 83, 72, 63, 2, 68, 51, 53, 97, 93, 70, 45, 52, 14, 59, 6, 10, 32, 33, 29, 30]"))


class TestSolrLoadLogicalFieldSettings(InvenioTestCase):
    """Test for loading Solr logical field settings. Requires:
    make install-solrutils
    cfg['CFG_SOLR_URL'] set
    WRD method referring to Solr: <invenio installation>/etc/bibrank$ cp template_word_similarity_solr.cfg wrd.cfg
    """

    @nottest
    def test_load_logical_fields(self):
        """solrutils - load logical fields"""
        self.assertEqual({'abstract': ['abstract'], 'author': ['author'], 'title': ['title'], 'keyword': ['keyword']},
                         get_logical_fields())

    @nottest
    def test_load_tags(self):
        """solrutils - load tags"""
        self.assertEqual({'abstract': ['520__%'], 'author': ['100__a', '700__a'], 'title': ['245__%', '246__%'], 'keyword': ['6531_a']},
                         get_tags())


class TestSolrBuildFieldContent(InvenioTestCase):
    """Test for building Solr field content. Requires:
    make install-solrutils
    cfg['CFG_SOLR_URL'] set
    WRD method referring to Solr: <invenio installation>/etc/bibrank$ cp template_word_similarity_solr.cfg wrd.cfg
    """

    @nottest
    def test_build_default_field_content(self):
        """solrutils - build default field content"""
        tags = get_tags()

        self.assertEqual(u'Ellis, J Enqvist, K Nanopoulos, D V',
                         get_field_content_in_utf8(18, 'author', tags))

        self.assertEqual(u'Kahler manifolds gravitinos axions constraints noscale',
                         get_field_content_in_utf8(18, 'keyword', tags))

        self.assertEqual(u'In 1962, CERN hosted the 11th International Conference on High Energy Physics. Among the distinguished visitors were eight Nobel prizewinners.Left to right: Cecil F. Powell, Isidor I. Rabi, Werner Heisenberg, Edwin M. McMillan, Emile Segre, Tsung Dao Lee, Chen Ning Yang and Robert Hofstadter.',
                         get_field_content_in_utf8(6, 'abstract', tags))

    @nottest
    def test_build_custom_field_content(self):
        """solrutils - build custom field content"""
        tags = {'abstract': ['520__%', '590__%']}

        self.assertEqual(u"""In 1962, CERN hosted the 11th International Conference on High Energy Physics. Among the distinguished visitors were eight Nobel prizewinners.Left to right: Cecil F. Powell, Isidor I. Rabi, Werner Heisenberg, Edwin M. McMillan, Emile Segre, Tsung Dao Lee, Chen Ning Yang and Robert Hofstadter. En 1962, le CERN est l'hote de la onzieme Conference Internationale de Physique des Hautes Energies. Parmi les visiteurs eminents se trouvaient huit laureats du prix Nobel.De gauche a droite: Cecil F. Powell, Isidor I. Rabi, Werner Heisenberg, Edwin M. McMillan, Emile Segre, Tsung Dao Lee, Chen Ning Yang et Robert Hofstadter.""",
                         get_field_content_in_utf8(6, 'abstract', tags))


TESTS = []


if cfg['CFG_SOLR_URL']:
    TESTS.extend((TestSolrSearch, TestSolrWebSearch))
    if get_external_word_similarity_ranker() == 'solr':
        TESTS.extend((TestSolrRanking,
                      TestSolrSimilarToRecid,
                      TestSolrWebRanking,
                      TestSolrWebSimilarToRecid,
                      TestSolrLoadLogicalFieldSettings,
                      TestSolrBuildFieldContent,
                      ))


TEST_SUITE = make_test_suite(*TESTS)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
