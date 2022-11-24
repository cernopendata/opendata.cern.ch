[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingLFVB2eMuLine

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/LFVB2eMuLine/Particles |
| Postscale      | 1.0000000                   |
| HLT1           | None                        |
| HLT2           | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

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

**CombineParticles/LFVB2eMuLine**

|                  |                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r0p1-stdlooseelectrons) ' , 'Phys/ [StdLooseMuons](./stripping21r0p1-stdloosemuons) ' ]                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(MIPCHI2DV(PRIMARY)\> 25.0)&(TRCHI2DOF \< 3.0)' , 'e-' : '(MIPCHI2DV(PRIMARY)\> 25.0)&(TRCHI2DOF \< 3.0)' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 25.0) & (TRCHI2DOF \< 3.0) & (TRGHOSTPROB\< 0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 25.0) & (TRCHI2DOF \< 3.0) & (TRGHOSTPROB\< 0.3)' } |
| CombinationCut   | (ADAMASS('B_s0') \< 1200.0)& (AMAXDOCA('') \< 0.3)                                                                                                                                                                                                                                                       |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 1200.0 )& (BPVDIRA \> 0) & (BPVVDCHI2 \> 225)& (BPVIPCHI2() \< 25)                                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[B_s0 -\> e+ mu-]cc' , '[B_s0 -\> e+ mu+]cc' ]                                                                                                                                                                                                                                                  |
| Output           | Phys/LFVB2eMuLine/Particles                                                                                                                                                                                                                                                                              |

**AddRelatedInfo/RelatedInfo1_LFVB2eMuLine**

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/LFVB2eMuLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo1_LFVB2eMuLine/Particles |

**AddRelatedInfo/RelatedInfo2_LFVB2eMuLine**

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/LFVB2eMuLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo2_LFVB2eMuLine/Particles |

**AddRelatedInfo/RelatedInfo3_LFVB2eMuLine**

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/LFVB2eMuLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo3_LFVB2eMuLine/Particles |

**AddRelatedInfo/RelatedInfo4_LFVB2eMuLine**

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/LFVB2eMuLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo4_LFVB2eMuLine/Particles |

**AddRelatedInfo/RelatedInfo5_LFVB2eMuLine**

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/LFVB2eMuLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo5_LFVB2eMuLine/Particles |

**AddRelatedInfo/RelatedInfo6_LFVB2eMuLine**

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/LFVB2eMuLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo6_LFVB2eMuLine/Particles |
