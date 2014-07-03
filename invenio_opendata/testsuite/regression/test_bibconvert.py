# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2007, 2008, 2010, 2011, 2012, 2013 CERN.
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

"""BibConvert Regression Test Suite."""

__revision__ = "$Id$"

from invenio.base.globals import cfg
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, test_web_page_existence, \
                              InvenioTestCase


class BibConvertWebPagesAvailabilityTest(InvenioTestCase):
    """Check BibConvert web pages whether they are up or not."""

    def test_availability_bibconvert_admin_guide(self):
        """bibconvert - availability of BibConvert Admin Guide page"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/help/admin/bibconvert-admin-guide',
                                               expected_text="BibConvert Admin Guide"))
        return

    def test_availability_bibconvert_admin_guide_parts(self):
        """bibconvert - availability of BibConvert Admin Guide parts"""
        test_web_page_existence(cfg['CFG_SITE_URL'] + '/static/bibconvert-admin-guide/bibtex.cfg')
        test_web_page_existence(cfg['CFG_SITE_URL'] + '/static/bibconvert-admin-guide/dcq.cfg')
        test_web_page_existence(cfg['CFG_SITE_URL'] + '/static/bibconvert-admin-guide/dcq.dat')
        test_web_page_existence(cfg['CFG_SITE_URL'] + '/static/bibconvert-admin-guide/dcxml-to-marcxml.cfg')
        test_web_page_existence(cfg['CFG_SITE_URL'] + '/static/bibconvert-admin-guide/example_oaimarc2xm.xsl')
        test_web_page_existence(cfg['CFG_SITE_URL'] + '/static/bibconvert-admin-guide/example_oaimarc2xm_collID.kb')
        test_web_page_existence(cfg['CFG_SITE_URL'] + '/static/bibconvert-admin-guide/sample.cfg')
        test_web_page_existence(cfg['CFG_SITE_URL'] + '/static/bibconvert-admin-guide/sample.dat')
        test_web_page_existence(cfg['CFG_SITE_URL'] + '/static/bibconvert-admin-guide/sample.kb')

    def test_availability_bibconvert_hacking_pages(self):
        """bibconvert - availability of BibConvert Hacking Guide pages"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/help/hacking/bibconvert-internals',
                                               expected_text="BibConvert Internals"))
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/help/hacking/bibconvert-api',
                                               expected_text="BibConvert API"))
        return

TEST_SUITE = make_test_suite(BibConvertWebPagesAvailabilityTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
