[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBc3pppiForBc3h

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/Bc3pppiForBc3h/Particles |
| Postscale      | 1.0000000                     |
| HLT            | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNProtons_Particles

|      |                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNProtons](./stripping21r1-commonparticles-stdalllooseannprotons)/Particles')\>0 |

FilterDesktop/SelProtonForBc3h

|                 |                                                                                                                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.4 ) & ( PT \> 500 \* MeV ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 10 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNp \> 0.15 ) & ( MIPCHI2DV() \> 4. ) |
| Inputs          | [ 'Phys/[StdAllLooseANNProtons](./stripping21r1-commonparticles-stdalllooseannprotons)' ]                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                 |
| Output          | Phys/SelProtonForBc3h/Particles                                                                                                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r1-commonparticles-stdalllooseannpions)/Particles')\>0 |

FilterDesktop/SelPionForBc3h

|                 |                                                                                                                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( CLONEDIST \> 5000 ) & ( TRGHOSTPROB \< 0.4 ) & ( PT \> 750 \* MeV ) & in_range ( 2 , ETA , 4.9 ) & in_range ( 3.2 \* GeV , P , 150 \* GeV ) & HASRICH & ( PROBNNpi \> 0.15 ) & ( MIPCHI2DV() \> 9. ) |
| Inputs          | [ 'Phys/[StdAllLooseANNPions](./stripping21r1-commonparticles-stdalllooseannpions)' ]                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                   |
| Output          | Phys/SelPionForBc3h/Particles                                                                                                                                                                          |

DaVinci::N3BodyDecays/Bc3pppiForBc3h

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelPionForBc3h' , 'Phys/SelProtonForBc3h' ]                                   |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }           |
| CombinationCut   | ( mbp_acut \| mbc_acut ) & ( ACHI2DOCA(1,3) \< 20 ) & ( ACHI2DOCA(2,3) \< 20 )          |
| MotherCut        | ( chi2vx \< 16 ) & ( ( mbp_cut & ( ctau \> 0.14 ) ) \| ( mbc_cut & ( ctau \> 0.08 ) ) ) |
| DecayDescriptor  | [B_c+ -\> p+ p~- pi+ ]cc                                                              |
| DecayDescriptors | [ '[B_c+ -\> p+ p~- pi+ ]cc' ]                                                      |
| Output           | Phys/Bc3pppiForBc3h/Particles                                                           |
