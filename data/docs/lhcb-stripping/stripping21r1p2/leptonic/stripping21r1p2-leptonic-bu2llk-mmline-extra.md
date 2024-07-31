[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBu2LLK_mmLine_extra

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/Bu2LLK_mmLine_extra/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

LoKi::VoidFilter/StrippingBu2LLK_mmLine_extraVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseDiMuon

|      |                                  |
|------|----------------------------------|
| Code | 0StdLooseDiMuon/Particles',True) |

FilterDesktop/SelDiMuonsTightForBu2LLK

|                 |                                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ID=='J/psi(1S)') & (PT \> 0 \*MeV) & (MM \< 5500 \*MeV) & (MINTREE(ABSID\<14,PT) \> 500 \*MeV) & (MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY)) \> 9) & (VFASPF(VCHI2/VDOF) \< 9) & (BPVVDCHI2 \> 16) & (MIPCHI2DV(PRIMARY) \> 0) & (2 == NINTREE((ABSID==13)&(HASMUON)&(ISMUON))) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21r1p2-commonparticles-stdloosedimuon)' ]                                                                                                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                                                                                        |
| Output          | Phys/SelDiMuonsTightForBu2LLK/Particles                                                                                                                                                                                                                                     |

GaudiSequencer/MERGED:MergeBu2LLK_mm_extra

GaudiSequencer/MERGEDINPUTS:MergeBu2LLK_mm_extra

GaudiSequencer/INPUT:K1ForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

DaVinci::N3BodyDecays/K1ForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' , 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.35) & (PROBNNk \> 0.05)' , 'K-' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.35) & (PROBNNk \> 0.05)' , 'pi+' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.05)' , 'pi-' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.05)' } |
| CombinationCut   | (AM \> 0\*MeV) & (AM \< 4200\*MeV) & ((APT1+APT2+APT3) \> 1200\*MeV)                                                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2) \< 12) & (SUMTREE(MIPCHI2DV(PRIMARY),((ABSID=='K+') \| (ABSID=='K-') \| (ABSID=='pi+') \| (ABSID=='pi-')),0.0) \> 48.0)                                                                                                                                                                             |
| DecayDescriptor  | [K_1(1270)+ -\> K+ pi+ pi-]cc                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ '[K_1(1270)+ -\> K+ pi+ pi-]cc' ]                                                                                                                                                                                                                                                                            |
| Output           | Phys/K1ForBu2LLK/Particles                                                                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:K2ForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

DaVinci::N3BodyDecays/K2ForBu2LLK

|                  |                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ]                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(P \> 2000 \*MeV) & (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.35) & (PROBNNk \> 0.05)' , 'K-' : '(P \> 2000 \*MeV) & (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.35) & (PROBNNk \> 0.05)' } |
| CombinationCut   | (AM \> 0\*MeV) & (AM \< 4200\*MeV) & ((APT1+APT2+APT3) \> 1200\*MeV)                                                                                                                                   |
| MotherCut        | (VFASPF(VCHI2) \< 12) & (SUMTREE(MIPCHI2DV(PRIMARY),((ABSID=='K+') \| (ABSID=='K-')),0.0) \> 48.0)                                                                                                     |
| DecayDescriptor  | [K_2(1770)+ -\> K+ K+ K-]cc                                                                                                                                                                          |
| DecayDescriptors | [ '[K_2(1770)+ -\> K+ K+ K-]cc' ]                                                                                                                                                                  |
| Output           | Phys/K2ForBu2LLK/Particles                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:PiPisForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

CombineParticles/PiPisForBu2LLK

|                  |                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT \> 350 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.1))' , 'pi-' : '(PT \> 350 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.1))' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 2600 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                                                                                                              |
| Output           | Phys/PiPisForBu2LLK/Particles                                                                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KPisForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

CombineParticles/KPisForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' , 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.1)' , 'K-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.1)' , 'pi+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNpi \> 0.1)' , 'pi-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNpi \> 0.1)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 2600 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptor  | [K\*\_0(1430)0 -\> K+ pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[K\*\_0(1430)0 -\> K+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output           | Phys/KPisForBu2LLK/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KKsForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

CombineParticles/KKsForBu2LLK

|                  |                                                                                                                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ]                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.1)' , 'K-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.1)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 5367 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                     |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                  |
| DecayDescriptor  | f'\_2(1525) -\> K+ K-                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ "f'\_2(1525) -\> K+ K-" ]                                                                                                                                                                                                                                                          |
| Output           | Phys/KKsForBu2LLK/Particles                                                                                                                                                                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:pPisForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

CombineParticles/pPisForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' , 'Phys/[StdLooseProtons](./stripping21r1p2-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT \> 350 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.1)' , 'pi+' : '(PT \> 250 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.1))' , 'pi-' : '(PT \> 250 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.1))' , 'p~-' : '(PT \> 350 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.1)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 2600 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | [N(1440)0 -\> p+ pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[N(1440)0 -\> p+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/pPisForBu2LLK/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ppsForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

CombineParticles/ppsForBu2LLK

|                  |                                                                                                                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseProtons](./stripping21r1p2-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) &(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) & (TRGHOSTPROB \< 0.35) & (PROBNNp \> 0.1)' , 'p~-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) &(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) & (TRGHOSTPROB \< 0.35) & (PROBNNp \> 0.1)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 5620 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                 |
| DecayDescriptor  | f_2(1950) -\> p+ p~-                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ 'f_2(1950) -\> p+ p~-' ]                                                                                                                                                                                                                                                          |
| Output           | Phys/ppsForBu2LLK/Particles                                                                                                                                                                                                                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:PiPisSSForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

CombineParticles/PiPisSSForBu2LLK

