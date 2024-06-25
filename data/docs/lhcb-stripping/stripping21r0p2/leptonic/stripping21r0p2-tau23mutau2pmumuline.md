[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingTau23MuTau2PMuMuLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/Tau23MuTau2PMuMuLine/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseProtons**

|      |                                     |
|------|-------------------------------------|
| Code | 0 StdLooseProtons /Particles',True) |

**CombineParticles/Tau23MuTau2PMuMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r0p2-stdloosemuons) ' , 'Phys/ [StdLooseProtons](./stripping21r0p2-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & ( PIDmu \> -5 ) & ( (PIDmu - PIDK) \> 0 ) & ( TRGHOSTPROB \< 0.45 )' , 'mu-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & ( PIDmu \> -5 ) & ( (PIDmu - PIDK) \> 0 ) & ( TRGHOSTPROB \< 0.45 )' , 'p+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (PIDp\>10) & ( TRGHOSTPROB \< 0.45 )' , 'p\~-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (PIDp\>10) & ( TRGHOSTPROB \< 0.45 )' } |
| CombinationCut   | ( (ADAMASS('tau+')\<150\*MeV) \| (ADAMASS('Lambda_c+')\<150\*MeV) )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME () \* c_light) \> 100 \* micrometer ) & ( BPVIPCHI2() \< 225 )                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ ' [ tau+ -\> p+ mu+ mu- ]cc' , ' [ tau+ -\> p\~- mu+ mu+ ]cc' , ' [ Lambda_c+ -\> p+ mu+ mu- ]cc' , ' [ Lambda_c+ -\> p\~- mu+ mu+ ]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output           | Phys/Tau23MuTau2PMuMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

**AddRelatedInfo/RelatedInfo1_Tau23MuTau2PMuMuLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau2PMuMuLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_Tau23MuTau2PMuMuLine/Particles |

**AddRelatedInfo/RelatedInfo2_Tau23MuTau2PMuMuLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau2PMuMuLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_Tau23MuTau2PMuMuLine/Particles |

**AddRelatedInfo/RelatedInfo3_Tau23MuTau2PMuMuLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau2PMuMuLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_Tau23MuTau2PMuMuLine/Particles |

**AddRelatedInfo/RelatedInfo4_Tau23MuTau2PMuMuLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau2PMuMuLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_Tau23MuTau2PMuMuLine/Particles |
