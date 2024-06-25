[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBu2LLK_eeLine2

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/Bu2LLK_eeLine2/Particles |
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

LoKi::VoidFilter/StrippingBu2LLK_eeLine2VOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdDiElectronFromTracks

|      |                                           |
|------|-------------------------------------------|
| Code | 0StdDiElectronFromTracks/Particles',True) |

FilterDesktop/SelDiElectronFromTracksForBu2LLK

|                 |                                                                                                                                                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ID=='J/psi(1S)') & (PT \> 0 \*MeV) & (MM \< 5500 \*MeV) & (MINTREE(ABSID\<14,PT) \> 350 \*MeV) & (MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY)) \> 9) & (VFASPF(VCHI2/VDOF) \< 9) & (BPVVDCHI2 \> 16) & (MIPCHI2DV(PRIMARY) \> 0) & (2 == NINTREE((ABSID==11)&(PIDe \> 0))) |
| Inputs          | [ 'Phys/[StdDiElectronFromTracks](./stripping21r0p2-commonparticles-stddielectronfromtracks)' ]                                                                                                                                                                    |
| DecayDescriptor | None                                                                                                                                                                                                                                                                 |
| Output          | Phys/SelDiElectronFromTracksForBu2LLK/Particles                                                                                                                                                                                                                      |

GaudiSequencer/MERGED:MergeBu2LLK_ee2

GaudiSequencer/MERGEDINPUTS:MergeBu2LLK_ee2

GaudiSequencer/INPUT:PionsForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/PionsForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                                  |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/PionsForBu2LLK/Particles                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KaonsForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/KaonsForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' ]                                                                  |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/KaonsForBu2LLK/Particles                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KstarsForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKstar2Kpi

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseKstar2Kpi/Particles',True) |

FilterDesktop/KstarsForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLooseKstar2Kpi](./stripping21r0p2-commonparticles-stdloosekstar2kpi)' ]                                                          |
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
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21r0p2-commonparticles-stdloosephi2kk)' ]                                                                |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/PhisForBu2LLK/Particles                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KshortsLLForBu2LLK

GaudiSequencer/MERGED:MergedKshortsLLForBu2LLK

GaudiSequencer/MERGEDINPUTS:MergedKshortsLLForBu2LLK

GaudiSequencer/INPUT:Phys/StdVeryLooseKsLL

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Phys/StdKs2PiPiLL

LoKi::VoidFilter/SELECT:Phys/StdKs2PiPiLL

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

FilterUnique/MergedKshortsLLForBu2LLK

