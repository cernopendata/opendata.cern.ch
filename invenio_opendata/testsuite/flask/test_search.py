# -*- coding: utf-8 -*-
#
## This file is part of Invenio.
## Copyright (C) 2012, 2013 CERN.
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

from fixture import SQLAlchemyFixture
from invenio.ext.sqlalchemy import db
from invenio.testsuite import make_flask_test_suite, run_test_suite, \
    FlaskSQLAlchemyTest, InvenioFixture
from invenio.websearch_fixtures import CollectionData, \
    CollectionCollectionData, ExternalcollectionData


def fixture_builder():
    from invenio.modules.accounts.models import User, Usergroup, UserUsergroup
    from invenio.modules.search.models import Collection, CollectionCollection, \
        Externalcollection

    return SQLAlchemyFixture(env={'UserData': User,
                                  'UsergroupData': Usergroup,
                                  'UserUsergroupData': UserUsergroup,
                                  'CollectionData': Collection,
                                  'ExternalcollectionData': Externalcollection,
                                  'CollectionCollectionData':
                                  CollectionCollection},
                             engine=db.metadata.bind,
                             session=db.session)

fixture = InvenioFixture(fixture_builder)


def p(c, level=0):
    if c:
        print ' ' * level, '- ', c.name
        for i in c.collection_children:
            p(i, level+1)


class WebSearchCollectionTest(FlaskSQLAlchemyTest):

    @fixture.with_data(ExternalcollectionData, CollectionData,
                       CollectionCollectionData)
    def test_loading_collection_tree(data, self):
        from invenio.modules.search.models import Collection
        print
        p(Collection.query.order_by(Collection.id).first())
        print

    @fixture.with_data(ExternalcollectionData, CollectionData)
    def test_external_collection(data, self):
        from invenio.modules.search.models import Collection
        print
        print '----# EXTERNAL COLLECTIONS ----'
        for c in Collection.query.all():
            print c.name, ': ',
            print len([a for a in c._externalcollections])
        print '-------------------------------'
        print 'Total: ', sum(map(len, [c._externalcollections for c in
                                       Collection.query.all()]))


TEST_SUITE = make_flask_test_suite(WebSearchCollectionTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
