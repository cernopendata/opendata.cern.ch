[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingLb2EtacKp_KsKPiLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/Lb2EtacKp_KsKPiLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelProtons

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB\<0.4)                         |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1p1-commonparticles-stdlooseprotons)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/Lb2EtacKpSelProtons/Particles                                                |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelKaons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4)                      |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p1-commonparticles-stdloosekaons)' ] |
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

GaudiSequencer/SeqLb2EtacKpInputKs

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpInputKs

|                 |                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                 |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLL](./stripping21r1p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                                                                                                |
| Output          | Phys/Lb2EtacKpInputKs/Particles                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Lb2EtacKpSelKs

|                 |                                           |
|-----------------|-------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.\*MeV) & (BPVDLS\>5) |
| Inputs          | [ 'Phys/Lb2EtacKpInputKs' ]             |
| DecayDescriptor | None                                      |
| Output          | Phys/Lb2EtacKpSelKs/Particles             |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/Lb2EtacKpSelPions

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB\<0.4)                     |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Lb2EtacKpSelPions/Particles                                              |

CombineParticles/Lb2EtacKpSelEtac2KsKPi

|                  |                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelKaons' , 'Phys/Lb2EtacKpSelKs' , 'Phys/Lb2EtacKpSelPions' ]                                               |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                    |
| CombinationCut   | (in_range(2.75\*GeV, AM, 3.25\*GeV))                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.8\*GeV, MM, 3.2\*GeV)) & (MIPCHI2DV(PRIMARY) \> 0.) & (BPVVDCHI2\>10) & (BPVDIRA\>0.9) |
| DecayDescriptor  | [eta_c(1S) -\> KS0 K+ pi-]cc                                                                                                  |
| DecayDescriptors | [ '[eta_c(1S) -\> KS0 K+ pi-]cc' ]                                                                                          |
| Output           | Phys/Lb2EtacKpSelEtac2KsKPi/Particles                                                                                           |

CombineParticles/Lb2EtacKp_KsKPiLine

|                  |                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2EtacKpSelEtac2KsKPi' , 'Phys/Lb2EtacKpSelLambdaS' ]                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' , 'eta_c(1S)' : 'ALL' }                                         |
| CombinationCut   | (ADAMASS('Lambda_b0') \< 500 \*MeV)                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10.) & (BPVDIRA\> 0.9999) & (BPVIPCHI2()\<25) & (BPVVDCHI2\>250) & (BPVVDRHO\>0.1\*mm) & (BPVVDZ\>2.0\*mm) |
| DecayDescriptor  | [Lambda_b0 -\> eta_c(1S) Lambda(1520)0]cc                                                                                       |
| DecayDescriptors | [ '[Lambda_b0 -\> eta_c(1S) Lambda(1520)0]cc' ]                                                                               |
| Output           | Phys/Lb2EtacKp_KsKPiLine/Particles                                                                                                |

AddRelatedInfo/RelatedInfo1_Lb2EtacKp_KsKPiLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKp_KsKPiLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo1_Lb2EtacKp_KsKPiLine/Particles |

AddRelatedInfo/RelatedInfo2_Lb2EtacKp_KsKPiLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKp_KsKPiLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo2_Lb2EtacKp_KsKPiLine/Particles |

AddRelatedInfo/RelatedInfo3_Lb2EtacKp_KsKPiLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKp_KsKPiLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo3_Lb2EtacKp_KsKPiLine/Particles |

AddRelatedInfo/RelatedInfo4_Lb2EtacKp_KsKPiLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKp_KsKPiLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo4_Lb2EtacKp_KsKPiLine/Particles |

AddRelatedInfo/RelatedInfo5_Lb2EtacKp_KsKPiLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Lb2EtacKp_KsKPiLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo5_Lb2EtacKp_KsKPiLine/Particles |
