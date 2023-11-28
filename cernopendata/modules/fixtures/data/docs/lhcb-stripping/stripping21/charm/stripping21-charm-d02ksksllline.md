[[stripping21 lines]](./stripping21-index)

# StrippingD02KSKSLLLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/D02KSKSLLLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/selKS2LL_KSforD02KSKSLL

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (log((CHILD(BPVIPCHI2(),1)\*CHILD(BPVIPCHI2(),2))/(BPVIPCHI2()\*BPVIPCHI2() + DOCAMAX\*DOCAMAX)) \> 0.0)&(BPVLTSIGNCHI2() \> 50.0)&(CHILD(TRGHOSTPROB, 1) \<=1.0 )&(CHILD(TRGHOSTPROB, 2) \<=1.0 ) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ]                                                                                                                            |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/selKS2LL_KSforD02KSKSLL/Particles                                                                                                                                                             |

CombineParticles/D02KSKSLLLine

|                  |                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/selKS2LL_KSforD02KSKSLL' ]                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(BPVLTSIGNCHI2() \> 200.0)' }                                                           |
| CombinationCut   | (ACUTDOCA(1.0\*mm,''))&(ADAMASS('D0') \< 150.0\*MeV)                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20.0) & (BPVIPCHI2() \< 50.0) & (BPVLTSIGNCHI2() \> -1.0) & (ADMASS('D0') \< 100.0\*MeV) |
| DecayDescriptor  | None                                                                                                            |
| DecayDescriptors | [ 'D0 -\> KS0 KS0' ]                                                                                          |
| Output           | Phys/D02KSKSLLLine/Particles                                                                                    |
