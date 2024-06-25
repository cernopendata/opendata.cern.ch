[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingWMuSingleTrackNoBiasLinePS

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/WMuSingleTrackNoBiasLinePS/Particles |
| Postscale      | 1.0000000                                 |
| HLT1           | HLT_PASS( 'Hlt1MBNoBiasDecision' )        |
| HLT2           | None                                      |
| Prescale       | 0.20000000                                |
| L0DU           | None                                      |
| ODIN           | None                                      |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsMuons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsMuons /Particles',True) |

**FilterDesktop/WMuSingleTrackNoBiasLinePS**

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | (PT\>5000.0)                                                            |
| Inputs          | [ 'Phys/ [StdAllNoPIDsMuons](./stripping21r1p2-stdallnopidsmuons) ' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/WMuSingleTrackNoBiasLinePS/Particles                               |
