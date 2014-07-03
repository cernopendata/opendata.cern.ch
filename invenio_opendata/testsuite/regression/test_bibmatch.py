# -*- coding: utf-8 -*-
##
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

# pylint: disable=E1102

"""Unit tests for bibmatch."""

__revision__ = "$Id$"

from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.testsuite import InvenioTestCase, make_test_suite, run_test_suite

create_records = lazy_import('invenio.legacy.bibrecord:create_records')
match_records = lazy_import('invenio.legacy.bibmatch.engine:match_records')


class BibMatchTest(InvenioTestCase):
    """Test functions to check the functionality of bibmatch."""

    def setUp(self):
        """setting up helper variables for tests"""
        self.textmarc = """
000000020 001__ 20
000000020 041__ $$aeng
000000020 088__ $$aJYFL-RR-82-7
000000020 100__ $$aArje, J$$uUniversity of Jyvaskyla
000000020 245__ $$aCharge creation and reset mechanisms in an ion guide isotope separator (IGIS)
000000020 260__ $$aJyvaskyla$$bFinland Univ. Dept. Phys.$$cJul 1982
000000020 300__ $$a18 p
000000020 65017 $$2SzGeCERN$$aDetectors and Experimental Techniques
000000020 909C0 $$y1982
000000020 909C0 $$b19
000000020 909C1 $$uJyväsklä Univ.
000000020 909C1 $$c1990-01-28$$l50$$m2002-01-04$$oBATCH
000000020 909CS $$sn$$w198238n
000000020 980__ $$aREPORT

000000019 001__ 19
000000019 041__ $$aeng
000000019 088__ $$aSTAN-CS-81-898-MF
000000019 100__ $$aWhang, K$$uStanford University
000000019 245__ $$aSeparability as a physical database design methodology
000000019 260__ $$aStanford, CA$$bStanford Univ. Comput. Sci. Dept.$$cOct 1981
000000019 300__ $$a60 p
000000019 65017 $$2SzGeCERN$$aComputing and Computers
000000019 700__ $$aWiederhold, G
000000019 700__ $$aSagalowicz, D
000000019 909C0 $$y1981
000000019 909C0 $$b19
000000019 909C1 $$uStanford Univ.
000000019 909C1 $$c1990-01-28$$l50$$m2002-01-04$$oBATCH
000000019 909CS $$sn$$w198238n
000000019 980__ $$aREPORT
        """

        #ambig match:  Changed Atlantis (Timaeus) ->Atlantis
        self.recxml1 = """<?xml version="1.0" encoding="UTF-8"?>
<collection xmlns="http://www.loc.gov/MARC21/slim">
<record>
  <controlfield tag="001">95</controlfield>
  <datafield tag="035" ind1=" " ind2=" ">
    <subfield code="a">0289446CERCER</subfield>
  </datafield>
  <datafield tag="035" ind1=" " ind2=" ">
    <subfield code="9">SLAC</subfield>
    <subfield code="a">3838510</subfield>
  </datafield>
  <datafield tag="041" ind1=" " ind2=" ">
    <subfield code="a">eng</subfield>
  </datafield>
  <datafield tag="100" ind1=" " ind2=" ">
    <subfield code="a">Polyakov, A M</subfield>
    <subfield code="u">Princeton University</subfield>
  </datafield>
  <datafield tag="245" ind1=" " ind2=" ">
    <subfield code="a">The wall of the cave</subfield>
  </datafield>
  <datafield tag="260" ind1=" " ind2=" ">
    <subfield code="c">1994</subfield>
  </datafield>
  <datafield tag="520" ind1=" " ind2=" ">
    <subfield code="a">In this article old and new relations between gauge fields and strings are discussed. We add new arguments that the Yang Mills theories must be described by the non-critical strings in the five dimensional curved space. The physical meaning of the fifth dimension is that of the renormalization scale represented by the Liouville field. We analyze the meaning of the zigzag symmetry and show that it is likely to be present if there is a minimal supersymmetry on the world sheet. We also present the new string backgrounds which may be relevant for the description of the ordinary bosonic Yang-Mills theories. The article is written on the occasion of the 40-th anniversary of the IHES.</subfield>
  </datafield>
  <datafield tag="595" ind1=" " ind2=" ">
    <subfield code="a">SIS LANLPUBL2001</subfield>
  </datafield>
  <datafield tag="595" ind1=" " ind2=" ">
    <subfield code="a">LANL EDS</subfield>
  </datafield>
  <datafield tag="595" ind1=" " ind2=" ">
    <subfield code="a">SIS:2001 PR/LKR added</subfield>
  </datafield>
  <datafield tag="650" ind1="1" ind2="7">
    <subfield code="2">SzGeCERN</subfield>
    <subfield code="a">Particle Physics - Theory</subfield>
  </datafield>
  <datafield tag="690" ind1="C" ind2=" ">
    <subfield code="a">ARTICLE</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="4">
    <subfield code="c">645-658</subfield>
    <subfield code="p">Int. J. Mod. Phys. A</subfield>
    <subfield code="v">14</subfield>
    <subfield code="y">1999</subfield>
  </datafield>
  <datafield tag="859" ind1=" " ind2=" ">
    <subfield code="f">polyakov@puhep1.princeton.edu</subfield>
  </datafield>
  <datafield tag="916" ind1=" " ind2=" ">
    <subfield code="s">n</subfield>
    <subfield code="w">199837</subfield>
  </datafield>
  <datafield tag="960" ind1=" " ind2=" ">
    <subfield code="a">13</subfield>
  </datafield>
  <datafield tag="961" ind1=" " ind2=" ">
    <subfield code="c">20060916</subfield>
    <subfield code="h">0007</subfield>
    <subfield code="l">CER01</subfield>
    <subfield code="x">19980910</subfield>
  </datafield>
  <datafield tag="963" ind1=" " ind2=" ">
    <subfield code="a">PUBLIC</subfield>
  </datafield>
  <datafield tag="970" ind1=" " ind2=" ">
    <subfield code="a">000289446CER</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">ARTICLE</subfield>
  </datafield>
  <datafield tag="856" ind1="4" ind2=" ">
    <subfield code="u">http://invenio-demo.cern.ch/record/95/files/9809057.pdf</subfield>
  </datafield>
</record>
</collection>
"""
        #this is not in the collection
        self.recxml2 = """
<?xml version="1.0" encoding="UTF-8"?>
<collection xmlns="http://www.loc.gov/MARC21/slim">
<record>
  <controlfield tag="001">9124</controlfield>
  <datafield tag="970" ind1=" " ind2=" ">
    <subfield code="a">SPIRES-5726484</subfield>
  </datafield>
  <datafield tag="100" ind1=" " ind2=" ">
    <subfield code="a">Schulz, Michael B.</subfield>
    <subfield code="u">Caltech</subfield>
  </datafield>
  <datafield tag="773" ind1=" " ind2=" ">
    <subfield code="w">C02/06/25.2</subfield>
    <subfield code="t">Prepared for</subfield>
    <subfield code="c">477-480</subfield>
  </datafield>
  <datafield tag="650" ind1="1" ind2="7">
    <subfield code="a">Theory-HEP</subfield>
    <subfield code="2">INSPIRE</subfield>
  </datafield>
  <datafield tag="690" ind1="C" ind2=" ">
    <subfield code="a">Conference Paper</subfield>
    <subfield code="2">INSPIRE</subfield>
  </datafield>
  <datafield tag="520" ind1=" " ind2=" ">
    <subfield code="a">A brief overview of hep-th/0201028 prepared for NATO Advanced Study Institute and EC Summer School on Progress in String, Field and Particle Theory, Cargese, Corsica, France, 25 June - 11 July 2002.</subfield>
    <subfield code="9">arXiv</subfield>
  </datafield>
  <datafield tag="037" ind1=" " ind2=" ">
    <subfield code="a">arXiv:0810.5197</subfield>
    <subfield code="9">arXiv</subfield>
    <subfield code="c">hep-th</subfield>
  </datafield>
  <datafield tag="035" ind1=" " ind2=" ">
    <subfield code="z">oai:arXiv.org:0810.5197</subfield>
    <subfield code="9">arXiv</subfield>
  </datafield>
  <datafield tag="037" ind1=" " ind2=" ">
    <subfield code="a">CALT-68-2441</subfield>
  </datafield>
  <datafield tag="245" ind1=" " ind2=" ">
    <subfield code="a">Moduli stabilization from fluxes</subfield>
  </datafield>
  <datafield tag="300" ind1=" " ind2=" ">
    <subfield code="a">5</subfield>
  </datafield>
  <datafield tag="695" ind1=" " ind2=" ">
    <subfield code="a">talk: Cargese 2002/06/25</subfield>
    <subfield code="2">INSPIRE</subfield>
  </datafield>
  <datafield tag="695" ind1=" " ind2=" ">
    <subfield code="a">string model</subfield>
    <subfield code="2">INSPIRE</subfield>
  </datafield>
  <datafield tag="695" ind1=" " ind2=" ">
    <subfield code="a">compactification</subfield>
    <subfield code="2">INSPIRE</subfield>
  </datafield>
  <datafield tag="695" ind1=" " ind2=" ">
    <subfield code="a">moduli: stability</subfield>
    <subfield code="2">INSPIRE</subfield>
  </datafield>
  <datafield tag="695" ind1=" " ind2=" ">
    <subfield code="a">orientifold</subfield>
    <subfield code="2">INSPIRE</subfield>
  </datafield>
  <datafield tag="695" ind1=" " ind2=" ">
    <subfield code="a">membrane model: D-brane</subfield>
    <subfield code="2">INSPIRE</subfield>
  </datafield>
  <datafield tag="695" ind1=" " ind2=" ">
    <subfield code="a">flux</subfield>
    <subfield code="2">INSPIRE</subfield>
  </datafield>
  <datafield tag="695" ind1=" " ind2=" ">
    <subfield code="a">supersymmetry</subfield>
    <subfield code="2">INSPIRE</subfield>
  </datafield>
  <datafield tag="035" ind1=" " ind2=" ">
    <subfield code="z">D04-00603</subfield>
    <subfield code="9">DESY</subfield>
  </datafield>
  <datafield tag="035" ind1=" " ind2=" ">
    <subfield code="z">Schulz:2002eh</subfield>
    <subfield code="9">SPIRESTeX</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">Conference</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">arXiv</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">Citeable</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">CORE</subfield>
  </datafield>
  <datafield tag="269" ind1=" " ind2=" ">
    <subfield code="c">2008-10</subfield>
  </datafield>
  <datafield tag="961" ind1=" " ind2=" ">
    <subfield code="x">2003-11-17</subfield>
  </datafield>
  <datafield tag="961" ind1=" " ind2=" ">
    <subfield code="c">2009-12-11</subfield>
  </datafield>
</record>
</collection>
"""
        #ambig
        self.recxml3 = """
<?xml version="1.0" encoding="UTF-8"?>
<collection xmlns="http://www.loc.gov/MARC21/slim">
<record>
  <datafield tag="020" ind1=" " ind2=" ">
    <subfield code="a">2225350574</subfield>
  </datafield>
  <datafield tag="041" ind1=" " ind2=" ">
    <subfield code="a">fre</subfield>
  </datafield>
  <datafield tag="080" ind1=" " ind2=" ">
    <subfield code="a">518.5:62.01</subfield>
  </datafield>
  <datafield tag="100" ind1=" " ind2=" ">
    <subfield code="a">Dasse, Michel</subfield>
  </datafield>
  <datafield tag="245" ind1=" " ind2=" ">
    <subfield code="a">Analyse informatique</subfield>
  </datafield>
  <datafield tag="260" ind1=" " ind2=" ">
    <subfield code="a">Paris</subfield>
    <subfield code="b">Masson</subfield>
    <subfield code="c">1972</subfield>
  </datafield>
  <datafield tag="490" ind1=" " ind2=" ">
    <subfield code="a">Informatique</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="0">
    <subfield code="y">1972</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="0">
    <subfield code="b">21</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="1">
    <subfield code="c">1990-01-27</subfield>
    <subfield code="l">00</subfield>
    <subfield code="m">2002-04-12</subfield>
    <subfield code="o">BATCH</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="S">
    <subfield code="s">m</subfield>
    <subfield code="w">198604</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">BOOK</subfield>
  </datafield>
</record>

</collection>
"""
        #matched: quasi-normal -> quasi normal + missing word in title
        self.recxml4 = """
<?xml version="1.0" encoding="UTF-8"?>
<collection xmlns="http://www.loc.gov/MARC21/slim">
<record>
  <controlfield tag="003">SzGeCERN</controlfield>
  <controlfield tag="005">20060616163757.0</controlfield>
  <datafield tag="037" ind1=" " ind2=" ">
    <subfield code="a">hep-th/0606096</subfield>
  </datafield>
  <datafield tag="041" ind1=" " ind2=" ">
    <subfield code="a">eng</subfield>
  </datafield>
  <datafield tag="088" ind1=" " ind2=" ">
    <subfield code="a">UTHET-2006-05-01</subfield>
  </datafield>
  <datafield tag="100" ind1=" " ind2=" ">
    <subfield code="a">Koutsoumbas, G</subfield>
    <subfield code="u">National Technical University of Athens</subfield>
  </datafield>
  <datafield tag="245" ind1=" " ind2=" ">
    <subfield code="a">Quasinormal Modes of Perturbations of Four-Dimensional Topological Black Holes</subfield>
  </datafield>
  <datafield tag="260" ind1=" " ind2=" ">
    <subfield code="c">2006</subfield>
  </datafield>
  <datafield tag="269" ind1=" " ind2=" ">
    <subfield code="c">10 Jun 2006</subfield>
  </datafield>
  <datafield tag="300" ind1=" " ind2=" ">
    <subfield code="a">17 p</subfield>
  </datafield>
  <datafield tag="520" ind1=" " ind2=" ">
    <subfield code="a">We study the perturbative behaviour of topological black holes with scalar hair. We calculate both analytically and numerically the quasi-normal modes of the electromagnetic perturbations. In the case of small black holes we find clear evidence of a second-order phase transition of a topological black hole to a hairy configuration. We also find evidence of a second-order phase transition of the AdS vacuum solution to a topological black hole.</subfield>
  </datafield>
  <datafield tag="650" ind1="1" ind2="7">
    <subfield code="2">SzGeCERN</subfield>
    <subfield code="a">Particle Physics - Theory</subfield>
  </datafield>
  <datafield tag="690" ind1="C" ind2=" ">
    <subfield code="a">ARTICLE</subfield>
  </datafield>
  <datafield tag="695" ind1=" " ind2=" ">
    <subfield code="9">LANL EDS</subfield>
    <subfield code="a">High Energy Physics - Theory</subfield>
  </datafield>
  <datafield tag="700" ind1=" " ind2=" ">
    <subfield code="a">Musiri, S</subfield>
  </datafield>
  <datafield tag="700" ind1=" " ind2=" ">
    <subfield code="a">Papantonopoulos, E</subfield>
  </datafield>
  <datafield tag="700" ind1=" " ind2=" ">
    <subfield code="a">Siopsis, G</subfield>
  </datafield>
  <datafield tag="720" ind1=" " ind2=" ">
    <subfield code="a">Koutsoumbas, George</subfield>
  </datafield>
  <datafield tag="720" ind1=" " ind2=" ">
    <subfield code="a">Musiri, Suphot</subfield>
  </datafield>
  <datafield tag="720" ind1=" " ind2=" ">
    <subfield code="a">Papantonopoulos, Eleftherios</subfield>
  </datafield>
  <datafield tag="720" ind1=" " ind2=" ">
    <subfield code="a">Siopsis, George</subfield>
  </datafield>
  <datafield tag="856" ind1="4" ind2=" ">
    <subfield code="u">http://137.138.33.172/%s/92/files/0606096.pdf</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="4">
    <subfield code="c">006</subfield>
    <subfield code="p">J. High Energy Phys.</subfield>
    <subfield code="v">10</subfield>
    <subfield code="y">2006</subfield>
  </datafield>
  <datafield tag="916" ind1=" " ind2=" ">
    <subfield code="s">n</subfield>
    <subfield code="w">200624</subfield>
  </datafield>
  <datafield tag="960" ind1=" " ind2=" ">
    <subfield code="a">13</subfield>
  </datafield>
  <datafield tag="961" ind1=" " ind2=" ">
    <subfield code="c">20070425</subfield>
    <subfield code="h">1021</subfield>
    <subfield code="l">CER01</subfield>
    <subfield code="x">20060613</subfield>
  </datafield>
  <datafield tag="963" ind1=" " ind2=" ">
    <subfield code="a">PUBLIC</subfield>
  </datafield>
  <datafield tag="970" ind1=" " ind2=" ">
    <subfield code="a">002628325CER</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">ARTICLE</subfield>
  </datafield>
</record>
</collection>
""" % cfg['CFG_SITE_RECORD']
        # Restricted record in thesis collection
        self.recxml5 = """
    <?xml version="1.0" encoding="UTF-8"?>
    <collection xmlns="http://www.loc.gov/MARC21/slim">
    <record>
      <controlfield tag="001">42</controlfield>
      <datafield tag="041" ind1=" " ind2=" ">
        <subfield code="a">eng</subfield>
      </datafield>
      <datafield tag="088" ind1=" " ind2=" ">
        <subfield code="a">LBL-28106</subfield>
      </datafield>
      <datafield tag="100" ind1=" " ind2=" ">
        <subfield code="a">Bertsche, K J</subfield>
        <subfield code="u">Calif. Univ. Berkeley</subfield>
      </datafield>
      <datafield tag="245" ind1=" " ind2=" ">
        <subfield code="a">A small low energy cyclotron for radioisotope measurements</subfield>
      </datafield>
      <datafield tag="260" ind1=" " ind2=" ">
        <subfield code="a">Berkeley, CA</subfield>
        <subfield code="b">Lawrence Berkeley Nat. Lab.</subfield>
        <subfield code="c">Nov 1989</subfield>
      </datafield>
      <datafield tag="300" ind1=" " ind2=" ">
        <subfield code="a">155 p</subfield>
      </datafield>
      <datafield tag="502" ind1=" " ind2=" ">
        <subfield code="a">Thesis : Calif. Univ. Berkeley</subfield>
      </datafield>
      <datafield tag="650" ind1="1" ind2="7">
        <subfield code="2">SzGeCERN</subfield>
        <subfield code="a">Accelerators and Storage Rings</subfield>
      </datafield>
      <datafield tag="653" ind1="1" ind2=" ">
        <subfield code="a">bibliography</subfield>
      </datafield>
      <datafield tag="690" ind1="C" ind2=" ">
        <subfield code="a">REPORT</subfield>
      </datafield>
      <datafield tag="690" ind1="C" ind2=" ">
        <subfield code="a">THESIS</subfield>
      </datafield>
      <datafield tag="909" ind1="C" ind2="0">
        <subfield code="b">14</subfield>
      </datafield>
      <datafield tag="909" ind1="C" ind2="0">
        <subfield code="y">1989</subfield>
      </datafield>
      <datafield tag="909" ind1="C" ind2="1">
        <subfield code="c">1990-02-28</subfield>
        <subfield code="l">50</subfield>
        <subfield code="m">2002-03-22</subfield>
        <subfield code="o">BATCH</subfield>
      </datafield>
      <datafield tag="909" ind1="C" ind2="S">
        <subfield code="s">h</subfield>
        <subfield code="w">199010n</subfield>
      </datafield>
      <datafield tag="980" ind1=" " ind2=" ">
        <subfield code="a">THESIS</subfield>
      </datafield>
    </record>
    </collection>
    """
        self.recxml6 = """
<?xml version="1.0" encoding="UTF-8"?>
<collection xmlns="http://www.loc.gov/MARC21/slim">
<record>
  <controlfield tag="001">14</controlfield>
  <datafield tag="041" ind1=" " ind2=" ">
    <subfield code="a">eng</subfield>
  </datafield>
  <datafield tag="088" ind1=" " ind2=" ">
    <subfield code="a">CERN-PRE-82-006</subfield>
  </datafield>
  <datafield tag="100" ind1=" " ind2=" ">
    <subfield code="a">Ellis, J</subfield>
    <subfield code="u">CERN</subfield>
  </datafield>
  <datafield tag="245" ind1=" " ind2=" ">
    <subfield code="a">From the standard model to grand unification</subfield>
  </datafield>
  <datafield tag="260" ind1=" " ind2=" ">
    <subfield code="a">Geneva</subfield>
    <subfield code="b">CERN</subfield>
    <subfield code="c">1982</subfield>
  </datafield>
  <datafield tag="300" ind1=" " ind2=" ">
    <subfield code="a">mult. p</subfield>
  </datafield>
  <datafield tag="650" ind1="1" ind2="7">
    <subfield code="2">SzGeCERN</subfield>
    <subfield code="a">General Theoretical Physics</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="0">
    <subfield code="y">1982</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="0">
    <subfield code="b">11</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="0">
    <subfield code="p">TH</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="1">
    <subfield code="c">1990-01-28</subfield>
    <subfield code="l">50</subfield>
    <subfield code="m">2001-09-15</subfield>
    <subfield code="o">BATCH</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="2">
    <subfield code="f">820332</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="O">
    <subfield code="o">oai:cds.cern.ch:CERN-PRE-82-006</subfield>
    <subfield code="p">cern:theory</subfield>
  </datafield>
  <datafield tag="909" ind1="C" ind2="S">
    <subfield code="s">h</subfield>
    <subfield code="w">1982n</subfield>
  </datafield>
  <datafield tag="980" ind1=" " ind2=" ">
    <subfield code="a">PREPRINT</subfield>
  </datafield>
</record>
</collection>
        """
        return

    def test_check_existing(self):
        """bibmatch - check existing record"""
        # Non-fuzzy searching will not find it
        records = create_records(self.recxml4)
        [nonmatchedrecs, dummy1, dummy2, dummy3] = match_records(records, \
                                                                 verbose=0, \
                                                                 fuzzy=False)
        self.assertEqual(1, len(nonmatchedrecs))

        # Fuzzy searching should find it
        records = create_records(self.recxml4)
        [dummy1, matchedrecs, dummy2, dummy3] = match_records(records, \
                                                              verbose=0, \
                                                              fuzzy=True)
        self.assertEqual(1, len(matchedrecs))

        # Check that searches returning more results are properly validated
        # This search should return 4 hits, but only real 1 match.
        records = create_records(self.recxml6)
        [dummy1, matchedrecs, dummy2, dummy3] = match_records(records, \
                                                              verbose=0)
        self.assertEqual(1, len(matchedrecs))

    def test_check_new(self):
        """bibmatch - check a new record"""
        records = create_records(self.recxml2)
        [newrecs, dummy1, dummy2, dummy3] = match_records(records, \
                                                          verbose=0)
        self.assertEqual(1, len(newrecs))

    def test_check_ambiguous(self):
        """bibmatch - check an ambiguous record"""
        records = create_records(self.recxml3)
        [dummy1, dummy2, ambigrecs, dummy3] = match_records(records, \
                                                            verbose=0)
        self.assertEqual(1, len(ambigrecs))

    def test_check_fuzzy(self):
        """bibmatch - check fuzzily matched record"""
        records = create_records(self.recxml1)
        [dummy1, dummy2, dummy3, fuzzyrecs] = match_records(records, \
                                                            verbose=0)
        self.assertEqual(1, len(fuzzyrecs))

    def test_check_remote(self):
        """bibmatch - check remote match (Invenio demo site)"""
        records = create_records(self.recxml6)
        [dummy1, matchedrecs, dummy3, dummy4] = match_records(records, \
                                                              server_url="http://invenio-demo.cern.ch", \
                                                              verbose=0)
        self.assertEqual(1, len(matchedrecs))

    def test_check_textmarc(self):
        """bibmatch - check textmarc as input"""
        from invenio.legacy.bibmatch.engine import transform_input_to_marcxml
        marcxml = transform_input_to_marcxml("", self.textmarc)
        records = create_records(marcxml)
        [dummy1, matchedrecs, dummy3, dummy4] = match_records(records, \
                                                              verbose=0)
        self.assertEqual(2, len(matchedrecs))

    def test_check_altered(self):
        """bibmatch - check altered match"""
        from invenio.legacy.bibrecord import record_has_field
        records = create_records(self.recxml4)
        self.assertTrue(not record_has_field(records[0][0], '001'))
        [dummy1, matchedrecs, dummy3, dummy4] = match_records(records, \
                                                              modify=1, \
                                                              verbose=0)
        self.assertTrue(record_has_field(matchedrecs[0][0], '001'))

    def test_check_qrystr(self):
        """bibmatch - check querystrings"""
        from invenio.legacy.bibmatch.engine import Querystring
        operator = "and"
        qrystr_old = "title||author"
        qrystr_new = "[title] %s [author]" % (operator,)
        querystring = Querystring(operator)
        records = create_records(self.recxml3)
        old_query = querystring.create_query(records[0], qrystr_old)
        new_query = querystring.create_query(records[0], qrystr_new)
        self.assertEqual(old_query, new_query)

    def test_check_collection(self):
        """bibmatch - check collection"""
        records = create_records(self.recxml4)
        [nomatchrecs, dummy1, dummy2, dummy3] = match_records(records, \
                                                              collections=["Books"], \
                                                              verbose=0)
        self.assertEqual(1, len(nomatchrecs))
        [dummy1, matchedrecs, dummy2, dummy3] = match_records(records, \
                                                              collections=["Articles"], \
                                                              verbose=0)
        self.assertEqual(1, len(matchedrecs))

    def test_restricted_collections_local(self):
        """bibmatch - check restricted collections local search"""
        records = create_records(self.recxml5)
        # Should not have access
        [nomatchrecs, dummy1, dummy2, dummy3] = match_records(records, \
                                                              qrystrs=[("", "[088__a]")], \
                                                              collections=["Theses"], \
                                                              verbose=0)
        self.assertEqual(1, len(nomatchrecs))

        # Jekyll should have access
        [dummy1, matchedrecs, dummy2, dummy3] = match_records(records, \
                                                              qrystrs=[("", "[088__a]")], \
                                                              collections=["Theses"], \
                                                              user="jekyll",
                                                              password="j123ekyll", \
                                                              verbose=0)
        self.assertEqual(1, len(matchedrecs))

    def test_restricted_collections_remote(self):
        """bibmatch - check restricted collections remote search"""
        records = create_records(self.recxml5)
        # Jekyll should have access
        [dummy1, matchedrecs, dummy2, dummy3] = match_records(records, \
                                                              qrystrs=[("", "[088__a]")], \
                                                              collections=["Theses"], \
                                                              server_url="https://invenio-demo.cern.ch", \
                                                              user  ="jekyll", \
                                                              password="j123ekyll",
                                                              verbose=0)
        self.assertEqual(1, len(matchedrecs))
        # Hyde should not have access
        [nomatchrecs, dummy1, dummy2, dummy3] = match_records(records, \
                                                              qrystrs=[("", "[088__a]")], \
                                                              collections=["Theses"], \
                                                              server_url="https://invenio-demo.cern.ch", \
                                                              user="hyde", \
                                                              password="h123yde",
                                                              verbose=0)
        self.assertEqual(1, len(nomatchrecs))

TEST_SUITE = make_test_suite(BibMatchTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
