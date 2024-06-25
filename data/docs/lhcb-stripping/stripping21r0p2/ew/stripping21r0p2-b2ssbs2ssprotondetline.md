[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2SSBs2SSProtonDetLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2SSBs2SSProtonDetLine/Particles |
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

**CombineParticles/DetachedProtonPairForB2SS**

|                  |                                                                 |
|------------------|-----------------------------------------------------------------|
| Inputs           | [ 'Phys/ProtonsForB2SS' ]                                     |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'p\~-' : 'ALL' }                  |
| CombinationCut   | (AMAXDOCA('')\<0.25\*mm) &(ASUM(PT)\>2000\*MeV)                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 2)& (BPVVDCHI2 \> 50)& (BPVIPCHI2()\> 50) |
| DecayDescriptor  | KS0 -\> p+ p\~-                                                 |
| DecayDescriptors | [ 'KS0 -\> p+ p\~-' ]                                         |
| Output           | Phys/DetachedProtonPairForB2SS/Particles                        |

**CombineParticles/B2SSBs2SSProtonDetLine**

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedProtonPairForB2SS' ]                                                |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }                                                        |
| CombinationCut   | (ASUM(PT)\>3500\*MeV) & (AM\>4600\*MeV) & (AM\<6000\*MeV) & ( abs(MS1-MS2)\<60\*MeV ) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 5)& (BPVDIRA \> 0.0)& (BPVVDCHI2\> 50)& (BPVIPCHI2()\< 15)      |
| DecayDescriptor  | B_s0 -\> KS0 KS0                                                                      |
| DecayDescriptors | [ 'B_s0 -\> KS0 KS0' ]                                                              |
| Output           | Phys/B2SSBs2SSProtonDetLine/Particles                                                 |
