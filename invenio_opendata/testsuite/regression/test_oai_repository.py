# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2013 CERN.
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

"""OAI Repository Regression Test Suite."""

__revision__ = "$Id$"

import time
from datetime import datetime, timedelta
import re

from cStringIO import StringIO

from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from intbitset import intbitset
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages, \
                              InvenioTestCase

oai_repository_server = lazy_import('invenio.legacy.oairepository.server')
search_engine = lazy_import('invenio.legacy.search_engine')
run_sql = lazy_import('invenio.legacy.dbquery:run_sql')


class OAIRepositoryTouchSetTest(InvenioTestCase):
    """Check OAI-PMH consistency when touching a set."""
    def setUp(self):
        """Backup the current configuration"""
        self.timestamps = run_sql("SELECT id, last_updated FROM oaiREPOSITORY")

    def tearDown(self):
        """Restore timestamps"""
        for id, last_updated in self.timestamps:
            run_sql("UPDATE oaiREPOSITORY SET last_updated=%s WHERE id=%s", (last_updated, id))

    def test_touching_set(self):
        """oairepository - touch a set"""
        req = StringIO()
        oai_repository_server.oai_list_records_or_identifiers(req,  {'verb': 'ListIdentifiers', 'metadataPrefix': 'marcxml', 'set':'cern:experiment'})
        response = req.getvalue()
        current_timestamps = re.findall("<datestamp>(.*?)</datestamp>", response)
        current_timestamps = [datetime(*time.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')[:-3]) for timestamp in current_timestamps]
        last_timestamp = max(current_timestamps)
        future_timestamp = last_timestamp + timedelta(0, 5) ## 5 seconds in the future to the last record
        future_timestamp = future_timestamp.strftime('%Y-%m-%dT%H:%M:%SZ')
        req = StringIO()
        oai_repository_server.oai_list_records_or_identifiers(req,  {'verb': 'ListIdentifiers', 'metadataPrefix': 'marcxml', 'set':'cern:experiment', 'from': future_timestamp})
        response = req.getvalue()
        self.failIf(re.findall("<datestamp>(.*?)</datestamp>", response))
        from invenio.legacy.oairepository.admin import touch_oai_set
        touch_oai_set('cern:experiment')
        req = StringIO()
        oai_repository_server.oai_list_records_or_identifiers(req,  {'verb': 'ListIdentifiers', 'metadataPrefix': 'marcxml', 'set':'cern:experiment', 'from': future_timestamp})
        response = req.getvalue()
        new_timestamps = re.findall("<datestamp>(.*?)</datestamp>", response)
        new_timestamps = [datetime(*time.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')[:-3]) for timestamp in new_timestamps]
        self.assertEqual(len(new_timestamps), len(current_timestamps), "new %s, old %s, from: %s" % (new_timestamps, current_timestamps, future_timestamp))
        self.failUnless(new_timestamps > current_timestamps)


class OAIRepositoryWebPagesAvailabilityTest(InvenioTestCase):
    """Check OAI Repository web pages whether they are up or not."""

    def test_oai_server_pages_availability(self):
        """oairepository - availability of OAI server pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/oai2d'

        _exports = [#fast commands first:
                    '?verb=Identify',
                    '?verb=ListMetadataFormats',
                    # sleepy commands now:
                    '?verb=ListSets',
                    '?verb=ListRecords',
                    '?verb=GetRecord']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            if url.endswith('Identify') or \
               url.endswith('ListMetadataFormats'):
                pass
            else:
                # some sleep required for verbs other than Identify
                # and ListMetadataFormats, since oai2d refuses too
                # frequent access:
                time.sleep(cfg['CFG_OAI_SLEEP'])
            error_messages.extend(test_web_page_content(url,
                                                        expected_text=
                                                        '</OAI-PMH>'))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return


class TestSelectiveHarvesting(InvenioTestCase):
    """Test set, from and until parameters used to do selective harvesting."""

    def test_set(self):
        """oairepository - testing selective harvesting with 'set' parameter"""
        self.assertEqual(intbitset([10, 17]), oai_repository_server.oai_get_recid_list(set_spec="cern:experiment"))
        self.assert_("Multifractal analysis of minimum bias events" in \
                     ''.join([oai_repository_server.print_record(recID) for recID in \
                              oai_repository_server.oai_get_recid_list(set_spec="cern:experiment")]))
        self.assert_("Multifractal analysis of minimum bias events" not in \
                     ''.join([oai_repository_server.print_record(recID) for recID in \
                              oai_repository_server.oai_get_recid_list(set_spec="cern:theory")]))
        self.failIf(oai_repository_server.oai_get_recid_list(set_spec="nonExistingSet"))

    def test_from_and_until(self):
        """oairepository - testing selective harvesting with 'from' and 'until' parameters"""

        req = StringIO()
        # List available records, get datestamps and play with them
        oai_repository_server.oai_list_records_or_identifiers(req, {'verb': 'ListIdentifiers', 'metadataPrefix': 'marcxml'})
        identifiers = req.getvalue()
        datestamps = re.findall('<identifier>(?P<id>.*?)</identifier>\s*<datestamp>(?P<date>.*?)</datestamp>', identifiers, re.M)

        sample_datestamp = datestamps[0][1] # Take one datestamp
        sample_oai_id = datestamps[0][0] # Take corresponding oai id
        sample_id = search_engine.perform_request_search(p=sample_oai_id,
                                                         f=cfg['CFG_OAI_ID_FIELD'])[0] # Find corresponding system number id

        # There must be some datestamps
        self.assertNotEqual([], datestamps)

        # We must be able to retrieve an id with the date we have just found
        self.assert_(sample_id in oai_repository_server.oai_get_recid_list(fromdate=sample_datestamp), "%s not in %s (fromdate=%s)" % (sample_id, oai_repository_server.oai_get_recid_list(fromdate=sample_datestamp), sample_datestamp))
        self.assert_(sample_id in oai_repository_server.oai_get_recid_list(untildate=sample_datestamp), "%s not in %s" % (sample_id, oai_repository_server.oai_get_recid_list(untildate=sample_datestamp)))
        self.assert_(sample_id in oai_repository_server.oai_get_recid_list(untildate=sample_datestamp, \
                                                                 fromdate=sample_datestamp))

        # Same, with short format date. Eg 2007-12-13
        self.assert_(sample_id in oai_repository_server.oai_get_recid_list(fromdate=sample_datestamp.split('T')[0]))
        self.assert_(sample_id in oai_repository_server.oai_get_recid_list(untildate=sample_datestamp.split('T')[0]))
        self.assert_(sample_id in oai_repository_server.oai_get_recid_list(fromdate=sample_datestamp.split('T')[0], \
                                                                 untildate=sample_datestamp.split('T')[0]))

        # At later date (year after) we should not find our id again
        sample_datestamp_year = int(sample_datestamp[0:4])
        sample_datestamp_rest = sample_datestamp[4:]
        later_datestamp = str(sample_datestamp_year + 1) + sample_datestamp_rest
        self.assert_(sample_id not in oai_repository_server.oai_get_recid_list(fromdate=later_datestamp))

        # At earlier date (year before) we should not find our id again
        earlier_datestamp = str(sample_datestamp_year - 1) + sample_datestamp_rest
        self.assert_(sample_id not in oai_repository_server.oai_get_recid_list(untildate=earlier_datestamp))

        # From earliest date to latest date must include all oai records
        dates = [(time.mktime(time.strptime(date[1], "%Y-%m-%dT%H:%M:%SZ")), date[1]) for date in datestamps]
        dates = dict(dates)
        sorted_times = dates.keys()
        sorted_times.sort()
        earliest_datestamp = dates[sorted_times[0]]
        latest_datestamp = dates[sorted_times[-1]]
        self.assertEqual(oai_repository_server.oai_get_recid_list(), \
                         oai_repository_server.oai_get_recid_list(fromdate=earliest_datestamp, \
                                                            untildate=latest_datestamp))

    def test_resumption_token(self):
        """oairepository - testing harvesting with bad resumption token"""
        # Non existing resumptionToken
        req = StringIO()
        oai_repository_server.oai_list_records_or_identifiers(req, {'resumptionToken': 'foobar', 'verb': 'ListRecords'})

        self.assert_('badResumptionToken' in req.getvalue())


class TestPerformance(InvenioTestCase):
    """Test performance of the repository """

    def setUp(self):
        """Setting up some variables"""
        # Determine how many records are served
        self.number_of_records = len(oai_repository_server.oai_get_recid_list("", "", ""))
        if cfg['CFG_OAI_LOAD'] < self.number_of_records:
            self.number_of_records = cfg['CFG_OAI_LOAD']

    def test_response_speed_oai(self):
        """oairepository - speed of response for oai_dc output"""
        allowed_seconds_per_record_oai = 0.03

        # Test oai ListRecords performance
        t0 = time.time()
        oai_repository_server.oai_list_records_or_identifiers(StringIO(), {'metadataPrefix': 'oai_dc', 'verb': 'ListRecords'})
        t = time.time() - t0
        if t > self.number_of_records * allowed_seconds_per_record_oai:
            self.fail("""Response for ListRecords with metadataPrefix=oai_dc took too much time:
%s seconds.
Limit: %s seconds""" % (t, self.number_of_records * allowed_seconds_per_record_oai))

    def test_response_speed_marcxml(self):
        """oairepository - speed of response for marcxml output"""
        allowed_seconds_per_record_marcxml = 0.05

        # Test marcxml ListRecords performance
        t0 = time.time()
        oai_repository_server.oai_list_records_or_identifiers(StringIO(), argd={'metadataPrefix': 'marcxml', 'verb': 'ListRecords'})
        t = time.time() - t0
        if t > self.number_of_records * allowed_seconds_per_record_marcxml:
            self.fail("""Response for ListRecords with metadataPrefix=marcxml took too much time:\n
%s seconds.
Limit: %s seconds""" % (t, self.number_of_records * allowed_seconds_per_record_marcxml))


TEST_SUITE = make_test_suite(OAIRepositoryTouchSetTest,
                             OAIRepositoryWebPagesAvailabilityTest,
                             TestSelectiveHarvesting,
                             TestPerformance)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
