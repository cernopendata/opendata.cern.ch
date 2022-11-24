[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingRareStrangeLambdaPPiLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/RareStrangeLambdaPPiLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 0.010000000                             |
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

**LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles**

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLoosePions](./stripping21r0p1-stdallloosepions) /Particles',True)\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                           |
|------|-------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21r0p1-stdlooseprotons) /Particles',True)\>0 |

**CombineParticles/RareStrangeLambdaPPiLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLoosePions](./stripping21r0p1-stdallloosepions) ' , 'Phys/ [StdLooseProtons](./stripping21r0p1-stdlooseprotons) ' ]                                                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'pi+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'pi-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'p\~-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05) & (MIPCHI2DV(PRIMARY)\>9.0)' } |
| CombinationCut   | (ADAMASS('Lambda0')\<50.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 25.0) & (PT\> 500.0 \*MeV)& (ADMASS('Lambda0') \< 50.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 6.0 \* ps)                                                                                                                                                                                                              |
| DecayDescriptor  | [Lambda0 -\> p+ pi-]cc                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[Lambda0 -\> p+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                     |
| Output           | Phys/RareStrangeLambdaPPiLine/Particles                                                                                                                                                                                                                                                                                                                              |

**AddRelatedInfo/RelatedInfo1_RareStrangeLambdaPPiLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeLambdaPPiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_RareStrangeLambdaPPiLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeLambdaPPiLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeLambdaPPiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo2_RareStrangeLambdaPPiLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeLambdaPPiLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeLambdaPPiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo3_RareStrangeLambdaPPiLine/Particles |
