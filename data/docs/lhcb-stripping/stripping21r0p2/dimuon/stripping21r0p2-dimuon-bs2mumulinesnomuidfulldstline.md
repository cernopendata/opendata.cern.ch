[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBs2MuMuLinesNoMuIDFullDSTLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/Bs2MuMuLinesNoMuIDFullDSTLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT1           | None                                         |
| HLT2           | None                                         |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionDimuon

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamDimuonBadEvent') & ~ALG_PASSED('StrippingStreamDimuonBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsMuons

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsMuons/Particles',True) |

CombineParticles/Bs2MuMuLinesNoMuIDFullDSTLine

|                  |                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsMuons](./stripping21r0p2-commonparticles-stdnopidsmuons)' ]                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 9 )&(TRCHI2DOF \< 4) & (0.5 9 )&(TRCHI2DOF \< 4) & (0.5                                                        |
| CombinationCut   | (ADAMASS('B_s0')\<500\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 500\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 121)& (BPVIPCHI2()\< 25) & (BPVLTIME()\<13.248\*ps)& (PT \> 350\*MeV) |
| DecayDescriptor  | B_s0 -\> mu+ mu-                                                                                                                                             |
| DecayDescriptors | [ 'B_s0 -\> mu+ mu-' ]                                                                                                                                     |
| Output           | Phys/Bs2MuMuLinesNoMuIDFullDSTLine/Particles                                                                                                                 |

AddRelatedInfo/RelatedInfo1_Bs2MuMuLinesNoMuIDFullDSTLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesNoMuIDFullDSTLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo1_Bs2MuMuLinesNoMuIDFullDSTLine/Particles |

AddRelatedInfo/RelatedInfo2_Bs2MuMuLinesNoMuIDFullDSTLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesNoMuIDFullDSTLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo2_Bs2MuMuLinesNoMuIDFullDSTLine/Particles |

AddRelatedInfo/RelatedInfo3_Bs2MuMuLinesNoMuIDFullDSTLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesNoMuIDFullDSTLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo3_Bs2MuMuLinesNoMuIDFullDSTLine/Particles |

AddRelatedInfo/RelatedInfo4_Bs2MuMuLinesNoMuIDFullDSTLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesNoMuIDFullDSTLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo4_Bs2MuMuLinesNoMuIDFullDSTLine/Particles |

AddRelatedInfo/RelatedInfo5_Bs2MuMuLinesNoMuIDFullDSTLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesNoMuIDFullDSTLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo5_Bs2MuMuLinesNoMuIDFullDSTLine/Particles |

AddRelatedInfo/RelatedInfo6_Bs2MuMuLinesNoMuIDFullDSTLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesNoMuIDFullDSTLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo6_Bs2MuMuLinesNoMuIDFullDSTLine/Particles |

AddRelatedInfo/RelatedInfo7_Bs2MuMuLinesNoMuIDFullDSTLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesNoMuIDFullDSTLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo7_Bs2MuMuLinesNoMuIDFullDSTLine/Particles |

AddRelatedInfo/RelatedInfo8_Bs2MuMuLinesNoMuIDFullDSTLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesNoMuIDFullDSTLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo8_Bs2MuMuLinesNoMuIDFullDSTLine/Particles |

AddRelatedInfo/RelatedInfo9_Bs2MuMuLinesNoMuIDFullDSTLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesNoMuIDFullDSTLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo9_Bs2MuMuLinesNoMuIDFullDSTLine/Particles |

AddRelatedInfo/RelatedInfo10_Bs2MuMuLinesNoMuIDFullDSTLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesNoMuIDFullDSTLine' ]                 |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo10_Bs2MuMuLinesNoMuIDFullDSTLine/Particles |
