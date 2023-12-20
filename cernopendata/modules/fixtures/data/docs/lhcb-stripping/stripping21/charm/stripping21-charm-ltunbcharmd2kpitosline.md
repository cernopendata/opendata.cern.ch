[[stripping21 lines]](./stripping21-index)

# StrippingLTUnbCharmD2KPiTOSLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/LTUnbCharmD2KPiTOSLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

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

FilterDesktop/LTUnbCharmPions2BFilterSel

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3) & (PT \> 800.0 \* MeV) & (PIDK \< 0) & (PIDp \< 0) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]          |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/LTUnbCharmPions2BFilterSel/Particles                                                  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/LTUnbCharmKaons2BFilterSel

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3) & (PT \> 800.0 \* MeV) & (PIDK \> 5)      |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/LTUnbCharmKaons2BFilterSel/Particles                                         |

CombineParticles/LTUnbCharmD2hh

|                  |                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LTUnbCharmKaons2BFilterSel' , 'Phys/LTUnbCharmPions2BFilterSel' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                        |
| CombinationCut   | (APT \> 2500 \* MeV ) & (AM \> 1700.\*MeV) & ( AMAXDOCA('') \< 0.1 )                                                                |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10) & ( PT \> 2500 \* MeV ) & ( ADMASS('D0') \< 65 \* MeV ) & ( BPVDIRA \> 0.98 ) & ( BPVLTIME() \> 0.00025 ) |
| DecayDescriptor  | [D0 -\> K+ pi-]cc                                                                                                                 |
| DecayDescriptors | [ '[D0 -\> K+ pi-]cc' ]                                                                                                         |
| Output           | Phys/LTUnbCharmD2hh/Particles                                                                                                       |

TisTosParticleTagger/LTUnbCharmD2KPiTOSLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/LTUnbCharmD2hh' ]                     |
| DecayDescriptor | None                                            |
| Output          | Phys/LTUnbCharmD2KPiTOSLine/Particles           |
| TisTosSpecs     | { 'Hlt2CharmHadMinBiasD02KPiDecision%TOS' : 0 } |
