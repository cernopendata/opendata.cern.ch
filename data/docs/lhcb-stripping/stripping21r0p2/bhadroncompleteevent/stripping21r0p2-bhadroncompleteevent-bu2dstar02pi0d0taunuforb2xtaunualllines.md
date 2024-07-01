[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBu2Dstar02Pi0D0TauNuForB2XTauNuAllLines

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/Bu2Dstar02Pi0D0TauNuForB2XTauNuAllLines/Particles |
| Postscale      | 1.0000000                                              |
| HLT1           | None                                                   |
| HLT2           | None                                                   |
| Prescale       | 1.0000000                                              |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseD02KPi

|      |                                  |
|------|----------------------------------|
| Code | 0StdLooseD02KPi/Particles',True) |

FilterDesktop/SelD0ForB2XTauNuAllLines

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1200.0\*MeV) & (ADMASS('D0') \< 40.0 \*MeV ) & (BPVDIRA \> 0.995) & (BPVVDCHI2 \> 36.0) & (VFASPF(VCHI2/VDOF)\<10.0) & (MIPCHI2DV(PRIMARY)\> 10.0)& CHILDCUT( ('K+'==ABSID) & (PT \> 1500.0\*MeV) & (TRCHI2DOF \< 30.0 ) & (TRPCHI2 \> 1e-08) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> 3),1) & CHILDCUT( ('pi+'==ABSID) & (PT\> 150.0\*MeV) & (TRPCHI2 \> 1e-08) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (PIDK \< 50.0),2) |
| Inputs          | [ 'Phys/[StdLooseD02KPi](./stripping21r0p2-commonparticles-stdloosed02kpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output          | Phys/SelD0ForB2XTauNuAllLines/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                          |

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

CombineParticles/SelDStar02Pi0D0

|                  |                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD0ForB2XTauNuAllLines' , 'Phys/[StdLooseResolvedPi0](./stripping21r0p2-commonparticles-stdlooseresolvedpi0)' ]                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi0' : '(PT\>200.0 \*MeV)' }                                                                                                 |
| CombinationCut   | ATRUE                                                                                                                                                                       |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 25.0 ) & (M-MAXTREE('D0'==ABSID,M)\>120.0\*MeV) & (M-MAXTREE('D0'==ABSID,M)\<200.0\*MeV) & (PT\>1250.0 \*MeV) & ((ADMASS('D\*(2007)0')\< 50.0\*MeV)) |
| DecayDescriptor  | None                                                                                                                                                                        |
| DecayDescriptors | [ '[D\*(2007)0 -\> D0 pi0]cc' ]                                                                                                                                         |
| Output           | Phys/SelDStar02Pi0D0/Particles                                                                                                                                              |

LoKi::VoidFilter/SELECT:Phys/StdLooseDetachedTau3pi

|      |                                          |
|------|------------------------------------------|
| Code | 0StdLooseDetachedTau3pi/Particles',True) |

CombineParticles/SelBu2Dstar02Pi0D0TauNu

|                  |                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDStar02Pi0D0' , 'Phys/[StdLooseDetachedTau3pi](./stripping21r0p2-commonparticles-stdloosedetachedtau3pi)' ]                                           |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2007)0' : 'ALL' , 'D\*(2007)~0' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                                                    |
| CombinationCut   | (((DAMASS('B+') \> -2579.0\*MeV) & (DAMASS('B+') \< 300.0\*MeV)) or ((DAMASS('B+') \> 720.0\*MeV) & (DAMASS('B+') \< 1721.0\*MeV))) & (AMAXDOCA('',0) \< 0.15\*mm) |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                               |
| DecayDescriptors | [ '[B- -\> D\*(2007)0 tau-]cc' ]                                                                                                                               |
| Output           | Phys/SelBu2Dstar02Pi0D0TauNu/Particles                                                                                                                             |

TisTosParticleTagger/Bu2Dstar02Pi0D0TauNuForB2XTauNuAllLines

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/SelBu2Dstar02Pi0D0TauNu' ]                   |
| DecayDescriptor | None                                                   |
| Output          | Phys/Bu2Dstar02Pi0D0TauNuForB2XTauNuAllLines/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }                          |
