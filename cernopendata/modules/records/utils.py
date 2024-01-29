# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017, 2018 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Implementention of various utility functions."""

import json

import six
from flask import abort, current_app, jsonify, render_template, request
from invenio_files_rest.views import ObjectResource
from invenio_records.api import Record
from invenio_records_files.utils import record_file_factory

# from invenio_files_rest.models import FileInstance, ObjectVersion
# from invenio_records.errors import MissingModelError
from invenio_records_ui.utils import obj_or_import_string
from invenio_xrootd import EOSFileStorage
from werkzeug.utils import import_string


def file_download_ui(pid, record, _record_file_factory=None, **kwargs):
    """File download view for a given record.

    Plug this method into your ``RECORDS_UI_ENDPOINTS`` configuration:

    .. code-block:: python

        RECORDS_UI_ENDPOINTS = dict(
            recid=dict(
                # ...
                route='/record/<pid_value/files/<filename>',
                view_imp='invenio_records_files.utils:file_download_ui',
                record_class='invenio_records_files.api:Record',
            )
        )

    :param pid: The :class:`invenio_pidstore.models.PersistentIdentifier`
        instance.
    :param record: The record metadata.
    """
    _record_file_factory = _record_file_factory or record_file_factory
    # Extract file from record.
    filename = kwargs.get("filename")

    if filename == "configFile.py":
        rf = record.files.dumps()
        for file in rf:
            if file.get("key", "").endswith("configFile.py"):
                filename = file.get("key")
                break

    fileobj = _record_file_factory(pid, record, filename)

    if not fileobj:
        abort(404)

    obj = fileobj.obj

    # Check permissions
    ObjectResource.check_object_permission(obj)

    # Send file.
    return ObjectResource.send_object(
        obj.bucket,
        obj,
        # expected_chksum=fileobj.get('checksum'),
        logger_data={
            "bucket_id": obj.bucket_id,
            "pid_type": pid.pid_type,
            "pid_value": pid.pid_value,
        },
        # create_dir=False
    )


def eos_file_download_ui(pid, record, _record_file_factory=None, **kwargs):
    """File download view for a given EOS uri."""
    if current_app.config.get("CERNOPENDATA_DISABLE_DOWNLOADS", False):
        abort(503)

    path = kwargs.get("filepath", "")

    return eos_send_file_or_404(path)


def eos_send_file_or_404(file_path=""):
    """File download for a given EOS uri."""
    storage = EOSFileStorage(
        "root://eospublic.cern.ch//eos/opendata/" + file_path,
        # create_dir=False
    )

    filename = file_path.split("/")[-1:]

    try:
        return storage.send_file(filename[0])
    except Exception:
        abort(404)


def get_paged_files(files, page, items_per_page=5):
    """Get files for current page."""
    start = (page - 1) * items_per_page
    end = (page) * items_per_page

    return files[start:end]


def record_file_page(pid, record, page=1, **kwargs):
    """Record view - get files for current page."""
    rf = record.get("files", [])

    items_per_page = request.args.get("perPage", 5)
    try:
        items_per_page = int(items_per_page)
    except Exception:
        items_per_page = 5

    if request.args.get("group"):
        # grouped = groupby(rf, lambda x: x.get('type'))
        index_files = [d for d in rf if (d.get("type", "") in ["index", "index.txt"])]
        _files = [
            d
            for d in rf
            if (d.get("type", "") not in ["index", "index.txt", "index.json"])
        ]
        grouped_files = {
            "index_files": {
                "total": len(index_files),
                "files": index_files[:items_per_page],
            },
            "files": {"total": len(_files), "files": _files[:items_per_page]},
        }

        return jsonify(grouped_files)

    file_type_filter = request.args.get("type")

    if file_type_filter == "index_files":
        filtered_files = [
            d for d in rf if (d.get("type", "") in ["index", "index.txt"])
        ]
        rf_len = len(filtered_files)
        paged_files = get_paged_files(filtered_files, page, items_per_page)
        return jsonify({"total": rf_len, "files": paged_files})
    else:
        filtered_files = [
            d
            for d in rf
            if (d.get("type", "") not in ["index", "index.txt", "index.json"])
        ]
        rf_len = len(filtered_files)
        paged_files = get_paged_files(filtered_files, page, items_per_page)
        return jsonify({"total": rf_len, "files": paged_files})

    rf_len = len(rf)
    paged_files = get_paged_files(rf, page, items_per_page)

    return jsonify({"total": rf_len, "files": paged_files})


def record_metadata_view(pid, record, template=None):
    """Record detail view."""
    collection = ""
    if len(record.get("collections", [])) > 0:
        collection = record.get("collections", [])[0]
    return render_template(
        [
            "cernopendata_records_ui/records/record_detail_{}.html".format(collection),
            "cernopendata_records_ui/records/record_detail.html",
        ],
        pid=pid,
        record=record,
        title=record.get("title", "Untitled record") + " | CERN Open Data Portal",
    )


def term_metadata_view(pid, record, template=None):
    """Term detail view."""
    return render_template(
        ["cernopendata_records_ui/terms/detail.html"],
        pid=pid,
        record=record,
        title=record.get("anchor", "Glossary term") + " | CERN Open Data Portal",
    )


def doc_metadata_view(pid, record, template=None):
    """Doc detail view."""
    return render_template(
        ["cernopendata_records_ui/docs/detail.html"],
        pid=pid,
        record=record,
        title=record.get("title", "Untitled document") + " | CERN Open Data Portal",
    )


def serialize_record(record, pid, serializer, module=None, throws=True, **kwargs):
    """Serialize record according to the passed serializer."""
    if isinstance(record, Record):
        try:
            module = module or "cernopendata.modules.records.serializers"
            serializer = import_string(".".join((module, serializer)))
            return serializer.serialize(pid, record, **kwargs)
        except Exception:
            current_app.logger.exception(
                "Record serialization failed {}.".format(str(record.id))
            )
            if throws:
                raise


def export_json_view(pid, record, template=None, **kwargs):
    r"""Record JSON export view.

    Serializes record with given format and renders record export template.
    :param pid: PID object.
    :param record: Record object.
    :param template: Template to render.
    :param \*\*kwargs: Additional view arguments based on URL rule.
    :return: The rendered template.
    """
    formats = current_app.config.get("RECORDS_UI_EXPORT_FORMATS", {}).get(pid.pid_type)
    fmt = formats.get(request.view_args.get("format"))

    if fmt is False:
        # If value is set to False, it means it was deprecated.
        abort(410)
    elif fmt is None:
        abort(404)
    else:
        try:
            serializer = obj_or_import_string(fmt["serializer"])
            data = serializer.serialize(pid, record)
            data = json.loads(data)
        except Exception:
            data = {}

        return jsonify(data)
