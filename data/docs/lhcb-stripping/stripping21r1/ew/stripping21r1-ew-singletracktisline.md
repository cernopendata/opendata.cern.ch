[[stripping21r1 lines]](./stripping21r1-index)

# StrippingSingleTrackTISLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/SingleTrackTISLine/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 0.10000000                        |
| L0DU           | None                              |
| ODIN           | None                              |

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

FilterDesktop/SingleTrackTISNoPIDs

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            |                                                                                     |
| Inputs          | [ 'Phys/[StdAllNoPIDsMuons](./stripping21r1-commonparticles-stdallnopidsmuons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/SingleTrackTISNoPIDs/Particles                                                 |

TisTosParticleTagger/SingleTrackTISHlt1TIS

|                 |                                      |
|-----------------|--------------------------------------|
| Inputs          | [ 'Phys/SingleTrackTISNoPIDs' ]    |
| DecayDescriptor | None                                 |
| Output          | Phys/SingleTrackTISHlt1TIS/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TIS' : 0 }        |

TisTosParticleTagger/SingleTrackTISLine

|                 |                                    |
|-----------------|------------------------------------|
| Inputs          | [ 'Phys/SingleTrackTISHlt1TIS' ] |
| DecayDescriptor | None                               |
| Output          | Phys/SingleTrackTISLine/Particles  |
| TisTosSpecs     | { 'Hlt2.\*Decision%TIS' : 0 }      |
