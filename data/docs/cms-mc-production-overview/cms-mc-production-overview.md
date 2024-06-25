This guide gives a brief overview of the main steps in the production chain of simulated data. Its primary objective is to explain how to find the parameters used in event generation for datasets that are available as public data. These parameters are displayed in the simulated-dataset records whenever possible, but in some cases they are hidden in different configuration files, or only available with a command-line script reading them from a data file directly. If you are interested in producing new simulated data, read [the guide for event production](/docs/cms-guide-event-production).

The CMS data files have gone through several processing steps before they are in a format that is good for analysis. The following diagram shows an overview of these steps. The arrows describe the direction of the flow of information.

<p align="center">
<img alt="CMS data-flow overview" src="/static/docs/cms-mc-production-overview/diagram.png" width=75%>
</p>

The data records on this portal keep track of this information, and provide the job-configuration files used in the processing as well as the CMSSW version and the Global Tag for condition data. This information describes the exact setup for the CMS software executable that was used in the data-processing steps and it is provided only for information purposes. Although all the components required to analyse the public primary datasets – such as corresponding input data, condition data, software version – are provided on this portal, it is not necessarily possible to reproduce all the described data-processing steps.

The *GEN* (Generation) step uses one of the available event generators to simulate beam collisions.

The next step is to simulate the effect of the detectors and electronics. The *L1 triggers*, *HLT* and pile-up are also simulated. The output of this stage is similar to the output of the experiment.

The *RECO* step uses simulated or real data for the reconstruction the events in the collisions. The reconstructed data is then used in the analysis.

## Finding the generator parameters

Generator-level datasets are produced in two ways:

