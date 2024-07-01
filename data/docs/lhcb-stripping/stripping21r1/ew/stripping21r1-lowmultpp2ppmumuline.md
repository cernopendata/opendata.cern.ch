[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLowMultPP2PPMuMuLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | None                                   |
| Postscale      | 1.0000000                              |
| HLT            | HLT_PASS('Hlt2diPhotonDiMuonDecision') |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

**LoKi::VoidFilter/StrippingLowMultPP2PPMuMuLineVOIDFilter**

|      |                                                                                                                               |
|------|-------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \> 0) & (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |
