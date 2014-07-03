# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013 CERN.
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

# pylint: disable=C0301

"""Regression tests for the BibUpload."""

__revision__ = "$Id$"

import base64
import cPickle
import re

import os
import pprint
import sys
import time

from marshal import loads
from zlib import decompress

from urllib import urlencode
from urllib2 import urlopen

from invenio.base.globals import cfg
from invenio.utils.json import json
from invenio.testsuite import InvenioTestCase, make_test_suite, run_test_suite, test_web_page_content

from invenio.base.wrappers import lazy_import
from invenio.utils.hash import md5
from invenio.utils.shell import run_shell_command

BibRecDocs = lazy_import('invenio.legacy.bibdocfile.api:BibRecDocs')
BibRelation = lazy_import('invenio.legacy.bibdocfile.api:BibRelation')
MoreInfo = lazy_import('invenio.legacy.bibdocfile.api:MoreInfo')
bibupload = lazy_import('invenio.legacy.bibupload:engine')
print_record = lazy_import('invenio.legacy.search_engine:print_record')
get_record = lazy_import('invenio.legacy.search_engine:get_record')
create_record = lazy_import('invenio.legacy.bibrecord:create_record')
records_identical = lazy_import('invenio.legacy.bibrecord:records_identical')
encode_for_xml = lazy_import('invenio.utils.text:encode_for_xml')

run_sql = lazy_import('invenio.legacy.dbquery:run_sql')
get_table_status_info = lazy_import('invenio.legacy.dbquery:get_table_status_info')

# helper functions:

RE_005 = re.compile(re.escape('tag="005"'))


def get_record_from_bibxxx(recid):
    """Return a recstruct built from bibxxx tables"""
    record = "<record>"
    record += """        <controlfield tag="001">%s</controlfield>\n""" % recid
    # controlfields
    query = "SELECT b.tag,b.value,bb.field_number FROM bib00x AS b, bibrec_bib00x AS bb "\
            "WHERE bb.id_bibrec=%s AND b.id=bb.id_bibxxx AND b.tag LIKE '00%%' "\
            "ORDER BY bb.field_number, b.tag ASC"
    res = run_sql(query, (recid, ))
    for row in res:
        field, value = row[0], row[1]
        value = encode_for_xml(value)
        record += """        <controlfield tag="%s">%s</controlfield>\n""" % \
                (encode_for_xml(field[0:3]), value)
    # datafields
    i = 1 # Do not process bib00x and bibrec_bib00x, as
            # they are controlfields. So start at bib01x and
            # bibrec_bib00x (and set i = 0 at the end of
            # first loop)
    for digit1 in range(0, 10):
        for digit2 in range(i, 10):
            bx = "bib%d%dx" % (digit1, digit2)
            bibx = "bibrec_bib%d%dx" % (digit1, digit2)
            query = "SELECT b.tag,b.value,bb.field_number FROM %s AS b, %s AS bb "\
                    "WHERE bb.id_bibrec=%%s AND b.id=bb.id_bibxxx AND b.tag LIKE %%s"\
                    "ORDER BY bb.field_number, b.tag ASC" % (bx, bibx)
            res = run_sql(query, (recid, str(digit1)+str(digit2)+'%'))
            field_number_old = -999
            field_old = ""
            for row in res:
                field, value, field_number = row[0], row[1], row[2]
                ind1, ind2 = field[3], field[4]
                if ind1 == "_" or ind1 == "":
                    ind1 = " "
                if ind2 == "_" or ind2 == "":
                    ind2 = " "
                if field_number != field_number_old or field[:-1] != field_old[:-1]:
                    if field_number_old != -999:
                        record += """        </datafield>\n"""
                    record += """        <datafield tag="%s" ind1="%s" ind2="%s">\n""" % \
                                (encode_for_xml(field[0:3]), encode_for_xml(ind1), encode_for_xml(ind2))
                    field_number_old = field_number
                    field_old = field
                # print subfield value
                value = encode_for_xml(value)
                record += """            <subfield code="%s">%s</subfield>\n""" % \
                    (encode_for_xml(field[-1:]), value)

            # all fields/subfields printed in this run, so close the tag:
            if field_number_old != -999:
                record += """        </datafield>\n"""
        i = 0 # Next loop should start looking at bib%0 and bibrec_bib00x
    # we are at the end of printing the record:
    record += "    </record>\n"
    return record

def remove_tag_001_from_xmbuffer(xmbuffer):
    """Remove tag 001 from MARCXML buffer.  Useful for testing two
       MARCXML buffers without paying attention to recIDs attributed
       during the bibupload.
    """
    return re.sub(r'<controlfield tag="001">.*</controlfield>', '', xmbuffer)

def compare_xmbuffers(xmbuffer1, xmbuffer2):
    """Compare two XM (XML MARC) buffers by removing whitespaces and version
       numbers in tags 005 before testing.
    """

    def remove_blanks_from_xmbuffer(xmbuffer):
        """Remove \n and blanks from XMBUFFER."""
        out = xmbuffer.replace("\n", "")
        out = out.replace(" ", "")
        return out

    # remove 005 revision numbers:
    xmbuffer1 = re.sub(r'<controlfield tag="005">.*?</controlfield>', '', xmbuffer1)
    xmbuffer2 = re.sub(r'<controlfield tag="005">.*?</controlfield>', '', xmbuffer2)

    # remove whitespace:
    xmbuffer1 = remove_blanks_from_xmbuffer(xmbuffer1)
    xmbuffer2 = remove_blanks_from_xmbuffer(xmbuffer2)

    if len(RE_005.findall(xmbuffer1)) > 1:
        return "More than 1 005 tag has been found in the first XM: %s" % xmbuffer1
    if len(RE_005.findall(xmbuffer2)) > 1:
        return "More than 1 005 tag has been found in the second XM: %s" % xmbuffer2


    if xmbuffer1 != xmbuffer2:
        return "\n=" + xmbuffer1 + "=\n" + '!=' + "\n=" + xmbuffer2 + "=\n"

    return ''

def remove_tag_001_from_hmbuffer(hmbuffer):
    """Remove tag 001 from HTML MARC buffer.  Useful for testing two
       HTML MARC buffers without paying attention to recIDs attributed
       during the bibupload.
    """
    return re.sub(r'(^|\n)(<pre>)?[0-9]{9}\s001__\s\d+($|\n)', '', hmbuffer)

def compare_hmbuffers(hmbuffer1, hmbuffer2):
    """Compare two HM (HTML MARC) buffers by removing whitespaces
       before testing.
    """

    hmbuffer1 = hmbuffer1.strip()
    hmbuffer2 = hmbuffer2.strip()

    # remove eventual <pre>...</pre> formatting:
    hmbuffer1 = re.sub(r'^<pre>', '', hmbuffer1)
    hmbuffer2 = re.sub(r'^<pre>', '', hmbuffer2)
    hmbuffer1 = re.sub(r'</pre>$', '', hmbuffer1)
    hmbuffer2 = re.sub(r'</pre>$', '', hmbuffer2)

    # remove 005 revision numbers:
    hmbuffer1 = re.sub(r'(^|\n)[0-9]{9}\s005.*($|\n)', '\n', hmbuffer1)
    hmbuffer2 = re.sub(r'(^|\n)[0-9]{9}\s005.*($|\n)', '\n', hmbuffer2)
    hmbuffer1 = hmbuffer1.strip()
    hmbuffer2 = hmbuffer2.strip()

    # remove leading recid, leaving only field values:
    hmbuffer1 = re.sub(r'(^|\n)[0-9]{9}\s', '', hmbuffer1)
    hmbuffer2 = re.sub(r'(^|\n)[0-9]{9}\s', '', hmbuffer2)

    # remove leading whitespace:
    hmbuffer1 = re.sub(r'(^|\n)\s+', '', hmbuffer1)
    hmbuffer2 = re.sub(r'(^|\n)\s+', '', hmbuffer2)

    compared_hmbuffers = hmbuffer1 == hmbuffer2

    if not compared_hmbuffers:
        return "\n=" + hmbuffer1 + "=\n" + '!=' + "\n=" + hmbuffer2 + "=\n"

    return ''

def wipe_out_record_from_all_tables(recid):
    """
    Wipe out completely the record and all its traces of RECID from
    the database (bibrec, bibrec_bibxxx, bibxxx, bibfmt).  Useful for
    the time being for test cases.
    """
    # delete all the linked bibdocs
    try:
        for bibdoc in BibRecDocs(recid).list_bibdocs():
            bibdoc.expunge()
        # delete from bibrec:
        run_sql("DELETE FROM bibrec WHERE id=%s", (recid,))
        # delete from bibrec_bibxxx:
        for i in range(0, 10):
            for j in range(0, 10):
                run_sql("DELETE FROM %(bibrec_bibxxx)s WHERE id_bibrec=%%s" %  # kwalitee: disable=sql
                        {'bibrec_bibxxx': "bibrec_bib%i%ix" % (i, j)},
                        (recid,))
        # delete all unused bibxxx values:
        for i in range(0, 10):
            for j in range(0, 10):
                run_sql("DELETE %(bibxxx)s FROM %(bibxxx)s " \
                        " LEFT JOIN %(bibrec_bibxxx)s " \
                        " ON %(bibxxx)s.id=%(bibrec_bibxxx)s.id_bibxxx " \
                        " WHERE %(bibrec_bibxxx)s.id_bibrec IS NULL" % \
                        {'bibxxx': "bib%i%ix" % (i, j),
                        'bibrec_bibxxx': "bibrec_bib%i%ix" % (i, j)})
        # delete from bibfmt:
        run_sql("DELETE FROM bibfmt WHERE id_bibrec=%s", (recid,))
        # delete from bibrec_bibdoc:
        run_sql("DELETE FROM bibrec_bibdoc WHERE id_bibrec=%s", (recid,))
        # delete from holdingpen
        run_sql("DELETE FROM bibHOLDINGPEN WHERE id_bibrec=%s", (recid,))
        # delete from hstRECORD
        run_sql("DELETE FROM hstRECORD WHERE id_bibrec=%s", (recid,))
    except Exception, err:
        print >> sys.stderr, "Exception captured while wiping records: %s" % err


def try_url_download(url):
    """Try to download a given URL"""
    try:
        open_url = urlopen(url)
        open_url.read()
    except Exception, e:
        raise StandardError("Downloading %s is impossible because of %s"
            % (url, str(e)))
    return True


def force_webcoll(recid):
    from invenio.legacy.bibindex.engine_config import CFG_BIBINDEX_INDEX_TABLE_TYPE
    from invenio.legacy.bibindex import engine as bibindex_engine
    reload(bibindex_engine)
    from invenio import websearch_webcoll
    reload(websearch_webcoll)
    index_id, index_name, index_tags = bibindex_engine.get_word_tables(["collection"])[0]
    bibindex_engine.WordTable(index_name, index_id, index_tags, "idxWORD%02dF", wordtable_type=CFG_BIBINDEX_INDEX_TABLE_TYPE["Words"], tag_to_tokenizer_map={'8564_u': "BibIndexFulltextTokenizer"}).add_recIDs([[recid, recid]], 1)
    #sleep 1s to make sure all tables are ready
    time.sleep(1)
    c = websearch_webcoll.Collection()
    c.calculate_reclist()
    c.update_reclist()


class GenericBibUploadTest(InvenioTestCase):
    """Generic BibUpload testing class with predefined
    setUp and tearDown methods.
    """
    def setUp(self):
        from invenio.legacy.bibsched.bibtask import task_set_task_param, setup_loggers
        self.verbose = 0
        setup_loggers()
        task_set_task_param('verbose', self.verbose)
        self.last_recid = run_sql("SELECT MAX(id) FROM bibrec")[0][0]

    def tearDown(self):
        for recid in run_sql("SELECT id FROM bibrec WHERE id>%s", (self.last_recid,)):
            wipe_out_record_from_all_tables(recid[0])

    def check_record_consistency(self, recid):
        rec_in_history = create_record(decompress(run_sql("SELECT marcxml FROM hstRECORD WHERE id_bibrec=%s ORDER BY job_date DESC LIMIT 1", (recid, ))[0][0]))[0]
        rec_in_xm = create_record(decompress(run_sql("SELECT value FROM bibfmt WHERE id_bibrec=%s AND format='xm'", (recid, ))[0][0]))[0]
        rec_in_bibxxx = create_record(get_record_from_bibxxx(recid))[0]
        self.failUnless(records_identical(rec_in_xm, rec_in_history, skip_005=False), "\n%s\n!=\n%s\n" % (rec_in_xm, rec_in_history))
        self.failUnless(records_identical(rec_in_xm, rec_in_bibxxx, skip_005=False, ignore_duplicate_subfields=True, ignore_duplicate_controlfields=True), "\n%s\n!=\n%s\n" % (rec_in_xm, rec_in_bibxxx))
        if cfg['CFG_BIBUPLOAD_SERIALIZE_RECORD_STRUCTURE']:
            rec_in_recstruct = loads(decompress(run_sql("SELECT value FROM bibfmt WHERE id_bibrec=%s AND format='recstruct'", (recid, ))[0][0]))
            self.failUnless(records_identical(rec_in_xm, rec_in_recstruct, skip_005=False, ignore_subfield_order=True), "\n%s\n!=\n%s\n" % (rec_in_xm, rec_in_recstruct))


class BibUploadRealCaseRemovalDOIViaBibEdit(GenericBibUploadTest):
    def test_removal_of_doi_via_bibedit(self):
        test = """<record>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">HEP</subfield>
  </datafield>
  <datafield tag="100" ind1=" " ind2=" ">
    <subfield code="a">Fiore, Gaetano</subfield>
  </datafield>
  <datafield tag="245" ind1=" " ind2=" ">
    <subfield code="a">On quantum mechanics with a magnetic field on R**n and on a torus T**n, and their relation</subfield>
  </datafield>
  <datafield tag="773" ind1=" " ind2=" ">
    <subfield code="p">Int.J.Theor.Phys.</subfield>
    <subfield code="v">52</subfield>
    <subfield code="c">877-896</subfield>
    <subfield code="y">2013</subfield>
  </datafield>
  <datafield tag="650" ind1="1" ind2="7">
    <subfield code="2">INSPIRE</subfield>
    <subfield code="a">General Physics</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">Published</subfield>
  </datafield>
  <datafield tag="300" ind1=" " ind2=" ">
    <subfield code="a">20</subfield>
  </datafield>
  <datafield tag="269" ind1=" " ind2=" ">
    <subfield code="c">2013</subfield>
  </datafield>
  <datafield tag="653" ind1="1" ind2=" ">
    <subfield code="9">author</subfield>
    <subfield code="a">Bloch theory with magnetic field</subfield>
  </datafield>
  <datafield tag="653" ind1="1" ind2=" ">
    <subfield code="9">author</subfield>
    <subfield code="a">Fiber bundles</subfield>
  </datafield>
  <datafield tag="653" ind1="1" ind2=" ">
    <subfield code="9">author</subfield>
    <subfield code="a">Gauge symmetry</subfield>
  </datafield>
  <datafield tag="653" ind1="1" ind2=" ">
    <subfield code="9">author</subfield>
    <subfield code="a">Quantization on manifolds</subfield>
  </datafield>
  <datafield tag="520" ind1=" " ind2=" ">
    <subfield code="9">Springer</subfield>
    <subfield code="a">We show in elementary terms the equivalence in a general gauge of a U(1)-gauge theory of a scalar charged particle on a torus to the analogous theory on ℝ( )n( ) constrained by quasiperiodicity under translations in the lattice Λ. The latter theory provides a global description of the former: the quasiperiodic wavefunctions ψ defined on ℝ( )n( ) play the role of sections of the associated hermitean line bundle E on , since also E admits a global description as a quotient. The components of the covariant derivatives corresponding to a constant (necessarily integral) magnetic field B=dA generate a Lie algebra g ( )Q( ) and together with the periodic functions the algebra of observables . The non-abelian part of g ( )Q( ) is a Heisenberg Lie algebra with the electric charge operator Q as the central generator, the corresponding Lie group G ( )Q( ) acts on the Hilbert space as the translation group up to phase factors. Also the space of sections of E is mapped into itself by g∈G ( )Q( ). We identify the socalled magnetic translation group as a subgroup of the observables’ group Y ( )Q( ). We determine the unitary irreducible representations of corresponding to integer charges and for each of them an associated orthonormal basis explicitly in configuration space. We also clarify how in the n=2m case a holomorphic structure and Theta functions arise on the associated complex torus.</subfield>
  </datafield>
  <datafield tag="024" ind1="7" ind2=" ">
    <subfield code="2">DOI</subfield>
    <subfield code="a">10.1007/s10773-012-1396-z</subfield>
  </datafield>
  <datafield tag="035" ind1=" " ind2=" ">
    <subfield code="a">Fiore:2013nua</subfield>
    <subfield code="9">INSPIRETeX</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">Published</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">Citeable</subfield>
  </datafield>
</record>
"""
        recs = create_record(test)
        _, recid, _ = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid)
        new_rec = get_record(recid)
        del new_rec['024'] ## let's delete DOI
        _, recid2, _ = bibupload.bibupload(new_rec, opt_mode='replace')
        self.assertEqual(recid, recid2)
        self.check_record_consistency(recid2)


class BibUploadTypicalBibEditSessionTest(GenericBibUploadTest):
    """Testing a typical BibEdit session"""

    def setUp(self):
        GenericBibUploadTest.setUp(self)
        self.test = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
        </record>
        """
        recs = bibupload.xml_marc_to_records(self.test)
        # We call the main function with the record as a parameter
        _, self.recid, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(self.recid)
        # We retrieve the inserted xml
        inserted_xm = print_record(self.recid, 'xm')
        # Compare if the two MARCXML are the same
        self.assertEqual(compare_xmbuffers(remove_tag_001_from_xmbuffer(inserted_xm),
                                          self.test), '')
        self.history = run_sql("SELECT * FROM hstRECORD WHERE id_bibrec=%s", (self.recid, )) # kwalitee: disable=sql
        self.timestamp = run_sql("SELECT modification_date FROM bibrec WHERE id=%s", (self.recid,))
        self.tag005 = get_record(self.recid)['005'][0][3]

    def test_simple_replace(self):
        """BibUpload - test a simple replace as in BibEdit"""
        marc_to_replace1 = """
        <record>
        <controlfield tag="001">%(recid)s</controlfield>
        <controlfield tag="005">%(tag005)s</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Foo</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
         <datafield tag="520" ind1=" " ind2=" ">
          <subfield code="a">bla bla bla</subfield>
         </datafield>
        </record>
        """ % {'recid': self.recid, 'tag005': self.tag005}
        recs = bibupload.xml_marc_to_records(marc_to_replace1)
        # We call the main function with the record as a parameter
        _, self.recid, _ = bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.check_record_consistency(self.recid)
        ## The change should have been applied!
        self.failUnless(records_identical(recs[0], get_record(self.recid)), "\n%s\n!=\n%s\n" % (recs[0], get_record(self.recid)))

        marc_to_replace2 = """
        <record>
        <controlfield tag="001">%(recid)s</controlfield>
        <controlfield tag="005">%(tag005)s</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
         <datafield tag="700" ind1=" " ind2=" ">
          <subfield code="a">Queen Elisabeth</subfield>
          <subfield code="u">Great Britain</subfield>
         </datafield>
        </record>
        """ % {'recid': self.recid, 'tag005': self.tag005}

        expected_marc = """
        <record>
        <controlfield tag="001">%(recid)s</controlfield>
        <controlfield tag="005">%(tag005)s</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Foo</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
         <datafield tag="520" ind1=" " ind2=" ">
          <subfield code="a">bla bla bla</subfield>
         </datafield>
         <datafield tag="700" ind1=" " ind2=" ">
          <subfield code="a">Queen Elisabeth</subfield>
          <subfield code="u">Great Britain</subfield>
         </datafield>
        </record>
        """ % {'recid': self.recid, 'tag005': self.tag005}
        recs = bibupload.xml_marc_to_records(marc_to_replace2)
        # We call the main function with the record as a parameter
        _, self.recid, _ = bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.check_record_consistency(self.recid)
        ## The change should have been merged with the previous without conflict
        self.failUnless(records_identical(bibupload.xml_marc_to_records(expected_marc)[0], get_record(self.recid)))

    def test_replace_with_conflict(self):
        """BibUpload - test a replace as in BibEdit that leads to conflicts"""
        marc_to_replace1 = """
        <record>
        <controlfield tag="001">%(recid)s</controlfield>
        <controlfield tag="005">%(tag005)s</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Foo</subfield>
          <subfield code="u">Test Institute2</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
         <datafield tag="520" ind1=" " ind2=" ">
          <subfield code="a">bla bla bla</subfield>
         </datafield>
        </record>
        """ % {'recid': self.recid, 'tag005': self.tag005}
        recs = bibupload.xml_marc_to_records(marc_to_replace1)
        # We call the main function with the record as a parameter
        _, self.recid, _ = bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.check_record_consistency(self.recid)

        ## The change should have been applied!
        self.failUnless(records_identical(recs[0], get_record(self.recid)), "\n%s\n!=\n%s" % (recs[0], get_record(self.recid)))

        marc_to_replace2 = """
        <record>
        <controlfield tag="001">%(recid)s</controlfield>
        <controlfield tag="005">%(tag005)s</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Queen Elisabeth</subfield>
          <subfield code="u">Great Britain</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">No more Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
         <datafield tag="520" ind1=" " ind2=" ">
          <subfield code="a">bla bla bla</subfield>
         </datafield>
        </record>
        """ % {'recid': self.recid, 'tag005': self.tag005}

        recs = bibupload.xml_marc_to_records(marc_to_replace2)
        # We call the main function with the record as a parameter
        _, self.recid, _ = bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.check_record_consistency(self.recid)
        ## The change should have been merged with the previous without conflict
        self.failUnless(records_identical(bibupload.xml_marc_to_records(marc_to_replace1)[0], get_record(self.recid)), "%s != %s" % (bibupload.xml_marc_to_records(marc_to_replace1)[0], get_record(self.recid)))
        self.failUnless(records_identical(bibupload.xml_marc_to_records(marc_to_replace2)[0], bibupload.xml_marc_to_records(run_sql("SELECT changeset_xml FROM bibHOLDINGPEN WHERE id_bibrec=%s", (self.recid,))[0][0])[0]))

class BibUploadNoUselessHistoryTest(GenericBibUploadTest):
    """Testing generation of history only when necessary"""

    def setUp(self):
        GenericBibUploadTest.setUp(self)
        self.test = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
        </record>
        """
        recs = bibupload.xml_marc_to_records(self.test)
        # We call the main function with the record as a parameter
        _, self.recid, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(self.recid)
        # We retrieve the inserted xml
        inserted_xm = print_record(self.recid, 'xm')
        # Compare if the two MARCXML are the same
        self.assertEqual(compare_xmbuffers(remove_tag_001_from_xmbuffer(inserted_xm),
                                          self.test), '')
        self.history = run_sql("SELECT * FROM hstRECORD WHERE id_bibrec=%s", (self.recid, )) # kwalitee: disable=sql
        self.timestamp = run_sql("SELECT modification_date FROM bibrec WHERE id=%s", (self.recid,))

    def test_replace_identical_record(self):
        """bibupload - replace with identical record does not touch history"""
        xml_to_upload = """
        <record>
        <controlfield tag="001">%s</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
        </record>
        """ % self.recid
        recs = bibupload.xml_marc_to_records(xml_to_upload)
        # We call the main function with the record as a parameter
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.check_record_consistency(recid)
        self.assertEqual(self.recid, recid)
        self.assertEqual(self.history, run_sql("SELECT * FROM hstRECORD WHERE id_bibrec=%s", (self.recid, ))) # kwalitee: disable=sql
        self.assertEqual(self.timestamp, run_sql("SELECT modification_date FROM bibrec WHERE id=%s", (self.recid,)))

    def test_correct_identical_correction(self):
        """bibupload - correct with identical correction does not touch history"""
        xml_to_upload = """
        <record>
        <controlfield tag="001">%s</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
        </record>
        """ % self.recid
        recs = bibupload.xml_marc_to_records(xml_to_upload)
        # We call the main function with the record as a parameter
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='correct')[0]
        self.check_record_consistency(recid)
        self.assertEqual(self.recid, recid)
        self.maxDiff = None
        self.assertEqual(self.history, run_sql("SELECT * FROM hstRECORD WHERE id_bibrec=%s", (self.recid, ))) # kwalitee: disable=sql
        self.assertEqual(self.timestamp, run_sql("SELECT modification_date FROM bibrec WHERE id=%s", (self.recid,)))


    def test_replace_different_record(self):
        """bibupload - replace with different records does indeed touch history"""
        xml_to_upload = """
        <record>
        <controlfield tag="001">%s</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
        </record>
        """ % self.recid
        recs = bibupload.xml_marc_to_records(xml_to_upload)
        # We call the main function with the record as a parameter
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.check_record_consistency(recid)
        self.assertEqual(self.recid, recid)
        self.assertNotEqual(self.history, run_sql("SELECT * FROM hstRECORD WHERE id_bibrec=%s", (self.recid, ))) # kwalitee: disable=sql
        self.failUnless(len(self.history) == 1 and len(run_sql("SELECT * FROM hstRECORD WHERE id_bibrec=%s", (self.recid, ))) == 2) # kwalitee: disable=sql
        self.assertNotEqual(self.timestamp, run_sql("SELECT modification_date FROM bibrec WHERE id=%s", (self.recid,)))

    def test_correct_different_correction(self):
        """bibupload - correct with different correction does indeed touch history"""
        xml_to_upload = """
        <record>
        <controlfield tag="001">%s</controlfield>
        <controlfield tag="003">FooBar</controlfield>
        </record>
        """ % self.recid
        recs = bibupload.xml_marc_to_records(xml_to_upload)
        # We call the main function with the record as a parameter
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='correct')[0]
        self.check_record_consistency(recid)
        self.assertEqual(self.recid, recid)
        self.assertNotEqual(self.history, run_sql("SELECT * FROM hstRECORD WHERE id_bibrec=%s", (self.recid, ))) # kwalitee: disable=sql
        self.failUnless(len(self.history) == 1 and len(run_sql("SELECT * FROM hstRECORD WHERE id_bibrec=%s", (self.recid, ))) == 2) # kwalitee: disable=sql
        self.assertNotEqual(self.timestamp, run_sql("SELECT modification_date FROM bibrec WHERE id=%s", (self.recid,)))


class BibUploadCallbackURLTest(GenericBibUploadTest):
    """Testing usage of CLI callback_url"""

    def setUp(self):
        GenericBibUploadTest.setUp(self)
        self.test = """<record>
        <datafield tag ="245" ind1=" " ind2=" ">
        <subfield code="a">something</subfield>
        </datafield>
        <datafield tag ="700" ind1=" " ind2=" ">
        <subfield code="a">Tester, J Y</subfield>
        <subfield code="u">MIT</subfield>
        </datafield>
        <datafield tag ="700" ind1=" " ind2=" ">
        <subfield code="a">Tester, K J</subfield>
        <subfield code="u">CERN2</subfield>
        </datafield>
        <datafield tag ="700" ind1=" " ind2=" ">
        <subfield code="a">Tester, G</subfield>
        <subfield code="u">CERN3</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="a">test11</subfield>
        <subfield code="c">test31</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="a">test12</subfield>
        <subfield code="c">test32</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="a">test13</subfield>
        <subfield code="c">test33</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="b">test21</subfield>
        <subfield code="d">test41</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="b">test22</subfield>
        <subfield code="d">test42</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="a">test14</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="e">test51</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="e">test52</subfield>
        </datafield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">CERN</subfield>
        </datafield>
        </record>"""
        self.testfile_path = os.path.join(cfg['CFG_TMPDIR'], 'bibupload_regression_test_input.xml')
        open(self.testfile_path, "w").write(self.test)
        self.resultfile_path = os.path.join(cfg['CFG_TMPDIR'], 'bibupload_regression_test_result.json')

    if False: #FIXME cfg['CFG_DEVEL_SITE']:
        def test_simple_insert_callback_url(self):
            """bibupload - --callback-url with simple insert"""
            from invenio.legacy.bibsched.bibtask import task_low_level_submission
            taskid = task_low_level_submission('bibupload', 'test', '-i', self.testfile_path, '--callback-url', cfg['CFG_SITE_URL'] + '/httptest/post2?%s' % urlencode({"save": self.resultfile_path}), '-v0')
            run_shell_command(cfg['CFG_BINDIR'] + '/bibupload %s', [str(taskid)])
            results = json.loads(open(self.resultfile_path).read())
            self.failUnless('results' in results)
            self.assertEqual(len(results['results']), 1)
            self.failUnless(results['results'][0]['success'])
            self.failUnless(results['results'][0]['recid'] > 0)
            self.failUnless("""<subfield code="a">Tester, J Y</subfield>""" in results['results'][0]['marcxml'], results['results'][0]['marcxml'])

class BibUploadBibRelationsTest(GenericBibUploadTest):
    def setUp(self):
        GenericBibUploadTest.setUp(self)
        self.upload_xml = """<record>
    <datafield tag="100" ind1=" " ind2=" ">
      <subfield code="a">A very wise author</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(url_site)s/img/user-icon-1-20x20.gif</subfield>
      <subfield code="t">Main</subfield>
      <subfield code="n">docname</subfield>
      <subfield code="i">TMP:id_identifier1</subfield>
      <subfield code="v">TMP:ver_identifier1</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(url_site)s/record/8/files/9812226.pdf?version=1</subfield>
      <subfield code="t">Main</subfield>
      <subfield code="n">docname2</subfield>
      <subfield code="i">TMP:id_identifier2</subfield>
      <subfield code="v">TMP:ver_identifier2</subfield>
    </datafield>
    <datafield tag="BDR" ind1=" " ind2=" ">
      <subfield code="i">TMP:id_identifier1</subfield>
      <subfield code="v">TMP:ver_identifier1</subfield>
      <subfield code="j">TMP:id_identifier2</subfield>
      <subfield code="w">TMP:ver_identifier2</subfield>
      <subfield code="t">is_extracted_from</subfield>
    </datafield>
  </record>""" % {'url_site' : cfg['CFG_SITE_URL']}

    def test_upload_with_tmpids(self):
        """bibupload - Trying to upload a relation between two new documents ... and then to delete"""
        recs = bibupload.xml_marc_to_records(self.upload_xml)
        _, recid, _ =  bibupload.bibupload_records(recs, opt_mode='insert')[0]
        # ertrive document numbers and check if there exists a relation between them
        brd = BibRecDocs(recid)

        docs = brd.list_bibdocs()
        self.assertEqual(2, len(docs), "Incorrect number of documents attached to a record")

        rels = docs[0].get_incoming_relations("is_extracted_from") + docs[0].get_outgoing_relations("is_extracted_from")
        self.assertEqual(1, len(rels), "Incorrect number of relations retrieved from the first document")

        rels = docs[1].get_incoming_relations("is_extracted_from") + docs[1].get_outgoing_relations("is_extracted_from")
        self.assertEqual(1, len(rels), "Incorrect number of relations retrieved from the second document")
        created_relation_id = rels[0].id

        rels = docs[0].get_incoming_relations("different_type_of_relation") + docs[0].get_outgoing_relations("different_type_of_relation")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the first document")

        upload_xml_2 = """<record>
    <controlfield tag="001">%(rec_id)s</controlfield>
    <datafield tag="BDR" ind1=" " ind2=" ">
      <subfield code="r">%(rel_id)s</subfield>
      <subfield code="d">DELETE</subfield>
    </datafield>
  </record>""" % {'rel_id' : created_relation_id, 'rec_id' : recid}
        recs = bibupload.xml_marc_to_records(upload_xml_2)

        bibupload.bibupload_records(recs, opt_mode='correct')[0]
        brd = BibRecDocs(recid)

        docs = brd.list_bibdocs()
        self.assertEqual(2, len(docs), "Incorrect number of documents attached to a record")

        rels = docs[0].get_incoming_relations("is_extracted_from") + docs[0].get_outgoing_relations("is_extracted_from")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the first document")

        rels = docs[1].get_incoming_relations("is_extracted_from") + docs[1].get_outgoing_relations("is_extracted_from")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the second document")
        rels = docs[0].get_incoming_relations("different_type_of_relation") + docs[0].get_outgoing_relations("different_type_of_relation")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the first document")

    def test_delete_by_docids(self):
        """bibupload - delete relation entry by the docid inside the currently modified record

        Uploading a sample relation and trying to modify it by refering to other parameters than
        the relation number"""
        recs = bibupload.xml_marc_to_records(self.upload_xml)
        dummyerr, recid, _ =  bibupload.bibupload_records(recs, opt_mode='insert')[0]
        brd = BibRecDocs(recid)
        docs = brd.list_bibdocs()
        self.assertEqual(2, len(docs), "Incorrect number of attached documents")

        rel = (docs[0].get_incoming_relations("is_extracted_from") + docs[0].get_outgoing_relations("is_extracted_from"))[0]

        upload_xml_2 = """<record>
    <controlfield tag="001">%(rec_id)s</controlfield>
    <datafield tag="BDR" ind1=" " ind2=" ">
      <subfield code="i">%(first_docid)s</subfield>
      <subfield code="v">%(first_docver)s</subfield>
      <subfield code="j">%(second_docid)s</subfield>
      <subfield code="w">%(second_docver)s</subfield>
      <subfield code="t">is_extracted_from</subfield>
      <subfield code="d">DELETE</subfield>
    </datafield>
  </record>""" % { 'rec_id' : recid,
                   'first_docid': rel.bibdoc1_id,
                   'first_docver' : rel.bibdoc1_ver,
                   'second_docid': rel.bibdoc2_id,
                   'second_docver' : rel.bibdoc2_ver}

        recs = bibupload.xml_marc_to_records(upload_xml_2)
        bibupload.bibupload_records(recs, opt_mode='correct')[0]
        brd = BibRecDocs(recid)

        docs = brd.list_bibdocs()
        self.assertEqual(2, len(docs), "Incorrect number of documents attached to a record")

        rels = docs[0].get_incoming_relations("is_extracted_from") + docs[0].get_outgoing_relations("is_extracted_from")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the first document")

        rels = docs[1].get_incoming_relations("is_extracted_from") + docs[1].get_outgoing_relations("is_extracted_from")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the second document")
        rels = docs[0].get_incoming_relations("different_type_of_relation") + docs[0].get_outgoing_relations("different_type_of_relation")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the first document")

    def test_remove_by_name(self):
        """bibupload - trying removing relation by providing bibdoc names rather than relation numbers"""
        recs = bibupload.xml_marc_to_records(self.upload_xml)
        _, recid, _ =  bibupload.bibupload_records(recs, opt_mode='insert')[0]
        brd = BibRecDocs(recid)
        docs = brd.list_bibdocs()
        self.assertEqual(2, len(docs), "Incorrect number of attached documents")

        rel = (docs[0].get_incoming_relations("is_extracted_from") + docs[0].get_outgoing_relations("is_extracted_from"))[0]

        upload_xml_2 = """<record>
    <controlfield tag="001">%(rec_id)s</controlfield>
    <datafield tag="BDR" ind1=" " ind2=" ">
      <subfield code="n">docname</subfield>
      <subfield code="v">%(first_docver)s</subfield>
      <subfield code="o">docname2</subfield>
      <subfield code="w">%(second_docver)s</subfield>
      <subfield code="t">is_extracted_from</subfield>
      <subfield code="d">DELETE</subfield>
    </datafield>
  </record>""" % {'rec_id' : recid,
                   'first_docver' : rel.bibdoc1_ver,
                   'second_docver' : rel.bibdoc2_ver}

        # the above is incorrect ! we assert that nothing has been removed
        recs = bibupload.xml_marc_to_records(upload_xml_2)
        _ = bibupload.bibupload_records(recs, opt_mode='correct')[0]
        brd = BibRecDocs(recid)

        docs = brd.list_bibdocs()
        self.assertEqual(2, len(docs), "Incorrect number of documents attached to a record")

        rels = docs[0].get_incoming_relations("is_extracted_from") + docs[0].get_outgoing_relations("is_extracted_from")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the first document")

        rels = docs[1].get_incoming_relations("is_extracted_from") + docs[1].get_outgoing_relations("is_extracted_from")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the second document")
        rels = docs[0].get_incoming_relations("different_type_of_relation") + docs[0].get_outgoing_relations("different_type_of_relation")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the first document")

    def test_remove_by_name_incorrect(self):
        """bibupload - trying removing relation by providing bibdoc names rather than relation numbers, but providing incorrect name"""
        recs = bibupload.xml_marc_to_records(self.upload_xml)
        _, recid, _ =  bibupload.bibupload_records(recs, opt_mode='insert')[0]
        brd = BibRecDocs(recid)
        docs = brd.list_bibdocs()
        self.assertEqual(2, len(docs), "Incorrect number of attached documents")

        rel = (docs[0].get_incoming_relations("is_extracted_from") + docs[0].get_outgoing_relations("is_extracted_from"))[0]

        upload_xml_2 = """<record>
    <controlfield tag="001">%(rec_id)s</controlfield>
    <datafield tag="BDR" ind1=" " ind2=" ">
      <subfield code="n">docname1</subfield>
      <subfield code="v">%(first_docver)s</subfield>
      <subfield code="o">docname2</subfield>
      <subfield code="w">%(second_docver)s</subfield>
      <subfield code="t">is_extracted_from</subfield>
      <subfield code="d">DELETE</subfield>
    </datafield>
  </record>""" % { 'rec_id' : recid,
                   'first_docver' : rel.bibdoc1_ver,
                   'second_docver' : rel.bibdoc2_ver}

        # the above is incorrect ! we assert that nothing has been removed
        recs = bibupload.xml_marc_to_records(upload_xml_2)
        _ = bibupload.bibupload_records(recs, opt_mode='correct')[0]
        brd = BibRecDocs(recid)

        docs = brd.list_bibdocs()
        self.assertEqual(2, len(docs), "Incorrect number of documents attached to a record")

        rels = docs[0].get_incoming_relations("is_extracted_from") + docs[0].get_outgoing_relations("is_extracted_from")
        self.assertEqual(1, len(rels), "Incorrect number of relations retrieved from the first document")

        rels = docs[1].get_incoming_relations("is_extracted_from") + docs[1].get_outgoing_relations("is_extracted_from")
        self.assertEqual(1, len(rels), "Incorrect number of relations retrieved from the second document")

        rels = docs[0].get_incoming_relations("different_type_of_relation") + docs[0].get_outgoing_relations("different_type_of_relation")
        self.assertEqual(0, len(rels), "Incorrect number of relations retrieved from the first document")

    def _upload_initial_moreinfo_key(self):
        """Prepare MoreInfo with sample keys and check it has been correctly uploaded

        uploaded dic: {"ns1" : {"k1":"val1", "k2":[1,2,3,"something"], "k3" : (1,3,2,"something else"), "k4" : {"a":"b", 1:2}}}
        ... after encoding gives KGRwMQpTJ25zMScKcDIKKGRwMwpTJ2szJwpwNAooSTEKSTMKSTIKUydzb21ldGhpbmcgZWxzZScKdHA1CnNTJ2syJwpwNgoobHA3CkkxCmFJMgphSTMKYVMnc29tZXRoaW5nJwpwOAphc1MnazEnCnA5ClMndmFsMScKcDEwCnNTJ2s0JwpwMTEKKGRwMTIKUydhJwpTJ2InCnNJMQpJMgpzc3Mu
        """
        moreinfo_str = "KGRwMQpTJ25zMScKcDIKKGRwMwpTJ2szJwpwNAooSTEKSTMKSTIKUydzb21ldGhpbmcgZWxzZScKdHA1CnNTJ2syJwpwNgoobHA3CkkxCmFJMgphSTMKYVMnc29tZXRoaW5nJwpwOAphc1MnazEnCnA5ClMndmFsMScKcDEwCnNTJ2s0JwpwMTEKKGRwMTIKUydhJwpTJ2InCnNJMQpJMgpzc3Mu"
        xml_to_upload = """<record>
    <datafield tag="100" ind1=" " ind2=" ">
      <subfield code="a">A very wise author</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(url_site)s/img/user-icon-1-20x20.gif</subfield>
      <subfield code="t">Main</subfield>
      <subfield code="n">docname</subfield>
      <subfield code="i">TMP:id_identifier1</subfield>
      <subfield code="v">TMP:ver_identifier1</subfield>
    </datafield>
    <datafield tag="FFT" ind1=" " ind2=" ">
      <subfield code="a">%(url_site)s/record/8/files/9812226.pdf?version=1</subfield>
      <subfield code="t">Main</subfield>
      <subfield code="n">docname2</subfield>
      <subfield code="i">TMP:id_identifier2</subfield>
      <subfield code="v">TMP:ver_identifier2</subfield>
    </datafield>
    <datafield tag="BDR" ind1=" " ind2=" ">
      <subfield code="i">TMP:id_identifier1</subfield>
      <subfield code="v">TMP:ver_identifier1</subfield>
      <subfield code="j">TMP:id_identifier2</subfield>
      <subfield code="w">TMP:ver_identifier2</subfield>
      <subfield code="t">is_extracted_from</subfield>
      <subfield code="m">%(moreinfo_str)s</subfield>
    </datafield>
  </record>""" % {'url_site' : cfg['CFG_SITE_URL'], 'moreinfo_str' : moreinfo_str}
        recs = bibupload.xml_marc_to_records(xml_to_upload)
        dummyerr, recid, dummy =  bibupload.bibupload_records(recs, opt_mode='insert')[0]

        brd = BibRecDocs(recid)

        docs = brd.list_bibdocs()
        self.assertEqual(2, len(docs), "Incorrect number of attached documents")
        return ((docs[0].get_incoming_relations("is_extracted_from") + docs[0].get_outgoing_relations("is_extracted_from"))[0], recid)

    def test_add_relation_moreinfo_key(self):
        """bibupload - upload new MoreInfo key into the dictionary related to a relation"""

        rel, _ = self._upload_initial_moreinfo_key()
        # asserting correctness of data


        self.assertEqual(rel.more_info.get_data("ns1", "k1"), "val1", "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k1)")

        self.assertEqual(rel.more_info.get_data("ns1", "k2")[0], 1, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")
        self.assertEqual(rel.more_info.get_data("ns1", "k2")[1], 2, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")
        self.assertEqual(rel.more_info.get_data("ns1", "k2")[2], 3, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")
        self.assertEqual(rel.more_info.get_data("ns1", "k2")[3], "something", "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")

        self.assertEqual(rel.more_info.get_data("ns1", "k3"), (1,3,2,"something else") , "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k3)")

        self.assertEqual(rel.more_info.get_data("ns1", "k4")[1], 2, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k4)")
        self.assertEqual(rel.more_info.get_data("ns1", "k4")["a"], "b", "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k4)")

    def test_modify_relation_moreinfo_key(self):
        """bibupload - modify existing MoreInfo key """

        #the update : {"ns1":{"k1": "different value"}}
        rel, recid = self._upload_initial_moreinfo_key()
        moreinfo_str = "KGRwMQpTJ25zMScKcDIKKGRwMwpTJ2sxJwpwNApTJ2RpZmZlcmVudCB2YWx1ZScKcDUKc3Mu"
        upload_xml =  """
        <record>
        <controlfield tag="001">%(rec_id)s</controlfield>
        <datafield tag="BDR" ind1=" " ind2=" ">
      <subfield code="n">docname</subfield>
      <subfield code="o">docname2</subfield>
      <subfield code="v">1</subfield>
      <subfield code="w">1</subfield>
      <subfield code="t">is_extracted_from</subfield>
      <subfield code="m">%(moreinfo_str)s</subfield>
    </datafield>
        </record>""" % {"rec_id" : recid, "moreinfo_str": moreinfo_str}



        recs = bibupload.xml_marc_to_records(upload_xml)

        bibupload.bibupload_records(recs, opt_mode='correct')[0]
        rel = BibRelation(rel_id = rel.id)

        self.assertEqual(rel.more_info.get_data("ns1", "k1"), "different value", "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k1)")

        self.assertEqual(rel.more_info.get_data("ns1", "k2")[0], 1, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")
        self.assertEqual(rel.more_info.get_data("ns1", "k2")[1], 2, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")
        self.assertEqual(rel.more_info.get_data("ns1", "k2")[2], 3, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")
        self.assertEqual(rel.more_info.get_data("ns1", "k2")[3], "something", "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")

        self.assertEqual(rel.more_info.get_data("ns1", "k3"), (1,3,2,"something else") , "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k3)")

        self.assertEqual(rel.more_info.get_data("ns1", "k4")[1], 2, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k4)")
        self.assertEqual(rel.more_info.get_data("ns1", "k4")["a"], "b", "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k4)")

        self.assertEqual(rel.more_info.get_data("ns2", "k4"), None, "Retrieved not none value for nonexisting namespace !")

    def test_remove_relation_moreinfo_key(self):
        """bibupload - remove existing MoreInfo key """

        #the update : {"ns1":{"k3": None}}
        rel, recid = self._upload_initial_moreinfo_key()
        moreinfo_str = "KGRwMQpTJ25zMScKcDIKKGRwMwpTJ2szJwpwNApOc3Mu"
        upload_xml =  """
        <record>
        <controlfield tag="001">%(rec_id)s</controlfield>
        <datafield tag="BDR" ind1=" " ind2=" ">
      <subfield code="n">docname</subfield>
      <subfield code="o">docname2</subfield>
      <subfield code="v">1</subfield>
      <subfield code="w">1</subfield>
      <subfield code="t">is_extracted_from</subfield>
      <subfield code="m">%(moreinfo_str)s</subfield>
    </datafield>
        </record>""" % {"rec_id" : recid, "moreinfo_str": moreinfo_str}

        recs = bibupload.xml_marc_to_records(upload_xml)
        bibupload.bibupload_records(recs, opt_mode='correct')
        rel = BibRelation(rel_id = rel.id)

        self.assertEqual(rel.more_info.get_data("ns1", "k1"), "val1", "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k1)")

        self.assertEqual(rel.more_info.get_data("ns1", "k2")[0], 1, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")
        self.assertEqual(rel.more_info.get_data("ns1", "k2")[1], 2, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")
        self.assertEqual(rel.more_info.get_data("ns1", "k2")[2], 3, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")
        self.assertEqual(rel.more_info.get_data("ns1", "k2")[3], "something", "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k2)")

        self.assertEqual(rel.more_info.get_data("ns1", "k3"), None , "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k3)")

        self.assertEqual(rel.more_info.get_data("ns1", "k4")[1], 2, "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k4)")
        self.assertEqual(rel.more_info.get_data("ns1", "k4")["a"], "b", "Retrieved incorrect data from the MoreInfo Dictionary (namespace : ns1 key: k4)")

class BibUploadMoreInfoTest(GenericBibUploadTest):
    """bibupload -  Testing upload of different types of MoreInfo """

    def _dict_checker(self, dic, more_info, equal = True):
        """ Check the more_info for being conform with the dictionary
        @param equal - The mode of conformity. True means that the dictionary
               has to be equal with the MoreInfo. False means that dictionary
               has to be contained in the MoreInfo
        """
        for namespace in dic:
            for key in dic[namespace]:
                self.assertEqual(cPickle.dumps(dic[namespace][key]),
                                 cPickle.dumps(more_info.get_data(namespace, key)),
                                 "Different values for the value of key %s in the namespace %s inside of the MoreInfo object" % \
                                     (namespace, key))

        if equal:
            for namespace in more_info.get_namespaces():
                for key in more_info.get_keys(namespace):
                    self.assertTrue(namespace in dic,
                                    "namespace %s present in the MoreInfo, but not present in the dictionary" % \
                                        (namespace, ))
                    self.assertTrue(key in dic[namespace],
                                    "key %s present in the namespace %s of the MoreInfo but not present in the dictionary" % \
                                        (namespace, key))
                    self.assertEqual(cPickle.dumps(more_info.get_data(namespace, key)),
                                     cPickle.dumps(dic[namespace][key]),
                                     "Value for namespace '%s' and key '%s' varies between MoreInfo and the dictionary. moreinfo value: '%s' dictionary value: '%s'" % \
                                         (namespace, key, repr(more_info.get_data(namespace, key)), repr(dic[namespace][key])))
    def test_relation_moreinfo_insert(self):
        """bibupload - Testing the upload of BibRelation and corresponding MoreInfo field"""
        # Cleaning existing data
        rels = BibRelation.get_relations(bibdoc1_id = 70, bibdoc2_id = 71, rel_type = "is_extracted_from")
        for rel in rels:
            rel.delete()

        # Uploading
        relation_upload_template = """
        <record>
           <datafield tag="BDR" ind1=" " ind2=" ">
              <subfield code="i">70</subfield>
              <subfield code="j">71</subfield>
              <subfield code="t">is_extracted_from</subfield>
              <subfield code="m">%s</subfield>
           </datafield>
           <datafield tag="100" ind1=" " ind2=" ">
              <subfield code="a">Some author</subfield>
           </datafield>
        </record>"""
        data_to_insert = {"first namespace": {"k1" : "val1", "k2" : "val2"},
                          "second" : {"k1" : "#@$#$@###!!!", "k123": {1:2, 9: (6,2,7)}}}
        serialised = base64.b64encode(cPickle.dumps(data_to_insert))

        recs = bibupload.xml_marc_to_records(relation_upload_template % (serialised, ))
        bibupload.bibupload_records(recs, opt_mode='insert')[0]

        # Verifying the correctness of the uploaded data
        rels = BibRelation.get_relations(bibdoc1_id = 70, bibdoc2_id = 71, rel_type = "is_extracted_from")
        self.assertEqual(len(rels), 1)
        rel = rels[0]

        self.assertEqual(rel.bibdoc1_id, 70)
        self.assertEqual(rel.bibdoc2_id, 71)
        self.assertEqual(rel.get_data("first namespace", "k1"), "val1")
        self.assertEqual(rel.get_data("first namespace", "k2"), "val2")
        self.assertEqual(rel.get_data("second", "k1"), "#@$#$@###!!!")
        self.assertEqual(rel.get_data("second", "k123")[1], 2)
        self.assertEqual(rel.get_data("second", "k123")[9], (6,2,7))

        self._dict_checker(data_to_insert, rel.more_info)

        # Cleaning after the upload ... just in case we have selected more
        for rel in rels:
            rel.delete()

    def _serialise_data(self, data):
        return base64.b64encode(cPickle.dumps(data))

    # Subfield tags used to upload particular types of MoreInfo
    _mi_bibdoc = "w"
    _mi_bibdoc_version = "p"
    _mi_bibdoc_version_format = "b"
    _mi_bibdoc_format = "u"

    def _generate_moreinfo_tag(self, mi_type, data):
        """
        """
        serialised = self._serialise_data(data)
        return """<subfield code="%s">%s</subfield>""" % (mi_type, serialised)

    def test_document_moreinfo_insert(self):
        """bibupload - Inserting new MoreInfo to the document
        1) Inserting new MoreInfo to new document
        2) Inserting new MoreInfo keys existing document version
        3) Removing keys from MoreInfo
        4) Removing document and asserting, MoreInfo gets removed as well
        5) Overriding MoreInfo keys
        """

        moreinfo_upload_template = """
        <record>
            <datafield tag="FFT" ind1=" " ind2=" ">
               <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
               <subfield code="n">0106015_01</subfield>
               <subfield code="f">.jpg</subfield>
               <subfield code="r">restricted_picture</subfield>
               %%(additional_content)s
           </datafield>
           <datafield tag="100" ind1=" " ind2=" ">
              <subfield code="a">Some author</subfield>
           </datafield>
        </record>""" % {"siteurl": cfg['CFG_SITE_URL']}

        sfs = []
        sfs.append(self._generate_moreinfo_tag(BibUploadMoreInfoTest._mi_bibdoc,
                                               {"first namespace" :
                                                {"type": "document moreinfo"}}))
        sfs.append(self._generate_moreinfo_tag(BibUploadMoreInfoTest._mi_bibdoc_version,
                                               {"first namespace" :
                                                {"type": "Bibdoc - version moreinfo"}}))
        sfs.append(self._generate_moreinfo_tag(BibUploadMoreInfoTest._mi_bibdoc_version_format,
                                               {"first namespace" :
                                                {"type": "Bibdoc - version, format moreinfo"}}))
        sfs.append(self._generate_moreinfo_tag(BibUploadMoreInfoTest._mi_bibdoc_format,
                                               {"first namespace" :
                                                {"type": "Bibdoc - format moreinfo"}}))
        marcxml_1 = moreinfo_upload_template % {"additional_content" : "\n".join(sfs)}
        recs = bibupload.xml_marc_to_records(marcxml_1)
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        # now checking if all the data has been uploaded correctly

        bdr = BibRecDocs(recid)
        doc = bdr.list_bibdocs()[0]
        docid = doc.get_id()
        mi_doc = MoreInfo(docid = docid)
        mi_doc_ver = MoreInfo(docid = docid, version = 1)
        mi_doc_ver_fmt = MoreInfo(docid = docid, version = 1, docformat=".jpg")
        mi_doc_fmt = MoreInfo(docid = docid, docformat=".jpg")
        self._dict_checker({"first namespace" : {"type": "document moreinfo"}},
                           mi_doc, equal=False) # in case of the document only inclusive check
        self._dict_checker({"first namespace" : {"type": "Bibdoc - version moreinfo"}},
                           mi_doc_ver)
        self._dict_checker({"first namespace" : {
                    "type": "Bibdoc - version, format moreinfo"}},
                           mi_doc_ver_fmt)
        self._dict_checker({"first namespace" : {"type": "Bibdoc - format moreinfo"}},
                           mi_doc_fmt)
        #now appending to a particular version of MoreInfo
        # uplad new key to an existing dictionary of a version
        def _get_mit_template(recid, bibdocid=None, bibdocname=None,
                              version=None, docformat=None, relation=None, data=None):
            if data is None:
                ser = None
            else:
                ser = base64.b64encode(cPickle.dumps(data))
            subfields = []

            for s_code, val in (("r", relation), ("i", bibdocid),
                                ("n", bibdocname), ("v", version),
                                ("f", docformat) , ("m", ser)):
                if not val is None:
                    subfields.append("""<subfield code="%s">%s</subfield>""" % \
                                         (s_code, val))

            return """<record>
              <controlfield tag="001">%s</controlfield>
              <datafield tag="BDM" ind1=" " ind2=" ">
                 %s
              </datafield>
              </record>""" % (str(recid), ("\n".join(subfields)))

        marcxml_2 = _get_mit_template(recid, version = 1, bibdocid = docid,
                                       data= {"first namespace" :
                                              {"new key": {1:2, 987:678}}})
        recs = bibupload.xml_marc_to_records(marcxml_2)
        bibupload.bibupload_records(recs, opt_mode='append')
        mi = MoreInfo(docid = docid, version = 1)

        self._dict_checker({
                "first namespace" : {"type": "Bibdoc - version moreinfo",
                                     "new key": {1:2, 987:678}
                                     }
                }, mi)

        #removing the entire old content of the MoreInfo and uploading new
        data = {"ns1" : {"nk1": 12, "mk1": "this is new content"},
                "namespace two" : {"ddd" : "bbb"}}
        marcxml_3 = _get_mit_template(recid, version = 1, bibdocid = docid,
                                       data= data)
        recs = bibupload.xml_marc_to_records(marcxml_3)
        bibupload.bibupload_records(recs, opt_mode='correct')
        mi = MoreInfo(docid = docid, version = 1)
        self._dict_checker(data, mi)

        # removing a particular key

        marcxml_4 = _get_mit_template(recid, version = 1, bibdocid = docid,
                                       data= {"ns1": {"nk1" : None}})
        recs = bibupload.xml_marc_to_records(marcxml_4)
        bibupload.bibupload_records(recs, opt_mode='append')
        mi = MoreInfo(docid = docid, version = 1)
        self._dict_checker( {"ns1" : { "mk1": "this is new content"},
                "namespace two" : {"ddd" : "bbb"}}, mi)

        # adding new key
        marcxml_5 = _get_mit_template(recid, version = 1, bibdocid = docid,
                                       data= {"ns1": {"newkey" : "newvalue"}})
        recs = bibupload.xml_marc_to_records(marcxml_5)
        bibupload.bibupload_records(recs, opt_mode='append')
        mi = MoreInfo(docid = docid, version = 1)
        self._dict_checker( {"ns1" : { "mk1": "this is new content", "newkey" : "newvalue"},
                "namespace two" : {"ddd" : "bbb"}}, mi)


class BibUploadInsertModeTest(GenericBibUploadTest):
    """Testing insert mode."""

    def setUp(self):
        # pylint: disable=C0103
        """Initialise the MARCXML variable"""
        GenericBibUploadTest.setUp(self)
        self.test = """<record>
        <datafield tag ="245" ind1=" " ind2=" ">
        <subfield code="a">something</subfield>
        </datafield>
        <datafield tag ="700" ind1=" " ind2=" ">
        <subfield code="a">Tester, J Y</subfield>
        <subfield code="u">MIT</subfield>
        </datafield>
        <datafield tag ="700" ind1=" " ind2=" ">
        <subfield code="a">Tester, K J</subfield>
        <subfield code="u">CERN2</subfield>
        </datafield>
        <datafield tag ="700" ind1=" " ind2=" ">
        <subfield code="a">Tester, G</subfield>
        <subfield code="u">CERN3</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="a">test11</subfield>
        <subfield code="c">test31</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="a">test12</subfield>
        <subfield code="c">test32</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="a">test13</subfield>
        <subfield code="c">test33</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="b">test21</subfield>
        <subfield code="d">test41</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="b">test22</subfield>
        <subfield code="d">test42</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="a">test14</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="e">test51</subfield>
        </datafield>
        <datafield tag ="111" ind1=" " ind2=" ">
        <subfield code="e">test52</subfield>
        </datafield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">CERN</subfield>
        </datafield>
        </record>"""
        self.test_hm = """
        100__ $$aTester, T$$uCERN
        111__ $$atest11$$ctest31
        111__ $$atest12$$ctest32
        111__ $$atest13$$ctest33
        111__ $$btest21$$dtest41
        111__ $$btest22$$dtest42
        111__ $$atest14
        111__ $$etest51
        111__ $$etest52
        245__ $$asomething
        700__ $$aTester, J Y$$uMIT
        700__ $$aTester, K J$$uCERN2
        700__ $$aTester, G$$uCERN3
        """

    def test_create_record_id(self):
        """bibupload - insert mode, trying to create a new record ID in the database"""
        rec_id = bibupload.create_new_record()
        self.assertNotEqual(None, rec_id)

    def test_create_specific_record_id(self):
        """bibupload - insert mode, trying to create a new specifc record ID in the database"""
        expected_rec_id = run_sql("SELECT MAX(id) FROM bibrec")[0][0] + 1
        rec_id = bibupload.create_new_record(expected_rec_id)
        self.assertEqual(rec_id, expected_rec_id)

    def test_no_retrieve_record_id(self):
        """bibupload - insert mode, detection of record ID in the input file"""
        # We create create the record out of the xml marc
        recs = bibupload.xml_marc_to_records(self.test)
        # We call the function which should retrieve the record id
        rec_id = bibupload.retrieve_rec_id(recs[0], 'insert')
        # We compare the value found with None
        self.assertEqual(None, rec_id)

    def test_insert_complete_xmlmarc(self):
        """bibupload - insert mode, trying to insert complete MARCXML file"""
        # Initialize the global variable
        # We create create the record out of the xml marc
        recs = bibupload.xml_marc_to_records(self.test)
        # We call the main function with the record as a parameter
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # We retrieve the inserted xml
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        inserted_hm = print_record(recid, 'hm')
        # Compare if the two MARCXML are the same
        self.assertEqual(compare_xmbuffers(remove_tag_001_from_xmbuffer(inserted_xm),
                                          self.test), '')
        self.assertEqual(compare_hmbuffers(remove_tag_001_from_hmbuffer(inserted_hm),
                                          self.test_hm), '')

    def test_retrieve_005_tag(self):
        """bibupload - insert mode, verifying insertion of 005 control field for record """
        # Convert marc xml into record structure
        from invenio.legacy.bibrecord import record_has_field, record_get_field_value
        recs = bibupload.xml_marc_to_records(self.test)
        dummy, recid, dummy = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid)
        # Retrive the inserted record based on the record id
        rec = get_record(recid)
        # We retrieve the creationdate date from the database
        query = """SELECT DATE_FORMAT(last_updated,'%%Y%%m%%d%%H%%i%%s') FROM bibfmt where id_bibrec=%s AND format='xm'"""
        res = run_sql(query, (recid, ))
        self.assertEqual(record_has_field(rec, '005'), True)
        self.assertEqual(str(res[0][0]) + '.0', record_get_field_value(rec, '005', '', ''))

class BibUploadAppendModeTest(GenericBibUploadTest):
    """Testing append mode."""

    def setUp(self):
        # pylint: disable=C0103
        """Initialize the MARCXML variable"""
        GenericBibUploadTest.setUp(self)
        self.test_existing = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHOPHO</subfield>
        </datafield>
        </record>"""
        self.test_to_append = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, U</subfield>
        <subfield code="u">CERN</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHOPHO</subfield>
        </datafield>
        </record>"""
        self.test_expected_xm = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">DESY</subfield>
        </datafield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, U</subfield>
        <subfield code="u">CERN</subfield>
        </datafield>
        <datafield tag ="970" ind1=" " ind2=" ">
        <subfield code="a">0003719PHOPHO</subfield>
        </datafield>
        </record>"""
        self.test_expected_hm = """
        001__ 123456789
        100__ $$aTester, T$$uDESY
        100__ $$aTester, U$$uCERN
        970__ $$a0003719PHOPHO
        """
        # insert test record:

        test_to_upload =  self.test_existing.replace('<controlfield tag="001">123456789</controlfield>',
                                                     '')
        recs = bibupload.xml_marc_to_records(test_to_upload)
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        self.test_recid = recid
        # replace test buffers with real recid of inserted test record:
        self.test_existing = self.test_existing.replace('123456789',
                                                        str(self.test_recid))
        self.test_to_append = self.test_to_append.replace('123456789',
                                                          str(self.test_recid))
        self.test_expected_xm = self.test_expected_xm.replace('123456789',
                                                              str(self.test_recid))
        self.test_expected_hm = self.test_expected_hm.replace('123456789',
                                                              str(self.test_recid))

    def test_retrieve_record_id(self):
        """bibupload - append mode, the input file should contain a record ID"""
        # We create create the record out of the xml marc
        recs = bibupload.xml_marc_to_records(self.test_to_append)
        # We call the function which should retrieve the record id
        rec_id = bibupload.retrieve_rec_id(recs[0], 'append')
        # We compare the value found with None
        self.assertEqual(self.test_recid, rec_id)
        # clean up after ourselves:

    def test_update_modification_record_date(self):
        """bibupload - append mode, checking the update of the modification date"""
        from invenio.utils.date import convert_datestruct_to_datetext
        # Initialize the global variable
        # We create create the record out of the xml marc
        recs = bibupload.xml_marc_to_records(self.test_existing)
        # We call the function which should retrieve the record id
        rec_id = bibupload.retrieve_rec_id(recs[0], opt_mode='append')
        # Retrieve current localtime
        now = time.localtime()
        # We update the modification date
        bibupload.update_bibrec_date(convert_datestruct_to_datetext(now), rec_id, False)
        # We retrieve the modification date from the database
        query = """SELECT DATE_FORMAT(modification_date,'%%Y-%%m-%%d %%H:%%i:%%s') FROM bibrec where id = %s"""
        res = run_sql(query, (str(rec_id), ))
        # We compare the two results
        self.assertEqual(res[0][0], convert_datestruct_to_datetext(now))
        # clean up after ourselves:

    def test_append_complete_xml_marc(self):
        """bibupload - append mode, appending complete MARCXML file"""
        # Now we append a datafield
        # We create create the record out of the xml marc
        recs = bibupload.xml_marc_to_records(self.test_to_append)
        # We call the main function with the record as a parameter
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='append')[0]
        self.check_record_consistency(recid)
        # We retrieve the inserted xm
        after_append_xm = print_record(recid, 'xm')
        after_append_hm = print_record(recid, 'hm')
        # Compare if the two MARCXML are the same
        self.assertEqual(compare_xmbuffers(after_append_xm, self.test_expected_xm), '')
        self.assertEqual(compare_hmbuffers(after_append_hm, self.test_expected_hm), '')

    def test_retrieve_updated_005_tag(self):
        """bibupload - append mode, updating 005 control tag after modifiction """
        from invenio.legacy.bibrecord import record_get_field_value
        recs = bibupload.xml_marc_to_records(self.test_to_append)
        _, recid, _ = bibupload.bibupload(recs[0], opt_mode='append')
        self.check_record_consistency(recid)
        rec = get_record(recid)
        query = """SELECT DATE_FORMAT(MAX(job_date),'%%Y%%m%%d%%H%%i%%s') FROM hstRECORD where id_bibrec = %s"""
        res =  run_sql(query, (str(recid), ))
        self.assertEqual(str(res[0][0])+'.0',record_get_field_value(rec,'005','',''))

class BibUploadCorrectModeTest(GenericBibUploadTest):
    """
    Testing correcting a record containing similar tags (identical
    tag, different indicators).  Currently Invenio replaces only
    those tags that have matching indicators too, unlike ALEPH500 that
    does not pay attention to indicators, it corrects all fields with
    the same tag, regardless of the indicator values.
    """

    def setUp(self):
        """Initialize the MARCXML test record."""
        GenericBibUploadTest.setUp(self)
        self.testrec1_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
        <datafield tag="100" ind1=" " ind2=" ">
         <subfield code="a">Test, Jane</subfield>
         <subfield code="u">Test Institute</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test, John</subfield>
         <subfield code="u">Test University</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="8">
         <subfield code="a">Cool</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test, Jim</subfield>
         <subfield code="u">Test Laboratory</subfield>
        </datafield>
        </record>
        """
        self.testrec1_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, Jane$$uTest Institute
        10047 $$aTest, John$$uTest University
        10048 $$aCool
        10047 $$aTest, Jim$$uTest Laboratory
        """
        self.testrec1_xm_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test, Joseph</subfield>
         <subfield code="u">Test Academy</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test2, Joseph</subfield>
         <subfield code="u">Test2 Academy</subfield>
        </datafield>
        </record>
        """
        self.testrec1_corrected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
        <datafield tag="100" ind1=" " ind2=" ">
         <subfield code="a">Test, Jane</subfield>
         <subfield code="u">Test Institute</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="8">
         <subfield code="a">Cool</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test, Joseph</subfield>
         <subfield code="u">Test Academy</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test2, Joseph</subfield>
         <subfield code="u">Test2 Academy</subfield>
        </datafield>
        </record>
        """
        self.testrec1_corrected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, Jane$$uTest Institute
        10048 $$aCool
        10047 $$aTest, Joseph$$uTest Academy
        10047 $$aTest2, Joseph$$uTest2 Academy
        """
        # insert test record:
        test_record_xm = self.testrec1_xm.replace('<controlfield tag="001">123456789</controlfield>',
                                                  '')
        recs = bibupload.xml_marc_to_records(test_record_xm)
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recID:
        self.testrec1_xm = self.testrec1_xm.replace('123456789', str(recid))
        self.testrec1_hm = self.testrec1_hm.replace('123456789', str(recid))
        self.testrec1_xm_to_correct = self.testrec1_xm_to_correct.replace('123456789', str(recid))
        self.testrec1_corrected_xm = self.testrec1_corrected_xm.replace('123456789', str(recid))
        self.testrec1_corrected_hm = self.testrec1_corrected_hm.replace('123456789', str(recid))
        # test of the inserted record:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm, self.testrec1_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm, self.testrec1_hm), '')

    def test_record_correction(self):
        """bibupload - correct mode, similar MARCXML tags/indicators"""
        # correct some tags:
        recs = bibupload.xml_marc_to_records(self.testrec1_xm_to_correct)
        _, self.recid, _ = bibupload.bibupload_records(recs, opt_mode='correct')[0]
        self.check_record_consistency(self.recid)
        corrected_xm = print_record(self.recid, 'xm')
        corrected_hm = print_record(self.recid, 'hm')
        # did it work?
        self.assertEqual(compare_xmbuffers(corrected_xm, self.testrec1_corrected_xm), '')
        self.assertEqual(compare_hmbuffers(corrected_hm, self.testrec1_corrected_hm), '')
        # clean up after ourselves:
        return

class BibUploadDeleteModeTest(GenericBibUploadTest):
    """
    Testing deleting specific tags from a record while keeping anything else
    untouched.  Currently Invenio deletes only those tags that have
    matching indicators too, unlike ALEPH500 that does not pay attention to
    indicators, it corrects all fields with the same tag, regardless of the
    indicator values.
    """

    def setUp(self):
        """Initialize the MARCXML test record."""
        GenericBibUploadTest.setUp(self)
        self.testrec1_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
        <datafield tag="100" ind1=" " ind2=" ">
         <subfield code="a">Test, Jane</subfield>
         <subfield code="u">Test Institute</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test, John</subfield>
         <subfield code="u">Test University</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="8">
         <subfield code="a">Cool</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test, Jim</subfield>
         <subfield code="u">Test Laboratory</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
         <subfield code="a">dumb text</subfield>
        </datafield>
        </record>
        """
        self.testrec1_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, Jane$$uTest Institute
        10047 $$aTest, John$$uTest University
        10048 $$aCool
        10047 $$aTest, Jim$$uTest Laboratory
        888__ $$adumb text
        """
        self.testrec1_xm_to_delete = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag="100" ind1=" " ind2=" ">
         <subfield code="a">Test, Jane</subfield>
         <subfield code="u">Test Institute</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test, Johnson</subfield>
         <subfield code="u">Test University</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="8">
         <subfield code="a">Cool</subfield>
        </datafield>
        <datafield tag="888" ind1=" " ind2=" ">
         <subfield code="a">dumb text</subfield>
        </datafield>
        </record>
        """
        self.testrec1_corrected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test, John</subfield>
         <subfield code="u">Test University</subfield>
        </datafield>
        <datafield tag="100" ind1="4" ind2="7">
         <subfield code="a">Test, Jim</subfield>
         <subfield code="u">Test Laboratory</subfield>
        </datafield>
        </record>
        """
        self.testrec1_corrected_hm = """
        001__ 123456789
        003__ SzGeCERN
        10047 $$aTest, John$$uTest University
        10047 $$aTest, Jim$$uTest Laboratory
        """
        # insert test record:
        test_record_xm = self.testrec1_xm.replace('<controlfield tag="001">123456789</controlfield>',
                                                  '')
        recs = bibupload.xml_marc_to_records(test_record_xm)
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recID:
        self.testrec1_xm = self.testrec1_xm.replace('123456789', str(recid))
        self.testrec1_hm = self.testrec1_hm.replace('123456789', str(recid))
        self.testrec1_xm_to_delete = self.testrec1_xm_to_delete.replace('123456789', str(recid))
        self.testrec1_corrected_xm = self.testrec1_corrected_xm.replace('123456789', str(recid))
        self.testrec1_corrected_hm = self.testrec1_corrected_hm.replace('123456789', str(recid))
        # test of the inserted record:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm, self.testrec1_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm, self.testrec1_hm), '')
        # Checking dumb text is in bibxxx
        self.failUnless(run_sql("SELECT id_bibrec from bibrec_bib88x WHERE id_bibrec=%s", (recid, )))

    def test_record_tags_deletion(self):
        """bibupload - delete mode, deleting specific tags"""
        # correct some tags:
        recs = bibupload.xml_marc_to_records(self.testrec1_xm_to_delete)
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='delete')[0]
        self.check_record_consistency(recid)
        corrected_xm = print_record(recid, 'xm')
        corrected_hm = print_record(recid, 'hm')
        # did it work?
        self.assertEqual(compare_xmbuffers(corrected_xm, self.testrec1_corrected_xm), '')
        self.assertEqual(compare_hmbuffers(corrected_hm, self.testrec1_corrected_hm), '')
        # Checking dumb text is no more in bibxxx
        self.failIf(run_sql("SELECT id_bibrec from bibrec_bib88x WHERE id_bibrec=%s", (recid, )))
        # clean up after ourselves:


class BibUploadReplaceModeTest(GenericBibUploadTest):
    """Testing replace mode."""

    def test_record_replace(self):
        """bibupload - replace mode, similar MARCXML tags/indicators"""
        # replace some tags:
        testrec1_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
        </record>
        """
        testrec1_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, Jane$$uTest Institute
        10047 $$aTest, John$$uTest University
        10048 $$aCool
        10047 $$aTest, Jim$$uTest Laboratory
        """
        testrec1_xm_to_replace = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Joseph</subfield>
          <subfield code="u">Test Academy</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test2, Joseph</subfield>
          <subfield code="u">Test2 Academy</subfield>
         </datafield>
        </record>
        """
        testrec1_replaced_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Joseph</subfield>
          <subfield code="u">Test Academy</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test2, Joseph</subfield>
          <subfield code="u">Test2 Academy</subfield>
         </datafield>
        </record>
        """
        testrec1_replaced_hm = """
        001__ 123456789
        10047 $$aTest, Joseph$$uTest Academy
        10047 $$aTest2, Joseph$$uTest2 Academy
        """
        # insert test record:
        test_record_xm = testrec1_xm.replace('<controlfield tag="001">123456789</controlfield>',
                                                  '')
        recs = bibupload.xml_marc_to_records(test_record_xm)
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recID:
        testrec1_xm = testrec1_xm.replace('123456789', str(recid))
        testrec1_hm = testrec1_hm.replace('123456789', str(recid))
        testrec1_xm_to_replace = testrec1_xm_to_replace.replace('123456789', str(recid))
        testrec1_replaced_xm = testrec1_replaced_xm.replace('123456789', str(recid))
        testrec1_replaced_hm = testrec1_replaced_hm.replace('123456789', str(recid))
        # test of the inserted record:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm, testrec1_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm, testrec1_hm), '')
        recs = bibupload.xml_marc_to_records(testrec1_xm_to_replace)
        _, recid, _ = bibupload.bibupload(recs[0], opt_mode='replace')
        self.check_record_consistency(recid)
        replaced_xm = print_record(recid, 'xm')
        replaced_hm = print_record(recid, 'hm')
        # did it work?
        self.assertEqual(compare_xmbuffers(replaced_xm, testrec1_replaced_xm), '')
        self.assertEqual(compare_hmbuffers(replaced_hm, testrec1_replaced_hm), '')

    def test_record_replace_force_non_existing(self):
        """bibupload - replace mode, force non existing recid"""
        from invenio.legacy.bibsched.bibtask import task_set_option
        # replace some tags:
        the_recid = self.last_recid + 1
        testrec1_xm = """
        <record>
        <controlfield tag="001">%s</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
        </record>
        """ % the_recid
        testrec1_hm = """
        001__ %s
        003__ SzGeCERN
        100__ $$aTest, Jane$$uTest Institute
        10047 $$aTest, John$$uTest University
        10048 $$aCool
        10047 $$aTest, Jim$$uTest Laboratory
        """ % the_recid
        recs = bibupload.xml_marc_to_records(testrec1_xm)
        task_set_option('force', True)
        try:
            err, recid, msg = bibupload.bibupload_records(recs, opt_mode='replace')[0]
            self.check_record_consistency(recid)
        finally:
            task_set_option('force', False)
        replaced_xm = print_record(recid, 'xm')
        replaced_hm = print_record(recid, 'hm')
        # did it work?
        self.assertEqual(compare_xmbuffers(replaced_xm, testrec1_xm), '')
        self.assertEqual(compare_hmbuffers(replaced_hm, testrec1_hm), '')
        self.assertEqual(recid, the_recid)

    def test_record_replace_non_existing(self):
        """bibupload - replace mode, non existing recid"""
        # replace some tags:
        the_recid = self.last_recid + 1
        testrec1_xm = """
        <record>
        <controlfield tag="001">%s</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
        </record>
        """ % the_recid

        recs = bibupload.xml_marc_to_records(testrec1_xm)
        err, recid, _ = bibupload.bibupload(recs[0], opt_mode='replace')
        self.assertEqual((err, recid), (1, -1))

    def test_record_replace_two_recids(self):
        """bibupload - replace mode, two recids"""
        # replace some tags:
        testrec1_xm = """
        <record>
        <controlfield tag="001">300</controlfield>
        <controlfield tag="001">305</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="8">
          <subfield code="a">Cool</subfield>
         </datafield>
         <datafield tag="100" ind1="4" ind2="7">
          <subfield code="a">Test, Jim</subfield>
          <subfield code="u">Test Laboratory</subfield>
         </datafield>
        </record>
        """
        recs = bibupload.xml_marc_to_records(testrec1_xm)
        err, recid, _ = bibupload.bibupload(recs[0], opt_mode='replace')
        # did it work?
        self.assertEqual((err, recid), (1, -1))


class BibUploadReferencesModeTest(GenericBibUploadTest):
    """Testing references mode.
    NOTE: in the past this was done by calling bibupload --reference|-z
    which is now simply implying bibupload --correct.
    """

    def setUp(self):
        """Initialize the MARCXML variable"""
        GenericBibUploadTest.setUp(self)
        self.test_insert = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">CERN</subfield>
        </datafield>
        </record>"""
        self.test_reference = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag =\"""" + cfg['CFG_BIBUPLOAD_REFERENCE_TAG'] + """\" ind1="C" ind2="5">
        <subfield code="m">M. Lüscher and P. Weisz, String excitation energies in SU(N) gauge theories beyond the free-string approximation,</subfield>
        <subfield code="s">J. High Energy Phys. 07 (2004) 014</subfield>
        </datafield>
        </record>"""
        self.test_reference_expected_xm = """<record>
        <controlfield tag="001">123456789</controlfield>
        <datafield tag ="100" ind1=" " ind2=" ">
        <subfield code="a">Tester, T</subfield>
        <subfield code="u">CERN</subfield>
        </datafield>
        <datafield tag =\"""" + cfg['CFG_BIBUPLOAD_REFERENCE_TAG'] + """\" ind1="C" ind2="5">
        <subfield code="m">M. Lüscher and P. Weisz, String excitation energies in SU(N) gauge theories beyond the free-string approximation,</subfield>
        <subfield code="s">J. High Energy Phys. 07 (2004) 014</subfield>
        </datafield>
        </record>"""
        self.test_insert_hm = """
        001__ 123456789
        100__ $$aTester, T$$uCERN
        """
        self.test_reference_expected_hm = """
        001__ 123456789
        100__ $$aTester, T$$uCERN
        %(reference_tag)sC5 $$mM. Lüscher and P. Weisz, String excitation energies in SU(N) gauge theories beyond the free-string approximation,$$sJ. High Energy Phys. 07 (2004) 014
        """ % {'reference_tag': cfg['CFG_BIBUPLOAD_REFERENCE_TAG']}
        # insert test record:
        test_insert = self.test_insert.replace('<controlfield tag="001">123456789</controlfield>',
                                               '')
        recs = bibupload.xml_marc_to_records(test_insert)
        _, recid, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recID:
        self.test_insert = self.test_insert.replace('123456789', str(recid))
        self.test_insert_hm = self.test_insert_hm.replace('123456789', str(recid))
        self.test_reference = self.test_reference.replace('123456789', str(recid))
        self.test_reference_expected_xm = self.test_reference_expected_xm.replace('123456789', str(recid))
        self.test_reference_expected_hm = self.test_reference_expected_hm.replace('123456789', str(recid))
        # test of the inserted record:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm, self.test_insert), '')
        self.assertEqual(compare_hmbuffers(inserted_hm, self.test_insert_hm), '')
        self.test_recid = recid

    def test_reference_complete_xml_marc(self):
        """bibupload - reference mode, inserting references MARCXML file"""
        # We create create the record out of the xml marc
        recs = bibupload.xml_marc_to_records(self.test_reference)
        # We call the main function with the record as a parameter
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='reference')[0]
        self.check_record_consistency(recid)
        # We retrieve the inserted xml
        reference_xm = print_record(recid, 'xm')
        reference_hm = print_record(recid, 'hm')
        # Compare if the two MARCXML are the same
        self.assertEqual(compare_xmbuffers(reference_xm, self.test_reference_expected_xm), '')
        self.assertEqual(compare_hmbuffers(reference_hm, self.test_reference_expected_hm), '')


class BibUploadRecordsWithSYSNOTest(GenericBibUploadTest):
    """Testing uploading of records that have external SYSNO present."""

    def setUp(self):
        # pylint: disable=C0103
        """Initialize the MARCXML test records."""
        GenericBibUploadTest.setUp(self)
        # Note that SYSNO fields are repeated but with different
        # subfields, this is to test whether bibupload would not
        # mistakenly pick up wrong values.
        self.xm_testrec1 = """
        <record>
         <controlfield tag="001">123456789</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1</subfield>
         </datafield>
         <datafield tag="%(sysnotag)s" ind1="%(sysnoind1)s" ind2="%(sysnoind2)s">
          <subfield code="%(sysnosubfieldcode)s">sysno1</subfield>
         </datafield>
         <datafield tag="%(sysnotag)s" ind1="%(sysnoind1)s" ind2="%(sysnoind2)s">
          <subfield code="0">sysno2</subfield>
         </datafield>
        </record>
        """ % {'sysnotag': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][0:3],
               'sysnoind1': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4] or " ",
               'sysnoind2': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5] or " ",
               'sysnosubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][5:6],
               }
        self.hm_testrec1 = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 1
        %(sysnotag)s%(sysnoind1)s%(sysnoind2)s $$%(sysnosubfieldcode)ssysno1
        %(sysnotag)s%(sysnoind1)s%(sysnoind2)s $$0sysno2
        """ % {'sysnotag': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][0:3],
               'sysnoind1': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4],
               'sysnoind2': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5],
               'sysnosubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][5:6],
               }
        self.xm_testrec1_to_update = """
        <record>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1 Updated</subfield>
         </datafield>
         <datafield tag="%(sysnotag)s" ind1="%(sysnoind1)s" ind2="%(sysnoind2)s">
          <subfield code="%(sysnosubfieldcode)s">sysno1</subfield>
         </datafield>
         <datafield tag="%(sysnotag)s" ind1="%(sysnoind1)s" ind2="%(sysnoind2)s">
          <subfield code="0">sysno2</subfield>
         </datafield>
        </record>
        """ % {'sysnotag': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][0:3],
               'sysnoind1': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4] or " ",
               'sysnoind2': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5] or " ",
               'sysnosubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][5:6],
               }
        self.xm_testrec1_updated = """
        <record>
         <controlfield tag="001">123456789</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1 Updated</subfield>
         </datafield>
         <datafield tag="%(sysnotag)s" ind1="%(sysnoind1)s" ind2="%(sysnoind2)s">
          <subfield code="%(sysnosubfieldcode)s">sysno1</subfield>
         </datafield>
         <datafield tag="%(sysnotag)s" ind1="%(sysnoind1)s" ind2="%(sysnoind2)s">
          <subfield code="0">sysno2</subfield>
         </datafield>
        </record>
        """ % {'sysnotag': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][0:3],
               'sysnoind1': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4] or " ",
               'sysnoind2': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5] or " ",
               'sysnosubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][5:6],
               }
        self.hm_testrec1_updated = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 1 Updated
        %(sysnotag)s%(sysnoind1)s%(sysnoind2)s $$%(sysnosubfieldcode)ssysno1
        %(sysnotag)s%(sysnoind1)s%(sysnoind2)s $$0sysno2
        """ % {'sysnotag': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][0:3],
               'sysnoind1': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4],
               'sysnoind2': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5],
               'sysnosubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][5:6],
               }
        self.xm_testrec2 = """
        <record>
         <controlfield tag="001">987654321</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 2</subfield>
         </datafield>
         <datafield tag="%(sysnotag)s" ind1="%(sysnoind1)s" ind2="%(sysnoind2)s">
          <subfield code="%(sysnosubfieldcode)s">sysno2</subfield>
         </datafield>
         <datafield tag="%(sysnotag)s" ind1="%(sysnoind1)s" ind2="%(sysnoind2)s">
          <subfield code="0">sysno1</subfield>
         </datafield>
        </record>
        """ % {'sysnotag': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][0:3],
               'sysnoind1': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4] or " ",
               'sysnoind2': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5] or " ",
               'sysnosubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][5:6],
               }
        self.hm_testrec2 = """
        001__ 987654321
        003__ SzGeCERN
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 2
        %(sysnotag)s%(sysnoind1)s%(sysnoind2)s $$%(sysnosubfieldcode)ssysno2
        %(sysnotag)s%(sysnoind1)s%(sysnoind2)s $$0sysno1
        """ % {'sysnotag': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][0:3],
               'sysnoind1': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][3:4],
               'sysnoind2': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][4:5],
               'sysnosubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_SYSNO_TAG'][5:6],
               }

    def test_insert_the_same_sysno_record(self):
        """bibupload - SYSNO tag, refuse to insert the same SYSNO record"""
        # initialize bibupload mode:
        if self.verbose:
            print "test_insert_the_same_sysno_record() started"
        # insert record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr1, recid1, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')
        # insert record 2 first time:
        testrec_to_insert_first = self.xm_testrec2.replace('<controlfield tag="001">987654321</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr2, recid2, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid2)
        inserted_xm = print_record(recid2, 'xm')
        inserted_hm = print_record(recid2, 'hm')
        # use real recID when comparing whether it worked:
        self.xm_testrec2 =  self.xm_testrec2.replace('987654321', str(recid2))
        self.hm_testrec2 =  self.hm_testrec2.replace('987654321', str(recid2))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec2), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec2), '')
        # try to insert updated record 1, it should fail:
        recs = bibupload.xml_marc_to_records(self.xm_testrec1_to_update)
        dummyerr1_updated, recid1_updated, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.assertEqual(-1, recid1_updated)
        if self.verbose:
            print "test_insert_the_same_sysno_record() finished"

    def test_insert_or_replace_the_same_sysno_record(self):
        """bibupload - SYSNO tag, allow to insert or replace the same SYSNO record"""
        # initialize bibupload mode:
        if self.verbose:
            print "test_insert_or_replace_the_same_sysno_record() started"
        # insert/replace record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr1, recid1, _ = bibupload.bibupload_records(recs, opt_mode='replace_or_insert')[0]
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          self.hm_testrec1), '')
        # try to insert/replace updated record 1, it should be okay:
        recs = bibupload.xml_marc_to_records(self.xm_testrec1_to_update)
        dummyerr1_updated, recid1_updated, _ = bibupload.bibupload_records(recs,
            opt_mode='replace_or_insert')[0]
        self.check_record_consistency(recid1_updated)
        inserted_xm = print_record(recid1_updated, 'xm')
        inserted_hm = print_record(recid1_updated, 'hm')
        self.assertEqual(recid1, recid1_updated)
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1_updated =  self.xm_testrec1_updated.replace('123456789', str(recid1))
        self.hm_testrec1_updated =  self.hm_testrec1_updated.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          self.xm_testrec1_updated), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          self.hm_testrec1_updated), '')
        if self.verbose:
            print "test_insert_or_replace_the_same_sysno_record() finished"

    def test_replace_nonexisting_sysno_record(self):
        """bibupload - SYSNO tag, refuse to replace non-existing SYSNO record"""
        # initialize bibupload mode:
        if self.verbose:
            print "test_replace_nonexisting_sysno_record() started"
        # insert record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummy, recid1, _ = bibupload.bibupload_records(recs, opt_mode='replace_or_insert')[0]
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')
        # try to replace record 2 it should fail:
        testrec_to_insert_first = self.xm_testrec2.replace('<controlfield tag="001">987654321</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummy, recid2, _ = bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.assertEqual(-1, recid2)
        if self.verbose:
            print "test_replace_nonexisting_sysno_record() finished"

class BibUploadRecordsWithEXTOAIIDTest(GenericBibUploadTest):
    """Testing uploading of records that have external EXTOAIID present."""

    def setUp(self):
        # pylint: disable=C0103
        """Initialize the MARCXML test records."""
        GenericBibUploadTest.setUp(self)
        # Note that EXTOAIID fields are repeated but with different
        # subfields, this is to test whether bibupload would not
        # mistakenly pick up wrong values.
        self.xm_testrec1 = """
        <record>
         <controlfield tag="001">123456789</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(extoaiidtag)s" ind1="%(extoaiidind1)s" ind2="%(extoaiidind2)s">
          <subfield code="%(extoaiidsubfieldcode)s">extoaiid1</subfield>
          <subfield code="%(extoaisrcsubfieldcode)s">extoaisrc1</subfield>
         </datafield>
         <datafield tag="%(extoaiidtag)s" ind1="%(extoaiidind1)s" ind2="%(extoaiidind2)s">
          <subfield code="0">extoaiid2</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1</subfield>
         </datafield>
        </record>
        """ % {'extoaiidtag': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][0:3],
               'extoaiidind1': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4] or " ",
               'extoaiidind2': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5] or " ",
               'extoaiidsubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][5:6],
               'extoaisrcsubfieldcode' : cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_PROVENANCE_TAG'][5:6],
               }
        self.hm_testrec1 = """
        001__ 123456789
        003__ SzGeCERN
        %(extoaiidtag)s%(extoaiidind1)s%(extoaiidind2)s $$%(extoaisrcsubfieldcode)sextoaisrc1$$%(extoaiidsubfieldcode)sextoaiid1
        %(extoaiidtag)s%(extoaiidind1)s%(extoaiidind2)s $$0extoaiid2
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 1
        """ % {'extoaiidtag': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][0:3],
               'extoaiidind1': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4],
               'extoaiidind2': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5],
               'extoaiidsubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][5:6],
               'extoaisrcsubfieldcode' : cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_PROVENANCE_TAG'][5:6],
               }
        self.xm_testrec1_to_update = """
        <record>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(extoaiidtag)s" ind1="%(extoaiidind1)s" ind2="%(extoaiidind2)s">
          <subfield code="%(extoaiidsubfieldcode)s">extoaiid1</subfield>
          <subfield code="%(extoaisrcsubfieldcode)s">extoaisrc1</subfield>
         </datafield>
         <datafield tag="%(extoaiidtag)s" ind1="%(extoaiidind1)s" ind2="%(extoaiidind2)s">
          <subfield code="0">extoaiid2</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1 Updated</subfield>
         </datafield>
        </record>
        """ % {'extoaiidtag': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][0:3],
               'extoaiidind1': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4] or " ",
               'extoaiidind2': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5] or " ",
               'extoaiidsubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][5:6],
               'extoaisrcsubfieldcode' : cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_PROVENANCE_TAG'][5:6],
               }
        self.xm_testrec1_updated = """
        <record>
         <controlfield tag="001">123456789</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(extoaiidtag)s" ind1="%(extoaiidind1)s" ind2="%(extoaiidind2)s">
          <subfield code="%(extoaiidsubfieldcode)s">extoaiid1</subfield>
          <subfield code="%(extoaisrcsubfieldcode)s">extoaisrc1</subfield>
         </datafield>
         <datafield tag="%(extoaiidtag)s" ind1="%(extoaiidind1)s" ind2="%(extoaiidind2)s">
          <subfield code="0">extoaiid2</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1 Updated</subfield>
         </datafield>
        </record>
        """ % {'extoaiidtag': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][0:3],
               'extoaiidind1': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4] or " ",
               'extoaiidind2': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5] or " ",
               'extoaiidsubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][5:6],
               'extoaisrcsubfieldcode' : cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_PROVENANCE_TAG'][5:6],
               }
        self.hm_testrec1_updated = """
        001__ 123456789
        003__ SzGeCERN
        %(extoaiidtag)s%(extoaiidind1)s%(extoaiidind2)s $$%(extoaisrcsubfieldcode)sextoaisrc1$$%(extoaiidsubfieldcode)sextoaiid1
        %(extoaiidtag)s%(extoaiidind1)s%(extoaiidind2)s $$0extoaiid2
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 1 Updated
        """ % {'extoaiidtag': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][0:3],
               'extoaiidind1': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4],
               'extoaiidind2': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5],
               'extoaiidsubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][5:6],
               'extoaisrcsubfieldcode' : cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_PROVENANCE_TAG'][5:6],
               }
        self.xm_testrec2 = """
        <record>
         <controlfield tag="001">987654321</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(extoaiidtag)s" ind1="%(extoaiidind1)s" ind2="%(extoaiidind2)s">
          <subfield code="%(extoaiidsubfieldcode)s">extoaiid2</subfield>
          <subfield code="%(extoaisrcsubfieldcode)s">extoaisrc1</subfield>
         </datafield>
         <datafield tag="%(extoaiidtag)s" ind1="%(extoaiidind1)s" ind2="%(extoaiidind2)s">
          <subfield code="0">extoaiid1</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 2</subfield>
         </datafield>
        </record>
        """ % {'extoaiidtag': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][0:3],
               'extoaiidind1': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4] or " ",
               'extoaiidind2': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5] or " ",
               'extoaiidsubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][5:6],
               'extoaisrcsubfieldcode' : cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_PROVENANCE_TAG'][5:6],
               }
        self.hm_testrec2 = """
        001__ 987654321
        003__ SzGeCERN
        %(extoaiidtag)s%(extoaiidind1)s%(extoaiidind2)s $$%(extoaisrcsubfieldcode)sextoaisrc1$$%(extoaiidsubfieldcode)sextoaiid2
        %(extoaiidtag)s%(extoaiidind1)s%(extoaiidind2)s $$0extoaiid1
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 2
        """ % {'extoaiidtag': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][0:3],
               'extoaiidind1': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4],
               'extoaiidind2': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5],
               'extoaiidsubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][5:6],
               'extoaisrcsubfieldcode' : cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_PROVENANCE_TAG'][5:6],
               }

    def test_insert_the_same_extoaiid_record(self):
        """bibupload - EXTOAIID tag, refuse to insert the same EXTOAIID record"""
        # initialize bibupload mode:
        if self.verbose:
            print "test_insert_the_same_extoaiid_record() started"
        # insert record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr1, recid1, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')
        # insert record 2 first time:
        testrec_to_insert_first = self.xm_testrec2.replace('<controlfield tag="001">987654321</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr2, recid2, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid2)
        inserted_xm = print_record(recid2, 'xm')
        inserted_hm = print_record(recid2, 'hm')
        # use real recID when comparing whether it worked:
        self.xm_testrec2 =  self.xm_testrec2.replace('987654321', str(recid2))
        self.hm_testrec2 =  self.hm_testrec2.replace('987654321', str(recid2))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec2), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec2), '')
        # try to insert updated record 1, it should fail:
        recs = bibupload.xml_marc_to_records(self.xm_testrec1_to_update)
        dummyerr1_updated, recid1_updated, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.assertEqual(-1, recid1_updated)
        if self.verbose:
            print "test_insert_the_same_extoaiid_record() finished"

    def test_insert_or_replace_the_same_extoaiid_record(self):
        """bibupload - EXTOAIID tag, allow to insert or replace the same EXTOAIID record"""
        # initialize bibupload mode:
        if self.verbose:
            print "test_insert_or_replace_the_same_extoaiid_record() started"
        # insert/replace record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr1, recid1, _ = bibupload.bibupload_records(recs, opt_mode='replace_or_insert')[0]
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          self.hm_testrec1), '')
        # try to insert/replace updated record 1, it should be okay:
        recs = bibupload.xml_marc_to_records(self.xm_testrec1_to_update)
        dummyerr1_updated, recid1_updated, _ = bibupload.bibupload_records(recs, opt_mode='replace_or_insert')[0]
        self.check_record_consistency(recid1_updated)
        inserted_xm = print_record(recid1_updated, 'xm')
        inserted_hm = print_record(recid1_updated, 'hm')
        self.assertEqual(recid1, recid1_updated)
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1_updated =  self.xm_testrec1_updated.replace('123456789', str(recid1))
        self.hm_testrec1_updated =  self.hm_testrec1_updated.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          self.xm_testrec1_updated), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          self.hm_testrec1_updated), '')
        if self.verbose:
            print "test_insert_or_replace_the_same_extoaiid_record() finished"

    def test_replace_nonexisting_extoaiid_record(self):
        """bibupload - EXTOAIID tag, refuse to replace non-existing EXTOAIID record"""
        # initialize bibupload mode:
        if self.verbose:
            print "test_replace_nonexisting_extoaiid_record() started"
        # insert record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr1, recid1, _ = bibupload.bibupload_records(recs, opt_mode='replace_or_insert')[0]
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')
        # try to replace record 2 it should fail:
        testrec_to_insert_first = self.xm_testrec2.replace('<controlfield tag="001">987654321</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr2, recid2, _ = bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.assertEqual(-1, recid2)
        if self.verbose:
            print "test_replace_nonexisting_extoaiid_record() finished"

class BibUploadRecordsWithOAIIDTest(GenericBibUploadTest):
    """Testing uploading of records that have OAI ID present."""

    def setUp(self):
        """Initialize the MARCXML test records."""
        GenericBibUploadTest.setUp(self)
        # Note that OAI fields are repeated but with different
        # subfields, this is to test whether bibupload would not
        # mistakenly pick up wrong values.
        self.xm_testrec1 = """
        <record>
         <controlfield tag="001">123456789</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1</subfield>
         </datafield>
         <datafield tag="%(oaitag)s" ind1="%(oaiind1)s" ind2="%(oaiind2)s">
          <subfield code="%(oaisubfieldcode)s">oai:foo:1</subfield>
         </datafield>
         <datafield tag="%(oaitag)s" ind1="%(oaiind1)s" ind2="%(oaiind2)s">
          <subfield code="0">oai:foo:2</subfield>
         </datafield>
        </record>
        """ % {'oaitag': cfg['CFG_OAI_ID_FIELD'][0:3],
               'oaiind1': cfg['CFG_OAI_ID_FIELD'][3:4] != "_" and \
                          cfg['CFG_OAI_ID_FIELD'][3:4] or " ",
               'oaiind2': cfg['CFG_OAI_ID_FIELD'][4:5] != "_" and \
                          cfg['CFG_OAI_ID_FIELD'][4:5] or " ",
               'oaisubfieldcode': cfg['CFG_OAI_ID_FIELD'][5:6],
               }
        self.hm_testrec1 = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 1
        %(oaitag)s%(oaiind1)s%(oaiind2)s $$%(oaisubfieldcode)soai:foo:1
        %(oaitag)s%(oaiind1)s%(oaiind2)s $$0oai:foo:2
        """ % {'oaitag': cfg['CFG_OAI_ID_FIELD'][0:3],
               'oaiind1': cfg['CFG_OAI_ID_FIELD'][3:4],
               'oaiind2': cfg['CFG_OAI_ID_FIELD'][4:5],
               'oaisubfieldcode': cfg['CFG_OAI_ID_FIELD'][5:6],
               }
        self.xm_testrec1_to_update = """
        <record>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1 Updated</subfield>
         </datafield>
         <datafield tag="%(oaitag)s" ind1="%(oaiind1)s" ind2="%(oaiind2)s">
          <subfield code="%(oaisubfieldcode)s">oai:foo:1</subfield>
         </datafield>
         <datafield tag="%(oaitag)s" ind1="%(oaiind1)s" ind2="%(oaiind2)s">
          <subfield code="0">oai:foo:2</subfield>
         </datafield>
        </record>
        """ % {'oaitag': cfg['CFG_OAI_ID_FIELD'][0:3],
               'oaiind1': cfg['CFG_OAI_ID_FIELD'][3:4] != "_" and \
                          cfg['CFG_OAI_ID_FIELD'][3:4] or " ",
               'oaiind2': cfg['CFG_OAI_ID_FIELD'][4:5] != "_" and \
                          cfg['CFG_OAI_ID_FIELD'][4:5] or " ",
               'oaisubfieldcode': cfg['CFG_OAI_ID_FIELD'][5:6],
               }
        self.xm_testrec1_updated = """
        <record>
         <controlfield tag="001">123456789</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1 Updated</subfield>
         </datafield>
         <datafield tag="%(oaitag)s" ind1="%(oaiind1)s" ind2="%(oaiind2)s">
          <subfield code="%(oaisubfieldcode)s">oai:foo:1</subfield>
         </datafield>
         <datafield tag="%(oaitag)s" ind1="%(oaiind1)s" ind2="%(oaiind2)s">
          <subfield code="0">oai:foo:2</subfield>
         </datafield>
        </record>
        """ % {'oaitag': cfg['CFG_OAI_ID_FIELD'][0:3],
               'oaiind1': cfg['CFG_OAI_ID_FIELD'][3:4] != "_" and \
                          cfg['CFG_OAI_ID_FIELD'][3:4] or " ",
               'oaiind2': cfg['CFG_OAI_ID_FIELD'][4:5] != "_" and \
                          cfg['CFG_OAI_ID_FIELD'][4:5] or " ",
               'oaisubfieldcode': cfg['CFG_OAI_ID_FIELD'][5:6],
               }
        self.hm_testrec1_updated = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 1 Updated
        %(oaitag)s%(oaiind1)s%(oaiind2)s $$%(oaisubfieldcode)soai:foo:1
        %(oaitag)s%(oaiind1)s%(oaiind2)s $$0oai:foo:2
        """ % {'oaitag': cfg['CFG_OAI_ID_FIELD'][0:3],
               'oaiind1': cfg['CFG_OAI_ID_FIELD'][3:4],
               'oaiind2': cfg['CFG_OAI_ID_FIELD'][4:5],
               'oaisubfieldcode': cfg['CFG_OAI_ID_FIELD'][5:6],
               }
        self.xm_testrec2 = """
        <record>
         <controlfield tag="001">987654321</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 2</subfield>
         </datafield>
         <datafield tag="%(oaitag)s" ind1="%(oaiind1)s" ind2="%(oaiind2)s">
          <subfield code="%(oaisubfieldcode)s">oai:foo:2</subfield>
         </datafield>
         <datafield tag="%(oaitag)s" ind1="%(oaiind1)s" ind2="%(oaiind2)s">
          <subfield code="0">oai:foo:1</subfield>
         </datafield>
        </record>
        """ % {'oaitag': cfg['CFG_OAI_ID_FIELD'][0:3],
               'oaiind1': cfg['CFG_OAI_ID_FIELD'][3:4] != "_" and \
                          cfg['CFG_OAI_ID_FIELD'][3:4] or " ",
               'oaiind2': cfg['CFG_OAI_ID_FIELD'][4:5] != "_" and \
                          cfg['CFG_OAI_ID_FIELD'][4:5] or " ",
               'oaisubfieldcode': cfg['CFG_OAI_ID_FIELD'][5:6],
               }
        self.hm_testrec2 = """
        001__ 987654321
        003__ SzGeCERN
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 2
        %(oaitag)s%(oaiind1)s%(oaiind2)s $$%(oaisubfieldcode)soai:foo:2
        %(oaitag)s%(oaiind1)s%(oaiind2)s $$0oai:foo:1
        """ % {'oaitag': cfg['CFG_OAI_ID_FIELD'][0:3],
               'oaiind1': cfg['CFG_OAI_ID_FIELD'][3:4],
               'oaiind2': cfg['CFG_OAI_ID_FIELD'][4:5],
               'oaisubfieldcode': cfg['CFG_OAI_ID_FIELD'][5:6],
               }

    def test_insert_the_same_oai_record(self):
        """bibupload - OAIID tag, refuse to insert the same OAI record"""
        # insert record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr1, recid1, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')
        # insert record 2 first time:
        testrec_to_insert_first = self.xm_testrec2.replace('<controlfield tag="001">987654321</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr2, recid2, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid2)
        inserted_xm = print_record(recid2, 'xm')
        inserted_hm = print_record(recid2, 'hm')
        # use real recID when comparing whether it worked:
        self.xm_testrec2 =  self.xm_testrec2.replace('987654321', str(recid2))
        self.hm_testrec2 =  self.hm_testrec2.replace('987654321', str(recid2))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec2), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec2), '')
        # try to insert updated record 1, it should fail:
        recs = bibupload.xml_marc_to_records(self.xm_testrec1_to_update)
        dummyerr1_updated, recid1_updated, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.assertEqual(-1, recid1_updated)

    def test_insert_or_replace_the_same_oai_record(self):
        """bibupload - OAIID tag, allow to insert or replace the same OAI record"""
        # initialize bibupload mode:
        # insert/replace record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr1, recid1, _ = bibupload.bibupload_records(recs, opt_mode='replace_or_insert')[0]
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')
        # try to insert/replace updated record 1, it should be okay:
        recs = bibupload.xml_marc_to_records(self.xm_testrec1_to_update)
        dummyerr1_updated, recid1_updated, _ = bibupload.bibupload_records(recs, opt_mode='replace_or_insert')[0]
        self.check_record_consistency(recid1_updated)
        inserted_xm = print_record(recid1_updated, 'xm')
        inserted_hm = print_record(recid1_updated, 'hm')
        self.assertEqual(recid1, recid1_updated)
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1_updated =  self.xm_testrec1_updated.replace('123456789', str(recid1))
        self.hm_testrec1_updated =  self.hm_testrec1_updated.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          self.xm_testrec1_updated), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          self.hm_testrec1_updated), '')

    def test_replace_nonexisting_oai_record(self):
        """bibupload - OAIID tag, refuse to replace non-existing OAI record"""
        # insert record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr1, recid1, _ = bibupload.bibupload_records(recs, opt_mode='replace_or_insert')[0]
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')
        # try to replace record 2 it should fail:
        testrec_to_insert_first = self.xm_testrec2.replace('<controlfield tag="001">987654321</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        dummyerr2, recid2, _ = bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.assertEqual(-1, recid2)

class BibUploadRecordsWithDOITest(GenericBibUploadTest):
    """Testing uploading of records with DOI."""

    def setUp(self):
        """Initialize the MARCXML test records."""
        GenericBibUploadTest.setUp(self)
        self.xm_testrec1 = """
        <record>
         <controlfield tag="001">123456789</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">doi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/123-456-789</subfield>
         </datafield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">nondoi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/123-456-789-0</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1</subfield>
         </datafield>
        </record>
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': ' ',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.hm_testrec1 = """
        001__ 123456789
        003__ SzGeCERN
        %(doitag)s%(doiind1)s%(doiind2)s $$%(doisubfieldcodesource)sdoi$$%(doisubfieldcodevalue)s10.5170/123-456-789
        %(doitag)s%(doiind1)s%(doiind2)s $$%(doisubfieldcodesource)snondoi$$%(doisubfieldcodevalue)s10.5170/123-456-789-0
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 1
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': '_',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.xm_testrec1_to_update = """
        <record>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">doi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/123-456-789</subfield>
         </datafield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">nondoi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/123-456-789-0</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1 Updated</subfield>
         </datafield>
        </record>
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': ' ',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.xm_testrec1_updated = """
        <record>
         <controlfield tag="001">123456789</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">doi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/123-456-789</subfield>
         </datafield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">nondoi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/123-456-789-0</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 1 Updated</subfield>
         </datafield>
        </record>
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': ' ',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.hm_testrec1_updated = """
        001__ 123456789
        003__ SzGeCERN
        %(doitag)s%(doiind1)s%(doiind2)s $$%(doisubfieldcodesource)sdoi$$%(doisubfieldcodevalue)s10.5170/123-456-789
        %(doitag)s%(doiind1)s%(doiind2)s $$%(doisubfieldcodesource)snondoi$$%(doisubfieldcodevalue)s10.5170/123-456-789-0
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 1 Updated
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': '_',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.xm_testrec2 = """
        <record>
         <controlfield tag="001">987654321</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">doi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/987-654-321</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 2</subfield>
         </datafield>
        </record>
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': ' ',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.hm_testrec2 = """
        001__ 987654321
        003__ SzGeCERN
        %(doitag)s%(doiind1)s%(doiind2)s $$%(doisubfieldcodesource)sdoi$$%(doisubfieldcodevalue)s10.5170/987-654-321
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 2
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': '_',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.xm_testrec2_to_update = """
        <record>
         <controlfield tag="001">987654321</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">doi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/123-456-789</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
        </record>
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': ' ',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.xm_testrec3 = """
        <record>
         <controlfield tag="001">192837645</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">doi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/123-456-789-0</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 4</subfield>
         </datafield>
        </record>
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': ' ',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.hm_testrec3 = """
        001__ 192837645
        003__ SzGeCERN
        %(doitag)s%(doiind1)s%(doiind2)s $$%(doisubfieldcodesource)sdoi$$%(doisubfieldcodevalue)s10.5170/123-456-789-0
        100__ $$aBar, Baz$$uFoo
        245__ $$aOn the quux and huux 4
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': '_',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.xm_testrec4 = """
        <record>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">doi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/123-456-789-non-existing</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 5</subfield>
         </datafield>
        </record>
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': ' ',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }
        self.xm_testrec5 = """
        <record>
         <controlfield tag="001">123456789</controlfield>
         <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">doi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/123-456-789</subfield>
         </datafield>
         <datafield tag="%(doitag)s" ind1="%(doiind1)s" ind2="%(doiind2)s">
          <subfield code="%(doisubfieldcodesource)s">doi</subfield>
          <subfield code="%(doisubfieldcodevalue)s">10.5170/987-654-321</subfield>
         </datafield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Bar, Baz</subfield>
          <subfield code="u">Foo</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">On the quux and huux 6</subfield>
         </datafield>
        </record>
        """ % {'doitag': '024',
               'doiind1': '7',
               'doiind2': ' ',
               'doisubfieldcodevalue': 'a',
               'doisubfieldcodesource': '2'
               }

    def test_insert_the_same_doi_matching_on_doi(self):
        """bibupload - DOI tag, refuse to "insert" twice same DOI (matching on DOI)"""
        # insert record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err1, recid1, msg1 = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')
        # insert record 2 first time:
        testrec_to_insert_first = self.xm_testrec2.replace('<controlfield tag="001">987654321</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err2, recid2, msg2 = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid2)
        inserted_xm = print_record(recid2, 'xm')
        inserted_hm = print_record(recid2, 'hm')
        # use real recID when comparing whether it worked:
        self.xm_testrec2 = self.xm_testrec2.replace('987654321', str(recid2))
        self.hm_testrec2 = self.hm_testrec2.replace('987654321', str(recid2))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec2), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec2), '')

        # try to insert again record 1 (without recid, matching on DOI)
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err1_updated, recid1_updated, msg1_updated = bibupload.bibupload(recs[0], opt_mode='insert')
        self.assertEqual(-1, recid1_updated)

        # if we try to update, append or correct, the same record is matched
        recs = bibupload.xml_marc_to_records(self.xm_testrec1_to_update)
        err1_updated, recid1_updated, msg1_updated = bibupload.bibupload(recs[0], opt_mode='correct')
        self.check_record_consistency(recid1_updated)
        self.assertEqual(recid1, recid1_updated)

        err1_updated, recid1_updated, msg1_updated = bibupload.bibupload(recs[0], opt_mode='append')
        self.check_record_consistency(recid1_updated)
        self.assertEqual(recid1, recid1_updated)

        err1_updated, recid1_updated, msg1_updated = bibupload.bibupload(recs[0], opt_mode='replace')
        self.check_record_consistency(recid1_updated)
        self.assertEqual(recid1, recid1_updated)

    def test_insert_the_same_doi_matching_on_recid(self):
        """bibupload - DOI tag, refuse to "insert" twice same DOI (matching on recid)"""
        # First upload 2 test records
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err1, recid1, msg1 = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid1)

        testrec_to_insert_first = self.xm_testrec2.replace('<controlfield tag="001">987654321</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err2, recid2, msg2 = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid2)

        # try to update record 2 with DOI already in record 1. It must fail:
        testrec_to_update = self.xm_testrec2_to_update.replace('<controlfield tag="001">987654321</controlfield>',
                                                               '<controlfield tag="001">%s</controlfield>' % recid2)
        recs = bibupload.xml_marc_to_records(testrec_to_update)
        err, recid, msg = bibupload.bibupload(recs[0], opt_mode='replace')
        self.check_record_consistency(recid)
        self.assertEqual(1, err)

        # Ditto in correct and append mode
        recs = bibupload.xml_marc_to_records(testrec_to_update)
        err, recid, msg = bibupload.bibupload(recs[0], opt_mode='correct')
        self.check_record_consistency(recid)
        self.assertEqual(1, err)

        recs = bibupload.xml_marc_to_records(testrec_to_update)
        err, recid, msg = bibupload.bibupload(recs[0], opt_mode='append')
        self.check_record_consistency(recid)
        self.assertEqual(1, err)

    def test_insert_or_replace_the_same_doi_record(self):
        """bibupload - DOI tag, allow to insert or replace matching on DOI"""
        # insert/replace record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err1, recid1, msg1 = bibupload.bibupload(recs[0], opt_mode='replace_or_insert')
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1 = self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 = self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')
        # try to insert/replace updated record 1, it should be okay:
        recs = bibupload.xml_marc_to_records(self.xm_testrec1_to_update)
        err1_updated, recid1_updated, msg1_updated = bibupload.bibupload(recs[0], opt_mode='replace_or_insert')
        self.check_record_consistency(recid1_updated)
        inserted_xm = print_record(recid1_updated, 'xm')
        inserted_hm = print_record(recid1_updated, 'hm')
        self.assertEqual(recid1, recid1_updated)
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1_updated = self.xm_testrec1_updated.replace('123456789', str(recid1))
        self.hm_testrec1_updated = self.hm_testrec1_updated.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          self.xm_testrec1_updated), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          self.hm_testrec1_updated), '')

    def test_correct_the_same_doi_record(self):
        """bibupload - DOI tag, allow to correct matching on DOI"""
        # insert/replace record 1 first time:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err1, recid1, msg1 = bibupload.bibupload(recs[0], opt_mode='replace_or_insert')
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1 =  self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 =  self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')
        # try to correct updated record 1, it should be okay:
        recs = bibupload.xml_marc_to_records(self.xm_testrec1_to_update)
        err1_updated, recid1_updated, msg1_updated = bibupload.bibupload(recs[0], opt_mode='correct')
        self.check_record_consistency(recid1_updated)
        inserted_xm = print_record(recid1_updated, 'xm')
        inserted_hm = print_record(recid1_updated, 'hm')
        self.assertEqual(recid1, recid1_updated)
        # use real recID in test buffers when comparing whether it worked:
        self.xm_testrec1_updated = self.xm_testrec1_updated.replace('123456789', str(recid1))
        self.hm_testrec1_updated = self.hm_testrec1_updated.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          self.xm_testrec1_updated), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          self.hm_testrec1_updated), '')

    def test_replace_nonexisting_doi_record(self):
        """bibupload - DOI tag, refuse to replace non-existing DOI record (matching on DOI)"""
        testrec_to_insert_first = self.xm_testrec4
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err4, recid4, msg4 = bibupload.bibupload(recs[0], opt_mode='replace')
        self.assertEqual(-1, recid4)

    def test_matching_on_doi_source_field(self):
        """bibupload - DOI tag, test matching records using DOI value AND source field ($2)"""
        # insert test record 1, with a "fake" doi (not "doi" in source field):
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err1, recid1, msg1 = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid1)
        inserted_xm = print_record(recid1, 'xm')
        inserted_hm = print_record(recid1, 'hm')
        # use real recID when comparing whether it worked:
        self.xm_testrec1 = self.xm_testrec1.replace('123456789', str(recid1))
        self.hm_testrec1 = self.hm_testrec1.replace('123456789', str(recid1))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec1), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec1), '')

        # insert record 3, which matches record 1 "fake" doi, so it
        # should work.
        testrec_to_insert_first = self.xm_testrec3.replace('<controlfield tag="001">192837645</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err3, recid3, msg3 = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid3)
        inserted_xm = print_record(recid3, 'xm')
        inserted_hm = print_record(recid3, 'hm')
        # use real recID when comparing whether it worked:
        self.xm_testrec3 = self.xm_testrec3.replace('192837645', str(recid3))
        self.hm_testrec3 = self.hm_testrec3.replace('192837645', str(recid3))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                           self.xm_testrec3), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                           self.hm_testrec3), '')

    def test_replace_or_update_record__with_ambiguous_doi(self):
        """bibupload - DOI tag, refuse to replace/correct/append on the basis of ambiguous DOI"""
        # First upload 2 test records with two different DOIs:
        testrec_to_insert_first = self.xm_testrec1.replace('<controlfield tag="001">123456789</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err1, recid1, msg1 = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid1)
        self.assertEqual(0, err1)

        testrec_to_insert_first = self.xm_testrec2.replace('<controlfield tag="001">987654321</controlfield>',
                                                           '')
        recs = bibupload.xml_marc_to_records(testrec_to_insert_first)
        err2, recid2, msg2 = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid2)
        self.assertEqual(0, err2)

        # Now try to insert record with DOIs matching the records
        # previously uploaded.  It must fail.
        testrec = self.xm_testrec5.replace('<controlfield tag="001">123456789</controlfield>',
                                           '')
        recs = bibupload.xml_marc_to_records(testrec)
        err5, recid5, msg5 = bibupload.bibupload(recs[0], opt_mode='insert')
        self.assertEqual(1, err5)

        # Ditto for other modes:
        recs = bibupload.xml_marc_to_records(testrec)
        err5, recid5, msg5 = bibupload.bibupload(recs[0], opt_mode='replace_or_insert')
        self.assertEqual(1, err5)

        recs = bibupload.xml_marc_to_records(testrec)
        err5, recid5, msg5 = bibupload.bibupload(recs[0], opt_mode='replace')
        self.assertEqual(1, err5)

        recs = bibupload.xml_marc_to_records(testrec)
        err5, recid5, msg5 = bibupload.bibupload(recs[0], opt_mode='correct')
        self.assertEqual(1, err5)

        recs = bibupload.xml_marc_to_records(testrec)
        err5, recid5, msg5 = bibupload.bibupload(recs[0], opt_mode='append')
        self.assertEqual(1, err5)

        # The same is true if a recid exists in the input MARCXML (as
        # long as DOIs are ambiguous):
        testrec = self.xm_testrec5.replace('<controlfield tag="001">123456789</controlfield>',
                                           '<controlfield tag="001">%s</controlfield>' % recid1)

        recs = bibupload.xml_marc_to_records(testrec)
        err5, recid5, msg5 = bibupload.bibupload(recs[0], opt_mode='replace_or_insert')
        self.assertEqual(1, err5)

        recs = bibupload.xml_marc_to_records(testrec)
        err5, recid5, msg5 = bibupload.bibupload(recs[0], opt_mode='replace')
        self.assertEqual(1, err5)

        recs = bibupload.xml_marc_to_records(testrec)
        err5, recid5, msg5 = bibupload.bibupload(recs[0], opt_mode='correct')
        self.assertEqual(1, err5)

        recs = bibupload.xml_marc_to_records(testrec)
        err5, recid5, msg5 = bibupload.bibupload(recs[0], opt_mode='append')
        self.assertEqual(1, err5)

class BibUploadIndicatorsTest(GenericBibUploadTest):
    """
    Testing uploading of a MARCXML record with indicators having
    either blank space (as per MARC schema) or empty string value (old
    behaviour).
    """

    def setUp(self):
        """Initialize the MARCXML test record."""
        GenericBibUploadTest.setUp(self)
        self.testrec1_xm = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
        </record>
        """
        self.testrec1_hm = """
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        """
        self.testrec2_xm = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1="" ind2="">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
        </record>
        """
        self.testrec2_hm = """
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        """

    def test_record_with_spaces_in_indicators(self):
        """bibupload - inserting MARCXML with spaces in indicators"""
        recs = bibupload.xml_marc_to_records(self.testrec1_xm)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(remove_tag_001_from_xmbuffer(inserted_xm),
                                          self.testrec1_xm), '')
        self.assertEqual(compare_hmbuffers(remove_tag_001_from_hmbuffer(inserted_hm),
                                          self.testrec1_hm), '')

    def test_record_with_no_spaces_in_indicators(self):
        """bibupload - inserting MARCXML with no spaces in indicators"""
        recs = bibupload.xml_marc_to_records(self.testrec2_xm)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(remove_tag_001_from_xmbuffer(inserted_xm),
                                          self.testrec2_xm), '')
        self.assertEqual(compare_hmbuffers(remove_tag_001_from_hmbuffer(inserted_hm),
                                          self.testrec2_hm), '')

