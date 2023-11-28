[[stripping21 lines]](./stripping21-index)

# StrippingDisplVerticesLinesJetSingleHighMass

## Properties:

|                |                                                    |
|----------------|----------------------------------------------------|
| OutputLocation | Phys/DisplVerticesLinesJetSingleHighMass/Particles |
| Postscale      | 1.0000000                                          |
| HLT            | None                                               |
| Prescale       | 1.0000000                                          |
| L0DU           | None                                               |
| ODIN           | None                                               |

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

FilterDesktop/DisplVerticesLinesJetSingleHighMassSelectionVertices

|                 |                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ~ISBASIC ) & ( ~INMATTER ) & ( MAXFRACTENERGYINSINGLETRACK \< 0.8 ) & ( MM \> 5000.0 ) & ( NDAUGS \>= 5 ) & ( SUMPT \> 7000.0 ) & ( FRACTDAUGHTERTRACKSWITHUPSTREAMHIT \< 0.49 ) & ( ENDVERTEXRHO \> 0.4 ) |
| Inputs          | [ 'Phys/DisplVerticesLinesWithVeloCandidates' ]                                                                                                                                                            |
| DecayDescriptor | ~chi_10                                                                                                                                                                                                      |
| Output          | Phys/DisplVerticesLinesJetSingleHighMassSelectionVertices/Particles                                                                                                                                          |

DisplacedVertexJetCandidateMakerS20p3/DisplVerticesLinesJetSingleHighMassSelectionJets

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesJetSingleHighMassSelectionVertices' ] |
| DecayDescriptor | None                                                              |
| Output          | Phys/DisplVerticesLinesJetSingleHighMassSelectionJets/Particles   |

FilterDesktop/DisplVerticesLinesJetSingleHighMass

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | ISLLP & ( NINTREE(ISJET) \>= 2 ) & ( MM \> 0.0 )              |
| Inputs          | [ 'Phys/DisplVerticesLinesJetSingleHighMassSelectionJets' ] |
| DecayDescriptor | ~chi_10                                                       |
| Output          | Phys/DisplVerticesLinesJetSingleHighMass/Particles            |

AddRelatedInfo/RelatedInfo1_DisplVerticesLinesJetSingleHighMass

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesJetSingleHighMass' ]                |
| DecayDescriptor | None                                                            |
| Output          | Phys/RelatedInfo1_DisplVerticesLinesJetSingleHighMass/Particles |
