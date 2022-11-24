[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingWMuControl10Line

## Properties:

|                |                                                    |
|----------------|----------------------------------------------------|
| OutputLocation | Phys/WMuControl10Line/Particles                    |
| Postscale      | 1.0000000                                          |
| HLT1           | None                                               |
| HLT2           | HLT_PASS_RE('Hlt2.\*SingleMuon.\*High.\*Decision') |
| Prescale       | 0.010000000                                        |
| L0DU           | None                                               |
| ODIN           | None                                               |

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

**FilterDesktop/WMuControl10Line**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PT\>10000.0)                                                         |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1p2-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/WMuControl10Line/Particles                                       |
