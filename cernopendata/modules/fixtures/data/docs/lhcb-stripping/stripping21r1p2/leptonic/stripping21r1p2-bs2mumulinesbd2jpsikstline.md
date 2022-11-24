[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBs2MuMuLinesBd2JPsiKstLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/Bs2MuMuLinesBd2JPsiKstLine/Particles |
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

**CombineParticles/Bs2MuMuLinesBd2JPsiKstSelJpsi**

|                  |                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r1p2-stdloosemuons) ' ]                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 4) & (MIPCHI2DV(PRIMARY)\> 25.) & ( TRGHOSTPROB \< 0.4 )' , 'mu-' : '(TRCHI2DOF \< 4) & (MIPCHI2DV(PRIMARY)\> 25.) & ( TRGHOSTPROB \< 0.4 )' } |
| CombinationCut   | (ADAMASS('J/psi(1S)')\<100\*MeV) & (AMAXDOCA('')\<0.3\*mm)                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2)\<9) & (ADMASS('J/psi(1S)') \< 100\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 121)                                                                                          |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                                                                                |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                                                                        |
| Output           | Phys/Bs2MuMuLinesBd2JPsiKstSelJpsi/Particles                                                                                                                                         |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions**

|      |                                    |
|------|------------------------------------|
| Code | 0 StdNoPIDsPions /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsKaons**

|      |                                    |
|------|------------------------------------|
| Code | 0 StdNoPIDsKaons /Particles',True) |

**CombineParticles/Bs2MuMuLinesBd2JPsiKstSelKst**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdNoPIDsKaons](./stripping21r1p2-stdnopidskaons) ' , 'Phys/ [StdNoPIDsPions](./stripping21r1p2-stdnopidspions) ' ]                                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(ISLONG) & (TRCHI2DOF \< 4 ) & ( TRGHOSTPROB \< 0.4 ) & (MIPCHI2DV(PRIMARY)\> 4.)& (PT\>250\*MeV)' , 'K-' : '(ISLONG) & (TRCHI2DOF \< 4 ) & ( TRGHOSTPROB \< 0.4 ) & (MIPCHI2DV(PRIMARY)\> 4.)& (PT\>250\*MeV)' , 'pi+' : '(ISLONG) & (TRCHI2DOF \< 4 ) & ( TRGHOSTPROB \< 0.4 )& (MIPCHI2DV(PRIMARY)\> 4.)& (PT\>250\*MeV)' , 'pi-' : '(ISLONG) & (TRCHI2DOF \< 4 ) & ( TRGHOSTPROB \< 0.4 )& (MIPCHI2DV(PRIMARY)\> 4.)& (PT\>250\*MeV)' } |
| CombinationCut   | (ADAMASS('K\*(892)0')\<2000\*MeV)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | (MIPCHI2DV(PRIMARY)\> 9)                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptor  | [K\*(892)0 -\> K+ pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/Bs2MuMuLinesBd2JPsiKstSelKst/Particles                                                                                                                                                                                                                                                                                                                                                                                                                        |

**CombineParticles/Bs2MuMuLinesBd2JPsiKstLine**

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2MuMuLinesBd2JPsiKstSelJpsi' , 'Phys/Bs2MuMuLinesBd2JPsiKstSelKst' ]   |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' } |
| CombinationCut   | (ADAMASS('B0') \< 500\*MeV)                                                        |
| MotherCut        | (BPVIPCHI2()\< 25) & (VFASPF(VCHI2)\<75)                                           |
| DecayDescriptor  | [B0 -\> J/psi(1S) K\*(892)0]cc                                                   |
| DecayDescriptors | [ '[B0 -\> J/psi(1S) K\*(892)0]cc' ]                                           |
| Output           | Phys/Bs2MuMuLinesBd2JPsiKstLine/Particles                                          |

**AddRelatedInfo/RelatedInfo1_Bs2MuMuLinesBd2JPsiKstLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_Bs2MuMuLinesBd2JPsiKstLine/Particles |

**AddRelatedInfo/RelatedInfo2_Bs2MuMuLinesBd2JPsiKstLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo2_Bs2MuMuLinesBd2JPsiKstLine/Particles |

**AddRelatedInfo/RelatedInfo3_Bs2MuMuLinesBd2JPsiKstLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo3_Bs2MuMuLinesBd2JPsiKstLine/Particles |

**AddRelatedInfo/RelatedInfo4_Bs2MuMuLinesBd2JPsiKstLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo4_Bs2MuMuLinesBd2JPsiKstLine/Particles |

**AddRelatedInfo/RelatedInfo5_Bs2MuMuLinesBd2JPsiKstLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo5_Bs2MuMuLinesBd2JPsiKstLine/Particles |

**AddRelatedInfo/RelatedInfo6_Bs2MuMuLinesBd2JPsiKstLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo6_Bs2MuMuLinesBd2JPsiKstLine/Particles |

**AddRelatedInfo/RelatedInfo7_Bs2MuMuLinesBd2JPsiKstLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo7_Bs2MuMuLinesBd2JPsiKstLine/Particles |

**AddRelatedInfo/RelatedInfo8_Bs2MuMuLinesBd2JPsiKstLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo8_Bs2MuMuLinesBd2JPsiKstLine/Particles |

**AddRelatedInfo/RelatedInfo9_Bs2MuMuLinesBd2JPsiKstLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBd2JPsiKstLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo9_Bs2MuMuLinesBd2JPsiKstLine/Particles |