|                  |                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT \> 350 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.1))' , 'pi-' : '(PT \> 350 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.1))' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 2600 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                      |
| DecayDescriptor  | [rho(770)0 -\> pi+ pi+]cc                                                                                                                                                                                                                                                                |
| DecayDescriptors | [ '[rho(770)0 -\> pi+ pi+]cc' ]                                                                                                                                                                                                                                                        |
| Output           | Phys/PiPisSSForBu2LLK/Particles                                                                                                                                                                                                                                                            |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KPisSSForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

CombineParticles/KPisSSForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' , 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.1)' , 'K-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.1)' , 'pi+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNpi \> 0.1)' , 'pi-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNpi \> 0.1)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 2600 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptor  | [K\*\_0(1430)0 -\> K+ pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[K\*\_0(1430)0 -\> K+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output           | Phys/KPisSSForBu2LLK/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KKsSSForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

CombineParticles/KKsSSForBu2LLK

|                  |                                                                                                                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ]                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.1)' , 'K-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.1)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 5367 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                     |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                  |
| DecayDescriptor  | [f'\_2(1525) -\> K+ K+]cc                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ "[f'\_2(1525) -\> K+ K+]cc" ]                                                                                                                                                                                                                                                    |
| Output           | Phys/KKsSSForBu2LLK/Particles                                                                                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:pPisSSForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

CombineParticles/pPisSSForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' , 'Phys/[StdLooseProtons](./stripping21r1p2-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT \> 350 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.1)' , 'pi+' : '(PT \> 250 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.1))' , 'pi-' : '(PT \> 250 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35) & (PROBNNpi \> 0.1))' , 'p~-' : '(PT \> 350 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.1)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 2600 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | [N(1440)0 -\> p+ pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[N(1440)0 -\> p+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/pPisSSForBu2LLK/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ppsSSForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

CombineParticles/ppsSSForBu2LLK

|                  |                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseProtons](./stripping21r1p2-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) & (TRGHOSTPROB \< 0.35) & (PROBNNp \> 0.1)' , 'p~-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) & (TRGHOSTPROB \< 0.35) & (PROBNNp \> 0.1)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 5620 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | [f_2(1950) -\> p+ p+]cc                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[f_2(1950) -\> p+ p+]cc' ]                                                                                                                                                                                                                                                       |
| Output           | Phys/ppsSSForBu2LLK/Particles                                                                                                                                                                                                                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/MergeBu2LLK_mm_extra

|                 |                                                                                                                                                                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                         |
| Inputs          | [ 'Phys/K1ForBu2LLK' , 'Phys/K2ForBu2LLK' , 'Phys/KKsForBu2LLK' , 'Phys/KKsSSForBu2LLK' , 'Phys/KPisForBu2LLK' , 'Phys/KPisSSForBu2LLK' , 'Phys/PiPisForBu2LLK' , 'Phys/PiPisSSForBu2LLK' , 'Phys/pPisForBu2LLK' , 'Phys/pPisSSForBu2LLK' , 'Phys/ppsForBu2LLK' , 'Phys/ppsSSForBu2LLK' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                        |
| Output          | Phys/MergeBu2LLK_mm_extra/Particles                                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/Bu2LLK_mmLine_extra

|                  |                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_mm_extra' , 'Phys/SelDiMuonsTightForBu2LLK' ]                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*\_0(1430)0' : 'ALL' , 'K\*\_0(1430)~0' : 'ALL' , 'K_1(1270)+' : 'ALL' , 'K_1(1270)-' : 'ALL' , 'K_2(1770)+' : 'ALL' , 'K_2(1770)-' : 'ALL' , 'N(1440)0' : 'ALL' , 'N(1440)~0' : 'ALL' , "f'\_2(1525)" : 'ALL' , 'f_2(1950)' : 'ALL' , 'rho(770)0' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 1500 \*MeV                                                                                                                                                                                                                                                                          |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 9) & (BPVIPCHI2() \< 25) & (BPVDIRA \> 0.9995) & (BPVVDCHI2 \> 100))                                                                                                                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[ B+ -\> J/psi(1S) K_1(1270)+ ]cc' , '[ B+ -\> J/psi(1S) K_2(1770)+ ]cc' , ' B0 -\> J/psi(1S) rho(770)0 ' , '[ B0 -\> J/psi(1S) K\*\_0(1430)0 ]cc' , " B_s0 -\> J/psi(1S) f'\_2(1525) " , ' B_s0 -\> J/psi(1S) f_2(1950) ' , '[ Lambda_b0 -\> J/psi(1S) N(1440)0 ]cc' ]                 |
| Output           | Phys/Bu2LLK_mmLine_extra/Particles                                                                                                                                                                                                                                                                   |

AddRelatedInfo/RelatedInfo1_Bu2LLK_mmLine_extra

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo1_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo2_Bu2LLK_mmLine_extra

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo2_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo3_Bu2LLK_mmLine_extra

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo3_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo4_Bu2LLK_mmLine_extra

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo4_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo5_Bu2LLK_mmLine_extra

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo5_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo6_Bu2LLK_mmLine_extra

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo6_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo7_Bu2LLK_mmLine_extra

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo7_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo8_Bu2LLK_mmLine_extra

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo8_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo9_Bu2LLK_mmLine_extra

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo9_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo10_Bu2LLK_mmLine_extra

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                 |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo10_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo11_Bu2LLK_mmLine_extra

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                 |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo11_Bu2LLK_mmLine_extra/Particles |

AddRelatedInfo/RelatedInfo12_Bu2LLK_mmLine_extra

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmLine_extra' ]                 |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo12_Bu2LLK_mmLine_extra/Particles |
