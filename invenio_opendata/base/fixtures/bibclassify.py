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

from fixture import DataSet
from .websearch import CollectionData


class ClsMETHODData(DataSet):

    class ClsMETHOD_1:
        id = 1
        last_updated = None
        description = u'High Energy Physics Taxonomy'
        name = u'HEP'
        location = u'http://invenio-software.org/download/invenio-demo-site-files/HEP.rdf'

    class ClsMETHOD_2:
        id = 2
        last_updated = None
        description = u'NASA Subjects'
        name = u'NASA-subjects'
        location = u'http://invenio-software.org/download/invenio-demo-site-files/NASA-subjects.rdf'


class CollectionClsMETHODData(DataSet):

    class CollectionClsMETHOD_12_2:
        id_clsMETHOD = ClsMETHODData.ClsMETHOD_2.ref('id')
        id_collection = CollectionData.experimentalPhysics.ref('id')

    class CollectionClsMETHOD_2_1:
        id_clsMETHOD = ClsMETHODData.ClsMETHOD_1.ref('id')
        id_collection = CollectionData.preprints.ref('id')
