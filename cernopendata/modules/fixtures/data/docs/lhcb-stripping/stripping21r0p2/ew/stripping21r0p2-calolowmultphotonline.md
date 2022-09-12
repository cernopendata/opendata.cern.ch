[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingCaloLowMultPhotonLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | None                                  |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | HLT_PASS('Hlt2LowMultPhotonDecision') |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionEW**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamEWBadEvent') & \~ALG_PASSED('StrippingStreamEWBadEvent') |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |
