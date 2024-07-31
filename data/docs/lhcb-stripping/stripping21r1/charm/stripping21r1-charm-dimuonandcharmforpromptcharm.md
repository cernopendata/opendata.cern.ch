[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDiMuonAndCharmForPromptCharm

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/DiMuonAndCharmForPromptCharm/Particles |
| Postscale      | 1.0000000                                   |
| HLT            | None                                        |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1-commonparticles-stdallloosemuons)/Particles')\>0 |

FilterDesktop/SelMuonForPromptCharm

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | ISMUON & in_range ( 2 , ETA , 4.9 ) & ( PT \> 550 \* MeV ) & ( PIDmu - PIDpi \> 0 ) & ( CLONEDIST \> 5000 ) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r1-commonparticles-stdallloosemuons)' ]                           |
| DecayDescriptor | None                                                                                                        |
| Output          | Phys/SelMuonForPromptCharm/Particles                                                                        |

CombineParticles/SelDiMuonForPromptCharm

|                  |                                                |
|------------------|------------------------------------------------|
| Inputs           | [ 'Phys/SelMuonForPromptCharm' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' } |
| CombinationCut   | psi \| psi_prime \| ( AM \> 8 \* GeV )         |
| MotherCut        | chi2vx \< 20                                   |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                          |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                  |
| Output           | Phys/SelDiMuonForPromptCharm/Particles         |

GaudiSequencer/SeqPromptCharmForPromptCharm

GaudiSequencer/SEQ:SelD02KpiForPromptCharm

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

CombineParticles/SelD02KpiForPromptCharm

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                       |
| CombinationCut   | ( ADAMASS('D0') \< 85 \* MeV ) & ( APT \> 950.0 )                                                  |
| MotherCut        | ( chi2vx \< 9 ) & ( PT \> 1000.0 ) & ( ADMASS('D0') \< 75 \* MeV ) & ( ctau \> 100 \* micrometer ) |
| DecayDescriptor  | [D0 -\> K- pi+]cc                                                                                |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                        |
| Output           | Phys/SelD02KpiForPromptCharm/Particles                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelDstarForPromptCharm

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

CombineParticles/SelD02KpiForPromptCharm

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                       |
| CombinationCut   | ( ADAMASS('D0') \< 85 \* MeV ) & ( APT \> 950.0 )                                                  |
| MotherCut        | ( chi2vx \< 9 ) & ( PT \> 1000.0 ) & ( ADMASS('D0') \< 75 \* MeV ) & ( ctau \> 100 \* micrometer ) |
| DecayDescriptor  | [D0 -\> K- pi+]cc                                                                                |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                        |
| Output           | Phys/SelD02KpiForPromptCharm/Particles                                                             |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/SelDstarForPromptCharm

|                  |                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD02KpiForPromptCharm' , 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                      |
| CombinationCut   | ( AM \< 2.5 \* GeV ) & ( AM - AM1 \< 165 \* MeV )                                                                  |
| MotherCut        | ( chi2vx \< 64 ) & ( M - M1 \< 155 \* MeV )                                                                        |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                        |
| DecayDescriptors | [ ' [D\*(2010)+ -\> D0 pi+]cc' ]                                                                               |
| Output           | Phys/SelDstarForPromptCharm/Particles                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelDsForPromptCharm

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

DaVinci::N3BodyDecays/SelDsForPromptCharm

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }               |
| CombinationCut   | ( APT \> 950.0 ) & ( admD \| admDs ) & ( ACHI2DOCA(1,3) \< 16 ) & ( ACHI2DOCA(2,3) \< 16 ) |
| MotherCut        | ( chi2vx \< 25 ) & ( PT \> 1000.0 ) & ( dmD \| dmDs ) & ( ctau \> 100 \* micrometer )      |
| DecayDescriptor  | [D_s+ -\> K- K+ pi+ ]cc                                                                  |
| DecayDescriptors | [ ' [D_s+ -\> K- K+ pi+ ]cc' ]                                                         |
| Output           | Phys/SelDsForPromptCharm/Particles                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelDForPromptCharm

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

