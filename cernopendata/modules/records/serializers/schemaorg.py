# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2018 CERN.
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
"""CERN Opendata schema.org JSON-LD serializer."""

import json

from invenio_records_rest.serializers.json import JSONSerializer

from cernopendata.modules.records.serializers.schemas import (
    schemaorg_schemas as schemas,
)


class BasicJSONSerializer(JSONSerializer):
    """Basic JSON serializer."""

    def serialize(self, pid, record, links_factory=None, **kwargs):
        """Serialize a single record and persistent identifier.

        :param pid: Persistent identifier instance.
        :param record: Record instance.
        :param links_factory: Factory function for record links.
        """
        return json.dumps(
            self.transform_record(pid, record, links_factory, **kwargs),
            indent=2,
            separators=(", ", ": "),
        )


class CODSchemaorgSerializer(BasicJSONSerializer):
    """CERN Open Data schema.org serializer.

    Serializes a Record based on its type (Dataset, Software, etc.) to
    schema.org compatible JSON-LD syntax.
    """

    SCHEMAS = {
        "Dataset": schemas.DatasetSchemaorgSchema,
        "Software": schemas.SoftwareSchemaorgSchema,
        "Environment": schemas.RecordSchemaorgSchema,
        "Supplementaries": schemas.RecordSchemaorgSchema,
        "Documentation": schemas.DocumentationSchemaorgSchema,
    }
    """Marsmallow Schemas for each Record type in CERN Open Data."""

    def dump(self, obj, context=None):
        """Serialize object with schema."""
        schema_cls = None

        obj = obj.get("metadata", obj)
        type = obj["type"]["primary"]

        schema_cls = self.SCHEMAS[type]
        return schema_cls(context=context).dump(obj)
