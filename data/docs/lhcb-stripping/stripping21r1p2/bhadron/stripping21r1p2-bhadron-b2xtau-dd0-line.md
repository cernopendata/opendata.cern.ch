[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2XTau_DD0_Line

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/B2XTau_DD0_Line/Particles |
| Postscale      | 1.0000000                      |
| HLT1           | None                           |
| HLT2           | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

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

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/PionsDForB2XTau

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000\*MeV) & (PT \> 250\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 4) & (TRGHOSTPROB \< 0.4) & (PROBNNpi \> 0.55) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                   |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/PionsDForB2XTau/Particles                                                                                                  |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/KaonsDForB2XTau

|                 |                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 2000\*MeV) & (PT \> 250\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 4) & (TRGHOSTPROB \< 0.4) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ]                              |
| DecayDescriptor | None                                                                                                       |
| Output          | Phys/KaonsDForB2XTau/Particles                                                                             |

CombineParticles/D0ForB2XTau

|                  |                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsDForB2XTau' , 'Phys/PionsDForB2XTau' ]                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                       |
| CombinationCut   | ( ( in_range ( 1750.0, AM, 2080.0 ) ) \| ( in_range ( 1938.0, AM, 1998.0 ) ) )& ( APT \> 800.0 )& ( AMAXDOCA('') \< 0.2 )& ( ANUM(PT \> 800.0)\>=1 )                               |
| MotherCut        | ( PT \> 1000.0 )& ( BPVDIRA \> 0.99 )& ( VFASPF(VCHI2) \< 16 ) & ( BPVVDCHI2 \> 16 ) & ( in_range ( 0.1, BPVVDRHO, 7.0 ) ) & ( BPVVDZ \> 5.0 )& ( in_range ( 1800.0, M, 2030.0 ) ) |
| DecayDescriptor  | None                                                                                                                                                                               |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                                                                                                        |
| Output           | Phys/D0ForB2XTau/Particles                                                                                                                                                         |

DaVinci::N3BodyDecays/DForB2XTau

|                  |                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsDForB2XTau' , 'Phys/PionsDForB2XTau' ]                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                       |
| CombinationCut   | ( ( in_range ( 1750.0, AM, 2080.0 ) ) \| ( in_range ( 1938.0, AM, 1998.0 ) ) )& ( APT \> 800.0 )& ( AMAXDOCA('') \< 0.2 )& ( ANUM(PT \> 800.0)\>=1 )                               |
| MotherCut        | ( PT \> 1000.0 )& ( BPVDIRA \> 0.99 )& ( VFASPF(VCHI2) \< 16 ) & ( BPVVDCHI2 \> 16 ) & ( in_range ( 0.1, BPVVDRHO, 7.0 ) ) & ( BPVVDZ \> 5.0 )& ( in_range ( 1800.0, M, 2030.0 ) ) |
| DecayDescriptor  | None                                                                                                                                                                               |
| DecayDescriptors | [ '[D+ -\> pi+ K- pi+]cc' , '[D+ -\> K+ K- pi+]cc' ]                                                                                                                         |
| Output           | Phys/DForB2XTau/Particles                                                                                                                                                          |

CombineParticles/B2XTau_DD0_Line

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D0ForB2XTau' , 'Phys/DForB2XTau' ]                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                             |
| CombinationCut   | (APT \> 1900\*MeV) & (AM \> 2000\*MeV) & (AM \< 7000\*MeV) & (AM \> 5000)                                                                                                                                                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 90) & (BPVDIRA \> 0.99) & (BPVVDCHI2 \> 225) & (BPVVD \< 90) & (PT \> 2000\*MeV) & (INGENERATION((PT \> 4000\*MeV),1)) & (INGENERATION((PT \> 2000\*MeV),2)) & (sumpt \>7000\*MeV) & (max(CHILD(ipsm,1),CHILD(ipsm,2)) \> 20) & (max(CHILD(MIPCHI2DV(PRIMARY),1),CHILD(MIPCHI2DV(PRIMARY),2)) \> 150) & (min(CHILD(MIPCHI2DV(PRIMARY),1),CHILD(MIPCHI2DV(PRIMARY),2)) \> 16) & (in_range(0\*MeV,MCOR,10000\*MeV)) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ '[B+ -\> D~0 D+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output           | Phys/B2XTau_DD0_Line/Particles                                                                                                                                                                                                                                                                                                                                                                                                          |

AddRelatedInfo/RelatedInfo1_B2XTau_DD0_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo1_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2XTau_DD0_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo2_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2XTau_DD0_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo3_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2XTau_DD0_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo4_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo5_B2XTau_DD0_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo5_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo6_B2XTau_DD0_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo6_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo7_B2XTau_DD0_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo7_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo8_B2XTau_DD0_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo8_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo9_B2XTau_DD0_Line

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo9_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo10_B2XTau_DD0_Line

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo10_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo11_B2XTau_DD0_Line

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo11_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo12_B2XTau_DD0_Line

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo12_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo13_B2XTau_DD0_Line

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo13_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo14_B2XTau_DD0_Line

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo14_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo15_B2XTau_DD0_Line

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo15_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo16_B2XTau_DD0_Line

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo16_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo17_B2XTau_DD0_Line

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo17_B2XTau_DD0_Line/Particles |

AddRelatedInfo/RelatedInfo18_B2XTau_DD0_Line

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_DD0_Line' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo18_B2XTau_DD0_Line/Particles |
