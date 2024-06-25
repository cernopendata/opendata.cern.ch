[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB0d2DstarTauNuInvVertForB2XTauNu

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/B0d2DstarTauNuInvVertForB2XTauNu/Particles |
| Postscale      | 1.0000000                                       |
| HLT            | None                                            |
| Prescale       | 1.0000000                                       |
| L0DU           | None                                            |
| ODIN           | None                                            |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDstarWithD02KPi_Particles

|      |                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDstarWithD02KPi](./stripping21r1-commonparticles-stdloosedstarwithd02kpi)/Particles')\>0 |

FilterDesktop/SelDstarForB0dInvVertB2XTauNu

|                 |                                                                                                                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (M-MAXTREE('D0'==ABSID,M)\>135.0\*MeV) & (M-MAXTREE('D0'==ABSID,M)\<150.0\*MeV) & (VFASPF(VCHI2/VDOF)\<10.0) & CHILDCUT( (ADMASS('D0') \< 40.0 \*MeV ),2) & INTREE( ('K-'==ABSID)& (TRCHI2DOF \< 30.0) & (TRGHP \< 0.4)) &INTREE( ('pi+'==ABSID)& (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4)) |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21r1-commonparticles-stdloosedstarwithd02kpi)' ]                                                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                   |
| Output          | Phys/SelDstarForB0dInvVertB2XTauNu/Particles                                                                                                                                                                                                                                           |

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedTau3pi_Particles

|      |                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDetachedTau3pi](./stripping21r1-commonparticles-stdloosedetachedtau3pi)/Particles')\>0 |

CombineParticles/SelB0d2DstarTauNuInvVert

|                  |                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDstarForB0dInvVertB2XTauNu' , 'Phys/[StdLooseDetachedTau3pi](./stripping21r1-commonparticles-stdloosedetachedtau3pi)' ]         |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                               |
| CombinationCut   | (ACHILD(VFASPF(VZ),2) - ACHILD(VFASPF(VZ),1) \> 1.0 \*mm)&(ACHILD(VFASPF(VZ),2) - ACHILD(VFASPF(VZ),1) \<50.) & (DAMASS('B0') \< 300.0\*MeV) |
| MotherCut        | (BPVDIRA \>0.995)                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                         |
| DecayDescriptors | [ '[B0 -\> D\*(2010)- tau+]cc' ]                                                                                                         |
| Output           | Phys/SelB0d2DstarTauNuInvVert/Particles                                                                                                      |

TisTosParticleTagger/B0d2DstarTauNuInvVertForB2XTauNu

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/SelB0d2DstarTauNuInvVert' ]           |
| DecayDescriptor | None                                            |
| Output          | Phys/B0d2DstarTauNuInvVertForB2XTauNu/Particles |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 }            |
