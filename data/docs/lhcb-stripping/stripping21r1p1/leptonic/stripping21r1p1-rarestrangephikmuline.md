[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingRareStrangePhiKMuLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/RareStrangePhiKMuLine/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 0.010000000                          |
| L0DU           | None                                 |
| ODIN           | None                                 |

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

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles**

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseKaons](./stripping21r1p1-stdallloosekaons) /Particles',True)\>0 |

**CombineParticles/RareStrangePhiKMuLine**

|                  |                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseKaons](./stripping21r1p1-stdallloosekaons) ' , 'Phys/ [StdAllLooseMuons](./stripping21r1p1-stdallloosemuons) ' ]                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF\<5) & (TRGHOSTPROB \< 0.3) & (PT\>400.0) & (PROBNNk \> 0.3)' , 'K-' : '(TRCHI2DOF\<5) & (TRGHOSTPROB \< 0.3) & (PT\>400.0) & (PROBNNk \> 0.3)' , 'mu+' : '(TRCHI2DOF\<5) & (TRGHOSTPROB \< 0.3) & (PT\>400.0)' , 'mu-' : '(TRCHI2DOF\<5) & (TRGHOSTPROB \< 0.3) & (PT\>400.0)' } |
| CombinationCut   | (AWM ('K+','mu+') \> 800 \*MeV) & (AWM ('K+','mu+') \< 1200 \*MeV) & (AMAXDOCA('')\< 0.1 \*mm)                                                                                                                                                                                                                     |
| MotherCut        | (PT\> 700 \* MeV) & (BPVDIRA \> 0.5)& (VFASPF(VCHI2/VDOF) \< 9)                                                                                                                                                                                                                                                    |
| DecayDescriptor  | [phi(1020) -\> K+ mu-]cc                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[phi(1020) -\> K+ mu-]cc' ]                                                                                                                                                                                                                                                                                 |
| Output           | Phys/RareStrangePhiKMuLine/Particles                                                                                                                                                                                                                                                                               |

**AddRelatedInfo/RelatedInfo1_RareStrangePhiKMuLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangePhiKMuLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_RareStrangePhiKMuLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangePhiKMuLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangePhiKMuLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_RareStrangePhiKMuLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangePhiKMuLine**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangePhiKMuLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_RareStrangePhiKMuLine/Particles |
