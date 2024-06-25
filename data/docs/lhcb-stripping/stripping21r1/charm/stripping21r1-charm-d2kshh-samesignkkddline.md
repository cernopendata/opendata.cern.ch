[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2KShh_samesignKKDDLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/D2KShh_samesignKKDDLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 0.010000000                            |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingD2KShh_samesignKKDDLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/KsDDForD2KShh_samesign

|                 |                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| Code            | (BPVVDZ \> 0.0 \* mm) & (BPVVDZ \< 2300.0 \* mm) & (BPVDIRA \> 0.99995 ) & (ADMASS('KS0') \< 40.0 \*MeV) & (BPVVDCHI2\> 100 ) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)' ]                                                     |
| DecayDescriptor | None                                                                                                                          |
| Output          | Phys/KsDDForD2KShh_samesign/Particles                                                                                         |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KForD2KShh_samesign

|                 |                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| Code            | ((P \> 1500.0 \*MeV)&(PIDe-PIDK \< 10.0 )&(PIDp-PIDK \< 15.0 ) &(PIDpi-PIDK \< -3.0 ) &(TRCHI2DOF \< 5.0 )) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ]                                 |
| DecayDescriptor | None                                                                                                        |
| Output          | Phys/KForD2KShh_samesign/Particles                                                                          |

CombineParticles/D2KShh_samesignKKDDLine

|                  |                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KForD2KShh_samesign' , 'Phys/KsDDForD2KShh_samesign' ]                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                       |
| CombinationCut   | ( (APT \> 1500.0 \* MeV) & (APT \> 1500.0 \* MeV) & (ADAMASS('D0') \< 270 \* MeV) )                                |
| MotherCut        | ( ((BPVVDZ \< 7000.0\*mm) ) & (ADMASS('D0') \< 85.0 \* MeV) & ( (CHILD(VFASPF(VZ),1) - VFASPF(VZ)) \> 10.0 \* mm)) |
| DecayDescriptor  | None                                                                                                               |
| DecayDescriptors | [ '[D0 -\> KS0 K+ K+]cc' ]                                                                                     |
| Output           | Phys/D2KShh_samesignKKDDLine/Particles                                                                             |
