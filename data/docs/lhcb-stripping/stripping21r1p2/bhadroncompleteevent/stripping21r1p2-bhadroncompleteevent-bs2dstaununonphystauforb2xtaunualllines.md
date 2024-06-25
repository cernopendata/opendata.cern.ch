[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBs2DsTauNuNonPhysTauForB2XTauNuAllLines

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/Bs2DsTauNuNonPhysTauForB2XTauNuAllLines/Particles |
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

LoKi::VoidFilter/SELECT:Phys/StdLooseDsplus2KKPi

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseDsplus2KKPi/Particles',True) |

FilterDesktop/SelDsForB2XTauNuAllLines

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1600.0\*MeV) & (ADMASS('D_s+') \< 40.0 \*MeV ) & (BPVDIRA \> 0.995) & (BPVVDCHI2 \> 36.0) & (VFASPF(VCHI2/VDOF)\<10.0) & (MIPCHI2DV(PRIMARY)\> 10.0)& CHILDCUT( ('K+'==ABSID) & (PT \> 1500.0\*MeV) & (TRCHI2DOF \< 30.0 ) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> 3),1) & CHILDCUT( ('K+'==ABSID) & (PT \> 1500.0\*MeV) & (TRCHI2DOF \< 30.0 ) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> 3),2) & CHILDCUT( ('pi+'==ABSID) & (PT\> 150.0\*MeV) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (PIDK \< 50.0),3) |
| Inputs          | [ 'Phys/[StdLooseDsplus2KKPi](./stripping21r1p2-commonparticles-stdloosedsplus2kkpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output          | Phys/SelDsForB2XTauNuAllLines/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

LoKi::VoidFilter/SELECT:Phys/StdLooseDetachedTau3piNonPhys

|      |                                                 |
|------|-------------------------------------------------|
| Code | 0StdLooseDetachedTau3piNonPhys/Particles',True) |

CombineParticles/SelBs2DsTauNuNonPhysTau

|                  |                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDsForB2XTauNuAllLines' , 'Phys/[StdLooseDetachedTau3piNonPhys](./stripping21r1p2-commonparticles-stdloosedetachedtau3pinonphys)' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'tau+' : '(BPVDIRA \> 0.98)' , 'tau-' : '(BPVDIRA \> 0.98)' }                                                             |
| CombinationCut   | (((DAMASS('B_s0') \> -2579.0\*MeV) & (DAMASS('B_s0') \< 300.0\*MeV)) or ((DAMASS('B_s0') \> 720.0\*MeV) & (DAMASS('B_s0') \< 1721.0\*MeV))) & (AMAXDOCA('',0) \< 0.15\*mm) |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                       |
| DecayDescriptors | [ '[B_s0 -\> D_s+ tau-]cc' ]                                                                                                                                           |
| Output           | Phys/SelBs2DsTauNuNonPhysTau/Particles                                                                                                                                     |

TisTosParticleTagger/Bs2DsTauNuNonPhysTauForB2XTauNuAllLines

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/SelBs2DsTauNuNonPhysTau' ]                   |
| DecayDescriptor | None                                                   |
| Output          | Phys/Bs2DsTauNuNonPhysTauForB2XTauNuAllLines/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }                          |
