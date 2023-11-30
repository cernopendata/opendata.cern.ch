# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Open Data Portal; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Locust file to test CERN Opendata.

Usage:

.. code-block:: console

  $ locust -f tests/locust/locustfile.py --host=http://0.0.0.0
  [2017-12-19 12:56:37,173] 127.0.0.1/INFO/locust.main: Starting web monitor \
  at *:8089
  [2017-12-19 12:56:37,175] 127.0.0.1/INFO/locust.main: Starting Locust 0.8
  ...
  $ firefox http://127.0.0.1:8089

If you need to run an specific set of tests:

.. code-block:: console

   $ locust -f tests/locust/locustfile.py Records --host=http://0.0.0.0
  [2017-12-19 12:56:37,173] 127.0.0.1/INFO/locust.main: Starting web monitor \
  at *:8089
  [2017-12-19 12:56:37,175] 127.0.0.1/INFO/locust.main: Starting Locust 0.8
  ...
  $ firefox http://127.0.0.1:8089

"""

from locust import HttpLocust, TaskSet, task

# 452, 3901, 3900, 4000 hidden Opera records.
RECORDS = [
    1,
    1000,
    1002,
    1050,
    1052,
    1100,
    11000,
    1120,
    1200,
    1204,
    1300,
    15,
    1700,
    1701,
    1800,
    1801,
    1803,
    200,
    2000,
    201,
    203,
    220,
    221,
    230,
    233,
    250,
    252,
    253,
    300,
    3000,
    320,
    328,
    35,
    3500,
    352,
    3600,
    3700,
    3800,
    3860,
    40,
    400,
    402,
    41,
    410,
    450,
    451,
    453,
    460,
    463,
    4900,
    50,
    5000,
    5001,
    5003,
    5100,
    5104,
    545,
    55,
    550,
    5500,
    551,
    553,
    554,
    556,
    560,
    60,
    600,
    6000,
    6026,
    6100,
    614,
    6200,
    7000,
    7100,
    7125,
    7299,
]


class MixTaskSet(TaskSet):
    @task(10)
    def frontpage(self):
        self.client.get("/")

    @task(5)
    def search(self):
        self.client.get("/search")

    @task(3)
    def search_type_glossary(self):
        self.client.get("/search?page=1&size=20&type=Glossary&sort=title")

    @task(3)
    def search_experiment_cms(self):
        self.client.get("/search?experiment=CMS")

    @task(3)
    def search_type_news(self):
        self.client.get("/search?type=News")

    @task(5)
    def api_search(self):
        self.client.get("/api/records")

    @task(3)
    def api_search_atlas(self):
        self.client.get("/api/records?page=1&size=20&experiment=ATLAS")

    @task(3)
    def api_search_alice(self):
        self.client.get("/api/records?page=1&size=20&experiment=ALICE")

    @task(3)
    def api_search_cms(self):
        self.client.get("/api/records?page=1&size=20&experiment=CMS")

    @task(3)
    def api_search_lhcb(self):
        self.client.get("/api/records?page=1&size=20&experiment=LHCb")

    @task(3)
    def api_search_dataset(self):
        self.client.get("/api/records?page=1&size=20&experiment=Dataset")

    @task(3)
    def api_search_software(self):
        self.client.get("/api/records?page=1&size=20&experiment=Software")

    @task(3)
    def api_search_environment(self):
        self.client.get("/api/records?page=1&size=20&experiment=Environment")

    @task(3)
    def api_search_documentation(self):
        self.client.get("/api/records?page=1&size=20&experiment=Documentation")

    @task(3)
    def api_search_keywords_education(self):
        self.client.get("/api/records?page=1&size=20&experiment=keywords:education")

    @task(3)
    def api_search_collision_data(self):
        self.client.get("/api/records?page=1&size=20&experiment=collision%20data")

    @task(3)
    def docs_alice_getting_started(self):
        self.client.get("/docs/alice-getting-started")

    @task(3)
    def docs_atlas_higgs_machine_learning_challenge(self):
        self.client.get("/docs/atlas-higgs-machine-learning-challenge")

    @task(3)
    def docs_cms_guide_for_education(self):
        self.client.get("/docs/cms-guide-for-education")

    @task(3)
    def docs_cms_guide_for_research(self):
        self.client.get("/docs/cms-guide-for-research")

    @task(3)
    def docs_cms_summer_student_report_2017(self):
        self.client.get("/docs/cms-summer-student-report-2017")

    @task(3)
    def docs_cms_the_future_is_open_2017(self):
        self.client.get("/docs/cms-the-future-is-open-2017")

    @task(3)
    def docs_lhcb_getting_started(self):
        self.client.get("/docs/lhcb-getting-started")

    @task(3)
    def docs_docs_welcome(self):
        self.client.get("/docs/welcome")

    @task(3)
    def visualise_events_cms(self):
        self.client.get("/visualise/events/cms")

    @task(3)
    def visualise_histograms(self):
        self.client.get("/visualise/histograms")

    @task(1)
    def record_detail_1002(self):
        self.client.get("/record/1002")

    @task(1)
    def record_detail_5001(self):
        self.client.get("/record/5001")

    @task(1)
    def cached_file_download(self):
        self.client.get("/record/545/files/Zee.csv")

    @task(1)
    def non_cached_file_download(self):
        self.client.get("/record/545/files/Dimuon_SingleMu.csv")


class RecordsTaskSet(TaskSet):
    @task
    def records_ui(self):
        for record_id in RECORDS:
            self.client.get("/record/{0}".format(record_id), name="/record/[id]")

    @task
    def records_api(self):
        for record_id in RECORDS:
            self.client.get(
                "/api/records/{0}".format(record_id), name="/api/records/[id]"
            )


class Records(HttpLocust):
    task_set = RecordsTaskSet


class Mix(HttpLocust):
    task_set = MixTaskSet
