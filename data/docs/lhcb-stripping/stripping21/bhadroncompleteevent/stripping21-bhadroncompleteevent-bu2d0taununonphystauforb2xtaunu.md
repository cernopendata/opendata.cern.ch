[[stripping21 lines]](./stripping21-index)

# StrippingBu2D0TauNuNonPhysTauForB2XTauNu

## Properties:

|                |                                                |
|----------------|------------------------------------------------|
| OutputLocation | Phys/Bu2D0TauNuNonPhysTauForB2XTauNu/Particles |
| Postscale      | 1.0000000                                      |
| HLT            | None                                           |
| Prescale       | 0.10000000                                     |
| L0DU           | None                                           |
| ODIN           | None                                           |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseD02KPi_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseD02KPi](./stripping21-commonparticles-stdloosed02kpi)/Particles')\>0 |

FilterDesktop/SelD0ForB2XTauNu

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1200.0\*MeV) & (ADMASS('D0') \< 40.0 \*MeV ) & (BPVDIRA \> 0.995) & (BPVVDCHI2 \> 36.0) & (VFASPF(VCHI2/VDOF)\<10.0) & (MIPCHI2DV(PRIMARY)\> 10.0)& CHILDCUT( ('K+'==ABSID) & (PT \> 1500.0\*MeV) & (TRCHI2DOF \< 30.0 ) & (TRPCHI2 \> 0.1) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> 3),1) & CHILDCUT( ('pi+'==ABSID) & (PT\> 150.0\*MeV) & (TRPCHI2 \> 0.1) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (PIDK \< 50.0),2) |
| Inputs          | [ 'Phys/[StdLooseD02KPi](./stripping21-commonparticles-stdloosed02kpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Output          | Phys/SelD0ForB2XTauNu/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedTau3piNonPhys_Particles

|      |                                                             |
|------|-------------------------------------------------------------|
| Code | CONTAINS('Phys/StdLooseDetachedTau3piNonPhys/Particles')\>0 |

CombineParticles/SelBu2D0TauNuNonPhysTau

|                  |                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD0ForB2XTauNu' , 'Phys/StdLooseDetachedTau3piNonPhys' ]                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'tau+' : '(BPVDIRA \> 0.98)' , 'tau-' : '(BPVDIRA \> 0.98)' }                                                        |
| CombinationCut   | (((DAMASS('B+') \> -2579.0\*MeV) & (DAMASS('B+') \< 300.0\*MeV)) or ((DAMASS('B+') \> 720.0\*MeV) & (DAMASS('B+') \< 1721.0\*MeV))) & (AMAXDOCA('',0) \< 0.15\*mm) |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                               |
| DecayDescriptors | [ '[B- -\> D0 tau-]cc' ]                                                                                                                                       |
| Output           | Phys/SelBu2D0TauNuNonPhysTau/Particles                                                                                                                             |

TisTosParticleTagger/Bu2D0TauNuNonPhysTauForB2XTauNu

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/SelBu2D0TauNuNonPhysTau' ]           |
| DecayDescriptor | None                                           |
| Output          | Phys/Bu2D0TauNuNonPhysTauForB2XTauNu/Particles |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 }           |
