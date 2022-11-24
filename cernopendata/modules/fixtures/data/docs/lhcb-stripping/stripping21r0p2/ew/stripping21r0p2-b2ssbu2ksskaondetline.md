[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2SSBu2KSSKaonDetLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2SSBu2KSSKaonDetLine/Particles |
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

**CombineParticles/DetachedKaonPairForB2SS**

|                  |                                                                 |
|------------------|-----------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForB2SS' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                    |
| CombinationCut   | (AMAXDOCA('')\<0.25\*mm) &(ASUM(PT)\>2000\*MeV)                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 2)& (BPVVDCHI2 \> 50)& (BPVIPCHI2()\> 50) |
| DecayDescriptor  | KS0 -\> K+ K-                                                   |
| DecayDescriptors | [ 'KS0 -\> K+ K-' ]                                           |
| Output           | Phys/DetachedKaonPairForB2SS/Particles                          |

**CombineParticles/B2SSBu2KSSKaonDetLine**

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedKaonPairForB2SS' , 'Phys/KaonsForB2SS' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                          |
| CombinationCut   | (ASUM(PT)\>3500\*MeV) & (AM\>4600\*MeV) & (AM\<6000\*MeV) & ( abs(MS1-MS2)\<60\*MeV ) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 5)& (BPVDIRA \> 0.0)& (BPVVDCHI2\> 50)& (BPVIPCHI2()\< 15)      |
| DecayDescriptor  | [B+ -\> K+ KS0 KS0]cc                                                               |
| DecayDescriptors | [ '[B+ -\> K+ KS0 KS0]cc' ]                                                       |
| Output           | Phys/B2SSBu2KSSKaonDetLine/Particles                                                  |
