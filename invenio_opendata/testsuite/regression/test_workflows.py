# -*- coding: utf-8 -*-
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

"""
BibWorkflow Unit tests - functions to test workflows
"""

from invenio.ext.sqlalchemy import db
from invenio.testsuite import (make_test_suite,
                               run_test_suite,
                               InvenioTestCase)
from invenio.modules.workflows.config import CFG_OBJECT_VERSION


class TestWorkflowStart(InvenioTestCase):
    """Tests for BibWorkflow API."""

    def setUp(self):
        self.test_data = {}
        self.id_workflows = []
        self.recxml = """<?xml version="1.0" encoding="UTF-8"?>
<OAI-PMH xmlns="http://www.openarchives.org/OAI/2.0/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.openarchives.org/OAI/2.0/ http://www.openarchives.org/OAI/2.0/OAI-PMH.xsd">
<responseDate>2013-04-03T13:56:49Z</responseDate>
<request verb="ListRecords" from="2013-03-25" metadataPrefix="arXiv" set="physics:astro-ph">http://export.arxiv.org/oai2</request>
<ListRecords>
<record>
<header>
 <identifier>oai:arXiv.org:0801.3931</identifier>
 <datestamp>2013-03-26</datestamp>
 <setSpec>physics:astro-ph</setSpec>
</header>
<metadata>
 <arXiv xmlns="http://arxiv.org/OAI/arXiv/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://arxiv.org/OAI/arXiv/ http://arxiv.org/OAI/arXiv.xsd">
 <id>0801.3931</id><created>2008-01-25</created><authors><author><keyname>Manos</keyname><forenames>T.</forenames></author><author><keyname>Athanassoula</keyname><forenames>E.</forenames></author></authors><title>Dynamical study of 2D and 3D barred galaxy models</title><categories>astro-ph</categories><comments>8 pages, 3 figures, to appear in the proceedings of the international
  conference &quot;Chaos in Astronomy&quot;, Athens, Greece (talk contribution)</comments><journal-ref>Chaos in Astronomy Astrophysics and Space Science Proceedings
  2009, pp 115-122</journal-ref><doi>10.1007/978-3-540-75826-6_11</doi><abstract>  We study the dynamics of 2D and 3D barred galaxy analytical models, focusing
on the distinction between regular and chaotic orbits with the help of the
Smaller ALigment Index (SALI), a very powerful tool for this kind of problems.
We present briefly the method and we calculate the fraction of chaotic and
regular orbits in several cases. In the 2D model, taking initial conditions on
a Poincar\'{e} $(y,p_y)$ surface of section, we determine the fraction of
regular and chaotic orbits. In the 3D model, choosing initial conditions on a
cartesian grid in a region of the $(x, z, p_y)$ space, which in coordinate
space covers the inner disc, we find how the fraction of regular orbits changes
as a function of the Jacobi constant. Finally, we outline that regions near the
$(x,y)$ plane are populated mainly by regular orbits. The same is true for
regions that lie either near to the galactic center, or at larger relatively
distances from it.
</abstract></arXiv>
</metadata>
</record>
</ListRecords>
</OAI-PMH>
"""

    def tearDown(self):
        """ Clean up created objects """
        from invenio.modules.workflows.models import (BibWorkflowObject,
                                                      Workflow,
                                                      BibWorkflowEngineLog,
                                                      BibWorkflowObjectLog)
        from invenio.modules.workflows.utils import get_redis_keys, set_up_redis

        workflows = Workflow.get(Workflow.module_name == "unit_tests").all()
        for workflow in workflows:
            BibWorkflowObject.query.filter(
                BibWorkflowObject.id_workflow == workflow.uuid
            ).delete()

            objects = BibWorkflowObjectLog.query.filter(
                BibWorkflowObject.id_workflow == workflow.uuid
            ).all()
            for obj in objects:
                db.session.delete(obj)
            db.session.delete(workflow)

            objects = BibWorkflowObjectLog.query.filter(
                BibWorkflowObject.id_workflow == workflow.uuid
            ).all()
            for obj in objects:
                BibWorkflowObjectLog.delete(id=obj.id)
            BibWorkflowEngineLog.delete(uuid=workflow.uuid)
        # Deleting dumy object created in tests
        db.session.query(BibWorkflowObject).filter(
            BibWorkflowObject.id_workflow.in_([11, 123, 253])
        ).delete(synchronize_session='fetch')
        Workflow.query.filter(Workflow.module_name == "unit_tests").delete()
        db.session.commit()

        rs = set_up_redis()
        keys = get_redis_keys()
        for key in keys:
            keys2 = get_redis_keys(key)
            for key2 in keys2:
                rs.delete("holdingpen_sort:%s:%s" % (key, key2,))
            rs.delete("holdingpen_sort:%s" % (key,))
        rs.delete("holdingpen_sort")

    def test_workflow_basic_run(self):
        """Tests running workflow with one data object"""
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import start
        self.test_data = {'data': 20}
        initial_data = self.test_data
        final_data = {'data': 41}

        workflow = start(workflow_name="test_workflow",
                         data=[self.test_data], module_name="unit_tests")

        # Keep id for cleanup after
        self.id_workflows.append(workflow.uuid)

        # Get parent object of the workflow we just ran
        initial_object = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid,
            BibWorkflowObject.id_parent == None)  # noqa E711
        all_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid)

        # There should only be 2 objects (initial, final)
        self.assertEqual(all_objects.count(), 2)
        self._check_workflow_execution(initial_object,
                                       initial_data, final_data)

    def test_workflow_complex_run(self):
        """Tests running workflow with several data objects"""
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import start

        self.test_data = [{'data': 1}, {'data': "wwww"}, {'data': 20}]
        final_data = [{'data': 19}, {'data': "wwww"}, {'data': 38}]

        workflow = start(workflow_name="test_workflow_2",
                         data=self.test_data, module_name="unit_tests")

        # Keep id for cleanup after
        self.id_workflows.append(workflow.uuid)

        # Get parent objects of the workflow we just ran
        objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid,
            BibWorkflowObject.id_parent == None)  # noqa E711

        # Let's check that we found anything.
        # There should only be three objects
        self.assertEqual(objects.count(), 3)

        all_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid)
        self.assertEqual(all_objects.count(), 6)

        for obj in objects.all():
            # The child object should have the final or halted version
            self.assertTrue(obj.child_objects[0].version
                            in (CFG_OBJECT_VERSION.FINAL,
                                CFG_OBJECT_VERSION.HALTED))
            # Making sure the final data is correct
            self.assertTrue(obj.child_objects[0].get_data()
                            in final_data)

    def test_workflow_recordxml(self):
        """Tests runnning a record ingestion workflow"""
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import start

        initial_data = self.recxml
        workflow = start(workflow_name="marcxml_workflow",
                         data=[initial_data], module_name="unit_tests")
        # Keep id for cleanup after
        self.id_workflows.append(workflow.uuid)

        # Get parent object of the workflow we just ran
        objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid,
            BibWorkflowObject.id_parent == None)  # noqa E711

        all_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid)
        self.assertEqual(all_objects.count(), 2)

        self._check_workflow_execution(objects,
                                       initial_data, None)

    def test_workflow_for_halted_object(self):
        """Test starting workflow with halted object given"""
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import start_by_oids
        initial_data = {'data': 1}
        obj_init = BibWorkflowObject(id_workflow=123,
                                     version=CFG_OBJECT_VERSION.INITIAL)
        obj_init.set_data(initial_data)
        obj_init._update_db()
        halted_data = {'data': 1}
        obj_halted = BibWorkflowObject(id_workflow=123,
                                       id_parent=obj_init.id,
                                       version=CFG_OBJECT_VERSION.HALTED)
        obj_halted.set_data(halted_data)
        obj_halted._update_db()

        workflow = start_by_oids('test_workflow',
                                 [obj_halted.id], module_name="unit_tests")

        final_data = {'data': 2}
        objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid,
            BibWorkflowObject.id_parent == None)  # noqa E711

        all_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid)
        self.assertEqual(all_objects.count(), 2)

        # Check the workflow execution
        self._check_workflow_execution(objects,
                                       halted_data,
                                       final_data)

        # Check copied INITIAL object
        self.assertEqual(obj_halted.get_data(), objects[0].get_data())

        # Check if first object were untached
        self.assertEqual(obj_init.id_workflow, "123")
        self.assertEqual(obj_halted.id_workflow, "123")

    def test_workflow_for_finished_object(self):
        """Test starting workflow with finished object given"""
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import start_by_oids
        initial_data = {'data': 20}
        obj_init = BibWorkflowObject(id_workflow=253,
                                     version=CFG_OBJECT_VERSION.INITIAL)
        obj_init.set_data(initial_data)
        obj_init._update_db()
        first_final_data = {u'data': 41}
        obj_final = BibWorkflowObject(id_workflow=253,
                                      id_parent=obj_init.id,
                                      version=CFG_OBJECT_VERSION.FINAL)
        obj_final.set_data(first_final_data)
        obj_final._update_db()

        workflow = start_by_oids('test_workflow',
                                 [obj_final.id], module_name="unit_tests")

        final_data = {u'data': 62}
        objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid,
            BibWorkflowObject.id_parent == None)  # noqa E711

        all_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid)
        self.assertEqual(all_objects.count(), 2)

        # Check the workflow execution
        self._check_workflow_execution(objects,
                                       first_final_data,
                                       final_data)

        # Check copied INITIAL object
        self.assertEqual(obj_final.get_data(), objects[0].get_data())

        # Check if first object were untached
        self.assertEqual(obj_init.id_workflow, "253")
        self.assertEqual(obj_final.id_workflow, "253")

    def test_logging_for_workflow_objects_without_workflow(self):
        """This test run a virtual object out of a workflow for
        test purpose, this object will log several things"""
        from invenio.modules.workflows.models import (BibWorkflowObject,
                                                      BibWorkflowObjectLog)

        initial_data = {'data': 20}
        obj_init = BibWorkflowObject(id_workflow=11,
                                     version=CFG_OBJECT_VERSION.INITIAL)
        obj_init.set_data(initial_data)
        obj_init._update_db()
        obj_init.save()
        obj_init.log.info("I am a test object")
        obj_init.log.error("This is an error message")
        # FIXME: loglevels are simply overwritten somewhere in Celery
        #        even if Celery is not being "used".
        #
        #        This means loglevel.DEBUG is NOT working at the moment!
        obj_init.log.debug("This is a debug message")
        obj_init._update_db()
        obj_test = BibWorkflowObjectLog.query.filter(
            BibWorkflowObjectLog.id_object == obj_init.id).all()
        messages_found = 0
        for current_obj in obj_test:
            if current_obj.message == "I am a test object" \
                    and messages_found == 0:
                messages_found += 1
            elif current_obj.message == "This is an error message" \
                    and messages_found == 1:
                messages_found += 1
            elif current_obj.message == "This is a debug message" \
                    and messages_found == 2:
                messages_found += 1
        self.assertEqual(messages_found, 2)  # FIXME: should be 3 when debug works

    def test_workflow_for_running_object(self):
        """Test starting workflow with running object given"""
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import start_by_oids
        initial_data = {'data': 20}
        obj_init = BibWorkflowObject(id_workflow=11,
                                     version=CFG_OBJECT_VERSION.INITIAL)
        obj_init.set_data(initial_data)
        obj_init._update_db()
        running_data = {'data': 26}
        obj_running = BibWorkflowObject(id_workflow=11,
                                        id_parent=obj_init.id,
                                        version=CFG_OBJECT_VERSION.RUNNING)
        obj_running.set_data(running_data)
        obj_running._update_db()
        workflow = start_by_oids('test_workflow',
                                 [obj_running.id], module_name="unit_tests")

        final_data = {u'data': 41}
        objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid,
            BibWorkflowObject.id_parent == None)  # noqa E711

        all_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid)
        self.assertEqual(all_objects.count(), 2)

        # Check the workflow execution
        self._check_workflow_execution(objects,
                                       initial_data,
                                       final_data)

        # Check copied INITIAL object
        self.assertEqual(obj_init.get_data(), objects[0].get_data())

        # Check if first object were untuched
        self.assertEqual(obj_init.id_workflow, "11")
        objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id == obj_running.id)
        self.assertEqual(objects.count(), 0)

    def test_continue_execution_for_object(self):
        """Tests continuing execution of workflow for object
        given object from prev, current and next task"""
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import (start,
                                                   continue_oid)
        initial_data = {'data': 1}
        final_data_prev = {'data': 3}
        final_data_curr = {'data': 2}
        final_data_next = {'data': 9}

        # testing restarting from previous task
        init_workflow = start("test_workflow",
                              data=[initial_data], module_name="unit_tests")

        obj_halted = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == init_workflow.uuid,
            BibWorkflowObject.version == CFG_OBJECT_VERSION.HALTED).first()

        workflow = continue_oid(oid=obj_halted.id,
                                start_point="restart_prev", module_name="unit_tests")

        new_object = BibWorkflowObject.query.filter(
            BibWorkflowObject.id == obj_halted.id)
        self.assertEqual(new_object.count(), 1)
        self.assertEqual(new_object[0].get_data(), final_data_prev)

        all_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid)
        self.assertEqual(all_objects.count(), 2)

        # testing restarting from current task
        init_workflow2 = start(workflow_name="test_workflow",
                               data=[initial_data], module_name="unit_tests")

        obj_halted2 = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == init_workflow2.uuid,
            BibWorkflowObject.version == CFG_OBJECT_VERSION.HALTED).first()
        workflow2 = continue_oid(oid=obj_halted.id,
                                 start_point="restart_task")
        object2 = BibWorkflowObject.query.filter(
            BibWorkflowObject.id == obj_halted2.id)
        self.assertEqual(object2.count(), 1)
        self.assertEqual(object2[0].get_data(), final_data_curr)

        all_objects2 = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow2.uuid)
        self.assertEqual(all_objects2.count(), 2)

        # testing continuing from next task
        init_workflow3 = start(workflow_name="test_workflow",
                               data=[initial_data], module_name="unit_tests")

        obj_halted3 = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == init_workflow3.uuid,
            BibWorkflowObject.version == CFG_OBJECT_VERSION.HALTED).first()
        workflow3 = continue_oid(oid=obj_halted3.id,
                                 start_point="continue_next", module_name="unit_tests")
        object3 = BibWorkflowObject.query.filter(
            BibWorkflowObject.id == obj_halted3.id)
        self.assertEqual(object3.count(), 1)
        self.assertEqual(object3[0].get_data(), final_data_next)

        all_objects3 = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow3.uuid)
        self.assertEqual(all_objects3.count(), 2)

    def test_restart_workflow(self):
        """Tests restarting workflow for given workflow id"""
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import (start, start_by_wid)

        initial_data = {'data': 1}

        # testing restarting from previous task
        init_workflow = start(workflow_name="test_workflow",
                              data=[initial_data], module_name="unit_tests")
        init_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == init_workflow.uuid)

        restarted_workflow = start_by_wid(wid=init_workflow.uuid, module_name="unit_tests")
        restarted_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == restarted_workflow.uuid)

        self.assertEqual(restarted_objects.count(), 1)

        self.assertEqual(restarted_objects[0].version, init_objects[1].version)
        self.assertEqual(restarted_objects[0].id_parent, init_objects[0].id)
        self.assertEqual(restarted_objects[0].get_data(), init_objects[1].get_data())

    def test_simplified_data(self):
        """Tests running workflow with simplified data."""
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import start
        self.test_data = 20
        initial_data = self.test_data
        final_data = 41

        workflow = start(workflow_name="simplified_data_test_workflow",
                         data=[self.test_data], module_name="unit_tests")

        # Keep id for cleanup after
        self.id_workflows.append(workflow.uuid)

        # Get parent object of the workflow we just ran
        # NOTE: ignore PEP8 here for None
        objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid,
            BibWorkflowObject.id_parent == None)  # noqa E711
        all_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid)
        self.assertEqual(all_objects.count(), 2)
        self._check_workflow_execution(objects,
                                       initial_data, final_data)

    def test_redis_for_halted(self):
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import start
        from invenio.modules.workflows.utils import set_up_redis
        initial_data = {'data': 1}

        workflow = start(workflow_name="test_workflow",
                         data=[initial_data], module_name="unit_tests")

        obj = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid,
            BibWorkflowObject.id_parent != None).one()

        rs = set_up_redis()
        entry1 = rs.smembers("holdingpen_sort:publisher:Desy")
        entry2 = rs.smembers("holdingpen_sort:category:lower_than_20")

        self.assertTrue(str(obj.id) in entry1)
        self.assertTrue(str(obj.id) in entry2)

    def test_redis_for_finished(self):
        pass

    def test_data_object_created_outside(self):
        from invenio.modules.workflows.models import BibWorkflowObject
        from invenio.modules.workflows.api import start

        obj = BibWorkflowObject()
        initial_data = {'data': 20}
        obj.set_data(initial_data)
        obj._update_db()

        final_data = {'data': 41}

        workflow = start(workflow_name="test_workflow",
                         data=[obj], module_name="unit_tests")
        # Keep id for cleanup after
        self.id_workflows.append(workflow.uuid)

        # Get parent object of the workflow we just ran
        initial_object = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid,
            BibWorkflowObject.id_parent == None)  # noqa E711
        all_objects = BibWorkflowObject.query.filter(
            BibWorkflowObject.id_workflow == workflow.uuid)

        # There should only be 2 objects (initial, final)
        self.assertEqual(all_objects.count(), 2)
        self.assertEqual(obj.get_data(), final_data)
        self.assertEqual(obj.version, CFG_OBJECT_VERSION.FINAL)
        self.assertEqual(obj.id_parent, initial_object[0].id)
        self.assertEqual(initial_object[0].get_data(), initial_data)


    def _check_workflow_execution(self, objects, initial_data, final_data):
        # Let's check that we found anything. There should only be one object
        self.assertEqual(objects.count(), 1)

        parent_object = objects[0]

        # The object should be the inital version
        self.assertEqual(parent_object.version, CFG_OBJECT_VERSION.INITIAL)

        # The object should have the inital data
        self.assertEqual(parent_object.get_data(), initial_data)

        # Fetch final object which should exist
        final_object = objects[0].child_objects[0]
        self.assertTrue(final_object)

        if final_data:
            # Check that final data is correct
            self.assertEqual(final_object.get_data(), final_data)


TEST_SUITE = make_test_suite(TestWorkflowStart)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE)
