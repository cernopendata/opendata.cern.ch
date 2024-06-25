[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2XTau_TauMu_SameSign_TOSLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/B2XTau_TauMu_SameSign_TOSLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT            | None                                         |
| Prescale       | 0.50000000                                   |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightDetachedTau3pi_Particles

|      |                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightDetachedTau3pi](./stripping21r1-commonparticles-stdtightdetachedtau3pi)/Particles')\>0 |

FilterDesktop/B2XTau_TauFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (PT \> 0\*MeV)                                                                                |
| Inputs          | [ 'Phys/[StdTightDetachedTau3pi](./stripping21r1-commonparticles-stdtightdetachedtau3pi)' ] |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/B2XTau_TauFilter/Particles                                                               |

LoKi::VoidFilter/SelFilterPhys_StdTightMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightMuons](./stripping21r1-commonparticles-stdtightmuons)/Particles')\>0 |

FilterDesktop/MuonsForB2XTau

|                 |                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 6000\*MeV) & (PT \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.3) & (HASMUON) & (PIDmu \> 0) |
| Inputs          | [ 'Phys/[StdTightMuons](./stripping21r1-commonparticles-stdtightmuons)' ]                                                            |
| DecayDescriptor | None                                                                                                                                   |
| Output          | Phys/MuonsForB2XTau/Particles                                                                                                          |

CombineParticles/B2XTau_TauMuSS

|                  |                                                                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2XTau_TauFilter' , 'Phys/MuonsForB2XTau' ]                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                                                                                                                                      |
| CombinationCut   | (APT \> 1900\*MeV) & (AM \> 2000\*MeV) & (AM \< 7000\*MeV)                                                                                                                                                                            |
| MotherCut        | ((CHILD(BPVVDCHI2,1)) \< 4000) & (MIPCHI2DV(PRIMARY) \< 200) & (BPVVD \< 35) & (PT \> 5000\*MeV) & (sumpt \>2500\*MeV) & ((CHILD(VFASPF(VCHI2),1)) \< 12) & (in_range(0\*MeV,MCOR,10000\*MeV)) &((CHILD(MIPCHI2DV(PRIMARY),1)) \> 50) |
| DecayDescriptor  | None                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[B0 -\> tau+ mu+]cc' ]                                                                                                                                                                                                         |
| Output           | Phys/B2XTau_TauMuSS/Particles                                                                                                                                                                                                         |

TisTosParticleTagger/B2XTau_TauMu_SameSign_TOSLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMuSS' ]                       |
| DecayDescriptor | None                                              |
| Output          | Phys/B2XTau_TauMu_SameSign_TOSLine/Particles      |
| TisTosSpecs     | { 'Hlt2(TopoMu\|SingleMuon).\*Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_B2XTau_TauMu_SameSign_TOSLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_SameSign_TOSLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo1_B2XTau_TauMu_SameSign_TOSLine/Particles |

AddRelatedInfo/RelatedInfo2_B2XTau_TauMu_SameSign_TOSLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_SameSign_TOSLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo2_B2XTau_TauMu_SameSign_TOSLine/Particles |

AddRelatedInfo/RelatedInfo3_B2XTau_TauMu_SameSign_TOSLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_SameSign_TOSLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo3_B2XTau_TauMu_SameSign_TOSLine/Particles |

AddRelatedInfo/RelatedInfo4_B2XTau_TauMu_SameSign_TOSLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_SameSign_TOSLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo4_B2XTau_TauMu_SameSign_TOSLine/Particles |

AddRelatedInfo/RelatedInfo5_B2XTau_TauMu_SameSign_TOSLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_SameSign_TOSLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo5_B2XTau_TauMu_SameSign_TOSLine/Particles |

AddRelatedInfo/RelatedInfo6_B2XTau_TauMu_SameSign_TOSLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_SameSign_TOSLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo6_B2XTau_TauMu_SameSign_TOSLine/Particles |

AddRelatedInfo/RelatedInfo7_B2XTau_TauMu_SameSign_TOSLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2XTau_TauMu_SameSign_TOSLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo7_B2XTau_TauMu_SameSign_TOSLine/Particles |
