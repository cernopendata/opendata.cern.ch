[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingInclusiveCharmBaryons_XicLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/InclusiveCharmBaryons_XicLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT1           | None                                         |
| HLT2           | None                                         |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:InclusiveCharmBaryonsMergedTracks

GaudiSequencer/MERGEDINPUTS:InclusiveCharmBaryonsMergedTracks

GaudiSequencer/INPUT:InclusiveCharmBaryonsDetachedLongPions

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/InclusiveCharmBaryonsDetachedLongPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/InclusiveCharmBaryonsDetachedLongPions/Particles                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:InclusiveCharmBaryonsDetachedLongKaons

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/InclusiveCharmBaryonsDetachedLongKaons

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)                                            |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p2-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/InclusiveCharmBaryonsDetachedLongKaons/Particles                                 |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:InclusiveCharmBaryonsDetachedLongProtons

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsProtons

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllNoPIDsProtons/Particles',True) |

FilterDesktop/InclusiveCharmBaryonsDetachedLongProtons

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)                                                |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r0p2-commonparticles-stdallnopidsprotons)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/InclusiveCharmBaryonsDetachedLongProtons/Particles                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/InclusiveCharmBaryonsMergedTracks

|                 |                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                   |
| Inputs          | [ 'Phys/InclusiveCharmBaryonsDetachedLongKaons' , 'Phys/InclusiveCharmBaryonsDetachedLongPions' , 'Phys/InclusiveCharmBaryonsDetachedLongProtons' ] |
| DecayDescriptor | None                                                                                                                                                  |
| Output          | Phys/InclusiveCharmBaryonsMergedTracks/Particles                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

DaVinci::N3BodyDecays/InclusiveCharmBaryonsProtoXic

|                  |                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/InclusiveCharmBaryonsMergedTracks' ]                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                      |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Xi_c+') \< 50\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\| ((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,3)\<0.5\*mm) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (CHI2VXNDF\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0) & (ADMASS('Xi_c+') \< 32\*MeV)                                                                                                                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[Xi_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                                                |
| Output           | Phys/InclusiveCharmBaryonsProtoXic/Particles                                                                                                                                                                                                                                     |

FilterDesktop/InclusiveCharmBaryons_XicLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/Xic_BDT')\>0.6 |
| Inputs          | [ 'Phys/InclusiveCharmBaryonsProtoXic' ]    |
| DecayDescriptor | None                                          |
| Output          | Phys/InclusiveCharmBaryons_XicLine/Particles  |
