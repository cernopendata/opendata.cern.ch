[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLc23MuLc2mueeLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/Lc23MuLc2mueeLine/Particles |
| Postscale      | 1.0000000                        |
| HLT1           | None                             |
| HLT2           | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseMuons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseMuons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseElectrons /Particles',True) |

**DaVinci::N3BodyDecays/Lc23MuLc2mueeLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r1p2-stdlooseelectrons) ' , 'Phys/ [StdLooseMuons](./stripping21r1p2-stdloosemuons) ' ]                                                                                                                                                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDe-PIDpi)\>2)' , 'e-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDe-PIDpi)\>2)' , 'mu+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n ' , 'mu-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n ' } |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 350\*MeV) & (ADOCA(1,3) \< 0.3\*mm) & (ADOCA(2,3) \< 0.3\*mm)                                                                                                                                                                                                                                                                                                                                                                             |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME()\*c_light) \> 70\*micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Lambda_c+ -\> mu+ e+ e-]cc' , '[Lambda_c+ -\> mu- e+ e+]cc' , '[Lambda_c+ -\> mu+ e+ e+]cc' ]                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/Lc23MuLc2mueeLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                   |

**AddRelatedInfo/RelatedInfo1_Lc23MuLc2mueeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2mueeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo1_Lc23MuLc2mueeLine/Particles |

**AddRelatedInfo/RelatedInfo2_Lc23MuLc2mueeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2mueeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo2_Lc23MuLc2mueeLine/Particles |

**AddRelatedInfo/RelatedInfo3_Lc23MuLc2mueeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2mueeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo3_Lc23MuLc2mueeLine/Particles |

**AddRelatedInfo/RelatedInfo4_Lc23MuLc2mueeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2mueeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo4_Lc23MuLc2mueeLine/Particles |

**AddRelatedInfo/RelatedInfo5_Lc23MuLc2mueeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2mueeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo5_Lc23MuLc2mueeLine/Particles |

**AddRelatedInfo/RelatedInfo6_Lc23MuLc2mueeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2mueeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo6_Lc23MuLc2mueeLine/Particles |

**AddRelatedInfo/RelatedInfo7_Lc23MuLc2mueeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2mueeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo7_Lc23MuLc2mueeLine/Particles |

**AddRelatedInfo/RelatedInfo8_Lc23MuLc2mueeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2mueeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo8_Lc23MuLc2mueeLine/Particles |
