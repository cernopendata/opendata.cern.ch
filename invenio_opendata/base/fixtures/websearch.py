# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2012, 2013, 2014 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

from fixture import DataSet
#from invenio.modules.search.fixtures import FormatData
from invenio.modules.search import fixtures as default

class CollectionData(DataSet):

    siteCollection = default.CollectionData.siteCollection

    class CMS(siteCollection):
        id = 2
        name = 'CMS'
        dbquery = None

    class CMSPrimaryDatasets(siteCollection):
        id = 3
        name = 'CMS-Primary-Datasets'
        dbquery = '980__a:"CMS-Primary-Datasets"'
        names = {
            ('en', 'ln'): u'CMS Primary Datasets',
        }

    class CMSDerivedDatasets(siteCollection):
        id = 4
        name = 'CMS-Derived-Datasets'
        dbquery = '980__a:"CMS-Derived-Datasets"'
        names = {
            ('en', 'ln'): u'CMS Derived Datasets',
        }

    class ALICE(siteCollection):
        id = 5
        name = 'ALICE'
        dbquery = None

    class ALICESimplifiedDatasets(siteCollection):
        id = 6
        name = 'ALICE-Simplified-Datasets'
        dbquery = '980__a:"ALICE-Simplified-Datasets"'
        names = {
            ('en', 'ln'): u'ALICE Simplified Datasets',
        }

    class ALICEAnalyses(siteCollection):
        id = 7
        name = 'ALICE-Analyses'
        dbquery = '980__a:"ALICE-Analyses"'
        names = {
            ('en', 'ln'): u'ALICE Analyses',
        }

    class CMSTools(siteCollection):
        id = 8
        name = 'CMS-Tools'
        dbquery = '980__a:"CMS-Tools"'
        names = {
            ('en', 'ln'): u'CMS Tools',
        }

    class CMSValidatedRuns(siteCollection):
        id = 9
        name = 'CMS-Validated-Runs'
        dbquery = '980__a:"CMS-Validated-Runs"'
        names = {
            ('en', 'ln'): u'CMS Validated Runs',
        }

    class CMSExternalResources(siteCollection):
        id = 10
        name = 'CMS-External-Resources'
        dbquery = '980__a:"CMS-External-Resources"'
        names = {
            ('en', 'ln'): u'CMS External Resources',
        }


class CollectionCollectionData(DataSet):

    class siteCollection_CMS:
        dad = CollectionData.siteCollection
        son = CollectionData.CMS
        score = 0
        type = 'v'

    class CMS_CMSPrimaryDatasets:
        dad = CollectionData.CMS
        son = CollectionData.CMSPrimaryDatasets
        score = 0
        type = 'r'

    class CMS_CMSDerivedDatasets:
        dad = CollectionData.CMS
        son = CollectionData.CMSDerivedDatasets
        score = 1
        type = 'r'

    class CMS_CMSTools:
        dad = CollectionData.CMS
        son = CollectionData.CMSTools
        score = 2
        type = 'r'

    class CMS_CMSValidatedRuns:
        dad = CollectionData.CMS
        son = CollectionData.CMSValidatedRuns
        score = 3
        type = 'r'

    class CMS_CMSExternalResources:
        dad = CollectionData.CMS
        son = CollectionData.CMSExternalResources
        score = 4
        type = 'r'

    class siteCollection_CMSPrimaryDatasets:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSPrimaryDatasets
        score = 0
        type = 'r'

    class siteCollection_CMSDerivedDatasets:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSDerivedDatasets
        score = 1
        type = 'r'

    class siteCollection_CMSTools:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSTools
        score = 2
        type = 'r'

    class siteCollection_CMSValidatedRuns:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSValidatedRuns
        score = 3
        type = 'r'

    class siteCollection_CMSExternalResources:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSExternalResources
        score = 4
        type = 'r'

    class siteCollection_ALICE:
        dad = CollectionData.siteCollection
        son = CollectionData.ALICE
        score = 1
        type = 'v'

    class ALICE_ALICESimplifiedDatasets:
        dad = CollectionData.ALICE
        son = CollectionData.ALICESimplifiedDatasets
        score = 0
        type = 'r'

    class ALICE_ALICEAnalyses:
        dad = CollectionData.ALICE
        son = CollectionData.ALICEAnalyses
        score = 1
        type = 'r'


class CollectiondetailedrecordpagetabsData(DataSet):

    class Collectiondetailedrecordpagetabs_1:
        tabs = u'metadata;files'
        id_collection = CollectionData.siteCollection.ref('id')


class CollectionFormatData(DataSet):

    class CollectionFormat_1_1:
        score = 100
        id_format = 1 # FormatData.Format_1.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_2:
        score = 90
        id_format = 2 # FormatData.Format_2.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_3:
        score = 80
        id_format = 3 # FormatData.Format_3.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_4:
        score = 70
        id_format = 4 # FormatData.Format_4.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_5:
        score = 60
        id_format = 5 # FormatData.Format_5.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')


