[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBu2D0TauNuNonPhysTauForB2XTauNuAllLines

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/Bu2D0TauNuNonPhysTauForB2XTauNuAllLines/Particles |
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

LoKi::VoidFilter/SELECT:Phys/StdLooseDetachedTau3piNonPhys

|      |                                                 |
|------|-------------------------------------------------|
| Code | 0StdLooseDetachedTau3piNonPhys/Particles',True) |

CombineParticles/SelBu2D0TauNuNonPhysTau

|                  |                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD0ForB2XTauNuAllLines' , 'Phys/[StdLooseDetachedTau3piNonPhys](./stripping21r0p2-commonparticles-stdloosedetachedtau3pinonphys)' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'tau+' : '(BPVDIRA \> 0.98)' , 'tau-' : '(BPVDIRA \> 0.98)' }                                                        |
| CombinationCut   | (((DAMASS('B+') \> -2579.0\*MeV) & (DAMASS('B+') \< 300.0\*MeV)) or ((DAMASS('B+') \> 720.0\*MeV) & (DAMASS('B+') \< 1721.0\*MeV))) & (AMAXDOCA('',0) \< 0.15\*mm) |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                               |
| DecayDescriptors | [ '[B- -\> D0 tau-]cc' ]                                                                                                                                       |
| Output           | Phys/SelBu2D0TauNuNonPhysTau/Particles                                                                                                                             |

TisTosParticleTagger/Bu2D0TauNuNonPhysTauForB2XTauNuAllLines

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/SelBu2D0TauNuNonPhysTau' ]                   |
| DecayDescriptor | None                                                   |
| Output          | Phys/Bu2D0TauNuNonPhysTauForB2XTauNuAllLines/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }                          |
