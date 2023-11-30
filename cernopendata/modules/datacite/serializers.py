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
"""Serializers for datacite module."""

from marshmallow import Schema, fields


class DataCiteSerializer(Schema):
    """DataCite complient schema."""

    identifier = fields.Method("get_identifier")
    creators = fields.Method("get_creators")
    titles = fields.Method("get_titles")
    resourceType = fields.Method("get_resourcetype")
    publisher = fields.Str()
    publicationYear = fields.Str(attribute="date_published")

    def get_identifier(self, obj):
        """Get identifier based on doi field."""
        return {"identifier": obj["doi"], "identifierType": "DOI"}

    def get_creators(self, obj):
        """Get creators based on authors or collaboration field."""
        authors = obj.get("authors", [obj.get("collaboration", None)])
        creators = [
            {
                "creatorName": author["name"],
                "nameIdentifiers": [
                    {
                        "nameIdentifier": author["orcid"],
                        "nameIdentifierScheme": "ORCID",
                        "schemeURI": "http://orcid.org/",
                    }
                ]
                if "orcid" in author
                else [],
            }
            for author in authors
        ]
        return creators

    def get_titles(self, obj):
        """Get title."""
        return [{"title": obj["title"]}]

    def get_resourcetype(self, obj):
        """Get resource type based on type field."""
        resource_type = "Other"
        if obj["type"]:
            type_primary = obj["type"].get("primary", "")
            if type_primary in ["Software", "Dataset"]:
                resource_type = type_primary
        return {"resourceTypeGeneral": resource_type}
