[[stripping21 lines]](./stripping21-index)

# StrippingLowMultMuonLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | None                                |
| Postscale      | 1.0000000                           |
| HLT            | HLT_PASS('Hlt2LowMultMuonDecision') |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

**LoKi::VoidFilter/StrippingLowMultMuonLineVOIDFilter**

|      |                                                                                                                                                                                              |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \> 0) & (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) & (recSummary(LHCb.RecSummary.nTracks, 'Rec/Track/Best') \< 6) |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |
