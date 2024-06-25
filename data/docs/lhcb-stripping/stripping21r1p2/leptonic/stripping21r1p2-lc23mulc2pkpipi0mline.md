[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLc23MuLc2pKpipi0MLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/Lc23MuLc2pKpipi0MLine/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 0.10000000                           |
| L0DU           | None                                 |
| ODIN           | None                                 |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseKaons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseKaons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLoosePions**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLoosePions /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseMergedPi0 /Particles',True) |

**DaVinci::N4BodyDecays/Lc23MuLc2pKpipi0MLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseKaons](./stripping21r1p2-stdloosekaons) ' , 'Phys/ [StdLooseMergedPi0](./stripping21r1p2-stdloosemergedpi0) ' , 'Phys/ [StdLoosePions](./stripping21r1p2-stdloosepions) ' , 'Phys/ [StdLooseProtons](./stripping21r1p2-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDK-PIDpi)\>5) & ((PIDK-PIDp)\>0)' , 'K-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDK-PIDpi)\>5) & ((PIDK-PIDp)\>0)' , 'p+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' , 'pi+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n ' , 'pi-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n ' , 'pi0' : '\n ( PT \> 500\*MeV )\n & (M \> 135 - 60 \*MeV) & (M \< 135 + 60 \*MeV)\n ' , 'p\~-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' } |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 500\*MeV) & (ACHI2DOCA(1,4) \< 10.0) & (ACHI2DOCA(2,4) \< 10.0) & (ACHI2DOCA(3,4) \< 10.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME()\*c_light) \> 70\*micrometer ) & ( BPVIPCHI2() \< 100 ) & ( BPVDIRA \> 0.999 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ K- pi+ pi0]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/Lc23MuLc2pKpipi0MLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

**AddRelatedInfo/RelatedInfo1_Lc23MuLc2pKpipi0MLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pKpipi0MLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_Lc23MuLc2pKpipi0MLine/Particles |

**AddRelatedInfo/RelatedInfo2_Lc23MuLc2pKpipi0MLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pKpipi0MLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_Lc23MuLc2pKpipi0MLine/Particles |

**AddRelatedInfo/RelatedInfo3_Lc23MuLc2pKpipi0MLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pKpipi0MLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_Lc23MuLc2pKpipi0MLine/Particles |

**AddRelatedInfo/RelatedInfo4_Lc23MuLc2pKpipi0MLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pKpipi0MLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo4_Lc23MuLc2pKpipi0MLine/Particles |

**AddRelatedInfo/RelatedInfo5_Lc23MuLc2pKpipi0MLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pKpipi0MLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo5_Lc23MuLc2pKpipi0MLine/Particles |

**AddRelatedInfo/RelatedInfo6_Lc23MuLc2pKpipi0MLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pKpipi0MLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo6_Lc23MuLc2pKpipi0MLine/Particles |

**AddRelatedInfo/RelatedInfo7_Lc23MuLc2pKpipi0MLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pKpipi0MLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo7_Lc23MuLc2pKpipi0MLine/Particles |

**AddRelatedInfo/RelatedInfo8_Lc23MuLc2pKpipi0MLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pKpipi0MLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo8_Lc23MuLc2pKpipi0MLine/Particles |
