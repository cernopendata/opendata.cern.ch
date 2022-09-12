[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2SSB2KstSSKaonDetLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2SSB2KstSSKaonDetLine/Particles |
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

**LoKi::VoidFilter/SELECT:Phys/StdLooseKstar2Kpi**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseKstar2Kpi /Particles',True) |

**FilterDesktop/KstarsForB2SS**

|                 |                                                                                                                                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( PT \> 1250\*MeV)& ( MIPCHI2DV(PRIMARY)\> 55)& (PT \> 2000\*MeV )& (M \< ( 892\*MeV + 130\*MeV ) )& (M \> ( 892\*MeV - 130\*MeV ) )& (VFASPF(VCHI2/VDOF) \< 2.5 )& ( CHILD( MIPCHI2DV(PRIMARY), 1) \> 55 ) & ( CHILD( MIPCHI2DV(PRIMARY), 2) \> 55 ) & (BPVVDCHI2 \> 50 ) |
| Inputs          | [ 'Phys/ [StdLooseKstar2Kpi](./stripping21r0p2-stdloosekstar2kpi) ' ]                                                                                                                                                                                                    |
| DecayDescriptor | None                                                                                                                                                                                                                                                                       |
| Output          | Phys/KstarsForB2SS/Particles                                                                                                                                                                                                                                               |

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

**CombineParticles/B2SSB2KstSSKaonDetLine**

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedKaonPairForB2SS' , 'Phys/KstarsForB2SS' ]                           |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' , 'KS0' : 'ALL' }          |
| CombinationCut   | (ASUM(PT)\>3500\*MeV) & (AM\>4600\*MeV) & (AM\<6000\*MeV) & ( abs(MS1-MS2)\<60\*MeV ) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 5)& (BPVDIRA \> 0.0)& (BPVVDCHI2\> 50)& (BPVIPCHI2()\< 15)      |
| DecayDescriptor  | [B0 -\> K\*(892)0 KS0 KS0]cc                                                        |
| DecayDescriptors | [ '[B0 -\> K\*(892)0 KS0 KS0]cc' ]                                                |
| Output           | Phys/B2SSB2KstSSKaonDetLine/Particles                                                 |
