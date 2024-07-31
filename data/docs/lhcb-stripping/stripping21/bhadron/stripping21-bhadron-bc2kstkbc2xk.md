[[stripping21 lines]](./stripping21-index)

# StrippingBc2KstKBc2XK

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/Bc2KstKBc2XK/Particles |
| Postscale      | 1.0000000                   |
| HLT            | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/SelKForBc2XK

|                 |                                                                                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( CLONEDIST \> 5000 ) & ( TRCHI2DOF \< 4 ) & ( TRGHOSTPROB \< 0.4 ) & ( PT \> 750 \* MeV ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & ( MIPCHI2DV() \> 9. ) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                            |
| DecayDescriptor | None                                                                                                                                                                                       |
| Output          | Phys/SelKForBc2XK/Particles                                                                                                                                                                |

LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKstar2Kpi](./stripping21-commonparticles-stdloosekstar2kpi)/Particles')\>0 |

FilterDesktop/SelKstarForBc2XK

|                 |                                                                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( PT \> 1000 \* MeV ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 5 \* GeV , P , 500 \* GeV ) & ( MIPCHI2DV() \> 9. ) & ( CHILDCUT ( ( PT\> 300\*MeV) , 1 ) ) & ( CHILDCUT ( ( PT\> 300\*MeV) , 2 ) ) |
| Inputs          | [ 'Phys/[StdLooseKstar2Kpi](./stripping21-commonparticles-stdloosekstar2kpi)' ]                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                |
| Output          | Phys/SelKstarForBc2XK/Particles                                                                                                                                                                     |

CombineParticles/Bc2KstKBc2XK

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKForBc2XK' , 'Phys/SelKstarForBc2XK' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' } |
| CombinationCut   | mbp_acut \| mbc_acut                                                                      |
| MotherCut        | ( chi2vx \< 16 ) & ( ( mbp_cut & ( ctau \> 0.14 ) ) \| ( mbc_cut & ( ctau \> 0.08 ) ) )   |
| DecayDescriptor  | [B_c+ -\> K\*(892)~0 K+]cc                                                              |
| DecayDescriptors | [ '[B_c+ -\> K\*(892)~0 K+]cc' ]                                                      |
| Output           | Phys/Bc2KstKBc2XK/Particles                                                               |
