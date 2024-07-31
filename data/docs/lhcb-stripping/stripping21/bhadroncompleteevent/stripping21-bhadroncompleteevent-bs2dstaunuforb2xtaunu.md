[[stripping21 lines]](./stripping21-index)

# StrippingBs2DsTauNuForB2XTauNu

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/Bs2DsTauNuForB2XTauNu/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseDsplus2KKPi_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDsplus2KKPi](./stripping21-commonparticles-stdloosedsplus2kkpi)/Particles')\>0 |

FilterDesktop/SelDsForB2XTauNu

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1600.0\*MeV) & (ADMASS('D_s+') \< 40.0 \*MeV ) & (BPVDIRA \> 0.995) & (BPVVDCHI2 \> 36.0) & (VFASPF(VCHI2/VDOF)\<10.0) & (MIPCHI2DV(PRIMARY)\> 10.0)& CHILDCUT( ('K+'==ABSID) & (PT \> 1500.0\*MeV) & (TRCHI2DOF \< 30.0 ) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> 3),1) & CHILDCUT( ('K+'==ABSID) & (PT \> 1500.0\*MeV) & (TRCHI2DOF \< 30.0 ) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> 3),2) & CHILDCUT( ('pi+'==ABSID) & (PT\> 150.0\*MeV) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (PIDK \< 50.0),3) |
| Inputs          | [ 'Phys/[StdLooseDsplus2KKPi](./stripping21-commonparticles-stdloosedsplus2kkpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output          | Phys/SelDsForB2XTauNu/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedTau3pi_Particles

|      |                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDetachedTau3pi](./stripping21-commonparticles-stdloosedetachedtau3pi)/Particles')\>0 |

CombineParticles/SelBs2DsTauNu

|                  |                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDsForB2XTauNu' , 'Phys/[StdLooseDetachedTau3pi](./stripping21-commonparticles-stdloosedetachedtau3pi)' ]                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'tau+' : '(BPVDIRA \> 0.98)' , 'tau-' : '(BPVDIRA \> 0.98)' }                                                             |
| CombinationCut   | (((DAMASS('B_s0') \> -2579.0\*MeV) & (DAMASS('B_s0') \< 300.0\*MeV)) or ((DAMASS('B_s0') \> 720.0\*MeV) & (DAMASS('B_s0') \< 1721.0\*MeV))) & (AMAXDOCA('',0) \< 0.15\*mm) |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                       |
| DecayDescriptors | [ '[B_s0 -\> D_s- tau+]cc' ]                                                                                                                                           |
| Output           | Phys/SelBs2DsTauNu/Particles                                                                                                                                               |

TisTosParticleTagger/Bs2DsTauNuForB2XTauNu

|                 |                                      |
|-----------------|--------------------------------------|
| Inputs          | [ 'Phys/SelBs2DsTauNu' ]           |
| DecayDescriptor | None                                 |
| Output          | Phys/Bs2DsTauNuForB2XTauNu/Particles |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 } |
