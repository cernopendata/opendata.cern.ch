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

"""Record serialization."""

from invenio_records_rest.schemas import RecordSchemaJSONV1
from invenio_records_rest.serializers.response import (
    record_responsify,
    search_responsify,
)

from .basic_json import BasicJSONSerializer, CODJSONSerializer, RecordSchemaV1
from .schemaorg import CODSchemaorgSerializer

json = BasicJSONSerializer(RecordSchemaV1)

schemaorg_jsonld = CODSchemaorgSerializer(replace_refs=True)

schemaorg_jsonld_response = record_responsify(schemaorg_jsonld, "application/ld+json")

json_search = CODJSONSerializer(RecordSchemaJSONV1)

json_v1_search = search_responsify(json_search, "application/json")
