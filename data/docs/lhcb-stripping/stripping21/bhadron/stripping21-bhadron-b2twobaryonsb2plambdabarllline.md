[[stripping21 lines]](./stripping21-index)

# StrippingB2TwoBaryonsB2PLambdabarLLLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/B2TwoBaryonsB2PLambdabarLLLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT            | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

LoKi::VoidFilter/StrippingB2TwoBaryonsB2PLambdabarLLLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)/Particles')\>0 |

FilterDesktop/Lambda0LLBLines

|                 |                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0')\<15.0\*MeV)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>50.0) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)' ]                                                      |
| DecayDescriptor | None                                                                                                                                 |
| Output          | Phys/Lambda0LLBLines/Particles                                                                                                       |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)/Particles')\>0 |

CombineParticles/B2TwoBaryonsB2PLambdabarLLLine

|                  |                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lambda0LLBLines' , 'Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)' ]                                  |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'p+' : 'TRCHI2DOF\<3.0' , 'p~-' : 'TRCHI2DOF\<3.0' }                            |
| CombinationCut   | (APT\>1000.0\*MeV)&(APT1\>500.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(AM\>(5279-800.0)\*MeV)&(AM\<(5279+800.0)\*MeV)&(ACUTDOCACHI2(5.0,'')) |
| MotherCut        | (PT\>1500.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVDIRA\>0.995)&(MIPCHI2DV(PRIMARY)\<8.0)&(VFASPF(VMINVDDV(PRIMARY))\>1.0)&(BPVVDCHI2\>50.0)   |
| DecayDescriptor  | None                                                                                                                                    |
| DecayDescriptors | [ 'B- -\> p~- Lambda0' , 'B+ -\> p+ Lambda~0' ]                                                                                       |
| Output           | Phys/B2TwoBaryonsB2PLambdabarLLLine/Particles                                                                                           |

AddRelatedInfo/RelatedInfo1_B2TwoBaryonsB2PLambdabarLLLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLLLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo1_B2TwoBaryonsB2PLambdabarLLLine/Particles |

AddRelatedInfo/RelatedInfo2_B2TwoBaryonsB2PLambdabarLLLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLLLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo2_B2TwoBaryonsB2PLambdabarLLLine/Particles |

AddRelatedInfo/RelatedInfo3_B2TwoBaryonsB2PLambdabarLLLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLLLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo3_B2TwoBaryonsB2PLambdabarLLLine/Particles |

AddRelatedInfo/RelatedInfo4_B2TwoBaryonsB2PLambdabarLLLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLLLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo4_B2TwoBaryonsB2PLambdabarLLLine/Particles |

AddRelatedInfo/RelatedInfo5_B2TwoBaryonsB2PLambdabarLLLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLLLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo5_B2TwoBaryonsB2PLambdabarLLLine/Particles |

AddRelatedInfo/RelatedInfo6_B2TwoBaryonsB2PLambdabarLLLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarLLLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo6_B2TwoBaryonsB2PLambdabarLLLine/Particles |
