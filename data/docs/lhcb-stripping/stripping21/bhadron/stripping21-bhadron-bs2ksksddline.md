[[stripping21 lines]](./stripping21-index)

# StrippingBs2KSKSDDLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Bs2KSKSDDLine/Particles |
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

FilterDesktop/selKS2DD_KSforBs2KSKSDD

|                 |                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------|
| Code            | (DOCAMAX \< 4.0\*mm)&(ADMASS('KS0')\<100.0\*MeV)&(CHILD(TRGHOSTPROB, 1) \<=1.0 )&(CHILD(TRGHOSTPROB, 2) \<=1.0 ) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' ]                                          |
| DecayDescriptor | None                                                                                                             |
| Output          | Phys/selKS2DD_KSforBs2KSKSDD/Particles                                                                           |

CombineParticles/Bs2KSKSDDLine

|                  |                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/selKS2DD_KSforBs2KSKSDD' ]                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }                                                                                               |
| CombinationCut   | (ACUTDOCA(4.0\*mm,''))&(ADAMASS('B_s0') \< 600.0\*MeV)                                                                       |
| MotherCut        | ((prob_BCu_1+prob_BCu_2+prob_BCu_3+prob_BCu_4+prob_BCu_5+prob_BCu_6+prob_BCu_7+prob_BCu_8+prob_BCu_9+prob_BCu_10)/10 \> 0.5) |
| DecayDescriptor  | None                                                                                                                         |
| DecayDescriptors | [ 'B_s0 -\> KS0 KS0' ]                                                                                                     |
| Output           | Phys/Bs2KSKSDDLine/Particles                                                                                                 |
