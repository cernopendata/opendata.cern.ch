[[stripping21r1 lines]](./stripping21r1-index)

# StrippingSingleTrackTISLowLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/SingleTrackTISLowLine/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 0.010000000                          |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

CheckPV/checkPVmin0

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsMuons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsMuons](./stripping21r1-commonparticles-stdallnopidsmuons)/Particles')\>0 |

FilterDesktop/SingleTrackTISNoPIDsLow

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            |                                                                                     |
| Inputs          | [ 'Phys/[StdAllNoPIDsMuons](./stripping21r1-commonparticles-stdallnopidsmuons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/SingleTrackTISNoPIDsLow/Particles                                              |

TisTosParticleTagger/SingleTrackTISHlt1TISLow

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/SingleTrackTISNoPIDsLow' ]    |
| DecayDescriptor | None                                    |
| Output          | Phys/SingleTrackTISHlt1TISLow/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TIS' : 0 }           |

TisTosParticleTagger/SingleTrackTISLowLine

|                 |                                       |
|-----------------|---------------------------------------|
| Inputs          | [ 'Phys/SingleTrackTISHlt1TISLow' ] |
| DecayDescriptor | None                                  |
| Output          | Phys/SingleTrackTISLowLine/Particles  |
| TisTosSpecs     | { 'Hlt2.\*Decision%TIS' : 0 }         |
