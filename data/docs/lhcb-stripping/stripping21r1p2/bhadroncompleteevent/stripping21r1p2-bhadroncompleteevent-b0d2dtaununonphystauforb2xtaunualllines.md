[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB0d2DTauNuNonPhysTauForB2XTauNuAllLines

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/B0d2DTauNuNonPhysTauForB2XTauNuAllLines/Particles |
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

LoKi::VoidFilter/SELECT:Phys/StdLooseDplus2KPiPi

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseDplus2KPiPi/Particles',True) |

FilterDesktop/SelDplusForB2XTauNuAllLines

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1600.0\*MeV) & (ADMASS('D+') \< 40.0 \*MeV ) & (BPVDIRA \> 0.995) & (BPVVDCHI2 \> 50.0) & (VFASPF(VCHI2/VDOF)\<10.0) & (MIPCHI2DV(PRIMARY)\> 10.0)& CHILDCUT( ('K+'==ABSID) & (PT \> 1500.0\*MeV) & (TRCHI2DOF \< 30.0 ) & (TRPCHI2 \> 1e-08) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> 3),1) & CHILDCUT( ('pi+'==ABSID) & (PT\> 150.0\*MeV) & (TRPCHI2 \> 1e-08) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (PIDK \< 50.0),2)& CHILDCUT( ('pi+'==ABSID) & (PT\> 150.0\*MeV) & (TRPCHI2 \> 1e-08) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0) & (PIDK \< 50.0),3) |
| Inputs          | [ 'Phys/[StdLooseDplus2KPiPi](./stripping21r1p2-commonparticles-stdloosedplus2kpipi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Output          | Phys/SelDplusForB2XTauNuAllLines/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

LoKi::VoidFilter/SELECT:Phys/StdLooseDetachedTau3piNonPhys

|      |                                                 |
|------|-------------------------------------------------|
| Code | 0StdLooseDetachedTau3piNonPhys/Particles',True) |

CombineParticles/SelB0d2DTauNuNonPhysTau

|                  |                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelDplusForB2XTauNuAllLines' , 'Phys/[StdLooseDetachedTau3piNonPhys](./stripping21r1p2-commonparticles-stdloosedetachedtau3pinonphys)' ]                 |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'tau+' : '(BPVDIRA \> 0.98)' , 'tau-' : '(BPVDIRA \> 0.98)' }                                                         |
| CombinationCut   | (((DAMASS('B0') \> -2579.0\*MeV) & (DAMASS('B0') \< 300.0\*MeV)) or ((DAMASS('B0') \> 720.0\*MeV) & (DAMASS('B0') \< 1721.0\*MeV))) & (AMAXDOCA('',0) \< 0.15\*mm) |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                               |
| DecayDescriptors | [ '[B0 -\> D- tau+]cc' ]                                                                                                                                       |
| Output           | Phys/SelB0d2DTauNuNonPhysTau/Particles                                                                                                                             |

TisTosParticleTagger/B0d2DTauNuNonPhysTauForB2XTauNuAllLines

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/SelB0d2DTauNuNonPhysTau' ]                   |
| DecayDescriptor | None                                                   |
| Output          | Phys/B0d2DTauNuNonPhysTauForB2XTauNuAllLines/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }                          |
