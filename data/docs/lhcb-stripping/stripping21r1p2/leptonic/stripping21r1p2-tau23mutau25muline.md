[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingTau23MuTau25MuLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/Tau23MuTau25MuLine/Particles |
| Postscale      | 1.0000000                         |
| HLT1           | None                              |
| HLT2           | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseMuons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseMuons /Particles',True) |

**CombineParticles/Tau23MuTau25MuLine**

|                  |                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r1p2-stdloosemuons) ' ]                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' ( PT \> 300 \* MeV ) & ( TRGHOSTPROB \< 0.45 ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) ' , 'mu-' : ' ( PT \> 300 \* MeV ) & ( TRGHOSTPROB \< 0.45 ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) ' } |
| CombinationCut   | (ADAMASS('tau+')\<400\*MeV)                                                                                                                                                                                                        |
| MotherCut        | ( VFASPF(VCHI2) \< 30 ) & ( (BPVLTIME () \* c_light) \> 100 \* micrometer ) & ( BPVIPCHI2() \< 225 )                                                                                                                               |
| DecayDescriptor  | [ tau+ -\> mu+ mu+ mu+ mu- mu-]cc                                                                                                                                                                                                |
| DecayDescriptors | [ ' [ tau+ -\> mu+ mu+ mu+ mu- mu-]cc' ]                                                                                                                                                                                       |
| Output           | Phys/Tau23MuTau25MuLine/Particles                                                                                                                                                                                                  |
