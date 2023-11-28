[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingBu2LLK_meSSLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/Bu2LLK_meSSLine/Particles |
| Postscale      | 1.0000000                      |
| HLT1           | None                           |
| HLT2           | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

LoKi::VoidFilter/StrippingBu2LLK_meSSLineVOIDFilter

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

LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseElectrons](./stripping21r1p1-commonparticles-stdlooseelectrons)/Particles',True)\>0 |

CombineParticles/MuESSForBu2LLK

|                  |                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseElectrons](./stripping21r1p1-commonparticles-stdlooseelectrons)' , 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' ]                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(PT \> 300) & (MIPCHI2DV(PRIMARY) \> 9)&(PIDe \> 0)' , 'e-' : '(PT \> 300) & (MIPCHI2DV(PRIMARY) \> 9)&(PIDe \> 0)' , 'mu+' : '(PT \> 300) & (MIPCHI2DV(PRIMARY) \> 9)&(HASMUON)&(ISMUON)' , 'mu-' : '(PT \> 300) & (MIPCHI2DV(PRIMARY) \> 9)&(HASMUON)&(ISMUON)' } |
| CombinationCut   | (AM \> 100\*MeV)                                                                                                                                                                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9)                                                                                                                                                                                                                                                                  |
| DecayDescriptor  | [J/psi(1S) -\> mu+ e+]cc                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[J/psi(1S) -\> mu+ e+]cc' ]                                                                                                                                                                                                                                                         |
| Output           | Phys/MuESSForBu2LLK/Particles                                                                                                                                                                                                                                                              |

FilterDesktop/SelMuESSForBu2LLK

|                 |                                                                                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ID=='J/psi(1S)') & (PT \> 0 \*MeV) & (MM \< 5500 \*MeV) & (MINTREE(ABSID\<14,PT) \> 300 \*MeV) & (MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY)) \> 9) & (VFASPF(VCHI2/VDOF) \< 9) & (BPVVDCHI2 \> 16) & (MIPCHI2DV(PRIMARY) \> 0) |
| Inputs          | [ 'Phys/MuESSForBu2LLK' ]                                                                                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                       |
| Output          | Phys/SelMuESSForBu2LLK/Particles                                                                                                                                                                                           |

GaudiSequencer/SeqMergeBu2LLK_meSS

GaudiSequencer/SEQ:KaonsForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/KaonsForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ]                                                                  |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/KaonsForBu2LLK/Particles                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KstarsForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKstar2Kpi](./stripping21r1p1-commonparticles-stdloosekstar2kpi)/Particles',True)\>0 |

FilterDesktop/KstarsForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseKstar2Kpi](./stripping21r1p1-commonparticles-stdloosekstar2kpi)' ]                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/KstarsForBu2LLK/Particles                                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:PhisForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePhi2KK](./stripping21r1p1-commonparticles-stdloosephi2kk)/Particles',True)\>0 |

FilterDesktop/PhisForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21r1p1-commonparticles-stdloosephi2kk)' ]                                                                |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/PhisForBu2LLK/Particles                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KshortsLLForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/KshortsLLForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)' ]                                                                    |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/KshortsLLForBu2LLK/Particles                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KshortsDDForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KshortsDDForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)' ]                                                                    |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/KshortsDDForBu2LLK/Particles                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:LambdasLLForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21r1p1-commonparticles-stdlooselambdall)/Particles',True)\>0 |

FilterDesktop/LambdasLLForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21r1p1-commonparticles-stdlooselambdall)' ]                                                            |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/LambdasLLForBu2LLK/Particles                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:LambdasDDForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r1p1-commonparticles-stdlooselambdadd)/Particles',True)\>0 |

FilterDesktop/LambdasDDForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1p1-commonparticles-stdlooselambdadd)' ]                                                            |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/LambdasDDForBu2LLK/Particles                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

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

GaudiSequencer/SEQ:KstarsPlusLLForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

CombineParticles/KstarsPlusLLForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)' , 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))' , 'pi+' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' , 'pi-' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' } |
| CombinationCut   | (APT \> 400 \*MeV) & (ADAMASS('K\*(892)+') \< 300 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                              |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | [K\*(892)+ -\> KS0 pi+]cc                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                                                                                                                                                                                                              |
| Output           | Phys/KstarsPlusLLForBu2LLK/Particles                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:KstarsPlusDDForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

CombineParticles/KstarsPlusDDForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)' , 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))' , 'pi+' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' , 'pi-' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' } |
| CombinationCut   | (APT \> 400 \*MeV) & (ADAMASS('K\*(892)+') \< 300 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                              |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | [K\*(892)+ -\> KS0 pi+]cc                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                                                                                                                                                                                                              |
| Output           | Phys/KstarsPlusDDForBu2LLK/Particles                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/MergeBu2LLK_meSS

|                 |                                                                                                                                                                                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                     |
| Inputs          | [ 'Phys/KaonsForBu2LLK' , 'Phys/KshortsDDForBu2LLK' , 'Phys/KshortsLLForBu2LLK' , 'Phys/KstarsForBu2LLK' , 'Phys/KstarsPlusDDForBu2LLK' , 'Phys/KstarsPlusLLForBu2LLK' , 'Phys/LambdasDDForBu2LLK' , 'Phys/LambdasLLForBu2LLK' , 'Phys/LambdastarsForBu2LLK' , 'Phys/PhisForBu2LLK' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                    |
| Output          | Phys/MergeBu2LLK_meSS/Particles                                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/Bu2LLK_meSSLine

|                  |                                                                                                                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_meSS' , 'Phys/SelMuESSForBu2LLK' ]                                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'K_1(1270)+' : 'ALL' , 'K_1(1270)-' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 1500 \*MeV                                                                                                                                                                                                                                                                                                                   |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 9) & (BPVIPCHI2() \< 25) & (BPVDIRA \> 0.9995) & (BPVVDCHI2 \> 100))                                                                                                                                                                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ '[ B+ -\> J/psi(1S) K+ ]cc' , '[ B+ -\> J/psi(1S) K\*(892)+ ]cc' , '[ B+ -\> J/psi(1S) K_1(1270)+ ]cc' , '[ B0 -\> J/psi(1S) KS0 ]cc' , '[ B0 -\> J/psi(1S) K\*(892)0 ]cc' , '[ B_s0 -\> J/psi(1S) phi(1020) ]cc' , '[ Lambda_b0 -\> J/psi(1S) Lambda0 ]cc' , '[ Lambda_b0 -\> J/psi(1S) Lambda(1520)0 ]cc' ]             |
| Output           | Phys/Bu2LLK_meSSLine/Particles                                                                                                                                                                                                                                                                                                                |

AddRelatedInfo/RelatedInfo1_Bu2LLK_meSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_meSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo1_Bu2LLK_meSSLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2LLK_meSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_meSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo2_Bu2LLK_meSSLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2LLK_meSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_meSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo3_Bu2LLK_meSSLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2LLK_meSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_meSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo4_Bu2LLK_meSSLine/Particles |

AddRelatedInfo/RelatedInfo5_Bu2LLK_meSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_meSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo5_Bu2LLK_meSSLine/Particles |

AddRelatedInfo/RelatedInfo6_Bu2LLK_meSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_meSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo6_Bu2LLK_meSSLine/Particles |
