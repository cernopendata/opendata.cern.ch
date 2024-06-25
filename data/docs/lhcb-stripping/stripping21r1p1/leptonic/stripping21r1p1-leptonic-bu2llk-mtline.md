[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingBu2LLK_mtLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Bu2LLK_mtLine/Particles |
| Postscale      | 1.0000000                    |
| HLT1           | None                         |
| HLT2           | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

LoKi::VoidFilter/StrippingBu2LLK_mtLineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdTightDetachedTau3pi_Particles

|      |                                                                                                                       |
|------|-----------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightDetachedTau3pi](./stripping21r1p1-commonparticles-stdtightdetachedtau3pi)/Particles',True)\>0 |

CombineParticles/MuTauForBu2LLK

|                  |                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' , 'Phys/[StdTightDetachedTau3pi](./stripping21r1p1-commonparticles-stdtightdetachedtau3pi)' ]                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(PT \> 300) & (MIPCHI2DV(PRIMARY) \> 9)&(HASMUON)&(ISMUON)' , 'mu-' : '(PT \> 300) & (MIPCHI2DV(PRIMARY) \> 9)&(HASMUON)&(ISMUON)' , 'tau+' : '(PT \> 300) & (MIPCHI2DV(PRIMARY) \> 9)&(PT \> 0)' , 'tau-' : '(PT \> 300) & (MIPCHI2DV(PRIMARY) \> 9)&(PT \> 0)' } |
| CombinationCut   | (AM \> 100\*MeV)                                                                                                                                                                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 150)                                                                                                                                                                                                                                                                |
| DecayDescriptor  | [J/psi(1S) -\> mu+ tau-]cc                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[J/psi(1S) -\> mu+ tau-]cc' ]                                                                                                                                                                                                                                                       |
| Output           | Phys/MuTauForBu2LLK/Particles                                                                                                                                                                                                                                                              |

FilterDesktop/SelMuTauForBu2LLK

|                 |                                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ID=='J/psi(1S)') & (PT \> 0 \*MeV) & (MM \< 5500 \*MeV) & (MINTREE(ABSID\<14,PT) \> 300 \*MeV) & (MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY)) \> 9) & (VFASPF(VCHI2/VDOF) \< 150) & (BPVVDCHI2 \> 16) & (MIPCHI2DV(PRIMARY) \> 0) |
| Inputs          | [ 'Phys/MuTauForBu2LLK' ]                                                                                                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                                                         |
| Output          | Phys/SelMuTauForBu2LLK/Particles                                                                                                                                                                                             |

GaudiSequencer/SeqMergeBu2LLK_mt

GaudiSequencer/SEQ:LambdastarsForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdastar2pK_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdastar2pK](./stripping21r1p1-commonparticles-stdlooselambdastar2pk)/Particles',True)\>0 |

FilterDesktop/LambdastarsForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseLambdastar2pK](./stripping21r1p1-commonparticles-stdlooselambdastar2pk)' ]                                                  |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/LambdastarsForBu2LLK/Particles                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/MergeBu2LLK_mt

|                 |                                   |
|-----------------|-----------------------------------|
| Code            | ALL                               |
| Inputs          | [ 'Phys/LambdastarsForBu2LLK' ] |
| DecayDescriptor | None                              |
| Output          | Phys/MergeBu2LLK_mt/Particles     |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Bu2LLK_mtLine

|                  |                                                                                                                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_mt' , 'Phys/SelMuTauForBu2LLK' ]                                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'K_1(1270)+' : 'ALL' , 'K_1(1270)-' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 5000 \*MeV                                                                                                                                                                                                                                                                                                                   |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 9) & (BPVIPCHI2() \< 25) & (BPVDIRA \> 0.9995) & (BPVVDCHI2 \> 100))                                                                                                                                                                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ '[ B+ -\> J/psi(1S) K+ ]cc' , '[ B+ -\> J/psi(1S) K\*(892)+ ]cc' , '[ B+ -\> J/psi(1S) K_1(1270)+ ]cc' , '[ B0 -\> J/psi(1S) KS0 ]cc' , '[ B0 -\> J/psi(1S) K\*(892)0 ]cc' , '[ B_s0 -\> J/psi(1S) phi(1020) ]cc' , '[ Lambda_b0 -\> J/psi(1S) Lambda0 ]cc' , '[ Lambda_b0 -\> J/psi(1S) Lambda(1520)0 ]cc' ]             |
| Output           | Phys/Bu2LLK_mtLine/Particles                                                                                                                                                                                                                                                                                                                  |

AddRelatedInfo/RelatedInfo1_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo1_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo2_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo3_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo4_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo5_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo5_Bu2LLK_mtLine/Particles |

AddRelatedInfo/RelatedInfo6_Bu2LLK_mtLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mtLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo6_Bu2LLK_mtLine/Particles |
