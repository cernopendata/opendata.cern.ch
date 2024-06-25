[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingChiAndCharmForPromptCharm

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/ChiAndCharmForPromptCharm/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLooseMuons/Particles',True) |

FilterDesktop/SelMuonForPromptCharm

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | ISMUON & in_range ( 2 , ETA , 4.9 ) & ( PT \> 550 \* MeV ) & ( PIDmu - PIDpi \> 0 ) & ( CLONEDIST \> 5000 ) |
| Inputs          | [ 'Phys/[StdAllLooseMuons](./stripping21r0p2-commonparticles-stdallloosemuons)' ]                         |
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

GaudiSequencer/MERGED:PromptCharmForPromptCharm

GaudiSequencer/MERGEDINPUTS:PromptCharmForPromptCharm

GaudiSequencer/INPUT:SelD02KpiForPromptCharm

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

CombineParticles/SelD02KpiForPromptCharm

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }               |
| CombinationCut   | ( ADAMASS('D0') \< 85 \* MeV ) & ( APT \> 950.0 )                                          |
| MotherCut        | ( chi2vx \< 9 ) & ( PT \> 1000.0 ) & ( ADMASS('D0') \< 75 \* MeV ) & ( ctau \> 0.1 \* mm ) |
| DecayDescriptor  | [D0 -\> K- pi+]cc                                                                        |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                |
| Output           | Phys/SelD02KpiForPromptCharm/Particles                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:SelDstarForPromptCharm

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

CombineParticles/SelD02KpiForPromptCharm

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }               |
| CombinationCut   | ( ADAMASS('D0') \< 85 \* MeV ) & ( APT \> 950.0 )                                          |
| MotherCut        | ( chi2vx \< 9 ) & ( PT \> 1000.0 ) & ( ADMASS('D0') \< 75 \* MeV ) & ( ctau \> 0.1 \* mm ) |
| DecayDescriptor  | [D0 -\> K- pi+]cc                                                                        |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                |
| Output           | Phys/SelD02KpiForPromptCharm/Particles                                                     |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNPions

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNPions/Particles',True) |

CombineParticles/SelDstarForPromptCharm

|                  |                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD02KpiForPromptCharm' , 'Phys/[StdAllLooseANNPions](./stripping21r0p2-commonparticles-stdalllooseannpions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                              |
| CombinationCut   | ( AM \< 2.5 \* GeV ) & ( AM - AM1 \< 165 \* MeV )                                                                          |
| MotherCut        | ( chi2vx \< 64 ) & ( M - M1 \< 155 \* MeV )                                                                                |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                                |
| DecayDescriptors | [ ' [D\*(2010)+ -\> D0 pi+]cc' ]                                                                                       |
| Output           | Phys/SelDstarForPromptCharm/Particles                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:SelDsForPromptCharm

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

DaVinci::N3BodyDecays/SelDsForPromptCharm

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }               |
| CombinationCut   | ( APT \> 950.0 ) & ( admD \| admDs ) & ( ACHI2DOCA(1,3) \< 16 ) & ( ACHI2DOCA(2,3) \< 16 ) |
| MotherCut        | ( chi2vx \< 25 ) & ( PT \> 1000.0 ) & ( dmD \| dmDs ) & ( ctau \> 0.1 \* mm )              |
| DecayDescriptor  | [D_s+ -\> K- K+ pi+ ]cc                                                                  |
| DecayDescriptors | [ ' [D_s+ -\> K- K+ pi+ ]cc' ]                                                         |
| Output           | Phys/SelDsForPromptCharm/Particles                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:SelDForPromptCharm

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

DaVinci::N3BodyDecays/SelDForPromptCharm

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForPromptCharm' , 'Phys/SelPionForPromptCharm' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                            |
| CombinationCut   | ( ADAMASS('D+') \< 65 \* MeV ) & ( APT \> 950.0 ) & ( ACHI2DOCA(1,3) \< 16 ) & ( ACHI2DOCA(2,3) \< 16 ) |
| MotherCut        | ( chi2vx \< 25 ) & ( PT \> 1000.0 ) & ( ADMASS ('D+' ) \< 55 \* MeV ) & ( ctau \> 0.1 \* mm )           |
| DecayDescriptor  | [D+ -\> K- pi+ pi+ ]cc                                                                                |
| DecayDescriptors | [ ' [D+ -\> K- pi+ pi+ ]cc' ]                                                                       |
| Output           | Phys/SelDForPromptCharm/Particles                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:SelLambdaCForPromptCharm

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

FilterDesktop/SelLambdaCForPromptCharm

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | ( PT \> 1000.0 ) & ( ctau \> 0.1 \* mm ) |
| Inputs          | [ 'Phys/SelpreLambdaCForPromptCharm' ] |
| DecayDescriptor | None                                     |
| Output          | Phys/SelLambdaCForPromptCharm/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:SelSigmaCForPromptCharm

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

FilterDesktop/SelLambdaCForPromptCharm

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | ( PT \> 1000.0 ) & ( ctau \> 0.1 \* mm ) |
| Inputs          | [ 'Phys/SelpreLambdaCForPromptCharm' ] |
| DecayDescriptor | None                                     |
| Output          | Phys/SelLambdaCForPromptCharm/Particles  |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNPions

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNPions/Particles',True) |

CombineParticles/SelSigmaCForPromptCharm

