[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBu2KSPiDDLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Bu2KSPiDDLine/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingBu2KSPiDDLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/KSforBu2KShDD

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | (P\>8000.0\*MeV)&(PT\>1000.0\*MeV)&(ADMASS('KS0')\<30.0\*MeV)&(VFASPF(VCHI2)\<10.0)&(BPVVDCHI2\>50.0) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)' ]                             |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/KSforBu2KShDD/Particles                                                                          |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)/Particles')\>0 |

FilterDesktop/HforBu2KSh

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB\<0.5)&(TRCHI2DOF\<3.0)&(PT\>1000.0\*MeV)                         |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/HforBu2KSh/Particles                                                     |

CombineParticles/Bu2KSPiDDLine

|                  |                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/HforBu2KSh' , 'Phys/KSforBu2KShDD' ]                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'TRCHI2DOF\<3.0' , 'pi-' : 'TRCHI2DOF\<3.0' }                                                 |
| CombinationCut   | ((APT1+APT2)\>4000.0\*MeV)&(AM\>(5279-500.0)\*MeV)&(AM\<(5279+1500.0)\*MeV)&(AVAL_MAX(MIPDV(PRIMARY),PT)\>0.05)                      |
| MotherCut        | (P\>25000.0\*MeV)&(VFASPF(VCHI2)\<6.0)&(BPVDIRA\>0.9995)&(MIPCHI2DV(PRIMARY)\<10.0)&(VFASPF(VMINVDDV(PRIMARY))\>1.0)&(BPVVDCHI2\>50) |
| DecayDescriptor  | None                                                                                                                                 |
| DecayDescriptors | [ 'B+ -\> pi+ KS0' , 'B- -\> pi- KS0' ]                                                                                            |
| Output           | Phys/Bu2KSPiDDLine/Particles                                                                                                         |
