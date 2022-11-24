[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLc23MuSigmacppLc2pemupi0MLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/Lc23MuSigmacppLc2pemupi0MLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT1           | None                                         |
| HLT2           | None                                         |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SELECT:Phys/StdLooseProtons**

|      |                                     |
|------|-------------------------------------|
| Code | 0 StdLooseProtons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseElectrons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseMuons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseMuons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseMergedPi0 /Particles',True) |

**DaVinci::N4BodyDecays/Lc23MuLc2pemupi0M**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r1p2-stdlooseelectrons) ' , 'Phys/ [StdLooseMergedPi0](./stripping21r1p2-stdloosemergedpi0) ' , 'Phys/ [StdLooseMuons](./stripping21r1p2-stdloosemuons) ' , 'Phys/ [StdLooseProtons](./stripping21r1p2-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDe-PIDpi)\>2)' , 'e-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDe-PIDpi)\>2)' , 'mu+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDmu-PIDpi)\>-5) & ((PIDmu-PIDK)\>-5)' , 'mu-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDmu-PIDpi)\>-5) & ((PIDmu-PIDK)\>-5)' , 'p+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' , 'pi0' : '\n ( PT \> 500\*MeV )\n & (M \> 135 - 60 \*MeV) & (M \< 135 + 60 \*MeV)\n ' , 'p\~-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' } |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 500\*MeV) & (ACHI2DOCA(1,4) \< 10.0) & (ACHI2DOCA(2,4) \< 10.0) & (ACHI2DOCA(3,4) \< 10.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME()\*c_light) \> 70\*micrometer ) & ( BPVIPCHI2() \< 100 ) & ( BPVDIRA \> 0.999 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ e+ mu- pi0]cc' , '[Lambda_c+ -\> p+ e- mu+ pi0]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/Lc23MuLc2pemupi0M/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsPions /Particles',True) |

**CombineParticles/Lc23MuSigmacppLc2pemupi0MLine**

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lc23MuLc2pemupi0M' , 'Phys/ [StdAllNoPIDsPions](./stripping21r1p2-stdallnopidspions) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c\~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }       |
| CombinationCut   | ( (AM - AM1) \< 400\*MeV )                                                                         |
| MotherCut        | ( VFASPF(VCHI2/VDOF) \< 30.0 )                                                                     |
| DecayDescriptor  | None                                                                                               |
| DecayDescriptors | [ '[Sigma_c++ -\> Lambda_c+ pi+]cc' ]                                                          |
| Output           | Phys/Lc23MuSigmacppLc2pemupi0MLine/Particles                                                       |
