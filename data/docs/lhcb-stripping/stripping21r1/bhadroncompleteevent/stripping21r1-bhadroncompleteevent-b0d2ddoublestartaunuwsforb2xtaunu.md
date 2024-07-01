[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB0d2DdoubleStarTauNuWSForB2XTauNu

## Properties:

|                |                                                  |
|----------------|--------------------------------------------------|
| OutputLocation | Phys/B0d2DdoubleStarTauNuWSForB2XTauNu/Particles |
| Postscale      | 1.0000000                                        |
| HLT            | None                                             |
| Prescale       | 1.0000000                                        |
| L0DU           | None                                             |
| ODIN           | None                                             |

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

FilterDesktop/SelDstarsForB2XTauNu

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF) \< 25.0 ) & (M-MAXTREE('D0'==ABSID,M)\>135.0\*MeV) & (M-MAXTREE('D0'==ABSID,M)\<150.0\*MeV) & (PT\>1250.0 \*MeV) & ((ADMASS('D\*(2010)+')\< 50.0\*MeV))& CHILDCUT(CHILDCUT( (PT \> 150.0\*MeV) & (TRCHI2DOF \< 30.0 ) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> -3),1),2) & CHILDCUT(CHILDCUT( (PT\> 150.0\*MeV) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0) & (PIDK \< 50.0),2),2)& CHILDCUT( (PT\>1200.0\*MeV) & (ADMASS('D0') \< 40.0 \*MeV ) & (BPVDIRA \> 0.995) & (BPVVDCHI2 \> 36.0) & (VFASPF(VCHI2/VDOF)\<10.0),2) & CHILDCUT( (PT\>50.0\*MeV) & (TRCHI2DOF \< 30.0) & (TRGHP \< 0.6),1) |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21r1-commonparticles-stdloosedstarwithd02kpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output          | Phys/SelDstarsForB2XTauNu/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

CombineParticles/SelDdoubleStar2DstarPi

|                  |                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDstarsForB2XTauNu' , 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY)\> 4.0 ) & (TRCHI2DOF \< 3.0) & (PIDK \< 8.0) & (TRGHP \< 0.6)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\> 4.0 ) & (TRCHI2DOF \< 3.0) & (PIDK \< 8.0) & (TRGHP \< 0.6)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 25.0 ) & (M-MAXTREE('D\*(2010)+'==ABSID,M)\>350.0\*MeV) & (M-MAXTREE('D\*(2010)+'==ABSID,M)\<450.0\*MeV) & (PT\>500.0 \*MeV) & ((ADMASS('D_1(2420)0')\< 300.0\*MeV))                                                              |
| DecayDescriptor  | None                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[D_1(2420)0 -\> D\*(2010)+ pi-]cc' , '[D\*\_2(2460)0 -\> D\*(2010)+ pi-]cc' ]                                                                                                                                                                   |
| Output           | Phys/SelDdoubleStar2DstarPi/Particles                                                                                                                                                                                                                    |

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedTau3pi_Particles

|      |                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDetachedTau3pi](./stripping21r1-commonparticles-stdloosedetachedtau3pi)/Particles')\>0 |

CombineParticles/SelB0d2DdoubleStarTauNuWS

|                  |                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDdoubleStar2DstarPi' , 'Phys/[StdLooseDetachedTau3pi](./stripping21r1-commonparticles-stdloosedetachedtau3pi)' ]                                      |
| DaughtersCuts    | { '' : 'ALL' , 'D\*\_2(2460)0' : 'ALL' , 'D\*\_2(2460)~0' : 'ALL' , 'D_1(2420)0' : 'ALL' , 'D_1(2420)~0' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }               |
| CombinationCut   | (((DAMASS('B0') \> -2579.0\*MeV) & (DAMASS('B0') \< 300.0\*MeV)) or ((DAMASS('B0') \> 720.0\*MeV) & (DAMASS('B0') \< 1721.0\*MeV))) & (AMAXDOCA('',0) \< 0.15\*mm) |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                               |
| DecayDescriptors | [ '[B~0 -\> D_1(2420)~0 tau-]cc' , '[B~0 -\> D\*\_2(2460)~0 tau-]cc' ]                                                                                       |
| Output           | Phys/SelB0d2DdoubleStarTauNuWS/Particles                                                                                                                           |

TisTosParticleTagger/B0d2DdoubleStarTauNuWSForB2XTauNu

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/SelB0d2DdoubleStarTauNuWS' ]           |
| DecayDescriptor | None                                             |
| Output          | Phys/B0d2DdoubleStarTauNuWSForB2XTauNu/Particles |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 }             |
