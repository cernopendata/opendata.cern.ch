[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLLP2JetsDoubleLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/LLP2JetsDoubleLine/Particles |
| Postscale      | 1.0000000                         |
| HLT1           | None                              |
| HLT2           | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

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

GaudiSequencer/MERGED:LLP2JetsDoubleLine

GaudiSequencer/MERGEDINPUTS:LLP2JetsDoubleLine

GaudiSequencer/INPUT:LIMIT_2/10000000000:NoVtxJetsLLP2Jets

LoKi::VoidFilter/SELECT:Phys/StdJets

|      |                           |
|------|---------------------------|
| Code | 0StdJets/Particles',True) |

FilterDesktop/NoVtxJetsLLP2Jets

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 10000.0)& (NINTREE(ISBASIC & HASTRACK & ISLONG & (25 \< MIPCHI2DV(PRIMARY))) \> 4) |
| Inputs          | [ 'Phys/[StdJets](./stripping21r0p2-commonparticles-stdjets)' ]                         |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/NoVtxJetsLLP2Jets/Particles                                                          |

LoKi::VoidFilter/LIMIT_2/10000000000:NoVtxJetsLLP2Jets

|      |                                                                           |
|------|---------------------------------------------------------------------------|
| Code | in_range(2,CONTAINS('Phys/NoVtxJetsLLP2Jets/Particles',True),10000000000) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/LLP2JetsDoubleLine

|                 |                                   |
|-----------------|-----------------------------------|
| Code            | ALL                               |
| Inputs          | [ 'Phys/NoVtxJetsLLP2Jets' ]    |
| DecayDescriptor | None                              |
| Output          | Phys/LLP2JetsDoubleLine/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |
