[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBu2LLK_mmSSLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/Bu2LLK_mmSSLine/Particles |
| Postscale      | 1.0000000                      |
| HLT1           | None                           |
| HLT2           | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

LoKi::VoidFilter/StrippingBu2LLK_mmSSLineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

CombineParticles/MuMuSSForBu2LLK

|                  |                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21r1p2-commonparticles-stdloosemuons)' ]                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(PT \> 350) & (MIPCHI2DV(PRIMARY) \> 9)&(HASMUON)&(ISMUON)' , 'mu-' : '(PT \> 350) & (MIPCHI2DV(PRIMARY) \> 9)&(HASMUON)&(ISMUON)' } |
| CombinationCut   | (AM \> 100\*MeV)                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9)                                                                                                                                    |
| DecayDescriptor  | [J/psi(1S) -\> mu+ mu+]cc                                                                                                                                  |
| DecayDescriptors | [ '[J/psi(1S) -\> mu+ mu+]cc' ]                                                                                                                          |
| Output           | Phys/MuMuSSForBu2LLK/Particles                                                                                                                               |

FilterDesktop/SelMuMuSSForBu2LLK

|                 |                                                                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ID=='J/psi(1S)') & (PT \> 0 \*MeV) & (MM \< 5500 \*MeV) & (MINTREE(ABSID\<14,PT) \> 500 \*MeV) & (MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY)) \> 9) & (VFASPF(VCHI2/VDOF) \< 9) & (BPVVDCHI2 \> 16) & (MIPCHI2DV(PRIMARY) \> 0) & (2 == NINTREE((ABSID==13)&(HASMUON)&(ISMUON))) |
| Inputs          | [ 'Phys/MuMuSSForBu2LLK' ]                                                                                                                                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                                                                        |
| Output          | Phys/SelMuMuSSForBu2LLK/Particles                                                                                                                                                                                                                                           |

GaudiSequencer/MERGED:MergeBu2LLK_mmSS

GaudiSequencer/MERGEDINPUTS:MergeBu2LLK_mmSS

GaudiSequencer/INPUT:PionsForBu2LLK

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

FilterDesktop/PionsForBu2LLK

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                  |
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
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ]                                                                  |
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
| Inputs          | [ 'Phys/StdKs2PiPiLL' , 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
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
| Inputs          | [ 'Phys/StdKs2PiPiDD' , 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' ] |
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
| Inputs          | [ 'Phys/StdKs2PiPiLL' , 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
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
| Inputs           | [ 'Phys/MergedKstarsPlusLLForBu2LLK' , 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                                                                                                                                               |
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
| Inputs          | [ 'Phys/StdKs2PiPiDD' , 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' ] |
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
| Inputs           | [ 'Phys/MergedKstarsPlusDDForBu2LLK' , 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                                                                                                                                               |
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
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' , 'Phys/[StdLooseResolvedPi0](./stripping21r1p2-commonparticles-stdlooseresolvedpi0)' ]                     |
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
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' , 'Phys/[StdLooseMergedPi0](./stripping21r1p2-commonparticles-stdloosemergedpi0)' ]                         |
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
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' , 'Phys/[StdLooseProtons](./stripping21r1p2-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                                         |
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

FilterDesktop/MergeBu2LLK_mmSS

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Inputs          | [ 'Phys/K2ForBu2LLK' , 'Phys/KKsForBu2LLK' , 'Phys/KKsSSForBu2LLK' , 'Phys/KPisForBu2LLK' , 'Phys/KaonsForBu2LLK' , 'Phys/KshortsDDForBu2LLK' , 'Phys/KshortsLLForBu2LLK' , 'Phys/KstarsForBu2LLK' , 'Phys/KstarsPlusDDForBu2LLK' , 'Phys/KstarsPlusLLForBu2LLK' , 'Phys/KstarsPlusPi0MrgForBu2LLK' , 'Phys/KstarsPlusPi0ResForBu2LLK' , 'Phys/LambdasDDForBu2LLK' , 'Phys/LambdasLLForBu2LLK' , 'Phys/PhisForBu2LLK' , 'Phys/PionsForBu2LLK' , 'Phys/pKsForBu2LLK' , 'Phys/pKsSSForBu2LLK' , 'Phys/pPisForBu2LLK' , 'Phys/ppsForBu2LLK' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Output          | Phys/MergeBu2LLK_mmSS/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/Bu2LLK_mmSSLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_mmSS' , 'Phys/SelMuMuSSForBu2LLK' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K\*\_0(1430)0' : 'ALL' , 'K\*\_0(1430)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'K_1(1270)+' : 'ALL' , 'K_1(1270)-' : 'ALL' , 'K_2(1770)+' : 'ALL' , 'K_2(1770)-' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'N(1440)0' : 'ALL' , 'N(1440)~0' : 'ALL' , "f'\_2(1525)" : 'ALL' , 'f_2(1950)' : 'ALL' , 'phi(1020)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'rho(770)0' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 1500 \*MeV                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 9) & (BPVIPCHI2() \< 25) & (BPVDIRA \> 0.9995) & (BPVVDCHI2 \> 100))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[ B+ -\> J/psi(1S) K+ ]cc' , '[ B+ -\> J/psi(1S) pi+ ]cc' , '[ B+ -\> J/psi(1S) K\*(892)+ ]cc' , '[ B+ -\> J/psi(1S) K_1(1270)+ ]cc' , '[ B+ -\> J/psi(1S) K_2(1770)+ ]cc' , ' B0 -\> J/psi(1S) KS0 ' , ' B0 -\> J/psi(1S) rho(770)0 ' , '[ B0 -\> J/psi(1S) K\*(892)0 ]cc' , '[ B0 -\> J/psi(1S) K\*\_0(1430)0 ]cc' , ' B_s0 -\> J/psi(1S) phi(1020) ' , " B_s0 -\> J/psi(1S) f'\_2(1525) " , ' B_s0 -\> J/psi(1S) f_2(1950) ' , '[ Lambda_b0 -\> J/psi(1S) Lambda0 ]cc' , '[ Lambda_b0 -\> J/psi(1S) N(1440)0 ]cc' , '[ Lambda_b0 -\> J/psi(1S) Lambda(1520)0 ]cc' ] |
| Output           | Phys/Bu2LLK_mmSSLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

AddRelatedInfo/RelatedInfo1_Bu2LLK_mmSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo1_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2LLK_mmSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo2_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2LLK_mmSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo3_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2LLK_mmSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo4_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo5_Bu2LLK_mmSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo5_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo6_Bu2LLK_mmSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo6_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo7_Bu2LLK_mmSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo7_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo8_Bu2LLK_mmSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo8_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo9_Bu2LLK_mmSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo9_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo10_Bu2LLK_mmSSLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo10_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo11_Bu2LLK_mmSSLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo11_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo12_Bu2LLK_mmSSLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo12_Bu2LLK_mmSSLine/Particles |

AddRelatedInfo/RelatedInfo13_Bu2LLK_mmSSLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_mmSSLine' ]                 |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo13_Bu2LLK_mmSSLine/Particles |
