# -*- coding: utf-8 -*-
##
## This file is part of Invenio.
## Copyright (C) 2014 CERN.
##
## Invenio is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## Invenio is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Invenio; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.


def get_filetypes(recid):
    """
        Returns filetypes extensions associated with given record.

        Takes as a parameter the recid of a record.
        @param url_field: recid of a record
    """
    from invenio.legacy.bibdocfile.api import BibRecDocs
    docs = BibRecDocs(recid)
    return [_get_filetype(d.format) for d in docs.list_latest_files()]


def _get_filetype(pre_ext):
    ext = pre_ext.split(";")[0]
    return ext[1:]
