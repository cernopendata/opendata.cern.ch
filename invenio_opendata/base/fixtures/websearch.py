# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2012, 2013, 2014, 2015, 2016 CERN.
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

from fixture import DataSet
# from invenio.modules.search.fixtures import FormatData
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

    class ALICEDerivedDatasets(siteCollection):
        id = 6
        name = 'ALICE-Derived-Datasets'
        dbquery = '980__a:"ALICE-Derived-Datasets"'
        names = {
            ('en', 'ln'): u'ALICE Derived Datasets',
        }

    class ALICETools(siteCollection):
        id = 7
        name = 'ALICE-Tools'
        dbquery = '980__a:"ALICE-Tools"'
        names = {
            ('en', 'ln'): u'ALICE Tools',
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

    class CMSLearningResources(siteCollection):
        id = 10
        name = 'CMS-Learning-Resources'
        dbquery = '980__a:"CMS-Learning-Resources"'
        names = {
            ('en', 'ln'): u'CMS Learning Resources',
        }

    class ALICEReconstructedData(siteCollection):
        id = 11
        name = 'ALICE-Reconstructed-Data'
        dbquery = '980__a:"ALICE-Reconstructed-Data"'
        names = {
            ('en', 'ln'): u'ALICE Reconstructed Data',
        }

    class ATLAS(siteCollection):
        id = 12
        name = 'ATLAS'
        dbquery = None

    class ATLASDerivedDatasets(siteCollection):
        id = 13
        name = 'ATLAS-Derived-Datasets'
        dbquery = '980__a:"ATLAS-Derived-Datasets"'
        names = {
            ('en', 'ln'): u'ATLAS Derived Datasets',
        }

    class ATLASLearningResources(siteCollection):
        id = 14
        name = 'ATLAS-Learning-Resources'
        dbquery = '980__a:"ATLAS-Learning-Resources"'
        names = {
            ('en', 'ln'): u'ATLAS Learning Resources',
        }

    class ATLASTools(siteCollection):
        id = 15
        name = 'ATLAS-Tools'
        dbquery = '980__a:"ATLAS-Tools"'
        names = {
            ('en', 'ln'): u'ATLAS Tools',
        }

    class LHCb(siteCollection):
        id = 16
        name = 'LHCb'
        dbquery = None

    class LHCbDerivedDatasets(siteCollection):
        id = 17
        name = 'LHCb-Derived-Datasets'
        dbquery = '980__a:"LHCb-Derived-Datasets"'
        names = {
            ('en', 'ln'): u'LHCb Derived Datasets',
        }

    class LHCbTools(siteCollection):
        id = 18
        name = 'LHCb-Tools'
        dbquery = '980__a:"LHCb-Tools"'
        names = {
            ('en', 'ln'): u'LHCb Tools',
        }

    class LHCbLearningResources(siteCollection):
        id = 19
        name = 'LHCb-Learning-Resources'
        dbquery = '980__a:"LHCb-Learning-Resources"'
        names = {
            ('en', 'ln'): u'LHCb Learning Resources',
        }

    class ALICELearningResources(siteCollection):
        id = 20
        name = 'ALICE-Learning-Resources'
        dbquery = '980__a:"ALICE-Learning-Resources"'
        names = {
            ('en', 'ln'): u'ALICE Learning Resources',
        }

    class CMSOpenDataInstructions(siteCollection):
        id = 21
        name = 'CMS-Open-Data-Instructions'
        dbquery = '980__a:"CMS-Open-Data-Instructions"'
        names = {
            ('en', 'ln'): u'CMS Open Data Instructions',
        }

    class AuthorLists(siteCollection):
        id = 22
        name = 'Author-Lists'
        dbquery = '980__a:"Author-Lists"'
        names = {
            ('en', 'ln'): u'Author Lists',
        }

    class DataPolicies(siteCollection):
        id = 23
        name = 'Data-Policies'
        dbquery = '980__a:"Data-Policies"'
        names = {
            ('en', 'ln'): u'Data-Policies',
        }

    class ATLASHiggsChallenge2014(siteCollection):
        id = 24
        name = 'ATLAS-Higgs-Challenge-2014'
        dbquery = '980__a:"ATLAS-Higgs-Challenge-2014"'
        names = {
            ('en', 'ln'): u'ATLAS Higgs Challenge 2014',
        }

    class CMSSimulatedDatasets(siteCollection):
        id = 25
        name = 'CMS-Simulated-Datasets'
        dbquery = '980__a:"CMS-Simulated-Datasets"'
        names = {
            ('en', 'ln'): u'CMS Simulated Datasets',
        }

    class CMSValidationUtilities(siteCollection):
        id = 26
        name = 'CMS-Validation-Utilities'
        dbquery = '980__a:"CMS-Validation-Utilities"'
        names = {
            ('en', 'ln'): u'CMS Validation Utilities',
        }

    class CMSTriggerInformation(siteCollection):
        id = 27
        name = 'CMS-Trigger-Information'
        dbquery = '980__a:"CMS-Trigger-Information"'
        names = {
            ('en', 'ln'): u'CMS Trigger Information',
        }

    class CMSConditionData(siteCollection):
        id = 28
        name = 'CMS-Condition-Data'
        dbquery = '980__a:"CMS-Condition-Data"'
        names = {
            ('en', 'ln'): u'CMS Condition Data',
        }

    class CMSConfigurationFiles(siteCollection):
        id = 29
        name = 'CMS-Configuration-Files'
        dbquery = '980__a:"CMS-Configuration-Files"'
        names = {
            ('en', 'ln'): u'CMS Configuration Files',
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

    class CMS_CMSSimulatedDatasets:
        dad = CollectionData.CMS
        son = CollectionData.CMSSimulatedDatasets
        score = 1
        type = 'r'

    class CMS_CMSDerivedDatasets:
        dad = CollectionData.CMS
        son = CollectionData.CMSDerivedDatasets
        score = 2
        type = 'r'

    class CMS_CMSTools:
        dad = CollectionData.CMS
        son = CollectionData.CMSTools
        score = 3
        type = 'r'

    class CMS_CMSValidationUtilities:
        dad = CollectionData.CMS
        son = CollectionData.CMSValidationUtilities
        score = 4
        type = 'r'

    class CMS_CMSLearningResources:
        dad = CollectionData.CMS
        son = CollectionData.CMSLearningResources
        score = 5
        type = 'r'

    class CMS_CMSOpenDataInstructions:
        dad = CollectionData.CMS
        son = CollectionData.CMSOpenDataInstructions
        score = 6
        type = 'r'

    class CMS_CMSTriggerInformation:
        dad = CollectionData.CMS
        son = CollectionData.CMSTriggerInformation
        score = 7
        type = 'r'

    class CMS_CMSConditionData:
        dad = CollectionData.CMS
        son = CollectionData.CMSConditionData
        score = 8
        type = 'r'

    class CMS_CMSConfigurationFiles:
        dad = CollectionData.CMS
        son = CollectionData.CMSConfigurationFiles
        score = 9
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

    class siteCollection_CMSValidationUtilities:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSValidationUtilities
        score = 3
        type = 'r'

    class siteCollection_CMSLearningResources:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSLearningResources
        score = 4
        type = 'r'

    class siteCollection_ALICE:
        dad = CollectionData.siteCollection
        son = CollectionData.ALICE
        score = 1
        type = 'v'

    class ALICE_ALICEDerivedDatasets:
        dad = CollectionData.ALICE
        son = CollectionData.ALICEDerivedDatasets
        score = 0
        type = 'r'

    class ALICE_ALICEReconstructedData:
        dad = CollectionData.ALICE
        son = CollectionData.ALICEReconstructedData
        score = 1
        type = 'r'

    class ALICE_ALICETools:
        dad = CollectionData.ALICE
        son = CollectionData.ALICETools
        score = 2
        type = 'r'

    class siteCollection_ALICEDerivedDatasets:
        dad = CollectionData.siteCollection
        son = CollectionData.ALICEDerivedDatasets
        score = 5
        type = 'r'

    class siteCollection_ALICEReconstructedData:
        dad = CollectionData.siteCollection
        son = CollectionData.ALICEReconstructedData
        score = 6
        type = 'r'

    class siteCollection_ALICETools:
        dad = CollectionData.siteCollection
        son = CollectionData.ALICETools
        score = 7
        type = 'r'

    class siteCollection_ATLAS:
        dad = CollectionData.siteCollection
        son = CollectionData.ATLAS
        score = 2
        type = 'v'

    class siteCollection_ATLASDerivedDatasets:
        dad = CollectionData.siteCollection
        son = CollectionData.ATLASDerivedDatasets
        score = 8
        type = 'r'

    class siteCollection_ATLASLearningResources:
        dad = CollectionData.siteCollection
        son = CollectionData.ATLASLearningResources
        score = 9
        type = 'r'

    class siteCollection_ATLASTools:
        dad = CollectionData.siteCollection
        son = CollectionData.ATLASTools
        score = 10
        type = 'r'

    class ATLAS_ATLASDerivedDatasets:
        dad = CollectionData.ATLAS
        son = CollectionData.ATLASDerivedDatasets
        score = 0
        type = 'r'

    class ATLAS_ATLASLearningResources:
        dad = CollectionData.ATLAS
        son = CollectionData.ATLASLearningResources
        score = 1
        type = 'r'

    class ATLAS_ATLASTools:
        dad = CollectionData.ATLAS
        son = CollectionData.ATLASTools
        score = 2
        type = 'r'

    class ATLAS_ATLASHiggsChallenge2014:
        dad = CollectionData.ATLAS
        son = CollectionData.ATLASHiggsChallenge2014
        score = 3
        type = 'r'

    class siteCollection_LHCb:
        dad = CollectionData.siteCollection
        son = CollectionData.LHCb
        score = 3
        type = 'v'

    class siteCollection_LHCbDerivedDatasets:
        dad = CollectionData.siteCollection
        son = CollectionData.LHCbDerivedDatasets
        score = 11
        type = 'r'

    class siteCollection_LHCbTools:
        dad = CollectionData.siteCollection
        son = CollectionData.LHCbTools
        score = 12
        type = 'r'

    class siteCollection_LHCbLearningResources:
        dad = CollectionData.siteCollection
        son = CollectionData.LHCbLearningResources
        score = 13
        type = 'r'

    class LHCb_LHCbDerivedDatasets:
        dad = CollectionData.LHCb
        son = CollectionData.LHCbDerivedDatasets
        score = 0
        type = 'r'

    class LHCb_LHCbTools:
        dad = CollectionData.LHCb
        son = CollectionData.LHCbTools
        score = 1
        type = 'r'

    class LHCb_LHCbLearningResources:
        dad = CollectionData.LHCb
        son = CollectionData.LHCbLearningResources
        score = 2
        type = 'r'

    class siteCollection_ALICELearningResources:
        dad = CollectionData.siteCollection
        son = CollectionData.ALICELearningResources
        score = 14
        type = 'r'

    class ALICE_ALICELearningResources:
        dad = CollectionData.ALICE
        son = CollectionData.ALICELearningResources
        score = 3
        type = 'r'

    class siteCollection_CMSOpenDataInstructions:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSOpenDataInstructions
        score = 14
        type = 'r'

    class siteCollection_AuthorLists:
        dad = CollectionData.siteCollection
        son = CollectionData.AuthorLists
        score = 15
        type = 'r'

    class siteCollection_DataPolicies:
        dad = CollectionData.siteCollection
        son = CollectionData.DataPolicies
        score = 16
        type = 'r'

    class siteCollection_ATLASHiggsChallenge2014:
        dad = CollectionData.siteCollection
        son = CollectionData.ATLASHiggsChallenge2014
        score = 17
        type = 'r'

    class siteCollection_CMSSimulatedDatasets:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSSimulatedDatasets
        score = 18
        type = 'r'

    class siteCollection_CMSTriggerInformation:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSTriggerInformation
        score = 19
        type = 'r'

    class siteCollection_CMSConditionData:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSConditionData
        score = 20
        type = 'r'

    class siteCollection_CMSConfigurationFiles:
        dad = CollectionData.siteCollection
        son = CollectionData.CMSConfigurationFiles
        score = 21
        type = 'r'


class CollectiondetailedrecordpagetabsData(DataSet):

    class Collectiondetailedrecordpagetabs_1:
        tabs = u'metadata;files'
        id_collection = CollectionData.siteCollection.ref('id')


class CollectionFormatData(DataSet):

    class CollectionFormat_1_1:
        score = 100
        id_format = 1  # FormatData.Format_1.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_2:
        score = 90
        id_format = 2  # FormatData.Format_2.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_3:
        score = 80
        id_format = 3  # FormatData.Format_3.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_4:
        score = 70
        id_format = 4  # FormatData.Format_4.ref('id')
        id_collection = CollectionData.siteCollection.ref('id')

    class CollectionFormat_1_5:
        score = 60
        id_format = 5  # FormatData.Format_5.ref('id')
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
        body = u'<a href="http://aliceinfo.cern.ch/Public/Welcome.html">ALICE</a> (A Large Ion Collider Experiment) is a heavy-ion <a href="http://home.web.cern.ch/about/how-detector-works">detector</a> designed to study the physics of strongly interacting matter at extreme energy densities, where a phase of matter called <a href="http://home.web.cern.ch/about/physics/heavy-ions-and-quark-gluon-plasma">quark-gluon plasma</a> forms.</br>The ALICE collaboration uses the 10,000-tonne ALICE detector – 26 m long, 16 m high and 16 m wide – to study quark-gluon plasma. The detector sits in a vast cavern 56 m below ground close to the village of St Genis-Pouilly in France, receiving beams from the LHC. More than 1000 scientists are part of the collaboration.'
        id = 3
        title = u'description'

    class Portalbox_4:
        body = u'ALICE.gif'
        id = 4
        title = u'image'

    class Portalbox_5:
        body = u'CMS primary datasets are AOD (Analysis Object Data) files, which contain the information that is needed for analysis#$#$#: (1) all the high-level physics objects (such as muons, electrons, etc.) (2) tracks with associated hits, calorimetric clusters with associated hits, vertices and (3) information about event selection (triggers), data needed for further selection and identification criteria for the physics objects.'
        id = 5
        title = u'description'

    class Portalbox_6:
        body = u'default.png'
        id = 6
        title = u'image'

    class Portalbox_7:
        body = u'This collection includes data that have been derived from the CMS primary datasets#$#$#. The data may be reduced in the sense that (a) only part of the information is kept or (b) only part of the events are selected. Datasets include those which may be accessed using the VM image of the CMS environment or those which are adapted for other tools and applications. The tools and instructions to access and use these data are linked to each record.'
        id = 7
        title = u'description'

    class Portalbox_8:
        body = u'default.png'
        id = 8
        title = u'image'

    class Portalbox_9:
        body = u'This collection contains all software packages needed to run a set of ALICE physics masterclasses and a simple ESD-based analysis.'
        id = 9
        title = u'description'

    class Portalbox_10:
        body = u'default.png'
        id = 10
        title = u'image'

    class Portalbox_11:
        body = u'This collection contains reduced information for the reconstructed tracks and their associated clusters from a set of PbPb events. It can be used by with ALICE RAA masterclass package including an event display.'
        id = 11
        title = u'description'

    class Portalbox_12:
        body = u'default.png'
        id = 12
        title = u'image'

    class Portalbox_13:
        body = u'This collection includes tools with which the CMS open data can be accessed and used#$#$#. It contains the VM image of the CMS environment through which the datasets can be read. It includes the software with which the derived datasets were produced, and analysis examples. It also contains the source code for the online applications deployed on this site.'
        id = 13
        title = u'description'

    class Portalbox_14:
        body = u'This collection includes CMS Validated Runs'
        id = 14
        title = u'description'

    class Portalbox_15:
        body = u'This collection includes learning resources that use CMS public data#$#$#. The items in this collection are suitable for education purposes.'
        id = 15
        title = u'description'

    class Portalbox_16:
        body = u'This collection contains files with reconstructed ALICE events in the Event Summary Data (ESD) format and they can be used for standard ALICE analysis.'
        id = 16
        title = u'description'

    class Portalbox_17:
        body = u'CMS Open Data are available in the same format as used in analysis by CMS physicists. A CMS-specific analysis framework is needed, and it is provided as a Virtual Machine image with the CMS analysis environment. The data can be accessed directly through the VM image. Basic information of the data contents is provided in <a href="http://opendata.cern.ch/about/CMS">About CMS</a> and in <a href="http://opendata.cern.ch/about/CMS-Physics-Objects">About CMS Physics Objects</a>. The original data are in primary datasets, i.e. no selection nor identification criteria have been applied (apart from the trigger decision), and these have to be applied in the subsequent analysis step. The 2011 data release includes simulated Monte Carlo datasets, but no simulated datasets are provided for the 2010 release.'
        id = 17
        title = u'research_description'

    class Portalbox_18:
        body = u'These ALICE datasets contain a sample of events from the pp and PbPb LHC runs in 2010, in the ESD (event summary data) format of the ALICE reconstruction program. The events are unbiased and are not a result of event selections and this format is directly usable by the analysis done by ALICE physicists. The data can be downloaded and used from a specific ALICE virtual machine image which can be installed using this procedure (link) and which demonstrates some ALICE analysis and event display examples. A single dataset is exposed in the form of a custom VSD (V0 summary data) format which is not usable in normal analysis but just by a set of masterclasses available also from the ALICE VM. For the first release, no simulated Monte Carlo datasets are provided.'
        id = 18
        title = u'research_description'

    class Portalbox_19:
        body = u'The ATLAS (A Toroidal LHC ApparatuS) experiment is a general purpose detector exploring topics like the properties of the Higgs-like particle, extra dimensions of space, unification of fundamental forces, and evidence for dark matter candidates in the Universe.'
        id = 19
        title = u'description'

    class Portalbox_20:
        body = u'ATLAS.svg'
        id = 20
        title = u'image'

    class Portalbox_21:
        body = u'This collection includes learning resources that use ATLAS public data#$#$#. The items in this collection are suitable for education purposes.'
        id = 21
        title = u'description'

    class Portalbox_22:
        body = u'This collection includes tools with which the ATLAS open data can be accessed and used#$#$#.'
        id = 22
        title = u'description'

    class Portalbox_23:
        body = u'According to the ATLAS Data Access Policy, reconstructed data and accompanying tools will be released after reasonable embargo periods.'
        id = 23
        title = u'research_description'

    class Portalbox_24:
        body = u'This collection includes ATLAS masterclass datasets.'
        id = 24
        title = u'description'

    class Portalbox_25:
        body = u'The LHCb (Large Hadron Collider beauty) experiment aims to record the decay of particles containing b and anti-b quarks,  known as B mesons. The detector is designed to gather information about the identity, trajectory, momentum and energy of each particle.'
        id = 25
        title = u'description'

    class Portalbox_26:
        body = u'LHCb.gif'
        id = 26
        title = u'image'

    class Portalbox_27:
        body = u'This collection contains LHCb simplified data events to be used for the masterclass exercises.'
        id = 27
        title = u'description'

    class Portalbox_28:
        body = u'This collection contains tools to access and analyse LHCb data.'
        id = 28
        title = u'description'

    class Portalbox_29:
        body = u'This collection contains links to public websites about LHCb experiment and LHCb data.'
        id = 29
        title = u'description'

    class Portalbox_30:
        body = u'This collection contains ALICE learning resources.'
        id = 30
        title = u'description'

    class Portalbox_31:
        body = u'This collection contains CMS open data instructions.'
        id = 31
        title = u'description'

    class Portalbox_32:
        body = u'The CMS (Compact Muon Solenoid) experiment is one of two large general-purpose detectors built on the Large Hadron Collider (LHC). Its goal is to investigate a wide range of physics such as the characteristics of the Higgs boson, extra dimensions or dark matter.'
        id = 32
        title = u'short_description_e'

    class Portalbox_33:
        body = u'<a href="http://aliceinfo.cern.ch/Public/Welcome.html">ALICE</a> (A Large Ion Collider Experiment) is a heavy-ion <a href="http://home.web.cern.ch/about/how-detector-works">detector</a> designed to study the physics of strongly interacting matter at extreme energy densities, where a phase of matter called <a href="http://home.web.cern.ch/about/physics/heavy-ions-and-quark-gluon-plasma">quark-gluon plasma</a> forms. More than 1000 scientists are part of the collaboration.'
        id = 33
        title = u'short_description_e'

    class Portalbox_34:
        body = u'The ATLAS (A Toroidal LHC ApparatuS) experiment is a general-purpose detector exploring topics like the properties of the Higgs-like particle, extra dimensions of space, unification of fundamental forces and evidence for dark matter candidates in the Universe.'
        id = 34
        title = u'short_description_e'

    class Portalbox_35:
        body = u'The LHCb (Large Hadron Collider beauty) experiment aims to record the decay of particles containing b and anti-b quarks,  known as B mesons. The detector is designed to gather information about the identity, trajectory, momentum and energy of each particle.'
        id = 35
        title = u'short_description_e'

    class Portalbox_36:
        body = u'To analyse CMS data, a Virtual Machine with the CMS analysis environment is provided. The data can be accessed directly through the VM. In the primary datasets, no selection nor identification criteria have been applied. The 2011 data release includes simulated Monte Carlo datasets, but no simulated datasets are provided for the 2010 release.'
        id = 36
        title = u'short_description_r'

    class Portalbox_37:
        body = u'According to the ALICE data preservation strategy, reconstructed data and Monte Carlo data as well as the analysis software and documentation needed to process them will be made available on a time scale of 5 years (for 10% of the data). Thus, the first release of ALICE research data will happen in 2018.'
        id = 37
        title = u'short_description_r'

    class Portalbox_38:
        body = u'According to the ATLAS Data Access Policy, reconstructed data and accompanying tools will be released after reasonable embargo periods.'
        id = 38
        title = u'short_description_r'

    class Portalbox_39:
        body = u'According to the LHCb External Data Access Policy, reconstructed data and accompanying tools will be released after reasonable embargo periods.'
        id = 39
        title = u'short_description_r'

    class Portalbox_40:
        body = u'According to the LHCb External Data Access Policy, reconstructed data will be made openly accessible 5 years after the data are taken. For the data that have already been taken, the 5 years are counted from the date of ratification of the experiment’s policy. Thus, the first release of LHCb data will happen in 2018.'
        id = 40
        title = u'research_description'

    class Portalbox_41:
        body = u'This collection contains author lists.'
        id = 41
        title = u'description'

    class Portalbox_42:
        body = u'This collection contains data policies.'
        id = 42
        title = u'description'

    class Portalbox_43:
        body = u'This collection contains ATLAS Higgs Machine Learning Challenge 2014.'
        id = 43
        title = u'description'

    class Portalbox_44:
        body = u'This collection contains CMS Simulated Datasets.'
        id = 44
        title = u'description'

    class Portalbox_45:
        body = u'This collection contains CMS Validation Utilities.'
        id = 45
        title = u'description'

    class Portalbox_46:
        body = u'This collection contains CMS Trigger Information.'
        id = 46
        title = u'description'

    class Portalbox_47:
        body = u'This collection contains CMS Condition Data.'
        id = 47
        title = u'description'

    class Portalbox_48:
        body = u'This collection contains the configuration files that were used in different steps of the data processing.'
        id = 48
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
        id_collection = CollectionData.ALICETools.ref('id')

    class CollectionPortalbox_6_10_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_10.ref('id')
        score = 100
        id_collection = CollectionData.ALICETools.ref('id')

    class CollectionPortalbox_7_11_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_11.ref('id')
        score = 100
        id_collection = CollectionData.ALICEDerivedDatasets.ref('id')

    class CollectionPortalbox_7_12_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_12.ref('id')
        score = 100
        id_collection = CollectionData.ALICEDerivedDatasets.ref('id')

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
        id_collection = CollectionData.CMSLearningResources.ref('id')

    class CollectionPortalbox_11_16_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_16.ref('id')
        score = 100
        id_collection = CollectionData.ALICEReconstructedData.ref('id')

    class CollectionPortalbox_2_17_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_17.ref('id')
        score = 100
        id_collection = CollectionData.CMS.ref('id')

    class CollectionPortalbox_5_18_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_18.ref('id')
        score = 100
        id_collection = CollectionData.ALICE.ref('id')

    class CollectionPortalbox_12_19_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_19.ref('id')
        score = 100
        id_collection = CollectionData.ATLAS.ref('id')

    class CollectionPortalbox_12_20_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_20.ref('id')
        score = 100
        id_collection = CollectionData.ATLAS.ref('id')

    class CollectionPortalbox_14_21_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_21.ref('id')
        score = 100
        id_collection = CollectionData.ATLASLearningResources.ref('id')

    class CollectionPortalbox_15_22_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_22.ref('id')
        score = 100
        id_collection = CollectionData.ATLASTools.ref('id')

    class CollectionPortalbox_12_23_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_23.ref('id')
        score = 100
        id_collection = CollectionData.ATLAS.ref('id')

    class CollectionPortalbox_13_24_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_24.ref('id')
        score = 100
        id_collection = CollectionData.ATLASDerivedDatasets.ref('id')

    class CollectionPortalbox_16_25_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_25.ref('id')
        score = 100
        id_collection = CollectionData.LHCb.ref('id')

    class CollectionPortalbox_16_26_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_26.ref('id')
        score = 100
        id_collection = CollectionData.LHCb.ref('id')

    class CollectionPortalbox_17_27_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_27.ref('id')
        score = 100
        id_collection = CollectionData.LHCbDerivedDatasets.ref('id')

    class CollectionPortalbox_18_28_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_28.ref('id')
        score = 100
        id_collection = CollectionData.LHCbTools.ref('id')

    class CollectionPortalbox_19_29_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_29.ref('id')
        score = 100
        id_collection = CollectionData.LHCbLearningResources.ref('id')

    class CollectionPortalbox_20_30_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_30.ref('id')
        score = 100
        id_collection = CollectionData.ALICELearningResources.ref('id')

    class CollectionPortalbox_21_31_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_31.ref('id')
        score = 100
        id_collection = CollectionData.CMSOpenDataInstructions.ref('id')

    class CollectionPortalbox_2_32_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_32.ref('id')
        score = 100
        id_collection = CollectionData.CMS.ref('id')

    class CollectionPortalbox_5_33_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_33.ref('id')
        score = 100
        id_collection = CollectionData.ALICE.ref('id')

    class CollectionPortalbox_12_34_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_34.ref('id')
        score = 100
        id_collection = CollectionData.ATLAS.ref('id')

    class CollectionPortalbox_16_35_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_35.ref('id')
        score = 100
        id_collection = CollectionData.LHCb.ref('id')

    class CollectionPortalbox_2_36_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_36.ref('id')
        score = 100
        id_collection = CollectionData.CMS.ref('id')

    class CollectionPortalbox_5_37_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_37.ref('id')
        score = 100
        id_collection = CollectionData.ALICE.ref('id')

    class CollectionPortalbox_12_38_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_38.ref('id')
        score = 100
        id_collection = CollectionData.ATLAS.ref('id')

    class CollectionPortalbox_16_39_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_39.ref('id')
        score = 100
        id_collection = CollectionData.LHCb.ref('id')

    class CollectionPortalbox_16_40_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_40.ref('id')
        score = 100
        id_collection = CollectionData.LHCb.ref('id')

    class CollectionPortalbox_22_41_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_41.ref('id')
        score = 100
        id_collection = CollectionData.AuthorLists.ref('id')

    class CollectionPortalbox_23_42_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_42.ref('id')
        score = 100
        id_collection = CollectionData.DataPolicies.ref('id')

    class CollectionPortalbox_24_43_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_43.ref('id')
        score = 100
        id_collection = CollectionData.ATLASHiggsChallenge2014.ref('id')

    class CollectionPortalbox_25_44_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_44.ref('id')
        score = 100
        id_collection = CollectionData.CMSSimulatedDatasets.ref('id')

    class CollectionPortalbox_26_45_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_45.ref('id')
        score = 100
        id_collection = CollectionData.CMSValidationUtilities.ref('id')

    class CollectionPortalbox_27_46_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_46.ref('id')
        score = 100
        id_collection = CollectionData.CMSTriggerInformation.ref('id')

    class CollectionPortalbox_28_47_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_47.ref('id')
        score = 100
        id_collection = CollectionData.CMSConditionData.ref('id')

    class CollectionPortalbox_29_48_en:
        ln = u'en'
        position = u'r'
        id_portalbox = PortalboxData.Portalbox_48.ref('id')
        score = 100
        id_collection = CollectionData.CMSConfigurationFiles.ref('id')


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
