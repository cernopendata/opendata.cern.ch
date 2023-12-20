[[stripping21 lines]](./stripping21-index)

# StrippingD02KSKSDDLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/D02KSKSDDLine/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/selKS2DD_KSforD02KSKSDD

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (log((CHILD(BPVIPCHI2(),1)\*CHILD(BPVIPCHI2(),2))/(BPVIPCHI2()\*BPVIPCHI2() + DOCAMAX\*DOCAMAX)) \> 0.0)&(BPVLTSIGNCHI2() \> 50.0)&(CHILD(TRGHOSTPROB, 1) \<=1.0 )&(CHILD(TRGHOSTPROB, 2) \<=1.0 ) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' ]                                                                                                                            |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/selKS2DD_KSforD02KSKSDD/Particles                                                                                                                                                             |

CombineParticles/D02KSKSDDLine

|                  |                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/selKS2DD_KSforD02KSKSDD' ]                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(log((CHILD(BPVIPCHI2(),1)\*CHILD(BPVIPCHI2(),2))/(BPVIPCHI2()\*BPVIPCHI2() + DOCAMAX\*DOCAMAX)) \> 4.0)' } |
| CombinationCut   | (ACUTDOCA(4.0\*mm,''))&(ADAMASS('D0') \< 150.0\*MeV)                                                                                |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20.0)&(BPVIPCHI2() \< 10.0)&(log(PT\*CHILD(PT,1)\*CHILD(PT,2)) \> 21.0) &(ADMASS('D0') \< 100.0\*MeV)        |
| DecayDescriptor  | None                                                                                                                                |
| DecayDescriptors | [ 'D0 -\> KS0 KS0' ]                                                                                                              |
| Output           | Phys/D02KSKSDDLine/Particles                                                                                                        |
