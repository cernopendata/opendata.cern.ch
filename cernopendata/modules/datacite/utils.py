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
"""Utilities for datacite module."""

import random
import string

from invenio_pidstore.errors import PIDDoesNotExistError
from invenio_pidstore.models import PersistentIdentifier


def generate_doi(prefix, experiment=None):
    """Generate random DOI, unique within PIDStore."""
    while True:
        doi = random_doi(prefix, experiment)
        try:
            PersistentIdentifier.get("doi", doi)
        except PIDDoesNotExistError:
            return doi


def random_doi(prefix, experiment=None):
    """Generate random DOI."""

    def _generate_random_string(length):
        chars = string.ascii_uppercase + string.digits
        return "".join((random.choice(chars)) for x in range(length))

    if experiment:
        base = "{}/OPENDATA.{}".format(prefix, experiment)
    else:
        base = "{}/OPENDATA".format(prefix)

    return "{}.{}.{}".format(
        base, _generate_random_string(4), _generate_random_string(4)
    ).upper()
