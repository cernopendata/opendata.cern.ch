[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2SSBs2SSElectronLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2SSBs2SSElectronLine/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseElectrons**

|      |                                          |
|------|------------------------------------------|
| Code | 0 StdAllLooseElectrons /Particles',True) |

**FilterDesktop/ElectronsForB2SS**

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | ( PT \> 25\*MeV)& ( MIPCHI2DV(PRIMARY)\> 15)                                  |
| Inputs          | [ 'Phys/ [StdAllLooseElectrons](./stripping21r0p2-stdalllooseelectrons) ' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/ElectronsForB2SS/Particles                                               |

**DaVinci::N4BodyDecays/B2SSBs2SSElectronLine**

|                  |                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ElectronsForB2SS' ]                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                                                                                                                                 |
| CombinationCut   | (AM\>4600\*MeV) & (AM\<6000\*MeV) & (( (abs(MYAM12-MYAM34)\< 100\*MeV) \| (abs(MYAM13-MYAM24)\< 100\*MeV) \| (abs(MYAM14-MYAM23)\< 100\*MeV) ))& ((AMAXDOCA('')\< 0.3\*mm) ) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 9)& (BPVDIRA \> 0)& (BPVVDCHI2\> 100)& (BPVIPCHI2()\< 15)                                                                                              |
| DecayDescriptor  | B_s0 -\> e+ e- e+ e-                                                                                                                                                         |
| DecayDescriptors | [ 'B_s0 -\> e+ e- e+ e-' ]                                                                                                                                                 |
| Output           | Phys/B2SSBs2SSElectronLine/Particles                                                                                                                                         |
