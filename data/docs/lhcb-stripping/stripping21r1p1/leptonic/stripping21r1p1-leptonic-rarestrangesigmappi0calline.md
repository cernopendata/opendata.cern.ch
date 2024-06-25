[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingRareStrangeSigmaPPi0CalLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaPPi0CalLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

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

GaudiSequencer/SeqPi0ForRareStrangeSigmaPPi0Cal

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1p1-commonparticles-stdloosemergedpi0)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

FilterDesktop/Pi0ForRareStrangeSigmaPPi0Cal

|                 |                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1p1-commonparticles-stdloosemergedpi0)' , 'Phys/[StdLooseResolvedPi0](./stripping21r1p1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                                                                                                        |
| Output          | Phys/Pi0ForRareStrangeSigmaPPi0Cal/Particles                                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

CombineParticles/RareStrangeSigmaPPi0CalLine

|                  |                                                                                                                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0ForRareStrangeSigmaPPi0Cal' , 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ]                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT \> 500.0) & (TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp \> 0.5 )' , 'pi0' : '(PT \> 700.0)' , 'p~-' : '(PT \> 500.0) & (TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp \> 0.5 )' } |
| CombinationCut   | (ADAMASS('Sigma+')\<150.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 36.0) & (PT\> 500.0 \*MeV)& (ADMASS('Sigma+') \< 150.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 6.0 \* ps)                                                         |
| DecayDescriptor  | [Sigma+ -\> p+ pi0]cc                                                                                                                                                                                         |
| DecayDescriptors | [ '[Sigma+ -\> p+ pi0]cc' ]                                                                                                                                                                                 |
| Output           | Phys/RareStrangeSigmaPPi0CalLine/Particles                                                                                                                                                                      |

AddRelatedInfo/RelatedInfo1_RareStrangeSigmaPPi0CalLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPPi0CalLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaPPi0CalLine/Particles |

AddRelatedInfo/RelatedInfo2_RareStrangeSigmaPPi0CalLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPPi0CalLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaPPi0CalLine/Particles |

AddRelatedInfo/RelatedInfo3_RareStrangeSigmaPPi0CalLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPPi0CalLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaPPi0CalLine/Particles |
