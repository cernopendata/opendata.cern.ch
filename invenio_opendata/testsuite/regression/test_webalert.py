# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013 CERN.
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

"""WebAlert Regression Test Suite."""

__revision__ = "$Id$"

from cStringIO import StringIO
import sys
import datetime
import time

from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import

from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages, \
                              InvenioTestCase

run_sql = lazy_import('invenio.legacy.dbquery:run_sql')
alert_engine = lazy_import('invenio.legacy.webalert:alert_engine')
get_creation_date = lazy_import('invenio.legacy.search_engine:get_creation_date')


class WebAlertWebPagesAvailabilityTest(InvenioTestCase):
    """Check WebAlert web pages whether they are up or not."""

    def test_your_alerts_pages_availability(self):
        """webalert - availability of Your Alerts pages"""
        from invenio.config import CFG_SITE_URL

        baseurl = CFG_SITE_URL + '/youralerts/'

        _exports = ['', 'display', 'input', 'modify', 'list', 'add',
                    'update', 'remove']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return


class WebAlertHTMLToTextTest(InvenioTestCase):
    """Check that HTML is properly converted to text."""

    def test_your_alerts_pages_availability(self):
        """webalert - HTML to text conversion"""
        get_as_text = lazy_import('invenio.legacy.webalert.htmlparser:get_as_text')

        out = get_as_text(5)
        self.assertIn("High energy cosmic rays striking atoms at the top of the atmosphere give the rise to showers of particles striking the Earth's surface", out)
        self.assertIn("Des rayons cosmiques de haute energie heurtent des atomes dans la haute atmosphere et donnent ainsi naissance a des gerbes de particules projetees sur la surface terrestre", out)
        self.assertIn("CERN-DI-9905005", out)

        out = get_as_text(74)
        self.assertIn("Quasinormal modes of Reissner-Nordstrom Anti-de Sitter Black Holes", out)
        self.assertIn("hep-th/0003295", out)
        self.assertIn("Complex frequencies associated with quasinormal modes for large Reissner-Nordstr$\\ddot{o}$m Anti-de Sitter black holes have been computed.", out)
        self.assertIn("Phys. Lett., B :481 2000 79-88", out)


