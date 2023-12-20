[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLLP2JetsSingleLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/LLP2JetsSingleLine/Particles |
| Postscale      | 1.0000000                         |
| HLT1           | None                              |
| HLT2           | None                              |
| Prescale       | 0.010000000                       |
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

LoKi::VoidFilter/SELECT:Phys/StdJets

|      |                           |
|------|---------------------------|
| Code | 0StdJets/Particles',True) |

FilterDesktop/LLP2JetsSingleLine

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 10000.0)& (NINTREE(ISBASIC & HASTRACK & ISLONG & (25 \< MIPCHI2DV(PRIMARY))) \> 4) |
| Inputs          | [ 'Phys/[StdJets](./stripping21r1p2-commonparticles-stdjets)' ]                         |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/LLP2JetsSingleLine/Particles                                                         |
