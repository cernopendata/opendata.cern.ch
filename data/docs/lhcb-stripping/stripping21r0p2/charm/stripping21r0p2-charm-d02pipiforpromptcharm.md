[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingD02pipiForPromptCharm

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/D02pipiForPromptCharm/Particles |
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

CombineParticles/D02pipiForPromptCharm

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelPionForPromptCharm' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                             |
| CombinationCut   | ( ADAMASS('D0') \< 85 \* MeV ) & ( APT \> 950.0 )                                          |
| MotherCut        | ( chi2vx \< 9 ) & ( PT \> 1000.0 ) & ( ADMASS('D0') \< 75 \* MeV ) & ( ctau \> 0.1 \* mm ) |
| DecayDescriptor  | D0 -\> pi- pi+                                                                             |
| DecayDescriptors | [ 'D0 -\> pi- pi+' ]                                                                     |
| Output           | Phys/D02pipiForPromptCharm/Particles                                                       |
