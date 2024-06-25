[[stripping21 lines]](./stripping21-index)

# StrippingB2DDphi_B2DsDsPhiLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2DDphi_B2DsDsPhiLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21-commonparticles-stdalllooseannkaons)/Particles')\>0 |

FilterDesktop/KForB2DDphi

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | ( PROBNNk \> 0.1)& ( PT \> 100 \*MeV)& ( P \> 1000 \*MeV)& ( TRGHP \< 0.4)& ( MIPCHI2DV(PRIMARY) \> 4) |
| Inputs          | [ 'Phys/[StdAllLooseANNKaons](./stripping21-commonparticles-stdalllooseannkaons)' ]                  |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/KForB2DDphi/Particles                                                                             |

LoKi::VoidFilter/SelFilterPhys_StdLooseDsplus2KKPi_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDsplus2KKPi](./stripping21-commonparticles-stdloosedsplus2kkpi)/Particles')\>0 |

FilterDesktop/Ds2KKPiForB2DDphi

|                 |                                                                                                                                                                                                                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (INTREE(('K+'==ABSID) & (PROBNNk \> 0.1) & (PT\>100 \*MeV) & (MIPCHI2DV(PRIMARY)\> 4) & (TRGHP \< 0.4)))& (INTREE(('pi+'==ABSID) & (PROBNNpi \> 0.1) & (PT\>100 \*MeV) & (MIPCHI2DV(PRIMARY)\> 4) & (TRGHP \< 0.4)))& (ADMASS('D_s+') \< 65 \*MeV)& (PT \> 1500.0 \*MeV)& (VFASPF(VCHI2/VDOF) \< 10) |
| Inputs          | [ 'Phys/[StdLooseDsplus2KKPi](./stripping21-commonparticles-stdloosedsplus2kkpi)' ]                                                                                                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                 |
| Output          | Phys/Ds2KKPiForB2DDphi/Particles                                                                                                                                                                                                                                                                     |

DaVinci::N4BodyDecays/B2DDphi_B2DsDsPhiLine

|                  |                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Ds2KKPiForB2DDphi' , 'Phys/KForB2DDphi' ]                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                  |
| CombinationCut   | (AM \> 4800 \*MeV) & (AM \< 6000 \*MeV) & (ACHI2DOCA(1,4)\< 16) & (ACHI2DOCA(2,4)\< 16) & (ACHI2DOCA(3,4)\< 16) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 15) & (BPVDIRA \> 0.99) & (BPVLTIME() \> 0.2\*ps)                                        |
| DecayDescriptor  | B_s0 -\> K+ K- D_s+ D_s-                                                                                        |
| DecayDescriptors | [ 'B_s0 -\> K+ K- D_s+ D_s-' ]                                                                                |
| Output           | Phys/B2DDphi_B2DsDsPhiLine/Particles                                                                            |