|                  |                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelLambdaCForPromptCharm' , 'Phys/[StdAllLooseANNPions](./stripping21r0p2-commonparticles-stdalllooseannpions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                 |
| CombinationCut   | ( AM - AM1 \< ( 140 \* MeV + 140 \* MeV ) )                                                                                 |
| MotherCut        | ( chi2vx \< 16 )                                                                                                            |
| DecayDescriptor  | None                                                                                                                        |
| DecayDescriptors | [ ' [ Sigma_c0 -\> Lambda_c+ pi- ]cc' , ' [ Sigma_c++ -\> Lambda_c+ pi+ ]cc' ]                                        |
| Output           | Phys/SelSigmaCForPromptCharm/Particles                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:SelLambdaCstarForPromptCharm

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

FilterDesktop/SelLambdaCForPromptCharm

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | ( PT \> 1000.0 ) & ( ctau \> 0.1 \* mm ) |
| Inputs          | [ 'Phys/SelpreLambdaCForPromptCharm' ] |
| DecayDescriptor | None                                     |
| Output          | Phys/SelLambdaCForPromptCharm/Particles  |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNPions

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNPions/Particles',True) |

DaVinci::N3BodyDecays/SelLambdaCstarForPromptCharm

|                  |                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelLambdaCForPromptCharm' , 'Phys/[StdAllLooseANNPions](./stripping21r0p2-commonparticles-stdalllooseannpions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                 |
| CombinationCut   | ( AM - AM1 \< ( 2 \* 140 \* MeV + 80 \* MeV ) ) & ( ACHI2DOCA(1,3) \< 16 ) & ( ACHI2DOCA(2,3) \< 16 )                       |
| MotherCut        | ( chi2vx \< 25 )                                                                                                            |
| DecayDescriptor  | [ Lambda_c(2625)+ -\> Lambda_c+ pi+ pi-]cc                                                                                |
| DecayDescriptors | [ ' [ Lambda_c(2625)+ -\> Lambda_c+ pi+ pi-]cc' ]                                                                       |
| Output           | Phys/SelLambdaCstarForPromptCharm/Particles                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/PromptCharmForPromptCharm

|                 |                                                                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                    |
| Inputs          | [ 'Phys/SelD02KpiForPromptCharm' , 'Phys/SelDForPromptCharm' , 'Phys/SelDsForPromptCharm' , 'Phys/SelDstarForPromptCharm' , 'Phys/SelLambdaCForPromptCharm' , 'Phys/SelLambdaCstarForPromptCharm' , 'Phys/SelSigmaCForPromptCharm' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                   |
| Output          | Phys/PromptCharmForPromptCharm/Particles                                                                                                                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/SelDiMuonAndCharmForPromptCharm

|                  |                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PromptCharmForPromptCharm' , 'Phys/SelDiMuonForPromptCharm' ]                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'D~0' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'Lambda_c(2625)+' : 'ALL' , 'Lambda_c(2625)~-' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'Sigma_c++' : 'ALL' , 'Sigma_c0' : 'ALL' , 'Sigma_c~--' : 'ALL' , 'Sigma_c~0' : 'ALL' } |
| CombinationCut   | AALL                                                                                                                                                                                                                                                                                                                                                                            |
| MotherCut        | ALL                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[Upsilon(1S) -\> J/psi(1S) D0]cc' , '[Upsilon(1S) -\> J/psi(1S) D+]cc' , '[Upsilon(1S) -\> J/psi(1S) D_s+]cc' , '[Upsilon(1S) -\> J/psi(1S) D\*(2010)+]cc' , '[Upsilon(1S) -\> J/psi(1S) Lambda_c+]cc' , '[Upsilon(1S) -\> J/psi(1S) Sigma_c0]cc' , '[Upsilon(1S) -\> J/psi(1S) Sigma_c++]cc' , '[Upsilon(1S) -\> J/psi(1S) Lambda_c(2625)+]cc' ]          |
| Output           | Phys/SelDiMuonAndCharmForPromptCharm/Particles                                                                                                                                                                                                                                                                                                                                  |

LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseAllPhotons/Particles',True) |

DaVinci::N3BodyDecays/SelPreChiAndCharmForPromptCharm

|                  |                                                                                                                                                                                                                                                                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PromptCharmForPromptCharm' , 'Phys/SelDiMuonAndCharmForPromptCharm' , 'Phys/SelDiMuonForPromptCharm' , 'Phys/[StdLooseAllPhotons](./stripping21r0p2-commonparticles-stdlooseallphotons)' ]                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'D~0' : 'ALL' , 'J/psi(1S)' : ' ( M \< 3.21 \* GeV ) \| in_range ( 9.3 \* GeV , M , 9.6 \* GeV ) ' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'gamma' : ' ( PT \> 400 \* MeV ) & ( CL \> 0.05 ) ' } |
| CombinationCut   | AM13 - AM1 \< 1.01 \* GeV                                                                                                                                                                                                                                                                                                                           |
| MotherCut        | ALL                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptors | [ '[ Upsilon(1S) -\> J/psi(1S) D0 gamma ]cc' , '[ Upsilon(1S) -\> J/psi(1S) D\*(2010)+ gamma ]cc' , '[ Upsilon(1S) -\> J/psi(1S) D+ gamma ]cc' , '[ Upsilon(1S) -\> J/psi(1S) D_s+ gamma ]cc' , '[ Upsilon(1S) -\> J/psi(1S) Lambda_c+ gamma ]cc' ]                                                                                     |
| Output           | Phys/SelPreChiAndCharmForPromptCharm/Particles                                                                                                                                                                                                                                                                                                      |

Pi0Veto::Tagger/ChiAndCharmForPromptCharm

|                 |                                              |
|-----------------|----------------------------------------------|
| Code            | "gamma" == ID                                |
| Inputs          | [ 'Phys/SelPreChiAndCharmForPromptCharm' ] |
| DecayDescriptor | None                                         |
| Output          | Phys/ChiAndCharmForPromptCharm/Particles     |
