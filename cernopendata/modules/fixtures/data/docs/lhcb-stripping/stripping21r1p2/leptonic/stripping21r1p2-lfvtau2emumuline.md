[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLFVTau2eMuMuLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/LFVTau2eMuMuLine/Particles |
| Postscale      | 1.0000000                       |
| HLT1           | None                            |
| HLT2           | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseElectrons /Particles',True) |

**CombineParticles/LFVTau2eMuMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r1p2-stdlooseelectrons) ' , 'Phys/ [StdLooseMuons](./stripping21r1p2-stdloosemuons) ' ]                                                                                                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (PIDe \> 2) ' , 'e-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (PIDe \> 2) ' , 'mu+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (TRGHOSTPROB\<0.3) ' , 'mu-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (TRGHOSTPROB\<0.3) ' } |
| CombinationCut   | (ADAMASS('tau+')\<200\*MeV)                                                                                                                                                                                                                                                                                                                                                                                        |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME () \* c_light) \> 100 \* micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ ' [ tau+ -\> e+ mu+ mu- ]cc' , ' [ tau+ -\> mu+ mu+ e- ]cc' ]                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/LFVTau2eMuMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                    |
