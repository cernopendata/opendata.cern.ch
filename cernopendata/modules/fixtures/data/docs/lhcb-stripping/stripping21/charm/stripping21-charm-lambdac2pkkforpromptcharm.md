[[stripping21 lines]](./stripping21-index)

# StrippingLambdaC2pKKForPromptCharm

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/LambdaC2pKKForPromptCharm/Particles |
| Postscale      | 1.0000000                                |
| HLT            | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNProtons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNProtons](./stripping21-commonparticles-stdlooseannprotons)/Particles')\>0 |

FilterDesktop/SelProtonForPromptCharm

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 10 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNp \> 0.1 ) & ( MIPCHI2DV() \> 9 ) |
| Inputs          | [ 'Phys/[StdLooseANNProtons](./stripping21-commonparticles-stdlooseannprotons)' ]                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/SelProtonForPromptCharm/Particles                                                                                                                                                             |

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

DaVinci::N3BodyDecays/LambdaC2pKKForPromptCharm

|                  |                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelProtonForPromptCharm' ]                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                                                                   |
| CombinationCut   | ( ( ADAMASS ( 'Lambda_c+' ) \< 65 \* MeV ) \| ( ADAMASS ( 'Xi_c+' ) \< 65 \* MeV ) ) & ( APT \> 950.0 ) & ( ACHI2DOCA(1,3) \< 16 ) & ( ACHI2DOCA(2,3) \< 16 ) |
| MotherCut        | ( chi2vx \< 25 ) & ( PT \> 1000.0 ) & ( ( ADMASS ( 'Lambda_c+' ) \< 55 \* MeV ) \| ( ADMASS ( 'Xi_c+' ) \< 55 \* MeV ) ) & ( ctau \> 100 \* micrometer )      |
| DecayDescriptor  | [ Lambda_c+ -\> p+ K- K+ ]cc                                                                                                                                |
| DecayDescriptors | [ ' [ Lambda_c+ -\> p+ K- K+ ]cc' ]                                                                                                                       |
| Output           | Phys/LambdaC2pKKForPromptCharm/Particles                                                                                                                      |
