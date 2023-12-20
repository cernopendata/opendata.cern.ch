[[stripping21 lines]](./stripping21-index)

# StrippingBc2JpsiTauNuForB2XTauNu

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/Bc2JpsiTauNuForB2XTauNu/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseJpsi2MuMu_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseJpsi2MuMu](./stripping21-commonparticles-stdloosejpsi2mumu)/Particles')\>0 |

FilterDesktop/SelJpsiForB2XTauNu

|                 |                                                                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('J/psi(1S)') \< 80.0 \*MeV) & (VFASPF(VCHI2PDOF)\< 9.0) & (PT \> 2000.0 \*MeV) & (MINTREE('mu+'==ABSID,PT) \> 1000.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 3.0) |
| Inputs          | [ 'Phys/[StdLooseJpsi2MuMu](./stripping21-commonparticles-stdloosejpsi2mumu)' ]                                                                                              |
| DecayDescriptor | None                                                                                                                                                                           |
| Output          | Phys/SelJpsiForB2XTauNu/Particles                                                                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedTau3pi_Particles

|      |                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDetachedTau3pi](./stripping21-commonparticles-stdloosedetachedtau3pi)/Particles')\>0 |

CombineParticles/SelBc2JpsiTauNu

|                  |                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelJpsiForB2XTauNu' , 'Phys/[StdLooseDetachedTau3pi](./stripping21-commonparticles-stdloosedetachedtau3pi)' ]                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                                                                                     |
| CombinationCut   | (((DAMASS('B_c+') \> -2579.0\*MeV) & (DAMASS('B_c+') \< 300.0\*MeV)) or ((DAMASS('B_c+') \> 720.0\*MeV) & (DAMASS('B_c+') \< 1721.0\*MeV))) & (AMAXDOCA('',0) \< 0.15\*mm) |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                       |
| DecayDescriptors | [ 'B_c+ -\> J/psi(1S) tau+' , 'B_c- -\> J/psi(1S) tau-' ]                                                                                                                |
| Output           | Phys/SelBc2JpsiTauNu/Particles                                                                                                                                             |

TisTosParticleTagger/Bc2JpsiTauNuForB2XTauNu

|                 |                                        |
|-----------------|----------------------------------------|
| Inputs          | [ 'Phys/SelBc2JpsiTauNu' ]           |
| DecayDescriptor | None                                   |
| Output          | Phys/Bc2JpsiTauNuForB2XTauNu/Particles |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 }   |
