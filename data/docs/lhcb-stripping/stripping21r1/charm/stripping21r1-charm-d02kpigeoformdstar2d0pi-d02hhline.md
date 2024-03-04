[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD02KPiGeoFormDstar2D0Pi_D02HHLine

## Properties:

|                |                                                  |
|----------------|--------------------------------------------------|
| OutputLocation | Phys/D02KPiGeoFormDstar2D0Pi_D02HHLine/Particles |
| Postscale      | 1.0000000                                        |
| HLT            | HLT_PASS_RE('Hlt1MB.\*')                         |
| Prescale       | 0.10000000                                       |
| L0DU           | None                                             |
| ODIN           | None                                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02KPiGeoFormD02HH

|                  |                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(ISLONG)' , 'K-' : '(ISLONG)' , 'pi+' : '(ISLONG)' , 'pi-' : '(ISLONG)' }                                                                    |
| CombinationCut   | (ADAMASS('D0') \< 250.0)& (AMAXDOCA('') \< 10.0)                                                                                                                    |
| MotherCut        | (ADMASS('D0') \< 125.0)& (NU_2 \> 0) & (NU_2PT \> 14.0)& (BPVVDSIGN \> 1.0)                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                |
| DecayDescriptors | [ 'D0 -\> pi+ pi-' , 'D0 -\> K- pi+' , 'D0 -\> K+ pi-' , 'D0 -\> K+ K-' ]                                                                                         |
| Output           | Phys/D02KPiGeoFormD02HH/Particles                                                                                                                                   |

CombineParticles/D02KPiGeoFormDstar2D0Pi_D02HHLine

|                  |                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02KPiGeoFormD02HH' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(ALL)' , 'pi-' : '(ALL)' }                               |
| CombinationCut   | ((AM - AM1) \< 160.0)                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 100.0)& ((M - M1) \< 155.0)                                                              |
| DecayDescriptor  | None                                                                                                            |
| DecayDescriptors | [ 'D\*(2010)+ -\> D0 pi+' , 'D\*(2010)- -\> D0 pi-' ]                                                         |
| Output           | Phys/D02KPiGeoFormDstar2D0Pi_D02HHLine/Particles                                                                |
