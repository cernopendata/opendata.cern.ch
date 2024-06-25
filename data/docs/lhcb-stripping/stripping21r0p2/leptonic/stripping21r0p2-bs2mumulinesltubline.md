[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBs2MuMuLinesLTUBLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/Bs2MuMuLinesLTUBLine/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**CombineParticles/Bs2MuMuLinesLTUBLine**

|                  |                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p2-stdallloosemuons) ' ]                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(PT \> 500\*MeV) & (TRCHI2DOF \< 4 ) & (0.5 500\*MeV) & (TRCHI2DOF \< 4 ) & (0.5                                        |
| CombinationCut   | (ADAMASS('B_s0')\<500\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 500\*MeV )& (BPVIPCHI2()\< 25) & (BPVLTIME()\>0.6\*ps)& (BPVLTIME()\<13.248\*ps)& (PT \> 500\*MeV) |
| DecayDescriptor  | B_s0 -\> mu+ mu-                                                                                                                                |
| DecayDescriptors | [ 'B_s0 -\> mu+ mu-' ]                                                                                                                        |
| Output           | Phys/Bs2MuMuLinesLTUBLine/Particles                                                                                                             |

**AddRelatedInfo/RelatedInfo1_Bs2MuMuLinesLTUBLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesLTUBLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_Bs2MuMuLinesLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo2_Bs2MuMuLinesLTUBLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesLTUBLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_Bs2MuMuLinesLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo3_Bs2MuMuLinesLTUBLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesLTUBLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_Bs2MuMuLinesLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo4_Bs2MuMuLinesLTUBLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesLTUBLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_Bs2MuMuLinesLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo5_Bs2MuMuLinesLTUBLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesLTUBLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo5_Bs2MuMuLinesLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo6_Bs2MuMuLinesLTUBLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesLTUBLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo6_Bs2MuMuLinesLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo7_Bs2MuMuLinesLTUBLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesLTUBLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo7_Bs2MuMuLinesLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo8_Bs2MuMuLinesLTUBLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesLTUBLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo8_Bs2MuMuLinesLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo9_Bs2MuMuLinesLTUBLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesLTUBLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo9_Bs2MuMuLinesLTUBLine/Particles |
