[[stripping21 lines]](./stripping21-index)

# StrippingWMuLine

## Properties:

|                |                        |
|----------------|------------------------|
| OutputLocation | Phys/WMuLine/Particles |
| Postscale      | 1.0000000              |
| HLT            | None                   |
| Prescale       | 1.0000000              |
| L0DU           | None                   |
| ODIN           | None                   |

## Filter sequence:

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) /Particles')\>0 |

**FilterDesktop/WMuLine**

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | (PT\>20.0\*GeV)                                                   |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                              |
| Output          | Phys/WMuLine/Particles                                            |
