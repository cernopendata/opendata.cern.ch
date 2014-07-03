# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2011, 2012, 2013 CERN.
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

"""WebLinkback - Regression Test Suite"""


from flask import url_for
from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.testsuite import make_test_suite, \
    run_test_suite, \
    nottest, \
    test_web_page_content, \
    merge_error_messages, \
    InvenioTestCase

try:
    from mock import patch
    HAS_MOCK = True
except ImportError:
    HAS_MOCK = False

run_sql = lazy_import('invenio.legacy.dbquery:run_sql')
CFG_DATABASE_NAME = lazy_import('invenio.legacy.dbquery:CFG_DATABASE_NAME')

weblinkback = lazy_import('invenio.legacy.weblinkback')

get_all_linkbacks = lazy_import('invenio.legacy.weblinkback.dblayer:get_all_linkbacks')
approve_linkback = lazy_import('invenio.legacy.weblinkback.dblayer:approve_linkback')
reject_linkback = lazy_import('invenio.legacy.weblinkback.dblayer:reject_linkback')
get_approved_latest_added_linkbacks = lazy_import('invenio.legacy.weblinkback.dblayer:get_approved_latest_added_linkbacks')
get_url_list = lazy_import('invenio.legacy.weblinkback.dblayer:get_url_list')
add_url_to_list = lazy_import('invenio.legacy.weblinkback.dblayer:add_url_to_list')
remove_url = lazy_import('invenio.legacy.weblinkback.dblayer:remove_url')
url_exists = lazy_import('invenio.legacy.weblinkback.dblayer:url_exists')
get_url_title = lazy_import('invenio.legacy.weblinkback.dblayer:get_url_title')
get_urls_and_titles = lazy_import('invenio.legacy.weblinkback.dblayer:get_urls_and_titles')
remove_linkback = lazy_import('invenio.legacy.weblinkback.dblayer:remove_linkback')
set_url_broken = lazy_import('invenio.legacy.weblinkback.dblayer:set_url_broken')
update_url_title = lazy_import('invenio.legacy.weblinkback.dblayer:update_url_title')

create_trackback = lazy_import('invenio.legacy.weblinkback.api:create_trackback')
delete_linkbacks_on_blacklist = lazy_import('invenio.legacy.weblinkback.api:delete_linkbacks_on_blacklist')
update_linkbacks = lazy_import('invenio.legacy.weblinkback.api:update_linkbacks')

CFG_WEBLINKBACK_STATUS = lazy_import('invenio.legacy.weblinkback.config:CFG_WEBLINKBACK_STATUS')
CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME = lazy_import('invenio.legacy.weblinkback.config:CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME')
CFG_WEBLINKBACK_LIST_TYPE = lazy_import('invenio.legacy.weblinkback.config:CFG_WEBLINKBACK_LIST_TYPE')
CFG_WEBLINKBACK_TYPE = lazy_import('invenio.legacy.weblinkback.config:CFG_WEBLINKBACK_TYPE')
CFG_WEBLINKBACK_PAGE_TITLE_STATUS = lazy_import('invenio.legacy.weblinkback.config:CFG_WEBLINKBACK_PAGE_TITLE_STATUS')


def get_max_auto_increment_id(table):
    return run_sql("SELECT Auto_increment FROM information_schema.tables WHERE table_name=%s AND table_schema=%s", (table, CFG_DATABASE_NAME))[0][0] - 1


@nottest
def remove_test_data():
    run_sql("DELETE FROM lnkENTRY")
    run_sql("DELETE FROM lnkENTRYURLTITLE")
    run_sql("DELETE FROM lnkENTRYLOG")
    run_sql("DELETE FROM lnkLOG")
    run_sql("DELETE FROM lnkADMINURL")
    run_sql("DELETE FROM lnkADMINURLLOG")


