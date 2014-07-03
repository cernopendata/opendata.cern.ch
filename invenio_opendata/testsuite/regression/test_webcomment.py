# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2006, 2007, 2008, 2010, 2011, 2012, 2013 CERN.
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

"""WebComment Regression Test Suite."""

__revision__ = "$Id$"

from invenio.testsuite import InvenioTestCase
import shutil
from flask import url_for
from mechanize import Browser, HTTPError
from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages, \
                              InvenioTestCase
from invenio.utils.htmlwasher import EmailWasher

run_sql = lazy_import('invenio.legacy.dbquery:run_sql')


def prepare_attachments():
    """
    We copy necessary files to temporary directory. Every time we will
    attach files to a comment, these files get moved, so this function
    must be called again.
    """
    shutil.copy(cfg['CFG_WEBDIR'] + '/img/journal_water_dog.gif', cfg['CFG_TMPDIR'])
    shutil.copy(cfg['CFG_WEBDIR'] + '/css/invenio.css', cfg['CFG_TMPDIR'])


class WebCommentWebPagesAvailabilityTest(InvenioTestCase):
    """Check WebComment web pages whether they are up or not."""

    def test_your_baskets_pages_availability(self):
        """webcomment - availability of comments pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/%s/10/comments/' % cfg['CFG_SITE_RECORD']
        basesecureurl = cfg['CFG_SITE_SECURE_URL'] + '/%s/10/comments/' % cfg['CFG_SITE_RECORD']

        _exports = ['', 'display', 'vote', 'report']
        _auth_exports = ['add']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url))
        for url in [basesecureurl + page for page in _auth_exports]:
            error_messages.extend(test_web_page_content(url, username='admin'))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_webcomment_admin_interface_availability(self):
        """webcomment - availability of WebComment Admin interface pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/admin/webcomment/webcommentadmin.py/'

        _exports = ['', 'comments', 'delete', 'users']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            # first try as guest:
            error_messages.extend(test_web_page_content(url,
                                                        username='guest',
                                                        expected_text=
                                                        'Authorization failure'))
            # then try as admin:
            error_messages.extend(test_web_page_content(url,
                                                        username='admin'))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_webcomment_admin_guide_availability(self):
        """webcomment - availability of WebComment Admin Guide"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/help/admin/webcomment-admin-guide',
                                               expected_text="WebComment Admin Guide"))
        return

    def test_webcomment_mini_review_availability(self):
        """webcomment - availability of mini-review panel on detailed record page"""
        url = cfg['CFG_SITE_URL'] + '/%s/12' % cfg['CFG_SITE_RECORD']
        error_messages = test_web_page_content(url,
                                               expected_text="(Not yet reviewed)")


class WebCommentRestrictionsTest(InvenioTestCase):
    """Check WebComment restrictions"""

    def setUp(self):
        """Insert some comments in some records"""
        from invenio.modules.comments.api import query_add_comment_or_remark
        from invenio.legacy.webcomment.adminlib import query_delete_comment_auth

        # Comments have access restrictions when:
        # - the comment is in a restricted collection ('viewrestrcoll' action)
        # - the comment is in a restricted discussion page ('viewcomment' action)
        # - the comment itself is restricted ('viewrestrcomment'
        #   action), either because of the markup of the record, or
        #   because it is a reply to a restricted comment.

        self.public_record = 5
        self.public_record_restr_comment = 6
        self.restr_record = 42
        self.restr_record_restr_comment = 41
        self.restricted_discussion = 76

        self.romeo_uid = 5
        self.jekyll_uid = 2
        self.attached_files = {'file1': cfg['CFG_TMPDIR'] + '/journal_water_dog.gif',
                               'file2': cfg['CFG_TMPDIR'] + '/invenio.css'}

        # Load content of texual file2
        prepare_attachments()
        fp = file(self.attached_files['file2'])
        self.attached_file2_content = fp.read()
        fp.close()

        # Insert a public comment in a public record (public collection)
        self.msg1 = "A test comment 1"
        self.public_comid = query_add_comment_or_remark(reviews=0, recID=self.public_record,
                                                        uid=self.romeo_uid, msg=self.msg1,
                                                        editor_type='textarea',
                                                        attached_files=self.attached_files)

        # Insert a public comment in a restricted record (restricted collection)
        self.msg2 = "A test comment 2"
        prepare_attachments()
        self.restr_comid_1 = \
                           query_add_comment_or_remark(reviews=0, recID=self.restr_record,
                                                       uid=self.jekyll_uid, msg=self.msg2,
                                                       editor_type='textarea',
                                                       attached_files=self.attached_files)

        # Insert a restricted comment in a public collection
        self.msg3 = "A test comment 3"
        prepare_attachments()
        self.restr_comid_2 = \
                           query_add_comment_or_remark(reviews=0, recID=self.public_record_restr_comment,
                                                       uid=self.jekyll_uid, msg=self.msg3,
                                                       editor_type='textarea',
                                                       attached_files=self.attached_files)

        # Insert a restricted comment, in a restricted collection
        self.msg5 = "A test comment 5"
        prepare_attachments()
        self.restr_comid_4 = \
                           query_add_comment_or_remark(reviews=0, recID=self.restr_record_restr_comment,
                                                       uid=self.romeo_uid, msg=self.msg5,
                                                       editor_type='textarea',
                                                       attached_files=self.attached_files)

        # Insert a public comment in a restricted discussion
        self.msg6 = "A test comment 6"
        prepare_attachments()
        self.restr_comid_5 = \
                           query_add_comment_or_remark(reviews=0, recID=self.restricted_discussion,
                                                       uid=self.romeo_uid, msg=self.msg6,
                                                       editor_type='textarea',
                                                       attached_files=self.attached_files)
        self.restr_comid_3 = None

        # Insert a public, deleted comment in a public record (public collection)
        self.msg7 = "A test comment 7"
        prepare_attachments()
        self.deleted_comid = query_add_comment_or_remark(reviews=0, recID=self.public_record,
                                                        uid=self.romeo_uid, msg=self.msg7,
                                                        editor_type='textarea',
                                                        attached_files=self.attached_files)
        query_delete_comment_auth(self.deleted_comid)

    def tearDown(self):
        """Remove inserted comments"""
        run_sql("""DELETE FROM cmtRECORDCOMMENT WHERE id=%s""", (self.public_comid,))
        run_sql("""DELETE FROM cmtRECORDCOMMENT WHERE id=%s""", (self.restr_comid_1,))
        run_sql("""DELETE FROM cmtRECORDCOMMENT WHERE id=%s""", (self.restr_comid_2,))
        if self.restr_comid_3:
            run_sql("""DELETE FROM cmtRECORDCOMMENT WHERE id=%s""", (self.restr_comid_3,))
        run_sql("""DELETE FROM cmtRECORDCOMMENT WHERE id=%s""", (self.restr_comid_4,))
        run_sql("""DELETE FROM cmtRECORDCOMMENT WHERE id=%s""", (self.restr_comid_5,))
        run_sql("""DELETE FROM cmtRECORDCOMMENT WHERE id=%s""", (self.deleted_comid,))
        pass

    def test_access_public_record_public_discussion_public_comment(self):
        """webcomment - accessing "public" comment in a "public" discussion of a restricted record"""
        # Guest user should not be able to access it
        self.assertNotEqual([],
                         test_web_page_content("%s/%s/%i/comments/" % (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record),
                                               expected_text=self.msg2))

        # Accessing a non existing file for a restricted comment should also ask to login
        self.assertEqual([],
                         test_web_page_content("%s/%s/%i/comments/attachments/get/%i/not_existing_file" % \
                                               (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record, self.restr_comid_1),
                                               expected_text='You are not authorized to perform this action'))

        # Check accessing file of a restricted comment
        self.assertEqual([],
                         test_web_page_content("%s/%s/%i/comments/attachments/get/%i/file2" % \
                                               (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record, self.restr_comid_1),
                                               expected_text='You are not authorized to perform this action'))


    def test_access_restricted_record_public_discussion_public_comment(self):
        """webcomment - accessing "public" comment in a "public" discussion of a restricted record"""
        # Guest user should not be able to access it
        self.assertNotEqual([],
                         test_web_page_content("%s/%s/%i/comments/" % (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record),
                                               expected_text=self.msg2))

        # Accessing a non existing file for a restricted comment should also ask to login
        self.assertEqual([],
                         test_web_page_content("%s/%s/%i/comments/attachments/get/%i/not_existing_file" % \
                                               (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record, self.restr_comid_1),
                                               expected_text='You are not authorized to perform this action'))

        # Check accessing file of a restricted comment
        self.assertEqual([],
                         test_web_page_content("%s/%s/%i/comments/attachments/get/%i/file2" % \
                                               (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record, self.restr_comid_1),
                                               expected_text='You are not authorized to perform this action'))

        # Juliet should not be able to access the comment
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/" % (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record))
        response = response.data
        if not self.msg2 in response:
            pass
        else:
            self.fail("Oops, this user should not have access to this comment")

        # Juliet should not be able to access the attached files
        response = self.client.get("%s/%s/%i/comments/attachments/get/%i/file2" % \
                     (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record, self.restr_comid_1))
        response = response.data
        if "You are not authorized" in response:
            pass
        else:
            self.fail("Oops, this user should not have access to this comment attachment")

        # Jekyll should be able to access the comment
        self.login('jekyll', 'j123ekyll')
        response = self.client.get("%s/%s/%i/comments/" % (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record))
        response = response.data
        if not self.msg2 in response:
            self.fail("Oops, this user should have access to this comment")

        # Jekyll should be able to access the attached files
        response = self.client.get("%s/%s/%i/comments/attachments/get/%i/file2" % \
                     (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record, self.restr_comid_1))
        response = response.data
        self.assertEqual(self.attached_file2_content, response)

    def test_access_public_record_restricted_discussion_public_comment(self):
        """webcomment - accessing "public" comment in a restricted discussion of a public record"""
        # Guest user should not be able to access it
        self.assertNotEqual([],
                         test_web_page_content("%s/%s/%i/comments/" % (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], self.restricted_discussion),
                                               expected_text=self.msg2))

        # Accessing a non existing file for a restricted comment should also ask to login
        self.assertEqual([],
                         test_web_page_content("%s/%s/%i/comments/attachments/get/%i/not_existing_file" % \
                                               (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], self.restricted_discussion, self.restr_comid_5),
                                               expected_text='You are not authorized to perform this action'))

        # Check accessing file of a restricted comment
        self.assertEqual([],
                         test_web_page_content("%s/%s/%i/comments/attachments/get/%i/file2" % \
                                               (cfg['CFG_SITE_URL'], cfg['CFG_SITE_RECORD'], self.restricted_discussion, self.restr_comid_5),
                                               expected_text='You are not authorized to perform this action'))

        # Juliet should not be able to access the comment
        self.login('juliet', 'j123uliet')
        response = self.client.get(url_for('comments.comments', recid=self.restricted_discussion, _external=True, _scheme='https'))
        self.assertNotIn(self.msg6, response.data)

        # Juliet should not be able to access the attached files
        response = self.client.get("%s/%s/%i/comments/attachments/get/%i/file2" % \
                     (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restricted_discussion, self.restr_comid_5))
        self.assertIn("You are not authorized", response.data)

        # Romeo should be able to access the comment
        self.login('romeo', 'r123omeo')
        response = self.client.get(url_for('comments.comments', recid=self.restricted_discussion, _external=True, _scheme='https'))
        self.assertIn(self.msg6, response.data)

        # Romeo should be able to access the attached files
        response = self.client.get("/%s/%i/comments/attachments/get/%i/file2" % \
                     (cfg['CFG_SITE_RECORD'], self.restricted_discussion, self.restr_comid_5))
        self.assertEqual(self.attached_file2_content, response.data)

    def test_comment_replies_inherit_restrictions(self):
        """webcomment - a reply to a comment inherits restrictions"""
        # In this test we reply to a restricted comment, and check if
        # the restriction is inherited. However, in order to make sure
        # that the comment restriction is inherited, and not the
        # record restriction, we temporary change the restriction of
        # the parent.
        from invenio.modules.comments.api import query_add_comment_or_remark

        self.public_record_restr_comment
        original_restriction = run_sql("SELECT restriction FROM cmtRECORDCOMMENT WHERE id=%s",
                                       (self.restr_comid_2,))[0][0]
        restriction_to_inherit = 'juliet_only'
        run_sql("UPDATE cmtRECORDCOMMENT SET restriction=%s WHERE id=%s",
                (restriction_to_inherit, self.restr_comid_2))

        # Reply to a restricted comment
        self.msg4 = "A test comment 4"
        prepare_attachments()
        self.restr_comid_3 = \
                           query_add_comment_or_remark(reviews=0, recID=self.public_record_restr_comment,
                                                       uid=self.jekyll_uid, msg=self.msg4,
                                                       editor_type='textarea',
                                                       attached_files=self.attached_files,
                                                       reply_to=self.restr_comid_2)

        inherited_restriction = run_sql("SELECT restriction FROM cmtRECORDCOMMENT WHERE id=%s",
                                        (self.restr_comid_3,))[0][0]

        self.assertEqual(restriction_to_inherit, inherited_restriction)

        # Restore original restriction
        run_sql("UPDATE cmtRECORDCOMMENT SET restriction=%s WHERE id=%s",
                (original_restriction, self.restr_comid_2))

    def test_comment_reply_with_wrong_record(self):
        """webcomment - replying to comment using mismatching recid"""
        # Juliet should not be able to reply to the comment, even through a public record
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/add?in_reply=%s&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.restr_comid_1))
        response = response.data
        if not self.msg2 in response and \
               "Authorization failure" in response:
            pass
        else:
            self.fail("Oops, users should not be able to reply to comment using mismatching recid")

        # Jekyll should also not be able to reply the comment using the wrong recid
        self.login('jekyll', 'j123ekyll')
        response = self.client.get("%s/%s/%i/comments/add?in_reply=%s&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.restr_comid_1))
        response = response.data
        if not self.msg2 in response and \
               "Authorization failure" in response:
            pass
        else:
            self.fail("Oops, users should not be able to reply to comment using mismatching recid")

    def test_comment_access_attachment_with_wrong_record(self):
        """webcomment - accessing attachments using mismatching recid"""
        # Juliet should not be able to access these files, especially with wrong recid
        self.login('juliet', 'j123uliet')
        try:
            response = self.client.get("%s/%s/%i/comments/attachments/get/%i/file2" % \
                     (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.restr_comid_1))
            response = response.data
        except HTTPError:
            pass
        else:
            self.fail("Oops, users should not be able to access comment attachment using mismatching recid")

        # Jekyll should also not be able to access these files when using wrong recid
        self.login('jekyll', 'j123ekyll')
        try:
            response = self.client.get("%s/%s/%i/comments/attachments/get/%i/file2" % \
                     (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.restr_comid_1))
            response = response.data
        except HTTPError:
            pass
        else:
            self.fail("Oops, users should not be able to access comment attachment using mismatching recid")

    def test_comment_reply_to_deleted_comment(self):
        """webcomment - replying to a deleted comment"""
        # Juliet should not be able to reply to the deleted comment
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/add?in_reply=%s&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.deleted_comid))
        response = response.data
        if not self.msg7 in response:
            # There should be no authorization failure, in case the
            # comment was deleted in between. We'll simply go on but
            # the orginal comment will not be included
            pass
        else:
            self.fail("Oops, users should not be able to reply to a deleted comment")

        # Jekyll should also not be able to reply the deleted comment
        self.login('jekyll', 'j123ekyll')
        response = self.client.get("%s/%s/%i/comments/add?in_reply=%s&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.deleted_comid))
        response = response.data
        if not self.msg7 in response:
            # There should be no authorization failure, in case the
            # comment was deleted in between. We'll simply go on but
            # the orginal comment will not be included
            pass
        else:
            self.fail("Oops, users should not be able to reply to a deleted comment")

    def test_comment_access_files_deleted_comment(self):
        """webcomment - access files of a deleted comment"""
        # Juliet should not be able to access the files
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/attachments/get/%i/file2" % \
                     (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.deleted_comid))
        response = response.data
        if "You cannot access files of a deleted comment" in response:
            pass
        else:
            self.fail("Oops, users should not have access to this deleted comment attachment")

        # Jekyll should also not be able to access the files
        self.login('jekyll', 'j123ekyll')
        response = self.client.get("%s/%s/%i/comments/attachments/get/%i/file2" % \
                     (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.deleted_comid))
        response = response.data
        if "Authorization failure" in response:
            pass
        else:
            self.fail("Oops, users should not have access to this deleted comment attachment")

    def test_comment_report_deleted_comment(self):
        """webcomment - report a deleted comment"""
        # Juliet should not be able to report a the deleted comment
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/report?comid=%s&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.deleted_comid))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, users should not be able to report a deleted comment")

    def test_comment_vote_deleted_comment(self):
        """webcomment - report a deleted comment"""
        # Juliet should not be able to vote for a the deleted comment/review
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/vote?comid=%s&com_value=1&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.deleted_comid))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, users should not be able to vote for a deleted comment")

    def test_comment_report_with_wrong_record(self):
        """webcomment - report a comment using mismatching recid"""
        # Juliet should not be able to report a comment she cannot access, even through public recid
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/report?comid=%s&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.restr_comid_1))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, users should not be able to report using mismatching recid")

        # Jekyll should also not be able to report the comment using the wrong recid
        self.login('jekyll', 'j123ekyll')
        response = self.client.get("%s/%s/%i/comments/report?comid=%s&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.restr_comid_1))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, users should not be able to report using mismatching recid")

    def test_comment_vote_with_wrong_record(self):
        """webcomment - vote for a comment using mismatching recid"""
        # Juliet should not be able to vote for a comment she cannot access, especially through public recid
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/vote?comid=%s&com_value=1&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.restr_comid_1))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, this user should not be able to report a deleted comment")

        # Jekyll should also not be able to vote for the comment using the wrong recid
        self.login('jekyll', 'j123ekyll')
        response = self.client.get("%s/%s/%i/comments/vote?comid=%s&com_value=1&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record, self.restr_comid_1))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, users should not be able to report using mismatching recid")

    def test_report_restricted_record_public_discussion_public_comment(self):
        """webcomment - report a comment restricted by 'viewrestrcoll'"""
        # Juliet should not be able to report the comment
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/report?comid=%s&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record, self.restr_comid_1))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, this user should not be able to report this comment")

    def test_report_public_record_restricted_discussion_public_comment(self):
        """webcomment - report a comment restricted by 'viewcomment'"""
        # Juliet should not be able to report the comment
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/report?comid=%s&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restricted_discussion, self.restr_comid_5))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, this user should not be able to report this comment")

    def test_report_public_record_public_discussion_restricted_comment(self):
        """webcomment - report a comment restricted by 'viewrestrcomment'"""
        # Juliet should not be able to report the comment
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/report?comid=%s&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record_restr_comment, self.restr_comid_2))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, this user should not be able to report this comment")

    def test_vote_restricted_record_public_discussion_public_comment(self):
        """webcomment - vote for a comment restricted by 'viewrestrcoll'"""
        # Juliet should not be able to vote for the comment
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/vote?comid=%s&com_value=1&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record, self.restr_comid_1))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, this user should not be able to report this comment")

    def test_vote_public_record_restricted_discussion_public_comment(self):
        """webcomment - vote for a comment restricted by 'viewcomment'"""
        # Juliet should not be able to vote for the comment
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/vote?comid=%s&com_value=1&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restricted_discussion, self.restr_comid_5))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, this user should not be able to report this comment")

    def test_vote_public_record_public_discussion_restricted_comment(self):
        """webcomment - vote for a comment restricted by 'viewrestrcomment'"""
        # Juliet should not be able to vote for the comment
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/vote?comid=%s&com_value=1&ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.public_record_restr_comment, self.restr_comid_2))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, this user should not be able to report this comment")

    def test_comment_subscribe_restricted_record_public_discussion(self):
        """webcomment - subscribe to a discussion restricted with 'viewrestrcoll'"""
        # Juliet should not be able to subscribe to the discussion
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/subscribe?ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, this user should not be able to subscribe to this discussion")

        # Jekyll should be able to subscribe
        self.login('jekyll', 'j123ekyll')
        response = self.client.get("%s/%s/%i/comments/subscribe?ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restr_record))
        response = response.data
        if not "You have been subscribed" in response or \
               "Authorization failure" in response:
            self.fail("Oops, this user should be able to subscribe to this discussion")

    def test_comment_subscribe_public_record_restricted_discussion(self):
        """webcomment - subscribe to a discussion restricted with 'viewcomment'"""
        # Juliet should not be able to subscribe to the discussion
        self.login('juliet', 'j123uliet')
        response = self.client.get("%s/%s/%i/comments/subscribe?ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restricted_discussion))
        response = response.data
        if not "Authorization failure" in response:
            self.fail("Oops, this user should not be able to subscribe to this discussion")

        # Romeo should be able to subscribe
        self.login('romeo', 'r123omeo')
        response = self.client.get("%s/%s/%i/comments/subscribe?ln=en" % \
                (cfg['CFG_SITE_SECURE_URL'], cfg['CFG_SITE_RECORD'], self.restricted_discussion))
        response = response.data
        if not "You have been subscribed" in response or \
               "Authorization failure" in response:
            print response
            self.fail("Oops, this user should be able to subscribe to this discussion")

class WebCommentTransformationHTMLMarkupTest(InvenioTestCase):
    """ Test functions related to transforming HTML markup."""

    def test_unordered_lists_markup_transformation(self):
        """webcomment - unordered lists markup transformation """
        washer = EmailWasher()
        body_input = """<ul>
          <li>foo</li>
          <li>bar</li>
        </ul>"""
        body_expected = """
  * foo
  * bar
