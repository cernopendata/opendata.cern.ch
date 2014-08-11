# -*- coding: utf-8 -*-
#
## This file is part of Invenio.
## Copyright (C) 2012, 2013, 2014 CERN.
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

from invenio.config import CFG_SITE_NAME
from fixture import DataSet
from invenio.modules.search.fixtures import FormatData


class CollectionData(DataSet):

    class siteCollection:
        id = 1
        name = CFG_SITE_NAME
        dbquery = None

    class CMS(siteCollection):
        id = 2
        name = 'CMS'
        dbquery = None

    class CMSPrimaryDataset(siteCollection):
        id = 3
        name = 'CMS Primary Dataset'
        dbquery = '980__a:"CMSPRIMARYDATASET"'

    class CMSReducedDataset(siteCollection):
        id = 4
        name = 'CMS Reduced Dataset'
        dbquery = '980__a:"CMSREDUCEDDATASET"'

    class ALICE(siteCollection):
        id = 5
        name = 'ALICE'
        dbquery = None

    class ALICESimplifiedDataset(siteCollection):
        id = 6
        name = 'ALICE Simplified Dataset'
        dbquery = '980__a:"ALICESIMPLIFIEDDATASET"'

    class ALICEAnalysis(siteCollection):
        id = 7
        name = 'ALICE Analysis'
        dbquery = '980__a:"ALICEANALYSIS"'


class CollectionCollectionData(DataSet):

    class siteCollection_CMS:
        dad = CollectionData.siteCollection
        son = CollectionData.CMS
        score = 0
        type = 'r'

    class CMS_CMSPrimaryDataset:
        dad = CollectionData.CMS
        son = CollectionData.CMSPrimaryDataset
        score = 0
        type = 'r'

    class CMS_CMSReducedDataset:
        dad = CollectionData.CMS
        son = CollectionData.CMSReducedDataset
        score = 1
        type = 'r'

    class siteCollection_ALICE:
        dad = CollectionData.siteCollection
        son = CollectionData.ALICE
        score = 1
        type = 'r'

    class ALICE_ALICESimplifiedDataset:
        dad = CollectionData.ALICE
        son = CollectionData.ALICESimplifiedDataset
        score = 0
        type = 'r'

    class ALICE_ALICEAnalysis:
        dad = CollectionData.ALICE
        son = CollectionData.ALICEAnalysis
        score = 1
        type = 'r'


class CollectiondetailedrecordpagetabsData(DataSet):

    class Collectiondetailedrecordpagetabs_1:
        tabs = u'metadata;files;comments'
        id_collection = CollectionData.siteCollection.ref('id')


class CollectionFormatData(DataSet):

    class CollectionFormat_1_1:
        score = 100
        id_format = FormatData.Format_1.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_2:
        score = 90
        id_format = FormatData.Format_2.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_3:
        score = 80
        id_format = FormatData.Format_3.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_4:
        score = 70
        id_format = FormatData.Format_4.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_5:
        score = 60
        id_format = FormatData.Format_5.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')
