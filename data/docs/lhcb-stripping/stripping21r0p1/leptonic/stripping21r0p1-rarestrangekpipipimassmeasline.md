[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingRareStrangeKPiPiPiMassMeasLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/RareStrangeKPiPiPiMassMeasLine/Particles |
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

**LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles**

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLoosePions](./stripping21r0p1-stdallloosepions) /Particles',True)\>0 |

**CombineParticles/RareStrangeKPiPiPiMassMeasLine**

|                  |                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLoosePions](./stripping21r0p1-stdallloosepions) ' ]                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(P\>1000) & (MIPCHI2DV(PRIMARY) \> 25.0) & (TRCHI2DOF\<5) & (TRGHOSTPROB \< 0.4)' , 'pi-' : '(P\>1000) & (MIPCHI2DV(PRIMARY) \> 25.0) & (TRCHI2DOF\<5) & (TRGHOSTPROB \< 0.4)' } |
| CombinationCut   | (ADAMASS('K+') \< 50.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                                                |
| MotherCut        | (PT\> 300.0) & (ADMASS('K+') \< 50.0 \*MeV) & (BPVDIRA \> 0.9998)& (VFASPF(VCHI2) \< 10.0) & (BPVVDCHI2 \> 100.0) & (BPVIPCHI2()\< 25.0 )                                                                |
| DecayDescriptor  | [K+ -\> pi+ pi+ pi-]cc                                                                                                                                                                                 |
| DecayDescriptors | [ '[K+ -\> pi+ pi+ pi-]cc' ]                                                                                                                                                                         |
| Output           | Phys/RareStrangeKPiPiPiMassMeasLine/Particles                                                                                                                                                            |

**AddRelatedInfo/RelatedInfo1_RareStrangeKPiPiPiMassMeasLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiMassMeasLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo1_RareStrangeKPiPiPiMassMeasLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeKPiPiPiMassMeasLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiMassMeasLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo2_RareStrangeKPiPiPiMassMeasLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeKPiPiPiMassMeasLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiMassMeasLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo3_RareStrangeKPiPiPiMassMeasLine/Particles |
