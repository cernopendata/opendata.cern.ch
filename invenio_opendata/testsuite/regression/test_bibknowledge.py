# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2009, 2010, 2011, 2012, 2013 CERN.
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

"""Regression tests for BibKnowledge."""

from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.testsuite import InvenioTestCase, make_test_suite, \
    run_test_suite, test_web_page_content


class BibknowledgeRegressionTests(InvenioTestCase):
    """Regression test functions for bibknowledge."""

    def _randomstring(self):
        """Produce a random 62-character alphanumeric string."""
        from random import shuffle
        sl = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        shuffle(sl)
        return ''.join(sl)

    def _name_a_db(self):
        return "unittest_dynamic_kb_"+self._randomstring()

    def setUp(self):
        """bibknowledge test setup

        Mostly just creates the dynamic kb used later.
        """
        from invenio.modules.knowledge.api import add_dynamic_kb, get_kb_name
        new_kb_id = add_dynamic_kb(self._name_a_db(), "100__a", searchwith="245__:*%*")
        self.dyn_kbname = get_kb_name(new_kb_id)

    def test_kb_pages_available(self):
        """bibknowledge - test /kb page availability"""
        kbpage = cfg['CFG_SITE_URL']+"/kb"
        errs = test_web_page_content(kbpage)
        self.assertEqual([], errs)

    def test_kb_pages_curator_can_read(self):
        """bibknowledge - test that balthasar from the curator group can read page"""
        kbpage = cfg['CFG_SITE_URL']+"/kb"
        errs = test_web_page_content(kbpage, username="balthasar",
                                     password="b123althasar",
                                     expected_text="BibKnowledge Admin")
        self.assertEqual([], errs)

    def test_EJOURNALS_exists(self):
        """bibknowledge - test that EJOURNALS kb is there"""
        from invenio.modules.knowledge.api import kb_exists
        isthere = kb_exists("EJOURNALS")
        self.assertEqual(True, isthere)

    def test_kbs_info(self):
        """bibknowledge - get_kbs_info returns EJOURNALS info"""
        from invenio.modules.knowledge.api import get_kbs_info
        myinfolist = get_kbs_info("", "EJOURNALS")
        myinfo = myinfolist[0]
        self.assertEqual(myinfo["name"],"EJOURNALS")

    def test_EJOURNALS_keys(self):
        """bibknowledge - test left/right rules (key lookups)"""
        from invenio.modules.knowledge.api import get_kbr_values, get_kbr_keys
        mykeys = get_kbr_keys("EJOURNALS", "Acta")
        self.assertEqual(2, len(mykeys))
        mykeys = get_kbr_values("EJOURNALS", '', searchtype='e')
        self.assertEqual(0, len(mykeys))
        mykeys = get_kbr_values("EJOURNALS", searchtype='s')
        self.assertEqual(327, len(mykeys))
        mykeys = get_kbr_values("EJOURNALS", searchkey='', searchtype='s')
        self.assertEqual(327, len(mykeys))

    def test_EJOURNALS_values(self):
        """bibknowledge - test a left/right rule (value lookup)"""
        from invenio.modules.knowledge.api import get_kbr_values
        vals = get_kbr_values("EJOURNALS", "Astron.")
        self.assertEqual(29, len(vals))

    def test_get_EJOURNALS_kba_values(self):
        """bibknowledge - test recovering just values"""
        from invenio.modules.knowledge.api import get_kba_values
        mylist = get_kba_values("EJOURNALS")
        self.assertEqual(327, len(mylist))

    def test_EJOURNALS_export_as_json(self):
        """bibknowledge - export key-value mappings to web as json list"""
        kbpage = cfg['CFG_SITE_URL']+"/kb/export?kbname=EJOURNALS&format=jquery"
        expected = '[{"value": "AAS Photo Bull.", "label": "AAS Photo Bull."},'
        errs = test_web_page_content(kbpage, expected_text=expected)
        self.assertEqual([], errs)

    def test_EJOURNALS_get_as_json(self):
        """bibknowledge - get key-value mappings as json list"""
        from invenio.modules.knowledge.api import get_kb_mappings_json
        api_returns = get_kb_mappings_json('EJOURNALS', 'AAS', 'AAS', 's')
        expected = '[{"value": "AAS Photo Bull.", "label": "AAS Photo Bull."}]'
        self.assertEqual(expected, api_returns)

    def test_add_get_remove(self):
        """bibknowledge - test creating a kb, adding a mapping, removing it, removing kb"""
        from invenio.modules.knowledge.api import add_kb, get_kb_name, \
            kb_mapping_exists, remove_kb_mapping, delete_kb, kb_exists, \
            add_kb_mapping
        new_kb_id = add_kb()
        new_name = get_kb_name(new_kb_id)
        add_kb_mapping(new_name, "foobar", "barfoo")
        fbexists = kb_mapping_exists(new_name, "foobar")
        self.assertEqual(True, fbexists)
        remove_kb_mapping(new_name, "foobar")
        fbexists = kb_mapping_exists(new_name, "foobar")
        self.assertEqual(False, fbexists)
        delete_kb(new_name)
        still_there = kb_exists(new_name)
        self.assertEqual(False, still_there)

    def test_taxonomy(self):
        """bibknowledge - test a taxonomy (must run as bibsched user)"""
        import mechanize
        from os import remove
        from invenio.modules.knowledge.api import get_kbt_items_for_bibedit, add_kb, \
            get_kb_name, delete_kb, kb_exists
        username = "balthasar"
        password = "b123althasar"
        #create a new taxonomy kb
        new_kb_id = add_kb("testtaxonomy","taxonomy")
        #what was the name?
        new_kb_name = get_kb_name(new_kb_id)
        #get the taxonomy file
        response = mechanize.urlopen("http://invenio-software.org/download/invenio-demo-site-files/HEP.rdf")
        content = response.read()
        f = open(cfg['CFG_TMPDIR']+"/HEP.rdf","w")
        f.write(content)
        f.close()
        #upload it to the right destination, but log in first
        browser = mechanize.Browser()
        browser.open(cfg['CFG_SITE_SECURE_URL'] + "/youraccount/login")
        browser.select_form(nr=0)
        browser['nickname'] = username
        browser['password'] = password
        browser.submit()
        #go to upload page
        uploadpage = browser.open(cfg['CFG_SITE_URL']+"/kb?kb="+str(new_kb_id))
        #check that we are there
        content = uploadpage.read()
        namethere = content.count("testtaxonomy")
        assert namethere > 0
        #upload
        browser.open(cfg['CFG_SITE_URL']+"/kb?kb="+str(new_kb_id))
        browser.select_form(name="upload")
        browser.form["kb"] = str(new_kb_id) #force the id
        browser.form.add_file(open(cfg['CFG_TMPDIR']+"/HEP.rdf"), content_type='text/plain', filename="HEP.rdf", name="file")
        browser.submit()
        #check that we can get an item from the kb
        items = get_kbt_items_for_bibedit(new_kb_name, "prefLabel", "Altarelli")
        #item should contain 1 string: 'Altarelli-Parisi equation'
        self.assertEqual(1, len(items))
        #delete the temp file
        remove(cfg['CFG_TMPDIR']+"/HEP.rdf")
        #delete the test odf the DB
        delete_kb(new_kb_name)
        still_there = kb_exists(new_kb_name)
        self.assertEqual(False, still_there)

    def test_get_kbd_values(self):
        """bibknowledge - search a "find x by y" kb"""
        from invenio.modules.knowledge.api import get_kbd_values
        vals = get_kbd_values(self.dyn_kbname, "Rodentia")
        self.assertEqual(1, len(vals))
        self.assertEqual(vals[0], 'Charles Darwin')

    def test_kbd_export_as_list(self):
        """bibknowledge - export dynamic kb to web as list of values"""
        kbpage = cfg['CFG_SITE_URL']+"/kb/export?kbname="+self.dyn_kbname
        errs = test_web_page_content(kbpage, expected_text=['Charles Darwin', '李白'])
        self.assertEqual([], errs)

    def test_kbd_export_as_json(self):
        """bibknowledge - export dynamic kb to web as json list"""
        kbpage = cfg['CFG_SITE_URL']+"/kb/export?kbname="+self.dyn_kbname+'&format=jquery'
        errs = test_web_page_content(kbpage, expected_text=['["Charles Darwin",', '"\\u674e\\u767d"]'])
        self.assertEqual([], errs)

    def test_kbd_retrieval_as_json(self):
        """bibknowledge - retrieve dynamic kb as json list"""
        get_kbd_values_json = lazy_import('invenio.modules.knowledge.api:get_kbd_values_json')
        api_returns = get_kbd_values_json(self.dyn_kbname, 'Rodentia')
        expected = '["Charles Darwin"]'
        self.assertEqual(expected, api_returns)

    def test_kbd_search_as_json(self):
        """bibknowledge - search dynamic kb on web; get json hits"""
        kbpage = cfg['CFG_SITE_URL']+"/kb/export?kbname="+self.dyn_kbname+'&format=jquery&term=Rodentia'
        errs = test_web_page_content(kbpage, expected_text='["Charles Darwin"]')
        self.assertEqual([], errs)

    def test_kb_for_bibedit(self):
        """bibknowledge - test a bibedit-style *very* dynamic kb"""
        get_kbd_values_for_bibedit = lazy_import('invenio.modules.knowledge.api:get_kbd_values_for_bibedit')
        myvalues = get_kbd_values_for_bibedit("100__a", searchwith="Ellis", expression="100__a:*%*")
        self.assertEqual(1, len(myvalues))

    def test_kb_attribute_update(self):
        """bibknowledge - attribute modifications persist in database"""
        from invenio.modules.knowledge.api import update_kb_attributes, get_kb_id
        from invenio.modules.knowledge.dblayer import get_kb_description
        # NB: Tested here because with the exception of get_kb_description,
        #     these are exported by module bibknowledge. This mostly is
        #     exercising bibknowledge_dblayer, though.
        dyn_kb_oldname = self.dyn_kbname
        dyn_kb_newname = self._name_a_db()
        junk_desc      = self._randomstring()
        dyn_kb_id      = get_kb_id(dyn_kb_oldname)
        # we created it so we know it has no desc
        self.assertEqual('', get_kb_description(dyn_kb_oldname))
        # now check that we can rename it
        update_kb_attributes(dyn_kb_oldname, dyn_kb_newname)
        self.assertEqual(None, get_kb_id(dyn_kb_oldname))
        self.assertEqual(dyn_kb_id, get_kb_id(dyn_kb_newname))
        # now check that we can tag it with a description
        update_kb_attributes(dyn_kb_newname, dyn_kb_newname, junk_desc)
        self.assertEqual(junk_desc, get_kb_description(dyn_kb_newname))
        update_kb_attributes(dyn_kb_newname, dyn_kb_oldname)

    def tearDown(self):
        """bbibknowledge test cleanup"""
        from invenio.modules.knowledge.api import delete_kb
        delete_kb(self.dyn_kbname)


TEST_SUITE = make_test_suite(BibknowledgeRegressionTests)


if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
