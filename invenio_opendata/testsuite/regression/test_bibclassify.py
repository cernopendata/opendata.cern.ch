# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2007, 2008, 2009, 2010, 2011, 2012 CERN.
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


"""BibClassify Regression Test Suite. This modules IS NOT standalone safe"""

import sys
import os
from warnings import warn

from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.testsuite import make_test_suite, run_test_suite, \
    test_web_page_content

from invenio.modules.classifier.testsuite.test_classifier import BibClassifyTestCase

bconfig = lazy_import('invenio.legacy.bibclassify.config')
bibclassify_cli = lazy_import('invenio.legacy.bibclassify.cli')
bibclassify_engine = lazy_import('invenio.legacy.bibclassify.engine')
bibclassify_ontology_reader = lazy_import('invenio.legacy.bibclassify.ontology_reader')


class BibClassifyRegressionTest(BibClassifyTestCase):
    """Check BibClassify web pages whether they are up or not."""

    def test_availability_bibclassify_admin_guide(self):
        """bibclassify - availability of BibClassify Admin Guide page"""
        self.assertEqual([], test_web_page_content(cfg['CFG_SITE_URL'] +
            '/help/admin/bibclassify-admin-guide',
            expected_text="BibClassify Admin Guide"))
        return

    def test_availability_bibclassify_hacking_pages(self):
        """bibclassify - availability of BibClassify Hacking Guide pages"""
        self.assertEqual([], test_web_page_content(cfg['CFG_SITE_URL'] +
            '/help/hacking/bibclassify-internals',
            expected_text="BibClassify Internals"))
        self.assertEqual([], test_web_page_content(cfg['CFG_SITE_URL'] +
            '/help/hacking/bibclassify-hep-taxonomy',
            expected_text="The HEP taxonomy: rationale and extensions"))
        self.assertEqual([], test_web_page_content(cfg['CFG_SITE_URL'] +
            '/help/hacking/bibclassify-extraction-algorithm',
            expected_text="The code behind BibClassify: the extraction algorithm"))
        return

    def test_cli_extract_from_url(self):
        """bibclassify -k ${taxonomy}.rdf {url/record/94}"""

        path, url = self.get_test_file(94)

        args = ("-k %s.rdf %s" % (self.taxonomy_name, url)).split()
        options = bibclassify_cli._read_options(args)

        self.redirect()

        bibclassify_engine.output_keywords_for_sources(options["text_files"],
            options["taxonomy"],
            rebuild_cache=options["rebuild_cache"],
            no_cache=options["no_cache"],
            output_mode=options["output_mode"],
            output_limit=options["output_limit"],
            spires=options["spires"],
            match_mode=options["match_mode"],
            with_author_keywords=options["with_author_keywords"],
            extract_acronyms=options["extract_acronyms"],
            only_core_tags=options["only_core_tags"])


        results, errors = self.unredirect()

        res, msg = check_pdf2(results)
        if not res:
            self.fail(msg)


    def test_extract_using_recid(self):
        """bibclassify  - extracting data from database (using recID to find fulltext)"""

        if not bconfig.STANDALONE:
            from invenio.legacy import dbquery
            from invenio.legacy.bibclassify import daemon as bibclassify_daemon
            bibtask = bibclassify_daemon.bibtask
            #first test if the record exists in the database
            record = dbquery.run_sql("SELECT * FROM bibrec WHERE id=94")

            if len(record):

                bibtask.task_set_task_param('verbose', 0)
                bibtask.task_set_task_param('task_id', 1)

                results = bibclassify_daemon._analyze_documents([94], self.taxonomy_name, "XXX", output_limit=100)

                res, msg = check_pdf3(results)
                if not res:
                    self.fail(msg)



    def test_cli_extract_from_filepath(self):
        """bibclassify -k ${taxonomy}.rdf {cache}/article.pdf"""


        path, url = self.get_test_file(94)

        if not os.path.exists(path):
            sys.stderr.write("No PDF for testing found, please load demo records\n")
            return

        args = ("-k %s.rdf %s" % (self.taxonomy_name, path)).split()
        options = bibclassify_cli._read_options(args)

        self.redirect()

        bibclassify_engine.output_keywords_for_sources(options["text_files"],
            options["taxonomy"],
            rebuild_cache=options["rebuild_cache"],
            no_cache=options["no_cache"],
            output_mode=options["output_mode"],
            output_limit=options["output_limit"],
            spires=options["spires"],
            match_mode=options["match_mode"],
            with_author_keywords=options["with_author_keywords"],
            extract_acronyms=options["extract_acronyms"],
            only_core_tags=options["only_core_tags"])


        results, errors = self.unredirect()


        res, msg = check_pdf2(results)
        if not res:
            self.fail(msg)



    def test_cli_extract_from_directory(self):
        """bibclassify -k ${taxonomy}.rdf directory/"""


        path, url = self.get_test_file(94)

        path = os.path.dirname(path)

        if not os.path.exists(path):
            sys.stderr.write("No PDF folder for testing found, returning\n")
            return


        args = ("-k %s.rdf %s" % (self.taxonomy_name, path)).split()
        options = bibclassify_cli._read_options(args)

        self.redirect()

        bibclassify_engine.output_keywords_for_sources(options["text_files"],
            options["taxonomy"],
            rebuild_cache=options["rebuild_cache"],
            no_cache=options["no_cache"],
            output_mode=options["output_mode"],
            output_limit=options["output_limit"],
            spires=options["spires"],
            match_mode=options["match_mode"],
            with_author_keywords=options["with_author_keywords"],
            extract_acronyms=options["extract_acronyms"],
            only_core_tags=options["only_core_tags"])

        results, errors = self.unredirect()


        res, msg = check_pdf2(results)
        if not res:
            self.fail(msg)



    def test_full_and_partial_matching_mode(self):
        """bibclassify - difference of extraction on part or full contents of pdf"""

        path, url = self.get_test_file(94)

        if not os.path.exists(path):
            sys.stderr.write("No PDF for testing found, returning\n")
            return

        results = []
        for case in ["-k %s.rdf %s" % (self.taxonomy_name, path), "-k %s.rdf %s -m partial" % (self.taxonomy_name, path)]:
            args = (case).split()
            options = bibclassify_cli._read_options(args)

            self.redirect()

            bibclassify_engine.output_keywords_for_sources(options["text_files"],
                options["taxonomy"],
                rebuild_cache=options["rebuild_cache"],
                no_cache=options["no_cache"],
                output_mode=options["output_mode"],
                output_limit=options["output_limit"],
                spires=options["spires"],
                match_mode=options["match_mode"],
                with_author_keywords=options["with_author_keywords"],
                extract_acronyms=options["extract_acronyms"],
                only_core_tags=options["only_core_tags"])

            r, e = self.unredirect()
            results.append(r)



        res, msg = check_pdf1(results[1])
        if not res:
            self.fail(msg)
        res, msg = check_pdf2(results[0])
        if not res:
            self.fail(msg)


