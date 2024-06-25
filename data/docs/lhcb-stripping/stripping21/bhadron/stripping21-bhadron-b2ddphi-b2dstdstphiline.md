[[stripping21 lines]](./stripping21-index)

# StrippingB2DDphi_B2DstDstPhiLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2DDphi_B2DstDstPhiLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseDstarWithD02KPi_Particles

|      |                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDstarWithD02KPi](./stripping21-commonparticles-stdloosedstarwithd02kpi)/Particles')\>0 |

FilterDesktop/Dst2D0Pi_D02KPiForB2DDphi

|                 |                                                                                                                                                                                                                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (INTREE(('K+'==ABSID) & (PROBNNk \> 0.1) & (PT\>100 \*MeV) & (MIPCHI2DV(PRIMARY)\> 4) & (TRGHP \< 0.4)))& (INTREE(('pi+'==ABSID) & (PROBNNpi \> 0.1) & (PT\>100 \*MeV) & (MIPCHI2DV(PRIMARY)\> 4) & (TRGHP \< 0.4)))& (ADMASS('D\*(2010)+') \< 50 \*MeV)& (PT \> 1500.0 \*MeV)& (VFASPF(VCHI2/VDOF) \< 15) |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21-commonparticles-stdloosedstarwithd02kpi)' ]                                                                                                                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                       |
| Output          | Phys/Dst2D0Pi_D02KPiForB2DDphi/Particles                                                                                                                                                                                                                                                                   |

DaVinci::N4BodyDecays/B2DDphi_B2DstDstPhiLine

|                  |                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Dst2D0Pi_D02KPiForB2DDphi' , 'Phys/KForB2DDphi' ]                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                      |
| CombinationCut   | (AM \> 4800 \*MeV) & (AM \< 6000 \*MeV) & (ACHI2DOCA(1,4)\< 16) & (ACHI2DOCA(2,4)\< 16) & (ACHI2DOCA(3,4)\< 16) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 15) & (BPVDIRA \> 0.99) & (BPVLTIME() \> 0.2\*ps)                                        |
| DecayDescriptor  | B_s0 -\> K+ K- D\*(2010)+ D\*(2010)-                                                                            |
| DecayDescriptors | [ 'B_s0 -\> K+ K- D\*(2010)+ D\*(2010)-' ]                                                                    |
| Output           | Phys/B2DDphi_B2DstDstPhiLine/Particles                                                                          |
