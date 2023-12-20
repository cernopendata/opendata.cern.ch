[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2XTauZVTOP_High_Line

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2XTauZVTOP_High_Line/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsForB2XTauZVTOP

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \>25) & (TRGHOSTPROB \< 0.3)                            |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/PionsForB2XTauZVTOP/Particles                                          |

TopoTauAlg/B2XTauZVTOP_IncTopoVtxFor

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/PionsForB2XTauZVTOP' ]         |
| DecayDescriptor | None                                     |
| Output          | Phys/B2XTauZVTOP_IncTopoVtxFor/Particles |

FilterDesktop/B2XTauZVTOP_High_Line

|                 |                                        |
|-----------------|----------------------------------------|
| Code            | (M \> 50000) & (BPVVDZ \> 1.0\*mm)     |
| Inputs          | [ 'Phys/B2XTauZVTOP_IncTopoVtxFor' ] |
| DecayDescriptor | None                                   |
| Output          | Phys/B2XTauZVTOP_High_Line/Particles   |

AddRelatedInfo/RelatedInfo1_B2XTauZVTOP_High_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_High_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_B2XTauZVTOP_High_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2XTauZVTOP_High_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_High_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_B2XTauZVTOP_High_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2XTauZVTOP_High_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_High_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_B2XTauZVTOP_High_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2XTauZVTOP_High_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_High_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo4_B2XTauZVTOP_High_Line/Particles |

AddRelatedInfo/RelatedInfo5_B2XTauZVTOP_High_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_High_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo5_B2XTauZVTOP_High_Line/Particles |

AddRelatedInfo/RelatedInfo6_B2XTauZVTOP_High_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_High_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo6_B2XTauZVTOP_High_Line/Particles |

AddRelatedInfo/RelatedInfo7_B2XTauZVTOP_High_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_High_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo7_B2XTauZVTOP_High_Line/Particles |
