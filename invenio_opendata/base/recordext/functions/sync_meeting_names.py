# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2014 CERN.
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

from invenio.modules.jsonalchemy.jsonext.functions.util_merge_fields_info_list \
    import util_merge_fields_info_list


def sync_meeting_names(self, field_name, connected_field, action):  # pylint: disable=W0613
    """
    Sync corporate names content only when `__setitem__` or similar is used
    """
    if action == 'set':
        if field_name == 'corporate_names' and self.get('corporate_names'):
            self.__setitem__('_first_corporate_name',
                             self['corporate_names'][0],
                             exclude=['connect'])
            if self['corporate_names'][1:]:
                self.__setitem__('_additional_corporate_names',
                                 self['corporate_names'][1:],
                                 exclude=['connect'])
        elif field_name in ('_first_author', '_additional_authors'):
            self.__setitem__(
                'corporate_names',
                util_merge_fields_info_list(self, ['_first_corporate_name',
                                            '_additional_corporate_names']),
                exclude=['connect'])
