[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2TwoBaryonsB2PLambdabarLL_MVALine

## Properties:

|                |                                                   |
|----------------|---------------------------------------------------|
| OutputLocation | Phys/B2TwoBaryonsB2PLambdabarLL_MVALine/Particles |
| Postscale      | 1.0000000                                         |
| HLT            | None                                              |
| Prescale       | 1.0000000                                         |
| L0DU           | None                                              |
| ODIN           | None                                              |

## Filter sequence:

LoKi::VoidFilter/StrippingB2TwoBaryonsB2PLambdabarLL_MVALineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)/Particles')\>0 |

CombineParticles/B2TwoBaryonsB2PLambdabarLL_MVALine

|                  |                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)' , 'Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                                                        |
| CombinationCut   | (ADAMASS('B-')\<500\*MeV)&(ACUTDOCACHI2(5.0,''))&(APT1\>500.0\*MeV)                                                                                           |
| MotherCut        | VALUE('LoKi::Hybrid::DictValue/MVAResponse') \> 0.95                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                          |
| DecayDescriptors | [ 'B- -\> p~- Lambda0' , 'B+ -\> p+ Lambda~0' ]                                                                                                             |
| Output           | Phys/B2TwoBaryonsB2PLambdabarLL_MVALine/Particles                                                                                                             |

AddRelatedInfo/RelatedInfo1_B2TwoBaryonsB2PLambdabarLL_MVALine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLL_MVALine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo1_B2TwoBaryonsB2PLambdabarLL_MVALine/Particles |

AddRelatedInfo/RelatedInfo2_B2TwoBaryonsB2PLambdabarLL_MVALine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLL_MVALine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo2_B2TwoBaryonsB2PLambdabarLL_MVALine/Particles |

AddRelatedInfo/RelatedInfo3_B2TwoBaryonsB2PLambdabarLL_MVALine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLL_MVALine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo3_B2TwoBaryonsB2PLambdabarLL_MVALine/Particles |

AddRelatedInfo/RelatedInfo4_B2TwoBaryonsB2PLambdabarLL_MVALine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLL_MVALine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo4_B2TwoBaryonsB2PLambdabarLL_MVALine/Particles |

AddRelatedInfo/RelatedInfo5_B2TwoBaryonsB2PLambdabarLL_MVALine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLL_MVALine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo5_B2TwoBaryonsB2PLambdabarLL_MVALine/Particles |

AddRelatedInfo/RelatedInfo6_B2TwoBaryonsB2PLambdabarLL_MVALine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLL_MVALine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo6_B2TwoBaryonsB2PLambdabarLL_MVALine/Particles |
