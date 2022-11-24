[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingRareStrangeSigmaPMuMuLFVDownLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaPMuMuLFVDownLine/Particles |
| Postscale      | 1.0000000                                       |
| HLT1           | None                                            |
| HLT2           | None                                            |
| Prescale       | 0.10000000                                      |
| L0DU           | None                                            |
| ODIN           | None                                            |

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
| Code | CONTAINS('Phys/ [StdLooseDownMuons](./stripping21r0p1-stdloosedownmuons) /Particles',True)\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownProtons_Particles**

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsDownProtons](./stripping21r0p1-stdnopidsdownprotons) /Particles',True)\>0 |

**CombineParticles/RareStrangeSigmaPMuMuLFVDownLine**

|                  |                                                                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseDownMuons](./stripping21r0p1-stdloosedownmuons) ' , 'Phys/ [StdNoPIDsDownProtons](./stripping21r0p1-stdnopidsdownprotons) ' ]                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF\<9.0) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'mu-' : '(TRCHI2DOF\<9.0) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'p+' : '(TRCHI2DOF\<9.0) & (TRGHOSTPROB\<0.3)' , 'p\~-' : '(TRCHI2DOF\<9.0) & (TRGHOSTPROB\<0.3)' } |
| CombinationCut   | (ADAMASS('Sigma+')\<500.0 \*MeV) & (AMAXDOCA('')\< 10.0 \*mm)                                                                                                                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 25.0) & (PT\> 0.0 \*MeV)& (ADMASS('Sigma+') \< 500.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 25.0)& (BPVLTIME()\> 7.0 \* ps)                                                                                                                          |
| DecayDescriptor  | [Sigma+ -\> p\~- mu+ mu+]cc                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[Sigma+ -\> p\~- mu+ mu+]cc' ]                                                                                                                                                                                                                                          |
| Output           | Phys/RareStrangeSigmaPMuMuLFVDownLine/Particles                                                                                                                                                                                                                                |

**AddRelatedInfo/RelatedInfo1_RareStrangeSigmaPMuMuLFVDownLine**

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuLFVDownLine' ]                |
| DecayDescriptor | None                                                         |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaPMuMuLFVDownLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeSigmaPMuMuLFVDownLine**

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuLFVDownLine' ]                |
| DecayDescriptor | None                                                         |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaPMuMuLFVDownLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeSigmaPMuMuLFVDownLine**

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuLFVDownLine' ]                |
| DecayDescriptor | None                                                         |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaPMuMuLFVDownLine/Particles |
