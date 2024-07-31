[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLc23MuLc2peeLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/Lc23MuLc2peeLine/Particles |
| Postscale      | 1.0000000                       |
| HLT1           | None                            |
| HLT2           | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseProtons**

|      |                                     |
|------|-------------------------------------|
| Code | 0 StdLooseProtons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseElectrons /Particles',True) |

**DaVinci::N3BodyDecays/Lc23MuLc2peeLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r0p2-stdlooseelectrons) ' , 'Phys/ [StdLooseProtons](./stripping21r0p2-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDe-PIDpi)\>2)' , 'e-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDe-PIDpi)\>2)' , 'p+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' , 'p\~-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' } |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 350\*MeV) & (ADOCA(1,3) \< 0.3\*mm) & (ADOCA(2,3) \< 0.3\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME()\*c_light) \> 70\*micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ e+ e-]cc' , '[Lambda_c+ -\> p\~- e+ e+]cc' , '[Lambda_c+ -\> p+ e+ e+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Output           | Phys/Lc23MuLc2peeLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

**AddRelatedInfo/RelatedInfo1_Lc23MuLc2peeLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2peeLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_Lc23MuLc2peeLine/Particles |

**AddRelatedInfo/RelatedInfo2_Lc23MuLc2peeLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2peeLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo2_Lc23MuLc2peeLine/Particles |

**AddRelatedInfo/RelatedInfo3_Lc23MuLc2peeLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2peeLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo3_Lc23MuLc2peeLine/Particles |

**AddRelatedInfo/RelatedInfo4_Lc23MuLc2peeLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2peeLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo4_Lc23MuLc2peeLine/Particles |

**AddRelatedInfo/RelatedInfo5_Lc23MuLc2peeLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2peeLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo5_Lc23MuLc2peeLine/Particles |

**AddRelatedInfo/RelatedInfo6_Lc23MuLc2peeLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2peeLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo6_Lc23MuLc2peeLine/Particles |

**AddRelatedInfo/RelatedInfo7_Lc23MuLc2peeLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2peeLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo7_Lc23MuLc2peeLine/Particles |

**AddRelatedInfo/RelatedInfo8_Lc23MuLc2peeLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2peeLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo8_Lc23MuLc2peeLine/Particles |
