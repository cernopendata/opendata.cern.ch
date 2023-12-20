[[stripping21 lines]](./stripping21-index)

# StrippingHb2V0V0h_KSKSLzDDL_Line

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/Hb2V0V0h_KSKSLzDDL_Line/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingHb2V0V0h_KSKSLzDDL_LineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/V0forHb2V0V0hKSDD

|                 |                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0')\<30.0\*MeV)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>50.0) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' ]                                                          |
| DecayDescriptor | None                                                                                                                             |
| Output          | Phys/V0forHb2V0V0hKSDD/Particles                                                                                                 |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)/Particles')\>0 |

FilterDesktop/V0forHb2V0V0hLzLL

|                 |                                                                                                                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0')\<20.0\*MeV)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(CHILDCUT((TRGHOSTPROB\<0.3),1))&(CHILDCUT((TRGHOSTPROB\<0.3),2))&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>80.0) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21-commonparticles-stdlooselambdall)' ]                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                   |
| Output          | Phys/V0forHb2V0V0hLzLL/Particles                                                                                                                                                                       |

CombineParticles/Hb2V0V0h_KSKSLzDDL_Line

|                  |                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/V0forHb2V0V0hKSDD' , 'Phys/V0forHb2V0V0hLzLL' ]                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' }                                                                                                     |
| CombinationCut   | (AM\>(5279-1279.0)\*MeV)&(AM\<(5279+921.0)\*MeV)&(APT\>1000.0\*MeV)                                                                                                         |
| MotherCut        | (BPVDIRA\>0.999)&(BPVVDCHI2\>50.0)&(MIPCHI2DV(PRIMARY)\<12.0)& (CHILDCUT(CHILDCUT(ISDOWN, 2), 1)) & (CHILDCUT(CHILDCUT(ISDOWN, 2), 2)) & (CHILDCUT(CHILDCUT(ISLONG, 2), 3)) |
| DecayDescriptor  | None                                                                                                                                                                        |
| DecayDescriptors | [ 'Lambda_b0 -\> KS0 KS0 Lambda0' ]                                                                                                                                       |
| Output           | Phys/Hb2V0V0h_KSKSLzDDL_Line/Particles                                                                                                                                      |

AddRelatedInfo/RelatedInfo1_Hb2V0V0h_KSKSLzDDL_Line

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Hb2V0V0h_KSKSLzDDL_Line' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo1_Hb2V0V0h_KSKSLzDDL_Line/Particles |

AddRelatedInfo/RelatedInfo2_Hb2V0V0h_KSKSLzDDL_Line

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Hb2V0V0h_KSKSLzDDL_Line' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo2_Hb2V0V0h_KSKSLzDDL_Line/Particles |

AddRelatedInfo/RelatedInfo3_Hb2V0V0h_KSKSLzDDL_Line

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Hb2V0V0h_KSKSLzDDL_Line' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo3_Hb2V0V0h_KSKSLzDDL_Line/Particles |

AddRelatedInfo/RelatedInfo4_Hb2V0V0h_KSKSLzDDL_Line

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/Hb2V0V0h_KSKSLzDDL_Line' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo4_Hb2V0V0h_KSKSLzDDL_Line/Particles |
