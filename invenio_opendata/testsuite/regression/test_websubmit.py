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

"""WebSubmit Regression Test Suite."""

__revision__ = "$Id$"

import os
from logging import StreamHandler, DEBUG
from cStringIO import StringIO

#from invenio.ext.logging import register_exception
#from invenio.config import CFG_SITE_URL, CFG_PREFIX, CFG_TMPDIR, CFG_PATH_PDFTK
from invenio.base.globals import cfg
from invenio.base.wrappers import lazy_import
from invenio.testsuite import make_test_suite, run_test_suite, \
                              test_web_page_content, merge_error_messages, \
                              InvenioTestCase
from invenio.base.factory import with_app_context

register_exception = lazy_import('invenio.ext.logging:register_exception')
websubmit_file_stamper = lazy_import('invenio.legacy.websubmit.file_stamper')

class WebSubmitWebPagesAvailabilityTest(InvenioTestCase):
    """Check WebSubmit web pages whether they are up or not."""

    def test_submission_pages_availability(self):
        """websubmit - availability of submission pages"""

        baseurl = cfg['CFG_SITE_URL'] + '/submit/'

        _exports = ['', 'direct']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_publiline_pages_availability(self):
        """websubmit - availability of approval pages"""

        baseurl = cfg['CFG_SITE_URL']

        _exports = ['/approve.py', '/publiline.py',
                    '/yourapprovals.py']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_your_submissions_pages_availability(self):
        """websubmit - availability of Your Submissions pages"""

        baseurl = cfg['CFG_SITE_URL']

        _exports = ['/yoursubmissions.py']

        error_messages = []
        for url in [baseurl + page for page in _exports]:
            error_messages.extend(test_web_page_content(url))
        if error_messages:
            self.fail(merge_error_messages(error_messages))
        return

    def test_help_page_availability(self):
        """websubmit - availability of WebSubmit help page"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/help/submit-guide',
                                               expected_text="Submit Guide"))

class WebSubmitLegacyURLsTest(InvenioTestCase):
    """ Check that the application still responds to legacy URLs"""

    def test_legacy_help_page_link(self):
        """websubmit - legacy Submit Guide page link"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/help/submit',
                                               expected_text="Submit Guide"))
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/help/submit/',
                                               expected_text="Submit Guide"))
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/help/submit/index.en.html',
                                              expected_text="Submit Guide"))
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/help/submit/access.en.html',
                                              expected_text="Submit Guide"))

class WebSubmitXSSVulnerabilityTest(InvenioTestCase):
    """Test possible XSS vulnerabilities of the submission engine."""

    def test_xss_in_submission_doctype(self):
        """websubmit - no XSS vulnerability in doctype parameter"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/submit?doctype=%3CSCRIPT%3Ealert%28%22XSS%22%29%3B%3C%2FSCRIPT%3E',
                                               expected_text='Unable to find document type: &lt;SCRIPT&gt;alert("XSS")', username="jekyll",
                          password="j123ekyll"))

    def test_xss_in_submission_act(self):
        """websubmit - no XSS vulnerability in act parameter"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] + '/submit?doctype=DEMOTHE&access=1_1&act=%3CSCRIPT%3Ealert%28%22XSS%22%29%3B%3C%2FSCRIPT%3E',
                                               expected_text='Invalid doctype and act parameters', username="jekyll",
                          password="j123ekyll"))

    def test_xss_in_submission_page(self):
        """websubmit - no XSS vulnerability in access parameter"""
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] +
                          '/submit?doctype=DEMOTHE&access=/../../../etc/passwd&act=SBI&startPg=1&ln=en&ln=en',                                               expected_text='Invalid parameters', username="jekyll",
                          password="j123ekyll"))
        self.assertEqual([],
                         test_web_page_content(cfg['CFG_SITE_URL'] +
                          '/submit?doctype=DEMOTHE&access=%3CSCRIPT%3Ealert%28%22XSS%22%29%3B%3C%2FSCRIPT%3E&act=SBI',                                               expected_text='Invalid parameters', username="jekyll",
                          password="j123ekyll"))


@with_app_context()
def WebSubmitFileConverterTestGenerator():
    from invenio.legacy.websubmit.file_converter import get_conversion_map, can_convert
    #FIXME
    if can_convert('.odt', '.txt'):
        ## Special test for unoconv/LibreOffice
        yield WebSubmitFileConverterTest(os.path.join(cfg['CFG_PREFIX'], 'lib', 'webtest', 'invenio', 'test.odt'), '.odt', '.txt')
    if can_convert('.doc', '.txt'):
        ## Special test for unoconv/LibreOffice
        yield WebSubmitFileConverterTest(os.path.join(cfg['CFG_PREFIX'], 'lib', 'webtest', 'invenio', 'test.doc'), '.doc', '.txt')
    for from_format in get_conversion_map().keys():
        input_file = os.path.join(cfg['CFG_PREFIX'], 'lib', 'webtest', 'invenio', 'test%s' % from_format)
        if not os.path.exists(input_file):
            ## Can't run such a test because there is no test example
            continue
        for to_format in get_conversion_map().keys():
            if from_format == to_format:
                continue
            conversion_map = can_convert(from_format, to_format)
            if conversion_map:
                if [converter for converter in conversion_map if converter[0].__name__ == 'unoconv']:
                    ## We don't want to test unoconv which is tested separately
                    continue
                yield WebSubmitFileConverterTest(input_file, from_format, to_format)

