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

"""Basic JSON serializer for records."""

from flask import current_app
from marshmallow import Schema, fields

from invenio_records_rest.serializers.json import JSONSerializer


class BasicJSONSerializer(JSONSerializer):
    """Basic JSON serializer."""

    pass


def dump_files(obj):
    """Basic JSON serializer."""
    _files = []
    _index_files = []

    recid = obj.get('pid').pid_value
    files = obj.get('metadata', {}).get('files', [])

    for file in files:
        _file = {
            "checksum": file.get('checksum', ''),
            "size": file.get('size', ''),
            "filename": file.get('key', ''),
            "uri_http": "{}/record/{}/files/{}".format(
                current_app.config.get('HOST_URI', 'http://opendata.cern.ch'),
                recid,
                file.get('key', '')),
            "uri_root": file.get('uri', '')
        }

        if 'index' in file.get('type', ''):
            _index_files.append(_file)
        else:
            _files.append(_file)

    return _files, _index_files


class RecordSchemaV1(Schema):
    """Common record schema."""

    id = fields.Integer(attribute='pid.pid_value', dump_only=True)
    created = fields.Str(dump_only=True)
    updated = fields.Str(dump_only=True)
    metadata = fields.Method('dump_metadata')

    def dump_metadata(self, obj):
        """Dumps metadata - removes '_files'."""
        del obj['metadata']["_files"]

        _files = dump_files(obj)
        obj['metadata']['files'] = _files[0]
        obj['metadata']['index_files'] = _files[1]

        return obj['metadata']
