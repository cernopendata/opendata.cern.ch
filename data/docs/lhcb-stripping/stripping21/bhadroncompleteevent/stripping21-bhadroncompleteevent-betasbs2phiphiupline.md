[[stripping21 lines]](./stripping21-index)

# StrippingBetaSBs2PhiPhiUpLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/BetaSBs2PhiPhiUpLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseANNUpKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNUpKaons](./stripping21-commonparticles-stdlooseannupkaons)/Particles')\>0 |

CombineParticles/BetaSBs2PhiPhiUp_LooseAllPhi2KK

|                  |                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21-commonparticles-stdalllooseannkaons)' , 'Phys/[StdLooseANNUpKaons](./stripping21-commonparticles-stdlooseannupkaons)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>0.0)' , 'K-' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>0.0)' }  |
| CombinationCut   | (AM\<(1090+30)\*MeV)                                                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<15)&(ADMASS('phi(1020)')\<25\*MeV)                                                                                                               |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                                                                                                                   |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                                                           |
| Output           | Phys/BetaSBs2PhiPhiUp_LooseAllPhi2KK/Particles                                                                                                                        |

CombineParticles/BetaSBs2PhiPhiUpLine

|                  |                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSBs2PhiPhiUp_LooseAllPhi2KK' ]                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : '(PT\>0\*MeV)' }                                                                                        |
| CombinationCut   | (ADAMASS('B_s0')\<((300+30)\*MeV))&(ACHILD(PT,1)\*ACHILD(PT,2)\>1.2\*GeV\*GeV)                                                       |
| MotherCut        | (INTREE( HASTRACK & ISUP ) & INTREE( HASTRACK & ISLONG )) & (BPVDIRA \> 0.999) & (VFASPF(VCHI2/VDOF)\<15)&(ADMASS('B_s0')\<300\*MeV) |
| DecayDescriptor  | B_s0 -\> phi(1020) phi(1020)                                                                                                         |
| DecayDescriptors | [ 'B_s0 -\> phi(1020) phi(1020)' ]                                                                                                 |
| Output           | Phys/BetaSBs2PhiPhiUpLine/Particles                                                                                                  |