class WebLinkbackWebPagesAvailabilityTest(InvenioTestCase):
    """Test WebLinkback web pages whether they are up or not"""

    def test_linkback_pages_availability(self):
        """weblinkback - availability of /linkbacks pages"""

        error_messages = []

        baseurl = cfg['CFG_SITE_SECURE_URL'] + '/%s/10/linkbacks/' % cfg['CFG_SITE_RECORD']
        _exports = ['', 'display', 'index', 'approve', 'reject']
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url))

        baseurl = cfg['CFG_SITE_URL'] + '/linkbacks/'
        error_messages.extend(test_web_page_content(baseurl))

        if error_messages:
            self.fail(merge_error_messages(error_messages))

    def test_weblinkback_admin_interface_availability(self):
        """weblinkback - availability of WebLinkback Admin interface pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/admin/weblinkback/weblinkbackadmin.py/'

        _exports = ['', 'lists', 'linkbacks']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            # first try as guest:
            error_messages.extend(test_web_page_content(url,
                                                        username='guest',
                                                        expected_text='Authorization failure'))
            # then try as admin:
            error_messages.extend(test_web_page_content(url,
                                                        username='admin'))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return


class WebLinkbackDatabaseTest(InvenioTestCase):
    """Test WebLinkback database layer"""

    def setUp(self):
        """Insert test data"""
        self.insert_time = []
        self.user_info = {'uid': 0}

        self.remove_test_data()

        # recid 41
        run_sql("INSERT INTO lnkENTRY (origin_url, id_bibrec, additional_properties, type, status, insert_time) VALUES ('URL1', 41, NULL, %s, %s, NOW())", (CFG_WEBLINKBACK_TYPE['TRACKBACK'], CFG_WEBLINKBACK_STATUS['PENDING']))
        last_linkback_entryid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        self.insert_time.append(run_sql("SELECT NOW()")[0][0])
        run_sql("INSERT INTO lnkLOG (id_user, action, log_time) VALUES (NULL, %s, %s)", (CFG_WEBLINKBACK_STATUS['INSERTED'], self.insert_time[0]))
        last_logid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkENTRYLOG (id_lnkENTRY, id_lnkLOG) VALUES (%s, %s)", (last_linkback_entryid, last_logid))

        run_sql("INSERT INTO lnkENTRY (origin_url, id_bibrec, additional_properties, type, status, insert_time) VALUES ('URL2', 41, NULL, %s, %s, NOW())", (CFG_WEBLINKBACK_TYPE['TRACKBACK'], CFG_WEBLINKBACK_STATUS['PENDING']))
        last_linkback_entryid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkLOG (id_user, action, log_time) VALUES (NULL, %s, NOW())", (CFG_WEBLINKBACK_STATUS['INSERTED'], ))
        last_logid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkENTRYLOG (id_lnkENTRY, id_lnkLOG) VALUES (%s, %s)", (last_linkback_entryid, last_logid))

        run_sql("INSERT INTO lnkENTRY (origin_url, id_bibrec, additional_properties, type, status, insert_time) VALUES ('URL3', 41, NULL, %s, %s, NOW())", (CFG_WEBLINKBACK_TYPE['TRACKBACK'], CFG_WEBLINKBACK_STATUS['PENDING']))
        last_linkback_entryid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkLOG (id_user, action, log_time) VALUES (NULL, %s, NOW())", (CFG_WEBLINKBACK_STATUS['INSERTED'], ))
        last_logid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkENTRYLOG (id_lnkENTRY, id_lnkLOG) VALUES (%s, %s)", (last_linkback_entryid, last_logid))

        run_sql("INSERT INTO lnkENTRY (origin_url, id_bibrec, additional_properties, type, status, insert_time) VALUES ('URL4', 41, NULL, %s, %s, NOW())", (CFG_WEBLINKBACK_TYPE['TRACKBACK'], CFG_WEBLINKBACK_STATUS['PENDING']))
        last_linkback_entryid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkLOG (id_user, action, log_time) VALUES (NULL, %s, NOW())", (CFG_WEBLINKBACK_STATUS['INSERTED'], ))
        last_logid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkENTRYLOG (id_lnkENTRY, id_lnkLOG) VALUES (%s, %s)", (last_linkback_entryid, last_logid))

        # recid 42
        run_sql("INSERT INTO lnkENTRY (origin_url, id_bibrec, additional_properties, type, status, insert_time) VALUES ('URL5', 42, NULL, %s, %s, NOW())", (CFG_WEBLINKBACK_TYPE['TRACKBACK'], CFG_WEBLINKBACK_STATUS['PENDING']))
        last_linkback_entryid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        self.insert_time.append(run_sql("SELECT NOW()")[0][0])
        run_sql("INSERT INTO lnkLOG (id_user, action, log_time) VALUES (NULL, %s, %s)", (CFG_WEBLINKBACK_STATUS['INSERTED'], self.insert_time[1]))
        last_logid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkENTRYLOG (id_lnkENTRY, id_lnkLOG) VALUES (%s, %s)", (last_linkback_entryid, last_logid))

        run_sql("INSERT INTO lnkENTRY (origin_url, id_bibrec, additional_properties, type, status, insert_time) VALUES ('URL6', 42, NULL, %s, %s, NOW())", (CFG_WEBLINKBACK_TYPE['TRACKBACK'], CFG_WEBLINKBACK_STATUS['PENDING']))
        last_linkback_entryid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkLOG (id_user, action, log_time) VALUES (NULL, %s, %s)", (CFG_WEBLINKBACK_STATUS['INSERTED'], self.insert_time[1]))
        last_logid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkENTRYLOG (id_lnkENTRY, id_lnkLOG) VALUES (%s, %s)", (last_linkback_entryid, last_logid))

        run_sql("INSERT INTO lnkENTRY (origin_url, id_bibrec, additional_properties, type, status, insert_time) VALUES ('URL7', 42, NULL, %s, %s, NOW())", (CFG_WEBLINKBACK_TYPE['TRACKBACK'], CFG_WEBLINKBACK_STATUS['PENDING']))
        last_linkback_entryid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkLOG (id_user, action, log_time) VALUES (NULL, %s, %s)", (CFG_WEBLINKBACK_STATUS['INSERTED'], self.insert_time[1]))
        last_logid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkENTRYLOG (id_lnkENTRY, id_lnkLOG) VALUES (%s, %s)", (last_linkback_entryid, last_logid))

        run_sql("INSERT INTO lnkENTRY (origin_url, id_bibrec, additional_properties, type, status, insert_time) VALUES ('URL8', 42, NULL, %s, %s, NOW())", (CFG_WEBLINKBACK_TYPE['TRACKBACK'], CFG_WEBLINKBACK_STATUS['PENDING']))
        last_linkback_entryid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkLOG (id_user, action, log_time) VALUES (NULL, %s, %s)", (CFG_WEBLINKBACK_STATUS['INSERTED'], self.insert_time[1]))
        last_logid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkENTRYLOG (id_lnkENTRY, id_lnkLOG) VALUES (%s, %s)", (last_linkback_entryid, last_logid))

        run_sql("INSERT INTO lnkENTRY (origin_url, id_bibrec, additional_properties, type, status, insert_time) VALUES ('URL1', 42, NULL, %s, %s, NOW())", (CFG_WEBLINKBACK_TYPE['TRACKBACK'], CFG_WEBLINKBACK_STATUS['PENDING']))
        last_linkback_entryid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkLOG (id_user, action, log_time) VALUES (NULL, %s, %s)", (CFG_WEBLINKBACK_STATUS['INSERTED'], self.insert_time[1]))
        last_logid = run_sql("SELECT LAST_INSERT_ID()")[0][0]
        run_sql("INSERT INTO lnkENTRYLOG (id_lnkENTRY, id_lnkLOG) VALUES (%s, %s)", (last_linkback_entryid, last_logid))

    def tearDown(self):
        """Remove test data"""
        self.remove_test_data()

    @nottest
    def remove_test_data(self):
        """Clean tables"""
        self._max_id_lnkENTRY = get_max_auto_increment_id('lnkENTRY')
        self._max_id_lnkADMINURL = get_max_auto_increment_id('lnkADMINURL')
        self._max_id_lnkLOG = get_max_auto_increment_id('lnkLOG')
        remove_test_data()

    def get_all_from_table(self, tableName):
        return run_sql("SELECT * FROM %s" % tableName) # kwalitee: disable=sql

    def test_get_all_linkbacks1(self):
        """weblinkback - get all linkbacks for lnkENTRY and with a certain status"""
        self.assertEqual(0, len(get_all_linkbacks(recid=5, status=CFG_WEBLINKBACK_STATUS['PENDING'])))
        self.assertEqual(4, len(get_all_linkbacks(recid=41, status=CFG_WEBLINKBACK_STATUS['PENDING'])))
        self.assertEqual(0, len(get_all_linkbacks(recid=41, status=CFG_WEBLINKBACK_STATUS['INSERTED'])))
        self.assertEqual(5, len(get_all_linkbacks(recid=42, status=CFG_WEBLINKBACK_STATUS['PENDING'])))
        self.assertEqual(0, len(get_all_linkbacks(recid=42, status=CFG_WEBLINKBACK_STATUS['APPROVED'])))

        url = cfg['CFG_SITE_SECURE_URL'] + '/%s/41/linkbacks/' % cfg['CFG_SITE_RECORD']
        expected_texts = ('Linkbacks to review: 4', 'Linkbacks: 0', 'URL1', 'URL2', 'URL3', 'URL4')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))

        url = cfg['CFG_SITE_SECURE_URL'] + '/%s/42/linkbacks/' % cfg['CFG_SITE_RECORD']
        expected_texts = ('Linkbacks to review: 5', 'Linkbacks: 0', 'URL5', 'URL6', 'URL7', 'URL8', 'URL1')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))

    def test_get_all_linkbacks2(self):
        """weblinkback - get all linkbacks with a certain status"""
        self.assertEqual(9, len(get_all_linkbacks(status=CFG_WEBLINKBACK_STATUS['PENDING'])))
        self.assertEqual(0, len(get_all_linkbacks(status=CFG_WEBLINKBACK_STATUS['APPROVED'])))

    def test_approve_linkback(self):
        """weblinkback - approve linkback"""
        linkback = get_all_linkbacks(41)[0]
        linkbackid = linkback[0]
        linkback_status = linkback[5]
        self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_status)

        approve_linkback(linkbackid, self.user_info)

        linkback = get_all_linkbacks(recid=41)[0]
        linkback_status = linkback[5]
        self.assertEqual(CFG_WEBLINKBACK_STATUS['APPROVED'], linkback_status)

        url = cfg['CFG_SITE_SECURE_URL'] + '/%s/41/linkbacks/' % cfg['CFG_SITE_RECORD']
        expected_texts = ('Linkbacks to review: 3', 'Linkbacks: 1')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))

    def test_reject_linkback(self):
        """weblinkback - reject linkback"""
        linkback = get_all_linkbacks(recid=42)[1]
        linkbackid = linkback[0]
        linkback_status = linkback[5]
        self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_status)

        reject_linkback(linkbackid, self.user_info)

        linkback = get_all_linkbacks(recid=42)[1]
        linkback_status = linkback[5]
        self.assertEqual(CFG_WEBLINKBACK_STATUS['REJECTED'], linkback_status)

        url = cfg['CFG_SITE_SECURE_URL'] + '/%s/42/linkbacks/' % cfg['CFG_SITE_RECORD']
        expected_texts = ('Linkbacks to review: 4', 'Linkbacks: 0')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))

    def test_create_linkback1(self):
        """weblinkback - create linkback"""
        recid = 42
        argd = {'url': 'URL',
                'title': CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME,
                'excerpt': CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME,
                'blog_name': 'Test Blog',
                'id': CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME,
                'source': CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME,
                }

        linkbackid = create_trackback(recid, argd['url'], argd['title'], argd['excerpt'], argd['blog_name'], argd['id'], argd['source'], self.user_info)
        self.assertEqual(10 + self._max_id_lnkENTRY, linkbackid)

        linkback = get_all_linkbacks(recid=recid)[5]
        self.assertEqual(linkbackid, linkback[0])
        self.assertEqual(argd['url'], linkback[1])
        self.assertEqual(recid, linkback[2])
        self.assertEqual(str({'blog_name': argd['blog_name']}), linkback[3])
        self.assertEqual(CFG_WEBLINKBACK_TYPE['TRACKBACK'], linkback[4])
        self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback[5])

        url = cfg['CFG_SITE_SECURE_URL'] + '/%s/42/linkbacks/' % cfg['CFG_SITE_RECORD']
        expected_texts = ('Linkbacks to review: 6', 'Linkbacks: 0')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))

        approve_linkback(linkbackid, self.user_info)

        linkback = get_all_linkbacks(recid=recid)[5]
        self.assertEqual(linkbackid, linkback[0])
        self.assertEqual(argd['url'], linkback[1])
        self.assertEqual(recid, linkback[2])
        self.assertEqual(str({'blog_name': argd['blog_name']}), linkback[3])
        self.assertEqual(CFG_WEBLINKBACK_TYPE['TRACKBACK'], linkback[4])
        self.assertEqual(CFG_WEBLINKBACK_STATUS['APPROVED'], linkback[5])

        url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
        self.assertEqual(1, len(url_titles))
        self.assertEqual(argd['url'], url_titles[0][1])
        self.assertEqual("", url_titles[0][2])
        self.assertEqual(0, url_titles[0][3])
        self.assertEqual(argd['url'], get_url_title(argd['url']))

        self.assertEqual(0, len(get_urls_and_titles(CFG_WEBLINKBACK_PAGE_TITLE_STATUS['OLD'])))
        self.assertEqual(1, len(get_urls_and_titles(CFG_WEBLINKBACK_PAGE_TITLE_STATUS['NEW'])))
        self.assertEqual(0, len(get_urls_and_titles(CFG_WEBLINKBACK_PAGE_TITLE_STATUS['MANUALLY_SET'])))

        url = cfg['CFG_SITE_SECURE_URL'] + '/%s/42/linkbacks/' % cfg['CFG_SITE_RECORD']
        expected_texts = ('Linkbacks to review: 5', 'Linkbacks: 1')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))

        self.assertEqual(10, len(self.get_all_from_table("lnkENTRY")))
        self.assertEqual(11, len(self.get_all_from_table("lnkENTRYLOG")))
        remove_linkback(linkbackid)
        self.assertEqual(9, len(self.get_all_from_table("lnkENTRY")))
        self.assertEqual(9, len(self.get_all_from_table("lnkENTRYLOG")))

    def test_create_linkback2(self):
        """weblinkback - create linkback with URL title"""
        recid = 42
        argd = {'url': 'URL',
                'title': 'My title',
                'excerpt': CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME,
                'blog_name': 'Test Blog',
                'id': CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME,
                'source': CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME,
                }

        linkbackid = create_trackback(recid, argd['url'], argd['title'], argd['excerpt'], argd['blog_name'], argd['id'], argd['source'], self.user_info)
        self.assertEqual(10 + self._max_id_lnkENTRY, linkbackid)

        linkback = get_all_linkbacks(recid=recid)[5]
        self.assertEqual(linkbackid, linkback[0])
        self.assertEqual(argd['url'], linkback[1])
        self.assertEqual(recid, linkback[2])
        self.assertEqual(CFG_WEBLINKBACK_TYPE['TRACKBACK'], linkback[4])
        self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback[5])

        url = cfg['CFG_SITE_SECURE_URL'] + '/%s/42/linkbacks/' % cfg['CFG_SITE_RECORD']
        expected_texts = ('Linkbacks to review: 6', 'Linkbacks: 0')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))

        approve_linkback(linkbackid, self.user_info)

        linkback = get_all_linkbacks(recid=recid)[5]
        self.assertEqual(linkbackid, linkback[0])
        self.assertEqual(argd['url'], linkback[1])
        self.assertEqual(recid, linkback[2])
        self.assertEqual(CFG_WEBLINKBACK_TYPE['TRACKBACK'], linkback[4])
        self.assertEqual(CFG_WEBLINKBACK_STATUS['APPROVED'], linkback[5])

        url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
        self.assertEqual(1, len(url_titles))
        self.assertEqual(argd['url'], url_titles[0][1])
        self.assertEqual(argd['title'], url_titles[0][2])
        self.assertEqual(1, url_titles[0][3])
        self.assertEqual(argd['title'], get_url_title(argd['url']))

        self.assertEqual(0, len(get_urls_and_titles(CFG_WEBLINKBACK_PAGE_TITLE_STATUS['OLD'])))
        self.assertEqual(0, len(get_urls_and_titles(CFG_WEBLINKBACK_PAGE_TITLE_STATUS['NEW'])))
        self.assertEqual(1, len(get_urls_and_titles(CFG_WEBLINKBACK_PAGE_TITLE_STATUS['MANUALLY_SET'])))

        url = cfg['CFG_SITE_SECURE_URL'] + '/%s/42/linkbacks/' % cfg['CFG_SITE_RECORD']
        expected_texts = ('Linkbacks to review: 5', 'Linkbacks: 1')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))

    def test_send_trackback(self):
        """weblinkback - create linkback through /sendtrackback"""
        def _test_send_trackback_enabled():
            url = url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.ch')
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text='<response></response>',
                                                       unexpected_text='<error>'))

            url = url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.ch')
            response = self.client.get(url,
                                       follow_redirects=True)
            self.assert200(response)

            url = url_for('weblinkback.sendtrackback', recid=30)
            response = self.client.get(url,
                                       follow_redirects=True)
            self.assert400(response)

            url_for('weblinkback.sendtrackback', recid=30, url='')
            response = self.client.get(url,
                                       follow_redirects=True)
            self.assert400(response)

            add_url_to_list('google', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
            url = url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.ch')
            response = self.client.get(url,
                                       follow_redirects=True)
            self.assert400(response)

        def _test_send_trackback_disabled():
            url = url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.ch')
            response = self.client.get(url,
                                       follow_redirects=True)
            self.assert404(response)

            url = url_for('weblinkback.sendtrackback', recid=30)
            response = self.client.get(url,
                                       follow_redirects=True)
            self.assert404(response)

        if cfg['CFG_WEBLINKBACK_TRACKBACK_ENABLED']:
            _test_send_trackback_enabled()
        else:
            _test_send_trackback_disabled()
        pass

    def test_get_approved_latest_added_linkback(self):
        """weblinkback - get approved latest added linkbacks"""
        for linkbackid in (1, 2, 5, 6, 7):
            approve_linkback(linkbackid + self._max_id_lnkENTRY, self.user_info)

        reject_linkback(4 + self._max_id_lnkENTRY, self.user_info)

        self.assertEqual(0, len(get_approved_latest_added_linkbacks(0)))
        self.assertEqual(1, len(get_approved_latest_added_linkbacks(1)))
        self.assertEqual(2, len(get_approved_latest_added_linkbacks(2)))
        self.assertEqual(3, len(get_approved_latest_added_linkbacks(3)))
        self.assertEqual(4, len(get_approved_latest_added_linkbacks(4)))
        self.assertEqual(5, len(get_approved_latest_added_linkbacks(5)))

        approved_linkbacks = get_approved_latest_added_linkbacks(6)
        self.assertEqual(5, len(approved_linkbacks))
        self.assertEqual(1 + self._max_id_lnkENTRY, approved_linkbacks[0][0])
        self.assertEqual(2 + self._max_id_lnkENTRY, approved_linkbacks[1][0])
        self.assertEqual(5 + self._max_id_lnkENTRY, approved_linkbacks[2][0])
        self.assertEqual(6 + self._max_id_lnkENTRY, approved_linkbacks[3][0])
        self.assertEqual(7 + self._max_id_lnkENTRY, approved_linkbacks[4][0])

        url = cfg['CFG_SITE_SECURE_URL'] + '/linkbacks/'
        expected_texts = ('URL1', 'URL2', 'URL5', 'URL6', 'URL7')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))
        unexpected_texts = ('URL3', 'URL4', 'URL8')
        for text in unexpected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       unexpected_text=text))

    def test_url_add(self):
        """weblinkback - test add URL to list"""
        add_url_to_list('url1', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        add_url_to_list('url2', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        add_url_to_list('url3', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)

        admin_url_table = self.get_all_from_table('lnkADMINURL')
        admin_url_log_table = self.get_all_from_table('lnkADMINURLLOG')
        log_table = self.get_all_from_table('lnkLOG')

        self.assertEqual(3, len(admin_url_table))
        self.assertEqual(3, len(admin_url_log_table))
        self.assertEqual(12, len(log_table))

        url = cfg['CFG_SITE_SECURE_URL'] + '/admin/weblinkback/weblinkbackadmin.py/lists'
        expected_texts = ('url1', 'url2', 'url3')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))

    def test_url_remove(self):
        """weblinkback - test remove URL rom list"""
        add_url_to_list('url1', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        add_url_to_list('url2', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        remove_url('url2')
        # creating a different log, might detect a bug in the logging ids
        approve_linkback(1 + self._max_id_lnkENTRY, self.user_info)
        add_url_to_list('url3', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)

        admin_url_table = self.get_all_from_table('lnkADMINURL')
        admin_url_log_table = self.get_all_from_table('lnkADMINURLLOG')
        logTable = self.get_all_from_table('lnkLOG')

        self.assertEqual(2, len(admin_url_table))
        self.assertEqual(2, len(admin_url_log_table))
        # there are more logs due to the inserted linkbacks in setUp()
        self.assertEqual(12, len(logTable))

        self.assertEqual(1 + self._max_id_lnkADMINURL, admin_url_table[0][0])
        # there are more logs due to the inserted linkbacks in setUp()
        self.assertEqual(1 + self._max_id_lnkADMINURL, admin_url_log_table[0][0])
        self.assertEqual(10 + self._max_id_lnkLOG, admin_url_log_table[0][1])

        self.assertEqual(3 + self._max_id_lnkADMINURL, admin_url_table[1][0])
        # there are more logs due to the inserted linkbacks in setUp()
        self.assertEqual(3 + self._max_id_lnkADMINURL, admin_url_log_table[1][0])
        # 9 linkbacks inserted  (9)
        # 2 urls inserted      (11)
        # 1 url removed        (11) (log id 10 removed)
        # 1 linkback approved  (12)
        # 1 url inserted       (13)
        self.assertEqual(13 + self._max_id_lnkLOG, admin_url_log_table[1][1])

        url = cfg['CFG_SITE_SECURE_URL'] + '/admin/weblinkback/weblinkbackadmin.py/lists'
        expected_texts = ('url1', 'url3')
        for text in expected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       expected_text=text))
        unexpected_texts = ('url2', )
        for text in unexpected_texts:
            self.assertEqual([], test_web_page_content(url,
                                                       username='admin',
                                                       unexpected_text=text))

    def test_url_lists(self):
        """weblinkback - test URL lists"""
        add_url_to_list('url1', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        add_url_to_list('url2', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        add_url_to_list('url3', CFG_WEBLINKBACK_LIST_TYPE['WHITELIST'], self.user_info)

        self.assertEqual(('url1', 'url2'), get_url_list(CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST']))
        self.assertEqual(('url3', ), get_url_list(CFG_WEBLINKBACK_LIST_TYPE['WHITELIST']))

        remove_url('url2')
        remove_url('url3')

        self.assertEqual(('url1', ), get_url_list(CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST']))
        self.assertEqual(tuple(), get_url_list(CFG_WEBLINKBACK_LIST_TYPE['WHITELIST']))

    def test_url_exists(self):
        """weblinkback - test URL existence"""
        add_url_to_list('url1', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        add_url_to_list('url2', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        add_url_to_list('url3', CFG_WEBLINKBACK_LIST_TYPE['WHITELIST'], self.user_info)

        self.assertTrue(url_exists('url1'))
        self.assertTrue(url_exists('url1', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST']))
        self.assertFalse(url_exists('url1', CFG_WEBLINKBACK_LIST_TYPE['WHITELIST']))

        remove_url('url1')
        self.assertFalse(url_exists('url1'))
        self.assertFalse(url_exists('url1', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST']))
        self.assertFalse(url_exists('url1', CFG_WEBLINKBACK_LIST_TYPE['WHITELIST']))

        self.assertTrue(url_exists('url3'))
        self.assertFalse(url_exists('url3', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST']))
        self.assertTrue(url_exists('url3', CFG_WEBLINKBACK_LIST_TYPE['WHITELIST']))

    def test_set_url_broken(self):
        """weblinkback - test set URL broken"""
        add_url_to_list('URL1', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        set_url_broken('URL1')
        entry_table = self.get_all_from_table('lnkENTRY')
        self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], entry_table[0][5])
        self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], entry_table[8][5])
        self.assertEqual(9, len(self.get_all_from_table("lnkENTRY")))
        self.assertEqual(11, len(self.get_all_from_table("lnkENTRYLOG")))

    def test_delete_linkbacks_on_blacklist(self):
        """weblinkback - test delete linkbacks on blacklist"""
        for linkbackid in (1, 2, 3, 4):
            approve_linkback(linkbackid + self._max_id_lnkENTRY, self.user_info)
        for linkbackid in (5, 6):
            reject_linkback(linkbackid + self._max_id_lnkENTRY, self.user_info)

        add_url_to_list('RL1', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        add_url_to_list('URL5', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        add_url_to_list('RL7', CFG_WEBLINKBACK_LIST_TYPE['BLACKLIST'], self.user_info)
        set_url_broken('URL1')
        entry_table = self.get_all_from_table('lnkENTRY')
        self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], entry_table[0][5])
        self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], entry_table[8][5])
        self.assertEqual(9, len(self.get_all_from_table("lnkENTRY")))
        self.assertEqual(17, len(self.get_all_from_table("lnkENTRYLOG")))
        self.assertEqual(20, len(self.get_all_from_table("lnkLOG")))

        delete_linkbacks_on_blacklist()
        self.assertEqual(5, len(self.get_all_from_table("lnkENTRY")))
        self.assertEqual(9, len(self.get_all_from_table("lnkENTRYLOG")))
        self.assertEqual(12, len(self.get_all_from_table("lnkLOG")))

    def test_url_xml_entity_removal(self):
        """weblinkback - URL XML entity removal"""
        url = 'This is a&nbsp;test'
        run_sql("INSERT INTO lnkENTRYURLTITLE ( url, title) VALUES ('URL1', %s)", (url,))
        self.assertEqual('This is a\xc2\xa0test', get_url_title(url))

        url = 'This &#8220;is&#8221; &nbsp;&#8220;&#8221;test&#8221;"'
        run_sql("INSERT INTO lnkENTRYURLTITLE ( url, title) VALUES ('URL2', %s)", (url,))
        self.assertEqual('This \xe2\x80\x9cis\xe2\x80\x9d \xc2\xa0\xe2\x80\x9c\xe2\x80\x9dtest\xe2\x80\x9d"', get_url_title(url))

    def test_get_pending_trackbacks(self):
        """weblinkback - get all pending trackbacks"""
        pending_trackbacks = get_all_linkbacks(linkback_type=CFG_WEBLINKBACK_TYPE['TRACKBACK'], status=CFG_WEBLINKBACK_STATUS['PENDING'])
        self.assertEqual(9, len(pending_trackbacks))
        for pending_trackback in pending_trackbacks:
            approve_linkback(pending_trackback[0], self.user_info)
        pending_trackbacks = get_all_linkbacks(linkback_type=CFG_WEBLINKBACK_TYPE['TRACKBACK'], status=CFG_WEBLINKBACK_STATUS['PENDING'])
        self.assertEqual(0, len(pending_trackbacks))

        recid = 42
        argd = {'url': 'URL',
                'title': 'My title',
                'excerpt': CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME,
                'blog_name': 'Test Blog',
                'id': CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME,
                'source': CFG_WEBLINKBACK_SUBSCRIPTION_DEFAULT_ARGUMENT_NAME,
                }
        linkbackid1 = create_trackback(recid, argd['url'], argd['title'], argd['excerpt'], argd['blog_name'], argd['id'], argd['source'], self.user_info)
        create_trackback(recid, argd['url'], argd['title'], argd['excerpt'], argd['blog_name'], argd['id'], argd['source'], self.user_info)

        pending_trackbacks = get_all_linkbacks(linkback_type=CFG_WEBLINKBACK_TYPE['TRACKBACK'], status=CFG_WEBLINKBACK_STATUS['PENDING'])
        self.assertEqual(2, len(pending_trackbacks))
        approve_linkback(linkbackid1, self.user_info)
        pending_trackbacks = get_all_linkbacks(linkback_type=CFG_WEBLINKBACK_TYPE['TRACKBACK'], status=CFG_WEBLINKBACK_STATUS['PENDING'])
        self.assertEqual(1, len(pending_trackbacks))

        create_trackback(recid, argd['url'], argd['title'], argd['excerpt'], argd['blog_name'], argd['id'], argd['source'], self.user_info)
        run_sql("INSERT INTO lnkENTRY (origin_url, id_bibrec, additional_properties, type, status, insert_time) VALUES ('URLN', 41, NULL, %s, %s, NOW())", (CFG_WEBLINKBACK_TYPE['PINGBACK'], CFG_WEBLINKBACK_STATUS['PENDING']))
        pending_trackbacks = get_all_linkbacks(linkback_type=CFG_WEBLINKBACK_TYPE['TRACKBACK'], status=CFG_WEBLINKBACK_STATUS['PENDING'])
        self.assertEqual(2, len(pending_trackbacks))


def get_title_of_page_mock1(url=""): # pylint: disable=W0613
    return "MOCK_TITLE1"


def get_title_of_page_mock2(url=""): # pylint: disable=W0613
    return "MOCK_TITLE2"


def get_title_of_page_mock_broken(url=""): # pylint: disable=W0613
    return None


class WebLinkbackUpdaterTest(InvenioTestCase):
    """Test WebLinkback updater"""

    def setUp(self):
        """Insert test data"""
        self.user_info = {'uid': 0}
        self.remove_test_data()

    def tearDown(self):
        """Remove test data"""
        self.remove_test_data()

    @nottest
    def remove_test_data(self):
        """Clean tables"""
        self._max_id_lnkENTRY = get_max_auto_increment_id('lnkENTRY')

        remove_test_data()

    def get_all_from_table(self, tableName):
        return run_sql("SELECT * FROM %s" % tableName) # kwalitee: disable=sql

    if HAS_MOCK:
        def test_update_titles_of_new_linkbacks(self):
            """weblinkback - test update titles of new linkbacks"""
            if cfg['CFG_WEBLINKBACK_TRACKBACK_ENABLED']:
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.au', title='Google'), username='admin'))
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.at'), username='admin'))
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.co.za', title='Google'), username='admin'))

                p = patch('invenio.legacy.weblinkback.get_title_of_page', get_title_of_page_mock1)
                p.start()
                update_linkbacks(1)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                self.assertEqual("Google", url_titles[0][2])
                self.assertEqual(get_title_of_page_mock1(), url_titles[1][2])
                self.assertEqual("Google", url_titles[2][2])
                p.stop()

    if HAS_MOCK:
        def test_update_titles_of_old_linkbacks(self):
            """weblinkback - test update titles of old linkbacks"""
            if cfg['CFG_WEBLINKBACK_TRACKBACK_ENABLED']:
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.au', title='Google'), username='admin'))
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.at'), username='admin'))
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.co.za', title='Google'), username='admin'))

                update_url_title("http://www.google.au", "Google AU")

                p = patch('invenio.legacy.weblinkback.get_title_of_page', get_title_of_page_mock1)
                p.start()
                update_linkbacks(2)
                url_entries = self.get_all_from_table("lnkENTRYURLTITLE")
                self.assertEqual(get_title_of_page_mock1(), url_entries[0][2])
                self.assertEqual("", url_entries[1][2])
                self.assertEqual("Google", url_entries[2][2])
                update_linkbacks(1)
                p.stop()

                p = patch('invenio.legacy.weblinkback.get_title_of_page', get_title_of_page_mock2)
                p.start()
                update_linkbacks(2)
                url_entries = self.get_all_from_table("lnkENTRYURLTITLE")
                self.assertEqual(get_title_of_page_mock2(), url_entries[0][2])
                self.assertEqual(get_title_of_page_mock2(), url_entries[1][2])
                self.assertEqual("Google", url_entries[2][2])
                p.stop()

    if HAS_MOCK:
        def test_update_manually_set_page_titles(self):
            """weblinkback - test update manually set page titles"""
            if cfg['CFG_WEBLINKBACK_TRACKBACK_ENABLED']:
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.au', title='Google'), username='admin'))
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.at'), username='admin'))
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.co.za', title='Google'), username='admin'))

                p = patch('invenio.legacy.weblinkback.get_title_of_page', get_title_of_page_mock1)
                p.start()
                update_linkbacks(3)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                self.assertEqual(get_title_of_page_mock1(), url_titles[0][2])
                self.assertEqual("", url_titles[1][2])
                self.assertEqual(get_title_of_page_mock1(), url_titles[2][2])
                p.stop()

    if HAS_MOCK:
        def test_detect_and_disable_broken_linkbacks(self):
            """weblinkback - test detect and disable broken linkbacks"""
            if cfg['CFG_WEBLINKBACK_TRACKBACK_ENABLED']:
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.au', title='Google'), username='admin'))
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.at'), username='admin'))
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.co.za', title='GoogleCOZA'), username='admin'))
                self.assertNotEqual([], test_web_page_content(url_for('weblinkback.sendtrackback', recid=30, url='http://www.google.co.za', title='Google'), username='admin'))

                run_sql("""INSERT INTO lnkENTRYURLTITLE (url, title, manual_set, broken_count)
                              VALUES
                              (%s, %s, %s, %s)
                        """, ("http://www.google.de", "Google DE", 0, 3))

                p = patch('invenio.legacy.weblinkback.get_title_of_page', get_title_of_page_mock_broken)
                p.start()
                update_linkbacks(4)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                linkback_entries = self.get_all_from_table("lnkENTRY")
                self.assertEqual("Google", url_titles[0][2])
                self.assertEqual(1, url_titles[0][4])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[0][5])
                self.assertEqual("", url_titles[1][2])
                self.assertEqual(1, url_titles[1][4])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[1][5])
                self.assertEqual("GoogleCOZA", url_titles[2][2])
                self.assertEqual(1, url_titles[2][4])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[3][5])
                self.assertEqual("Google DE", url_titles[3][2])
                self.assertEqual(4, url_titles[3][4])

                update_linkbacks(4)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                linkback_entries = self.get_all_from_table("lnkENTRY")
                self.assertEqual("Google", url_titles[0][2])
                self.assertEqual(2, url_titles[0][4])
                self.assertEqual(0, url_titles[0][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[0][5])
                self.assertEqual("", url_titles[1][2])
                self.assertEqual(2, url_titles[1][4])
                self.assertEqual(0, url_titles[1][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[1][5])
                self.assertEqual("GoogleCOZA", url_titles[2][2])
                self.assertEqual(2, url_titles[2][4])
                self.assertEqual(0, url_titles[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[3][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[3][2])
                self.assertEqual(5, url_titles[3][4])
                self.assertEqual(1, url_titles[3][5])

                update_linkbacks(4)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                linkback_entries = self.get_all_from_table("lnkENTRY")
                self.assertEqual("Google", url_titles[0][2])
                self.assertEqual(3, url_titles[0][4])
                self.assertEqual(0, url_titles[0][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[0][5])
                self.assertEqual("", url_titles[1][2])
                self.assertEqual(3, url_titles[1][4])
                self.assertEqual(0, url_titles[1][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[1][5])
                self.assertEqual("GoogleCOZA", url_titles[2][2])
                self.assertEqual(3, url_titles[2][4])
                self.assertEqual(0, url_titles[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[3][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[3][2])
                self.assertEqual(5, url_titles[3][4])
                self.assertEqual(1, url_titles[3][5])
                p.stop()

                p = patch('invenio.legacy.weblinkback.get_title_of_page', get_title_of_page_mock1)
                p.start()
                update_linkbacks(1)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                linkback_entries = self.get_all_from_table("lnkENTRY")
                self.assertEqual("Google", url_titles[0][2])
                self.assertEqual(3, url_titles[0][4])
                self.assertEqual(0, url_titles[0][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[0][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[1][2])
                self.assertEqual(0, url_titles[1][4])
                self.assertEqual(0, url_titles[1][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[1][5])
                self.assertEqual("GoogleCOZA", url_titles[2][2])
                self.assertEqual(3, url_titles[2][4])
                self.assertEqual(0, url_titles[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[3][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[3][2])
                self.assertEqual(5, url_titles[3][4])
                self.assertEqual(1, url_titles[3][5])

                approve_linkback(4 + self._max_id_lnkENTRY, self.user_info)

                update_linkbacks(3)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                linkback_entries = self.get_all_from_table("lnkENTRY")
                self.assertEqual(get_title_of_page_mock1(), url_titles[0][2])
                self.assertEqual(0, url_titles[0][4])
                self.assertEqual(0, url_titles[0][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[0][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[1][2])
                self.assertEqual(0, url_titles[1][4])
                self.assertEqual(0, url_titles[1][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[1][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[2][2])
                self.assertEqual(0, url_titles[2][4])
                self.assertEqual(0, url_titles[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['APPROVED'], linkback_entries[3][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[3][2])
                self.assertEqual(5, url_titles[3][4])
                self.assertEqual(1, url_titles[3][5])
                p.stop()

                p = patch('invenio.legacy.weblinkback.get_title_of_page', get_title_of_page_mock_broken)
                p.start()
                update_linkbacks(4)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                linkback_entries = self.get_all_from_table("lnkENTRY")
                self.assertEqual(get_title_of_page_mock1(), url_titles[0][2])
                self.assertEqual(1, url_titles[0][4])
                self.assertEqual(0, url_titles[0][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[0][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[1][2])
                self.assertEqual(1, url_titles[1][4])
                self.assertEqual(0, url_titles[1][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[1][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[2][2])
                self.assertEqual(1, url_titles[2][4])
                self.assertEqual(0, url_titles[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['APPROVED'], linkback_entries[3][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[3][2])
                self.assertEqual(5, url_titles[3][4])
                self.assertEqual(1, url_titles[3][5])

                reject_linkback(1 + self._max_id_lnkENTRY, self.user_info)
                reject_linkback(3 + self._max_id_lnkENTRY, self.user_info)

                update_linkbacks(4)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                linkback_entries = self.get_all_from_table("lnkENTRY")
                self.assertEqual(get_title_of_page_mock1(), url_titles[0][2])
                self.assertEqual(2, url_titles[0][4])
                self.assertEqual(0, url_titles[0][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['REJECTED'], linkback_entries[0][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[1][2])
                self.assertEqual(2, url_titles[1][4])
                self.assertEqual(0, url_titles[1][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[1][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[2][2])
                self.assertEqual(2, url_titles[2][4])
                self.assertEqual(0, url_titles[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['REJECTED'], linkback_entries[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['APPROVED'], linkback_entries[3][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[3][2])
                self.assertEqual(5, url_titles[3][4])
                self.assertEqual(1, url_titles[3][5])

                update_linkbacks(4)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                linkback_entries = self.get_all_from_table("lnkENTRY")
                self.assertEqual(get_title_of_page_mock1(), url_titles[0][2])
                self.assertEqual(3, url_titles[0][4])
                self.assertEqual(0, url_titles[0][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['REJECTED'], linkback_entries[0][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[1][2])
                self.assertEqual(3, url_titles[1][4])
                self.assertEqual(0, url_titles[1][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[1][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[2][2])
                self.assertEqual(3, url_titles[2][4])
                self.assertEqual(0, url_titles[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['REJECTED'], linkback_entries[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['APPROVED'], linkback_entries[3][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[3][2])
                self.assertEqual(5, url_titles[3][4])
                self.assertEqual(1, url_titles[3][5])

                update_linkbacks(4)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                linkback_entries = self.get_all_from_table("lnkENTRY")
                self.assertEqual(get_title_of_page_mock1(), url_titles[0][2])
                self.assertEqual(4, url_titles[0][4])
                self.assertEqual(0, url_titles[0][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['REJECTED'], linkback_entries[0][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[1][2])
                self.assertEqual(4, url_titles[1][4])
                self.assertEqual(0, url_titles[1][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['PENDING'], linkback_entries[1][5])
                self.assertEqual(get_title_of_page_mock1(), url_titles[2][2])
                self.assertEqual(4, url_titles[2][4])
                self.assertEqual(0, url_titles[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['REJECTED'], linkback_entries[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['APPROVED'], linkback_entries[3][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[3][2])
                self.assertEqual(5, url_titles[3][4])
                self.assertEqual(1, url_titles[3][5])

                update_linkbacks(4)
                url_titles = self.get_all_from_table("lnkENTRYURLTITLE")
                linkback_entries = self.get_all_from_table("lnkENTRY")
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[0][2])
                self.assertEqual(5, url_titles[0][4])
                self.assertEqual(1, url_titles[0][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], linkback_entries[0][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[1][2])
                self.assertEqual(5, url_titles[1][4])
                self.assertEqual(1, url_titles[1][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], linkback_entries[1][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[2][2])
                self.assertEqual(5, url_titles[2][4])
                self.assertEqual(1, url_titles[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], linkback_entries[2][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], linkback_entries[3][5])
                self.assertEqual(CFG_WEBLINKBACK_STATUS['BROKEN'], url_titles[3][2])
                self.assertEqual(5, url_titles[3][4])
                self.assertEqual(1, url_titles[3][5])
                p.stop()


TEST_SUITE = make_test_suite(WebLinkbackWebPagesAvailabilityTest,
                             WebLinkbackDatabaseTest,
                             WebLinkbackUpdaterTest,
                             )


if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
