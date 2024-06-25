[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLLP2JetsSingleLowMassLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/LLP2JetsSingleLowMassLine/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

FilterDesktop/LLP2JetsSingleLowMassLine

|                 |                                                                                                                                                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 15000.0)& (NINTREE(ISBASIC & HASTRACK & ISLONG & (25 \< MIPCHI2DV(PRIMARY))) \> 5)& (NINGENERATION( ('D0'==ABSID) & (0.9\< abs(VFASPF(VX_BEAMSPOTRHO(0.6)))), 1) \>= 3)& (SUMTREE( ('D0'==ABSID) & (0.9 \< abs(VFASPF(VX_BEAMSPOTRHO(0.6)))), NDAUGS ) \>= 7) |
| Inputs          | [ 'Phys/StdJetsVtxAlg' ]                                                                                                                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                                                                                                                 |
| Output          | Phys/LLP2JetsSingleLowMassLine/Particles                                                                                                                                                                                                                             |
