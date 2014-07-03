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

"""WebMessage Regression Test Suite."""

__revision__ = "$Id$"

from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages, \
                              InvenioTestCase
webmessage = lazy_import('invenio.legacy.webmessage.api')

CFG_WEBMESSAGE_STATUS_CODE = lazy_import('invenio.modules.messages.query:CFG_WEBMESSAGE_STATUS_CODE')
check_quota = lazy_import('invenio.modules.messages.query:check_quota')
count_nb_messages = lazy_import('invenio.modules.messages.query:count_nb_messages')
create_message = lazy_import('invenio.modules.messages.query:create_message')
datetext_default = lazy_import('invenio.modules.messages.query:datetext_default')
delete_all_messages = lazy_import('invenio.modules.messages.query:delete_all_messages')
delete_message_from_user_inbox = lazy_import('invenio.modules.messages.query:delete_message_from_user_inbox')
get_all_messages_for_user = lazy_import('invenio.modules.messages.query:get_all_messages_for_user')
get_gids_from_groupnames = lazy_import('invenio.modules.messages.query:get_gids_from_groupnames')
get_groupnames_like = lazy_import('invenio.modules.messages.query:get_groupnames_like')
get_nb_new_messages_for_user = lazy_import('invenio.modules.messages.query:get_nb_new_messages_for_user')
get_nb_readable_messages_for_user = lazy_import('invenio.modules.messages.query:get_nb_readable_messages_for_user')
get_nicknames_like = lazy_import('invenio.modules.messages.query:get_nicknames_like')
get_nicks_from_uids = lazy_import('invenio.modules.messages.query:get_nicks_from_uids')
get_uids_from_emails = lazy_import('invenio.modules.messages.query:get_uids_from_emails')
get_uids_from_nicks = lazy_import('invenio.modules.messages.query:get_uids_from_nicks')
get_uids_members_of_groups = lazy_import('invenio.modules.messages.query:get_uids_members_of_groups')
send_message = lazy_import('invenio.modules.messages.query:send_message')
set_message_status = lazy_import('invenio.modules.messages.query:set_message_status')
user_exists = lazy_import('invenio.modules.messages.query:user_exists')


