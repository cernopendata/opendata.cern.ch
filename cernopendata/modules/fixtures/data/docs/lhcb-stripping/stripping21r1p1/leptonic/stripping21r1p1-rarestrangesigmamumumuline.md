[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingRareStrangeSigmaMuMuMuLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaMuMuMuLine/Particles |
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

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r1p1-stdallloosemuons) /Particles',True)\>0 |

**CombineParticles/RareStrangeSigmaMuMuMuLine**

|                  |                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r1p1-stdallloosemuons) ' ]                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>5.0)' , 'mu-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>5.0)' } |
| CombinationCut   | (ADAMASS('Sigma+')\<500.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 36.0) & (PT\> 0.0 \*MeV)& (ADMASS('Sigma+') \< 500.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 3 \* ps)                    |
| DecayDescriptor  | [Sigma+ -\> mu+ mu+ mu-]cc                                                                                                                                           |
| DecayDescriptors | [ '[Sigma+ -\> mu+ mu+ mu-]cc' ]                                                                                                                                   |
| Output           | Phys/RareStrangeSigmaMuMuMuLine/Particles                                                                                                                              |

**AddRelatedInfo/RelatedInfo1_RareStrangeSigmaMuMuMuLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaMuMuMuLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaMuMuMuLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeSigmaMuMuMuLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaMuMuMuLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaMuMuMuLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeSigmaMuMuMuLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaMuMuMuLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaMuMuMuLine/Particles |
