# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017, 2022 CERN.
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

"""Cernopendata JSON serializer for records."""

from flask import current_app, json
from invenio_records_rest.serializers.json import JSONSerializer
from marshmallow import Schema, fields


class BasicJSONSerializer(JSONSerializer):
    """Basic JSON serializer."""

    # We need to override `dump()` as invenio-records-rest attempts to
    # return `.data` which it doesn't exist in Marshmallow v3.
    # (https://github.com/inveniosoftware/invenio-records-rest/blob/c4a3717afcf9b08b6e42f3529addecc64bb2e47c/invenio_records_rest/serializers/marshmallow.py#L28)
    def dump(self, obj, context=None):
        """Serialize object with schema."""
        return self.schema_class(context=context).dump(obj)


class CODJSONSerializer(JSONSerializer):
    """UI search serializer."""

    # We need to override `serialize_search()` as we have a custom
    # `filtered` field in aggregation in `cernopendata_facets_factory` and
    # react-search-kit expect the buckets inside the aggregations directly
    # not inside filtered object.
    def serialize_search(
        self, pid_fetcher, search_result, links=None, item_links_factory=None, **kwargs
    ):
        """Serialize a search result.

        :param pid_fetcher: Persistent identifier fetcher.
        :param search_result: Elasticsearch search result.
        :param links: Dictionary of links to add to response.
        """
        total = search_result["hits"]["total"]["value"]

        # Serialize aggregation and remove `filtered` object
        aggregations = (search_result.get("aggregations", dict()),)
        for k, agg in aggregations[0].items():
            if "filtered" in agg:
                buckets = agg.get("filtered")
                if buckets:
                    agg.update(buckets)
                    agg.pop("filtered")

        aggregations = aggregations[0]

        # Remove empty buckets in number_of_events facet
        if "number_of_events" in aggregations.keys():
            new_event_list = []
            for bucket in aggregations["number_of_events"]["buckets"]:
                if bucket["doc_count"] != 0:
                    new_event_list.append(bucket)
            aggregations["number_of_events"]["buckets"] = new_event_list

        return json.dumps(
            dict(
                hits=dict(
                    hits=[
                        self.transform_search_hit(
                            pid_fetcher(hit["_id"], hit["_source"]),
                            hit,
                            links_factory=item_links_factory,
                            **kwargs
                        )
                        for hit in search_result["hits"]["hits"]
                    ],
                    total=total,
                ),
                links=links or {},
                aggregations=aggregations,
            ),
            **self._format_args()
        )


def dump_files(obj):
    """Basic JSON serializer."""
    _files = []
    _index_files = []

    recid = obj.get("pid").pid_value
    files = obj.get("metadata", {}).get("files", [])

    for file in files:
        _file = {
            "checksum": file.get("checksum", ""),
            "size": file.get("size", ""),
            "filename": file.get("key", ""),
            "uri_http": "{}/record/{}/files/{}".format(
                current_app.config.get("HOST_URI", "http://opendata.cern.ch"),
                recid,
                file.get("key", ""),
            ),
            "uri_root": file.get("uri", ""),
        }

        if "index" in file.get("type", ""):
            _index_files.append(_file)
        else:
            _files.append(_file)

    return _files, _index_files


class RecordSchemaV1(Schema):
    """Common record schema."""

    id = fields.Integer(attribute="pid.pid_value", dump_only=True)
    created = fields.Str(dump_only=True)
    updated = fields.Str(dump_only=True)
    metadata = fields.Method("dump_metadata")

    def dump_metadata(self, obj):
        """Dumps metadata and removes `_files`."""
        if "_files" in obj["metadata"]:
            del obj["metadata"]["_files"]

        if "_bucket" in obj["metadata"]:
            del obj["metadata"]["_bucket"]

        _files = dump_files(obj)
        obj["metadata"]["files"] = _files[0]
        obj["metadata"]["index_files"] = _files[1]

        return obj["metadata"]