class BibUploadUpperLowerCaseTest(GenericBibUploadTest):
    """
    Testing treatment of similar records with only upper and lower
    case value differences in the bibxxx table.
    """

    def setUp(self):
        """Initialize the MARCXML test records."""
        GenericBibUploadTest.setUp(self)
        self.testrec1_xm = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
        </record>
        """
        self.testrec1_hm = """
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        """
        self.testrec2_xm = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1="" ind2="">
          <subfield code="a">TeSt, JoHn</subfield>
          <subfield code="u">Test UniVeRsity</subfield>
         </datafield>
        </record>
        """
        self.testrec2_hm = """
        003__ SzGeCERN
        100__ $$aTeSt, JoHn$$uTest UniVeRsity
        """

    def test_record_with_upper_lower_case_letters(self):
        """bibupload - inserting similar MARCXML records with upper/lower case"""
        # insert test record #1:
        recs = bibupload.xml_marc_to_records(self.testrec1_xm)
        dummyerr1, recid1, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid1)
        recid1_inserted_xm = print_record(recid1, 'xm')
        recid1_inserted_hm = print_record(recid1, 'hm')
        # insert test record #2:
        recs = bibupload.xml_marc_to_records(self.testrec2_xm)
        dummyerr1, recid2, _ = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid2)
        recid2_inserted_xm = print_record(recid2, 'xm')
        recid2_inserted_hm = print_record(recid2, 'hm')
        # let us compare stuff now:
        self.assertEqual(compare_xmbuffers(remove_tag_001_from_xmbuffer(recid1_inserted_xm),
                                          self.testrec1_xm), '')
        self.assertEqual(compare_hmbuffers(remove_tag_001_from_hmbuffer(recid1_inserted_hm),
                                          self.testrec1_hm), '')
        self.assertEqual(compare_xmbuffers(remove_tag_001_from_xmbuffer(recid2_inserted_xm),
                                          self.testrec2_xm), '')
        self.assertEqual(compare_hmbuffers(remove_tag_001_from_hmbuffer(recid2_inserted_hm),
                                          self.testrec2_hm), '')


