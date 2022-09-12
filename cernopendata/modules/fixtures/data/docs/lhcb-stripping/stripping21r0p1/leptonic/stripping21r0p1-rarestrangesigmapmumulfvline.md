[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingRareStrangeSigmaPMuMuLFVLine

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaPMuMuLFVLine/Particles |
| Postscale      | 1.0000000                                   |
| HLT1           | None                                        |
| HLT2           | None                                        |
| Prescale       | 1.0000000                                   |
| L0DU           | None                                        |
| ODIN           | None                                        |

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
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r0p1-stdallloosemuons) /Particles',True)\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                           |
|------|-------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21r0p1-stdlooseprotons) /Particles',True)\>0 |

**CombineParticles/RareStrangeSigmaPMuMuLFVLine**

|                  |                                                                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p1-stdallloosemuons) ' , 'Phys/ [StdLooseProtons](./stripping21r0p1-stdlooseprotons) ' ]                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'mu-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'p+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05)' , 'p\~-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05)' } |
| CombinationCut   | (ADAMASS('Sigma+')\<500.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 36.0) & (PT\> 500.0 \*MeV)& (ADMASS('Sigma+') \< 500.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 6.0 \* ps)                                                                                                                                                      |
| DecayDescriptor  | [Sigma+ -\> p\~- mu+ mu+]cc                                                                                                                                                                                                                                                                                |
| DecayDescriptors | [ '[Sigma+ -\> p\~- mu+ mu+]cc' ]                                                                                                                                                                                                                                                                        |
| Output           | Phys/RareStrangeSigmaPMuMuLFVLine/Particles                                                                                                                                                                                                                                                                  |

**AddRelatedInfo/RelatedInfo1_RareStrangeSigmaPMuMuLFVLine**

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuLFVLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaPMuMuLFVLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeSigmaPMuMuLFVLine**

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuLFVLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaPMuMuLFVLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeSigmaPMuMuLFVLine**

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuLFVLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaPMuMuLFVLine/Particles |
