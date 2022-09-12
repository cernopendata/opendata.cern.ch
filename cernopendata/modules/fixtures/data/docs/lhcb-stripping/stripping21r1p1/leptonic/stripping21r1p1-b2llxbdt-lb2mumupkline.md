[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2LLXBDT_Lb2mumuPKLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2LLXBDT_Lb2mumuPKLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

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

**LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles**

|      |                                                                                         |
|------|-----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseDiMuon](./stripping21r1p1-stdloosedimuon) /Particles',True)\>0 |

**FilterDesktop/B2LLXBDTSelDiMuon**

|                 |                                                                                                                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<5.0\*GeV) & (INTREE( (ID=='mu+') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (TRGHOSTPROB\<0.5) )) & (INTREE( (ID=='mu-') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (TRGHOSTPROB\<0.5) )) |
| Inputs          | [ 'Phys/ [StdLooseDiMuon](./stripping21r1p1-stdloosedimuon) ' ]                                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                                                     |
| Output          | Phys/B2LLXBDTSelDiMuon/Particles                                                                                                                                                                                                         |

**LoKi::VoidFilter/SelFilterPhys_StdLooseANNProtons_Particles**

|      |                                                                                                 |
|------|-------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseANNProtons](./stripping21r1p1-stdlooseannprotons) /Particles',True)\>0 |

**FilterDesktop/B2LLXBDTSelProtons**

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PROBNNp\> 0.05) & (PT\>300\*MeV) & (TRGHOSTPROB\<0.4)                    |
| Inputs          | [ 'Phys/ [StdLooseANNProtons](./stripping21r1p1-stdlooseannprotons) ' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/B2LLXBDTSelProtons/Particles                                         |

**LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles**

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseANNKaons](./stripping21r1p1-stdlooseannkaons) /Particles',True)\>0 |

**FilterDesktop/B2LLXBDTSelKaons**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT\>300\*MeV) & (TRGHOSTPROB\<0.4)                |
| Inputs          | [ 'Phys/ [StdLooseANNKaons](./stripping21r1p1-stdlooseannkaons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/B2LLXBDTSelKaons/Particles                                       |

**CombineParticles/B2LLXBDTSelLambdastar**

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelKaons' , 'Phys/B2LLXBDTSelProtons' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p\~-' : 'ALL' } |
| CombinationCut   | (AM \< 5.6\*GeV)                                                             |
| MotherCut        | (VFASPF(VCHI2) \< 25.)                                                       |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K-]cc                                                |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K-]cc' ]                                        |
| Output           | Phys/B2LLXBDTSelLambdastar/Particles                                         |

**CombineParticles/B2LLXBDTSelLb2mumuPK**

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelDiMuon' , 'Phys/B2LLXBDTSelLambdastar' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)\~0' : 'ALL' }                             |
| CombinationCut   | (in_range(3.7\*GeV, AM, 7.1\*GeV))                                                                                     |
| MotherCut        | (in_range(4.0\*GeV, M, 6.8\*GeV)) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.999) & (BPVDLS\>0) & (BPVIPCHI2()\<400) |
| DecayDescriptor  | [Lambda_b0 -\> J/psi(1S) Lambda(1520)0]cc                                                                            |
| DecayDescriptors | [ '[Lambda_b0 -\> J/psi(1S) Lambda(1520)0]cc' ]                                                                    |
| Output           | Phys/B2LLXBDTSelLb2mumuPK/Particles                                                                                    |

**FilterDesktop/B2LLXBDT_Lb2mumuPKLine**

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2LLXBDTMvaLb2mumuPK')\>-0.11 |
| Inputs          | [ 'Phys/B2LLXBDTSelLb2mumuPK' ]                            |
| DecayDescriptor | None                                                         |
| Output          | Phys/B2LLXBDT_Lb2mumuPKLine/Particles                        |

****Tools:****

**B2LLXBDTMvaLb2mumuPK**

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
| Options :                | { 'KeepVars' : '0' , 'Name' : 'BDT' , 'XMLFile' : '/afs/cern.ch/lhcb/software/releases/PARAM/TMVAWeights/v1r7/data/Lb2eePK_BDT_v1r0.xml' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Variables :              | { 'B_DIRA_OWNPV' : 'BPVDIRA' , 'log(B_PT)' : 'log(PT)' , 'log(H1_PT)' : 'log(CHILD(PT, 2, 1))' , 'log(H2_PT)' : 'log(CHILD(PT, 2, 2))' , 'log(Jpsi_PT)' : 'log(CHILD(PT, 1))' , 'log(L1_PT)' : 'log(CHILD(PT, 1, 1))' , 'log(L2_PT)' : 'log(CHILD(PT, 1, 2))' , 'log(X_PT)' : 'log(CHILD(PT, 2))' , 'sqrt(B_FDCHI2_OWNPV)' : 'sqrt(BPVVDCHI2)' , 'sqrt(B_IPCHI2_OWNPV)' : 'sqrt(BPVIPCHI2())' , 'sqrt(H1_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 2, 1))' , 'sqrt(H2_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 2, 2))' , 'sqrt(Jpsi_FDCHI2_OWNPV)' : 'sqrt(CHILD(BPVVDCHI2,1))' , 'sqrt(Jpsi_IPCHI2_OWNPV}' : 'sqrt(CHILD(MIPCHI2DV(), 1 ))' , 'sqrt(L1_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 1, 1))' , 'sqrt(L2_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 1, 2))' , 'sqrt(X_FDCHI2_OWNPV)' : 'sqrt(CHILD(BPVVDCHI2,2))' , 'sqrt(X_IPCHI2_OWNPV}' : 'sqrt(CHILD(MIPCHI2DV(), 2 ))' } |
| AuditStart :             | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CounterList :            | [ '.\*' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

**AddRelatedInfo/RelatedInfo1_B2LLXBDT_Lb2mumuPKLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2mumuPKLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_B2LLXBDT_Lb2mumuPKLine/Particles |

**AddRelatedInfo/RelatedInfo2_B2LLXBDT_Lb2mumuPKLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2mumuPKLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_B2LLXBDT_Lb2mumuPKLine/Particles |

**AddRelatedInfo/RelatedInfo3_B2LLXBDT_Lb2mumuPKLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2mumuPKLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_B2LLXBDT_Lb2mumuPKLine/Particles |

**AddRelatedInfo/RelatedInfo4_B2LLXBDT_Lb2mumuPKLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2mumuPKLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_B2LLXBDT_Lb2mumuPKLine/Particles |

**AddRelatedInfo/RelatedInfo5_B2LLXBDT_Lb2mumuPKLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2mumuPKLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo5_B2LLXBDT_Lb2mumuPKLine/Particles |

**AddRelatedInfo/RelatedInfo6_B2LLXBDT_Lb2mumuPKLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2mumuPKLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo6_B2LLXBDT_Lb2mumuPKLine/Particles |
