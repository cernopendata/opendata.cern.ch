[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingRareStrangeLambdaPPiEELine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/RareStrangeLambdaPPiEELine/Particles |
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
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1p1-commonparticles-stdallloosepions)/Particles',True)\>0 |

CombineParticles/RareStrangeLambdaPPiEELine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/RareStrangeDiElectronDetached' , 'Phys/[StdAllLoosePions](./stripping21r1p1-commonparticles-stdallloosepions)' , 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : '(MIPCHI2DV(PRIMARY)\>9)' , 'p+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'pi+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'pi-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'p~-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp\> 0.05) & (MIPCHI2DV(PRIMARY)\>9.0)' } |
| CombinationCut   | (ADAMASS('Lambda0')\<500.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                                                                                                                                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 25.0) & (PT\> 500.0 \*MeV)& (ADMASS('Lambda0') \< 500.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 6.0 \* ps)                                                                                                                                                                                                                                                |
| DecayDescriptor  | [Lambda0 -\> p+ pi- KS0]cc                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[Lambda0 -\> p+ pi- KS0]cc' ]                                                                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/RareStrangeLambdaPPiEELine/Particles                                                                                                                                                                                                                                                                                                                                                               |

AddRelatedInfo/RelatedInfo1_RareStrangeLambdaPPiEELine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeLambdaPPiEELine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo1_RareStrangeLambdaPPiEELine/Particles |

AddRelatedInfo/RelatedInfo2_RareStrangeLambdaPPiEELine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeLambdaPPiEELine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo2_RareStrangeLambdaPPiEELine/Particles |

AddRelatedInfo/RelatedInfo3_RareStrangeLambdaPPiEELine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeLambdaPPiEELine' ]                |
| DecayDescriptor | None                                                   |
| Output          | Phys/RelatedInfo3_RareStrangeLambdaPPiEELine/Particles |
