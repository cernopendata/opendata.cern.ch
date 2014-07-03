# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
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

"""WebTag Regression Tests"""

from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.ext.sqlalchemy import db
from invenio.testsuite import \
    InvenioTestCase, \
    make_test_suite, \
    run_test_suite
from mechanize import Browser

models = lazy_import('invenio.modules.tags.models')


class WebTagDeletionTest(InvenioTestCase):
    """Check if deleting w WtgTAG clears all associations"""
    def test_record_association_deletion(self):
        """webtag - are WtgTAGRecord rows deleted when WtgTAG is deleted?"""

        # (1) Create a new tag
        new_tag = models.WtgTAG()
        new_tag.id_user = 1
        new_tag.name = 'test record association deletion'
        db.session.add(new_tag)
        db.session.commit()
        db.session.refresh(new_tag)

        new_tag_id = new_tag.id

        # (2) Create the associations
        for recid in range(1, 5):
            new_association = models.WtgTAGRecord()
            new_association.tag = new_tag
            new_association.id_bibrec = recid
            db.session.add(new_association)

        db.session.commit()

        # (3) Delete the tag
        db.session.delete(new_tag)
        db.session.commit()

        # (4) Are there any associations left?
        associations_left = models.WtgTAGRecord.query\
            .filter_by(id_tag=new_tag_id)\
            .count()

        self.assertEqual(0, associations_left)


class WebTagUserSettingsTest(InvenioTestCase):
    """Check if the preferences for WebTag are editable and properly saved"""

    def login(self, username, password):
        browser = Browser()
        browser.open(cfg['CFG_SITE_SECURE_URL'] + "/youraccount/login/")
        browser.select_form(nr=0)
        browser['nickname'] = username
        browser['password'] = password

        try:
            browser.submit()
        except Exception:
            self.fail("Cannot login with nickname={name} password={pw}."\
                .format(name=username, pw=password))

        return browser

    def test_preferences_edition(self):
        browser = self.login('admin', '')

        browser.open(cfg['CFG_SITE_SECURE_URL'] + "/youraccount/edit/WebTagSettings")
        browser.select_form(nr=0)
        browser.form.find_control(name='display_tags_public').items[0].selected = False
        browser.submit()

        browser.open(cfg['CFG_SITE_SECURE_URL'] + "/youraccount/edit/WebTagSettings")
        browser.select_form(nr=0)

        if browser.form.find_control(name='display_tags_public').items[0].selected == False:
            self.fail("Setting 'display_tags_public' saved as False, but is still True")

        browser.form.find_control(name='display_tags_public').items[0].selected = True
        browser.submit()


# Running tests
TEST_SUITE = make_test_suite(
    WebTagDeletionTest,
    WebTagUserSettingsTest
)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
