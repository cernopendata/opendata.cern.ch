[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBc3kForBc3h

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/Bc3kForBc3h/Particles |
| Postscale      | 1.0000000                  |
| HLT            | None                       |
| Prescale       | 1.0000000                  |
| L0DU           | None                       |
| ODIN           | None                       |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21r1-commonparticles-stdalllooseannkaons)/Particles')\>0 |

FilterDesktop/SelKaonForBc3h

|                 |                                                                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.4 ) & ( PT \> 750 \* MeV ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNk \> 0.20 ) & ( MIPCHI2DV() \> 9. ) |
| Inputs          | [ 'Phys/[StdAllLooseANNKaons](./stripping21r1-commonparticles-stdalllooseannkaons)' ]                                                                                                               |
| DecayDescriptor | None                                                                                                                                                                                                  |
| Output          | Phys/SelKaonForBc3h/Particles                                                                                                                                                                         |

DaVinci::N3BodyDecays/Bc3kForBc3h

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelKaonForBc3h' ]                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                            |
| CombinationCut   | ( mbp_acut \| mbc_acut ) & ( ACHI2DOCA(1,3) \< 20 ) & ( ACHI2DOCA(2,3) \< 20 )          |
| MotherCut        | ( chi2vx \< 16 ) & ( ( mbp_cut & ( ctau \> 0.14 ) ) \| ( mbc_cut & ( ctau \> 0.08 ) ) ) |
| DecayDescriptor  | [B_c+ -\> K+ K- K+ ]cc                                                                |
| DecayDescriptors | [ '[B_c+ -\> K+ K- K+ ]cc' ]                                                        |
| Output           | Phys/Bc3kForBc3h/Particles                                                              |
