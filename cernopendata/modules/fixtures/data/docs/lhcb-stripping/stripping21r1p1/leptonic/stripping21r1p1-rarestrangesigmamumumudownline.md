[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingRareStrangeSigmaMuMuMuDownLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaMuMuMuDownLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT1           | None                                          |
| HLT2           | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

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

**LoKi::VoidFilter/SelFilterPhys_StdLooseDownMuons_Particles**

|      |                                                                                               |
|------|-----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseDownMuons](./stripping21r1p1-stdloosedownmuons) /Particles',True)\>0 |

**CombineParticles/RareStrangeSigmaMuMuMuDownLine**

|                  |                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseDownMuons](./stripping21r1p1-stdloosedownmuons) ' ]                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF\< 9.0) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>5.0)' , 'mu-' : '(TRCHI2DOF\< 9.0) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>5.0)' } |
| CombinationCut   | (ADAMASS('Sigma+')\<500.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 100.0) & (PT\> 0.0 \*MeV)& (ADMASS('Sigma+') \< 500.0 \*MeV )& (BPVDIRA \> 0.1) & (BPVIPCHI2()\< 100.0)& (BPVLTIME()\> 2 \* ps)                        |
| DecayDescriptor  | [Sigma+ -\> mu+ mu+ mu-]cc                                                                                                                                                 |
| DecayDescriptors | [ '[Sigma+ -\> mu+ mu+ mu-]cc' ]                                                                                                                                         |
| Output           | Phys/RareStrangeSigmaMuMuMuDownLine/Particles                                                                                                                                |

**AddRelatedInfo/RelatedInfo1_RareStrangeSigmaMuMuMuDownLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaMuMuMuDownLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaMuMuMuDownLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeSigmaMuMuMuDownLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaMuMuMuDownLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaMuMuMuDownLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeSigmaMuMuMuDownLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaMuMuMuDownLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaMuMuMuDownLine/Particles |
