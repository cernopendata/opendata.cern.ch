[[stripping21 lines]](./stripping21-index)

# StrippingD02HHForXSecDstar2D0Pi_D02HHLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/D02HHForXSecDstar2D0Pi_D02HHLine/Particles |
| Postscale      | 1.0000000                                       |
| HLT            | HLT_PASS_RE('Hlt1MB.\*')                        |
| Prescale       | 1.0000000                                       |
| L0DU           | None                                            |
| ODIN           | None                                            |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D02HHForXSecD02HH

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 250.0)& (BPVIPCHI2() \> 4.0)&(HASRICH)& (in_range(pidFiducialPMin, P, pidFiducialPMax))& (in_range(2.0, ETA, 5.0))& (PIDK-PIDpi \> 0.0)' , 'K-' : '(PT \> 250.0)& (BPVIPCHI2() \> 4.0)&(HASRICH)& (in_range(pidFiducialPMin, P, pidFiducialPMax))& (in_range(2.0, ETA, 5.0))& (PIDK-PIDpi \> 0.0)' , 'pi+' : '(PT \> 250.0)& (BPVIPCHI2() \> 4.0)&(HASRICH)& (in_range(pidFiducialPMin, P, pidFiducialPMax))& (in_range(2.0, ETA, 5.0))& (PIDK-PIDpi \< 3.0)' , 'pi-' : '(PT \> 250.0)& (BPVIPCHI2() \> 4.0)&(HASRICH)& (in_range(pidFiducialPMin, P, pidFiducialPMax))& (in_range(2.0, ETA, 5.0))& (PIDK-PIDpi \< 3.0)' } |
| CombinationCut   | (ADAMASS('D0') \< 80.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 25.0)& (((BPVVDCHI2 \> 16.0)\|(BPVLTIME() \> 0.150 \* picosecond)))& (BPVDIRA \> bpvdirathresh)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'D0 -\> pi+ pi-' , 'D0 -\> K- pi+' , 'D0 -\> K+ pi-' , 'D0 -\> K+ K-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/D02HHForXSecD02HH/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

CombineParticles/D02HHForXSecDstar2D0Pi_D02HHLine

|                  |                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02HHForXSecD02HH' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(ALL)' , 'pi-' : '(ALL)' }                            |
| CombinationCut   | ((AM - AM1) \< 160.0)                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 100.0)                                                                                |
| DecayDescriptor  | None                                                                                                         |
| DecayDescriptors | [ 'D\*(2010)+ -\> D0 pi+' , 'D\*(2010)- -\> D0 pi-' ]                                                      |
| Output           | Phys/D02HHForXSecDstar2D0Pi_D02HHLine/Particles                                                              |
