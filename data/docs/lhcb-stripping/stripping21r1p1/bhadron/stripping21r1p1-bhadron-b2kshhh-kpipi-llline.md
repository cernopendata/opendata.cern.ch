[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2KShhh_KPiPi_LLLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/B2KShhh_KPiPi_LLLine/Particles           |
| Postscale      | 1.0000000                                     |
| HLT1           | HLT_PASS_RE('Hlt1TrackAllL0Decision')         |
| HLT2           | HLT_PASS_RE('Hlt2Topo[234]Body.\*Decision') |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21r1p1-commonparticles-stdnopidspions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21r1p1-commonparticles-stdnopidskaons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/SelKSLLForB2KShhh

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | (BPVVDZ \> 0.0 ) &(BPVVDZ \< 9999.0 ) &(BPVDIRA \> 0.999 ) &(ADMASS('KS0') \< 35.0 ) &(BPVVDCHI2\> 5 ) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)' ]                            |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/SelKSLLForB2KShhh/Particles                                                                       |

DaVinci::N4BodyDecays/B2KShhh_KPiPi_LLLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKSLLForB2KShhh' , 'Phys/[StdNoPIDsKaons](./stripping21r1p1-commonparticles-stdnopidskaons)' , 'Phys/[StdNoPIDsPions](./stripping21r1p1-commonparticles-stdnopidspions)' ]                                                                                                                                                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : ' (TRGHOSTPROB \< 0.4)&(TRCHI2DOF \< 4)&(PT \> 500.0)&(P \> 1500.0)&(MIPCHI2DV(PRIMARY) \> 4 )&(PIDK \> 0)' , 'K-' : ' (TRGHOSTPROB \< 0.4)&(TRCHI2DOF \< 4)&(PT \> 500.0)&(P \> 1500.0)&(MIPCHI2DV(PRIMARY) \> 4 )&(PIDK \> 0)' , 'KS0' : 'ALL' , 'pi+' : ' (TRGHOSTPROB \< 0.4)&(TRCHI2DOF \< 4)&(PT \> 500.0)&(P \> 1500.0)&(MIPCHI2DV(PRIMARY) \> 4 )&(PIDK \< 0)' , 'pi-' : ' (TRGHOSTPROB \< 0.4)&(TRCHI2DOF \< 4)&(PT \> 500.0)&(P \> 1500.0)&(MIPCHI2DV(PRIMARY) \> 4 )&(PIDK \< 0)' } |
| CombinationCut   | (in_range( 4500.0, AM, 7200.0 )) &( (APT1+APT2+APT3+APT4) \> 500.0 )&( ACHI2DOCA(1,4) \< 10.0 ) &( ACHI2DOCA(2,4) \< 10.0 ) &( ACHI2DOCA(3,4) \< 10.0 )                                                                                                                                                                                                                                                                                                                                                              |
| MotherCut        | (in_range( 4700.0, M, 7000.0 )) &(PT \> 1500.0)&(VFASPF(VCHI2PDOF) \< 12.0)&(BPVDIRA \> 0.99995 )&(BPVLTIME() \> 0.0001 )                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[B+ -\> pi+ K- pi+ KS0]cc' , '[B+ -\> pi+ pi- K+ KS0]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/B2KShhh_KPiPi_LLLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

AddRelatedInfo/RelatedInfo1_B2KShhh_KPiPi_LLLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2KShhh_KPiPi_LLLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_B2KShhh_KPiPi_LLLine/Particles |

AddRelatedInfo/RelatedInfo2_B2KShhh_KPiPi_LLLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2KShhh_KPiPi_LLLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_B2KShhh_KPiPi_LLLine/Particles |

AddRelatedInfo/RelatedInfo3_B2KShhh_KPiPi_LLLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2KShhh_KPiPi_LLLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_B2KShhh_KPiPi_LLLine/Particles |

AddRelatedInfo/RelatedInfo4_B2KShhh_KPiPi_LLLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2KShhh_KPiPi_LLLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_B2KShhh_KPiPi_LLLine/Particles |

AddRelatedInfo/RelatedInfo5_B2KShhh_KPiPi_LLLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2KShhh_KPiPi_LLLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo5_B2KShhh_KPiPi_LLLine/Particles |
