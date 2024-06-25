[[stripping21 lines]](./stripping21-index)

# StrippingBu2MuNuControlLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/Bu2MuNuControlLine/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 0.015000000                       |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqBu2MuNuControlLine

LoKi::VoidFilter/SelFilterPhys_Bu2MuNu_MuForBu2MuNuControl_Particles

|      |                                                           |
|------|-----------------------------------------------------------|
| Code | CONTAINS('Phys/Bu2MuNu_MuForBu2MuNuControl/Particles')\>0 |

FilterDesktop/Bu2MuNuControlLine

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | ALL                                      |
| Inputs          | [ 'Phys/Bu2MuNu_MuForBu2MuNuControl' ] |
| DecayDescriptor | None                                     |
| Output          | Phys/Bu2MuNuControlLine/Particles        |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

AddRelatedInfo/RelatedInfo1_Bu2MuNuControlLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuControlLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo1_Bu2MuNuControlLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2MuNuControlLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuControlLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo2_Bu2MuNuControlLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2MuNuControlLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuControlLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo3_Bu2MuNuControlLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2MuNuControlLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuControlLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo4_Bu2MuNuControlLine/Particles |

AddRelatedInfo/RelatedInfo5_Bu2MuNuControlLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuControlLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo5_Bu2MuNuControlLine/Particles |

AddRelatedInfo/RelatedInfo6_Bu2MuNuControlLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuControlLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo6_Bu2MuNuControlLine/Particles |

AddRelatedInfo/RelatedInfo7_Bu2MuNuControlLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuControlLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo7_Bu2MuNuControlLine/Particles |

AddRelatedInfo/RelatedInfo8_Bu2MuNuControlLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuControlLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo8_Bu2MuNuControlLine/Particles |

AddRelatedInfo/RelatedInfo9_Bu2MuNuControlLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuControlLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo9_Bu2MuNuControlLine/Particles |

AddRelatedInfo/RelatedInfo10_Bu2MuNuControlLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuControlLine' ]                 |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo10_Bu2MuNuControlLine/Particles |
