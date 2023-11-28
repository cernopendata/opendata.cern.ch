[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLambdaCLooseChi2IPForPromptCharm

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/LambdaCLooseChi2IPForPromptCharm/Particles |
| Postscale      | 1.0000000                                       |
| HLT1           | None                                            |
| HLT2           | None                                            |
| Prescale       | 0.20000000                                      |
| L0DU           | None                                            |
| ODIN           | None                                            |

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

LoKi::VoidFilter/SELECT:Phys/StdLooseANNProtons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseANNProtons/Particles',True) |

FilterDesktop/SelProtonForPromptCharm

|                 |                                                                                                                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 10 \* GeV , P , 150 \* GeV ) & HASRICH & ( MIPCHI2DV() \> 9 ) )&( PROBNNp \> 0.1 ) |
| Inputs          | [ 'Phys/[StdLooseANNProtons](./stripping21r0p2-commonparticles-stdlooseannprotons)' ]                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                                                 |
| Output          | Phys/SelProtonForPromptCharm/Particles                                                                                                                                                               |

LoKi::VoidFilter/SELECT:Phys/StdLooseANNKaons

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseANNKaons/Particles',True) |

FilterDesktop/SelKaonForPromptCharm

|                 |                                                                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( MIPCHI2DV() \> 9 ) )&( PROBNNk \> 0.1 ) |
| Inputs          | [ 'Phys/[StdLooseANNKaons](./stripping21r0p2-commonparticles-stdlooseannkaons)' ]                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                  |
| Output          | Phys/SelKaonForPromptCharm/Particles                                                                                                                                                                  |

LoKi::VoidFilter/SELECT:Phys/StdLooseANNPions

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseANNPions/Particles',True) |

FilterDesktop/SelPionForPromptCharm

|                 |                                                                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( (PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( MIPCHI2DV() \> 9 ) )&( PROBNNpi \> 0.1 ) |
| Inputs          | [ 'Phys/[StdLooseANNPions](./stripping21r0p2-commonparticles-stdlooseannpions)' ]                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                  |
| Output          | Phys/SelPionForPromptCharm/Particles                                                                                                                                                                  |

DaVinci::N3BodyDecays/SelpreLambdaCForPromptCharm

|                  |                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' , 'Phys/SelProtonForPromptCharm' ]                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                   |
| CombinationCut   | ( ( ADAMASS ( 'Lambda_c+' ) \< 65 \* MeV ) \| ( ADAMASS ( 'Xi_c+' ) \< 65 \* MeV ) ) & ( APT \> 850.0 ) & ( ACHI2DOCA(1,3) \< 16 ) & ( ACHI2DOCA(2,3) \< 16 ) |
| MotherCut        | ( chi2vx \< 25 ) & ( PT \> 1000.0 ) & ( ( ADMASS ( 'Lambda_c+' ) \< 55 \* MeV ) \| ( ADMASS ( 'Xi_c+' ) \< 55 \* MeV ) )                                      |
| DecayDescriptor  | [ Lambda_c+ -\> p+ K- pi+ ]cc                                                                                                                               |
| DecayDescriptors | [ ' [ Lambda_c+ -\> p+ K- pi+ ]cc' ]                                                                                                                      |
| Output           | Phys/SelpreLambdaCForPromptCharm/Particles                                                                                                                    |

FilterDesktop/LambdaCLooseChi2IPForPromptCharm

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | ( PT \> 1000.0 ) & ( ctau_400 \> 0.1 \* mm )    |
| Inputs          | [ 'Phys/SelpreLambdaCForPromptCharm' ]        |
| DecayDescriptor | None                                            |
| Output          | Phys/LambdaCLooseChi2IPForPromptCharm/Particles |
