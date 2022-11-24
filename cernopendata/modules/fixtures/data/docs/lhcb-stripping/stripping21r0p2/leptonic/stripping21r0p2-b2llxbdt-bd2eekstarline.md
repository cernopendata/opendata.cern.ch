[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2LLXBDT_Bd2eeKstarLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2LLXBDT_Bd2eeKstarLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdDiElectronFromTracks**

|      |                                             |
|------|---------------------------------------------|
| Code | 0 StdDiElectronFromTracks /Particles',True) |

**FilterDesktop/B2LLXBDTSelDiElectron**

|                 |                                                                                                                                                                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<5.0\*GeV) & (INTREE( (ID=='e+') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (PIDe\>-2) & (TRGHOSTPROB\<0.5) )) & (INTREE( (ID=='e-') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (PIDe\>-2) & (TRGHOSTPROB\<0.5) )) |
| Inputs          | [ 'Phys/ [StdDiElectronFromTracks](./stripping21r0p2-stddielectronfromtracks) ' ]                                                                                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                                                                                                             |
| Output          | Phys/B2LLXBDTSelDiElectron/Particles                                                                                                                                                                                                                             |

**LoKi::VoidFilter/SELECT:Phys/StdVeryLooseDetachedKst2Kpi**

|      |                                                 |
|------|-------------------------------------------------|
| Code | 0 StdVeryLooseDetachedKst2Kpi /Particles',True) |

**FilterDesktop/B2LLXBDTSelKstar**

|                 |                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF)\<16) & (ADMASS('K\*(892)0')\< 300\*MeV)                                 |
| Inputs          | [ 'Phys/ [StdVeryLooseDetachedKst2Kpi](./stripping21r0p2-stdveryloosedetachedkst2kpi) ' ] |
| DecayDescriptor | None                                                                                        |
| Output          | Phys/B2LLXBDTSelKstar/Particles                                                             |

**CombineParticles/B2LLXBDTSelBd2eeKstar**

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelDiElectron' , 'Phys/B2LLXBDTSelKstar' ]                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' }                                     |
| CombinationCut   | (in_range(3.7\*GeV, AM, 6.8\*GeV))                                                                                     |
| MotherCut        | (in_range(4.0\*GeV, M, 6.5\*GeV)) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.999) & (BPVDLS\>0) & (BPVIPCHI2()\<400) |
| DecayDescriptor  | [B0 -\> J/psi(1S) K\*(892)0]cc                                                                                       |
| DecayDescriptors | [ '[B0 -\> J/psi(1S) K\*(892)0]cc' ]                                                                               |
| Output           | Phys/B2LLXBDTSelBd2eeKstar/Particles                                                                                   |

**FilterDesktop/B2LLXBDT_Bd2eeKstarLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2LLXBDTMvaBd2eeKstar')\>0. |
| Inputs          | [ 'Phys/B2LLXBDTSelBd2eeKstar' ]                         |
| DecayDescriptor | None                                                       |
| Output          | Phys/B2LLXBDT_Bd2eeKstarLine/Particles                     |

****Tools:****

**B2LLXBDTMvaBd2eeKstar**

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Factory :                | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Source :                 | LoKi::Hybrid::DictOfFunctors/MVAdict                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Preambulo :              | [ ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ErrorsPrint :            | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| StatEntityList :         | [ ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| RootInTES :              | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| AuditFinalize :          | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Key :                    | BDT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TypePrint :              | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| UseEfficiencyRowFormat : | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ContextService :         | AlgContextSvc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| AuditTools :             | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MonitorService :         | MonitorSvc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| AuditInitialize :        | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| OutputLevel :            | 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| StatPrint :              | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| AuditStop :              | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Context :                | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PropertiesPrint :        | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Options :                | { 'KeepVars' : '0' , 'Name' : 'BDT' , 'XMLFile' : '/cvmfs/lhcb.cern.ch/lib/lhcb/PARAM/TMVAWeights/v1r15/data/Bd2eeKstar_BDT_v1r0.xml' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Variables :              | { 'B_DIRA_OWNPV' : 'BPVDIRA' , 'log(B_PT)' : 'log(PT)' , 'log(H1_PT)' : 'log(CHILD(PT, 2, 1))' , 'log(H2_PT)' : 'log(CHILD(PT, 2, 2))' , 'log(Jpsi_PT)' : 'log(CHILD(PT, 1))' , 'log(L1_PT)' : 'log(CHILD(PT, 1, 1))' , 'log(L2_PT)' : 'log(CHILD(PT, 1, 2))' , 'log(X_PT)' : 'log(CHILD(PT, 2))' , 'sqrt(B_FDCHI2_OWNPV)' : 'sqrt(BPVVDCHI2)' , 'sqrt(B_IPCHI2_OWNPV)' : 'sqrt(BPVIPCHI2())' , 'sqrt(H1_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 2, 1))' , 'sqrt(H2_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 2, 2))' , 'sqrt(Jpsi_FDCHI2_OWNPV)' : 'sqrt(CHILD(BPVVDCHI2,1))' , 'sqrt(Jpsi_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 1 ))' , 'sqrt(L1_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 1, 1))' , 'sqrt(L2_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 1, 2))' , 'sqrt(X_FDCHI2_OWNPV)' : 'sqrt(CHILD(BPVVDCHI2,2))' , 'sqrt(X_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 2 ))' } |
| AuditStart :             | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CounterList :            | [ '.\*' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

**AddRelatedInfo/RelatedInfo1_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo1_B2LLXBDT_Bd2eeKstarLine/Particles |

**AddRelatedInfo/RelatedInfo2_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo2_B2LLXBDT_Bd2eeKstarLine/Particles |

**AddRelatedInfo/RelatedInfo3_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo3_B2LLXBDT_Bd2eeKstarLine/Particles |

**AddRelatedInfo/RelatedInfo4_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo4_B2LLXBDT_Bd2eeKstarLine/Particles |

**AddRelatedInfo/RelatedInfo5_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo5_B2LLXBDT_Bd2eeKstarLine/Particles |

**AddRelatedInfo/RelatedInfo6_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo6_B2LLXBDT_Bd2eeKstarLine/Particles |

**AddRelatedInfo/RelatedInfo7_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo7_B2LLXBDT_Bd2eeKstarLine/Particles |

**AddRelatedInfo/RelatedInfo8_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo8_B2LLXBDT_Bd2eeKstarLine/Particles |

**AddRelatedInfo/RelatedInfo9_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo9_B2LLXBDT_Bd2eeKstarLine/Particles |

**AddRelatedInfo/RelatedInfo10_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                 |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo10_B2LLXBDT_Bd2eeKstarLine/Particles |

**AddRelatedInfo/RelatedInfo11_B2LLXBDT_Bd2eeKstarLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKstarLine' ]                 |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo11_B2LLXBDT_Bd2eeKstarLine/Particles |
