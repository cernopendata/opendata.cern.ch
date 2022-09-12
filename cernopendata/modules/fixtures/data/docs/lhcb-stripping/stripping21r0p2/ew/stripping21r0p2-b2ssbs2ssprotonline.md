[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2SSBs2SSProtonLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B2SSBs2SSProtonLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionEW**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamEWBadEvent') & \~ALG_PASSED('StrippingStreamEWBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseProtons**

|      |                                        |
|------|----------------------------------------|
| Code | 0 StdAllLooseProtons /Particles',True) |

**FilterDesktop/ProtonsForB2SS**

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PIDp \> 3.5) &( PT \> 1250\*MeV)& ( MIPCHI2DV(PRIMARY)\> 55)             |
| Inputs          | [ 'Phys/ [StdAllLooseProtons](./stripping21r0p2-stdalllooseprotons) ' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/ProtonsForB2SS/Particles                                             |

**DaVinci::N4BodyDecays/B2SSBs2SSProtonLine**

|                  |                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ProtonsForB2SS' ]                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'p\~-' : 'ALL' }                                                                                                                               |
| CombinationCut   | (AM\>4600\*MeV) & (AM\<6000\*MeV) & (( (abs(MYAM12-MYAM34)\< 100\*MeV) \| (abs(MYAM13-MYAM24)\< 100\*MeV) \| (abs(MYAM14-MYAM23)\< 100\*MeV) ))& ((AMAXDOCA('')\< 0.3\*mm) ) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 9)& (BPVDIRA \> 0)& (BPVVDCHI2\> 100)& (BPVIPCHI2()\< 15)                                                                                              |
| DecayDescriptor  | B_s0 -\> p+ p\~- p+ p\~-                                                                                                                                                     |
| DecayDescriptors | [ 'B_s0 -\> p+ p\~- p+ p\~-' ]                                                                                                                                             |
| Output           | Phys/B2SSBs2SSProtonLine/Particles                                                                                                                                           |