def check_pdf0(result):
    """
    Results for: http://arxiv.org/PS_cache/arxiv/pdf/0808/0808.1825v1.pdf
                 http://arxiv.org/pdf/0808.1825

    These results will depend on the taxonomy, but let's have them, as they can
    serve as early-warning.

    """

    output = """
Composite keywords:
9  top: mass [10, 22]
3  W: mass [11, 22]
2  Higgs particle: mass [3, 22]
2  electroweak interaction: radiative correction [5, 3]
1  mass: transverse [22, 1]
1  W: transverse [11, 1]
1  particle: massive [4, 1]
1  correction: quantum [1, 2]
1  boson: vector [2, 1]
1  p: beam [2, 1]

Single keywords:
11  CERN LHC Coll
9  Batavia TEVATRON Coll
9  CERN LEP Stor
7  ATLAS
7  SLD
4  SLAC SLC Linac
2  statistics
2  background
2  lepton
1  leptonic decay
1  supersymmetry
1  higher-order
1  accelerator
1  Monte Carlo
1  CERN Lab
1  hadron
1  W W
1  CDF

Core keywords:
11  CERN LHC Coll
9  Batavia TEVATRON Coll
9  CERN LEP Stor
7  ATLAS
7  SLD
4  SLAC SLC Linac
1  supersymmetry
1  CERN Lab
1  CDF """
    return check_pdf(result, output)

def check_pdf1(result):
    """ test for:
    /opt/cds-invenio/var/data/files/g0/90/9611103.pdf -m partial
    """

    output = """
Composite keywords:
3  gaugefieldtheory: Yang-Mills: supersymmetry [4, 9]
2  dimension: 10 [5, 6]
2  symmetry: gauge [5, 2]
2  field equations: Yang-Mills [1, 2]
1  quantum mechanics: model [3, 9]
1  invariance: Lorentz [2, 1]

Single keywords:
8  matrix model
3  light cone
3  M-theory
3  algebra
1  dimensional reduction
1  commutation relations
1  invariance gauge
1  field strength
1  expansion 1/N
1  F-theory

Core keywords:
3  M-theory
-  supersymmetry (9)
-  Yang-Mills (2)
"""

    output_bad_pdftotext = """
Composite keywords:
3  gaugefieldtheory: Yang-Mills: supersymmetry [4, 8]
2  supersymmetry: transformation [8, 4]
2  dimension: 10 [6, 6]
2  symmetry: gauge [3, 4]
2  field equations: Yang-Mills [2, 2]
1  quantum mechanics: model [2, 4]
1  invariance: Lorentz [2, 1]

Single keywords:
3  matrix model
2  dimensional reduction
2  commutation relations
2  light cone
2  M-theory
2  algebra
1  invariance gauge
1  field strength
1  expansion 1/N
1  translation
1  F-theory

Core keywords:
2  M-theory
-  supersymmetry (8)
-  Yang-Mills (2)
"""

    return check_pdf(result, output, output_bad_pdftotext)

