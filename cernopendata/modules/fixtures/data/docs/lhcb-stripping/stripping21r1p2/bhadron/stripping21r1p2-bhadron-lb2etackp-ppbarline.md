[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLb2EtacKp_PPbarLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/Lb2EtacKp_PPbarLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

FilterDesktop/Lb2EtacKpSelProtons

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (PROBNNp \> 0.1) & (PT \> 300\*MeV) & (P \> 10\*GeV) & (TRGHOSTPROB\<0.4)         |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p2-commonparticles-stdlooseprotons)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/Lb2EtacKpSelProtons/Particles                                                |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/Lb2EtacKpSelKaons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4)                      |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Lb2EtacKpSelKaons/Particles                                              |

CombineParticles/Lb2EtacKpSelLambdaS

|                  |                                                                                          |
|------------------|------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelKaons' , 'Phys/Lb2EtacKpSelProtons' ]                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }              |
| CombinationCut   | (ACHILD(PT,1)+ACHILD(PT,2) \> 900.\*MeV) & (AM \< 4.0 \*GeV) & (ADOCACHI2CUT(20., ''))   |
| MotherCut        | (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2 \> 10.) & (VFASPF(VCHI2) \< 9.) & (BPVDIRA\>0.9) |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K-]cc                                                            |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K-]cc' ]                                                    |
| Output           | Phys/Lb2EtacKpSelLambdaS/Particles                                                       |

CombineParticles/Lb2EtacKpSelEtac2PPbar

|                  |                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelProtons' ]                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                                                                   |
| CombinationCut   | (in_range(2.65\*GeV, AM, 3.35\*GeV))                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.7\*GeV, MM, 3.3\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>10) & (BPVDIRA\>0.9) |
| DecayDescriptor  | eta_c(1S) -\> p+ p~-                                                                                                            |
| DecayDescriptors | [ 'eta_c(1S) -\> p+ p~-' ]                                                                                                    |
| Output           | Phys/Lb2EtacKpSelEtac2PPbar/Particles                                                                                           |

CombineParticles/Lb2EtacKp_PPbarLine

|                  |                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelEtac2PPbar' , 'Phys/Lb2EtacKpSelLambdaS' ]                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'eta_c(1S)' : 'ALL' }                                         |
| CombinationCut   | (ADAMASS('Lambda_b0') \< 500 \*MeV)                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10.) & (BPVDIRA\> 0.9999) & (BPVIPCHI2()\<25) & (BPVVDCHI2\>250) & (BPVVDRHO\>0.1\*mm) & (BPVVDZ\>2.0\*mm) |
| DecayDescriptor  | [Lambda_b0 -\> eta_c(1S) Lambda(1520)0]cc                                                                                       |
| DecayDescriptors | [ '[Lambda_b0 -\> eta_c(1S) Lambda(1520)0]cc' ]                                                                               |
| Output           | Phys/Lb2EtacKp_PPbarLine/Particles                                                                                                |

AddRelatedInfo/RelatedInfo1_Lb2EtacKp_PPbarLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKp_PPbarLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo1_Lb2EtacKp_PPbarLine/Particles |

AddRelatedInfo/RelatedInfo2_Lb2EtacKp_PPbarLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKp_PPbarLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo2_Lb2EtacKp_PPbarLine/Particles |

AddRelatedInfo/RelatedInfo3_Lb2EtacKp_PPbarLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKp_PPbarLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo3_Lb2EtacKp_PPbarLine/Particles |

AddRelatedInfo/RelatedInfo4_Lb2EtacKp_PPbarLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKp_PPbarLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo4_Lb2EtacKp_PPbarLine/Particles |

AddRelatedInfo/RelatedInfo5_Lb2EtacKp_PPbarLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKp_PPbarLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo5_Lb2EtacKp_PPbarLine/Particles |