class WebMessageWebPagesAvailabilityTest(InvenioTestCase):
    """Check WebMessage web pages whether they are up or not."""

    def test_your_message_pages_availability(self):
        """webmessage - availability of Your Messages pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/yourmessages/'

        _exports = ['', 'display', 'write', 'send', 'delete', 'delete_all',
                    'display_msg']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url,
                                                        username='jekyll',
                                                        password='j123ekyll'))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

class WebMessageSendingAndReceivingMessageTest(InvenioTestCase):
    """Check sending and receiving message throught WebMessage"""

    def test_sending_message(self):
        """webmessage - send and receive a message"""
        # juliet writes the message to romeo
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        # it is verified that romeo received the message
        result = get_all_messages_for_user(5)
        self.assertEqual("Hi romeo", result[0].subject)
        self.assertEqual("juliet", result[0].user_from.nickname)
        webmessage.perform_request_delete_msg(5, result[0].id, ln=cfg['CFG_SITE_LANG'])

    def test_setting_message_status(self):
        """webmessage - status from "new" to "read" """
        # juliet writes the message to romeo
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        msgid =  get_all_messages_for_user(5)[0].id
        # status is changed
        set_message_status(5, msgid, 'R')
        msgstatus = get_all_messages_for_user(5)[0].sent_to_users[0].status
        self.assertEqual(msgstatus, 'R')
        webmessage.perform_request_delete_msg(5, msgid, ln=cfg['CFG_SITE_LANG'])

    def test_getting_nb_new_msg(self):
        """webmessage - count the nb of new message"""
        delete_all_messages(5)
        # juliet writes the message to romeo
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        self.assertEqual(get_nb_new_messages_for_user(5), 1)

    def test_getting_nb_readable_messages(self):
        """webmessage - get the nb of readable messages"""
        delete_all_messages(5)
        # juliet writes the message to romeo
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        msgid =  get_all_messages_for_user(5)[0].id
        # status is changed
        set_message_status(5, msgid, 'R')
        self.assertEqual(get_nb_readable_messages_for_user(5), 1)
        webmessage.perform_request_delete_msg(5, msgid, ln=cfg['CFG_SITE_LANG'])

    def test_getting_all_messages_for_user(self):
        """webmessage - get all message for user"""
        delete_all_messages(5)
        # juliet writes 3 messages to romeo
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        self.assertEqual(len(get_all_messages_for_user(5)), 3)
        delete_all_messages(5)

    def test_count_nb_message(self):
        """webmessage - count the number of messages"""
        delete_all_messages(5)
        # juliet writes 3 messages to romeo
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        self.assertEqual(count_nb_messages(5), 3)
        delete_all_messages(5)
        self.assertEqual(count_nb_messages(5), 0)


    def test_delete_message_from_user_inbox(self):
        """webmessage - delete message from user inbox"""
        delete_all_messages(5)
        # juliet writes a message to romeo
        webmessage.perform_request_send(6,
                                        msg_to_user="romeo",
                                        msg_to_group="",
                                        msg_subject="Hi romeo",
                                        msg_body="hello romeo how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        msg_id = get_all_messages_for_user(5)[0].id
        delete_message_from_user_inbox(5, msg_id)
        self.assertEqual(count_nb_messages(5), 0)

    def test_create_message(self):
        """webmessage - create msg but do not send it"""
        msgid = create_message(6,
                               users_to_str="romeo",
                               groups_to_str="montague-family",
                               msg_subject="hello",
                               msg_body="how are you",
                               msg_send_on_date=datetext_default)
        send_message(5, msgid, status=CFG_WEBMESSAGE_STATUS_CODE['NEW'])
        result = get_all_messages_for_user(5)
        self.assertEqual(msgid, result[0].id)
        delete_all_messages(2)

    def test_send_message(self):
        """webmessage - sending message using uid msgid"""
        #create a message to know the msgid
        msgid = create_message(6,
                               users_to_str="romeo",
                               groups_to_str="montague-family",
                               msg_subject="hello",
                               msg_body="how are you",
                               msg_send_on_date=datetext_default)
        send_message(5, msgid, status=CFG_WEBMESSAGE_STATUS_CODE['NEW'])
        result = get_all_messages_for_user(5)
        self.assertEqual("hello", result[0].subject)
        webmessage.perform_request_delete_msg(5, result[0].id, ln=cfg['CFG_SITE_LANG'])

    def test_check_quota(self):
        """webmessage - you give a quota, it returns users over-quota"""
        webmessage.perform_request_send(6,
                                        msg_to_user="jekyll",
                                        msg_to_group="",
                                        msg_subject="Hi jekyll",
                                        msg_body="hello how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        webmessage.perform_request_send(6,
                                        msg_to_user="jekyll",
                                        msg_to_group="",
                                        msg_subject="Hi jekyll",
                                        msg_body="hello how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        webmessage.perform_request_send(6,
                                        msg_to_user="jekyll",
                                        msg_to_group="",
                                        msg_subject="Hi jekyll",
                                        msg_body="hello how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        webmessage.perform_request_send(6,
                                        msg_to_user="jekyll",
                                        msg_to_group="",
                                        msg_subject="Hi jekyll",
                                        msg_body="hello how are you?",
                                        ln=cfg['CFG_SITE_LANG'])
        d = check_quota(3)
        self.assertEqual(d.keys()[0], 2)
        delete_all_messages(2)


class WebMessageGettingUidsGidsTest(InvenioTestCase):
    """Many way to get uids or gids"""

    def test_get_uids_from_nicks(self):
        """webmessage - get uid from nick"""
        d = get_uids_from_nicks('juliet')
        self.assertEqual(d.get('juliet'), 6)

    def test_get_nicks_from_uids(self):
        """webmessage - get nick from uid"""
        d = get_nicks_from_uids(6)
        self.assertEqual(d.get(6), 'juliet')

    def test_get_uids_from_emails(self):
        """webmessage - get uid from email"""
        d = get_uids_from_emails('juliet.capulet@cds.cern.ch')
        self.assertEqual(d.get('juliet.capulet@cds.cern.ch'), 6)

    def test_get_gids_from_groupnames(self):
        """webmessage - get gid from groupname"""
        d =  get_gids_from_groupnames('montague-family')
        self.assertEqual(d.get('montague-family'), 2)

    def test_get_uids_members_of_groups(self):
        """webmessage - get uids members of group"""
        uids = get_uids_members_of_groups(2)
        self.assertEqual(uids[0], 5)
        self.assertEqual(uids[1], 6)
        self.assertEqual(uids[2], 7)

    def test_user_exists(self):
        """webmessage - check if a user exist"""
        self.assertEqual(user_exists(6), 1)

class WebMessagePatternTest(InvenioTestCase):
    """pattern"""

    def test_get_nicknames_like(self):
        """webmessage - get nickname"""
        result = get_nicknames_like('j.')
        self.assertEqual(result[0], ('jekyll',))
        self.assertEqual(result[1], ('juliet',))
        result = get_nicknames_like('j+')
        self.assertEqual(result[0], ('jekyll',))
        self.assertEqual(result[1], ('juliet',))

    def test_get_groupnames_like(self):
        """webmessage - get groupname"""
        d = get_groupnames_like(5,'mont+')
        self.assertEqual(d.keys()[0], 2L)
        self.assertEqual(d.values()[0], 'montague-family')

TEST_SUITE = make_test_suite(WebMessageWebPagesAvailabilityTest,
                             WebMessageSendingAndReceivingMessageTest,
                             WebMessageGettingUidsGidsTest,
                             WebMessagePatternTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
