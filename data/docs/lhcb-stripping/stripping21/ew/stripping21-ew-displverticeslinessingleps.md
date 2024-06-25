[[stripping21 lines]](./stripping21-index)

# StrippingDisplVerticesLinesSinglePS

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/DisplVerticesLinesSinglePS/Particles |
| Postscale      | 1.0000000                                 |
| HLT            | None                                      |
| Prescale       | 0.0050000000                              |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterRec_Track_Best

|      |                               |
|------|-------------------------------|
| Code | CONTAINS('Rec/Track/Best')\>0 |

VeloEventShapeCutsS20p3/DisplVerticesLinesVeloGEC

SelectVeloTracksNotFromPVS20p3/DisplVerticesLinesVeloFilteredTracks

|        |                                                     |
|--------|-----------------------------------------------------|
| Inputs | [ 'Rec/Track/Best' ]                              |
| Output | Phys/DisplVerticesLinesVeloFilteredTracks/Particles |

PatPV3D/DisplVerticesLinesWithVeloVertexing

LLParticlesFromRecVertices/DisplVerticesLinesWithVeloCandidates

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ ]                                               |
| DecayDescriptor | None                                                |
| Output          | Phys/DisplVerticesLinesWithVeloCandidates/Particles |

FilterDesktop/DisplVerticesLinesSinglePS

|                 |                                                                                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ~ISBASIC ) & ( MAXFRACTENERGYINSINGLETRACK \< 10.0 ) & ( MM \> 3000.0 ) & ( NDAUGS \>= 5 ) & ( SUMPT \> 0.0 ) & ( FRACTDAUGHTERTRACKSWITHUPSTREAMHIT \< 10.0 ) & ( ENDVERTEXRHO \> 0.5 ) |
| Inputs          | [ 'Phys/DisplVerticesLinesWithVeloCandidates' ]                                                                                                                                          |
| DecayDescriptor | ~chi_10                                                                                                                                                                                    |
| Output          | Phys/DisplVerticesLinesSinglePS/Particles                                                                                                                                                  |

AddRelatedInfo/RelatedInfo1_DisplVerticesLinesSinglePS

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesSinglePS' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_DisplVerticesLinesSinglePS/Particles |