class BibUploadControlledProvenanceTest(GenericBibUploadTest):
    """Testing treatment of tags under controlled provenance in the correct mode."""

    def setUp(self):
        """Initialize the MARCXML test record."""
        GenericBibUploadTest.setUp(self)
        self.testrec1_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">Test title</subfield>
         </datafield>
         <datafield tag="653" ind1="1" ind2=" ">
          <subfield code="a">blabla</subfield>
          <subfield code="9">sam</subfield>
         </datafield>
         <datafield tag="653" ind1="1" ind2=" ">
          <subfield code="a">blublu</subfield>
          <subfield code="9">sim</subfield>
         </datafield>
         <datafield tag="653" ind1="1" ind2=" ">
          <subfield code="a">human</subfield>
         </datafield>
        </record>
        """
        self.testrec1_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, Jane$$uTest Institute
        245__ $$aTest title
        6531_ $$9sam$$ablabla
        6531_ $$9sim$$ablublu
        6531_ $$ahuman
        """
        self.testrec1_xm_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="653" ind1="1" ind2=" ">
          <subfield code="a">bleble</subfield>
          <subfield code="9">sim</subfield>
         </datafield>
         <datafield tag="653" ind1="1" ind2=" ">
          <subfield code="a">bloblo</subfield>
          <subfield code="9">som</subfield>
         </datafield>
        </record>
        """
        self.testrec1_corrected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">Test title</subfield>
         </datafield>
         <datafield tag="653" ind1="1" ind2=" ">
          <subfield code="a">blabla</subfield>
          <subfield code="9">sam</subfield>
         </datafield>
         <datafield tag="653" ind1="1" ind2=" ">
          <subfield code="a">human</subfield>
         </datafield>
         <datafield tag="653" ind1="1" ind2=" ">
          <subfield code="a">bleble</subfield>
          <subfield code="9">sim</subfield>
         </datafield>
         <datafield tag="653" ind1="1" ind2=" ">
          <subfield code="a">bloblo</subfield>
          <subfield code="9">som</subfield>
         </datafield>
        </record>
        """
        self.testrec1_corrected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, Jane$$uTest Institute
        245__ $$aTest title
        6531_ $$9sam$$ablabla
        6531_ $$ahuman
        6531_ $$9sim$$ableble
        6531_ $$9som$$abloblo
        """
        # insert test record:
        test_record_xm = self.testrec1_xm.replace('<controlfield tag="001">123456789</controlfield>',
                                                  '')
        recs = bibupload.xml_marc_to_records(test_record_xm)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recID:
        self.testrec1_xm = self.testrec1_xm.replace('123456789', str(recid))
        self.testrec1_hm = self.testrec1_hm.replace('123456789', str(recid))
        self.testrec1_xm_to_correct = self.testrec1_xm_to_correct.replace('123456789', str(recid))
        self.testrec1_corrected_xm = self.testrec1_corrected_xm.replace('123456789', str(recid))
        self.testrec1_corrected_hm = self.testrec1_corrected_hm.replace('123456789', str(recid))
        # test of the inserted record:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm, self.testrec1_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm, self.testrec1_hm), '')

    def test_controlled_provenance_persistence(self):
        """bibupload - correct mode, tags with controlled provenance"""
        # correct metadata tags; will the protected tags be kept?
        recs = bibupload.xml_marc_to_records(self.testrec1_xm_to_correct)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='correct')[0]
        self.check_record_consistency(recid)
        corrected_xm = print_record(recid, 'xm')
        corrected_hm = print_record(recid, 'hm')
        # did it work?
        self.assertEqual(compare_xmbuffers(corrected_xm, self.testrec1_corrected_xm), '')
        self.assertEqual(compare_hmbuffers(corrected_hm, self.testrec1_corrected_hm), '')


class BibUploadStrongTagsTest(GenericBibUploadTest):
    """Testing treatment of strong tags and the replace mode."""

    def setUp(self):
        """Initialize the MARCXML test record."""
        GenericBibUploadTest.setUp(self)
        self.testrec1_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Jane</subfield>
          <subfield code="u">Test Institute</subfield>
         </datafield>
         <datafield tag="245" ind1=" " ind2=" ">
          <subfield code="a">Test title</subfield>
         </datafield>
         <datafield tag="%(strong_tag)s" ind1=" " ind2=" ">
          <subfield code="a">A value</subfield>
          <subfield code="b">Another value</subfield>
         </datafield>
        </record>
        """ % {'strong_tag': bibupload.CFG_BIBUPLOAD_STRONG_TAGS[0]}
        self.testrec1_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, Jane$$uTest Institute
        245__ $$aTest title
        %(strong_tag)s__ $$aA value$$bAnother value
        """ % {'strong_tag': bibupload.CFG_BIBUPLOAD_STRONG_TAGS[0]}
        self.testrec1_xm_to_replace = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Joseph</subfield>
          <subfield code="u">Test Academy</subfield>
         </datafield>
        </record>
        """
        self.testrec1_replaced_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, Joseph</subfield>
          <subfield code="u">Test Academy</subfield>
         </datafield>
         <datafield tag="%(strong_tag)s" ind1=" " ind2=" ">
          <subfield code="a">A value</subfield>
          <subfield code="b">Another value</subfield>
         </datafield>
        </record>
        """ % {'strong_tag': bibupload.CFG_BIBUPLOAD_STRONG_TAGS[0]}
        self.testrec1_replaced_hm = """
        001__ 123456789
        100__ $$aTest, Joseph$$uTest Academy
        %(strong_tag)s__ $$aA value$$bAnother value
        """ % {'strong_tag': bibupload.CFG_BIBUPLOAD_STRONG_TAGS[0]}
        # insert test record:
        test_record_xm = self.testrec1_xm.replace('<controlfield tag="001">123456789</controlfield>',
                                                  '')
        recs = bibupload.xml_marc_to_records(test_record_xm)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recID:
        self.testrec1_xm = self.testrec1_xm.replace('123456789', str(recid))
        self.testrec1_hm = self.testrec1_hm.replace('123456789', str(recid))
        self.testrec1_xm_to_replace = self.testrec1_xm_to_replace.replace('123456789', str(recid))
        self.testrec1_replaced_xm = self.testrec1_replaced_xm.replace('123456789', str(recid))
        self.testrec1_replaced_hm = self.testrec1_replaced_hm.replace('123456789', str(recid))
        # test of the inserted record:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm, self.testrec1_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm, self.testrec1_hm), '')

    def test_strong_tags_persistence(self):
        """bibupload - strong tags, persistence in replace mode"""
        # replace all metadata tags; will the strong tags be kept?
        recs = bibupload.xml_marc_to_records(self.testrec1_xm_to_replace)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.check_record_consistency(recid)
        replaced_xm = print_record(recid, 'xm')
        replaced_hm = print_record(recid, 'hm')
        # did it work?
        self.assertEqual(compare_xmbuffers(replaced_xm, self.testrec1_replaced_xm), '')
        self.assertEqual(compare_hmbuffers(replaced_hm, self.testrec1_replaced_hm), '')

class BibUploadPretendTest(GenericBibUploadTest):
    """
    Testing bibupload --pretend correctness.
    """
    def setUp(self):
        from invenio.legacy.bibsched.bibtask import task_set_task_param
        GenericBibUploadTest.setUp(self)
        self.demo_data = bibupload.xml_marc_to_records(open(os.path.join(cfg['CFG_TMPDIR'], 'demobibdata.xml')).read())[0]
        self.before = self._get_tables_fingerprint()
        task_set_task_param('pretend', True)

    def tearDown(self):
        from invenio.legacy.bibsched.bibtask import task_set_task_param
        GenericBibUploadTest.tearDown(self)
        task_set_task_param('pretend', False)

    @staticmethod
    def _get_tables_fingerprint():
        """
        Take lenght and last modification time of all the tables that
        might be touched by bibupload and return them in a nice structure.
        """
        fingerprint = {}
        tables = ['bibrec', 'bibdoc', 'bibrec_bibdoc', 'bibdoc_bibdoc', 'bibfmt', 'hstDOCUMENT', 'hstRECORD', 'bibHOLDINGPEN', 'bibdocmoreinfo', 'bibdocfsinfo']
        for i in xrange(100):
            tables.append('bib%02dx' % i)
            tables.append('bibrec_bib%02dx' % i)
        for table in tables:
            fingerprint[table] = get_table_status_info(table)
        return fingerprint

    @staticmethod
    def _checks_tables_fingerprints(before, after):
        """
        Checks differences in table_fingerprints.
        """
        for table in before.keys():
            if before[table] != after[table]:
                raise StandardError("Table %s has been modified: before was [%s], after was [%s]" % (table, pprint.pformat(before[table]), pprint.pformat(after[table])))
        return True

    def test_pretend_insert(self):
        """bibupload - pretend insert"""
        bibupload.bibupload_records([self.demo_data], opt_mode='insert', pretend=True)
        self.failUnless(self._checks_tables_fingerprints(self.before, self._get_tables_fingerprint()))

    def test_pretend_correct(self):
        """bibupload - pretend correct"""
        bibupload.bibupload_records([self.demo_data], opt_mode='correct', pretend=True)
        self.failUnless(self._checks_tables_fingerprints(self.before, self._get_tables_fingerprint()))

    def test_pretend_replace(self):
        """bibupload - pretend replace"""
        bibupload.bibupload_records([self.demo_data], opt_mode='replace', pretend=True)
        self.failUnless(self._checks_tables_fingerprints(self.before, self._get_tables_fingerprint()))

    def test_pretend_append(self):
        """bibupload - pretend append"""
        bibupload.bibupload_records([self.demo_data], opt_mode='append', pretend=True)
        self.failUnless(self._checks_tables_fingerprints(self.before, self._get_tables_fingerprint()))

    def test_pretend_replace_or_insert(self):
        """bibupload - pretend replace or insert"""
        bibupload.bibupload_records([self.demo_data], opt_mode='replace_or_insert', pretend=True)
        self.failUnless(self._checks_tables_fingerprints(self.before, self._get_tables_fingerprint()))

    def test_pretend_holdingpen(self):
        """bibupload - pretend holdingpen"""
        bibupload.bibupload_records([self.demo_data], opt_mode='holdingpen', pretend=True)
        self.failUnless(self._checks_tables_fingerprints(self.before, self._get_tables_fingerprint()))

    def test_pretend_delete(self):
        """bibupload - pretend delete"""
        bibupload.bibupload_records([self.demo_data], opt_mode='delete', pretend=True)
        self.failUnless(self._checks_tables_fingerprints(self.before, self._get_tables_fingerprint()))

    def test_pretend_reference(self):
        """bibupload - pretend reference"""
        bibupload.bibupload_records([self.demo_data], opt_mode='reference', pretend=True)
        self.failUnless(self._checks_tables_fingerprints(self.before, self._get_tables_fingerprint()))

class BibUploadHoldingPenTest(GenericBibUploadTest):
    """
    Testing the Holding Pen usage.
    """
    def setUp(self):
        from invenio.legacy.bibsched.bibtask import task_set_task_param, setup_loggers
        GenericBibUploadTest.setUp(self)
        self.verbose = 9
        setup_loggers()
        task_set_task_param('verbose', self.verbose)
        self.recid = 10
        self.oai_id = "oai:cds.cern.ch:CERN-EP-2001-094"

    def test_holding_pen_upload_with_recid(self):
        """bibupload - holding pen upload with recid"""
        test_to_upload = """<?xml version="1.0" encoding="UTF-8"?>
            <collection xmlns="http://www.loc.gov/MARC21/slim">
            <record>
            <controlfield tag="001">%s</controlfield>
            <datafield tag="700" ind1=" " ind2=" ">
                <subfield code="a">Kleefeld, F</subfield>
            </datafield>
            <datafield tag="700" ind1=" " ind2=" ">
                <subfield code="a">Newcomer, Y</subfield>
            </datafield>
            <datafield tag="700" ind1=" " ind2=" ">
                <subfield code="a">Rupp, G</subfield>
            </datafield>
            <datafield tag="700" ind1=" " ind2=" ">
                <subfield code="a">Scadron, M D</subfield>
            </datafield>
            </record>
            </collection>""" % self.recid
        recs = bibupload.xml_marc_to_records(test_to_upload)
        bibupload.insert_record_into_holding_pen(recs[0], "")
        res = run_sql("SELECT changeset_xml FROM bibHOLDINGPEN WHERE id_bibrec=%s", (self.recid, ))
        self.failUnless("Rupp, G" in res[0][0])

    def test_holding_pen_upload_with_oai_id(self):
        """bibupload - holding pen upload with oai_id"""
        test_to_upload = """<?xml version="1.0" encoding="UTF-8"?>
            <collection xmlns="http://www.loc.gov/MARC21/slim">
            <record>
            <datafield tag="700" ind1=" " ind2=" ">
                <subfield code="a">Kleefeld, F</subfield>
            </datafield>
            <datafield tag="700" ind1=" " ind2=" ">
                <subfield code="a">Newcomer, Y</subfield>
            </datafield>
            <datafield tag="700" ind1=" " ind2=" ">
                <subfield code="a">Rupp, G</subfield>
            </datafield>
            <datafield tag="700" ind1=" " ind2=" ">
                <subfield code="a">Scadron, M D</subfield>
            </datafield>
            <datafield tag="%(extoaiidtag)s" ind1="%(extoaiidind1)s" ind2="%(extoaiidind2)s">
                <subfield code="%(extoaiidsubfieldcode)s">%(value)s</subfield>
            </datafield>
            </record>
            </collection>""" % {'extoaiidtag': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][0:3],
               'extoaiidind1': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][3:4] or " ",
               'extoaiidind2': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5] != "_" and \
                            cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][4:5] or " ",
               'extoaiidsubfieldcode': cfg['CFG_BIBUPLOAD_EXTERNAL_OAIID_TAG'][5:6],
               'value': self.oai_id
            }
        recs = bibupload.xml_marc_to_records(test_to_upload)
        bibupload.insert_record_into_holding_pen(recs[0], self.oai_id)
        res = run_sql("SELECT changeset_xml FROM bibHOLDINGPEN WHERE id_bibrec=%s AND oai_id=%s", (self.recid, self.oai_id))
        self.failUnless("Rupp, G" in res[0][0])

    def tearDown(self):
        GenericBibUploadTest.tearDown(self)
        run_sql("DELETE FROM bibHOLDINGPEN WHERE id_bibrec=%s", (self.recid, ))

class BibUploadFFTModeTest(GenericBibUploadTest):
    """
    Testing treatment of fulltext file transfer import mode.
    """
    def _test_bibdoc_status(self, recid, docname, status):
        res = run_sql('SELECT bd.status FROM bibrec_bibdoc as bb JOIN bibdoc as bd ON bb.id_bibdoc = bd.id WHERE bb.id_bibrec = %s AND bb.docname = %s', (recid, docname))
        self.failUnless(res)
        self.assertEqual(status, res[0][0])

    def test_writing_rights(self):
        """bibupload - FFT has writing rights"""
        self.failUnless(bibupload.writing_rights_p())

    def test_simple_fft_insert(self):
        """bibupload - simple FFT insert"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')
        self.failUnless(try_url_download(testrec_expected_url))

    def test_fft_insert_with_valid_embargo(self):
        """bibupload - FFT insert with valid embargo"""
        # define the test case:
        future_date = time.strftime('%Y-%m-%d', time.gmtime(time.time() + 24 * 3600 * 2))
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="r">firerole: deny until '%(future_date)s'
allow any</subfield>
         </datafield>
        </record>
        """ % {
            'future_date': future_date,
            'siteurl': cfg['CFG_SITE_URL']
        }
        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')
        result = urlopen(testrec_expected_url).read()
        self.failUnless("This file is restricted." in result, result)

    def test_fft_insert_with_expired_embargo(self):
        """bibupload - FFT insert with expired embargo"""
        # define the test case:
        past_date = time.strftime('%Y-%m-%d', time.gmtime(time.time() - 24 * 3600 * 2))
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="980" ind1=" " ind2=" ">
          <subfield code="a">ARTICLE</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="r">firerole: deny until '%(past_date)s'
allow any</subfield>
         </datafield>
        </record>
        """ % {
            'past_date': past_date,
            'siteurl': cfg['CFG_SITE_URL']
        }
        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif</subfield>
         </datafield>
         <datafield tag="980" ind1=" " ind2=" ">
          <subfield code="a">ARTICLE</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif
        980__ $$aARTICLE
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')
        result = urlopen(testrec_expected_url).read()
        self.failIf("If you already have an account, please login using the form below." in result, result)
        self.assertEqual(test_web_page_content(testrec_expected_url, 'hyde', 'h123yde', expected_text='Authorization failure'), [])
        force_webcoll(recid)
        self.assertEqual(test_web_page_content(testrec_expected_url, 'hyde', 'h123yde', expected_text=urlopen("%(siteurl)s/img/site_logo.gif" % {
            'siteurl': cfg['CFG_SITE_URL']
        }).read()), [])

    def test_exotic_format_fft_append(self):
        """bibupload - exotic format FFT append"""
        # define the test case:
        from invenio.modules.access.local_config import CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS
        testfile = os.path.join(cfg['CFG_TMPDIR'], 'test.ps.Z')
        open(testfile, 'w').write('TEST')
        email_tag = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][0:3]
        email_ind1 = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][3]
        email_ind2 = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][4]
        email_code = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][5]
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="%(email_tag)s" ind1="%(email_ind1)s" ind2="%(email_ind2)s">
          <subfield code="%(email_code)s">jekyll@cds.cern.ch</subfield>
         </datafield>
        </record>
        """ % {
            'email_tag': email_tag,
            'email_ind1': email_ind1 == '_' and ' ' or email_ind1,
            'email_ind2': email_ind2 == '_' and ' ' or email_ind2,
            'email_code': email_code}
        testrec_to_append = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%s</subfield>
         </datafield>
        </record>
        """ % testfile

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="%(email_tag)s" ind1="%(email_ind1)s" ind2="%(email_ind2)s">
          <subfield code="%(email_code)s">jekyll@cds.cern.ch</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/test.ps.Z</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'],
            'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == '_' and ' ' or email_ind1,
            'email_ind2': email_ind2 == '_' and ' ' or email_ind2,
            'email_code': email_code}

        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        %(email_tag)s%(email_ind1)s%(email_ind2)s $$%(email_code)sjekyll@cds.cern.ch
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/test.ps.Z
        """ % {'siteurl': cfg['CFG_SITE_URL'],
            'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == ' ' and '_' or email_ind1,
            'email_ind2': email_ind2 == ' ' and '_' or email_ind2,
            'email_code': email_code}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/test.ps.Z" \
               % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url2 = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/test?format=ps.Z" \
               % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_to_append = testrec_to_append.replace('123456789',
                                                          str(recid))
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        testrec_expected_url2 = testrec_expected_url.replace('123456789',
                                                          str(recid))
        recs = bibupload.xml_marc_to_records(testrec_to_append)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='append')[0]
        self.check_record_consistency(recid)
        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')
        self.assertEqual(test_web_page_content(testrec_expected_url, 'jekyll', 'j123ekyll', expected_text='TEST'), [])
        self.assertEqual(test_web_page_content(testrec_expected_url2, 'jekyll', 'j123ekyll', expected_text='TEST'), [])


    def test_fft_check_md5_through_bibrecdoc_str(self):
        """bibupload - simple FFT insert, check md5 through BibRecDocs.str()"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%s/img/head.gif</subfield>
         </datafield>
        </record>
        """ % cfg['CFG_SITE_URL']
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)

        original_md5 = md5(urlopen('%s/img/head.gif' % cfg['CFG_SITE_URL']).read()).hexdigest()

        bibrec_str = str(BibRecDocs(int(recid)))

        md5_found = False
        for row in bibrec_str.split('\n'):
            if 'checksum' in row:
                if original_md5 in row:
                    md5_found = True

        self.failUnless(md5_found)


    def test_detailed_fft_insert(self):
        """bibupload - detailed FFT insert"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="t">SuperMain</subfield>
          <subfield code="d">This is a description</subfield>
          <subfield code="z">This is a comment</subfield>
          <subfield code="n">CIDIESSE</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/rss.png</subfield>
          <subfield code="t">SuperMain</subfield>
          <subfield code="f">.jpeg</subfield>
          <subfield code="d">This is a description</subfield>
          <subfield code="z">This is a second comment</subfield>
          <subfield code="n">CIDIESSE</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/CIDIESSE.gif</subfield>
          <subfield code="y">This is a description</subfield>
          <subfield code="z">This is a comment</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/CIDIESSE.jpeg</subfield>
          <subfield code="y">This is a description</subfield>
          <subfield code="z">This is a second comment</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/CIDIESSE.gif$$yThis is a description$$zThis is a comment
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/CIDIESSE.jpeg$$yThis is a description$$zThis is a second comment
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url1 = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/CIDIESSE.gif" % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url2 = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/CIDIESSE.jpeg" % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url1 = testrec_expected_url1.replace('123456789',
                                                          str(recid))
        testrec_expected_url2 = testrec_expected_url1.replace('123456789',
                                                          str(recid))
        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')
        self.failUnless(try_url_download(testrec_expected_url1))
        self.failUnless(try_url_download(testrec_expected_url2))


    def test_simple_fft_insert_with_restriction(self):
        """bibupload - simple FFT insert with restriction"""
        # define the test case:
        from invenio.modules.access.local_config import CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS
        email_tag = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][0:3]
        email_ind1 = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][3]
        email_ind2 = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][4]
        email_code = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][5]
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="%(email_tag)s" ind1="%(email_ind1)s" ind2="%(email_ind2)s">
          <subfield code="%(email_code)s">jekyll@cds.cern.ch</subfield>
         </datafield>
         <datafield tag="980" ind1=" " ind2=" ">
          <subfield code="a">ARTICLE</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="r">thesis</subfield>
          <subfield code="x">%(siteurl)s/img/sb.gif</subfield>
         </datafield>
        </record>
        """ % {'email_tag': email_tag,
            'email_ind1': email_ind1 == '_' and ' ' or email_ind1,
            'email_ind2': email_ind2 == '_' and ' ' or email_ind2,
            'email_code': email_code,
            'siteurl': cfg['CFG_SITE_URL']}

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="%(email_tag)s" ind1="%(email_ind1)s" ind2="%(email_ind2)s">
          <subfield code="%(email_code)s">jekyll@cds.cern.ch</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif?subformat=icon</subfield>
          <subfield code="x">icon</subfield>
         </datafield>
         <datafield tag="980" ind1=" " ind2=" ">
          <subfield code="a">ARTICLE</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'],
            'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == '_' and ' ' or email_ind1,
            'email_ind2': email_ind2 == '_' and ' ' or email_ind2,
            'email_code': email_code}

        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        %(email_tag)s%(email_ind1)s%(email_ind2)s $$%(email_code)sjekyll@cds.cern.ch
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif?subformat=icon$$xicon
        980__ $$aARTICLE
        """ % {'siteurl': cfg['CFG_SITE_URL'],
            'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == ' ' and '_' or email_ind1,
            'email_ind2': email_ind2 == ' ' and '_' or email_ind2,
            'email_code': email_code}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_icon = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif?subformat=icon" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        testrec_expected_icon = testrec_expected_icon.replace('123456789',
                                                          str(recid))
        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        self.assertEqual(test_web_page_content(testrec_expected_icon, 'jekyll', 'j123ekyll', expected_text=urlopen('%(siteurl)s/img/sb.gif' % {
            'siteurl': cfg['CFG_SITE_URL']
        }).read()), [])
        self.assertEqual(test_web_page_content(testrec_expected_icon, 'hyde', 'h123yde', expected_text='Authorization failure'), [])
        force_webcoll(recid)
        self.assertEqual(test_web_page_content(testrec_expected_icon, 'hyde', 'h123yde', expected_text=urlopen('%(siteurl)s/img/restricted.gif' % {'siteurl': cfg['CFG_SITE_URL']}).read()), [])

        self.failUnless("HTTP Error 401: Unauthorized" in test_web_page_content(testrec_expected_url, 'hyde', 'h123yde')[0])
        self.failUnless("This file is restricted." in urlopen(testrec_expected_url).read())

    def test_simple_fft_insert_with_icon(self):
        """bibupload - simple FFT insert with icon"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="x">%(siteurl)s/img/sb.gif</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif?subformat=icon</subfield>
          <subfield code="x">icon</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif?subformat=icon$$xicon
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_icon = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif?subformat=icon" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        testrec_expected_icon = testrec_expected_icon.replace('123456789',
                                                          str(recid))
        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        self.failUnless(try_url_download(testrec_expected_url))
        self.failUnless(try_url_download(testrec_expected_icon))

    def test_multiple_fft_insert(self):
        """bibupload - multiple FFT insert"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/head.gif</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/95/files/9809057.pdf</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(prefix)s/var/tmp/demobibdata.xml</subfield>
         </datafield>
        </record>
        """ % {
            'prefix': cfg['CFG_PREFIX'],
            'siteurl': cfg['CFG_SITE_URL'],
            'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'],
        }
        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/9809057.pdf</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/demobibdata.xml</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/head.gif</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/9809057.pdf
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/demobibdata.xml
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/head.gif
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        testrec_expected_urls = []
        for files in ('site_logo.gif', 'head.gif', '9809057.pdf', 'demobibdata.xml'):
            testrec_expected_urls.append('%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/%(files)s' % {'siteurl' : cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'], 'files' : files})
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_urls = []
        for files in ('site_logo.gif', 'head.gif', '9809057.pdf', 'demobibdata.xml'):
            testrec_expected_urls.append('%(siteurl)s/%(CFG_SITE_RECORD)s/%(recid)s/files/%(files)s' % {'siteurl' : cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'], 'files' : files, 'recid' : recid})
        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')

        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')
        for url in testrec_expected_urls:
            self.failUnless(try_url_download(url))

        self._test_bibdoc_status(recid, 'head', '')
        self._test_bibdoc_status(recid, '9809057', '')
        self._test_bibdoc_status(recid, 'site_logo', '')
        self._test_bibdoc_status(recid, 'demobibdata', '')

    def test_simple_fft_correct(self):
        """bibupload - simple FFT correct"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/sb.gif</subfield>
          <subfield code="n">site_logo</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        test_to_correct = test_to_correct.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        bibupload.bibupload_records(recs, opt_mode='correct')[0]
        self.check_record_consistency(recid)

        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.failUnless(try_url_download(testrec_expected_url))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        self._test_bibdoc_status(recid, 'site_logo', '')

    def test_fft_correct_already_exists(self):
        """bibupload - FFT correct with already identical existing file"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="d">a description</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/help.png</subfield>
          <subfield code="n">site_logo</subfield>
          <subfield code="d">another description</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/rss.png</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/line.gif</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/merge.png</subfield>
          <subfield code="n">line</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="d">a second description</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/help.png</subfield>
          <subfield code="n">site_logo</subfield>
          <subfield code="d">another second description</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/refresh.png</subfield>
          <subfield code="n">rss</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/line.gif</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/merge-small.png</subfield>
          <subfield code="n">line</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/line.gif</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/line.png</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/rss.png</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif</subfield>
          <subfield code="y">a second description</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.png</subfield>
          <subfield code="y">another second description</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/line.gif
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/line.png
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/rss.png
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif$$ya second description
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.png$$yanother second description
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url2 = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/rss.png" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url3 = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.png" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url4 = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/line.png" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url5 = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/line.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        _, recid, _ = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        testrec_expected_url2 = testrec_expected_url2.replace('123456789',
                                                          str(recid))
        testrec_expected_url3 = testrec_expected_url3.replace('123456789',
                                                          str(recid))
        testrec_expected_url4 = testrec_expected_url4.replace('123456789',
                                                          str(recid))
        testrec_expected_url5 = testrec_expected_url5.replace('123456789',
                                                          str(recid))
        test_to_correct = test_to_correct.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        bibupload.bibupload(recs[0], opt_mode='correct')
        self.check_record_consistency(recid)

        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.failUnless(try_url_download(testrec_expected_url))
        self.failUnless(try_url_download(testrec_expected_url2))
        self.failUnless(try_url_download(testrec_expected_url3))
        self.failUnless(try_url_download(testrec_expected_url4))
        self.failUnless(try_url_download(testrec_expected_url5))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        bibrecdocs = BibRecDocs(recid)
        self.failUnless(bibrecdocs.get_bibdoc('rss').list_versions(), [1, 2])
        self.failUnless(bibrecdocs.get_bibdoc('site_logo').list_versions(), [1])
        self.failUnless(bibrecdocs.get_bibdoc('line').list_versions(), [1, 2])

    def test_fft_correct_modify_doctype(self):
        """bibupload - FFT correct with different doctype"""
        test_to_upload = """
        <record>
            <controlfield tag="003">SzGeCERN</controlfield>
            <datafield tag="FFT" ind1=" " ind2=" ">
                <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
                <subfield code="d">a description</subfield>
                <subfield code="t">TEST1</subfield>
            </datafield>
        </record>
        """ % {
              'siteurl': cfg['CFG_SITE_URL']
              }

        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="n">site_logo</subfield>
          <subfield code="t">TEST2</subfield>
         </datafield>
        </record>
        """
        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif</subfield>
          <subfield code="y">a description</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        _, recid, _ = bibupload.bibupload(recs[0], opt_mode='insert')
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        bibrecdocs = BibRecDocs(recid)
        self.failUnless(bibrecdocs.get_bibdoc('site_logo').doctype, 'TEST1')

        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        bibupload.bibupload(recs[0], opt_mode='correct')

        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')

        bibrecdocs = BibRecDocs(recid)
        self.failUnless(bibrecdocs.get_bibdoc('site_logo').doctype, 'TEST2')

    def test_fft_append_already_exists(self):
        """bibupload - FFT append with already identical existing file"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="d">a description</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        test_to_append = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="d">a second description</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/help.png</subfield>
          <subfield code="n">site_logo</subfield>
          <subfield code="d">another second description</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif</subfield>
          <subfield code="y">a description</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.png</subfield>
          <subfield code="y">another second description</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif$$ya description
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.png$$yanother second description
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url2 = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.png" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        _, recid, _ = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        test_to_append = test_to_append.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_append)
        err, recid, msg = bibupload.bibupload(recs[0], opt_mode='append')
        self.check_record_consistency(recid)

        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.failUnless(try_url_download(testrec_expected_url))
        self.failUnless(try_url_download(testrec_expected_url2))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')


    def test_fft_implicit_fix_marc(self):
        """bibupload - FFT implicit FIX-MARC"""
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="0" ind2=" ">
          <subfield code="f">foo@bar.com</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="f">%(siteurl)s/img/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="856" ind1="0" ind2=" ">
          <subfield code="f">foo@bar.com</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/img/site_logo.gif</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="0" ind2=" ">
          <subfield code="f">foo@bar.com</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/img/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8560_ $$ffoo@bar.com
        8564_ $$u%(siteurl)s/img/site_logo.gif
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        test_to_correct = test_to_correct.replace('123456789',
                                                          str(recid))
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        # correct test record with implicit FIX-MARC:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        bibupload.bibupload_records(recs, opt_mode='correct')[0]
        self.check_record_consistency(recid)
        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

    def test_fft_vs_bibedit(self):
        """bibupload - FFT Vs. BibEdit compatibility"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        test_to_replace = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">http://www.google.com/</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="z">BibEdit Comment</subfield>
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif</subfield>
          <subfield code="y">BibEdit Description</subfield>
          <subfield code="x">01</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">http://cern.ch/</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}

        testrec_expected_xm = str(test_to_replace)
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$uhttp://www.google.com/
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif$$x01$$yBibEdit Description$$zBibEdit Comment
        8564_ $$uhttp://cern.ch/
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        test_to_replace = test_to_replace.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_replace)
        bibupload.bibupload_records(recs, opt_mode='replace')[0]
        self.check_record_consistency(recid)

        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.failUnless(try_url_download(testrec_expected_url))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        self._test_bibdoc_status(recid, 'site_logo', '')

        bibrecdocs = BibRecDocs(recid)
        bibdoc = bibrecdocs.get_bibdoc('site_logo')
        self.assertEqual(bibdoc.get_description('.gif'), 'BibEdit Description')


    def test_detailed_fft_correct(self):
        """bibupload - detailed FFT correct
        """
        # define the test case:

        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="d">Try</subfield>
          <subfield code="z">Comment</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }

        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/head.gif</subfield>
          <subfield code="n">site_logo</subfield>
          <subfield code="m">patata</subfield>
          <subfield code="d">Next Try</subfield>
          <subfield code="z">KEEP-OLD-VALUE</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/patata.gif</subfield>
          <subfield code="y">Next Try</subfield>
          <subfield code="z">Comment</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/patata.gif$$yNext Try$$zComment
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/patata.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}

        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)

        # replace test buffers with real recid of inserted test record:

        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))

        test_to_correct = test_to_correct.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        bibupload.bibupload_records(recs, opt_mode='correct')
        self.check_record_consistency(recid)

        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')

        self.failUnless(try_url_download(testrec_expected_url))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '', "bufers not equal: %s and %s" % (inserted_xm, testrec_expected_xm))

        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '', "bufers not equal: %s and %s" % (inserted_hm, testrec_expected_hm))

        self._test_bibdoc_status(recid, 'patata', '')

    def test_no_url_fft_correct(self):
        """bibupload - no_url FFT correct"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="d">Try</subfield>
          <subfield code="z">Comment</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="n">site_logo</subfield>
          <subfield code="m">patata</subfield>
          <subfield code="f">.gif</subfield>
          <subfield code="d">KEEP-OLD-VALUE</subfield>
          <subfield code="z">Next Comment</subfield>
         </datafield>
        </record>
        """

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/patata.gif</subfield>
          <subfield code="y">Try</subfield>
          <subfield code="z">Next Comment</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/patata.gif$$yTry$$zNext Comment
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/patata.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}

        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)

        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))

        test_to_correct = test_to_correct.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        bibupload.bibupload_records(recs, opt_mode='correct')[0]
        self.check_record_consistency(recid)

        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')

        self.failUnless(try_url_download(testrec_expected_url))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        self._test_bibdoc_status(recid, 'patata', '')

    def test_new_icon_fft_append(self):
        """bibupload - new icon FFT append"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
        </record>
        """
        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="n">site_logo</subfield>
          <subfield code="x">%(siteurl)s/img/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif?subformat=icon</subfield>
          <subfield code="x">icon</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif?subformat=icon$$xicon
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif?subformat=icon" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}

        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)

        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))

        test_to_correct = test_to_correct.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        bibupload.bibupload_records(recs, opt_mode='append')[0]
        self.check_record_consistency(recid)

        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')

        self.failUnless(try_url_download(testrec_expected_url))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        self._test_bibdoc_status(recid, 'site_logo', '')


    def test_multiple_fft_correct(self):
        """bibupload - multiple FFT correct"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="d">Try</subfield>
          <subfield code="z">Comment</subfield>
          <subfield code="r">Restricted</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/okay.gif</subfield>
          <subfield code="n">site_logo</subfield>
          <subfield code="f">.jpeg</subfield>
          <subfield code="d">Try jpeg</subfield>
          <subfield code="z">Comment jpeg</subfield>
          <subfield code="r">Restricted</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/loading.gif</subfield>
          <subfield code="n">site_logo</subfield>
          <subfield code="m">patata</subfield>
          <subfield code="f">.gif</subfield>
          <subfield code="r">New restricted</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/patata.gif</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/patata.gif
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/patata.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}

        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)

        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))

        test_to_correct = test_to_correct.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        bibupload.bibupload_records(recs, opt_mode='correct')[0]
        self.check_record_consistency(recid)

        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')

        self.failUnless("This file is restricted." in urlopen(testrec_expected_url).read())
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        self._test_bibdoc_status(recid, 'patata', 'New restricted')

    def test_purge_fft_correct(self):
        """bibupload - purge FFT correct"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/head.gif</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        test_to_purge = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="t">PURGE</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/head.gif</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/head.gif
        8564_ $$u%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif
        """ % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}

        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        test_to_correct = test_to_correct.replace('123456789',
                                                          str(recid))
        test_to_purge = test_to_purge.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        bibupload.bibupload_records(recs, opt_mode='correct')[0]
        self.check_record_consistency(recid)

        # purge test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_purge)
        bibupload.bibupload_records(recs, opt_mode='correct')
        self.check_record_consistency(recid)


        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.failUnless(try_url_download(testrec_expected_url))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        self._test_bibdoc_status(recid, 'site_logo', '')
        self._test_bibdoc_status(recid, 'head', '')

    def test_revert_fft_correct(self):
        """bibupload - revert FFT correct"""
        # define the test case:
        from invenio.modules.access.local_config import CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS
        email_tag = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][0:3]
        email_ind1 = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][3]
        email_ind2 = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][4]
        email_code = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][5]
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="%(email_tag)s" ind1="%(email_ind1)s" ind2="%(email_ind2)s">
          <subfield code="%(email_code)s">jekyll@cds.cern.ch</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/iconpen.gif</subfield>
          <subfield code="n">site_logo</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == '_' and ' ' or email_ind1,
            'email_ind2': email_ind2 == '_' and ' ' or email_ind2,
            'email_code': email_code}
        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%s/img/head.gif</subfield>
          <subfield code="n">site_logo</subfield>
         </datafield>
        </record>
        """ % cfg['CFG_SITE_URL']
        test_to_revert = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="n">site_logo</subfield>
          <subfield code="t">REVERT</subfield>
          <subfield code="v">1</subfield>
         </datafield>
        </record>
        """

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="%(email_tag)s" ind1="%(email_ind1)s" ind2="%(email_ind2)s">
          <subfield code="%(email_code)s">jekyll@cds.cern.ch</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'],
            'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == '_' and ' ' or email_ind1,
            'email_ind2': email_ind2 == '_' and ' ' or email_ind2,
            'email_code': email_code}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        %(email_tag)s%(email_ind1)s%(email_ind2)s $$%(email_code)sjekyll@cds.cern.ch
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif
        """ % {'siteurl': cfg['CFG_SITE_URL'],
            'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == ' ' and '_' or email_ind1,
            'email_ind2': email_ind2 == ' ' and '_' or email_ind2,
            'email_code': email_code}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}

        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        test_to_correct = test_to_correct.replace('123456789',
                                                          str(recid))
        test_to_revert = test_to_revert.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        bibupload.bibupload_records(recs, opt_mode='correct')
        self.check_record_consistency(recid)

        # revert test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_revert)
        bibupload.bibupload_records(recs, opt_mode='correct')
        self.check_record_consistency(recid)


        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.failUnless(try_url_download(testrec_expected_url))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        self._test_bibdoc_status(recid, 'site_logo', '')

        expected_content_version1 = urlopen('%s/img/iconpen.gif' % cfg['CFG_SITE_URL']).read()
        expected_content_version2 = urlopen('%s/img/head.gif' % cfg['CFG_SITE_URL']).read()
        expected_content_version3 = expected_content_version1

        self.assertEqual(test_web_page_content('%s/%s/%s/files/site_logo.gif?version=1' % (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], recid), 'jekyll', 'j123ekyll', expected_content_version1), [])
        self.assertEqual(test_web_page_content('%s/%s/%s/files/site_logo.gif?version=2' % (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], recid), 'jekyll', 'j123ekyll', expected_content_version2), [])
        self.assertEqual(test_web_page_content('%s/%s/%s/files/site_logo.gif?version=3' % (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], recid), 'jekyll', 'j123ekyll', expected_content_version3), [])


    def test_simple_fft_replace(self):
        """bibupload - simple FFT replace"""
        # define the test case:
        from invenio.modules.access.local_config import CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS
        email_tag = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][0:3]
        email_ind1 = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][3]
        email_ind2 = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][4]
        email_code = CFG_ACC_GRANT_AUTHOR_RIGHTS_TO_EMAILS_IN_TAGS[0][5]
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="%(email_tag)s" ind1="%(email_ind1)s" ind2="%(email_ind2)s">
          <subfield code="%(email_code)s">jekyll@cds.cern.ch</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/iconpen.gif</subfield>
          <subfield code="n">site_logo</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == '_' and ' ' or email_ind1,
            'email_ind2': email_ind2 == '_' and ' ' or email_ind2,
            'email_code': email_code}

        test_to_replace = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="%(email_tag)s" ind1="%(email_ind1)s" ind2="%(email_ind2)s">
          <subfield code="%(email_code)s">jekyll@cds.cern.ch</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/head.gif</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == '_' and ' ' or email_ind1,
            'email_ind2': email_ind2 == '_' and ' ' or email_ind2,
            'email_code': email_code}

        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="%(email_tag)s" ind1="%(email_ind1)s" ind2="%(email_ind2)s">
          <subfield code="%(email_code)s">jekyll@cds.cern.ch</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/head.gif</subfield>
         </datafield>
        </record>
        """ % {
             'siteurl': cfg['CFG_SITE_URL'],
            'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == '_' and ' ' or email_ind1,
            'email_ind2': email_ind2 == '_' and ' ' or email_ind2,
            'email_code': email_code}

        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        %(email_tag)s%(email_ind1)s%(email_ind2)s $$%(email_code)sjekyll@cds.cern.ch
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/head.gif
        """ % {
            'siteurl': cfg['CFG_SITE_URL'],
            'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'],
            'email_tag': email_tag,
            'email_ind1': email_ind1 == ' ' and '_' or email_ind1,
            'email_ind2': email_ind2 == ' ' and '_' or email_ind2,
            'email_code': email_code}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/head.gif" % { 'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}

        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        test_to_replace = test_to_replace.replace('123456789',
                                                          str(recid))
        # replace test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_replace)
        bibupload.bibupload_records(recs, opt_mode='replace')
        self.check_record_consistency(recid)

        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.failUnless(try_url_download(testrec_expected_url))
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')

        expected_content_version = urlopen('%s/img/head.gif' % cfg['CFG_SITE_URL']).read()

        self.assertEqual(test_web_page_content(testrec_expected_url, 'hyde', 'h123yde', expected_text='Authorization failure'), [])
        self.assertEqual(test_web_page_content(testrec_expected_url, 'jekyll', 'j123ekyll', expected_text=expected_content_version), [])


    def test_simple_fft_insert_with_modification_time(self):
        """bibupload - simple FFT insert with modification time"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="980" ind1=" " ind2=" ">
          <subfield code="a">ARTICLE</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="s">2006-05-04 03:02:01</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        testrec_expected_xm = """
        <record>
        <controlfield tag="001">123456789</controlfield>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="856" ind1="4" ind2=" ">
          <subfield code="u">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/123456789/files/site_logo.gif</subfield>
         </datafield>
         <datafield tag="980" ind1=" " ind2=" ">
          <subfield code="a">ARTICLE</subfield>
         </datafield>
        </record>
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_hm = """
        001__ 123456789
        003__ SzGeCERN
        100__ $$aTest, John$$uTest University
        8564_ $$u%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif
        980__ $$aARTICLE
        """ % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/site_logo.gif" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        testrec_expected_url2 = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload_records(recs, opt_mode='insert')[0]
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_xm = testrec_expected_xm.replace('123456789',
                                                          str(recid))
        testrec_expected_hm = testrec_expected_hm.replace('123456789',
                                                          str(recid))
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        testrec_expected_url2 = testrec_expected_url2.replace('123456789',
                                                          str(recid))
        # compare expected results:
        inserted_xm = print_record(recid, 'xm')
        inserted_hm = print_record(recid, 'hm')
        self.assertEqual(compare_xmbuffers(inserted_xm,
                                          testrec_expected_xm), '')
        self.assertEqual(compare_hmbuffers(inserted_hm,
                                          testrec_expected_hm), '')
        self.failUnless(try_url_download(testrec_expected_url))
        force_webcoll(recid)
        self.assertEqual(test_web_page_content(testrec_expected_url2, expected_text='<em>04 May 2006, 03:02</em>'), [])


    def test_multiple_fft_insert_with_modification_time(self):
        """bibupload - multiple FFT insert with modification time"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="980" ind1=" " ind2=" ">
          <subfield code="a">ARTICLE</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="s">2006-05-04 03:02:01</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/head.gif</subfield>
          <subfield code="s">2007-05-04 03:02:01</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/%(cfg['CFG_SITE_RECORD'])s/95/files/9809057.pdf</subfield>
          <subfield code="s">2008-05-04 03:02:01</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(prefix)s/var/tmp/demobibdata.xml</subfield>
          <subfield code="s">2009-05-04 03:02:01</subfield>
         </datafield>
        </record>
        """ % {
            'prefix': cfg['CFG_PREFIX'],
            'siteurl': cfg['CFG_SITE_URL'],
            'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD'],
        }
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        force_webcoll(recid)
        self.assertEqual(test_web_page_content(testrec_expected_url, expected_text=['<em>04 May 2006, 03:02</em>', '<em>04 May 2007, 03:02</em>', '<em>04 May 2008, 03:02</em>', '<em>04 May 2009, 03:02</em>']), [])

    def test_simple_fft_correct_with_modification_time(self):
        """bibupload - simple FFT correct with modification time"""
        # define the test case:
        test_to_upload = """
        <record>
        <controlfield tag="003">SzGeCERN</controlfield>
         <datafield tag="100" ind1=" " ind2=" ">
          <subfield code="a">Test, John</subfield>
          <subfield code="u">Test University</subfield>
         </datafield>
         <datafield tag="980" ind1=" " ind2=" ">
          <subfield code="a">ARTICLE</subfield>
         </datafield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/site_logo.gif</subfield>
          <subfield code="s">2007-05-04 03:02:01</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        test_to_correct = """
        <record>
        <controlfield tag="001">123456789</controlfield>
         <datafield tag="FFT" ind1=" " ind2=" ">
          <subfield code="a">%(siteurl)s/img/sb.gif</subfield>
          <subfield code="n">site_logo</subfield>
          <subfield code="s">2008-05-04 03:02:01</subfield>
         </datafield>
        </record>
        """ % {
            'siteurl': cfg['CFG_SITE_URL']
        }
        testrec_expected_url = "%(siteurl)s/%(CFG_SITE_RECORD)s/123456789/files/" \
            % {'siteurl': cfg['CFG_SITE_URL'], 'CFG_SITE_RECORD': cfg['CFG_SITE_RECORD']}
        # insert test record:
        recs = bibupload.xml_marc_to_records(test_to_upload)
        dummy, recid, dummy = bibupload.bibupload(recs[0], opt_mode='insert')
        self.check_record_consistency(recid)
        # replace test buffers with real recid of inserted test record:
        testrec_expected_url = testrec_expected_url.replace('123456789',
                                                          str(recid))
        test_to_correct = test_to_correct.replace('123456789',
                                                          str(recid))
        # correct test record with new FFT:
        recs = bibupload.xml_marc_to_records(test_to_correct)
        err, recid, msg = bibupload.bibupload(recs[0], opt_mode='correct')
        self.check_record_consistency(recid)
        force_webcoll(recid)
        self.assertEqual(test_web_page_content(testrec_expected_url, expected_text=['<em>04 May 2008, 03:02</em>']), [])


TEST_SUITE = make_test_suite(BibUploadNoUselessHistoryTest,
                             BibUploadHoldingPenTest,
                             BibUploadInsertModeTest,
                             BibUploadAppendModeTest,
                             BibUploadCorrectModeTest,
                             BibUploadDeleteModeTest,
                             BibUploadReplaceModeTest,
                             BibUploadReferencesModeTest,
                             BibUploadRecordsWithSYSNOTest,
                             BibUploadRecordsWithEXTOAIIDTest,
                             BibUploadRecordsWithOAIIDTest,
                             BibUploadIndicatorsTest,
                             BibUploadUpperLowerCaseTest,
                             BibUploadControlledProvenanceTest,
                             BibUploadStrongTagsTest,
                             BibUploadFFTModeTest,
                             BibUploadPretendTest,
                             BibUploadCallbackURLTest,
                             BibUploadMoreInfoTest,
                             BibUploadBibRelationsTest,
                             BibUploadRecordsWithDOITest,
                             BibUploadTypicalBibEditSessionTest,
                             BibUploadRealCaseRemovalDOIViaBibEdit,
                             )

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
