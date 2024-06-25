[[stripping21 lines]](./stripping21-index)

# StrippingDisplVerticesLinesJetSingleLowMass

## Properties:

|                |                                                   |
|----------------|---------------------------------------------------|
| OutputLocation | Phys/DisplVerticesLinesJetSingleLowMass/Particles |
| Postscale      | 1.0000000                                         |
| HLT            | None                                              |
| Prescale       | 1.0000000                                         |
| L0DU           | None                                              |
| ODIN           | None                                              |

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

FilterDesktop/DisplVerticesLinesJetSingleLowMassSelectionVertices

|                 |                                                                                                                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ~ISBASIC ) & ( ~INMATTER ) & ( MAXFRACTENERGYINSINGLETRACK \< 0.8 ) & ( MM \> 0.0 ) & ( NDAUGS \>= 5 ) & ( SUMPT \> 10000.0 ) & ( FRACTDAUGHTERTRACKSWITHUPSTREAMHIT \< 0.49 ) & ( ENDVERTEXRHO \> 0.4 ) |
| Inputs          | [ 'Phys/DisplVerticesLinesWithVeloCandidates' ]                                                                                                                                                          |
| DecayDescriptor | ~chi_10                                                                                                                                                                                                    |
| Output          | Phys/DisplVerticesLinesJetSingleLowMassSelectionVertices/Particles                                                                                                                                         |

DisplacedVertexJetCandidateMakerS20p3/DisplVerticesLinesJetSingleLowMassSelectionJets

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesJetSingleLowMassSelectionVertices' ] |
| DecayDescriptor | None                                                             |
| Output          | Phys/DisplVerticesLinesJetSingleLowMassSelectionJets/Particles   |

FilterDesktop/DisplVerticesLinesJetSingleLowMass

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Code            | ISLLP & ( MM \> 0.0 )                                        |
| Inputs          | [ 'Phys/DisplVerticesLinesJetSingleLowMassSelectionJets' ] |
| DecayDescriptor | ~chi_10                                                      |
| Output          | Phys/DisplVerticesLinesJetSingleLowMass/Particles            |

AddRelatedInfo/RelatedInfo1_DisplVerticesLinesJetSingleLowMass

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesJetSingleLowMass' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo1_DisplVerticesLinesJetSingleLowMass/Particles |
