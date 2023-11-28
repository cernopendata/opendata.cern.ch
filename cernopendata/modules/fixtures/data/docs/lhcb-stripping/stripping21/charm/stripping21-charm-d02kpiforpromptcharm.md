[[stripping21 lines]](./stripping21-index)

# StrippingD02KpiForPromptCharm

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/D02KpiForPromptCharm/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 0.050000000                         |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNKaons](./stripping21-commonparticles-stdlooseannkaons)/Particles')\>0 |

FilterDesktop/SelKaonForPromptCharm

|                 |                                                                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNk \> 0.1 ) & ( MIPCHI2DV() \> 9 ) |
| Inputs          | [ 'Phys/[StdLooseANNKaons](./stripping21-commonparticles-stdlooseannkaons)' ]                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                |
| Output          | Phys/SelKaonForPromptCharm/Particles                                                                                                                                                                |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNPions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNPions](./stripping21-commonparticles-stdlooseannpions)/Particles')\>0 |

FilterDesktop/SelPionForPromptCharm

|                 |                                                                                                                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNpi \> 0.1 ) & ( MIPCHI2DV() \> 9 ) |
| Inputs          | [ 'Phys/[StdLooseANNPions](./stripping21-commonparticles-stdlooseannpions)' ]                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                                                                 |
| Output          | Phys/SelPionForPromptCharm/Particles                                                                                                                                                                 |

CombineParticles/D02KpiForPromptCharm

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                       |
| CombinationCut   | ( ADAMASS('D0') \< 85 \* MeV ) & ( APT \> 950.0 )                                                  |
| MotherCut        | ( chi2vx \< 9 ) & ( PT \> 1000.0 ) & ( ADMASS('D0') \< 75 \* MeV ) & ( ctau \> 100 \* micrometer ) |
| DecayDescriptor  | [D0 -\> K- pi+]cc                                                                                |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                        |
| Output           | Phys/D02KpiForPromptCharm/Particles                                                                |
