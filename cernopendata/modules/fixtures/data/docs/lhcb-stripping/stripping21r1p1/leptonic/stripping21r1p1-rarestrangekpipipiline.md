[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingRareStrangeKPiPiPiLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/RareStrangeKPiPiPiLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 0.010000000                           |
| L0DU           | None                                  |
| ODIN           | None                                  |

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
| Code | CONTAINS('Phys/ [StdAllLoosePions](./stripping21r1p1-stdallloosepions) /Particles',True)\>0 |

**CombineParticles/RareStrangeKPiPiPiLine**

|                  |                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLoosePions](./stripping21r1p1-stdallloosepions) ' ]                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(P\>1000) & (TRCHI2DOF\<3.0) & (TRGHOSTPROB \< 0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'pi-' : '(P\>1000) & (TRCHI2DOF\<3.0) & (TRGHOSTPROB \< 0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' } |
| CombinationCut   | (ADAMASS('K+') \< 100.0 \*MeV) & (AMAXDOCA('')\< 3.0 \*mm)                                                                                                                                             |
| MotherCut        | (PT\> 100.0) & (ADMASS('K+') \< 100.0 \*MeV) & (BPVDIRA \> 0.98)& (VFASPF(VCHI2) \< 25.0) & (BPVVDCHI2 \> 36.0) & (BPVIPCHI2()\< 25.0 )                                                                |
| DecayDescriptor  | [K+ -\> pi+ pi+ pi-]cc                                                                                                                                                                               |
| DecayDescriptors | [ '[K+ -\> pi+ pi+ pi-]cc' ]                                                                                                                                                                       |
| Output           | Phys/RareStrangeKPiPiPiLine/Particles                                                                                                                                                                  |

**AddRelatedInfo/RelatedInfo1_RareStrangeKPiPiPiLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_RareStrangeKPiPiPiLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeKPiPiPiLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_RareStrangeKPiPiPiLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeKPiPiPiLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_RareStrangeKPiPiPiLine/Particles |
