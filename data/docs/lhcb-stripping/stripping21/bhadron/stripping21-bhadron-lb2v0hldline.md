[[stripping21 lines]](./stripping21-index)

# StrippingLb2V0hLDLine

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/Lb2V0hLDLine/Particles |
| Postscale      | 1.0000000                   |
| HLT            | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

## Filter sequence:

LoKi::VoidFilter/StrippingLb2V0hLDLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLD_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLD](./stripping21-commonparticles-stdlooselambdald)/Particles')\>0 |

FilterDesktop/Lambda0LDLbLines

|                 |                                                                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P\>5000.0\*MeV)&(ADMASS('Lambda0')\<25.0\*MeV)&(VFASPF(VCHI2)\<15.0) &(BPVVDCHI2\>50.0)&(CHILDCUT((TRGHOSTPROB\<0.5),1))&(CHILDCUT((TRGHOSTPROB\<0.5),2)) |
| Inputs          | [ 'Phys/[StdLooseLambdaLD](./stripping21-commonparticles-stdlooselambdald)' ]                                                                            |
| DecayDescriptor | None                                                                                                                                                       |
| Output          | Phys/Lambda0LDLbLines/Particles                                                                                                                            |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)/Particles')\>0 |

CombineParticles/Lb2V0hLDLine

|                  |                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lambda0LDLbLines' , 'Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)' ]                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : 'TRCHI2DOF\<3.0' , 'pi-' : 'TRCHI2DOF\<3.0' }                                                               |
| CombinationCut   | (APT\>1000.0\*MeV)&(APT1\>500.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(AM\>(5619-800.0)\*MeV)&(AM\<(5619+800.0)\*MeV)&(AVAL_MAX(MIPDV(PRIMARY),PT)\>0.05)&(ACUTDOCACHI2(5.0,'')) |
| MotherCut        | (PT\>800.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVDIRA\>0.995)&(MIPCHI2DV(PRIMARY)\<15.0)&(VFASPF(VMINVDDV(PRIMARY))\>1.0)&(BPVVDCHI2\>30.0)                                       |
| DecayDescriptor  | None                                                                                                                                                                        |
| DecayDescriptors | [ 'Lambda_b0 -\> pi- Lambda0' , 'Lambda_b~0 -\> pi+ Lambda~0' ]                                                                                                           |
| Output           | Phys/Lb2V0hLDLine/Particles                                                                                                                                                 |

AddRelatedInfo/RelatedInfo1_Lb2V0hLDLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hLDLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo1_Lb2V0hLDLine/Particles |

AddRelatedInfo/RelatedInfo2_Lb2V0hLDLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hLDLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo2_Lb2V0hLDLine/Particles |

AddRelatedInfo/RelatedInfo3_Lb2V0hLDLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hLDLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo3_Lb2V0hLDLine/Particles |

AddRelatedInfo/RelatedInfo4_Lb2V0hLDLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hLDLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo4_Lb2V0hLDLine/Particles |

AddRelatedInfo/RelatedInfo5_Lb2V0hLDLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hLDLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo5_Lb2V0hLDLine/Particles |