DaVinci::N3BodyDecays/SelDForPromptCharm

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                            |
| CombinationCut   | ( ADAMASS('D+') \< 65 \* MeV ) & ( APT \> 950.0 ) & ( ACHI2DOCA(1,3) \< 16 ) & ( ACHI2DOCA(2,3) \< 16 ) |
| MotherCut        | ( chi2vx \< 25 ) & ( PT \> 1000.0 ) & ( ADMASS ('D+' ) \< 55 \* MeV ) & ( ctau \> 100 \* micrometer )   |
| DecayDescriptor  | [D+ -\> K- pi+ pi+ ]cc                                                                                |
| DecayDescriptors | [ ' [D+ -\> K- pi+ pi+ ]cc' ]                                                                       |
| Output           | Phys/SelDForPromptCharm/Particles                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:SelLambdaCForPromptCharm

LoKi::VoidFilter/SelFilterPhys_StdLooseANNProtons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNProtons](./stripping21r1-commonparticles-stdlooseannprotons)/Particles')\>0 |

FilterDesktop/SelProtonForPromptCharm

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( PT \> 250 \* MeV ) & ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.5 ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 10 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNp \> 0.1 ) & ( MIPCHI2DV() \> 9 ) |
| Inputs          | [ 'Phys/[StdLooseANNProtons](./stripping21r1-commonparticles-stdlooseannprotons)' ]                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/SelProtonForPromptCharm/Particles                                                                                                                                                             |

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

DaVinci::N3BodyDecays/SelLambdaCForPromptCharm

|                  |                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' , 'Phys/SelProtonForPromptCharm' ]                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                   |
| CombinationCut   | ( ( ADAMASS ( 'Lambda_c+' ) \< 65 \* MeV ) \| ( ADAMASS ( 'Xi_c+' ) \< 65 \* MeV ) ) & ( APT \> 950.0 ) & ( ACHI2DOCA(1,3) \< 16 ) & ( ACHI2DOCA(2,3) \< 16 ) |
| MotherCut        | ( chi2vx \< 25 ) & ( PT \> 1000.0 ) & ( ( ADMASS ( 'Lambda_c+' ) \< 55 \* MeV ) \| ( ADMASS ( 'Xi_c+' ) \< 55 \* MeV ) ) & ( ctau \> 100 \* micrometer )      |
| DecayDescriptor  | [ Lambda_c+ -\> p+ K- pi+ ]cc                                                                                                                               |
| DecayDescriptors | [ ' [ Lambda_c+ -\> p+ K- pi+ ]cc' ]                                                                                                                      |
| Output           | Phys/SelLambdaCForPromptCharm/Particles                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/PromptCharmForPromptCharm

|                 |                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                             |
| Inputs          | [ 'Phys/SelD02KpiForPromptCharm' , 'Phys/SelDForPromptCharm' , 'Phys/SelDsForPromptCharm' , 'Phys/SelDstarForPromptCharm' , 'Phys/SelLambdaCForPromptCharm' ] |
| DecayDescriptor | None                                                                                                                                                            |
| Output          | Phys/PromptCharmForPromptCharm/Particles                                                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/DiMuonAndCharmForPromptCharm

|                  |                                                                                                                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PromptCharmForPromptCharm' , 'Phys/SelDiMuonForPromptCharm' ]                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'D~0' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' }    |
| CombinationCut   | AALL                                                                                                                                                                                                                              |
| MotherCut        | ALL                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                              |
| DecayDescriptors | [ '[ Upsilon(1S) -\> J/psi(1S) D0 ]cc' , '[ Upsilon(1S) -\> J/psi(1S) D\*(2010)+ ]cc' , '[ Upsilon(1S) -\> J/psi(1S) D+ ]cc' , '[ Upsilon(1S) -\> J/psi(1S) D_s+ ]cc' , '[ Upsilon(1S) -\> J/psi(1S) Lambda_c+ ]cc' ] |
| Output           | Phys/DiMuonAndCharmForPromptCharm/Particles                                                                                                                                                                                       |
