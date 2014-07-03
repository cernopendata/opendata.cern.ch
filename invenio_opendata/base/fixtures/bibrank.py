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
from .websearch import \
    CollectionData as CollectionDataDemosite


class RnkMETHODData(DataSet):

    class RnkMETHOD_2:
        last_updated = None
        id = 2
        name = u'demo_jif'

    class RnkMETHOD_3:
        last_updated = None
        id = 3
        name = u'citation'

    class RnkMETHOD_4:
        last_updated = None
        id = 4
        name = u'citerank_citation_t'

    class RnkMETHOD_5:
        last_updated = None
        id = 5
        name = u'citerank_pagerank_c'

    class RnkMETHOD_6:
        last_updated = None
        id = 6
        name = u'citerank_pagerank_t'

    class RnkMETHOD_7:
        last_updated = None
        id = 7
        name = u'selfcites'


class CollectionRnkMETHODData(DataSet):

    class CollectionRnkMETHOD_15_2:
        score = 90
        id_rnkMETHOD = RnkMETHODData.RnkMETHOD_2.ref('id')
        id_collection = CollectionDataDemosite.articlesPreprints.ref('id')

    class CollectionRnkMETHOD_15_3:
        score = 80
        id_rnkMETHOD = RnkMETHODData.RnkMETHOD_3.ref('id')
        id_collection = CollectionDataDemosite.articlesPreprints.ref('id')

    class CollectionRnkMETHOD_15_4:
        score = 70
        id_rnkMETHOD = RnkMETHODData.RnkMETHOD_4.ref('id')
        id_collection = CollectionDataDemosite.articlesPreprints.ref('id')

    class CollectionRnkMETHOD_15_5:
        score = 60
        id_rnkMETHOD = RnkMETHODData.RnkMETHOD_5.ref('id')
        id_collection = CollectionDataDemosite.articlesPreprints.ref('id')

    class CollectionRnkMETHOD_15_6:
        score = 50
        id_rnkMETHOD = RnkMETHODData.RnkMETHOD_6.ref('id')
        id_collection = CollectionDataDemosite.articlesPreprints.ref('id')

    class CollectionRnkMETHOD_15_7:
        score = 80
        id_rnkMETHOD = RnkMETHODData.RnkMETHOD_7.ref('id')
        id_collection = CollectionDataDemosite.articlesPreprints.ref('id')

    class CollectionRnkMETHOD_1_3:
        score = 10
        id_rnkMETHOD = RnkMETHODData.RnkMETHOD_3.ref('id')
        id_collection = CollectionDataDemosite.siteCollection.ref('id')

    class CollectionRnkMETHOD_1_7:
        score = 10
        id_rnkMETHOD = RnkMETHODData.RnkMETHOD_7.ref('id')
        id_collection = CollectionDataDemosite.siteCollection.ref('id')
