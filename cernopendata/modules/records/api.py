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
from invenio_records_files.api import FileObject, FilesIterator, _writable

from invenio_records_files.models import RecordsBuckets
from invenio_records_files.utils import sorted_files_from_bucket


class CODFileObject(FileObject):

    def dumps(self):
        """Create a dump of the metadata associated to the record."""
        # import ipdb
        # ipdb.set_trace()
        self.data.update({
            'bucket': str(self.obj.bucket_id),
            'checksum': self.obj.file.checksum,
            'key': self.obj.key,  # IMPORTANT it must stay here!
            'size': self.obj.file.size,
            'type': self.data.get("filetype", ""),
            'version_id': str(self.obj.version_id),
        })
        return self.data


class CODFilesIterator(FilesIterator):
    """Iterator for files."""

    @_writable
    def __setitem__(self, key, item):
        """Add file inside a deposit."""
        assert 'uri' in item
        assert 'size' in item
        assert 'checksum' in item

        with db.session.begin_nested():
            # save the file
            f = FileInstance.create()
            f.set_uri(item.get("uri"), item.get(
                "size"), item.get("checksum"))

            obj = ObjectVersion.create(
                bucket=self.bucket, key=key, _file_id=f.id)
            self.filesmap[key] = self.file_cls(
                obj, item.get("data", {})).dumps()
            self.flush()


class CODFilesMixin(object):
    """Implement files attribute for Record models.
    .. note::
       Implement ``_create_bucket()`` in subclass to allow files property
       to automatically create a bucket in case no bucket is present.
    """

    file_cls = CODFileObject
    """File class used to generate the instance of files. Default to
    :class:`~invenio_records_files.api.FileObject`
    """

    files_iter_cls = CODFilesIterator
    """Files iterator class used to generate the files iterator. Default to
    :class:`~invenio_records_files.api.FilesIterator`
    """

    def _create_bucket(self):
        """Return an instance of ``Bucket`` class.
        .. note:: Reimplement in children class for custom behavior.
        :returns: Instance of :class:`invenio_files_rest.models.Bucket`.
        """
        return None

    @property
    def files(self):
        """Get files iterator.
        :returns: Files iterator.
        """
        if self.model is None:
            raise MissingModelError()

        records_buckets = RecordsBuckets.query.filter_by(
            record_id=self.id).first()

        if not records_buckets:
            bucket = self._create_bucket()
            if not bucket:
                return None
            RecordsBuckets.create(record=self.model, bucket=bucket)
        else:
            bucket = records_buckets.bucket

        return self.files_iter_cls(self, bucket=bucket, file_cls=self.file_cls)

    @files.setter
    def files(self, data):
        """Set files from data."""
        current_files = self.files
        if current_files:
            raise RuntimeError('Can not update existing files.')
        for key in data:
            current_files[key] = data[key]


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
