[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBs2KSKSLDLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Bs2KSKSLDLine/Particles |
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

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/selKS2LL_KSforBs2KSKSLL

|                 |                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------|
| Code            | (DOCAMAX \< 1.0\*mm)&(ADMASS('KS0')\<50.0\*MeV)&(CHILD(TRGHOSTPROB, 1) \<=1.0 )&(CHILD(TRGHOSTPROB, 2) \<=1.0 ) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)' ]                                       |
| DecayDescriptor | None                                                                                                            |
| Output          | Phys/selKS2LL_KSforBs2KSKSLL/Particles                                                                          |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/selKS2DD_KSforBs2KSKSDD

|                 |                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------|
| Code            | (DOCAMAX \< 4.0\*mm)&(ADMASS('KS0')\<100.0\*MeV)&(CHILD(TRGHOSTPROB, 1) \<=1.0 )&(CHILD(TRGHOSTPROB, 2) \<=1.0 ) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)' ]                                        |
| DecayDescriptor | None                                                                                                             |
| Output          | Phys/selKS2DD_KSforBs2KSKSDD/Particles                                                                           |

CombineParticles/Bs2KSKSLDLine

|                  |                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/selKS2DD_KSforBs2KSKSDD' , 'Phys/selKS2LL_KSforBs2KSKSLL' ]                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                       |
| CombinationCut   | (ACUTDOCA(4.0\*mm,''))&(ADAMASS('B_s0') \< 600.0\*MeV) & ((prob_BCC_1+prob_BCC_2+prob_BCC_3+prob_BCC_4+prob_BCC_5+prob_BCC_6+prob_BCC_7+prob_BCC_8+prob_BCC_9+prob_BCC_10)/10 \> 0.5)                |
| MotherCut        | INTREE((ABSID=='pi+') & (ISLONG)) & INTREE((ABSID=='pi+') & (ISDOWN)) & ((prob_BCu_1+prob_BCu_2+prob_BCu_3+prob_BCu_4+prob_BCu_5+prob_BCu_6+prob_BCu_7+prob_BCu_8+prob_BCu_9+prob_BCu_10)/10 \> 0.5) |
| DecayDescriptor  | None                                                                                                                                                                                                 |
| DecayDescriptors | [ 'B_s0 -\> KS0 KS0' ]                                                                                                                                                                             |
| Output           | Phys/Bs2KSKSLDLine/Particles                                                                                                                                                                         |
