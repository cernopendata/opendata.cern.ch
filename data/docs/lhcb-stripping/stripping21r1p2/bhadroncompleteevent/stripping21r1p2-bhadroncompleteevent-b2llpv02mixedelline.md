[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2LLPV02MixedElLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B2LLPV02MixedElLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

CombineParticles/V02HHNOIPElB2LLPV0

|                  |                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(P \> 2000.0) & (MIPCHI2DV(PRIMARY) \> 50.0) & (PROBNNe\>0.2)' , 'pi-' : '(P \> 2000.0) & (MIPCHI2DV(PRIMARY) \> 50.0) & (PROBNNe\>0.2)' } |
| CombinationCut   | ( ADOCACHI2CUT(15.0, '') )                                                                                                                                         |
| MotherCut        | ( CHI2VX \< 10.0 )                                                                                                                                                 |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                                                    |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                                                            |
| Output           | Phys/V02HHNOIPElB2LLPV0/Particles                                                                                                                                  |

CombineParticles/B2LLPV02MixedElLine

|                  |                                                    |
|------------------|----------------------------------------------------|
| Inputs           | [ 'Phys/V02HHNOIPElB2LLPV0' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(BPVIPCHI2()\> 25)' }      |
| CombinationCut   | (ASUM(PT)\>1000\*MeV) & ( abs(MS1-MS2)\<100\*MeV ) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 25)& (BPVVDCHI2\> 50)        |
| DecayDescriptor  | B0 -\> KS0 KS0                                     |
| DecayDescriptors | [ 'B0 -\> KS0 KS0' ]                             |
| Output           | Phys/B2LLPV02MixedElLine/Particles                 |
