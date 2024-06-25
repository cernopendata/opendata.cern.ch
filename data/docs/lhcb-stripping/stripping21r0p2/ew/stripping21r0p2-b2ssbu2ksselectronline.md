[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2SSBu2KSSElectronLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2SSBu2KSSElectronLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseKaons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseKaons /Particles',True) |

**FilterDesktop/KaonsForB2SS**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PIDK \> 0) &( PT \> 1250\*MeV)& ( MIPCHI2DV(PRIMARY)\> 55)           |
| Inputs          | [ 'Phys/ [StdAllLooseKaons](./stripping21r0p2-stdallloosekaons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/KaonsForB2SS/Particles                                           |

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

**DaVinci::N5BodyDecays/B2SSBu2KSSElectronLine**

|                  |                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ElectronsForB2SS' , 'Phys/KaonsForB2SS' ]                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                                                                                                   |
| CombinationCut   | (AM\>4600\*MeV) & (AM\<6000\*MeV) & (( (abs(MYAM12-MYAM34)\< 100\*MeV) \| (abs(MYAM13-MYAM24)\< 100\*MeV) \| (abs(MYAM14-MYAM23)\< 100\*MeV) ))& ((AMAXDOCA('')\< 0.3\*mm) ) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 9)& (BPVDIRA \> 0)& (BPVVDCHI2\> 100)& (BPVIPCHI2()\< 15)                                                                                              |
| DecayDescriptor  | [B+ -\> e+ e- e+ e- K+]cc                                                                                                                                                  |
| DecayDescriptors | [ '[B+ -\> e+ e- e+ e- K+]cc' ]                                                                                                                                          |
| Output           | Phys/B2SSBu2KSSElectronLine/Particles                                                                                                                                        |
