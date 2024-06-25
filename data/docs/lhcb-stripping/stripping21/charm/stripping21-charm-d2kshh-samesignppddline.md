[[stripping21 lines]](./stripping21-index)

# StrippingD2KShh_samesignPPDDLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/D2KShh_samesignPPDDLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 0.010000000                            |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingD2KShh_samesignPPDDLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/KsDDForD2KShh_samesign

|                 |                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| Code            | (BPVVDZ \> 0.0 \* mm) & (BPVVDZ \< 2300.0 \* mm) & (BPVDIRA \> 0.99995 ) & (ADMASS('KS0') \< 40.0 \*MeV) & (BPVVDCHI2\> 100 ) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' ]                                                       |
| DecayDescriptor | None                                                                                                                          |
| Output          | Phys/KsDDForD2KShh_samesign/Particles                                                                                         |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PForD2KShh_samesign

|                 |                                                                                                                |
|-----------------|----------------------------------------------------------------------------------------------------------------|
| Code            | ((P \> 1500.0 \*MeV)&(PIDe-PIDpi \< 10.0 )&(PIDp-PIDpi \< 15.0 ) &(PIDK -PIDpi \< -1.0 ) &(TRCHI2DOF \< 4.0 )) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                      |
| DecayDescriptor | None                                                                                                           |
| Output          | Phys/PForD2KShh_samesign/Particles                                                                             |

CombineParticles/D2KShh_samesignPPDDLine

|                  |                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KsDDForD2KShh_samesign' , 'Phys/PForD2KShh_samesign' ]                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                      |
| CombinationCut   | ( (APT \> 1500.0 \* MeV) & (APT \> 1500.0 \* MeV) & (ADAMASS('D0') \< 270 \* MeV) )                                 |
| MotherCut        | ( ((BPVVDZ \< 7000.0\*mm) ) & (ADMASS('D0') \< 150.0 \* MeV) & ( (CHILD(VFASPF(VZ),1) - VFASPF(VZ)) \> 10.0 \* mm)) |
| DecayDescriptor  | None                                                                                                                |
| DecayDescriptors | [ '[D0 -\> KS0 pi+ pi+]cc' ]                                                                                    |
| Output           | Phys/D2KShh_samesignPPDDLine/Particles                                                                              |