* using a *general-purpose generator* to simulate the event and the hadronisation. Examples are: [Pythia](http://home.thep.lu.se/~torbjorn/Pythia.html), [Herwig](http://herwig.hepforge.org/), [Tauola](https://tauolapp.web.cern.ch/tauolapp/).

* using a *Matrix Element (ME) generator* to deliver the event at the parton level and then a general-purpose generator to hadronise the event. Examples are: [Powheg](http://powhegbox.mib.infn.it/), [MadGraph5_aMCatNLO](http://amcatnlo.web.cern.ch/amcatnlo/), [Alpgen](http://mlm.home.cern.ch/mlm/alpgen/).

In addition, it is also possible to use a *particle-gun simulator*, or a specific generator for diffractive physics, cosmic-muon generators, heavy ions&hellip;

To extract the generator parameters, look for the initialisation of the `cms.EDFilter` in the python config file for the *SIM* step. Some examples of how to obtain these data are presented below.

### For general-purpose generators

- Example dataset: [QCD_Pt-15to30_TuneZ2_7TeV_pythia6](../record/1366)

Under the section *How were these data generated?*, download the Python configuration file for the step *SIM*.

This dataset used [Pythia6](http://home.thep.lu.se/~torbjorn/Pythia.html) as generator. All the parameters are defined in the `PythiaParameters` [PSet](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideAboutPythonConfigFile?rev=85#Parameter_Set_PSet_Objects). Lines 67–102 of the python configuration script:

```python
process.generator = cms.EDFilter("Pythia6GeneratorFilter",
     pythiaPylistVerbosity = cms.untracked.int32(0),
     filterEfficiency = cms.untracked.double(1),
     pythiaHepMCVerbosity = cms.untracked.bool(False),
     comEnergy = cms.double(7000.0),
     crossSection = cms.untracked.double(815912800.0),
     maxEventsToPrint = cms.untracked.int32(0),
     PythiaParameters = cms.PSet(
         pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution',
             'MSTJ(22)=2     ! Decay those unstable particles',
             'PARJ(71)=10 .  ! for which ctau  10 mm',
             'MSTP(33)=0     ! no K factors in hard cross sections',
             'MSTP(2)=1      ! which order running alphaS',
             'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
             'MSTP(52)=2     ! work with LHAPDF',
             'PARP(82)=1.832 ! pt cutoff for multiparton interactions',
             'PARP(89)=1800\. ! sqrts for which PARP82 is set',
             'PARP(90)=0.275 ! Multiple interactions: rescaling power',
             'MSTP(95)=6     ! CR (color reconnection parameters)',
             'PARP(77)=1.016 ! CR',
             'PARP(78)=0.538 ! CR',
             'PARP(80)=0.1   ! Prob. colored parton from BBR',
             'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter',
             'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter',
             'PARP(62)=1.025 ! ISR cutoff',
             'MSTP(91)=1     ! Gaussian primordial kT',
             'PARP(93)=10.0  ! primordial kT-max',
             'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default',
             'MSTP(82)=4     ! Defines the multi-parton model'),
         processParameters = cms.vstring('MSEL = 1        ! QCD hight pT processes',
             'CKIN(3) = 15    ! minimum pt hat for hard interactions',
             'CKIN(4) = 30    ! maximum pt hat for hard interactions'),
         parameterSets = cms.vstring('pythiaUESettings',
             'processParameters')
     )
 )
```

### For ME generators

- Example dataset: [VBFHiggs0MToZZTo4L_M-125p6_7TeV-JHUGenV4](../record/1352)

Lines 30–34 of the configuration file define the input of the generator as a [`PoolSource`](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGeneration#FwkSources):

```python
# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('/store/generator/Summer11LegpLHE/GluGluTo2e2mu_SMH_M-125p6_7TeV-MCFM67-pythia6/GEN/START53_LV4-v1/00000/EEA88C0D-4E63-E411-A160-02163E0100B6.root')
)
```

That means this dataset had the parton-level events generated with an external tool. The next step is to generate fully hadronised events, for example using Pythia.
Lines 70–115 defines an `cms.EDFilter` named `Pythia6HadronizerFilter` for this purpose:

```python
process.generator = cms.EDFilter("Pythia6HadronizerFilter",
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            UseTauolaPolarization = cms.bool(True),
            InputCards = cms.PSet(
                mdtau = cms.int32(0),
                pjak2 = cms.int32(0),
                pjak1 = cms.int32(0)
            )
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    comEnergy = cms.double(7000.0),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTU(21)=1     ! Check on possible errors during program execution',
            'MSTJ(22)=2     ! Decay those unstable particles',
            'PARJ(71)=10 .  ! for which ctau  10 mm',
            'MSTP(33)=0     ! no K factors in hard cross sections',
            'MSTP(2)=1      ! which order running alphaS',
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
            'MSTP(52)=2     ! work with LHAPDF',
            'PARP(82)=1.832 ! pt cutoff for multiparton interactions',
            'PARP(89)=1800. ! sqrts for which PARP82 is set',
            'PARP(90)=0.275 ! Multiple interactions: rescaling power',
            'MSTP(95)=6     ! CR (color reconnection parameters)',
            'PARP(77)=1.016 ! CR',
            'PARP(78)=0.538 ! CR',
            'PARP(80)=0.1   ! Prob. colored parton from BBR',
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter',
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter',
            'PARP(62)=1.025 ! ISR cutoff',
            'MSTP(91)=1     ! Gaussian primordial kT',
            'PARP(93)=10.0  ! primordial kT-max',
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default',
            'MSTP(82)=4     ! Defines the multi-parton model'),
        processParameters = cms.vstring('MSEL=0          ! User defined processes',
            'PMAS(5,1)=4.8   ! b quark mass',
            'PMAS(6,1)=172.5 ! t quark mass'),
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters')
    )
)
```

To extract the LHE information, which contains details about the generator used, download the file index (that contains the path to the root files), select one item of the list and run the `dumpLHEHeader.py` script available in the [CMS working environment](/docs/cms-getting-started-2011) on the [CMS Open Data VM](/docs/cms-virtual-machine-2011):

```sh
cmsrel CMSSW_5_3_32
cd CMSSW_5_3_32/src
cmsenv
dumpLHEHeader.py input=file:root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2011/Summer11LegDR/VBFHiggs0MToZZTo4L_M-125p6_7TeV-JHUGenV4/AODSIM/PU_S13_START53_LV6-v1/00000/08628529-8292-E411-91E1-002618943972.root output=1352_2.lhe
```

The outputfile `1352_2.root` contains information about the generator used and its input parameters. In this case, it used [JHUGenerator](http://spin.pha.jhu.edu/):

```
<LesHouchesEvents version="1.0">
<header>
<!--
Output from the JHUGenerator v4.3.1 described in arXiv:1001.3396 [hep-ph],arXiv:1208.4018 [hep-ph],arXiv:1309.4819 [hep-ph]


   Command line: ./JHUGen Collider=1 PChannel=0 Process=0 Unweighted=1 ReadLHE=/afs/cern.ch/user/h/hroskes/work/public/HiggsPropertiesMC/JHUGen/H/VBFHiggs0M_M-125p6_7TeV-JHUGenV4/VBFHiggs0M_M-125p6_7TeV-JHUGenV4_0.lhe DecayMode1=0 DecayMode2=0 OffXVV=011 DataFile=VBFHiggs0MToZZTo4L_M-125p6_7TeV-JHUGenV4/VBFHiggs0MToZZTo4L_M-125p6_7TeV-JHUGenV4_0

   Input Parameter:
    Collider: P-P, sqrt(s)= 7000.00
    Resonance: spin=0, mass= 125.60 width= 0.004
               (This is ReadLHEFile mode. Resonance mass is read from LHE input file.)
    DecayMode1: 0  DecayMode2: 0
    Z-boson: mass=91.188, width=2.4952
    Interference: T

    spin-0-VV couplings:
      generate_as=F
      ghg2= 0.10000000E+01 0.00000000E+00i
      ghg3= 0.00000000E+00 0.00000000E+00i
      ghg4= 0.00000000E+00 0.00000000E+00i
      ghz1= 0.00000000E+00 0.00000000E+00i
      ghz2= 0.00000000E+00 0.00000000E+00i
      ghz3= 0.00000000E+00 0.00000000E+00i
      ghz4= 0.10000000E+01 0.00000000E+00i
      ghz1_prime= 0.00000000E+00 0.00000000E+00i,    Lambda_z1=  1.0000E+04
      ghz2_prime= 0.00000000E+00 0.00000000E+00i,    Lambda_z2=  1.0000E+04
      ghz3_prime= 0.00000000E+00 0.00000000E+00i,    Lambda_z3=  1.0000E+04
      ghz4_prime= 0.00000000E+00 0.00000000E+00i,    Lambda_z4=  1.0000E+04
      Lambda=  1000.0

    LHE output: VBFHiggs0MToZZTo4L_M-125p6_7TeV-JHUGenV4/VBFHiggs0MToZZTo4L_M-125p6_7TeV-JHUGenV4_0.lhe
    Histogram output: VBFHiggs0MToZZTo4L_M-125p6_7TeV-JHUGenV4/VBFHiggs0MToZZTo4L_M-125p6_7TeV-JHUGenV4_0.dat
    Log file: VBFHiggs0MToZZTo4L_M-125p6_7TeV-JHUGenV4/VBFHiggs0MToZZTo4L_M-125p6_7TeV-JHUGenV4_0.log
    LHE input: /afs/cern.ch/user/h/hroskes/work/public/HiggsPropertiesMC/JHUGen/H/VBFHiggs0M_M-125p6_7TeV-JHUGenV4/VBFHiggs0M_M-125p6_7TeV-JHUGenV4_0.lhe


Output from the JHUGenerator v4.3.2 described in arXiv:1001.3396 [hep-ph],arXiv:1208.4018 [hep-ph],arXiv:1309.4819 [hep-ph]


   Command line: ./JHUGen Collider=1 Process=60 Unweighted=1 ReadCSmax=1 VegasNc2=2000 OffXVV=011 DataFile=7TeV0minus250

   Input Parameter:
    Collider: P-P, sqrt(s)= 7000.00
    Resonance: spin=0, mass= 125.60 width= 0.004
    DecayMode1: 0  DecayMode2: 0
    Z-boson: mass=91.188, width=2.4952

    OffXVV: FTT
    PChannel: 2
    PDFSet: 1
    Unweighted: T
    Interference: T

    spin-0-VV couplings:
      generate_as=F
      ghg2=  0.10000000E+01  0.00000000E+00i
      ghg3=  0.00000000E+00  0.00000000E+00i
      ghg4=  0.00000000E+00  0.00000000E+00i
      ghz1=  0.00000000E+00  0.00000000E+00i
      ghz2=  0.00000000E+00  0.00000000E+00i
      ghz3=  0.00000000E+00  0.00000000E+00i
      ghz4=  0.10000000E+01  0.00000000E+00i
      Lambda=  1000.0

    LHE output: 7TeV0minus250.lhe
    Histogram output: 7TeV0minus250.dat
    Log file: 7TeV0minus250.log

-->
</header>
<init>
    2212  2212  3.5000000E+03  3.5000000E+03  0  0  10042  10042  3  1
    4.3538821E-03	7.2559368E-06	1.0000000E+00	100
</init>
</LesHouchesEvents>
```


### From a `GenFragment`

`GenFragment` is a code snippet that contains only the specific generator parameters for that process.

- Example dataset: [/BBH_HToTauTau_M_125_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM](../record/7299)

The `genFragment` is:

```python
import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
from GeneratorInterface.ExternalDecays.TauolaSettings_cff import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    # put here the efficiency of your filter (1. if no filter)
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    # put here the cross section of your process (in pb)
    crossSection = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    comEnergy = cms.double(8000.0),
    ExternalDecays = cms.PSet(
        Tauola = cms.untracked.PSet(
            TauolaPolar,
            TauolaDefaultInputCards
        ),
        parameterSets = cms.vstring('Tauola')
    ),
    UseExternalGenerators = cms.untracked.bool(True),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring('PMAS(25,1)=125.0        !mass of Higgs',
            'MSEL=0                  ! user selection for process',
            'MSUB(102)=0             !ggH',
            'MSUB(123)=0             !ZZ fusion to H',
            'MSUB(124)=0             !WW fusion to H',
            'MSUB(24)=0              !ZH production',
            'MSUB(26)=0              !WH production',
            'MSUB(121)= 1   ! gg->QQbarH (SM)',
            'KFPR(121,2)= 5 ! Q = b',
            'MSUB(122)= 1   ! qq->QQbarH (SM)',
            'KFPR(122,2)= 5 ! Q = b',
            'MDME(210,1)=0           !Higgs decay into dd',
            'MDME(211,1)=0           !Higgs decay into uu',
            'MDME(212,1)=0           !Higgs decay into ss',
            'MDME(213,1)=0           !Higgs decay into cc',
            'MDME(214,1)=0           !Higgs decay into bb',
            'MDME(215,1)=0           !Higgs decay into tt',
            'MDME(216,1)=0           !Higgs decay into',
            'MDME(217,1)=0           !Higgs decay into Higgs decay',
            'MDME(218,1)=0           !Higgs decay into e nu e',
            'MDME(219,1)=0           !Higgs decay into mu nu mu',
            'MDME(220,1)=1           !Higgs decay into tau nu tau',
            'MDME(221,1)=0           !Higgs decay into Higgs decay',
            'MDME(222,1)=0           !Higgs decay into g g',
            'MDME(223,1)=0           !Higgs decay into gam gam',
            'MDME(224,1)=0           !Higgs decay into gam Z',
            'MDME(225,1)=0           !Higgs decay into Z Z',
            'MDME(226,1)=0           !Higgs decay into W W'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters')
    )
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/EightTeV/TTH_HToBB_M_125_TuneZ2star_8TeV_pythia6_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA6 bbH, H->tautau mH=125GeV with TAUOLA at 8TeV')
)
```

Apart from the process-specific parameters, there are some general Pythia and Tauola parameters. Those parameters are not in the `genFragment`, but they can be found in `CMSSW` source code. In this example, the first two lines of the `genFragment` indicate where they can be found. As this dataset was generated with `CMSSW_5_3_X`, the links to these parameters are:

- [TauolaPolar, TauolaDefaultInputCards](https://github.com/cms-sw/cmssw/blob/CMSSW_5_3_X/GeneratorInterface/ExternalDecays/python/TauolaSettings_cff.py)
- [pythiaUESettings](https://github.com/cms-sw/cmssw/blob/CMSSW_5_3_X/Configuration/Generator/python/PythiaUEZ2starSettings_cfi.py)


### For any dataset

`CMSSW` also provides the `edmProvDump` utility, which prints out all the tracked parameters. The output is lengthy and it is recommended to redirect the output to a file:

```sh
cmsrel CMSSW_5_3_32
cd CMSSW_5_3_32/src
cmsenv
edmProvDump root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2012/Summer12_DR53X/DiPhotonBox_Pt-10To25_8TeV-pythia6/AODSIM/PU_RD1_START53_V7N-v1/20000/78CFFDF5-29CF-E211-B7C7-1CC1DE056008.root > edmProvDump.out
```

Search for the blocks starting with `Module: generator SIM`. The generator parameters are inside these blocks:

```
[...]
Module: generator SIM
 PSet id:b0b73c73e8f1cee3fbb45c93be379cac
 products: {
  GenEventInfoProduct_generator__SIM.
  GenRunInfoProduct_generator__SIM.
  edmHepMCProduct_generator__SIM.
 }
 parameters: {
  @module_edm_type: string tracked  = 'EDFilter'
  @module_label: string tracked  = 'generator'
  @module_type: string tracked  = 'Pythia6GeneratorFilter'
  comEnergy: double tracked  = 8000
  PythiaParameters: PSet tracked = ({
   parameterSets: vstring tracked  = {'pythiaUESettings','processParameters'}
   processParameters: vstring tracked  = {'MSEL=0 ','MSUB(114)=1       ','CKIN(3)=10.          ! minimum pt hat for hard interactions','CKIN(4)=25.          ! maximum pt hat for hard interactions'}
   pythiaUESettings: vstring tracked  = {'MSTU(21)=1     ! Check on possible errors during program execution','MSTJ(22)=2     ! Decay those unstable particles','PARJ(71)=10 .  ! for which ctau  10 mm','MSTP(33)=0     ! no K factors in hard cross sections','MSTP(2)=1      ! which order running alphaS','MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)','MSTP(52)=2     ! work with LHAPDF','PARP(82)=1.921 ! pt cutoff for multiparton interactions','PARP(89)=1800. ! sqrts for which PARP82 is set','PARP(90)=0.227 ! Multiple interactions: rescaling power','MSTP(95)=6     ! CR (color reconnection parameters)','PARP(77)=1.016 ! CR','PARP(78)=0.538 ! CR','PARP(80)=0.1   ! Prob. colored parton from BBR','PARP(83)=0.356 ! Multiple interactions: matter distribution parameter','PARP(84)=0.651 ! Multiple interactions: matter distribution parameter','PARP(62)=1.025 ! ISR cutoff','MSTP(91)=1     ! Gaussian primordial kT','PARP(93)=10.0  ! primordial kT-max','MSTP(81)=21    ! multiple parton interactions 1 is Pythia default','MSTP(82)=4     ! Defines the multi-parton model'}
  })
 }

Module: generator SIM
 PSet id:b0b73c73e8f1cee3fbb45c93be379cac
 products: {
  GenEventInfoProduct_generator__SIM.
  GenRunInfoProduct_generator__SIM.
  edmHepMCProduct_generator__SIM.
 }
 parameters: {
  @module_edm_type: string tracked  = 'EDFilter'
  @module_label: string tracked  = 'generator'
  @module_type: string tracked  = 'Pythia6GeneratorFilter'
  comEnergy: double tracked  = 8000
  PythiaParameters: PSet tracked = ({
   parameterSets: vstring tracked  = {'pythiaUESettings','processParameters'}
   processParameters: vstring tracked  = {'MSEL=0 ','MSUB(114)=1       ','CKIN(3)=10.          ! minimum pt hat for hard interactions','CKIN(4)=25.          ! maximum pt hat for hard interactions'}
   pythiaUESettings: vstring tracked  = {'MSTU(21)=1     ! Check on possible errors during program execution','MSTJ(22)=2     ! Decay those unstable particles','PARJ(71)=10 .  ! for which ctau  10 mm','MSTP(33)=0     ! no K factors in hard cross sections','MSTP(2)=1      ! which order running alphaS','MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)','MSTP(52)=2     ! work with LHAPDF','PARP(82)=1.921 ! pt cutoff for multiparton interactions','PARP(89)=1800. ! sqrts for which PARP82 is set','PARP(90)=0.227 ! Multiple interactions: rescaling power','MSTP(95)=6     ! CR (color reconnection parameters)','PARP(77)=1.016 ! CR','PARP(78)=0.538 ! CR','PARP(80)=0.1   ! Prob. colored parton from BBR','PARP(83)=0.356 ! Multiple interactions: matter distribution parameter','PARP(84)=0.651 ! Multiple interactions: matter distribution parameter','PARP(62)=1.025 ! ISR cutoff','MSTP(91)=1     ! Gaussian primordial kT','PARP(93)=10.0  ! primordial kT-max','MSTP(81)=21    ! multiple parton interactions 1 is Pythia default','MSTP(82)=4     ! Defines the multi-parton model'}
  })
 }
 PSet id:f06dfae5c9dbba5c1b076ed33fd13ce6
 products: {
  GenEventInfoProduct_generator__SIM.
  GenRunInfoProduct_generator__SIM.
  edmHepMCProduct_generator__SIM.
 }
 parameters: {
  @module_edm_type: string tracked  = 'EDFilter'
  @module_label: string tracked  = 'generator'
  @module_type: string tracked  = 'Pythia6GeneratorFilter'
  comEnergy: double tracked  = 8000
  PythiaParameters: PSet tracked = ({
   parameterSets: vstring tracked  = {'pythiaUESettings','processParameters'}
   processParameters: vstring tracked  = {'MSEL=0         ! User defined processes','MSUB(11)=1     ! Min bias process','MSUB(12)=1     ! Min bias process','MSUB(13)=1     ! Min bias process','MSUB(28)=1     ! Min bias process','MSUB(53)=1     ! Min bias process','MSUB(68)=1     ! Min bias process','MSUB(92)=1     ! Min bias process, single diffractive','MSUB(93)=1     ! Min bias process, single diffractive','MSUB(94)=1     ! Min bias process, double diffractive','MSUB(95)=1     ! Min bias process'}
   pythiaUESettings: vstring tracked  = {'MSTU(21)=1     ! Check on possible errors during program execution','MSTJ(22)=2     ! Decay those unstable particles','PARJ(71)=10 .  ! for which ctau  10 mm','MSTP(33)=0     ! no K factors in hard cross sections','MSTP(2)=1      ! which order running alphaS','MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)','MSTP(52)=2     ! work with LHAPDF','PARP(82)=1.921 ! pt cutoff for multiparton interactions','PARP(89)=1800. ! sqrts for which PARP82 is set','PARP(90)=0.227 ! Multiple interactions: rescaling power','MSTP(95)=6     ! CR (color reconnection parameters)','PARP(77)=1.016 ! CR','PARP(78)=0.538 ! CR','PARP(80)=0.1   ! Prob. colored parton from BBR','PARP(83)=0.356 ! Multiple interactions: matter distribution parameter','PARP(84)=0.651 ! Multiple interactions: matter distribution parameter','PARP(62)=1.025 ! ISR cutoff','MSTP(91)=1     ! Gaussian primordial kT','PARP(93)=10.0  ! primordial kT-max','MSTP(81)=21    ! multiple parton interactions 1 is Pythia default','MSTP(82)=4     ! Defines the multi-parton model'}
  })
 }
[...]
```

It is also possible to get only the information about the modules with contain the string `generator SIM`:

```sh
edmProvDump -f "generator SIM" root://eospublic.cern.ch//eos/opendata/cms/MonteCarlo2012/Summer12_DR53X/DiPhotonBox_Pt-10To25_8TeV-pythia6/AODSIM/PU_RD1_START53_V7N-v1/20000/78CFFDF5-29CF-E211-B7C7-1CC1DE056008.root > edmProvDump.out
```

More information can be found in the `--help` command of `edmProvDump`.

---

Read more in the [Introduction to Generation and Simulation](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookGenIntro)
and
[CMS Computing Model](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookComputingModel).
