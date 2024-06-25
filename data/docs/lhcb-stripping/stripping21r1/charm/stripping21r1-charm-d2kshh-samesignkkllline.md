[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2KShh_samesignKKLLLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/D2KShh_samesignKKLLLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 0.010000000                            |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingD2KShh_samesignKKLLLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/KsLLForD2KShh_samesign

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (BPVVDZ \> -1000.0 \* mm) & (BPVVDZ \< 650.0 \* mm) & (BPVDIRA \> 0.9997 ) & (ADMASS('KS0') \< 20.0 \*MeV) & (BPVVDCHI2\> 100 ) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)' ]                                                       |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/KsLLForD2KShh_samesign/Particles                                                                                           |

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

CombineParticles/D2KShh_samesignKKLLLine

|                  |                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KForD2KShh_samesign' , 'Phys/KsLLForD2KShh_samesign' ]                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' }                                                       |
| CombinationCut   | ( (APT \> 1500.0 \* MeV) & (APT \> 1500.0 \* MeV) & (ADAMASS('D0') \< 130 \* MeV) )                                |
| MotherCut        | ( ((BPVVDZ \< 7000.0\*mm) ) & (ADMASS('D0') \< 70.0 \* MeV) & ( (CHILD(VFASPF(VZ),1) - VFASPF(VZ)) \> 10.0 \* mm)) |
| DecayDescriptor  | None                                                                                                               |
| DecayDescriptors | [ '[D0 -\> KS0 K+ K+]cc' ]                                                                                     |
| Output           | Phys/D2KShh_samesignKKLLLine/Particles                                                                             |