class WebAlertFilteringRestrictedRecords(InvenioTestCase):
    """Check that restricted records are filtered out for unauthorized users"""

    def setUp(self):
        """
        webalert - prepare test alerts
        """
        from invenio.config import CFG_SITE_ADMIN_EMAIL
        from invenio.legacy.webalert import alert_engine_config

        # TODO: test alerts for baskets too
        self.added_query_ids = []
        q_query = """INSERT INTO query (type, urlargs) VALUES (%s,%s)"""
        q_user_query = """INSERT INTO user_query (id_user, id_query, date) VALUES (%%s,%(id_query)s,NOW())"""
        q_user_query_basket = """INSERT INTO user_query_basket (id_user, id_query, id_basket,
                                             frequency, date_creation,
                                             alert_name, notification, alert_recipient)
                                             VALUES (%%s,%(id_query)s,%%s,%%s,DATE(NOW()),%%s,%%s,%%s)"""
        parameters = {'romeo 1': {'query_params': ('r', 'c=Theses&c=Poetry',),
                                  'user_query_params': (5,),
                                  'user_query_basket_params': (5, 0, 'day', 'Romeo alert 1', 'y', '',)},
                      'juliet 1': {'query_params': ('r', 'c=Theses&c=Poetry',),
                                   'user_query_params': (6,),
                                   'user_query_basket_params': (6, 0, 'day', 'Juliet alert 1', 'y', '',)},
                      'mailing list 1': {'query_params': ('r', 'c=Theses&c=Poetry',),
                                         'user_query_params': (6,),
                                         'user_query_basket_params': (6, 0, 'day', 'Mailing list alert 1', 'y', CFG_SITE_ADMIN_EMAIL,)},
                      'juliet 2': {'query_params': ('r', 'c=Theses',),
                                   'user_query_params': (6,),
                                   'user_query_basket_params': (6, 0, 'day', 'Juliet alert 2', 'y', '',)},
                      }

        for params in parameters.values():
            row_id = run_sql(q_query, params['query_params'])
            self.added_query_ids.append(row_id)
            run_sql(q_user_query % {'id_query': row_id}, params['user_query_params'])
            run_sql(q_user_query_basket % {'id_query': row_id}, params['user_query_basket_params'])

        # Run the alert for a date when we expect some result, and
        # record output for later analysis.
        # First get creation date of demo records:
        alert_date = datetime.datetime(*(time.strptime(get_creation_date(41, fmt="%Y-%m-%d"),
                                                       '%Y-%m-%d')[:6])).date() + datetime.timedelta(days=1)
        # Prevent emails to be sent, raise verbosity:
        previous_cfg_webalert_debug_level = alert_engine_config.CFG_WEBALERT_DEBUG_LEVEL
        alert_engine_config.CFG_WEBALERT_DEBUG_LEVEL = 3
        # Re-route standard output:
        previous_stdout = sys.stdout # Re-route standard output
        sys.stdout = alert_output = StringIO()
        # Run the alert
        alert_engine.run_alerts(date=alert_date)
        # Restore standard output and alert debug level
        sys.stdout = previous_stdout
        alert_engine_config.CFG_WEBALERT_DEBUG_LEVEL = previous_cfg_webalert_debug_level

        # Remove test alerts
        for query_id in self.added_query_ids:
            run_sql('DELETE FROM user_query_basket WHERE id_query=%s', (query_id,))
            run_sql('DELETE FROM user_query WHERE id_query=%s', (query_id,))
            run_sql('DELETE FROM query WHERE id=%s', (query_id,))

        # Identify alerts, organize by name (hopefully unique for
        # these tests)
        self.alerts = {}
        for alert_message in alert_output.getvalue().split("+" * 80 + '\n'):
            if 'alert name: ' in alert_message:
                alert_name = alert_message.split('alert name: ')[1].split('\n')[0]
                self.alerts[alert_name] = alert_message

    def test_alert_theses_and_poems_for_juliet(self):
        """webalert - Juliet does not get Theses in alert"""
        from invenio.config import CFG_SITE_RECORD
        self.assert_('-> these records have been filtered out, as user id 6 did not have access:\n[35, 36, 37, 38, 39, 40, 41, 42' in self.alerts['Juliet alert 1'])
        self.assert_(CFG_SITE_RECORD + '/35' not in self.alerts['Juliet alert 1'])
        self.assert_(CFG_SITE_RECORD + '/41' not in self.alerts['Juliet alert 1'])
        self.assert_(CFG_SITE_RECORD + '/75' in self.alerts['Juliet alert 1'])

    def test_alert_theses_and_poems_for_romeo(self):
        """webalert - Romeo gets Theses in alert"""
        from invenio.config import CFG_SITE_RECORD
        self.assert_(CFG_SITE_RECORD + '/35' in self.alerts['Romeo alert 1'])
        self.assert_(CFG_SITE_RECORD + '/41' in self.alerts['Romeo alert 1'])
        self.assert_(CFG_SITE_RECORD + '/75' in self.alerts['Romeo alert 1'])

    def test_alert_theses_for_juliet(self):
        """webalert - Juliet does not receive empty Theses alert"""
        self.assert_(not self.alerts.has_key('Juliet alert 2'))

    def test_alert_theses_and_poems_for_mailinglist(self):
        """webalert - Mailing list gets Theses in alert"""
        from invenio.config import CFG_SITE_RECORD
        self.assert_('-> these records have been filtered out' not in self.alerts['Mailing list alert 1'])
        self.assert_(CFG_SITE_RECORD + '/35' in self.alerts['Mailing list alert 1'])
        self.assert_(CFG_SITE_RECORD + '/41' in self.alerts['Mailing list alert 1'])
        self.assert_(CFG_SITE_RECORD + '/75' in self.alerts['Mailing list alert 1'])

TEST_SUITE = make_test_suite(WebAlertWebPagesAvailabilityTest,
                             WebAlertHTMLToTextTest,
                             WebAlertFilteringRestrictedRecords)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
