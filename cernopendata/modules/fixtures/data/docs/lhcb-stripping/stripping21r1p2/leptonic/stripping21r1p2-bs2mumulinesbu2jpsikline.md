[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBs2MuMuLinesBu2JPsiKLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/Bs2MuMuLinesBu2JPsiKLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

**CombineParticles/Bs2MuMuLinesBu2JPsiKSelJpsi**

|                  |                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r1p2-stdloosemuons) ' ]                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 4) & (MIPCHI2DV(PRIMARY)\> 25.) & ( TRGHOSTPROB \< 0.4 )' , 'mu-' : '(TRCHI2DOF \< 4) & (MIPCHI2DV(PRIMARY)\> 25.) & ( TRGHOSTPROB \< 0.4 )' } |
| CombinationCut   | (ADAMASS('J/psi(1S)')\<100\*MeV) & (AMAXDOCA('')\<0.3\*mm)                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2)\<9) & (ADMASS('J/psi(1S)') \< 100\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 121)                                                                                          |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                                                                                |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                                                                        |
| Output           | Phys/Bs2MuMuLinesBu2JPsiKSelJpsi/Particles                                                                                                                                           |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsKaons**

|      |                                    |
|------|------------------------------------|
| Code | 0 StdNoPIDsKaons /Particles',True) |

**CombineParticles/Bs2MuMuLinesBu2JPsiKLine**

|                  |                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2MuMuLinesBu2JPsiKSelJpsi' , 'Phys/ [StdNoPIDsKaons](./stripping21r1p2-stdnopidskaons) ' ]                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : '(ISLONG) & (TRCHI2DOF \< 4 ) &(MIPCHI2DV(PRIMARY)\>9)& (PT\>250\*MeV) & ( TRGHOSTPROB \< 0.4 )' , 'K-' : '(ISLONG) & (TRCHI2DOF \< 4 ) &(MIPCHI2DV(PRIMARY)\>9)& (PT\>250\*MeV) & ( TRGHOSTPROB \< 0.4 )' } |
| CombinationCut   | (ADAMASS('B+') \< 500\*MeV)                                                                                                                                                                                                                              |
| MotherCut        | (BPVIPCHI2()\< 25)& (VFASPF(VCHI2)\<45)                                                                                                                                                                                                                  |
| DecayDescriptor  | [B+ -\> J/psi(1S) K+]cc                                                                                                                                                                                                                                |
| DecayDescriptors | [ ' [B+ -\> J/psi(1S) K+]cc ' ]                                                                                                                                                                                                                      |
| Output           | Phys/Bs2MuMuLinesBu2JPsiKLine/Particles                                                                                                                                                                                                                  |

**AddRelatedInfo/RelatedInfo1_Bs2MuMuLinesBu2JPsiKLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_Bs2MuMuLinesBu2JPsiKLine/Particles |

**AddRelatedInfo/RelatedInfo2_Bs2MuMuLinesBu2JPsiKLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo2_Bs2MuMuLinesBu2JPsiKLine/Particles |

**AddRelatedInfo/RelatedInfo3_Bs2MuMuLinesBu2JPsiKLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo3_Bs2MuMuLinesBu2JPsiKLine/Particles |

**AddRelatedInfo/RelatedInfo4_Bs2MuMuLinesBu2JPsiKLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo4_Bs2MuMuLinesBu2JPsiKLine/Particles |

**AddRelatedInfo/RelatedInfo5_Bs2MuMuLinesBu2JPsiKLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo5_Bs2MuMuLinesBu2JPsiKLine/Particles |

**AddRelatedInfo/RelatedInfo6_Bs2MuMuLinesBu2JPsiKLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo6_Bs2MuMuLinesBu2JPsiKLine/Particles |

**AddRelatedInfo/RelatedInfo7_Bs2MuMuLinesBu2JPsiKLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo7_Bs2MuMuLinesBu2JPsiKLine/Particles |

**AddRelatedInfo/RelatedInfo8_Bs2MuMuLinesBu2JPsiKLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo8_Bs2MuMuLinesBu2JPsiKLine/Particles |

**AddRelatedInfo/RelatedInfo9_Bs2MuMuLinesBu2JPsiKLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBu2JPsiKLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo9_Bs2MuMuLinesBu2JPsiKLine/Particles |
