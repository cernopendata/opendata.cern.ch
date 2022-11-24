[[stripping21r1 lines]](./stripping21r1-index)

# StrippingWMuSingleTrackNoBiasLinePS

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/WMuSingleTrackNoBiasLinePS/Particles |
| Postscale      | 1.0000000                                 |
| HLT            | HLT_PASS( 'Hlt1MBNoBiasDecision' )        |
| Prescale       | 0.20000000                                |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsMuons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsMuons](./stripping21r1-stdallnopidsmuons) /Particles')\>0 |

**FilterDesktop/WMuSingleTrackNoBiasLinePS**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PT\>5.0\*GeV)                                                        |
| Inputs          | [ 'Phys/ [StdAllNoPIDsMuons](./stripping21r1-stdallnopidsmuons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/WMuSingleTrackNoBiasLinePS/Particles                             |
