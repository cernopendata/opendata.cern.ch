[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDisplVerticesLinesCharmHLT

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/DisplVerticesLinesCharmHLT/Particles    |
| Postscale      | 1.0000000                                    |
| HLT            | HLT_PASS('Hlt2CharmHadD02HH_D02KPiDecision') |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

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

FilterDesktop/DisplVerticesLinesCharmHLT

|                 |                                                                                                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ~ISBASIC ) & ( MAXFRACTENERGYINSINGLETRACK \< 10.0 ) & ( MM \> 6000.0 ) & ( NDAUGS \>= 6 ) & ( SUMPT \> 3000.0 ) & ( FRACTDAUGHTERTRACKSWITHUPSTREAMHIT \< 10.0 ) & ( ENDVERTEXRHO \> 0.6 ) |
| Inputs          | [ 'Phys/DisplVerticesLinesWithVeloCandidates' ]                                                                                                                                             |
| DecayDescriptor | ~chi_10                                                                                                                                                                                       |
| Output          | Phys/DisplVerticesLinesCharmHLT/Particles                                                                                                                                                     |

AddRelatedInfo/RelatedInfo1_DisplVerticesLinesCharmHLT

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesCharmHLT' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_DisplVerticesLinesCharmHLT/Particles |
