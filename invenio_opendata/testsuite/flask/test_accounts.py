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

from invenio.ext.sqlalchemy import db
from invenio.ext.login import current_user, login_user, logout_user
from invenio.testsuite import make_flask_test_suite, run_test_suite, \
    FlaskSQLAlchemyTest, InvenioFixture
from fixture import SQLAlchemyFixture
from invenio.webaccount_fixtures import UserData, UsergroupData, \
    UserUsergroupData


def fixture_builder():
    from invenio.modules.accounts.models import User, Usergroup, UserUsergroup
    return SQLAlchemyFixture(env={'UserData': User, 'UsergroupData': Usergroup,
                                  'UserUsergroupData': UserUsergroup},
                             engine=db.metadata.bind,
                             session=db.session)

fixture = InvenioFixture(fixture_builder)


class WebAccountTest(FlaskSQLAlchemyTest):

    @fixture.with_data(UserData)
    def test_low_level_login(data, self):
        users = data.UserData

        assert current_user.is_guest
        login_user(users.admin.id)
        assert current_user.get_id() == users.admin.id
        logout_user()
        assert current_user.get_id() != users.admin.id
        assert current_user.is_guest
        login_user(users.romeo.id)
        assert not current_user.is_guest
        assert current_user.get_id() == users.romeo.id
        login_user(users.admin.id)
        assert current_user.get_id() == users.admin.id
        logout_user()

    @fixture.with_data(UserData)
    def test_login(data, self):
        users = data.UserData

        # Valid credentials.
        for name, u in users:
            response = self.login(u.nickname, u.password)
            assert u.nickname in response.data
            self.logout()

        # Valid credentials using email.
        for name, u in users:
            response = self.login(u.email, u.password)
            assert u.nickname in response.data
            self.logout()

        # Empty form should not work.
        response = self.login('', '')
        assert 'logout' not in response.data
        # Not existing user.
        response = self.login('NOT EXISTS', '')
        assert 'logout' not in response.data
        # Existing password with not existing user name.
        response = self.login('NOT EXISTS', users.romeo.password)
        assert 'logout' not in response.data
        # Invalid password for admin.
        response = self.login(users.admin.nickname, 'FAIL')
        assert 'logout' not in response.data

    @fixture.with_data(UserData)
    def test_change_password(data, self):
        from invenio.modules.accounts.models import User
        NEW_PASSWORD = 'admin'
        users = data.UserData

        response = self.login(users.admin.nickname, users.admin.password)
        assert users.admin.nickname in response.data
        self.logout()

        admin = User.query.filter(User.id == users.admin.id).one()
        admin.password = NEW_PASSWORD
        db.session.merge(admin)
        db.session.commit()

        new_passwd = db.session.query(User.password).filter(User.id == users.admin.id).one()
        assert users.admin.password != new_passwd

        # Invalid password for admin.
        response = self.login(users.admin.nickname, users.admin.password)
        assert 'logout' not in response.data

        # Valid credentials.
        response = self.login(users.admin.nickname, NEW_PASSWORD)
        assert users.admin.nickname in response.data
        self.logout()


class UserGroupTest(FlaskSQLAlchemyTest):

    @fixture.with_data(UserData, UsergroupData, UserUsergroupData)
    def test_group_relation_consistency(data, self):
        from invenio.modules.accounts.models import User, Usergroup
        orig_len = len(dict(data.UserUsergroupData))
        user_len = sum(len(u.usergroups) for u in User.query.all())
        ugrp_len = sum(len(g.users) for g in Usergroup.query.all())

        assert orig_len == user_len
        assert user_len == ugrp_len


TEST_SUITE = make_flask_test_suite(WebAccountTest, UserGroupTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
