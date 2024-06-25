[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBc2JpsiTauNuNonPhysTauForB2XTauNuAllLines

## Properties:

|                |                                                          |
|----------------|----------------------------------------------------------|
| OutputLocation | Phys/Bc2JpsiTauNuNonPhysTauForB2XTauNuAllLines/Particles |
| Postscale      | 1.0000000                                                |
| HLT1           | None                                                     |
| HLT2           | None                                                     |
| Prescale       | 1.0000000                                                |
| L0DU           | None                                                     |
| ODIN           | None                                                     |

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

LoKi::VoidFilter/SELECT:Phys/StdLooseJpsi2MuMu

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseJpsi2MuMu/Particles',True) |

FilterDesktop/SelJpsiForB2XTauNuAllLines

|                 |                                                                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('J/psi(1S)') \< 80.0 \*MeV) & (VFASPF(VCHI2PDOF)\< 9.0) & (PT \> 2000.0 \*MeV) & (MINTREE('mu+'==ABSID,PT) \> 1000.0 \*MeV) & (MAXTREE('mu+'==ABSID,TRCHI2DOF) \< 3.0) |
| Inputs          | [ 'Phys/[StdLooseJpsi2MuMu](./stripping21r0p2-commonparticles-stdloosejpsi2mumu)' ]                                                                                          |
| DecayDescriptor | None                                                                                                                                                                           |
| Output          | Phys/SelJpsiForB2XTauNuAllLines/Particles                                                                                                                                      |

LoKi::VoidFilter/SELECT:Phys/StdLooseDetachedTau3piNonPhys

|      |                                                 |
|------|-------------------------------------------------|
| Code | 0StdLooseDetachedTau3piNonPhys/Particles',True) |

CombineParticles/SelBc2JpsiTauNuNonPhysTau

|                  |                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelJpsiForB2XTauNuAllLines' , 'Phys/[StdLooseDetachedTau3piNonPhys](./stripping21r0p2-commonparticles-stdloosedetachedtau3pinonphys)' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }                                                                                                     |
| CombinationCut   | (((DAMASS('B_c+') \> -2579.0\*MeV) & (DAMASS('B_c+') \< 300.0\*MeV)) or ((DAMASS('B_c+') \> 720.0\*MeV) & (DAMASS('B_c+') \< 1721.0\*MeV))) & (AMAXDOCA('',0) \< 0.15\*mm) |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                       |
| DecayDescriptors | [ 'B_c+ -\> J/psi(1S) tau+' , 'B_c- -\> J/psi(1S) tau-' ]                                                                                                                |
| Output           | Phys/SelBc2JpsiTauNuNonPhysTau/Particles                                                                                                                                   |

TisTosParticleTagger/Bc2JpsiTauNuNonPhysTauForB2XTauNuAllLines

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/SelBc2JpsiTauNuNonPhysTau' ]                   |
| DecayDescriptor | None                                                     |
| Output          | Phys/Bc2JpsiTauNuNonPhysTauForB2XTauNuAllLines/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }                            |