class WebSubmitFileConverterTest(InvenioTestCase):
    """Test WebSubmit file converter tool"""

    def __init__(self, input_file, from_format, to_format):
        super(WebSubmitFileConverterTest, self).__init__('_run_test')
        self.from_format = from_format
        self.to_format = to_format
        self.input_file = input_file

    def setUp(self):
        from invenio.legacy.websubmit.file_converter import get_file_converter_logger
        logger = get_file_converter_logger()
        self.log = StringIO()
        logger.setLevel(DEBUG)
        for handler in logger.handlers:
            logger.removeHandler(handler)
        handler = StreamHandler(self.log)
        handler.setLevel(DEBUG)
        logger.addHandler(handler)


    def shortDescription(self):
        return """websubmit - test %s to %s conversion""" % (self.from_format, self.to_format)

    def _run_test(self):
        from invenio.legacy.websubmit.file_converter import InvenioWebSubmitFileConverterError, convert_file
        try:
            tmpdir_snapshot1 = set(os.listdir(cfg['CFG_TMPDIR']))
            output_file = convert_file(self.input_file, output_format=self.to_format)
            tmpdir_snapshot2 = set(os.listdir(cfg['CFG_TMPDIR']))
            tmpdir_snapshot2.discard(os.path.basename(output_file))
            if not os.path.exists(output_file):
                raise InvenioWebSubmitFileConverterError("output_file %s was not correctly created" % output_file)
            if tmpdir_snapshot2 - tmpdir_snapshot1:
                raise InvenioWebSubmitFileConverterError("Some temporary files were left over: %s" % (tmpdir_snapshot2 - tmpdir_snapshot1))
        except Exception, err:
            register_exception(alert_admin=True)
            self.fail("ERROR: when converting from %s to %s: %s, the log contained: %s" % (self.from_format, self.to_format, err, self.log.getvalue()))

if False: #FIXME cfg['CFG_PATH_PDFTK']:
    class WebSubmitStampingTest(InvenioTestCase):
        """Test WebSubmit file stamping tool"""

        def test_stamp_coverpage(self):
            """websubmit - creation of a PDF cover page stamp (APIs)"""
            file_stamper_options = { 'latex-template'      : "demo-stamp-left.tex",
                                    'latex-template-var'  : {'REPORTNUMBER':'TEST-2010','DATE':'10/10/2000'},
                                    'input-file'          : cfg['CFG_PREFIX'] + "/lib/webtest/invenio/test.pdf",
                                    'output-file'         : "test-stamp-coverpage.pdf",
                                    'stamp'               : "coverpage",
                                    'layer'               : "foreground",
                                    'verbosity'           : 0,
                                    }
            try:
                (stamped_file_path_only, stamped_file_name) = \
                        websubmit_file_stamper.stamp_file(file_stamper_options)
            except:
                self.fail("Stamping failed")

            # Test that file is now bigger...
            assert os.path.getsize(os.path.join(stamped_file_path_only,
                                                stamped_file_name)) > 12695

        def test_stamp_firstpage(self):
            """websubmit - stamping first page of a PDF (APIs)"""
            file_stamper_options = { 'latex-template'      : "demo-stamp-left.tex",
                                    'latex-template-var'  : {'REPORTNUMBER':'TEST-2010','DATE':'10/10/2000'},
                                    'input-file'          : cfg['CFG_PREFIX'] + "/lib/webtest/invenio/test.pdf",
                                    'output-file'         : "test-stamp-firstpage.pdf",
                                    'stamp'               : "first",
                                    'layer'               : "background",
                                    'verbosity'           : 0,
                                    }
            try:
                (stamped_file_path_only, stamped_file_name) = \
                        websubmit_file_stamper.stamp_file(file_stamper_options)
            except:
                self.fail("Stamping failed")

            # Test that file is now bigger...
            assert os.path.getsize(os.path.join(stamped_file_path_only,
                                                stamped_file_name)) > 12695

        def test_stamp_allpages(self):
            """websubmit - stamping all pages of a PDF (APIs)"""
            file_stamper_options = { 'latex-template'      : "demo-stamp-left.tex",
                                    'latex-template-var'  : {'REPORTNUMBER':'TEST-2010','DATE':'10/10/2000'},
                                    'input-file'          : cfg['CFG_PREFIX'] + "/lib/webtest/invenio/test.pdf",
                                    'output-file'         : "test-stamp-allpages.pdf",
                                    'stamp'               : "all",
                                    'layer'               : "foreground",
                                    'verbosity'           : 0,
                                    }
            try:
                (stamped_file_path_only, stamped_file_name) = \
                        websubmit_file_stamper.stamp_file(file_stamper_options)
            except:
                self.fail("Stamping failed")

            # Test that file is now bigger...
            assert os.path.getsize(os.path.join(stamped_file_path_only,
                                                stamped_file_name)) > 12695
else:
    ## pdftk is not available. Disabling stamping-related
    ## regression tests.
    class WebSubmitStampingTest(InvenioTestCase):
        pass

TEST_SUITE = make_test_suite(WebSubmitWebPagesAvailabilityTest,
                             WebSubmitLegacyURLsTest,
                             WebSubmitXSSVulnerabilityTest,
                             WebSubmitStampingTest)

for test in WebSubmitFileConverterTestGenerator():
    TEST_SUITE.addTest(test)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
