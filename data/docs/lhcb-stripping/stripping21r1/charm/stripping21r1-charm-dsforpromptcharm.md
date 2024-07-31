[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDsForPromptCharm

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/DsForPromptCharm/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 0.50000000                      |
| L0DU           | None                            |
| ODIN           | None                            |

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

DaVinci::N3BodyDecays/DsForPromptCharm

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }               |
| CombinationCut   | ( APT \> 950.0 ) & ( admD \| admDs ) & ( ACHI2DOCA(1,3) \< 16 ) & ( ACHI2DOCA(2,3) \< 16 ) |
| MotherCut        | ( chi2vx \< 25 ) & ( PT \> 1000.0 ) & ( dmD \| dmDs ) & ( ctau \> 100 \* micrometer )      |
| DecayDescriptor  | [D_s+ -\> K- K+ pi+ ]cc                                                                  |
| DecayDescriptors | [ ' [D_s+ -\> K- K+ pi+ ]cc' ]                                                         |
| Output           | Phys/DsForPromptCharm/Particles                                                            |
