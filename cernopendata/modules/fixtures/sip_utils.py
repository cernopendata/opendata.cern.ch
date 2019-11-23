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

"""SIP utils for CERN Open Data Portal."""

from __future__ import absolute_import, print_function

import glob
import json


from invenio_db import db
from invenio_sipstore.models import SIPMetadataType, \
    SIP as SIPModel, RecordSIP as RecordSIPModel
from invenio_sipstore.api import RecordSIP, SIP as SIPApi

from cernopendata.modules.sipstore.archivers.bagit_archiver import \
    CODBagItArchiver


def handle_sipstore_record_file_index(f):
    # [TOFIX] Fetch real file from EOS need to rebase
    # local fork of invenio-files-rest
    #
    json_str = f.storage(create_dir=False).open().read()
    json_index = json.loads(json_str)

    content = []

    for _file in json_index:
        content += handle_sipstore_record_file(_file)

    return content

def handle_sipstore_record_file(file, filename=None):
    return [handle_sipstore_record_file_json(file, filename),]
    # return handle_sipstore_record_file_txt(file, filename)


def handle_sipstore_record_file_txt(file, filename=None):
    _filename = filename or file.get("filename", None)
    content = "{} - {} - {} - {} - {}\n".format(
        file.get("uri", None),
        file.get("size", None),
        "data/{}".format(_filename),
        file.get("checksum", None),
        _filename
    )

    return content

def handle_sipstore_record_file_json(file, filename=None):
    _filename = filename or file.get("filename", None)
    return dict(
        uri=file.get("uri", None),
        size=file.get("size", None),
        checksum=file.get("checksum", None),
        filepath="data/{}".format(_filename),
        filename=_filename,
        # _fetch=True
    )


def sip_record(recid, record, files_content, inserted_or_updated):
    sip_patch_of = None

    if inserted_or_updated == "updated":
        sip_recid = recid

        sip_patch_of = (
            db.session.query(SIPModel)
            .join(RecordSIPModel, RecordSIPModel.sip_id == SIPModel.id)
            .filter(RecordSIPModel.pid_id == sip_recid.id)
            .order_by(SIPModel.created.desc())
            .first()
        )

    recordsip = RecordSIP.create(
        recid,
        record, archivable=True,
        create_sip_files=True,
        # sip_metadata_type='record-json',
        user_id=None,
        agent={}
        # agent=sip_agent
    )

    archiver = CODBagItArchiver(
        recordsip.sip, include_all_previous=False,
        patch_of=sip_patch_of, files_content=files_content
    )

    archiver.save_bagit_metadata()

    sip = (
         RecordSIPModel.query
         .filter_by(pid_id=recid.id)
         .order_by(RecordSIPModel.created.desc())
         .first().sip
    )

    # archive_sip.delay(str(sip.id))
    archive_sip(str(sip.id))


# @shared_task(ignore_result=True, max_retries=6,
#              default_retry_delay=4 * 60 * 60)
def archive_sip(sip_uuid):
    """Send the SIP for archiving.
    Retries every 4 hours, six times, which should work for up to 24 hours
    archiving system downtime.
    :param sip_uuid: UUID of the SIP for archiving.
    :type sip_uuid: str
    """
    try:
        sip = SIPApi(SIPModel.query.get(sip_uuid))
        archiver = CODBagItArchiver(sip)
        bagmeta = archiver.get_bagit_metadata(sip)
        if bagmeta is None:
            raise ArchivingError(
                'Bagit metadata does not exist for SIP: {0}.'.format(sip.id))
        if sip.archived:
            raise ArchivingError(
                'SIP was already archived {0}.'.format(sip.id))
        archiver.write_all_files()
        sip.archived = True
        db.session.commit()
    except Exception as exc:
        # On ArchivingError (see above), do not retry, but re-raise
        raise
        if not isinstance(exc, ArchivingError):
            archive_sip.retry(exc=exc)
        raise
