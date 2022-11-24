[[stripping21 lines]](./stripping21-index)

# StrippingWMuSingleTrackNoBiasLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/WMuSingleTrackNoBiasLine/Particles |
| Postscale      | 1.0000000                               |
| HLT            | HLT_PASS( 'Hlt1MBNoBiasDecision' )      |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsMuons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsMuons](./stripping21-stdallnopidsmuons) /Particles')\>0 |

**FilterDesktop/WMuSingleTrackNoBiasLine**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (PT\>15.0\*GeV)                                                     |
| Inputs          | [ 'Phys/ [StdAllNoPIDsMuons](./stripping21-stdallnopidsmuons) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/WMuSingleTrackNoBiasLine/Particles                             |
