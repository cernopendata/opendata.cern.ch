[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingTau23MuTau23MuLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/Tau23MuTau23MuLine/Particles |
| Postscale      | 1.0000000                         |
| HLT1           | None                              |
| HLT2           | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

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

**CombineParticles/Tau23MuTau23MuLine**

|                  |                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r0p2-stdloosemuons) ' ]                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' ( PT \> 300 \* MeV ) & ( TRGHOSTPROB \< 0.45 ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) ' , 'mu-' : ' ( PT \> 300 \* MeV ) & ( TRGHOSTPROB \< 0.45 ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) ' } |
| CombinationCut   | (ADAMASS('tau+')\<400\*MeV)                                                                                                                                                                                                        |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME () \* c_light) \> 100 \* micrometer ) & ( BPVIPCHI2() \< 225 )                                                                                                                               |
| DecayDescriptor  | [ tau+ -\> mu+ mu+ mu- ]cc                                                                                                                                                                                                       |
| DecayDescriptors | [ ' [ tau+ -\> mu+ mu+ mu- ]cc' ]                                                                                                                                                                                              |
| Output           | Phys/Tau23MuTau23MuLine/Particles                                                                                                                                                                                                  |

**AddRelatedInfo/RelatedInfo1_Tau23MuTau23MuLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau23MuLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo1_Tau23MuTau23MuLine/Particles |

**AddRelatedInfo/RelatedInfo2_Tau23MuTau23MuLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau23MuLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo2_Tau23MuTau23MuLine/Particles |

**AddRelatedInfo/RelatedInfo3_Tau23MuTau23MuLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau23MuLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo3_Tau23MuTau23MuLine/Particles |

**AddRelatedInfo/RelatedInfo4_Tau23MuTau23MuLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau23MuLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo4_Tau23MuTau23MuLine/Particles |

**AddRelatedInfo/RelatedInfo5_Tau23MuTau23MuLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau23MuLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo5_Tau23MuTau23MuLine/Particles |

**AddRelatedInfo/RelatedInfo6_Tau23MuTau23MuLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau23MuLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo6_Tau23MuTau23MuLine/Particles |
