# -*- coding: utf-8 -*-
##
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


from invenio.testsuite import make_test_suite, run_test_suite, InvenioTestCase


class TestWebDepositAPI(InvenioTestCase):
    def clear_tables(self):
        from invenio.modules.workflows.models import Workflow, WfeObject
        from invenio.sqlalchemyutils import db

        Workflow.query.delete()
        WfeObject.query.delete()
        db.session.commit()

    def setUp(self):
        from random import randint
        from invenio.modules.apikeys import create_new_web_api_key, \
            get_available_web_api_keys
        #FIXME unknown import 'deposition_metadata'
        from invenio.modules.deposit.loader import deposition_metadata
        # self.clear_tables()

        create_new_web_api_key(1, key_description='webdeposit_api_testing')
        keys = get_available_web_api_keys(1)
        self.apikey = keys[0].id

        # Test random deposition
        self.deposition = deposition_metadata.keys()[randint(0, len(deposition_metadata.keys()) - 1)]
        super(TestWebDepositAPI, self).setUp()

    def tearDown(self):
        # self.clear_tables()
        super(TestWebDepositAPI, self).tearDown()

    def test_create(self):
        from flask import current_app, url_for
        from invenio.modules.apikeys import build_web_request

        url = url_for('webdeposit_api.deposition_create',
                      deposition_types=self.deposition)

        url_create = build_web_request(url, api_key=self.apikey,
                                       timestamp=False)
        with current_app.test_client() as c:
            response = c.get(url_create)

            self.assert200(response)

            assert "uuid" in response.json

    def test_json_get_set_functions(self):
        import json
        from flask import current_app, url_for
        from invenio.modules.deposit.loader import \
            deposition_metadata
        from invenio.webdeposit_utils import create_workflow
        from wtforms import TextAreaField
        from invenio.modules.deposit import forms
        from invenio.modules.apikeys import build_web_request

        self.uuid = create_workflow(self.deposition, user_id=1).get_uuid()

        # Get form from deposition
        for fun in deposition_metadata[self.deposition]['workflow']:
            if fun.func_name == 'render':
                form_type = fun.__form_type__

        form = forms[form_type]()

        # Insert form data
        form_data = {}
        for field in form:
            if isinstance(field, TextAreaField):
                form_data[field.name] = 'testing webdeposit API'

        data = {'form_data': json.dumps(form_data),
                'uuid': self.uuid}
        url = url_for('webdeposit_api.json_set',
                      deposition_metadata=self.deposition)
        url_set = build_web_request(url, {},
                                    uid=1, api_key=self.apikey,
                                    timestamp=False)
        with current_app.test_client() as c:
            response = c.post(url_set, data=data)
            assert response._status_code == 200

            url = url_for('webdeposit_api.json_get', deposition_metadata=self.deposition)
            url_get = build_web_request(url, {'uuid':
                                        self.uuid},
                                        uid=1, api_key=self.apikey,
                                        timestamp=False)
            response = c.get(url_get)
            assert response._status_code == 200

            for field in form:
                if isinstance(field, TextAreaField):
                    assert response.json[field.name] == 'testing webdeposit API'

TEST_SUITE = make_test_suite(TestWebDepositAPI)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
