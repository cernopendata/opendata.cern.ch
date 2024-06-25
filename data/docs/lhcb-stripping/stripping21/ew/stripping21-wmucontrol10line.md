[[stripping21 lines]](./stripping21-index)

# StrippingWMuControl10Line

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/WMuControl10Line/Particles          |
| Postscale      | 1.0000000                                |
| HLT            | HLT_PASS('Hlt2SingleMuonHighPTDecision') |
| Prescale       | 0.010000000                              |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

**FilterDesktop/WMuControl10Line**

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | (PT\>10.0\*GeV)                                                   |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                              |
| Output          | Phys/WMuControl10Line/Particles                                   |
