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
"""CERN Opendata schema.org marshmallow schema."""

from __future__ import absolute_import, print_function

from marshmallow import Schema, fields

from marshmallow.decorators import post_dump

SITE_URL = "http://opendata.cern.ch"


class RecordSchemaorgSchema(Schema):
    """schema.org JSON-LD schema for CERN Opendata Record."""

    # JSON-LD minimum requirements
    context_ = fields.Field(default='https://schema.org/', dump_to='@context')
    id_ = fields.Method('get_identifier', dump_to='@id')

    # Minimum functional
    type_ = fields.Method('get_type', dump_to='@type')
    name = fields.Str(attribute='title', dump_to='name')
    description = fields.Method('get_description', dump_to='description')
    identifier = fields.Method('get_identifier', dump_to='identifier')
    url = fields.Method('get_url', dump_to='url')
    creator = fields.Method('get_creator', dump_to='creator')
    date_created = fields.Method('get_date_created', dump_to='dateCreated')
    date_published = fields.Str(attribute='date_published',
                                dump_to='datePublished')
    publisher = fields.Method('get_publisher', dump_to='publisher')

    # Minimum operational
    # license = fields.Str('license', dump_to='license')
    # data_standard = fields.Str('dataStandard', dump_to='dataStandard')
    # date_modified = fields.Str('dateModified', dump_to='dateModified')
    # structure = fields.Str('structure', dump_to='structure')
    # access_url = fields.Str('accessUrl', dump_to='accessUrl')
    # access_interface = fields.str('accessInterface',
    #                              dump_to='accessInterface')

    def get_creator(self, obj):
        """Get creator(s) based on authors or collaboration field."""
        authors = obj.get('authors', None)

        if authors:
            return [{"@type": "Person", 'name': x['name']} for x in authors]
        else:
            # Note: Can there be many Organizations in a Record?
            #       Now only one is expected.
            collaboration = obj.get('collaboration', {}).get('name', None)
            if collaboration:
                return {"@type": "Organization", 'name': collaboration}
            return None

    def get_description(self, obj):
        """Get description based on abstract.description field."""
        return obj.get('abstract', {}).get('description', None)

    def get_identifier(self, obj):
        """Get identifier based on doi or recid field."""
        doi = obj.get('doi', None)

        if doi:
            return "https://doi.org/{}".format(doi)
        else:
            recid = obj.get('recid', None)
            return "{}/record/{}".format(SITE_URL, recid)

    def get_date_created(self, obj):
        """Get most recent date_created year."""
        return max(obj.get('date_created', ['0', ]))

    def get_publisher(self, obj):
        """Get publisher based on publisher field."""
        # Organization or Person - The publisher of the creative work.
        publisher = obj.get('publisher', None)
        if publisher:
            return {"@type": "Organization", 'name': publisher}
        return None

    def get_type(self, obj):
        """Get resource type based on Record type."""
        return "CreativeWork"

    def get_url(self, obj):
        """Get url based on recid field."""
        recid = obj.get('recid', None)
        return "{}/record/{}".format(SITE_URL, recid)


class DatasetSchemaorgSchema(RecordSchemaorgSchema):
    """schema.org JSON-LD schema for CERN Opendata Dataset Record."""

    def get_type(self, obj):
        """Get resource type based on Record type."""
        return "Dataset"


class DocumentationSchemaorgSchema(RecordSchemaorgSchema):
    """schema.org JSON-LD schema for CERN Opendata Documentation Record."""

    REMOVE_IF_EMPTY = ['creator', 'description']
    """Keys that should be removed in case they don't have a value."""

    @post_dump
    def remove_empty_keys(self, data):
        """Remove 'null' valued keys from serialized Document Record.

        Since Document Record (usually?) doesn't contain necessary information
        to populate 'creator' and 'description' field they are removed.
        """
        for k in self.REMOVE_IF_EMPTY:
            if k in data and not data[k]:
                del data[k]
        return data

    def get_publisher(self, obj):
        """Return 'CERN Open Data Portal' as publisher for Document Records."""
        return {"@type": "Organization", 'name': 'CERN Open Data Portal'}

    def get_url(self, obj):
        """Get url based on slug field."""
        slug = obj.get('slug', None)
        return "{}/docs/{}".format(SITE_URL, slug)


class SoftwareSchemaorgSchema(RecordSchemaorgSchema):
    """schema.org JSON-LD schema for CERN Opendata Software Record."""

    def get_type(self, obj):
        """Get resource type based on Record type."""
        return "SoftwareSourceCode"
