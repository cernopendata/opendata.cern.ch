[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingInclusiveDoubleDLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/InclusiveDoubleDLine/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharmCompleteEvent

|      |                                                                                                                      |
|------|----------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamCharmCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:InclusiveDoubleDMergedCharm

GaudiSequencer/MERGEDINPUTS:InclusiveDoubleDMergedCharm

GaudiSequencer/INPUT:InclusiveDoubleD_D_MVAFilter

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/InclusiveDoubleDDetachedLongPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/InclusiveDoubleDDetachedLongPions/Particles                                      |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/InclusiveDoubleDDetachedLongKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/InclusiveDoubleDDetachedLongKaons/Particles                                      |

DaVinci::N3BodyDecays/InclusiveDoubleDProtoD

|                  |                                                                                                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/InclusiveDoubleDDetachedLongKaons' , 'Phys/InclusiveDoubleDDetachedLongPions' ]                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('D+') \< 50\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\| ((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,3)\<0.5\*mm) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (CHI2VXNDF\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0) & (ADMASS('D+') \< 32\*MeV)                                                                                                                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ '[D+ -\> K- pi+ pi+]cc' ]                                                                                                                                                                                                                                               |
| Output           | Phys/InclusiveDoubleDProtoD/Particles                                                                                                                                                                                                                                         |

FilterDesktop/InclusiveDoubleD_D_MVAFilter

|                 |                                              |
|-----------------|----------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/D_BDT')\>0.05 |
| Inputs          | [ 'Phys/InclusiveDoubleDProtoD' ]          |
| DecayDescriptor | None                                         |
| Output          | Phys/InclusiveDoubleD_D_MVAFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:InclusiveDoubleD_D0_MVAFilter

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/InclusiveDoubleDDetachedLongPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/InclusiveDoubleDDetachedLongPions/Particles                                      |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/InclusiveDoubleDDetachedLongKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/InclusiveDoubleDDetachedLongKaons/Particles                                      |

CombineParticles/InclusiveDoubleDProtoD0

|                  |                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/InclusiveDoubleDDetachedLongKaons' , 'Phys/InclusiveDoubleDDetachedLongPions' ]                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                           |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('D0') \< 60\*MeV) & (ADOCA(1,2)\<0.5\*mm) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV)))) |
| MotherCut        | (CHI2VXNDF\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0) & (ADMASS('D0') \< 32\*MeV)                                                                                           |
| DecayDescriptor  | None                                                                                                                                                                   |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                                                                                            |
| Output           | Phys/InclusiveDoubleDProtoD0/Particles                                                                                                                                 |

FilterDesktop/InclusiveDoubleD_D0_MVAFilter

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/D0_BDT')\>0.15 |
| Inputs          | [ 'Phys/InclusiveDoubleDProtoD0' ]          |
| DecayDescriptor | None                                          |
| Output          | Phys/InclusiveDoubleD_D0_MVAFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:InclusiveDoubleD_Ds_MVAFilter

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/InclusiveDoubleDDetachedLongPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/InclusiveDoubleDDetachedLongPions/Particles                                      |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/InclusiveDoubleDDetachedLongKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/InclusiveDoubleDDetachedLongKaons/Particles                                      |

DaVinci::N3BodyDecays/InclusiveDoubleDProtoDs

|                  |                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/InclusiveDoubleDDetachedLongKaons' , 'Phys/InclusiveDoubleDDetachedLongPions' ]                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                    |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('D_s+') \< 50\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\| ((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,3)\<0.5\*mm) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (CHI2VXNDF\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0) & (ADMASS('D_s+') \< 32\*MeV)                                                                                                                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[D_s+ -\> K+ K- pi+]cc' ]                                                                                                                                                                                                                                                |
| Output           | Phys/InclusiveDoubleDProtoDs/Particles                                                                                                                                                                                                                                          |

FilterDesktop/InclusiveDoubleD_Ds_MVAFilter

|                 |                                              |
|-----------------|----------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/Ds_BDT')\>0.4 |
| Inputs          | [ 'Phys/InclusiveDoubleDProtoDs' ]         |
| DecayDescriptor | None                                         |
| Output          | Phys/InclusiveDoubleD_Ds_MVAFilter/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/InclusiveDoubleDMergedCharm

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                     |
| Inputs          | [ 'Phys/InclusiveDoubleD_D0_MVAFilter' , 'Phys/InclusiveDoubleD_D_MVAFilter' , 'Phys/InclusiveDoubleD_Ds_MVAFilter' ] |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/InclusiveDoubleDMergedCharm/Particles                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/InclusiveDoubleDLine

|                  |                                                                                                                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/InclusiveDoubleDMergedCharm' ]                                                                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'D~0' : 'ALL' }                                                                                                                                                                          |
| CombinationCut   | AM \> 0                                                                                                                                                                                                                                                                                |
| MotherCut        | (CHI2VXNDF\<10)                                                                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ 'B0 -\> D0 D~0' , '[B0 -\> D0 D0]cc' , '[B0 -\> D0 D+]cc' , '[B0 -\> D0 D-]cc' , '[B0 -\> D0 D_s+]cc' , '[B0 -\> D0 D_s-]cc' , 'B0 -\> D+ D-' , '[B0 -\> D+ D+]cc' , '[B0 -\> D+ D_s+]cc' , '[B0 -\> D+ D_s-]cc' , 'B0 -\> D_s+ D_s-' , '[B0 -\> D_s+ D_s+]cc' ] |
| Output           | Phys/InclusiveDoubleDLine/Particles                                                                                                                                                                                                                                                    |
