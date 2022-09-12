[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLFVBu2KJPsieeLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/LFVBu2KJPsieeLine/Particles |
| Postscale      | 1.0000000                        |
| HLT1           | None                             |
| HLT2           | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseElectrons /Particles',True) |

**CombineParticles/LFVBu2KJPsiee**

|                  |                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r1p2-stdlooseelectrons) ' ]                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 25.) & (PIDe \> 2) ' , 'e-' : '(TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 25.) & (PIDe \> 2) ' } |
| CombinationCut   | (ADAMASS('J/psi(1S)')\<1000\*MeV) & (AMAXDOCA('')\<0.3\*mm)                                                                                                      |
| MotherCut        | (VFASPF(VCHI2)\<9) & (ADMASS('J/psi(1S)') \< 1000\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\>169)                                                                      |
| DecayDescriptor  | J/psi(1S) -\> e+ e-                                                                                                                                              |
| DecayDescriptors | [ 'J/psi(1S) -\> e+ e-' ]                                                                                                                                      |
| Output           | Phys/LFVBu2KJPsiee/Particles                                                                                                                                     |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsKaons**

|      |                                    |
|------|------------------------------------|
| Code | 0 StdNoPIDsKaons /Particles',True) |

**CombineParticles/LFVBu2KJPsieeLine**

|                  |                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LFVBu2KJPsiee' , 'Phys/ [StdNoPIDsKaons](./stripping21r1p2-stdnopidskaons) ' ]                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : '(ISLONG) & (TRCHI2DOF \< 3 ) &(MIPCHI2DV(PRIMARY)\>25)& (PT\>250\*MeV) & (TRGHOSTPROB\<0.3) ' , 'K-' : '(ISLONG) & (TRCHI2DOF \< 3 ) &(MIPCHI2DV(PRIMARY)\>25)& (PT\>250\*MeV) & (TRGHOSTPROB\<0.3) ' } |
| CombinationCut   | (ADAMASS('B+') \< 600\*MeV)                                                                                                                                                                                                                          |
| MotherCut        | (BPVIPCHI2()\< 25)& (VFASPF(VCHI2)\<45)                                                                                                                                                                                                              |
| DecayDescriptor  | [B+ -\> J/psi(1S) K+]cc                                                                                                                                                                                                                            |
| DecayDescriptors | [ ' [B+ -\> J/psi(1S) K+]cc ' ]                                                                                                                                                                                                                  |
| Output           | Phys/LFVBu2KJPsieeLine/Particles                                                                                                                                                                                                                     |

**AddRelatedInfo/RelatedInfo1_LFVBu2KJPsieeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/LFVBu2KJPsieeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo1_LFVBu2KJPsieeLine/Particles |

**AddRelatedInfo/RelatedInfo2_LFVBu2KJPsieeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/LFVBu2KJPsieeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo2_LFVBu2KJPsieeLine/Particles |

**AddRelatedInfo/RelatedInfo3_LFVBu2KJPsieeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/LFVBu2KJPsieeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo3_LFVBu2KJPsieeLine/Particles |

**AddRelatedInfo/RelatedInfo4_LFVBu2KJPsieeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/LFVBu2KJPsieeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo4_LFVBu2KJPsieeLine/Particles |

**AddRelatedInfo/RelatedInfo5_LFVBu2KJPsieeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/LFVBu2KJPsieeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo5_LFVBu2KJPsieeLine/Particles |

**AddRelatedInfo/RelatedInfo6_LFVBu2KJPsieeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/LFVBu2KJPsieeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo6_LFVBu2KJPsieeLine/Particles |

**AddRelatedInfo/RelatedInfo7_LFVBu2KJPsieeLine**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/LFVBu2KJPsieeLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo7_LFVBu2KJPsieeLine/Particles |
