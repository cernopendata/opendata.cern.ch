[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLb2pTauNuWSForB2XTauNuAllLines

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/Lb2pTauNuWSForB2XTauNuAllLines/Particles |
| Postscale      | 1.0000000                                     |
| HLT1           | None                                          |
| HLT2           | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

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

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

FilterDesktop/SelpForB2XTauNuAllLines

|                 |                                                                                                                                                                |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ('p+'==ABSID) & (PT\> 1200.0\*MeV) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 25.0) & (PROBNNp \> 0.6) & (PROBNNk \< .1) & (PROBNNpi \< .1) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r0p2-commonparticles-stdlooseprotons)' ]                                                                              |
| DecayDescriptor | None                                                                                                                                                           |
| Output          | Phys/SelpForB2XTauNuAllLines/Particles                                                                                                                         |

LoKi::VoidFilter/SELECT:Phys/StdLooseDetachedTau3pi

|      |                                          |
|------|------------------------------------------|
| Code | 0StdLooseDetachedTau3pi/Particles',True) |

CombineParticles/SelLb2pTauNuWS

|                  |                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelpForB2XTauNuAllLines' , 'Phys/[StdLooseDetachedTau3pi](./stripping21r0p2-commonparticles-stdloosedetachedtau3pi)' ]                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' , 'tau+' : '(BPVDIRA \> 0.995)' , 'tau-' : '(BPVDIRA \> 0.995)' }                                                                                          |
| CombinationCut   | ATRUE                                                                                                                                                                                                  |
| MotherCut        | (CHILD(BPVVDZ,2) -BPVVDZ \> 3\* 1.0 \*mm) & (CHILD(BPVVDZ,2) -BPVVDZ \<50.) & (CHILD(MIPCHI2DV(PRIMARY),2)\>15) & (CHILD(BPVVDR,2)\<5) & (CHILD(BPVVDR,2)\>.2)& (CHILD(BPVVDCHI2,2)\>100) & (MM\<5000) |
| DecayDescriptor  | None                                                                                                                                                                                                   |
| DecayDescriptors | [ '[Lambda_b0 -\> p+ tau+]cc' ]                                                                                                                                                                    |
| Output           | Phys/SelLb2pTauNuWS/Particles                                                                                                                                                                          |

TisTosParticleTagger/Lb2pTauNuWSForB2XTauNuAllLines

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/SelLb2pTauNuWS' ]                   |
| DecayDescriptor | None                                          |
| Output          | Phys/Lb2pTauNuWSForB2XTauNuAllLines/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }                 |
