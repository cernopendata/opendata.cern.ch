[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2SSBu2KSSElectronDetLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/B2SSBu2KSSElectronDetLine/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

**CombineParticles/DetachedElectronPairForB2SS**

|                  |                                                                  |
|------------------|------------------------------------------------------------------|
| Inputs           | [ 'Phys/ElectronsForB2SS' ]                                    |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                     |
| CombinationCut   | (AMAXDOCA('')\<0.5\*mm) &(ASUM(PT)\>50\*MeV)                     |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 16)& (BPVVDCHI2 \> 15)& (BPVIPCHI2()\> 10) |
| DecayDescriptor  | KS0 -\> e+ e-                                                    |
| DecayDescriptors | [ 'KS0 -\> e+ e-' ]                                            |
| Output           | Phys/DetachedElectronPairForB2SS/Particles                       |

**CombineParticles/B2SSBu2KSSElectronDetLine**

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedElectronPairForB2SS' , 'Phys/KaonsForB2SS' ]                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                          |
| CombinationCut   | (ASUM(PT)\>3500\*MeV) & (AM\>4600\*MeV) & (AM\<6000\*MeV) & ( abs(MS1-MS2)\<60\*MeV ) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 5)& (BPVDIRA \> 0.0)& (BPVVDCHI2\> 50)& (BPVIPCHI2()\< 15)      |
| DecayDescriptor  | [B+ -\> K+ KS0 KS0]cc                                                               |
| DecayDescriptors | [ '[B+ -\> K+ KS0 KS0]cc' ]                                                       |
| Output           | Phys/B2SSBu2KSSElectronDetLine/Particles                                              |
