[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingDstarCPForPromptCharm

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/DstarCPForPromptCharm/Particles |
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

GaudiSequencer/MERGED:SelD02CPForPromptCharm

GaudiSequencer/MERGEDINPUTS:SelD02CPForPromptCharm

GaudiSequencer/INPUT:SelD02KKForPromptCharm

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

CombineParticles/SelD02KKForPromptCharm

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                               |
| CombinationCut   | ( ADAMASS('D0') \< 85 \* MeV ) & ( APT \> 950.0 )                                          |
| MotherCut        | ( chi2vx \< 9 ) & ( PT \> 1000.0 ) & ( ADMASS('D0') \< 75 \* MeV ) & ( ctau \> 0.1 \* mm ) |
| DecayDescriptor  | D0 -\> K- K+                                                                               |
| DecayDescriptors | [ 'D0 -\> K- K+' ]                                                                       |
| Output           | Phys/SelD02KKForPromptCharm/Particles                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:SelD02pipiForPromptCharm

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

CombineParticles/SelD02pipiForPromptCharm

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelPionForPromptCharm' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                             |
| CombinationCut   | ( ADAMASS('D0') \< 85 \* MeV ) & ( APT \> 950.0 )                                          |
| MotherCut        | ( chi2vx \< 9 ) & ( PT \> 1000.0 ) & ( ADMASS('D0') \< 75 \* MeV ) & ( ctau \> 0.1 \* mm ) |
| DecayDescriptor  | D0 -\> pi- pi+                                                                             |
| DecayDescriptors | [ 'D0 -\> pi- pi+' ]                                                                     |
| Output           | Phys/SelD02pipiForPromptCharm/Particles                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/SelD02CPForPromptCharm

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | ALL                                                                   |
| Inputs          | [ 'Phys/SelD02KKForPromptCharm' , 'Phys/SelD02pipiForPromptCharm' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/SelD02CPForPromptCharm/Particles                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNPions

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNPions/Particles',True) |

CombineParticles/DstarCPForPromptCharm

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD02CPForPromptCharm' , 'Phys/[StdAllLooseANNPions](./stripping21r0p2-commonparticles-stdalllooseannpions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                             |
| CombinationCut   | ( AM \< 2.5 \* GeV ) & ( AM - AM1 \< 165 \* MeV )                                                                         |
| MotherCut        | ( chi2vx \< 64 ) & ( M - M1 \< 155 \* MeV )                                                                               |
| DecayDescriptor  | None                                                                                                                      |
| DecayDescriptors | [ ' D\*(2010)+ -\> D0 pi+ ' , ' D\*(2010)- -\> D0 pi- ' ]                                                               |
| Output           | Phys/DstarCPForPromptCharm/Particles                                                                                      |
