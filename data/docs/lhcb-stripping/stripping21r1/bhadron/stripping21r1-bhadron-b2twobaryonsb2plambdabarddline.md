[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2TwoBaryonsB2PLambdabarDDLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/B2TwoBaryonsB2PLambdabarDDLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT            | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

LoKi::VoidFilter/StrippingB2TwoBaryonsB2PLambdabarDDLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)/Particles')\>0 |

FilterDesktop/Lambda0DDBLines

|                 |                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>8000.0\*MeV)&(ADMASS('Lambda0')\<20.0\*MeV)&(VFASPF(VCHI2)\<12.0) &(VFASPF(VMINVDDV(PRIMARY))\>300.0)&(BPVVDCHI2\>50.0) |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21r1-commonparticles-stdlooselambdadd)' ]                                           |
| DecayDescriptor | None                                                                                                                        |
| Output          | Phys/Lambda0DDBLines/Particles                                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)/Particles')\>0 |

CombineParticles/B2TwoBaryonsB2PLambdabarDDLine

|                  |                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lambda0DDBLines' , 'Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)' ]                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'p+' : 'TRCHI2DOF\<3.0' , 'p~-' : 'TRCHI2DOF\<3.0' }                                                                |
| CombinationCut   | (APT\>1000.0\*MeV)&(APT1\>500.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(AM\>(5620-800.0)\*MeV)&(AM\<(5620+800.0)\*MeV)&(AVAL_MAX(MIPDV(PRIMARY),PT)\>0.05)&(ACUTDOCACHI2(5.0,'')) |
| MotherCut        | (PT\>1500.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVDIRA\>0.995)&(MIPCHI2DV(PRIMARY)\<8.0)&(VFASPF(VMINVDDV(PRIMARY))\>1.0)&(BPVVDCHI2\>50.0)                                       |
| DecayDescriptor  | None                                                                                                                                                                        |
| DecayDescriptors | [ 'B- -\> p~- Lambda0' , 'B+ -\> p+ Lambda~0' ]                                                                                                                           |
| Output           | Phys/B2TwoBaryonsB2PLambdabarDDLine/Particles                                                                                                                               |

AddRelatedInfo/RelatedInfo1_B2TwoBaryonsB2PLambdabarDDLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarDDLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo1_B2TwoBaryonsB2PLambdabarDDLine/Particles |

AddRelatedInfo/RelatedInfo2_B2TwoBaryonsB2PLambdabarDDLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarDDLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo2_B2TwoBaryonsB2PLambdabarDDLine/Particles |

AddRelatedInfo/RelatedInfo3_B2TwoBaryonsB2PLambdabarDDLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarDDLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo3_B2TwoBaryonsB2PLambdabarDDLine/Particles |

AddRelatedInfo/RelatedInfo4_B2TwoBaryonsB2PLambdabarDDLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarDDLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo4_B2TwoBaryonsB2PLambdabarDDLine/Particles |

AddRelatedInfo/RelatedInfo5_B2TwoBaryonsB2PLambdabarDDLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarDDLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo5_B2TwoBaryonsB2PLambdabarDDLine/Particles |

AddRelatedInfo/RelatedInfo6_B2TwoBaryonsB2PLambdabarDDLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PLambdabarDDLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo6_B2TwoBaryonsB2PLambdabarDDLine/Particles |
