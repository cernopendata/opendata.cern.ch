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

from datetime import datetime
from fixture import DataSet


class OaiREPOSITORYData(DataSet):

    class OaiREPOSITORY_2:
        f1 = u'reportnumber'
        f2 = u'division'
        f3 = u''
        setRecList = None
        setDefinition = u'c=;p1=CERN;f1=reportnumber;m1=a;p2=(EP|PPE);f2=division;m2=r;p3=;f3=;m3=;'
        last_updated = datetime.now()
        id = 2
        setSpec = u'cern:experiment'
        setDescription = u''
        p3 = u''
        p1 = u'CERN'
        setName = u'CERN experimental papers'
        setCollection = u''
        p2 = u'(EP|PPE)'
        m1 = u'a'
        m3 = u''
        m2 = u'r'

    class OaiREPOSITORY_3:
        f1 = u'reportnumber'
        f2 = u'division'
        f3 = u''
        setRecList = None
        setDefinition = u'c=;p1=CERN;f1=reportnumber;m1=a;p2=TH;f2=division;m2=e;p3=;f3=;m3=;'
        last_updated = datetime.now()
        id = 3
        setSpec = u'cern:theory'
        setDescription = u''
        p3 = u''
        p1 = u'CERN'
        setName = u'CERN theoretical papers'
        setCollection = u''
        p2 = u'TH'
        m1 = u'a'
        m3 = u''
        m2 = u'e'
