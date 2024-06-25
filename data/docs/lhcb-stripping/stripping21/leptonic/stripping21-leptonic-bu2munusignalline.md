[[stripping21 lines]](./stripping21-index)

# StrippingBu2MuNuSignalLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/Bu2MuNuSignalLine/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

LoKi::VoidFilter/StrippingBu2MuNuSignalLineVOIDFilter

|      |                                      |
|------|--------------------------------------|
| Code | ( CONTAINS('Rec/Track/Best')\< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqBu2MuNuSignalLine

LoKi::VoidFilter/SelFilterPhys_Bu2MuNu_MuForBu2MuNu_Particles

|      |                                                    |
|------|----------------------------------------------------|
| Code | CONTAINS('Phys/Bu2MuNu_MuForBu2MuNu/Particles')\>0 |

FilterDesktop/Bu2MuNuSignalLine

|                 |                                   |
|-----------------|-----------------------------------|
| Code            | ALL                               |
| Inputs          | [ 'Phys/Bu2MuNu_MuForBu2MuNu' ] |
| DecayDescriptor | None                              |
| Output          | Phys/Bu2MuNuSignalLine/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

AddRelatedInfo/RelatedInfo1_Bu2MuNuSignalLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuSignalLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo1_Bu2MuNuSignalLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2MuNuSignalLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuSignalLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo2_Bu2MuNuSignalLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2MuNuSignalLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuSignalLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo3_Bu2MuNuSignalLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2MuNuSignalLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuSignalLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo4_Bu2MuNuSignalLine/Particles |

AddRelatedInfo/RelatedInfo5_Bu2MuNuSignalLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuSignalLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo5_Bu2MuNuSignalLine/Particles |

AddRelatedInfo/RelatedInfo6_Bu2MuNuSignalLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuSignalLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo6_Bu2MuNuSignalLine/Particles |

AddRelatedInfo/RelatedInfo7_Bu2MuNuSignalLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuSignalLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo7_Bu2MuNuSignalLine/Particles |

AddRelatedInfo/RelatedInfo8_Bu2MuNuSignalLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuSignalLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo8_Bu2MuNuSignalLine/Particles |

AddRelatedInfo/RelatedInfo9_Bu2MuNuSignalLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuSignalLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo9_Bu2MuNuSignalLine/Particles |

AddRelatedInfo/RelatedInfo10_Bu2MuNuSignalLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2MuNuSignalLine' ]                 |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo10_Bu2MuNuSignalLine/Particles |
