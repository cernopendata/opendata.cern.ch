[[stripping21 lines]](./stripping21-index)

# StrippingLb2V0hhLLLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Lb2V0hhLLLine/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingLb2V0hhLLLineVOIDFilter

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

FilterDesktop/Lambda0LLLbLines

|                 |                                                                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0')\<20.0\*MeV)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(VFASPF(VCHI2)\<15.0)&(CHILDCUT((TRGHOSTPROB\<0.5),1))&(CHILDCUT((TRGHOSTPROB\<0.5),2)) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)' ]                                                                                                      |
| DecayDescriptor | None                                                                                                                                                                                 |
| Output          | Phys/Lambda0LLLbLines/Particles                                                                                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)/Particles')\>0 |

CombineParticles/Lb2V0hhLLLine

|                  |                                                                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lambda0LLLbLines' , 'Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)' ]                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.5)' , 'pi-' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.5)' } |
| CombinationCut   | (APT\>1000.0\*MeV)&((APT1+APT2+APT3)\>3000.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(AM\>(5619-1319.0)\*MeV)&(AM\<(5619+600.0)\*MeV)&(ACUTDOCACHI2(5.0,''))   |
| MotherCut        | (PT\>800.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVDIRA\>0.995)&(MIPCHI2DV(PRIMARY)\<15.0)&(BPVVDCHI2\>30.0)&(VFASPF(VMINVDDV(PRIMARY))\>1.0)                   |
| DecayDescriptor  | None                                                                                                                                                    |
| DecayDescriptors | [ 'Lambda_b0 -\> pi+ pi- Lambda0' , 'Lambda_b~0 -\> pi+ pi- Lambda~0' ]                                                                               |
| Output           | Phys/Lb2V0hhLLLine/Particles                                                                                                                            |

AddRelatedInfo/RelatedInfo1_Lb2V0hhLLLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hhLLLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo1_Lb2V0hhLLLine/Particles |

AddRelatedInfo/RelatedInfo2_Lb2V0hhLLLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hhLLLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo2_Lb2V0hhLLLine/Particles |

AddRelatedInfo/RelatedInfo3_Lb2V0hhLLLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hhLLLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo3_Lb2V0hhLLLine/Particles |

AddRelatedInfo/RelatedInfo4_Lb2V0hhLLLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hhLLLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo4_Lb2V0hhLLLine/Particles |

AddRelatedInfo/RelatedInfo5_Lb2V0hhLLLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hhLLLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo5_Lb2V0hhLLLine/Particles |
