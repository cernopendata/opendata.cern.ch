[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingRareStrangeSigmaPMuMuDetLine

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaPMuMuDetLine/Particles |
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

**CombineParticles/RareStrangeDiMuonDetached**

|                  |                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p1-stdallloosemuons) ' ]                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'mu-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' } |
| CombinationCut   | (AM \<700 \*MeV) & (AMAXDOCA('')\< 2 \*mm)                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 36) & (PT\> 0 \*MeV)                                                                                                                             |
| DecayDescriptor  | KS0 -\> mu+ mu-                                                                                                                                                        |
| DecayDescriptors | [ 'KS0 -\> mu+ mu-' ]                                                                                                                                                |
| Output           | Phys/RareStrangeDiMuonDetached/Particles                                                                                                                               |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                           |
|------|-------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21r0p1-stdlooseprotons) /Particles',True)\>0 |

**CombineParticles/RareStrangeSigmaPMuMuDetLine**

|                  |                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/RareStrangeDiMuonDetached' , 'Phys/ [StdLooseProtons](./stripping21r0p1-stdlooseprotons) ' ]                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(MIPCHI2DV(PRIMARY)\>9)' , 'p+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05)' , 'p\~-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05)' } |
| CombinationCut   | (ADAMASS('Sigma+')\<500.0 \*MeV)                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 25) & (PT\> 500.0 \*MeV)& (ADMASS('Sigma+') \< 500.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 6.0 \* ps)                                    |
| DecayDescriptor  | [Sigma+ -\> p+ KS0 ]cc                                                                                                                                                                 |
| DecayDescriptors | [ '[Sigma+ -\> p+ KS0 ]cc' ]                                                                                                                                                         |
| Output           | Phys/RareStrangeSigmaPMuMuDetLine/Particles                                                                                                                                              |

**AddRelatedInfo/RelatedInfo1_RareStrangeSigmaPMuMuDetLine**

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuDetLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaPMuMuDetLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeSigmaPMuMuDetLine**

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuDetLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaPMuMuDetLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeSigmaPMuMuDetLine**

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuDetLine' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaPMuMuDetLine/Particles |
