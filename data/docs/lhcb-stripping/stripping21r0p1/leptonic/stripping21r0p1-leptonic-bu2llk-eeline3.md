[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingBu2LLK_eeLine3

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/Bu2LLK_eeLine3/Particles |
| Postscale      | 1.0000000                     |
| HLT1           | None                          |
| HLT2           | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

LoKi::VoidFilter/StrippingBu2LLK_eeLine3VOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqMergeBu2LLK_ee3

GaudiSequencer/SEQ:KstarsForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKstar2Kpi](./stripping21r0p1-commonparticles-stdloosekstar2kpi)/Particles',True)\>0 |

FilterDesktop/KstarsForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseKstar2Kpi](./stripping21r0p1-commonparticles-stdloosekstar2kpi)' ]                                                          |
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
| Code | CONTAINS('Phys/[StdLoosePhi2KK](./stripping21r0p1-commonparticles-stdloosephi2kk)/Particles',True)\>0 |

FilterDesktop/PhisForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21r0p1-commonparticles-stdloosephi2kk)' ]                                                                |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/PhisForBu2LLK/Particles                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:LambdasLLForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21r0p1-commonparticles-stdlooselambdall)/Particles',True)\>0 |

FilterDesktop/LambdasLLForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21r0p1-commonparticles-stdlooselambdall)' ]                                                            |
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
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r0p1-commonparticles-stdlooselambdadd)/Particles',True)\>0 |

FilterDesktop/LambdasDDForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r0p1-commonparticles-stdlooselambdadd)' ]                                                            |
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
| Code | CONTAINS('Phys/[StdLooseLambdastar2pK](./stripping21r0p1-commonparticles-stdlooselambdastar2pk)/Particles',True)\>0 |

FilterDesktop/LambdastarsForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseLambdastar2pK](./stripping21r0p1-commonparticles-stdlooselambdastar2pk)' ]                                                  |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/LambdastarsForBu2LLK/Particles                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:K1ForBu2LLK

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

CombineParticles/K1ForBu2LLK

|                  |                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)' , 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ]                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.4)' , 'K-' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.4)' , 'pi+' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.4)' , 'pi-' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.4)' } |
| CombinationCut   | (AM \> 0\*MeV) & (AM \< 6000\*MeV) & ((APT1+APT2+APT3) \> 800\*MeV)                                                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2) \< 12) & (SUMTREE(MIPCHI2DV(PRIMARY),((ABSID=='K+') \| (ABSID=='K-') \| (ABSID=='pi+') \| (ABSID=='pi-')),0.0) \> 48.0)                                                                                       |
| DecayDescriptor  | [K_1(1270)+ -\> K+ pi+ pi-]cc                                                                                                                                                                                              |
| DecayDescriptors | [ '[K_1(1270)+ -\> K+ pi+ pi-]cc' ]                                                                                                                                                                                      |
| Output           | Phys/K1ForBu2LLK/Particles                                                                                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/MergeBu2LLK_ee3

|                 |                                                                                                                                                                |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                            |
| Inputs          | [ 'Phys/K1ForBu2LLK' , 'Phys/KstarsForBu2LLK' , 'Phys/LambdasDDForBu2LLK' , 'Phys/LambdasLLForBu2LLK' , 'Phys/LambdastarsForBu2LLK' , 'Phys/PhisForBu2LLK' ] |
| DecayDescriptor | None                                                                                                                                                           |
| Output          | Phys/MergeBu2LLK_ee3/Particles                                                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaLL_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseGammaLL](./stripping21r0p1-commonparticles-stdallloosegammall)/Particles',True)\>0 |

FilterDesktop/SelPhotonForBu2LLK

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PT \> 1000\*MeV) & (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 9)                             |
| Inputs          | [ 'Phys/[StdAllLooseGammaLL](./stripping21r0p1-commonparticles-stdallloosegammall)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/SelPhotonForBu2LLK/Particles                                                       |

CombineParticles/Bu2LLK_eeLine3

|                  |                                                                                                                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_ee3' , 'Phys/SelPhotonForBu2LLK' ]                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'gamma' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 1500 \*MeV                                                                                                                                                                       |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 9) & (BPVIPCHI2() \< 25) & (BPVDIRA \> 0.9995) & (BPVVDCHI2 \> 100))                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                              |
| DecayDescriptors | [ '[ B0 -\> gamma K\*(892)0 ]cc' , '[ B_s0 -\> gamma phi(1020) ]cc' , '[ Lambda_b0 -\> gamma Lambda0 ]cc' , '[ Lambda_b0 -\> gamma Lambda(1520)0 ]cc' ]                                 |
| Output           | Phys/Bu2LLK_eeLine3/Particles                                                                                                                                                                     |

AddRelatedInfo/RelatedInfo1_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo1_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo2_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo2_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo3_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo3_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo4_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo4_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo5_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo5_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo6_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo6_Bu2LLK_eeLine3/Particles |
