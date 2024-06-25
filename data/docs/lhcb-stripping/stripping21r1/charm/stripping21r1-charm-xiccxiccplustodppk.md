[[stripping21r1 lines]](./stripping21r1-index)

# StrippingXiccXiccPlusToDpPK

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/XiccXiccPlusToDpPK/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

LoKi::VoidFilter/StrippingXiccXiccPlusToDpPKVOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDplus2KPiPi_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDplus2KPiPi](./stripping21r1-commonparticles-stdloosedplus2kpipi)/Particles')\>0 |

FilterDesktop/XiccFilteredDplus2KPiPi

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (ADMASS('D+')\<75.0)& (BPVVDCHI2\>100.0)                                                |
| Inputs          | [ 'Phys/[StdLooseDplus2KPiPi](./stripping21r1-commonparticles-stdloosedplus2kpipi)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/XiccFilteredDplus2KPiPi/Particles                                                  |

TisTosParticleTagger/XiccdplusTisTos

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XiccFilteredDplus2KPiPi' ]          |
| DecayDescriptor | None                                          |
| Output          | Phys/XiccdplusTisTos/Particles                |
| TisTosSpecs     | { 'Hlt2.\*CharmHadD2HHH.\*Decision%TOS' : 0 } |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseProtons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseProtons](./stripping21r1-commonparticles-stdalllooseprotons)/Particles')\>0 |

FilterDesktop/XiccFilteredProtons

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (HASRICH)&(PIDp-PIDpi\>5.0)& (HASRICH)&(PIDp-PIDK\>0.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0) |
| Inputs          | [ 'Phys/[StdAllLooseProtons](./stripping21r1-commonparticles-stdalllooseprotons)' ]                                           |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/XiccFilteredProtons/Particles                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21r1-commonparticles-stdallloosekaons)/Particles')\>0 |

FilterDesktop/XiccFilteredKaons

|                 |                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<5.0)& (P\>2000.0)& (HASRICH)&(PIDK-PIDpi\>5.0)& (PT\>250.0)& (MIPCHI2DV(PRIMARY)\>-1.0) |
| Inputs          | [ 'Phys/[StdAllLooseKaons](./stripping21r1-commonparticles-stdallloosekaons)' ]                   |
| DecayDescriptor | None                                                                                                |
| Output          | Phys/XiccFilteredKaons/Particles                                                                    |

CombineParticles/XiccXiccPlusToDpPK

|                  |                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XiccFilteredKaons' , 'Phys/XiccFilteredProtons' , 'Phys/XiccdplusTisTos' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' } |
| CombinationCut   | (AM\<4000.0)& (APT\>2000.0)& (ADOCAMAX('')\<0.5)                                                          |
| MotherCut        | (VFASPF(VCHI2)\<30.0)&(CHILD(VFASPF(VZ),1) - VFASPF(VZ) \> 0.01)& (BPVVDCHI2 \> -1.0)& (BPVDIRA \> 0.0)   |
| DecayDescriptor  | [Xi_cc+ -\> D+ p+ K-]cc                                                                                 |
| DecayDescriptors | [ '[Xi_cc+ -\> D+ p+ K-]cc' ]                                                                         |
| Output           | Phys/XiccXiccPlusToDpPK/Particles                                                                         |
