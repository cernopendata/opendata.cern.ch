[[stripping21 lines]](./stripping21-index)

# StrippingB2DDphi_B2D0D0PhiLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2DDphi_B2D0D0PhiLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseD02KPi_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseD02KPi](./stripping21-commonparticles-stdloosed02kpi)/Particles')\>0 |

FilterDesktop/D02KPiForB2DDphi

|                 |                                                                                                                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (INTREE(('K+'==ABSID) & (PROBNNk \> 0.1) & (PT\>100 \*MeV) & (MIPCHI2DV(PRIMARY)\> 4) & (TRGHP \< 0.4)))& (INTREE(('pi+'==ABSID) & (PROBNNpi \> 0.1) & (PT\>100 \*MeV) & (MIPCHI2DV(PRIMARY)\> 4) & (TRGHP \< 0.4)))& (ADMASS('D0') \< 65 \*MeV)& (PT \> 1500.0 \*MeV)& (VFASPF(VCHI2/VDOF) \< 10) |
| Inputs          | [ 'Phys/[StdLooseD02KPi](./stripping21-commonparticles-stdloosed02kpi)' ]                                                                                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                               |
| Output          | Phys/D02KPiForB2DDphi/Particles                                                                                                                                                                                                                                                                    |

DaVinci::N4BodyDecays/B2DDphi_B2D0D0PhiLine

|                  |                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02KPiForB2DDphi' , 'Phys/KForB2DDphi' ]                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                     |
| CombinationCut   | (AM \> 4500 \*MeV) & (AM \< 6000 \*MeV) & (ACHI2DOCA(1,4)\< 16) & (ACHI2DOCA(2,4)\< 16) & (ACHI2DOCA(3,4)\< 16) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 15) & (BPVDIRA \> 0.99) & (BPVLTIME() \> 0.2\*ps)                                        |
| DecayDescriptor  | B_s0 -\> K+ K- D0 D~0                                                                                           |
| DecayDescriptors | [ 'B_s0 -\> K+ K- D0 D~0' ]                                                                                   |
| Output           | Phys/B2DDphi_B2D0D0PhiLine/Particles                                                                            |
