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

"""DataCite client."""

from datacite.client import DataCiteMDSClient
from datacite.errors import DataCiteError
from flask import current_app


class DataCiteMDSClientWrapper(DataCiteMDSClient):
    """DataCite client."""

    def __init__(self):
        """Initialize client using given config variables.

        * `PIDSTORE_DATACITE_USERNAME` as username.
        * `PIDSTORE_DATACITE_PASSWORD` as password.
        * `PIDSTORE_DATACITE_DOI_PREFIX` as DOI prefix.
        * `PIDSTORE_DATACITE_TESTMODE` to `True` if it configured in test mode.
        * `PIDSTORE_DATACITE_URL` as DataCite URL.
        """
        super(DataCiteMDSClientWrapper, self).__init__(
            username=current_app.config.get("PIDSTORE_DATACITE_USERNAME"),
            password=current_app.config.get("PIDSTORE_DATACITE_PASSWORD"),
            prefix=current_app.config.get("PIDSTORE_DATACITE_DOI_PREFIX"),
            test_mode=current_app.config.get("PIDSTORE_DATACITE_TESTMODE", False),
            url=current_app.config.get("PIDSTORE_DATACITE_URL"),
        )

    def doi_get_all(self):
        """Get list of all registered DOIs."""
        r = self._request_factory()
        r.get("doi")

        if r.code == 200:
            return r.data
        else:
            raise DataCiteError.factory(r.code, r.data)