def check_pdf2(result):
    """ test for:
    /opt/cds-invenio/var/data/files/g0/90/9611103.pdf -m full
    """

    output = """
Composite keywords:
6  invariance: Lorentz [10, 7]
5  symmetry: gauge [10, 11]
3  gaugefieldtheory: Yang-Mills: supersymmetry [5, 19]
3  field equations: Yang-Mills [4, 4]
2  supersymmetry: transformation [19, 6]
2  dimension: 10 [10, 14]
1  quantum mechanics: model [5, 16]

Single keywords:
10  matrix model
8  light cone
6  translation
6  algebra
5  dimensional reduction
3  M-theory
2  commutation relations
2  invariance gauge
2  expansion 1/N
1  field strength
1  F-theory

Core keywords:
3  M-theory
-  Yang-Mills (4)
-  supersymmetry (19)
"""

    output_bad_pdftotext = """
Composite keywords:
5  symmetry: gauge [8, 10]
5  invariance: Lorentz [9, 6]
3  gaugefieldtheory: Yang-Mills: supersymmetry [4, 14]
3  field equations: Yang-Mills [5, 4]
2  dimension: 10 [9, 13]
2  supersymmetry: transformation [14, 6]
1  quantum mechanics: model [3, 8]

Single keywords:
6  translation
5  matrix model
5  algebra
4  dimensional reduction
3  light cone
2  commutation relations
2  invariance gauge
2  M-theory
1  field strength
1  expansion 1/N
1  F-theory

Core keywords:
2  M-theory
-  Yang-Mills (4)
-  supersymmetry (14)
"""

    return check_pdf(result, output, output_bad_pdftotext)

def check_pdf3(result):
    """ test for:
    /opt/cds-invenio/var/data/files/g0/90/9611103.pdf -m full -o marcxml
    """

    output = """
<record>
<controlfield tag="001">94</controlfield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">matrix model</subfield>
    <subfield code="n">8</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">quantum mechanics: model</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">M-theory</subfield>
    <subfield code="n">3</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">dimensional reduction</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">algebra</subfield>
    <subfield code="n">3</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">gaugefieldtheory: Yang-Mills: supersymmetry</subfield>
    <subfield code="n">3</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">expansion 1/N</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">light cone</subfield>
    <subfield code="n">3</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">invariance gauge</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">dimension: 10</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">symmetry: gauge</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">F-theory</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">field strength</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">invariance: Lorentz</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">commutation relations</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">field equations: Yang-Mills</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>

</record>
"""

    output_bad_pdftotext = """
<record>
<controlfield tag="001">94</controlfield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">matrix model</subfield>
    <subfield code="n">3</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">quantum mechanics: model</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">M-theory</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">dimensional reduction</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">algebra</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">gaugefieldtheory: Yang-Mills: supersymmetry</subfield>
    <subfield code="n">3</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">supersymmetry: transformation</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">expansion 1/N</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">light cone</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">invariance gauge</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">dimension: 10</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">symmetry: gauge</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">F-theory</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">translation</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">field equations: Yang-Mills</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">invariance: Lorentz</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">commutation relations</subfield>
    <subfield code="n">2</subfield>
    <subfield code="9">HEP</subfield>
</datafield>
<datafield tag="653" ind1="1" ind2="">
    <subfield code="2">BibClassify</subfield>
    <subfield code="a">field strength</subfield>
    <subfield code="n">1</subfield>
    <subfield code="9">HEP</subfield>
</datafield>

</record>
"""

    return check_pdf(result, output, output_bad_pdftotext)


def check_pdf(result, output, output_bad_pdftotext=""):
    msg = ""
    for line in output.splitlines():
        line = line.strip()
        if line:
            if line not in result:
                msg = "\nGot: %s\nMissing: \"%s\"" % (result, line)
                break
    if msg and output_bad_pdftotext:
        warn("Standard test failed; let's try a test amended for older pdftotext versions now. If this succeeds, please consider upgrading to the latest version of pdftotext.")
        msg = ""
        for line in output_bad_pdftotext.splitlines():
            line = line.strip()
            if line:
                if line not in result:
                    msg = "\nGot: %s\nMissing: \"%s\"" % (result, line)
                    break
    if msg:
        return (False, msg)
    else:
        return (True, True)



if 'custom' in sys.argv:
    from unittest import suite
    TEST_SUITE = suite(BibClassifyRegressionTest)
else:
    TEST_SUITE = make_test_suite(BibClassifyRegressionTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
