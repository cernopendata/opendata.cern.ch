[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD02KKForPromptCharm

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/D02KKForPromptCharm/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 0.10000000                         |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNKaons](./stripping21r1-commonparticles-stdlooseannkaons)/Particles')\>0 |

FilterDesktop/SelKaonForPromptCharm

|                 |                                                                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNk \> 0.1 ) & ( MIPCHI2DV() \> 9 ) |
| Inputs          | [ 'Phys/[StdLooseANNKaons](./stripping21r1-commonparticles-stdlooseannkaons)' ]                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                |
| Output          | Phys/SelKaonForPromptCharm/Particles                                                                                                                                                                |

CombineParticles/D02KKForPromptCharm

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' ]                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                       |
| CombinationCut   | ( ADAMASS('D0') \< 85 \* MeV ) & ( APT \> 950.0 )                                                  |
| MotherCut        | ( chi2vx \< 9 ) & ( PT \> 1000.0 ) & ( ADMASS('D0') \< 75 \* MeV ) & ( ctau \> 100 \* micrometer ) |
| DecayDescriptor  | D0 -\> K- K+                                                                                       |
| DecayDescriptors | [ 'D0 -\> K- K+' ]                                                                               |
| Output           | Phys/D02KKForPromptCharm/Particles                                                                 |
