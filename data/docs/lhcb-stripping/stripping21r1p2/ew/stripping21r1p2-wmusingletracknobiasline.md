[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingWMuSingleTrackNoBiasLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/WMuSingleTrackNoBiasLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | HLT_PASS( 'Hlt1MBNoBiasDecision' )      |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

**FilterDesktop/WMuSingleTrackNoBiasLine**

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | (PT\>15000.0)                                                           |
| Inputs          | [ 'Phys/ [StdAllNoPIDsMuons](./stripping21r1p2-stdallnopidsmuons) ' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/WMuSingleTrackNoBiasLine/Particles                                 |
