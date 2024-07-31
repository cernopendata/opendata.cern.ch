[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLc23MuLc2pemupi0RLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/Lc23MuLc2pemupi0RLine/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 1.0000000                            |
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

**LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseElectrons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseMuons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseMuons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0**

|      |                                         |
|------|-----------------------------------------|
| Code | 0 StdLooseResolvedPi0 /Particles',True) |

**DaVinci::N4BodyDecays/Lc23MuLc2pemupi0RLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r0p2-stdlooseelectrons) ' , 'Phys/ [StdLooseMuons](./stripping21r0p2-stdloosemuons) ' , 'Phys/ [StdLooseProtons](./stripping21r0p2-stdlooseprotons) ' , 'Phys/ [StdLooseResolvedPi0](./stripping21r0p2-stdlooseresolvedpi0) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDe-PIDpi)\>2)' , 'e-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDe-PIDpi)\>2)' , 'mu+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDmu-PIDpi)\>-5) & ((PIDmu-PIDK)\>-5)' , 'mu-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDmu-PIDpi)\>-5) & ((PIDmu-PIDK)\>-5)' , 'p+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' , 'pi0' : '\n (PT \> 300\*MeV) \n & (M \> 135 - 25 \*MeV) & (M \< 135 + 25 \*MeV)\n & ( CHILDCUT( (CL \> 0.2) ,1) )\n & ( CHILDCUT( (CL \> 0.2) ,2) )\n ' , 'p\~-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' } |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 500\*MeV) & (ACHI2DOCA(1,4) \< 10.0) & (ACHI2DOCA(2,4) \< 10.0) & (ACHI2DOCA(3,4) \< 10.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME()\*c_light) \> 70\*micrometer ) & ( BPVIPCHI2() \< 100 ) & ( BPVDIRA \> 0.999 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ e+ mu- pi0]cc' , '[Lambda_c+ -\> p+ e- mu+ pi0]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/Lc23MuLc2pemupi0RLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

**AddRelatedInfo/RelatedInfo1_Lc23MuLc2pemupi0RLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pemupi0RLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_Lc23MuLc2pemupi0RLine/Particles |

**AddRelatedInfo/RelatedInfo2_Lc23MuLc2pemupi0RLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pemupi0RLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_Lc23MuLc2pemupi0RLine/Particles |

**AddRelatedInfo/RelatedInfo3_Lc23MuLc2pemupi0RLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pemupi0RLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_Lc23MuLc2pemupi0RLine/Particles |

**AddRelatedInfo/RelatedInfo4_Lc23MuLc2pemupi0RLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pemupi0RLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo4_Lc23MuLc2pemupi0RLine/Particles |

**AddRelatedInfo/RelatedInfo5_Lc23MuLc2pemupi0RLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pemupi0RLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo5_Lc23MuLc2pemupi0RLine/Particles |

**AddRelatedInfo/RelatedInfo6_Lc23MuLc2pemupi0RLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pemupi0RLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo6_Lc23MuLc2pemupi0RLine/Particles |

**AddRelatedInfo/RelatedInfo7_Lc23MuLc2pemupi0RLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pemupi0RLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo7_Lc23MuLc2pemupi0RLine/Particles |

**AddRelatedInfo/RelatedInfo8_Lc23MuLc2pemupi0RLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Lc23MuLc2pemupi0RLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo8_Lc23MuLc2pemupi0RLine/Particles |
