[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingRareStrangeKPiMuMuLFVLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/RareStrangeKPiMuMuLFVLine/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

**LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles**

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLoosePions](./stripping21r0p1-stdallloosepions) /Particles',True)\>0 |

**CombineParticles/RareStrangeKPiMuMuLFVLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r0p1-stdallloosemuons) ' , 'Phys/ [StdAllLoosePions](./stripping21r0p1-stdallloosepions) ' ]                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(P\>3000) & (TRCHI2DOF\<3.0) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'mu-' : '(P\>3000) & (TRCHI2DOF\<3.0) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'pi+' : '(P\>1000) & (TRCHI2DOF\<3.0) & (TRGHOSTPROB \< 0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'pi-' : '(P\>1000) & (TRCHI2DOF\<3.0) & (TRGHOSTPROB \< 0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' } |
| CombinationCut   | (ADAMASS('K+') \< 100.0 \*MeV) & (AMAXDOCA('')\< 3.0 \*mm)                                                                                                                                                                                                                                                                                                                                 |
| MotherCut        | (PT\> 100.0) & (ADMASS('K+') \< 100.0 \*MeV) & ((BPVDIRA \> 0.98))& (VFASPF(VCHI2) \< 25.0) & (BPVVDCHI2 \> 36.0) & (BPVIPCHI2()\< 25.0 )                                                                                                                                                                                                                                                  |
| DecayDescriptor  | [K+ -\> pi- mu+ mu+]cc                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[K+ -\> pi- mu+ mu+]cc' ]                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/RareStrangeKPiMuMuLFVLine/Particles                                                                                                                                                                                                                                                                                                                                                   |

**AddRelatedInfo/RelatedInfo1_RareStrangeKPiMuMuLFVLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiMuMuLFVLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo1_RareStrangeKPiMuMuLFVLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeKPiMuMuLFVLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiMuMuLFVLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo2_RareStrangeKPiMuMuLFVLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeKPiMuMuLFVLine**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiMuMuLFVLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo3_RareStrangeKPiMuMuLFVLine/Particles |
