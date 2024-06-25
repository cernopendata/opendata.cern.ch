[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLLP2JetsSingleHighMassLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/LLP2JetsSingleHighMassLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT1           | None                                      |
| HLT2           | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

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

LoKi::VoidFilter/SELECT:Phys/StdJetsVtxAlg

|      |     |
|------|-----|
| Code | 0   |

FilterDesktop/LLP2JetsSingleHighMassLine

|                 |                                                                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 10000.0)& (NINTREE(ISBASIC & HASTRACK & ISLONG & (25 \< MIPCHI2DV(PRIMARY))) \> 5)& (SUMTREE( ('D0'==ABSID) & (0.9 \< abs(VFASPF(VX_BEAMSPOTRHO(0.6)))), NDAUGS) \>= 9) |
| Inputs          | [ 'Phys/StdJetsVtxAlg' ]                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                           |
| Output          | Phys/LLP2JetsSingleHighMassLine/Particles                                                                                                                                      |
