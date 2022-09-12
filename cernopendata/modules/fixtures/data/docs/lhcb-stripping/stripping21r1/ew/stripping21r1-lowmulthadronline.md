[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLowMultHadronLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | None                                  |
| Postscale      | 1.0000000                             |
| HLT            | HLT_PASS('Hlt2LowMultHadronDecision') |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

**LoKi::VoidFilter/StrippingLowMultHadronLineVOIDFilter**

|      |                                                                                                                                                                   |
|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \> 1) & (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) & (CONTAINS('Rec/Track/Best') \< 6) |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |
