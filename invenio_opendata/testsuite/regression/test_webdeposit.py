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

from invenio.testsuite import make_test_suite, run_test_suite, \
    InvenioTestCase, make_pdf_fixture


class TestWebDepositUtils(InvenioTestCase):

    def clear_tables(self):
        from invenio.modules.workflows.models import Workflow, BibWorkflowObject
        from invenio.ext.sqlalchemy import db

        dep_workflows = Workflow.get(
            Workflow.module_name == "webdeposit"
        ).all()
        for workflow in dep_workflows:
            BibWorkflowObject.query.filter(
                BibWorkflowObject.id_workflow == workflow.uuid
            ).delete()
        Workflow.get(Workflow.module_name == "webdeposit").delete()
        db.session.commit()

    def setUp(self):
        self.clear_tables()
        super(TestWebDepositUtils, self).setUp()

    def tearDown(self):
        self.clear_tables()
        super(TestWebDepositUtils, self).tearDown()

    #
    # Utility methods
    #
    def login_user(self, username='admin'):
        from invenio.legacy.websession_model import User
        from invenio.ext.login import login_user, current_user
        user_id = User.query.filter_by(nickname=username).one().id
        login_user(user_id)
        assert user_id == current_user.get_id()
        return user_id

    #
    # Tests
    #
    def test_deposit_files(self):
        from flask import current_app, url_for
        from invenio.modules.deposit.loader import \
            deposition_metadata
        from invenio.modules.workflows.models import Workflow
        from invenio.webdeposit_utils import create_workflow, deposit_files, \
            get_latest_or_new_workflow

        user_id = self.login_user()

        # Test for every deposition type
        for deposition_type in deposition_metadata.keys():
            workflow = create_workflow(deposition_type, user_id)
            uuid = workflow.get_uuid()

            pdffile = make_pdf_fixture("test.pdf")

            with current_app.test_request_context(
                url_for(
                    'webdeposit.upload_file', deposition_type=deposition_type,
                    uuid=uuid
                ),
                method='POST',
                data={
                    'file': pdffile,
                    'name': 'test.pdf', }):

                deposit_files(user_id, deposition_type, uuid, preingest=True)

            workflow = get_latest_or_new_workflow(deposition_type, user_id)
            workflow.run()

            draft = Workflow.get(
                Workflow.id_user == user_id, Workflow.uuid == uuid
            ).one().extra_data['drafts'][0]

            assert len(draft['form_values']['files']) == 1
            filemeta = draft['form_values']['files'][0]
            assert filemeta['name'] == 'test.pdf'
            assert filemeta['content_type'] == 'application/pdf'

    def test_workflow_creation(self):
        from invenio.modules.deposit.loader import \
            deposition_metadata
        from invenio.modules.workflows.models import Workflow
        from invenio.webdeposit_workflow import DepositionWorkflow
        from invenio.webdeposit_utils import get_latest_or_new_workflow, \
            get_workflow, delete_workflow, InvenioWebDepositNoDepositionType

        user_id = self.login_user()

        number_of_dep_types = len(deposition_metadata)
        # Test for every deposition type
        for deposition_type in deposition_metadata.keys():
            # New workflow is created
            workflow = get_latest_or_new_workflow(deposition_type,
                                                  user_id=user_id)
            self.assertTrue(workflow is not None)
            # The just created workflow is retrieved as latest
            workflow2 = get_latest_or_new_workflow(deposition_type,
                                                   user_id=user_id)
            self.assertTrue(workflow2 is not None)

            self.assertEqual(str(workflow2.uuid), str(workflow.uuid))

            # and also retrieved with its uuid
            workflow = get_workflow(workflow.uuid, deposition_type)
            self.assertTrue(workflow is not None)

        # Test get_workflow function with random arguments
        deposition_type = deposition_metadata.keys()[-1]
        workflow = get_workflow('some_uuid_that_doesnt_exist', deposition_type)
        self.assertTrue(workflow is None)

        # Create workflow without using webdeposit_utils
        workflow = DepositionWorkflow(deposition_type=deposition_type,
                                      user_id=1)

        self.assertRaises(InvenioWebDepositNoDepositionType,
                          get_workflow, workflow.get_uuid(),
                          'deposition_type_that_doesnt_exist')

        # Test that the retrieved workflow is the same and not None
        workflow2 = get_workflow(workflow.get_uuid(), deposition_type)
        self.assertTrue(workflow2 is not None)
        self.assertEqual(workflow2.get_uuid(), workflow.get_uuid())

        # Check the number of created workflows
        count_workflows = Workflow.get(
            Workflow.module_name == "webdeposit"
        ).count()
        self.assertEqual(count_workflows, number_of_dep_types + 1)

        uuid = workflow.get_uuid()
        delete_workflow(1, uuid)

        workflow = get_workflow(uuid, deposition_type)
        self.assertTrue(workflow is None)

    def test_form_functions(self):
        from invenio.modules.deposit.loader import \
            deposition_metadata
        from invenio.modules.deposit import forms
        from invenio.webdeposit_workflow import DepositionWorkflow
        from invenio.webdeposit_utils import get_form, \
            get_form_status, set_form_status, CFG_DRAFT_STATUS
        from invenio.modules.workflows.models import Workflow

        for metadata in deposition_metadata.values():
            for wf_function in metadata['workflow']:
                if 'render_form' == wf_function.func_name:
                    break

        user_id = self.login_user()

        deposition_workflow = DepositionWorkflow(deposition_type='Article',
                                                 user_id=user_id)

        uuid = deposition_workflow.get_uuid()

        # Run the workflow to insert a form in the db
        deposition_workflow.run()

        # There is only one form in the db
        workflows = Workflow.get(module_name='webdeposit')
        assert len(workflows.all()) == 1
        assert len(workflows[0].extra_data['drafts']) == 1

        # Test that guest user doesn't have access to the form
        form = get_form(0, uuid=uuid)
        assert form is None

        # Test that the current form has the right type
        form = get_form(user_id, uuid=deposition_workflow.get_uuid())
        assert isinstance(form, forms['ArticleForm'])
        assert str(uuid) == str(deposition_workflow.get_uuid())

        # Test that form is returned with get_form function
        form = get_form(user_id, deposition_workflow.get_uuid())
        assert form is not None

        form = get_form(user_id, deposition_workflow.get_uuid(), step=0)
        assert form is not None

        # Second step doesn't have a form
        form = get_form(user_id, deposition_workflow.get_uuid(), step=1)
        assert form is None

        form_status = get_form_status(user_id, deposition_workflow.get_uuid())
        assert form_status == CFG_DRAFT_STATUS['unfinished']

        form_status = get_form_status(user_id, deposition_workflow.get_uuid(),
                                      step=2)
        assert form_status is None

        set_form_status(user_id, uuid, CFG_DRAFT_STATUS['finished'])
        form_status = get_form_status(user_id, deposition_workflow.get_uuid())
        assert form_status == CFG_DRAFT_STATUS['finished']

    def test_field_functions(self):
        from invenio.webdeposit_workflow import DepositionWorkflow
        from invenio.webdeposit_utils import draft_field_get, draft_field_set

        user_id = self.login_user()
        workflow = DepositionWorkflow(deposition_type='Article',
                                      user_id=user_id)

        workflow.run()  # Insert a form
        uuid = workflow.get_uuid()

        # Test for a field that's not there
        value = draft_field_get(user_id, uuid, 'field_that_doesnt_exist')
        self.assertTrue(value is None)

        # Test for a field that hasn't been inserted in db yet
        value = draft_field_get(user_id, uuid, 'publisher')
        self.assertTrue(value is None)

        draft_field_set(user_id, uuid, 'publisher',
                        'Test Publishers Association')

        value = draft_field_get(user_id, uuid, 'publisher')
        self.assertTrue(value is 'Test Publishers Association')

    def test_record_creation(self):
        import os
        from wtforms import TextAreaField
        from datetime import datetime

        from invenio.legacy.search_engine import record_exists
        from invenio.cache import cache
        from invenio.config import CFG_PREFIX
        from invenio.modules.workflows.models import Workflow
        from invenio.modules.workflows.config import CFG_WORKFLOW_STATUS
        from invenio.modules.scheduler.models import SchTASK

        from invenio.webdeposit_utils import get_form, create_workflow, \
            set_form_status, CFG_DRAFT_STATUS
        from invenio.modules.deposit.loader import \
            deposition_metadata
        from invenio.webdeposit_workflow_utils import \
            create_record_from_marc
        from invenio.modules.record.api import get_record

        user_id = self.login_user()
        for deposition_type in deposition_metadata.keys():

            deposition = create_workflow(deposition_type, user_id)
            assert deposition is not None

            # Check if deposition creates a record
            create_rec = create_record_from_marc()
            function_exists = False
            for workflow_function in deposition.workflow:
                if create_rec.func_code == workflow_function .func_code:
                    function_exists = True
            if not function_exists:
                # if a record is not created,
                #continue with the next deposition
                continue

            uuid = deposition.get_uuid()

            cache.delete_many("1:current_deposition_type", "1:current_uuid")
            cache.add("1:current_deposition_type", deposition_type)
            cache.add("1:current_uuid", uuid)

            # Run the workflow
            deposition.run()

            # Create form's json based on the field name
            form = get_form(user_id, uuid=uuid)
            webdeposit_json = {}

            # Fill the json with dummy data
            for field in form:
                if isinstance(field, TextAreaField):
                    # If the field is associated with a marc field
                    if field.has_recjson_key() or field.has_cook_function():
                        webdeposit_json[field.name] = "test " + field.name

            draft = dict(form_type=form.__class__.__name__,
                         form_values=webdeposit_json,
                         step=0,  # dummy step
                         status=CFG_DRAFT_STATUS['finished'],
                         timestamp=str(datetime.now()))

            # Add a draft for the first step
            Workflow.set_extra_data(user_id=user_id, uuid=uuid,
                                    key='drafts', value={0: draft})

            workflow_status = CFG_WORKFLOW_STATUS.RUNNING
            while workflow_status != CFG_WORKFLOW_STATUS.COMPLETED:
                # Continue workflow
                deposition.run()
                set_form_status(user_id, uuid, CFG_DRAFT_STATUS['finished'])
                workflow_status = deposition.get_status()

            # Workflow is finished. Test if record is created
            recid = deposition.get_data('recid')
            assert recid is not None
            # Test that record id exists
            assert record_exists(recid) == 1

            # Test that the task exists
            task_id = deposition.get_data('task_id')
            assert task_id is not None

            bibtask = SchTASK.query.filter(SchTASK.id == task_id).first()
            assert bibtask is not None

            # Run bibupload, bibindex, webcoll manually
            cmd = "%s/bin/bibupload %s" % (CFG_PREFIX, task_id)
            assert not os.system(cmd)
            rec = get_record(recid)
            marc = rec.legacy_export_as_marc()
            for field in form:
                if isinstance(field, TextAreaField):
                    # If the field is associated with a marc field
                    if field.has_recjson_key() or field.has_cook_function():
                        assert "test " + field.name in marc


TEST_SUITE = make_test_suite(TestWebDepositUtils)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
