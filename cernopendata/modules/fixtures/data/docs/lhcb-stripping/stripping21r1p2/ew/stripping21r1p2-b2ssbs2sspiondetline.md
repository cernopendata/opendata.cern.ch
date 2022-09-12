[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2SSBs2SSPionDetLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/B2SSBs2SSPionDetLine/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllLoosePions**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLoosePions /Particles',True) |

**FilterDesktop/PionsForB2SS**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | ( PT \> 1500\*MeV)& ( MIPCHI2DV(PRIMARY)\> 64)                        |
| Inputs          | [ 'Phys/ [StdAllLoosePions](./stripping21r1p2-stdallloosepions) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/PionsForB2SS/Particles                                           |

**CombineParticles/DetachedPionPairForB2SS**

|                  |                                                                 |
|------------------|-----------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForB2SS' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                  |
| CombinationCut   | (AMAXDOCA('')\<0.25\*mm) &(ASUM(PT)\>2000\*MeV)                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 2)& (BPVVDCHI2 \> 50)& (BPVIPCHI2()\> 50) |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                 |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                         |
| Output           | Phys/DetachedPionPairForB2SS/Particles                          |

**CombineParticles/B2SSBs2SSPionDetLine**

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedPionPairForB2SS' ]                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }                                                        |
| CombinationCut   | (ASUM(PT)\>3500\*MeV) & (AM\>4600\*MeV) & (AM\<6000\*MeV) & ( abs(MS1-MS2)\<60\*MeV ) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 5)& (BPVDIRA \> 0.0)& (BPVVDCHI2\> 50)& (BPVIPCHI2()\< 15)      |
| DecayDescriptor  | B_s0 -\> KS0 KS0                                                                      |
| DecayDescriptors | [ 'B_s0 -\> KS0 KS0' ]                                                              |
| Output           | Phys/B2SSBs2SSPionDetLine/Particles                                                   |
