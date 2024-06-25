[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBu2LLK_eeLine3

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/Bu2LLK_eeLine3/Particles |
| Postscale      | 1.0000000                     |
| HLT1           | None                          |
| HLT2           | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

LoKi::VoidFilter/StrippingBu2LLK_eeLine3VOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:MergeBu2LLK_ee3

GaudiSequencer/MERGEDINPUTS:MergeBu2LLK_ee3

GaudiSequencer/INPUT:KstarsForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKstar2Kpi

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseKstar2Kpi/Particles',True) |

FilterDesktop/KstarsForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseKstar2Kpi](./stripping21r1p2-commonparticles-stdloosekstar2kpi)' ]                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/KstarsForBu2LLK/Particles                                                                                                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:PhisForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLoosePhi2KK

|      |                                  |
|------|----------------------------------|
| Code | 0StdLoosePhi2KK/Particles',True) |

FilterDesktop/PhisForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21r1p2-commonparticles-stdloosephi2kk)' ]                                                                |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/PhisForBu2LLK/Particles                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:LambdasLLForBu2LLK

GaudiSequencer/MERGED:MergedLambdasLLForBu2LLK

GaudiSequencer/MERGEDINPUTS:MergedLambdasLLForBu2LLK

GaudiSequencer/INPUT:Phys/StdVeryLooseLambdaLL

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseLambdaLL

|      |                                        |
|------|----------------------------------------|
| Code | 0StdVeryLooseLambdaLL/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Phys/StdLambda2PPiLL

LoKi::VoidFilter/SELECT:Phys/StdLambda2PPiLL

|      |     |
|------|-----|
| Code | 0   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterUnique/MergedLambdasLLForBu2LLK

|                 |                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                  |
| Inputs          | [ 'Phys/StdLambda2PPiLL' , 'Phys/[StdVeryLooseLambdaLL](./stripping21r1p2-commonparticles-stdverylooselambdall)' ] |
| DecayDescriptor | None                                                                                                                 |
| Output          | Phys/MergedLambdasLLForBu2LLK/Particles                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/LambdasLLForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/MergedLambdasLLForBu2LLK' ]                                                                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/LambdasLLForBu2LLK/Particles                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:LambdasDDForBu2LLK

GaudiSequencer/MERGED:MergedLambdasDDForBu2LLK

GaudiSequencer/MERGEDINPUTS:MergedLambdasDDForBu2LLK

GaudiSequencer/INPUT:Phys/StdLooseLambdaDD

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaDD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaDD/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Phys/StdLambda2PPiDD

LoKi::VoidFilter/SELECT:Phys/StdLambda2PPiDD

|      |     |
|------|-----|
| Code | 0   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterUnique/MergedLambdasDDForBu2LLK

|                 |                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                          |
| Inputs          | [ 'Phys/StdLambda2PPiDD' , 'Phys/[StdLooseLambdaDD](./stripping21r1p2-commonparticles-stdlooselambdadd)' ] |
| DecayDescriptor | None                                                                                                         |
| Output          | Phys/MergedLambdasDDForBu2LLK/Particles                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/LambdasDDForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/MergedLambdasDDForBu2LLK' ]                                                                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/LambdasDDForBu2LLK/Particles                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

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

GaudiSequencer/INPUT:pKsForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdAllLooseProtons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdAllLooseProtons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseKaons

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLooseKaons/Particles',True) |

CombineParticles/pKsForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21r1p2-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLooseProtons](./stripping21r1p2-commonparticles-stdalllooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.05)' , 'K-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.05)' , 'p+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.05)' , 'p~-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.05)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 5620 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/pKsForBu2LLK/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

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

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/MergeBu2LLK_ee3

|                 |                                                                                                                                                                                                                                                                          |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                      |
| Inputs          | [ 'Phys/K1ForBu2LLK' , 'Phys/KKsForBu2LLK' , 'Phys/KPisForBu2LLK' , 'Phys/KstarsForBu2LLK' , 'Phys/LambdasDDForBu2LLK' , 'Phys/LambdasLLForBu2LLK' , 'Phys/PhisForBu2LLK' , 'Phys/PiPisForBu2LLK' , 'Phys/pKsForBu2LLK' , 'Phys/pPisForBu2LLK' , 'Phys/ppsForBu2LLK' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                     |
| Output          | Phys/MergeBu2LLK_ee3/Particles                                                                                                                                                                                                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseGammaLL

|      |                                      |
|------|--------------------------------------|
| Code | 0StdAllLooseGammaLL/Particles',True) |

FilterDesktop/SelPhotonForBu2LLK

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PT \> 1000\*MeV) & (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 9)                             |
| Inputs          | [ 'Phys/[StdAllLooseGammaLL](./stripping21r1p2-commonparticles-stdallloosegammall)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/SelPhotonForBu2LLK/Particles                                                       |

CombineParticles/Bu2LLK_eeLine3

|                  |                                                                                                                                                                                                                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_ee3' , 'Phys/SelPhotonForBu2LLK' ]                                                                                                                                                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K\*\_0(1430)0' : 'ALL' , 'K\*\_0(1430)~0' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'N(1440)0' : 'ALL' , 'N(1440)~0' : 'ALL' , "f'\_2(1525)" : 'ALL' , 'f_2(1950)' : 'ALL' , 'gamma' : 'ALL' , 'phi(1020)' : 'ALL' , 'rho(770)0' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 1500 \*MeV                                                                                                                                                                                                                                                                                                                                           |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 9) & (BPVIPCHI2() \< 25) & (BPVDIRA \> 0.9995) & (BPVVDCHI2 \> 100))                                                                                                                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[ B0 -\> gamma K\*(892)0 ]cc' , '[ B0 -\> gamma K\*\_0(1430)0 ]cc' , ' B0 -\> gamma rho(770)0 ' , ' B_s0 -\> gamma phi(1020) ' , " B_s0 -\> gamma f'\_2(1525) " , ' B_s0 -\> gamma f_2(1950) ' , '[ Lambda_b0 -\> gamma Lambda0 ]cc' , '[ Lambda_b0 -\> gamma N(1440)0 ]cc' , '[ Lambda_b0 -\> gamma Lambda(1520)0 ]cc' ]                              |
| Output           | Phys/Bu2LLK_eeLine3/Particles                                                                                                                                                                                                                                                                                                                                         |

AddRelatedInfo/RelatedInfo1_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo1_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo2_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo2_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo3_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo3_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo4_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo4_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo5_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo5_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo6_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo6_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo7_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo7_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo8_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo8_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo9_Bu2LLK_eeLine3

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo9_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo10_Bu2LLK_eeLine3

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                 |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo10_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo11_Bu2LLK_eeLine3

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                 |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo11_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo12_Bu2LLK_eeLine3

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                 |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo12_Bu2LLK_eeLine3/Particles |

AddRelatedInfo/RelatedInfo13_Bu2LLK_eeLine3

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                 |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo13_Bu2LLK_eeLine3/Particles |
