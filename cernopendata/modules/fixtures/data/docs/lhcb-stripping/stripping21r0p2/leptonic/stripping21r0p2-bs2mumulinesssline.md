[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBs2MuMuLinesSSLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/Bs2MuMuLinesSSLine/Particles |
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

**CombineParticles/Bs2MuMuLinesSSLine**

|                  |                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r0p2-stdloosemuons) ' ]                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 9 )&(TRCHI2DOF \< 4 ) & ( TRGHOSTPROB \< 0.4 )' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 9 )&(TRCHI2DOF \< 4 ) & ( TRGHOSTPROB \< 0.4 )' } |
| CombinationCut   | (ADAMASS('B_s0')\<200\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 200\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 121)& (BPVIPCHI2()\< 25)                                                                  |
| DecayDescriptor  | [B_s0 -\> mu+ mu+]cc                                                                                                                                                           |
| DecayDescriptors | [ '[B_s0 -\> mu+ mu+]cc' ]                                                                                                                                                   |
| Output           | Phys/Bs2MuMuLinesSSLine/Particles                                                                                                                                                |

**AddRelatedInfo/RelatedInfo1_Bs2MuMuLinesSSLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesSSLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo1_Bs2MuMuLinesSSLine/Particles |

**AddRelatedInfo/RelatedInfo2_Bs2MuMuLinesSSLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesSSLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo2_Bs2MuMuLinesSSLine/Particles |

**AddRelatedInfo/RelatedInfo3_Bs2MuMuLinesSSLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesSSLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo3_Bs2MuMuLinesSSLine/Particles |

**AddRelatedInfo/RelatedInfo4_Bs2MuMuLinesSSLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesSSLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo4_Bs2MuMuLinesSSLine/Particles |

**AddRelatedInfo/RelatedInfo5_Bs2MuMuLinesSSLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesSSLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo5_Bs2MuMuLinesSSLine/Particles |

**AddRelatedInfo/RelatedInfo6_Bs2MuMuLinesSSLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesSSLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo6_Bs2MuMuLinesSSLine/Particles |

**AddRelatedInfo/RelatedInfo7_Bs2MuMuLinesSSLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesSSLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo7_Bs2MuMuLinesSSLine/Particles |

**AddRelatedInfo/RelatedInfo8_Bs2MuMuLinesSSLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesSSLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo8_Bs2MuMuLinesSSLine/Particles |

**AddRelatedInfo/RelatedInfo9_Bs2MuMuLinesSSLine**

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesSSLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo9_Bs2MuMuLinesSSLine/Particles |

**AddRelatedInfo/RelatedInfo10_Bs2MuMuLinesSSLine**

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesSSLine' ]                 |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo10_Bs2MuMuLinesSSLine/Particles |
