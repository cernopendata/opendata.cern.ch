# -*- coding: utf-8 -*-
#
## This file is part of Invenio.
## Copyright (C) 2013 CERN.
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

import datetime
from fixture import DataSet


class JrnJOURNALData(DataSet):

    class JrnJOURNAL_1:
        id = 1
        name = u'AtlantisTimes'


class JrnISSUEData(DataSet):

    class JrnISSUE_1_022009:
        id_jrnJOURNAL = JrnJOURNALData.JrnJOURNAL_1.ref('id')
        issue_number = u'02/2009'
        date_announced = datetime.datetime(2009, 1, 9, 0, 0)
        issue_display = u'02-03/2009'
        date_released = datetime.datetime(2009, 1, 9, 0, 0)

    class JrnISSUE_1_032009:
        id_jrnJOURNAL = JrnJOURNALData.JrnJOURNAL_1.ref('id')
        issue_number = u'03/2009'
        date_announced = None
        issue_display = u'02-03/2009'
        date_released = datetime.datetime(2009, 1, 16, 0, 0)