"""
        self.assertEqual(washer.wash(body_input),
                         body_expected)

        # Without spaces and EOL
        body_input = '<ul><li>foo</li><li>bar</li></ul>'
        self.assertEqual(washer.wash(body_input),
                         body_expected)

    def test_ordered_lists_markup_transformation(self):
        """ webcomment - ordered lists markup transformation """
        washer = EmailWasher()
        body_input = """<ol>
          <li>foo</li>
          <li>bar</li>
        </ol>"""
        body_expected = """
  1. foo
  2. bar
"""
        self.assertEqual(washer.wash(body_input),
                         body_expected)

        # Without spaces and EOL
        body_input = '<ol><li>foo</li><li>bar</li></ol>'
        self.assertEqual(washer.wash(body_input),
                         body_expected)

    def test_nested_lists_markup_transformation(self):
        """ webcomment - nested lists markup transformation """
        washer = EmailWasher()
        body_input =  """<ol>
          <li>foo
            <ol>
              <li>nested foo</li>
            </ol>
          </li>
          <li>bar</li>
        </ol>"""
        body_expected = """
  1. foo
    1. nested foo
  2. bar
"""
        self.assertEqual(washer.wash(body_input),
                         body_expected)

        # Without spaces and EOL
        body_input = '<ol><li>foo<ol><li>nested foo</li></ol></li><li>bar</li></ol>'
        self.assertEqual(washer.wash(body_input),
                         body_expected)

    def test_links_markup_transformation(self):
        """ webcomment - links markup transformation """

        washer = EmailWasher()
        body_input = 'text http://foo.com some more text'
        body_expected = 'text http://foo.com some more text'
        self.assertEqual(washer.wash(body_input),
                         body_expected)

        washer = EmailWasher()
        body_input = '<a href="https://cds.cern.ch/">CDS</a>'
        body_expected = '<https://cds.cern.ch/>(CDS)'
        self.assertEqual(washer.wash(body_input),
                         body_expected)

        washer = EmailWasher()
        body_input = '<a href="https://cds.cern.ch/">https://cds.cern.ch/</a>'
        body_expected = '<https://cds.cern.ch/>'
        self.assertEqual(washer.wash(body_input),
                         body_expected)

    def test_global_markup_transformation(self):
        """ webcomment - global transformation """
        washer = EmailWasher()
        body_input = """<a href="http://foo.com">http://foo.com</a>
        <ol>
          <li>Main Ordered List item</li>
          <li>Below is an example of HTML nested unordered list
            <ul>
              <li>nested list item 1</li>

                 <li>nested list item 2</li>
              <li>Sub nested ordered list
                <ol>
                  <li>sub nested list item A</li>
                  <li>sub nested list item B</li>
                </ol>
              </li>
            </ul>
          </li>
          <li>The last line in the main ordered list</li>
        </ol> <a href="http://foo.com">bar</a>"""
        body_expected = """<http://foo.com>
  1. Main Ordered List item
  2. Below is an example of HTML nested unordered list
    * nested list item 1
    * nested list item 2
    * Sub nested ordered list
      1. sub nested list item A
      2. sub nested list item B
  3. The last line in the main ordered list
 <http://foo.com>(bar)"""
        self.assertEqual(washer.wash(body_input),
                         body_expected)

        # Without spaces and EOL
        body_input = '<a href="http://foo.com">http://foo.com</a><ol><li>Main Ordered List item</li><li>Below is an example of HTML nested unordered list<ul><li>nested list item 1</li><li>nested list item 2</li><li>Sub nested ordered list<ol><li>sub nested list item A</li><li>sub nested list item B</li></ol></li></ul></li><li>The last line in the main ordered list</li></ol> <a href="http://foo.com">bar</a>'
        self.assertEqual(washer.wash(body_input),
                         body_expected)

TEST_SUITE = make_test_suite(WebCommentWebPagesAvailabilityTest,
                             WebCommentRestrictionsTest,
                             WebCommentTransformationHTMLMarkupTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
