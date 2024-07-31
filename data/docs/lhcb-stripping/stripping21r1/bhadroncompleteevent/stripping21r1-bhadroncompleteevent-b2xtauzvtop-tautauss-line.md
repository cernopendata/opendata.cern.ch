[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2XTauZVTOP_TauTauSS_Line

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/B2XTauZVTOP_TauTauSS_Line/Particles |
| Postscale      | 1.0000000                                |
| HLT            | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

FilterDesktop/B2XTauZVTOP_TauFilter

|                 |                                        |
|-----------------|----------------------------------------|
| Code            | (BPVVDZ\>5.0\*mm) & (BPVDIRA\>0.99)    |
| Inputs          | [ 'Phys/B2XTauZVTOP_IncTopoVtxFor' ] |
| DecayDescriptor | None                                   |
| Output          | Phys/B2XTauZVTOP_TauFilter/Particles   |

CombineParticles/B2XTauZVTOP_TauTauSS_Line

|                  |                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2XTauZVTOP_TauFilter' ]                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                                                        |
| CombinationCut   | (APT \> 1900\*MeV) & (AM \> 2000\*MeV) & (AM \< 7000\*MeV)                                                              |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 90) & (BPVVDCHI2 \> 225) & (BPVVD \< 90) & (PT \> 2000\*MeV) & (in_range(0\*MeV,MCOR,10000\*MeV)) |
| DecayDescriptor  | None                                                                                                                    |
| DecayDescriptors | [ '[B0 -\> tau+ tau+]cc' ]                                                                                          |
| Output           | Phys/B2XTauZVTOP_TauTauSS_Line/Particles                                                                                |

AddRelatedInfo/RelatedInfo1_B2XTauZVTOP_TauTauSS_Line

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_TauTauSS_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo1_B2XTauZVTOP_TauTauSS_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2XTauZVTOP_TauTauSS_Line

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_TauTauSS_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo2_B2XTauZVTOP_TauTauSS_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2XTauZVTOP_TauTauSS_Line

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_TauTauSS_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo3_B2XTauZVTOP_TauTauSS_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2XTauZVTOP_TauTauSS_Line

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_TauTauSS_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo4_B2XTauZVTOP_TauTauSS_Line/Particles |

AddRelatedInfo/RelatedInfo5_B2XTauZVTOP_TauTauSS_Line

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_TauTauSS_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo5_B2XTauZVTOP_TauTauSS_Line/Particles |

AddRelatedInfo/RelatedInfo6_B2XTauZVTOP_TauTauSS_Line

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_TauTauSS_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo6_B2XTauZVTOP_TauTauSS_Line/Particles |

AddRelatedInfo/RelatedInfo7_B2XTauZVTOP_TauTauSS_Line

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTauZVTOP_TauTauSS_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo7_B2XTauZVTOP_TauTauSS_Line/Particles |
