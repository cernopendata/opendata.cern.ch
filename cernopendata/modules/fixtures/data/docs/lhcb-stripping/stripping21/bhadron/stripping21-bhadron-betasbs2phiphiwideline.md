[[stripping21 lines]](./stripping21-index)

# StrippingBetaSBs2PhiPhiWideLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/BetaSBs2PhiPhiWideLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 0.15000000                            |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21-commonparticles-stdalllooseannkaons)/Particles')\>0 |

CombineParticles/BetaSBs2PhiPhiWide_LoosePhi2KK

|                  |                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21-commonparticles-stdalllooseannkaons)' ]                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>0.0)' , 'K-' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>0.0)' } |
| CombinationCut   | (AM\<(1090+30)\*MeV)                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<15)&(MM\<1090\*MeV)                                                                                                                             |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                                                                                                                  |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                                                          |
| Output           | Phys/BetaSBs2PhiPhiWide_LoosePhi2KK/Particles                                                                                                                        |

CombineParticles/BetaSBs2PhiPhiWideLine

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSBs2PhiPhiWide_LoosePhi2KK' ]                                    |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : '(PT\>0\*MeV)' }                                  |
| CombinationCut   | (ADAMASS('B_s0')\<((300+30)\*MeV))&(ACHILD(PT,1)\*ACHILD(PT,2)\>1.2\*GeV\*GeV) |
| MotherCut        | (BPVDIRA \> 0.999) & (VFASPF(VCHI2/VDOF)\<15)&(ADMASS('B_s0')\<300\*MeV)       |
| DecayDescriptor  | B_s0 -\> phi(1020) phi(1020)                                                   |
| DecayDescriptors | [ 'B_s0 -\> phi(1020) phi(1020)' ]                                           |
| Output           | Phys/BetaSBs2PhiPhiWideLine/Particles                                          |

AddRelatedInfo/RelatedInfo1_BetaSBs2PhiPhiWideLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/BetaSBs2PhiPhiWideLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_BetaSBs2PhiPhiWideLine/Particles |

AddRelatedInfo/RelatedInfo2_BetaSBs2PhiPhiWideLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/BetaSBs2PhiPhiWideLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_BetaSBs2PhiPhiWideLine/Particles |

AddRelatedInfo/RelatedInfo3_BetaSBs2PhiPhiWideLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/BetaSBs2PhiPhiWideLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_BetaSBs2PhiPhiWideLine/Particles |

AddRelatedInfo/RelatedInfo4_BetaSBs2PhiPhiWideLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/BetaSBs2PhiPhiWideLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_BetaSBs2PhiPhiWideLine/Particles |

AddRelatedInfo/RelatedInfo5_BetaSBs2PhiPhiWideLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/BetaSBs2PhiPhiWideLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo5_BetaSBs2PhiPhiWideLine/Particles |
