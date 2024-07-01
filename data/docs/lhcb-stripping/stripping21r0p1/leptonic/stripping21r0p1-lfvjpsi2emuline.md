[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingLFVJPsi2eMuLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/LFVJPsi2eMuLine/Particles |
| Postscale      | 1.0000000                      |
| HLT1           | None                           |
| HLT2           | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

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

**LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21r0p1-stdloosemuons) /Particles',True)\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles**

|      |                                                                                               |
|------|-----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseElectrons](./stripping21r0p1-stdlooseelectrons) /Particles',True)\>0 |

**CombineParticles/LFVJPsi2eMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r0p1-stdlooseelectrons) ' , 'Phys/ [StdLooseMuons](./stripping21r0p1-stdloosemuons) ' ]                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(MIPCHI2DV(PRIMARY)\> 36.0)&(TRCHI2DOF \< 3.0)&(PIDe\>-2)' , 'e-' : '(MIPCHI2DV(PRIMARY)\> 36.0)&(TRCHI2DOF \< 3.0)&(PIDe\>-2)' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 36.0) & (TRCHI2DOF \< 3.0) & (TRGHOSTPROB\< 0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 36.0) & (TRCHI2DOF \< 3.0) & (TRGHOSTPROB\< 0.3)' } |
| CombinationCut   | (ADAMASS('J/psi(1S)') \< 1000)& (AMAXDOCA('') \< 0.3)                                                                                                                                                                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('J/psi(1S)') \< 1000 )& (BPVDIRA \> 0) & (BPVVDCHI2 \> 256)& (BPVIPCHI2() \< 25)                                                                                                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ '[J/psi(1S) -\> e+ mu-]cc' , '[J/psi(1S) -\> e+ mu+]cc' ]                                                                                                                                                                                                                                                              |
| Output           | Phys/LFVJPsi2eMuLine/Particles                                                                                                                                                                                                                                                                                                 |

**AddRelatedInfo/RelatedInfo1_LFVJPsi2eMuLine**

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/LFVJPsi2eMuLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo1_LFVJPsi2eMuLine/Particles |

**AddRelatedInfo/RelatedInfo2_LFVJPsi2eMuLine**

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/LFVJPsi2eMuLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo2_LFVJPsi2eMuLine/Particles |

**AddRelatedInfo/RelatedInfo3_LFVJPsi2eMuLine**

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/LFVJPsi2eMuLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo3_LFVJPsi2eMuLine/Particles |

**AddRelatedInfo/RelatedInfo4_LFVJPsi2eMuLine**

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/LFVJPsi2eMuLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo4_LFVJPsi2eMuLine/Particles |

**AddRelatedInfo/RelatedInfo5_LFVJPsi2eMuLine**

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/LFVJPsi2eMuLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo5_LFVJPsi2eMuLine/Particles |

**AddRelatedInfo/RelatedInfo6_LFVJPsi2eMuLine**

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/LFVJPsi2eMuLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo6_LFVJPsi2eMuLine/Particles |
