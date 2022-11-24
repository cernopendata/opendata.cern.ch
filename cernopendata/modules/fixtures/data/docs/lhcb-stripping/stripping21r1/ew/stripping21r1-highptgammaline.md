[[stripping21r1 lines]](./stripping21r1-index)

# StrippingHighPtGammaLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/HighPtGammaLine/Particles |
| Postscale      | 1.0000000                      |
| HLT            | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLoosePhotons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePhotons](./stripping21r1-stdloosephotons) /Particles')\>0 |

**FilterDesktop/selHighPtGammaPhoton**

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | (PT\>12.5\*GeV) & (PPINFO(LHCb.ProtoParticle.CaloTrMatch,-1)\>25) |
| Inputs          | [ 'Phys/ [StdLoosePhotons](./stripping21r1-stdloosephotons) ' ] |
| DecayDescriptor | None                                                              |
| Output          | Phys/selHighPtGammaPhoton/Particles                               |

**LoKi::VoidFilter/SelFilterPhys_StdJets_Particles**

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdJets](./stripping21r1-stdjets) /Particles')\>0 |

**CombineParticles/SelHighPtGammaDiJet**

|                  |                                                       |
|------------------|-------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdJets](./stripping21r1-stdjets) ' ]     |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : ' (PT \> 12.5 \* GeV ) ' } |
| CombinationCut   | AALLSAMEBPV                                           |
| MotherCut        | ALL                                                   |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet                              |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet' ]                      |
| Output           | Phys/SelHighPtGammaDiJet/Particles                    |

**CombineParticles/HighPtGammaLine**

|                  |                                                                |
|------------------|----------------------------------------------------------------|
| Inputs           | [ 'Phys/SelHighPtGammaDiJet' , 'Phys/selHighPtGammaPhoton' ] |
| DaughtersCuts    | { '' : 'ALL' , 'H_10' : 'ALL' , 'gamma' : 'ALL' }              |
| CombinationCut   | ATRUE                                                          |
| MotherCut        | ALL                                                            |
| DecayDescriptor  | H_20 -\> H_10 gamma                                            |
| DecayDescriptors | [ 'H_20 -\> H_10 gamma' ]                                    |
| Output           | Phys/HighPtGammaLine/Particles                                 |
