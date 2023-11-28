[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLb2LcTauNuNonPhysTauForB2XTauNuAllLines

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/Lb2LcTauNuNonPhysTauForB2XTauNuAllLines/Particles |
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

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdac2PKPi

|      |                                        |
|------|----------------------------------------|
| Code | 0StdLooseLambdac2PKPi/Particles',True) |

FilterDesktop/SelLcForB2XTauNuAllLines

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1200.0\*MeV) & (ADMASS('Lambda_c+') \< 30.0 \*MeV )& (BPVDIRA \> 0.995) & (BPVVDCHI2 \> 50.0) & (VFASPF(VCHI2/VDOF)\<10.0) & (MIPCHI2DV(PRIMARY)\> 10.0)& INTREE( ('p+'==ABSID) & (PT\> 150.0\*MeV) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0) & (PIDp \> 5.0))& INTREE ( ('pi+'==ABSID) & (PT\> 150.0\*MeV) & (TRPCHI2 \> 1e-08) & (TRCHI2DOF \< 3.0) & (TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (PIDK \< 50.0))& INTREE( ('K-'==ABSID) & (PT \> 150.0\*MeV) & (TRCHI2DOF \< 3.0 ) & (TRPCHI2 \> 1e-08) & (MIPCHI2DV(PRIMARY)\> 10.0 ) & (TRGHP \< 0.4) & (PIDK \> 3.0)) |
| Inputs          | [ 'Phys/[StdLooseLambdac2PKPi](./stripping21r0p2-commonparticles-stdlooselambdac2pkpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output          | Phys/SelLcForB2XTauNuAllLines/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

LoKi::VoidFilter/SELECT:Phys/StdLooseDetachedTau3piNonPhys

|      |                                                 |
|------|-------------------------------------------------|
| Code | 0StdLooseDetachedTau3piNonPhys/Particles',True) |

CombineParticles/SelLb2LcTauNuNonPhysTau

|                  |                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelLcForB2XTauNuAllLines' , 'Phys/[StdLooseDetachedTau3piNonPhys](./stripping21r0p2-commonparticles-stdloosedetachedtau3pinonphys)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'tau+' : '(BPVDIRA \> 0.995)' , 'tau-' : '(BPVDIRA \> 0.995)' }                     |
| CombinationCut   | (DAMASS('Lambda_b0') \< 300.0\*MeV) & (AMAXDOCA('') \< 0.15\*mm)                                                                                |
| MotherCut        | (BPVDIRA \> 0.995)                                                                                                                              |
| DecayDescriptor  | None                                                                                                                                            |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda_c+ tau-]cc' ]                                                                                                      |
| Output           | Phys/SelLb2LcTauNuNonPhysTau/Particles                                                                                                          |

TisTosParticleTagger/Lb2LcTauNuNonPhysTauForB2XTauNuAllLines

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/SelLb2LcTauNuNonPhysTau' ]                   |
| DecayDescriptor | None                                                   |
| Output          | Phys/Lb2LcTauNuNonPhysTauForB2XTauNuAllLines/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }                          |
