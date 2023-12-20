[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD02pipiForPromptCharm

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/D02pipiForPromptCharm/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 0.10000000                           |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

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

CombineParticles/D02pipiForPromptCharm

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelPionForPromptCharm' ]                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                     |
| CombinationCut   | ( ADAMASS('D0') \< 85 \* MeV ) & ( APT \> 950.0 )                                                  |
| MotherCut        | ( chi2vx \< 9 ) & ( PT \> 1000.0 ) & ( ADMASS('D0') \< 75 \* MeV ) & ( ctau \> 100 \* micrometer ) |
| DecayDescriptor  | D0 -\> pi- pi+                                                                                     |
| DecayDescriptors | [ 'D0 -\> pi- pi+' ]                                                                             |
| Output           | Phys/D02pipiForPromptCharm/Particles                                                               |
