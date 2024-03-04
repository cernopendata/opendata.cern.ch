[[stripping21 lines]](./stripping21-index)

# StrippingLTUnbCharmDs2KKPiLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/LTUnbCharmDs2KKPiLine/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/LTUnbCharmPions3BFilterSel

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3) & (PT \> 500.0 \* MeV) & (PIDK \< 0) & (PIDp \< 0) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]          |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/LTUnbCharmPions3BFilterSel/Particles                                                  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/LTUnbCharmKaons3BFilterSel

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3) & (PT \> 500.0 \* MeV) & (PIDK \> 5)      |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/LTUnbCharmKaons3BFilterSel/Particles                                         |

CombineParticles/LTUnbCharmDs2KKPi

|                  |                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LTUnbCharmKaons3BFilterSel' , 'Phys/LTUnbCharmPions3BFilterSel' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                        |
| CombinationCut   | (APT \> 2500 \* MeV ) & (AM \> 1700.\*MeV) & ( AMAXDOCA('') \< 0.1 )                                                                |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10) & ( PT \> 2500 \* MeV ) & ( ADMASS('D0') \< 65 \* MeV ) & ( BPVDIRA \> 0.98 ) & ( BPVLTIME() \> 0.00025 ) |
| DecayDescriptor  | [D_s+ -\> K- K+ pi+]cc                                                                                                            |
| DecayDescriptors | [ '[D_s+ -\> K- K+ pi+]cc' ]                                                                                                    |
| Output           | Phys/LTUnbCharmDs2KKPi/Particles                                                                                                    |

TisTosParticleTagger/LTUnbCharmDs2KKPiLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/LTUnbCharmDs2KKPi' ]                            |
| DecayDescriptor | None                                                      |
| Output          | Phys/LTUnbCharmDs2KKPiLine/Particles                      |
| TisTosSpecs     | { 'Hlt1.\*Decision%TIS' : 0 , 'Hlt2.\*Decision%TIS' : 0 } |
