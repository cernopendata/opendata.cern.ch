[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLc23MuSigmacppLc2pKpiLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/Lc23MuSigmacppLc2pKpiLine/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 0.010000000                              |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseKaons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseKaons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLoosePions**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLoosePions /Particles',True) |

**DaVinci::N3BodyDecays/Lc23MuLc2pKpi**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseKaons](./stripping21r1p2-stdloosekaons) ' , 'Phys/ [StdLoosePions](./stripping21r1p2-stdloosepions) ' , 'Phys/ [StdLooseProtons](./stripping21r1p2-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDK-PIDpi)\>5) & ((PIDK-PIDp)\>0)' , 'K-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDK-PIDpi)\>5) & ((PIDK-PIDp)\>0)' , 'p+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' , 'pi+' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n ' , 'pi-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n ' , 'p\~-' : '\n (PT \> 300\*MeV)\n & (BPVIPCHI2() \> 9)\n & (TRCHI2DOF \< 4.0)\n & (TRGHP \< 0.4)\n & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' } |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 150\*MeV) & (ADOCA(1,3) \< 0.3\*mm) & (ADOCA(2,3) \< 0.3\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME()\*c_light) \> 70\*micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Output           | Phys/Lc23MuLc2pKpi/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsPions /Particles',True) |

**CombineParticles/Lc23MuSigmacppLc2pKpiLine**

|                  |                                                                                                |
|------------------|------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lc23MuLc2pKpi' , 'Phys/ [StdAllNoPIDsPions](./stripping21r1p2-stdallnopidspions) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c\~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }   |
| CombinationCut   | ( (AM - AM1) \< 400\*MeV )                                                                     |
| MotherCut        | ( VFASPF(VCHI2/VDOF) \< 30.0 )                                                                 |
| DecayDescriptor  | None                                                                                           |
| DecayDescriptors | [ '[Sigma_c++ -\> Lambda_c+ pi+]cc' ]                                                      |
| Output           | Phys/Lc23MuSigmacppLc2pKpiLine/Particles                                                       |
