[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingRareStrangeKPiMuMuDownLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/RareStrangeKPiMuMuDownLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT1           | None                                      |
| HLT2           | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

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

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownPions_Particles**

|      |                                                                                                 |
|------|-------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsDownPions](./stripping21r1p1-stdnopidsdownpions) /Particles',True)\>0 |

**CombineParticles/RareStrangeKPiMuMuDownLine**

|                  |                                                                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseDownMuons](./stripping21r1p1-stdloosedownmuons) ' , 'Phys/ [StdNoPIDsDownPions](./stripping21r1p1-stdnopidsdownpions) ' ]                                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF\<3.0) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>5.0)' , 'mu-' : '(TRCHI2DOF\<3.0) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>5.0)' , 'pi+' : '(TRCHI2DOF\<3.0) & (TRGHOSTPROB \< 0.3) & (MIPCHI2DV(PRIMARY)\>5.0)' , 'pi-' : '(TRCHI2DOF\<3.0) & (TRGHOSTPROB \< 0.3) & (MIPCHI2DV(PRIMARY)\>5.0)' } |
| CombinationCut   | (ADAMASS('K+') \< 100.0 \*MeV) & (AMAXDOCA('')\< 10.0 \*mm)                                                                                                                                                                                                                                                                                |
| MotherCut        | (PT\> 0.0) & (ADMASS('K+') \< 100.0 \*MeV) & (BPVDIRA \> 0.98)& (VFASPF(VCHI2) \< 25.0) & (BPVVDCHI2 \> 49.0) & (BPVVDZ \> 500.0\*mm) & (BPVVDZ \< 2500.0\*mm)                                                                                                                                                                             |
| DecayDescriptor  | [K+ -\> pi+ mu+ mu-]cc                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[K+ -\> pi+ mu+ mu-]cc' ]                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/RareStrangeKPiMuMuDownLine/Particles                                                                                                                                                                                                                                                                                                  |

**AddRelatedInfo/RelatedInfo1_RareStrangeKPiMuMuDownLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiMuMuDownLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_RareStrangeKPiMuMuDownLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeKPiMuMuDownLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiMuMuDownLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo2_RareStrangeKPiMuMuDownLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeKPiMuMuDownLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiMuMuDownLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo3_RareStrangeKPiMuMuDownLine/Particles |
