# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""API for manipulating files associated to a record."""

from collections import OrderedDict
from functools import wraps

from invenio_db import db
from invenio_files_rest.errors import InvalidOperationError
from invenio_files_rest.models import ObjectVersion, FileInstance
from invenio_records.api import Record as _Record
from invenio_records.errors import MissingModelError
from invenio_records_files.api import FileObject, FilesIterator, _writable, FilesMixin

from invenio_records_files.models import RecordsBuckets
from invenio_records_files.utils import sorted_files_from_bucket


class CODFileObject(FileObject):

    def dumps(self):
        """Create a dump of the metadata associated to the record."""
        self.data.update({
            'bucket': str(self.obj.bucket_id),
            'checksum': self.obj.file.checksum,
            'key': self.obj.key,  # IMPORTANT it must stay here!
            'size': self.obj.file.size,
            'tags': self.obj.get_tags(),
            'version_id': str(self.obj.version_id),
        })
        return self.data


FilesMixin.file_cls = CODFileObject


class CODFilesMixin(FilesMixin):
    """Implement files attribute for Record models."""
    pass


class Record(_Record, CODFilesMixin):
    """Define API for files manipulation using ``FilesMixin``."""

    def delete(self, force=False):
        """Delete a record and also remove the RecordsBuckets if necessary.
        :param force: True to remove also the
            :class:`~invenio_records_files.models.RecordsBuckets` object.
        :returns: Deleted record.
        """
        if force:
            RecordsBuckets.query.filter_by(
                record=self.model,
                bucket=self.files.bucket
            ).delete()
        return super(Record, self).delete(force)
