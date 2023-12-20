[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLTUnbCharmD2KPiPiLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/LTUnbCharmD2KPiPiLine/Particles |
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

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/LTUnbCharmPions3BFilterSel

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3) & (PT \> 500.0 \* MeV) & (PIDK \< 0) & (PIDp \< 0) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]        |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/LTUnbCharmPions3BFilterSel/Particles                                                  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/LTUnbCharmKaons3BFilterSel

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3) & (PT \> 500.0 \* MeV) & (PIDK \> 5)        |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/LTUnbCharmKaons3BFilterSel/Particles                                           |

CombineParticles/LTUnbCharmD2KPiPi

|                  |                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LTUnbCharmKaons3BFilterSel' , 'Phys/LTUnbCharmPions3BFilterSel' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                        |
| CombinationCut   | (APT \> 2500 \* MeV ) & (AM \> 1700.\*MeV) & ( AMAXDOCA('') \< 0.1 )                                                                |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10) & ( PT \> 2500 \* MeV ) & ( ADMASS('D0') \< 65 \* MeV ) & ( BPVDIRA \> 0.98 ) & ( BPVLTIME() \> 0.00025 ) |
| DecayDescriptor  | [D+ -\> K- pi+ pi+]cc                                                                                                             |
| DecayDescriptors | [ '[D+ -\> K- pi+ pi+]cc' ]                                                                                                     |
| Output           | Phys/LTUnbCharmD2KPiPi/Particles                                                                                                    |

TisTosParticleTagger/LTUnbCharmD2KPiPiLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/LTUnbCharmD2KPiPi' ]                            |
| DecayDescriptor | None                                                      |
| Output          | Phys/LTUnbCharmD2KPiPiLine/Particles                      |
| TisTosSpecs     | { 'Hlt1.\*Decision%TIS' : 0 , 'Hlt2.\*Decision%TIS' : 0 } |
