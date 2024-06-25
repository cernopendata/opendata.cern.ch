[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingRareStrangeSigmaPEMuLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaPEMuLine/Particles |
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

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r1p1-stdallloosemuons) /Particles',True)\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseElectrons_Particles**

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseElectrons](./stripping21r1p1-stdalllooseelectrons) /Particles',True)\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                           |
|------|-------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21r1p1-stdlooseprotons) /Particles',True)\>0 |

**CombineParticles/RareStrangeSigmaPEMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseElectrons](./stripping21r1p1-stdalllooseelectrons) ' , 'Phys/ [StdAllLooseMuons](./stripping21r1p1-stdallloosemuons) ' , 'Phys/ [StdLooseProtons](./stripping21r1p1-stdlooseprotons) ' ]                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'e-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'mu+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'mu-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'p+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05)' , 'p\~-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05)' } |
| CombinationCut   | (ADAMASS('Sigma+')\<500.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                                                                                                                                                                                                                                                                                                       |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 36.0) & (PT\> 500.0 \*MeV)& (ADMASS('Sigma+') \< 500.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 6.0 \* ps)                                                                                                                                                                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Sigma+ -\> p+ e+ mu-]cc' , '[Sigma+ -\> p+ mu+ e-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/RareStrangeSigmaPEMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                            |

**AddRelatedInfo/RelatedInfo1_RareStrangeSigmaPEMuLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPEMuLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaPEMuLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeSigmaPEMuLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPEMuLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaPEMuLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeSigmaPEMuLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPEMuLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaPEMuLine/Particles |
