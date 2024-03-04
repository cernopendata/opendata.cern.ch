[[stripping21 lines]](./stripping21-index)

# StrippingBc3kpiForBc3h

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Bc3kpiForBc3h/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21-commonparticles-stdalllooseannkaons)/Particles')\>0 |

FilterDesktop/SelKaonForBc3h

|                 |                                                                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.4 ) & ( PT \> 750 \* MeV ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNk \> 0.20 ) & ( MIPCHI2DV() \> 9. ) |
| Inputs          | [ 'Phys/[StdAllLooseANNKaons](./stripping21-commonparticles-stdalllooseannkaons)' ]                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                  |
| Output          | Phys/SelKaonForBc3h/Particles                                                                                                                                                                         |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21-commonparticles-stdalllooseannpions)/Particles')\>0 |

FilterDesktop/SelPionForBc3h

|                 |                                                                                                                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.4 ) & ( PT \> 750 \* MeV ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNpi \> 0.15 ) & ( MIPCHI2DV() \> 9. ) |
| Inputs          | [ 'Phys/[StdAllLooseANNPions](./stripping21-commonparticles-stdalllooseannpions)' ]                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                                   |
| Output          | Phys/SelPionForBc3h/Particles                                                                                                                                                                          |

DaVinci::N3BodyDecays/Bc3kpiForBc3h

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForBc3h' , 'Phys/SelPionForBc3h' ]                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }            |
| CombinationCut   | ( mbp_acut \| mbc_acut ) & ( ACHI2DOCA(1,3) \< 20 ) & ( ACHI2DOCA(2,3) \< 20 )          |
| MotherCut        | ( chi2vx \< 16 ) & ( ( mbp_cut & ( ctau \> 0.14 ) ) \| ( mbc_cut & ( ctau \> 0.08 ) ) ) |
| DecayDescriptor  | None                                                                                    |
| DecayDescriptors | [ '[B_c+ -\> K+ K- pi+ ]cc' , '[B_c+ -\> K+ pi- pi+ ]cc' ]                        |
| Output           | Phys/Bc3kpiForBc3h/Particles                                                            |
