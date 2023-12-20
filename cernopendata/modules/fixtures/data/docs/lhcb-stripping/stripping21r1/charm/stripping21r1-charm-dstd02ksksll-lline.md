[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDstD02KSKSLL_LLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/DstD02KSKSLL_LLine/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/selKS2LL_KSforD02KSKSLL

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (log((CHILD(BPVIPCHI2(),1)\*CHILD(BPVIPCHI2(),2))/(BPVIPCHI2()\*BPVIPCHI2() + DOCAMAX\*DOCAMAX)) \> 0.0)&(BPVLTSIGNCHI2() \> 50.0)&(CHILD(TRGHOSTPROB, 1) \<=1.0 )&(CHILD(TRGHOSTPROB, 2) \<=1.0 ) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)' ]                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/selKS2LL_KSforD02KSKSLL/Particles                                                                                                                                                             |

CombineParticles/D02KSKSLL

|                  |                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/selKS2LL_KSforD02KSKSLL' ]                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(BPVLTSIGNCHI2() \> 200.0)' }                                                           |
| CombinationCut   | (ACUTDOCA(1.0\*mm,''))&(ADAMASS('D0') \< 150.0\*MeV)                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20.0) & (BPVIPCHI2() \< 50.0) & (BPVLTSIGNCHI2() \> -1.0) & (ADMASS('D0') \< 100.0\*MeV) |
| DecayDescriptor  | None                                                                                                            |
| DecayDescriptors | [ 'D0 -\> KS0 KS0' ]                                                                                          |
| Output           | Phys/D02KSKSLL/Particles                                                                                        |

CombineParticles/DstD02KSKSLL_LLine

|                  |                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02KSKSLL' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(TRGHOSTPROB \<=1.0 )' , 'pi-' : '(TRGHOSTPROB \<=1.0 )' }                                                       |
| CombinationCut   | (ADAMASS('D\*(2010)+') \< 200.0\*MeV)                                                                                                                                   |
| MotherCut        | (switch(CHILD(ABSID, 2) == 211, MM - CHILD(MM,1), MM - CHILD(MM,2)) \> 135.0\*MeV) & (switch(CHILD(ABSID, 2) == 211, MM - CHILD(MM,1), MM - CHILD(MM,2)) \< 160.0\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                    |
| DecayDescriptors | [ 'D\*(2010)+ -\> D0 pi+' , 'D\*(2010)- -\> D0 pi-' ]                                                                                                                 |
| Output           | Phys/DstD02KSKSLL_LLine/Particles                                                                                                                                       |
