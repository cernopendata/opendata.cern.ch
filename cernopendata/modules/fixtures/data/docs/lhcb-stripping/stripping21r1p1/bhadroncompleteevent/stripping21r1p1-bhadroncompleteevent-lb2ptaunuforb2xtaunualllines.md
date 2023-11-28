[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingLb2pTauNuForB2XTauNuAllLines

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/Lb2pTauNuForB2XTauNuAllLines/Particles |
| Postscale      | 1.0000000                                   |
| HLT1           | None                                        |
| HLT2           | None                                        |
| Prescale       | 0.16660000                                  |
| L0DU           | None                                        |
| ODIN           | None                                        |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

FilterDesktop/SelpForB2XTauNuAllLines

|                 |                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ('p+'==ABSID) & (PT\> 1200.0\*MeV) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 25.0) & (PIDp \> 10.0)& (PIDp \> PIDK+10.0) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ]                                                            |
| DecayDescriptor | None                                                                                                                                         |
| Output          | Phys/SelpForB2XTauNuAllLines/Particles                                                                                                       |

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedTau3pi_Particles

|      |                                                                                                                       |
|------|-----------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDetachedTau3pi](./stripping21r1p1-commonparticles-stdloosedetachedtau3pi)/Particles',True)\>0 |

CombineParticles/SelLb2pTauNu

|                  |                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelpForB2XTauNuAllLines' , 'Phys/[StdLooseDetachedTau3pi](./stripping21r1p1-commonparticles-stdloosedetachedtau3pi)' ]                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' , 'tau+' : '(BPVDIRA \> 0.995)' , 'tau-' : '(BPVDIRA \> 0.995)' }                                                                                          |
| CombinationCut   | ATRUE                                                                                                                                                                                                  |
| MotherCut        | (CHILD(BPVVDZ,2) -BPVVDZ \> 3\* 1.0 \*mm) & (CHILD(BPVVDZ,2) -BPVVDZ \<50.) & (CHILD(MIPCHI2DV(PRIMARY),2)\>15) & (CHILD(BPVVDR,2)\<5) & (CHILD(BPVVDR,2)\>.2)& (CHILD(BPVVDCHI2,2)\>100) & (MM\<5000) |
| DecayDescriptor  | None                                                                                                                                                                                                   |
| DecayDescriptors | [ '[Lambda_b0 -\> p+ tau-]cc' ]                                                                                                                                                                    |
| Output           | Phys/SelLb2pTauNu/Particles                                                                                                                                                                            |

TisTosParticleTagger/Lb2pTauNuForB2XTauNuAllLines

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/SelLb2pTauNu' ]                   |
| DecayDescriptor | None                                        |
| Output          | Phys/Lb2pTauNuForB2XTauNuAllLines/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }               |
