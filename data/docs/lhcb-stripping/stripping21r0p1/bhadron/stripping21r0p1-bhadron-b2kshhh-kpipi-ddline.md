[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB2KShhh_KPiPi_DDLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/B2KShhh_KPiPi_DDLine/Particles           |
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
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21r0p1-commonparticles-stdnopidspions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21r0p1-commonparticles-stdnopidskaons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/SelKSDDForB2KShhh

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | (BPVVDZ \> 0.0 ) &(BPVVDZ \< 9999.0 ) &(BPVDIRA \> 0.999 ) &(ADMASS('KS0') \< 50.0 ) &(BPVVDCHI2\> 5 ) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ]                            |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/SelKSDDForB2KShhh/Particles                                                                       |

DaVinci::N4BodyDecays/B2KShhh_KPiPi_DDLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKSDDForB2KShhh' , 'Phys/[StdNoPIDsKaons](./stripping21r0p1-commonparticles-stdnopidskaons)' , 'Phys/[StdNoPIDsPions](./stripping21r0p1-commonparticles-stdnopidspions)' ]                                                                                                                                                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : ' (TRGHOSTPROB \< 0.4)&(TRCHI2DOF \< 4)&(PT \> 500.0)&(P \> 1500.0)&(MIPCHI2DV(PRIMARY) \> 4 )&(PIDK \> 0)' , 'K-' : ' (TRGHOSTPROB \< 0.4)&(TRCHI2DOF \< 4)&(PT \> 500.0)&(P \> 1500.0)&(MIPCHI2DV(PRIMARY) \> 4 )&(PIDK \> 0)' , 'KS0' : 'ALL' , 'pi+' : ' (TRGHOSTPROB \< 0.4)&(TRCHI2DOF \< 4)&(PT \> 500.0)&(P \> 1500.0)&(MIPCHI2DV(PRIMARY) \> 4 )&(PIDK \< 0)' , 'pi-' : ' (TRGHOSTPROB \< 0.4)&(TRCHI2DOF \< 4)&(PT \> 500.0)&(P \> 1500.0)&(MIPCHI2DV(PRIMARY) \> 4 )&(PIDK \< 0)' } |
| CombinationCut   | (in_range( 4500.0, AM, 7200.0 )) &( (APT1+APT2+APT3+APT4) \> 500.0 )&( ACHI2DOCA(1,4) \< 10.0 ) &( ACHI2DOCA(2,4) \< 10.0 ) &( ACHI2DOCA(3,4) \< 10.0 )                                                                                                                                                                                                                                                                                                                                                              |
| MotherCut        | (in_range( 4700.0, M, 7000.0 )) &(PT \> 1500.0)&(VFASPF(VCHI2PDOF) \< 12.0)&(BPVDIRA \> 0.99995 )&(BPVLTIME() \> 0.0001 )                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[B+ -\> pi+ K- pi+ KS0]cc' , '[B+ -\> pi+ pi- K+ KS0]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/B2KShhh_KPiPi_DDLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

AddRelatedInfo/RelatedInfo1_B2KShhh_KPiPi_DDLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2KShhh_KPiPi_DDLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_B2KShhh_KPiPi_DDLine/Particles |

AddRelatedInfo/RelatedInfo2_B2KShhh_KPiPi_DDLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2KShhh_KPiPi_DDLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_B2KShhh_KPiPi_DDLine/Particles |

AddRelatedInfo/RelatedInfo3_B2KShhh_KPiPi_DDLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2KShhh_KPiPi_DDLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_B2KShhh_KPiPi_DDLine/Particles |

AddRelatedInfo/RelatedInfo4_B2KShhh_KPiPi_DDLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2KShhh_KPiPi_DDLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_B2KShhh_KPiPi_DDLine/Particles |

AddRelatedInfo/RelatedInfo5_B2KShhh_KPiPi_DDLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2KShhh_KPiPi_DDLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo5_B2KShhh_KPiPi_DDLine/Particles |
