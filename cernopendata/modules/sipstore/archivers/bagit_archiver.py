import os
import zlib
import json
import re

from hashlib import md5

from invenio_sipstore.archivers import BagItArchiver
from werkzeug.utils import secure_filename
from invenio_files_rest.models import FileInstance

from flask import current_app
from invenio_db import db
from jsonschema import validate
from six import string_types
from werkzeug.utils import import_string

from invenio_sipstore.api import SIP
from invenio_sipstore.archivers import BaseArchiver
from invenio_sipstore.models import SIPMetadata, SIPMetadataType, \
    current_jsonschemas


class CODBagItArchiver(BagItArchiver):
    def __init__(self, sip, data_dir='data/files',
                 metadata_dir='data/metadata', extra_dir='', patch_of=None,
                 include_all_previous=False, tags=None,
                 filenames_mapping_file='data/filenames.txt',
                 files_content=None):

        self.files_content = files_content

        super(CODBagItArchiver, self).__init__(
            sip, data_dir=data_dir, metadata_dir=metadata_dir,
            extra_dir=extra_dir, patch_of=patch_of,
            include_all_previous=include_all_previous, tags=tags,
            filenames_mapping_file=filenames_mapping_file)

    def _calculate_checksum(self, content):
        """Calculate checksum for given content"""
        ad32 = hex(zlib.adler32(content, 1) & 0xffffffff)[2:]

        return "{}:{}".format(self.checksum_algorithm, str(ad32))

    def _get_checksum(self, checksum, checksum_algorithm=None):
        """Return the checksum if the type is the expected."""
        _checksum_algorithm = checksum_algorithm if checksum_algorithm \
            else self.checksum_algorithm

        checksum = checksum.split(':')
        if checksum[0] != _checksum_algorithm or len(checksum) != 2:
            raise AttributeError('Checksum format is not correct.')
        else:
            return checksum[1]

    def _get_data_files(self):
        """Get the file information for all the data files.

        The structure is defined by the JSON Schema
        ``sipstore/file-v1.0.0.json``.

        :return: list of dict containing file information.
        """
        files = []
        for f in self.sip.files:
            files.append(self._generate_sipfile_info(f))

        for f in self.files_content:
            filename = secure_filename(f.get("filename"))

            filepath = re.sub(
                'root://eospublic.cern.ch//eos/opendata/', '',
                f.get("uri"))
            filepath = os.path.join(self.data_dir, filepath)

            files.append(
                dict(
                    checksum=f.get("checksum"),
                    size=f.get("size"),
                    filepath=filepath,
                    fullpath=f.get("uri"),
                    sipfilepath=filename,
                    filename=f.get("filename"),
                    fetched=True,
                )
            )

        return files

    def _write_sipfile(self, fileinfo=None, sipfile=None):
        """Write a SIP file to disk.

        ***Requires** either `fileinfo` or `sipfile` to be passed.

        Parameter `fileinfo` with the file information
        ('file_uuid' key required) or `sipfile` - the
        :py:data:`~invenio_sipstore.models.SIPFile` instance, in which case the
        relevant file information will be generated on the spot.

        :param fileinfo: File information on the SIPFile that is to be written.
        :type fileinfo: dict
        :param sipfile: SIP file to be written.
        :type sipfile: ``invenio_sipstore.models.SIPFile``
        """
        assert fileinfo or sipfile
        if not fileinfo:
            fileinfo = self._generate_sipfile_info(sipfile)
        if sipfile:
            fi = sipfile.file
        else:
            fi = FileInstance.query.get(fileinfo['file_uuid'])
        sf = self.storage_factory(fileurl=fileinfo['fullpath'],
                                  size=fileinfo['size'],
                                  modified=fi.updated)
        return sf.copy(fi.storage(create_dir=False))
