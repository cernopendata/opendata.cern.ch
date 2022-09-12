[[stripping21 lines]](./stripping21-index)

# StrippingHighPtGammaLooseLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/HighPtGammaLooseLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 0.10000000                          |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLoosePhotons_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePhotons](./stripping21-stdloosephotons) /Particles')\>0 |

**FilterDesktop/selHighPtGammaPhotonLoose**

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Code            | (PT\>7.5\*GeV) & (PPINFO(LHCb.ProtoParticle.CaloTrMatch,-1)\>20) |
| Inputs          | [ 'Phys/ [StdLoosePhotons](./stripping21-stdloosephotons) ' ]  |
| DecayDescriptor | None                                                             |
| Output          | Phys/selHighPtGammaPhotonLoose/Particles                         |

**LoKi::VoidFilter/SelFilterPhys_StdJets_Particles**

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdJets](./stripping21-stdjets) /Particles')\>0 |

**CombineParticles/SelHighPtGammaDiJetLoose**

|                  |                                                      |
|------------------|------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdJets](./stripping21-stdjets) ' ]      |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : ' (PT \> 7.5 \* GeV ) ' } |
| CombinationCut   | AALLSAMEBPV                                          |
| MotherCut        | ALL                                                  |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet                             |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet' ]                     |
| Output           | Phys/SelHighPtGammaDiJetLoose/Particles              |

**CombineParticles/HighPtGammaLooseLine**

|                  |                                                                          |
|------------------|--------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelHighPtGammaDiJetLoose' , 'Phys/selHighPtGammaPhotonLoose' ] |
| DaughtersCuts    | { '' : 'ALL' , 'H_10' : 'ALL' , 'gamma' : 'ALL' }                        |
| CombinationCut   | ATRUE                                                                    |
| MotherCut        | ALL                                                                      |
| DecayDescriptor  | H_20 -\> H_10 gamma                                                      |
| DecayDescriptors | [ 'H_20 -\> H_10 gamma' ]                                              |
| Output           | Phys/HighPtGammaLooseLine/Particles                                      |
