[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBs2MuMuLinesBs2JPsiPhiLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/Bs2MuMuLinesBs2JPsiPhiLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT1           | None                                      |
| HLT2           | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

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

**CombineParticles/Bs2MuMuLinesBs2JPsiPhiSelJpsi**

|                  |                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r1p2-stdloosemuons) ' ]                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 4) & (MIPCHI2DV(PRIMARY)\> 25.) & ( TRGHOSTPROB \< 0.4 )' , 'mu-' : '(TRCHI2DOF \< 4) & (MIPCHI2DV(PRIMARY)\> 25.) & ( TRGHOSTPROB \< 0.4 )' } |
| CombinationCut   | (ADAMASS('J/psi(1S)')\<100\*MeV) & (AMAXDOCA('')\<0.3\*mm)                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2)\<9) & (ADMASS('J/psi(1S)') \< 100\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 121)                                                                                          |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                                                                                |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                                                                        |
| Output           | Phys/Bs2MuMuLinesBs2JPsiPhiSelJpsi/Particles                                                                                                                                         |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsKaons**

|      |                                    |
|------|------------------------------------|
| Code | 0 StdNoPIDsKaons /Particles',True) |

**CombineParticles/Bs2MuMuLinesBs2JPsiPhiSelPhi**

|                  |                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdNoPIDsKaons](./stripping21r1p2-stdnopidskaons) ' ]                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(ISLONG) & (TRCHI2DOF \< 4 ) & (MIPCHI2DV(PRIMARY)\> 4.) & (PT\>250\*MeV) & ( TRGHOSTPROB \< 0.4 )' , 'K-' : '(ISLONG) & (TRCHI2DOF \< 4 ) & (MIPCHI2DV(PRIMARY)\> 4.) & (PT\>250\*MeV) & ( TRGHOSTPROB \< 0.4 )' } |
| CombinationCut   | (ADAMASS('phi(1020)')\<20\*MeV)                                                                                                                                                                                                            |
| MotherCut        | (MIPCHI2DV(PRIMARY)\> 9)                                                                                                                                                                                                                   |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                                                                                                                                                                                        |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                                                                                                                                |
| Output           | Phys/Bs2MuMuLinesBs2JPsiPhiSelPhi/Particles                                                                                                                                                                                                |

**CombineParticles/Bs2MuMuLinesBs2JPsiPhiLine**

|                  |                                                                                  |
|------------------|----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2MuMuLinesBs2JPsiPhiSelJpsi' , 'Phys/Bs2MuMuLinesBs2JPsiPhiSelPhi' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'phi(1020)' : 'ALL' }                       |
| CombinationCut   | (ADAMASS('B_s0') \< 500\*MeV)                                                    |
| MotherCut        | (BPVIPCHI2()\< 25)& (VFASPF(VCHI2)\<75)                                          |
| DecayDescriptor  | B_s0 -\> J/psi(1S) phi(1020)                                                     |
| DecayDescriptors | [ 'B_s0 -\> J/psi(1S) phi(1020)' ]                                             |
| Output           | Phys/Bs2MuMuLinesBs2JPsiPhiLine/Particles                                        |

**AddRelatedInfo/RelatedInfo1_Bs2MuMuLinesBs2JPsiPhiLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_Bs2MuMuLinesBs2JPsiPhiLine/Particles |

**AddRelatedInfo/RelatedInfo2_Bs2MuMuLinesBs2JPsiPhiLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo2_Bs2MuMuLinesBs2JPsiPhiLine/Particles |

**AddRelatedInfo/RelatedInfo3_Bs2MuMuLinesBs2JPsiPhiLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo3_Bs2MuMuLinesBs2JPsiPhiLine/Particles |

**AddRelatedInfo/RelatedInfo4_Bs2MuMuLinesBs2JPsiPhiLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo4_Bs2MuMuLinesBs2JPsiPhiLine/Particles |

**AddRelatedInfo/RelatedInfo5_Bs2MuMuLinesBs2JPsiPhiLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo5_Bs2MuMuLinesBs2JPsiPhiLine/Particles |

**AddRelatedInfo/RelatedInfo6_Bs2MuMuLinesBs2JPsiPhiLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo6_Bs2MuMuLinesBs2JPsiPhiLine/Particles |

**AddRelatedInfo/RelatedInfo7_Bs2MuMuLinesBs2JPsiPhiLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo7_Bs2MuMuLinesBs2JPsiPhiLine/Particles |

**AddRelatedInfo/RelatedInfo8_Bs2MuMuLinesBs2JPsiPhiLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo8_Bs2MuMuLinesBs2JPsiPhiLine/Particles |

**AddRelatedInfo/RelatedInfo9_Bs2MuMuLinesBs2JPsiPhiLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBs2JPsiPhiLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo9_Bs2MuMuLinesBs2JPsiPhiLine/Particles |
