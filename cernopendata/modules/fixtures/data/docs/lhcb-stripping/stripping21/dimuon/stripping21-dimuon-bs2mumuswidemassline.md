[[stripping21 lines]](./stripping21-index)

# StrippingBs2MuMusWideMassLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/Bs2MuMusWideMassLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

CombineParticles/Bs2MuMusWideMassLine

|                  |                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 9)&(TRCHI2DOF \< 3 )' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 9)&(TRCHI2DOF \< 3 )' } |
| CombinationCut   | (ADAMASS('B_s0')\<1200\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 1200\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 121)& (BPVIPCHI2()\< 25)             |
| DecayDescriptor  | B_s0 -\> mu+ mu-                                                                                                             |
| DecayDescriptors | [ 'B_s0 -\> mu+ mu-' ]                                                                                                     |
| Output           | Phys/Bs2MuMusWideMassLine/Particles                                                                                          |

AddRelatedInfo/RelatedInfo1_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo2_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo3_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo4_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo5_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo5_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo6_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo6_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo7_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo7_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo8_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo8_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo9_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo9_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo1_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo2_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo3_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo4_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo5_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo5_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo6_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo6_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo7_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo7_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo8_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo8_Bs2MuMusWideMassLine/Particles |

AddRelatedInfo/RelatedInfo9_Bs2MuMusWideMassLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusWideMassLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo9_Bs2MuMusWideMassLine/Particles |
