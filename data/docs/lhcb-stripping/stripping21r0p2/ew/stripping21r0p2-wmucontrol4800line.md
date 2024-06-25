[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingWMuControl4800Line

## Properties:

|                |                                                |
|----------------|------------------------------------------------|
| OutputLocation | Phys/WMuControl4800Line/Particles              |
| Postscale      | 1.0000000                                      |
| HLT1           | None                                           |
| HLT2           | HLT_PASS_RE('Hlt2.\*SingleMuonLow.\*Decision') |
| Prescale       | 0.40000000                                     |
| L0DU           | None                                           |
| ODIN           | None                                           |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**FilterDesktop/WMuControl4800Line**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PT\>4800.0)                                                          |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p2-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/WMuControl4800Line/Particles                                     |
