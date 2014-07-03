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

"""Unit tests for REST like authentication API."""

import re
import hmac
import urllib
import time

from invenio.utils.hash import sha1
from invenio.testsuite import InvenioTestCase, make_test_suite, \
    run_test_suite


def build_web_request(path, params, api_key=None, secret_key=None):
    items = (hasattr(params, 'items') and [params.items()] or [list(params)])[0]
    if api_key:
        items.append(('apikey', api_key))
    if secret_key:
        items.append(('timestamp', str(int(time.time()))))
        items = sorted(items, key=lambda x: x[0].lower())
        url = '%s?%s' % (path, urllib.urlencode(items))
        signature = hmac.new(secret_key, url, sha1).hexdigest()
        items.append(('signature', signature))
    if not items:
        return path
    return '%s?%s' % (path, urllib.urlencode(items))


class APIKeyTest(InvenioTestCase):
    """ Test functions related to the REST authentication API """
    def setUp(self):
        from invenio.modules import apikeys as web_api_key
        from invenio.modules.accounts.models import User
        from invenio.modules.apikeys.models import WebAPIKey
        self.model = WebAPIKey
        self.web_api_key = web_api_key
        self.web_api_key.CFG_WEB_API_KEY_ALLOWED_URL = [('/search\?*', 0, True),
                                                        ('/bad\?*', -1, True)]  # Just for testing

        self.web_api_key._CFG_WEB_API_KEY_ALLOWED_URL = \
            [(re.compile(_url), _authorized_time,
             _need_timestamp) for _url, _authorized_time, _need_timestamp in
             self.web_api_key.CFG_WEB_API_KEY_ALLOWED_URL]
        self.model.query.delete()
        self.id_admin = User.query.filter_by(nickname='admin').one().id

    def tearDown(self):
        self.model.query.delete()

    def test_create_remove_show_key(self):
        """apikey - create/list/delete REST key"""

        self.assertEqual(0, len(self.web_api_key.show_web_api_keys(uid=self.id_admin)))

        self.web_api_key.create_new_web_api_key(self.id_admin, "Test key I")
        self.web_api_key.create_new_web_api_key(self.id_admin, "Test key II")
        self.web_api_key.create_new_web_api_key(self.id_admin, "Test key III")
        self.web_api_key.create_new_web_api_key(self.id_admin, "Test key IV")
        self.web_api_key.create_new_web_api_key(self.id_admin, "Test key V")

        self.assertEqual(5, len(self.web_api_key.show_web_api_keys(uid=self.id_admin)))
        self.assertEqual(5, len(self.web_api_key.show_web_api_keys(uid=self.id_admin, diff_status='')))

        keys_info = self.web_api_key.show_web_api_keys(uid=self.id_admin)
        self.web_api_key.mark_web_api_key_as_removed(keys_info[0].id)

        self.assertEqual(4, len(self.web_api_key.show_web_api_keys(uid=self.id_admin)))
        self.assertEqual(5, len(self.web_api_key.show_web_api_keys(uid=self.id_admin, diff_status='')))

        self.model.mark_as(keys_info[1].id,
                           self.model.CFG_WEB_API_KEY_STATUS['WARNING'])
        self.model.mark_as(keys_info[2].id,
                           self.model.CFG_WEB_API_KEY_STATUS['REVOKED'])

        self.assertEqual(4, len(self.web_api_key.show_web_api_keys(uid=self.id_admin)))
        self.assertEqual(5, len(self.web_api_key.show_web_api_keys(uid=self.id_admin, diff_status='')))

    def test_acc_get_uid_from_request(self):
        """webapikey - Login user from request using REST key"""
        from flask import current_app
        path = '/search'
        params = 'ln=es&sc=1&c=Articles & Preprints&action_search=Buscar&p=ellis'

        self.assertEqual(0, len(self.web_api_key.show_web_api_keys(uid=self.id_admin)))
        self.web_api_key.create_new_web_api_key(self.id_admin, "Test key I")

        key_info = self.model.query.filter_by(id_user=self.id_admin).all()
        url = self.web_api_key.build_web_request(path, params,
                                                 api_key=key_info[0].id)
        with current_app.test_client() as client:
            client.get(url, follow_redirects=True)
            uid = self.web_api_key.acc_get_uid_from_request()
        self.assertEqual(uid, self.id_admin)

        url = self.web_api_key.build_web_request(path, params, api_key=key_info[0].id)
        url += "123"  # corrupt the key
        with current_app.test_client() as client:
            client.get(url, follow_redirects=True)
            uid = self.web_api_key.acc_get_uid_from_request()
        self.assertEqual(uid, -1)

        path = '/bad'
        self.client.get(path, follow_redirects=True)
        uid = self.web_api_key.acc_get_uid_from_request()
        self.assertEqual(uid, -1)

        params = {'nocache': 'yes', 'limit': 123}
        with current_app.test_client() as client:
            url = self.web_api_key.build_web_request(path, params,
                                                     api_key=key_info[0].id)
            client.get(path, follow_redirects=True)
        uid = self.web_api_key.acc_get_uid_from_request()
        self.assertEqual(uid, -1)


TEST_SUITE = make_test_suite(APIKeyTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
