[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingXiCstarForPromptCharm

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/XiCstarForPromptCharm/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNProtons_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNProtons](./stripping21r1p1-commonparticles-stdlooseannprotons)/Particles',True)\>0 |

FilterDesktop/SelProtonForPromptCharm

|                 |                                                                                                                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 10 \* GeV , P , 150 \* GeV ) & HASRICH & ( MIPCHI2DV() \> 9 ) )&( PROBNNp \> 0.1 ) |
| Inputs          | [ 'Phys/[StdLooseANNProtons](./stripping21r1p1-commonparticles-stdlooseannprotons)' ]                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                                                 |
| Output          | Phys/SelProtonForPromptCharm/Particles                                                                                                                                                               |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNKaons](./stripping21r1p1-commonparticles-stdlooseannkaons)/Particles',True)\>0 |

FilterDesktop/SelKaonForPromptCharm

|                 |                                                                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( MIPCHI2DV() \> 9 ) )&( PROBNNk \> 0.1 ) |
| Inputs          | [ 'Phys/[StdLooseANNKaons](./stripping21r1p1-commonparticles-stdlooseannkaons)' ]                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                  |
| Output          | Phys/SelKaonForPromptCharm/Particles                                                                                                                                                                  |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNPions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNPions](./stripping21r1p1-commonparticles-stdlooseannpions)/Particles',True)\>0 |

FilterDesktop/SelPionForPromptCharm

|                 |                                                                                                                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( MIPCHI2DV() \> 9 ) )&( PROBNNpi \> 0.1 ) |
| Inputs          | [ 'Phys/[StdLooseANNPions](./stripping21r1p1-commonparticles-stdlooseannpions)' ]                                                                                                                    |
| DecayDescriptor | None                                                                                                                                                                                                   |
| Output          | Phys/SelPionForPromptCharm/Particles                                                                                                                                                                   |

DaVinci::N4BodyDecays/SelpreXiC0ForPromptCharm

|                  |                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' , 'Phys/SelProtonForPromptCharm' ]                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                             |
| CombinationCut   | ( ( ADAMASS ( 'Omega_c0' ) \< 65 \* MeV ) \| ( ADAMASS ( 'Xi_c0' ) \< 65 \* MeV ) ) & ( APT \> 850.0 ) & ( ACHI2DOCA(1,4) \< 16 ) & ( ACHI2DOCA(2,4) \< 16 ) & ( ACHI2DOCA(3,4) \< 16 ) |
| MotherCut        | ( chi2vx \< 25 ) & ( PT \> 1000.0 ) & ( ( ADMASS ( 'Omega_c0' ) \< 55 \* MeV ) \| ( ADMASS ( 'Xi_c0' ) \< 55 \* MeV ) )                                                                 |
| DecayDescriptor  | [ Xi_c0 -\> p+ K- K- pi+ ]cc                                                                                                                                                          |
| DecayDescriptors | [ ' [ Xi_c0 -\> p+ K- K- pi+ ]cc' ]                                                                                                                                                 |
| Output           | Phys/SelpreXiC0ForPromptCharm/Particles                                                                                                                                                 |

FilterDesktop/SelXiC0ForPromptCharm

|                 |                                                                                |
|-----------------|--------------------------------------------------------------------------------|
| Code            | ( ADMASS ( 'Xi_c0' ) \< 55 \* MeV ) & ( PT \> 1000.0 ) & ( ctau \> 0.1 \* mm ) |
| Inputs          | [ 'Phys/SelpreXiC0ForPromptCharm' ]                                          |
| DecayDescriptor | None                                                                           |
| Output          | Phys/SelXiC0ForPromptCharm/Particles                                           |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r1p1-commonparticles-stdalllooseannpions)/Particles',True)\>0 |

CombineParticles/XiCstarForPromptCharm

|                  |                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelXiC0ForPromptCharm' , 'Phys/[StdAllLooseANNPions](./stripping21r1p1-commonparticles-stdalllooseannpions)' ]                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c0' : 'ALL' , 'Xi_c~0' : 'ALL' , 'pi+' : '\n ( CLONEDIST \> 5000 ) &\n ( TRGHOSTPROB \< 0.5 ) &\n in_range ( 2 , ETA , 4.9 ) &\n HASRICH\n ' , 'pi-' : '\n ( CLONEDIST \> 5000 ) &\n ( TRGHOSTPROB \< 0.5 ) &\n in_range ( 2 , ETA , 4.9 ) &\n HASRICH\n ' } |
| CombinationCut   | AM - AM1 \< ( 140 \* MeV + 150.0 )                                                                                                                                                                                                                                              |
| MotherCut        | ( chi2vx \< 16 )                                                                                                                                                                                                                                                                |
| DecayDescriptor  | [ Xi_c\*+ -\> Xi_c0 pi+ ]cc                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ ' [ Xi_c\*+ -\> Xi_c0 pi+ ]cc' ]                                                                                                                                                                                                                                          |
| Output           | Phys/XiCstarForPromptCharm/Particles                                                                                                                                                                                                                                            |
