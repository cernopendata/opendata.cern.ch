[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingWMuLowLine

## Properties:

|                |                           |
|----------------|---------------------------|
| OutputLocation | Phys/WMuLowLine/Particles |
| Postscale      | 1.0000000                 |
| HLT1           | None                      |
| HLT2           | None                      |
| Prescale       | 0.10000000                |
| L0DU           | None                      |
| ODIN           | None                      |

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

**FilterDesktop/WMuLowLine**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PT\>15000.0)                                                         |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p2-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/WMuLowLine/Particles                                             |
