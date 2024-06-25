[[stripping21 lines]](./stripping21-index)

# StrippingWMuControl4800Line

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/WMuControl4800Line/Particles       |
| Postscale      | 1.0000000                               |
| HLT            | HLT_PASS('Hlt2SingleMuonLowPTDecision') |
| Prescale       | 0.40000000                              |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

**FilterDesktop/WMuControl4800Line**

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | (PT\>4.8\*GeV)                                                    |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                              |
| Output          | Phys/WMuControl4800Line/Particles                                 |
