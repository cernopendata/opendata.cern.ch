[[stripping21 lines]](./stripping21-index)

# StrippingXiccControlD0

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/XiccControlD0/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 0.0010000000                 |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingXiccControlD0VOIDFilter

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Code | (recSummary (LHCb.RecSummary.nLongTracks, 'Rec/Track/Long') \< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseD02KPi_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseD02KPi](./stripping21-commonparticles-stdloosed02kpi)/Particles')\>0 |

FilterDesktop/XiccFilteredD02KPi

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('D0')\<75.0)& (BPVVDCHI2\>64.0)                                     |
| Inputs          | [ 'Phys/[StdLooseD02KPi](./stripping21-commonparticles-stdloosed02kpi)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/XiccFilteredD02KPi/Particles                                           |

TisTosParticleTagger/XiccControlD0

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/XiccFilteredD02KPi' ]             |
| DecayDescriptor | None                                        |
| Output          | Phys/XiccControlD0/Particles                |
| TisTosSpecs     | { 'Hlt2.\*CharmHadD02.\*Decision%TOS' : 0 } |
