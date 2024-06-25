[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingRareStrangeSigmaPEEDetLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaPEEDetLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT1           | None                                      |
| HLT2           | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

DiElectronMaker/RareStrangeDiElectronDetached

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/Charged' ]                   |
| DecayDescriptor | KS0                                          |
| Output          | Phys/RareStrangeDiElectronDetached/Particles |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r0p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

CombineParticles/RareStrangeSigmaPEEDetLine

|                  |                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/RareStrangeDiElectronDetached' , 'Phys/[StdLooseProtons](./stripping21r0p1-commonparticles-stdlooseprotons)' ]                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(MIPCHI2DV(PRIMARY)\>9)' , 'p+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05)' , 'p~-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05)' } |
| CombinationCut   | (ADAMASS('Sigma+')\<500.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 36.0) & (PT\> 500.0 \*MeV)& (ADMASS('Sigma+') \< 500.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 6.0 \* ps)                                 |
| DecayDescriptor  | [Sigma+ -\> p+ KS0]cc                                                                                                                                                                 |
| DecayDescriptors | [ '[Sigma+ -\> p+ KS0]cc' ]                                                                                                                                                         |
| Output           | Phys/RareStrangeSigmaPEEDetLine/Particles                                                                                                                                               |

AddRelatedInfo/RelatedInfo1_RareStrangeSigmaPEEDetLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPEEDetLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaPEEDetLine/Particles |

AddRelatedInfo/RelatedInfo2_RareStrangeSigmaPEEDetLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPEEDetLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaPEEDetLine/Particles |

AddRelatedInfo/RelatedInfo3_RareStrangeSigmaPEEDetLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPEEDetLine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaPEEDetLine/Particles |
