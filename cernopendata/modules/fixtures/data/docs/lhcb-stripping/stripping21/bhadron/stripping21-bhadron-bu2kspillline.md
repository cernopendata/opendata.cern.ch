[[stripping21 lines]](./stripping21-index)

# StrippingBu2KSPiLLLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Bu2KSPiLLLine/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingBu2KSPiLLLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/KSforBu2KShLL

|                 |                                                                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CHILDCUT((TRGHOSTPROB\<0.5),1))&(CHILDCUT((TRGHOSTPROB\<0.5),2))&(P\>8000.0\*MeV)&(PT\>1000.0\*MeV)&(ADMASS('KS0')\<15.0\*MeV)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(VFASPF(VCHI2)\<10.0)&(BPVVDCHI2\>100.0) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ]                                                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                                   |
| Output          | Phys/KSforBu2KShLL/Particles                                                                                                                                                                                                           |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)/Particles')\>0 |

FilterDesktop/HforBu2KSh

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB\<0.5)&(TRCHI2DOF\<3.0)&(PT\>1000.0\*MeV)                       |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/HforBu2KSh/Particles                                                   |

CombineParticles/Bu2KSPiLLLine

|                  |                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/HforBu2KSh' , 'Phys/KSforBu2KShLL' ]                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'TRCHI2DOF\<3.0' , 'pi-' : 'TRCHI2DOF\<3.0' }                                                 |
| CombinationCut   | ((APT1+APT2)\>4000.0\*MeV)&(AM\>(5279-500.0)\*MeV)&(AM\<(5279+1500.0)\*MeV)&(AVAL_MAX(MIPDV(PRIMARY),PT)\>0.05)                      |
| MotherCut        | (P\>25000.0\*MeV)&(VFASPF(VCHI2)\<6.0)&(BPVDIRA\>0.9995)&(MIPCHI2DV(PRIMARY)\<10.0)&(VFASPF(VMINVDDV(PRIMARY))\>1.0)&(BPVVDCHI2\>50) |
| DecayDescriptor  | None                                                                                                                                 |
| DecayDescriptors | [ 'B+ -\> pi+ KS0' , 'B- -\> pi- KS0' ]                                                                                            |
| Output           | Phys/Bu2KSPiLLLine/Particles                                                                                                         |