|                 |                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                       |
| Inputs          | [ 'Phys/StdKs2PiPiLL' , 'Phys/[StdVeryLooseKsLL](./stripping21r0p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                                      |
| Output          | Phys/MergedKshortsLLForBu2LLK/Particles                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/KshortsLLForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/MergedKshortsLLForBu2LLK' ]                                                                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/KshortsLLForBu2LLK/Particles                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KshortsDDForBu2LLK

GaudiSequencer/MERGED:MergedKshortsDDForBu2LLK

GaudiSequencer/MERGEDINPUTS:MergedKshortsDDForBu2LLK

GaudiSequencer/INPUT:Phys/StdLooseKsDD

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Phys/StdKs2PiPiDD

LoKi::VoidFilter/SELECT:Phys/StdKs2PiPiDD

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

FilterUnique/MergedKshortsDDForBu2LLK

|                 |                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                               |
| Inputs          | [ 'Phys/StdKs2PiPiDD' , 'Phys/[StdLooseKsDD](./stripping21r0p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                                              |
| Output          | Phys/MergedKshortsDDForBu2LLK/Particles                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/KshortsDDForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/MergedKshortsDDForBu2LLK' ]                                                                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/KshortsDDForBu2LLK/Particles                                                                                                              |

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
| Inputs          | [ 'Phys/StdLambda2PPiLL' , 'Phys/[StdVeryLooseLambdaLL](./stripping21r0p2-commonparticles-stdverylooselambdall)' ] |
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
| Inputs          | [ 'Phys/StdLambda2PPiDD' , 'Phys/[StdLooseLambdaDD](./stripping21r0p2-commonparticles-stdlooselambdadd)' ] |
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

GaudiSequencer/INPUT:KstarsPlusLLForBu2LLK

GaudiSequencer/MERGED:MergedKstarsPlusLLForBu2LLK

GaudiSequencer/MERGEDINPUTS:MergedKstarsPlusLLForBu2LLK

GaudiSequencer/INPUT:Phys/StdVeryLooseKsLL

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Phys/StdKs2PiPiLL

LoKi::VoidFilter/SELECT:Phys/StdKs2PiPiLL

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

FilterUnique/MergedKstarsPlusLLForBu2LLK

|                 |                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                       |
| Inputs          | [ 'Phys/StdKs2PiPiLL' , 'Phys/[StdVeryLooseKsLL](./stripping21r0p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                                      |
| Output          | Phys/MergedKstarsPlusLLForBu2LLK/Particles                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

CombineParticles/KstarsPlusLLForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergedKstarsPlusLLForBu2LLK' , 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))' , 'pi+' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' , 'pi-' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' } |
| CombinationCut   | (APT \> 400 \*MeV) & (ADAMASS('K\*(892)+') \< 300 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                              |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | [K\*(892)+ -\> KS0 pi+]cc                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                                                                                                                                                                                                              |
| Output           | Phys/KstarsPlusLLForBu2LLK/Particles                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KstarsPlusDDForBu2LLK

GaudiSequencer/MERGED:MergedKstarsPlusDDForBu2LLK

GaudiSequencer/MERGEDINPUTS:MergedKstarsPlusDDForBu2LLK

GaudiSequencer/INPUT:Phys/StdLooseKsDD

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Phys/StdKs2PiPiDD

LoKi::VoidFilter/SELECT:Phys/StdKs2PiPiDD

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

FilterUnique/MergedKstarsPlusDDForBu2LLK

|                 |                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                               |
| Inputs          | [ 'Phys/StdKs2PiPiDD' , 'Phys/[StdLooseKsDD](./stripping21r0p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                                              |
| Output          | Phys/MergedKstarsPlusDDForBu2LLK/Particles                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

CombineParticles/KstarsPlusDDForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergedKstarsPlusDDForBu2LLK' , 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))' , 'pi+' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' , 'pi-' : '(PT \> 400 \*MeV) & (M \< 2600\*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' } |
| CombinationCut   | (APT \> 400 \*MeV) & (ADAMASS('K\*(892)+') \< 300 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                              |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | [K\*(892)+ -\> KS0 pi+]cc                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                                                                                                                                                                                                              |
| Output           | Phys/KstarsPlusDDForBu2LLK/Particles                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KstarsPlusPi0ResForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

CombineParticles/KstarsPlusPi0ResForBu2LLK

|                  |                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' , 'Phys/[StdLooseResolvedPi0](./stripping21r0p2-commonparticles-stdlooseresolvedpi0)' ]                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 400 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' , 'K-' : '(PT \> 400 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' , 'pi0' : '(PT \> 600 \* MeV)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (ADAMASS('K\*(892)+') \< 300 \*MeV)                                                                                                                                |
| MotherCut        | (ADMASS('K\*(892)+') \< 300 \*MeV)                                                                                                                                                      |
| DecayDescriptor  | [K\*(892)+ -\> K+ pi0]cc                                                                                                                                                              |
| DecayDescriptors | [ '[K\*(892)+ -\> K+ pi0]cc' ]                                                                                                                                                      |
| Output           | Phys/KstarsPlusPi0ResForBu2LLK/Particles                                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:KstarsPlusPi0MrgForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

CombineParticles/KstarsPlusPi0MrgForBu2LLK

|                  |                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' , 'Phys/[StdLooseMergedPi0](./stripping21r0p2-commonparticles-stdloosemergedpi0)' ]                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 400 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' , 'K-' : '(PT \> 400 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9))' , 'pi0' : '(PT \> 600 \* MeV)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (ADAMASS('K\*(892)+') \< 300 \*MeV)                                                                                                                                |
| MotherCut        | (ADMASS('K\*(892)+') \< 300 \*MeV)                                                                                                                                                      |
| DecayDescriptor  | [K\*(892)+ -\> K+ pi0]cc                                                                                                                                                              |
| DecayDescriptors | [ '[K\*(892)+ -\> K+ pi0]cc' ]                                                                                                                                                      |
| Output           | Phys/KstarsPlusPi0MrgForBu2LLK/Particles                                                                                                                                                |

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
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21r0p2-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLooseProtons](./stripping21r0p2-commonparticles-stdalllooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                             |
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

GaudiSequencer/INPUT:pKsSSForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

CombineParticles/pKsSSForBu2LLK

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' , 'Phys/[StdLooseProtons](./stripping21r0p2-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.05)' , 'K-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNk \> 0.05)' , 'p+' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.05)' , 'p~-' : '(PT \> 250 \*MeV) & (P \> 2000 \*MeV) & (ISBASIC & (MIPCHI2DV(PRIMARY) \> 9) & (TRGHOSTPROB \< 0.35)) & (PROBNNp \> 0.05)' } |
| CombinationCut   | (APT \> 400 \*MeV) & (AM \< 5620 \*MeV) & (ADOCACHI2CUT( 30 , ''))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2) \< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/pKsSSForBu2LLK/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/MergeBu2LLK_ee2

|                 |                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                                                                                                   |
| Inputs          | [ 'Phys/KaonsForBu2LLK' , 'Phys/KshortsDDForBu2LLK' , 'Phys/KshortsLLForBu2LLK' , 'Phys/KstarsForBu2LLK' , 'Phys/KstarsPlusDDForBu2LLK' , 'Phys/KstarsPlusLLForBu2LLK' , 'Phys/KstarsPlusPi0MrgForBu2LLK' , 'Phys/KstarsPlusPi0ResForBu2LLK' , 'Phys/LambdasDDForBu2LLK' , 'Phys/LambdasLLForBu2LLK' , 'Phys/PhisForBu2LLK' , 'Phys/PionsForBu2LLK' , 'Phys/pKsForBu2LLK' , 'Phys/pKsSSForBu2LLK' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                  |
| Output          | Phys/MergeBu2LLK_ee2/Particles                                                                                                                                                                                                                                                                                                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/Bu2LLK_eeLine2

|                  |                                                                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_ee2' , 'Phys/SelDiElectronFromTracksForBu2LLK' ]                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'phi(1020)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 1500 \*MeV                                                                                                                                                                                                                                                                                                     |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 9) & (BPVIPCHI2() \< 25) & (BPVDIRA \> 0.9995) & (BPVVDCHI2 \> 100))                                                                                                                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[ B+ -\> J/psi(1S) K+ ]cc' , '[ B+ -\> J/psi(1S) pi+ ]cc' , '[ B+ -\> J/psi(1S) K\*(892)+ ]cc' , ' B0 -\> J/psi(1S) KS0 ' , '[ B0 -\> J/psi(1S) K\*(892)0 ]cc' , ' B_s0 -\> J/psi(1S) phi(1020) ' , '[ Lambda_b0 -\> J/psi(1S) Lambda0 ]cc' , '[ Lambda_b0 -\> J/psi(1S) Lambda(1520)0 ]cc' ]                  |
| Output           | Phys/Bu2LLK_eeLine2/Particles                                                                                                                                                                                                                                                                                                   |

AddRelatedInfo/RelatedInfo1_Bu2LLK_eeLine2

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo1_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo2_Bu2LLK_eeLine2

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo2_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo3_Bu2LLK_eeLine2

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo3_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo4_Bu2LLK_eeLine2

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo4_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo5_Bu2LLK_eeLine2

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo5_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo6_Bu2LLK_eeLine2

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo6_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo7_Bu2LLK_eeLine2

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo7_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo8_Bu2LLK_eeLine2

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo8_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo9_Bu2LLK_eeLine2

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo9_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo10_Bu2LLK_eeLine2

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                 |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo10_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo11_Bu2LLK_eeLine2

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                 |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo11_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo12_Bu2LLK_eeLine2

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                 |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo12_Bu2LLK_eeLine2/Particles |

AddRelatedInfo/RelatedInfo13_Bu2LLK_eeLine2

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine2' ]                 |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo13_Bu2LLK_eeLine2/Particles |
