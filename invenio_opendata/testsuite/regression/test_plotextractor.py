# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2010, 2011, 2013 CERN.
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

"""Regression tests for the plotextract script."""

__revision__ = "$Id$"

import os

from invenio.base.globals import cfg
from invenio.testsuite import make_test_suite, run_test_suite, InvenioTestCase


class GetDefaultsTest(InvenioTestCase):
    """Test function to get default values."""
    def setUp(self):
        self.arXiv_id = "arXiv:astro-ph_0104076"
        self.tarball = "%s/2001/04/arXiv:astro-ph_0104076/arXiv:astro-ph_0104076" % (cfg['CFG_TMPDIR'],)

    def test_get_defaults(self):
        """plotextractor - get defaults"""
        from invenio.utils.shell import run_shell_command
        from invenio.utils.plotextractor.cli import get_defaults
        sdir_should_be = os.path.join(cfg['CFG_TMPDIR'], self.arXiv_id + '_plots')
        refno_should_be = "15" # Note: For ATLANTIS DEMO site
        sdir, refno = get_defaults(tarball=self.tarball, sdir=None, refno_url=cfg['CFG_SITE_URL'])
        if sdir != None:
            run_shell_command("rm -rf %s" % (sdir,))
        self.assertTrue(sdir == sdir_should_be, \
                         "didn\'t get correct default scratch dir")
        self.assertTrue(refno == refno_should_be, \
                         'didn\'t get correct default reference number')

TEST_SUITE = make_test_suite(GetDefaultsTest)

if __name__ == "__main__":
    run_test_suite(TEST_SUITE, warn_user=True)