class PortalboxData(DataSet):

    class Portalbox_1:
        body = u'The CMS (Compact Muon Solenoid) experiment is one of two large general-purpose particle physics detectors built on the Large Hadron Collider (LHC) at CERN in Switzerland and France. The goal of CMS is to investigate a wide range of physics, including properties of the recently discovered Higgs boson as well as searches for extra dimensions and particles that could make up dark matter.'
        id = 1
        title = u'description'

    class Portalbox_2:
        body = u'CMS.gif'
        id = 2
        title = u'image'

    class Portalbox_3:
        body = u'ALICE (A Large Ion Collider Experiment) is one of seven detector experiments at the Large Hadron Collider at CERN. The other six are: ATLAS, CMS, TOTEM, LHCb, LHCf and MoEDAL. ALICE is optimized to study heavy-ion (Pb-Pb nuclei) collisions at a centre of mass energy of 2.76 TeV per nucleon pair. The resulting temperature and energy density are expected to be high enough to produce quark–gluon plasma, a state of matter wherein quarks and gluons are freed. Similar conditions are believed to existed a fraction of the second after the Big Bang before quarks and gluons bound together to form hadrons and heavier particles.'
        id = 3
        title = u'description'

    class Portalbox_4:
        body = u'ALICE.gif'
        id = 4
        title = u'image'

    class Portalbox_5:
        body = u'CMS primary datasets are AOD (Analysis Object Data) files, which contain the information that is needed for analysis: (1) all the high-level physics objects (such as muons, electrons, etc.) (2) tracks with associated hits, calorimetric clusters with associated hits, vertices and (3) information about event selection (triggers), data needed for further selection and identification criteria for the physics objects.'
        id = 5
        title = u'description'

    class Portalbox_6:
        body = u'default.png'
        id = 6
        title = u'image'

    class Portalbox_7:
        body = u'This collection includes any data, which have been derived from the CMS primary datasets. They may be reduced in sense that only part of the information is kept, or only part of the events are selected. - It includes datasets, which may be accessed using the VM image of the CMS environment, and datasets, which are adapted to other tools and applications. The tools and instruction to use and access these data are linked to the record.'
        id = 7
        title = u'description'

    class Portalbox_8:
        body = u'default.png'
        id = 8
        title = u'image'

    class Portalbox_9:
        body = u'ALICE Simplified Datasets.ALICE Simplified Datasets.ALICE Simplified Datasets.ALICE Simplified Datasets.ALICE Simplified Datasets.ALICE Simplified Datasets.ALICE Simplified Datasets.ALICE Simplified Datasets.ALICE Simplified Datasets.ALICE Simplified Datasets'
        id = 9
        title = u'description'

    class Portalbox_10:
        body = u'default.png'
        id = 10
        title = u'image'

    class Portalbox_11:
        body = u'ALICE Analyses.ALICE Analyses.ALICE Analyses.ALICE Analyses.ALICE Analyses.ALICE Analyses.ALICE Analyses.ALICE Analyses.ALICE Analyses.ALICE Analyses'
        id = 11
        title = u'description'

    class Portalbox_12:
        body = u'default.png'
        id = 12
        title = u'image'

    class Portalbox_13:
        body = u'This collection includes tools, with which the CMS open data can be accessed and used. It contains the VM image of the CMS environment through which the datasets can be read. It includes the software with which the derived datasets were produced, and analysis examples. It also contains the source code for the online applications deployed on this site.'
        id = 13
        title = u'description'

    class Portalbox_14:
        body = u'This collection includes CMS Validated Runs'
        id = 14
        title = u'description'

    class Portalbox_15:
        body = u'This collection includes CMS external resources'
        id = 15
        title = u'description'

class CollectionPortalboxData(DataSet):

    class CollectionPortalbox_2_1_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_1.ref('id')
        score = 100
        id_collection = CollectionData.CMS.ref('id')

    class CollectionPortalbox_2_2_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_2.ref('id')
        score = 100
        id_collection = CollectionData.CMS.ref('id')

    class CollectionPortalbox_5_3_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_3.ref('id')
        score = 100
        id_collection = CollectionData.ALICE.ref('id')

    class CollectionPortalbox_5_4_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_4.ref('id')
        score = 100
        id_collection = CollectionData.ALICE.ref('id')

    class CollectionPortalbox_3_5_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_5.ref('id')
        score = 100
        id_collection = CollectionData.CMSPrimaryDatasets.ref('id')

    class CollectionPortalbox_3_6_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_6.ref('id')
        score = 100
        id_collection = CollectionData.CMSPrimaryDatasets.ref('id')

    class CollectionPortalbox_4_7_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_7.ref('id')
        score = 100
        id_collection = CollectionData.CMSDerivedDatasets.ref('id')

    class CollectionPortalbox_4_8_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_8.ref('id')
        score = 100
        id_collection = CollectionData.CMSDerivedDatasets.ref('id')

    class CollectionPortalbox_6_9_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_9.ref('id')
        score = 100
        id_collection = CollectionData.ALICEAnalyses.ref('id')

    class CollectionPortalbox_6_10_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_10.ref('id')
        score = 100
        id_collection = CollectionData.ALICEAnalyses.ref('id')

    class CollectionPortalbox_7_11_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_11.ref('id')
        score = 100
        id_collection = CollectionData.ALICESimplifiedDatasets.ref('id')

    class CollectionPortalbox_7_12_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_12.ref('id')
        score = 100
        id_collection = CollectionData.ALICESimplifiedDatasets.ref('id')

    class CollectionPortalbox_8_13_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_13.ref('id')
        score = 100
        id_collection = CollectionData.CMSTools.ref('id')

    class CollectionPortalbox_9_14_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_14.ref('id')
        score = 100
        id_collection = CollectionData.CMSValidatedRuns.ref('id')

    class CollectionPortalbox_10_15_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_15.ref('id')
        score = 100
        id_collection = CollectionData.CMSExternalResources.ref('id')


class FacetCollectionData(DataSet):

    class FacetCollection_1:
        id = 1
        id_collection = CollectionData.siteCollection.ref('id')
        order = 1
        facet_name = 'collection'


__all__ = (
    'CollectionData',
    'CollectionCollectionData',
    'CollectiondetailedrecordpagetabsData',
    'CollectionFormatData',
    'PortalboxData',
    'CollectionPortalboxData',
    'FacetCollectionData',
)
