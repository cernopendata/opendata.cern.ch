[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBs2MuMuLinesBs2KKLTUBLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/Bs2MuMuLinesBs2KKLTUBLine/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseKaons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseKaons /Particles',True) |

**CombineParticles/Bs2MuMuLinesBs2KKLTUBLine**

|                  |                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseKaons](./stripping21r1p2-stdallloosekaons) ' ]                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 500\*MeV) & (TRCHI2DOF \< 4 ) & (0.5 5) ' , 'K-' : '(PT \> 500\*MeV) & (TRCHI2DOF \< 4 ) & (0.5 5) ' }            |
| CombinationCut   | (ADAMASS('B_s0')\<500\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 500\*MeV )& (BPVIPCHI2()\< 25) & (BPVLTIME()\>0.6\*ps)& (BPVLTIME()\<13.248\*ps)& (PT \> 500\*MeV) |
| DecayDescriptor  | B_s0 -\> K+ K-                                                                                                                                  |
| DecayDescriptors | [ 'B_s0 -\> K+ K-' ]                                                                                                                          |
| Output           | Phys/Bs2MuMuLinesBs2KKLTUBLine/Particles                                                                                                        |

**AddRelatedInfo/RelatedInfo1_Bs2MuMuLinesBs2KKLTUBLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2KKLTUBLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo1_Bs2MuMuLinesBs2KKLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo2_Bs2MuMuLinesBs2KKLTUBLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2KKLTUBLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo2_Bs2MuMuLinesBs2KKLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo3_Bs2MuMuLinesBs2KKLTUBLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2KKLTUBLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo3_Bs2MuMuLinesBs2KKLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo4_Bs2MuMuLinesBs2KKLTUBLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2KKLTUBLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo4_Bs2MuMuLinesBs2KKLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo5_Bs2MuMuLinesBs2KKLTUBLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2KKLTUBLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo5_Bs2MuMuLinesBs2KKLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo6_Bs2MuMuLinesBs2KKLTUBLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2KKLTUBLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo6_Bs2MuMuLinesBs2KKLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo7_Bs2MuMuLinesBs2KKLTUBLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2KKLTUBLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo7_Bs2MuMuLinesBs2KKLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo8_Bs2MuMuLinesBs2KKLTUBLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2KKLTUBLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo8_Bs2MuMuLinesBs2KKLTUBLine/Particles |

**AddRelatedInfo/RelatedInfo9_Bs2MuMuLinesBs2KKLTUBLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2KKLTUBLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo9_Bs2MuMuLinesBs2KKLTUBLine/Particles |
