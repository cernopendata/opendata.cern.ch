[[stripping21r1 lines]](./stripping21r1-index)

# StrippingWMuLowLine

## Properties:

|                |                           |
|----------------|---------------------------|
| OutputLocation | Phys/WMuLowLine/Particles |
| Postscale      | 1.0000000                 |
| HLT            | None                      |
| Prescale       | 0.10000000                |
| L0DU           | None                      |
| ODIN           | None                      |

## Filter sequence:

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) /Particles')\>0 |

**FilterDesktop/WMuLowLine**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (PT\>15.0\*GeV)                                                     |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/WMuLowLine/Particles                                           |
