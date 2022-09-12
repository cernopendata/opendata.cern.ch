[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingWMuIsoLine

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/WMuIsoFilter/Particles |
| Postscale      | 1.0000000                   |
| HLT1           | None                        |
| HLT2           | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

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

**FilterDesktop/WMuIsoLine**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PT \> 15000.0)                                                       |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p2-stdallloosemuons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/WMuIsoLine/Particles                                             |

**AddRelatedInfo/RelatedInfo1_WMuIsoLine**

|                 |                                        |
|-----------------|----------------------------------------|
| Inputs          | [ 'Phys/WMuIsoLine' ]                |
| DecayDescriptor | None                                   |
| Output          | Phys/RelatedInfo1_WMuIsoLine/Particles |

**FilterDesktop/WMuIsoFilter**

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Code            | RELINFO('/Event/Phys/WMuIsoLine/Iso', 'CONEPT', 100000.) \< 4000.0 |
| Inputs          | [ 'Phys/WMuIsoLine' ]                                            |
| DecayDescriptor | None                                                               |
| Output          | Phys/WMuIsoFilter/Particles                                        |

**AddRelatedInfo/RelatedInfo1_WMuIsoFilter**

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/WMuIsoFilter' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo1_WMuIsoFilter/Particles |
