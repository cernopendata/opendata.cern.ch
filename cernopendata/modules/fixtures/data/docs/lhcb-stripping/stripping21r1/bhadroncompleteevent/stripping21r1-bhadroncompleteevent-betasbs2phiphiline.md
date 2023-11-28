[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSBs2PhiPhiLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/BetaSBs2PhiPhiLine/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21r1-commonparticles-stdalllooseannkaons)/Particles')\>0 |

CombineParticles/BetaSBs2PhiPhi_LoosePhi2KK

|                  |                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21r1-commonparticles-stdalllooseannkaons)' ]                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>0.0)' , 'K-' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>0.0)' } |
| CombinationCut   | (AM\<(1090+30)\*MeV)                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<15)&(ADMASS('phi(1020)')\<25\*MeV)                                                                                                              |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                                                                                                                  |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                                                          |
| Output           | Phys/BetaSBs2PhiPhi_LoosePhi2KK/Particles                                                                                                                            |

CombineParticles/BetaSBs2PhiPhiLine

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSBs2PhiPhi_LoosePhi2KK' ]                                        |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : '(PT\>0\*MeV)' }                                  |
| CombinationCut   | (ADAMASS('B_s0')\<((300+30)\*MeV))&(ACHILD(PT,1)\*ACHILD(PT,2)\>1.2\*GeV\*GeV) |
| MotherCut        | (BPVDIRA \> 0.999) & (VFASPF(VCHI2/VDOF)\<15)&(ADMASS('B_s0')\<300\*MeV)       |
| DecayDescriptor  | B_s0 -\> phi(1020) phi(1020)                                                   |
| DecayDescriptors | [ 'B_s0 -\> phi(1020) phi(1020)' ]                                           |
| Output           | Phys/BetaSBs2PhiPhiLine/Particles                                              |
