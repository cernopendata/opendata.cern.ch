[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingCaloLowMultElectronLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | None                                    |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | HLT_PASS('Hlt2LowMultElectronDecision') |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionEW**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamEWBadEvent') & \~ALG_PASSED('StrippingStreamEWBadEvent') |

**LoKi::VoidFilter/StrippingCaloLowMultElectronLineVOIDFilter**

|      |                                                                                                                                |
|------|--------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) & (recSummary(LHCb.RecSummary.nTracks, 'Rec/Track/Best') \< 6) |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |
