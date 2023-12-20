[[stripping21 lines]](./stripping21-index)

# StrippingDisplVerticesLinesDouble

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/DisplVerticesLinesDouble/Particles |
| Postscale      | 1.0000000                               |
| HLT            | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

CombineParticles/DisplVerticesLinesDouble

|                  |                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DisplVerticesLinesWithVeloCandidates' ]                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , '~chi_10' : '( ~ISBASIC )\n & ( MAXFRACTENERGYINSINGLETRACK \< 0.8 )\n & ( MM \> 3000.0 )\n & ( NDAUGS \>= 6 )\n & ( SUMPT \> 3000.0 )\n & ( FRACTDAUGHTERTRACKSWITHUPSTREAMHIT \< 0.49 )\n & ( ENDVERTEXRHO \> 0.6 )' } |
| CombinationCut   | ( AHASCHILD( ~INMATTER ) ) & ( AHASCHILD( MM \> 3000.0 ) )                                                                                                                                                                              |
| MotherCut        | ALL                                                                                                                                                                                                                                     |
| DecayDescriptor  | H_10 -\> ~chi_10 ~chi_10                                                                                                                                                                                                                |
| DecayDescriptors | [ 'H_10 -\> ~chi_10 ~chi_10' ]                                                                                                                                                                                                        |
| Output           | Phys/DisplVerticesLinesDouble/Particles                                                                                                                                                                                                 |

AddRelatedInfo/RelatedInfo1_DisplVerticesLinesDouble

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesDouble' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_DisplVerticesLinesDouble/Particles |
