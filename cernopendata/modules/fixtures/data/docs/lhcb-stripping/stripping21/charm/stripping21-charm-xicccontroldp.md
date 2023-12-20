[[stripping21 lines]](./stripping21-index)

# StrippingXiccControlDp

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/XiccControlDp/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 0.0010000000                 |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingXiccControlDpVOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDplus2KPiPi_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDplus2KPiPi](./stripping21-commonparticles-stdloosedplus2kpipi)/Particles')\>0 |

FilterDesktop/XiccFilteredDplus2KPiPi

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (ADMASS('D+')\<75.0)& (BPVVDCHI2\>100.0)                                              |
| Inputs          | [ 'Phys/[StdLooseDplus2KPiPi](./stripping21-commonparticles-stdloosedplus2kpipi)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/XiccFilteredDplus2KPiPi/Particles                                                |

TisTosParticleTagger/XiccControlDp

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XiccFilteredDplus2KPiPi' ]          |
| DecayDescriptor | None                                          |
| Output          | Phys/XiccControlDp/Particles                  |
| TisTosSpecs     | { 'Hlt2.\*CharmHadD2HHH.\*Decision%TOS' : 0 } |
