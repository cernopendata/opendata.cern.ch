[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDForPromptCharm

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/DForPromptCharm/Particles |
| Postscale      | 1.0000000                      |
| HLT            | None                           |
| Prescale       | 0.050000000                    |
| L0DU           | None                           |
| ODIN           | None                           |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseANNPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNPions](./stripping21r1-commonparticles-stdlooseannpions)/Particles')\>0 |

FilterDesktop/SelPionForPromptCharm

|                 |                                                                                                                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNpi \> 0.1 ) & ( MIPCHI2DV() \> 9 ) |
| Inputs          | [ 'Phys/[StdLooseANNPions](./stripping21r1-commonparticles-stdlooseannpions)' ]                                                                                                                    |
| DecayDescriptor | None                                                                                                                                                                                                 |
| Output          | Phys/SelPionForPromptCharm/Particles                                                                                                                                                                 |

DaVinci::N3BodyDecays/DForPromptCharm

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                            |
| CombinationCut   | ( ADAMASS('D+') \< 65 \* MeV ) & ( APT \> 950.0 ) & ( ACHI2DOCA(1,3) \< 16 ) & ( ACHI2DOCA(2,3) \< 16 ) |
| MotherCut        | ( chi2vx \< 25 ) & ( PT \> 1000.0 ) & ( ADMASS ('D+' ) \< 55 \* MeV ) & ( ctau \> 100 \* micrometer )   |
| DecayDescriptor  | [D+ -\> K- pi+ pi+ ]cc                                                                                |
| DecayDescriptors | [ ' [D+ -\> K- pi+ pi+ ]cc' ]                                                                       |
| Output           | Phys/DForPromptCharm/Particles                                                                          |
