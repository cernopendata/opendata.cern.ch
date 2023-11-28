[[stripping21 lines]](./stripping21-index)

# StrippingHb2V0V0h_KSLzhLD_Line

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/Hb2V0V0h_KSLzhLD_Line/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

LoKi::VoidFilter/StrippingHb2V0V0h_KSLzhLD_LineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/V0forHb2V0V0hKSLL

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0')\<20.0\*MeV)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(CHILDCUT((TRGHOSTPROB\<0.3),1))&(CHILDCUT((TRGHOSTPROB\<0.3),2))&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>80.0) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ]                                                                                                                            |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/V0forHb2V0V0hKSLL/Particles                                                                                                                                                                   |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)/Particles')\>0 |

FilterDesktop/V0forHb2V0V0hLzDD

|                 |                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('Lambda0')\<30.0\*MeV)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>50.0) |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)' ]                                                      |
| DecayDescriptor | None                                                                                                                                 |
| Output          | Phys/V0forHb2V0V0hLzDD/Particles                                                                                                     |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/Hb2V0V0h_KSLzhLD_Line

|                  |                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' , 'Phys/V0forHb2V0V0hKSLL' , 'Phys/V0forHb2V0V0hLzDD' ]                                 |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.3)' , 'pi-' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.3)' } |
| CombinationCut   | (AM\>(5279-1279.0)\*MeV)&(AM\<(5279+921.0)\*MeV)&(APT\>1000.0\*MeV)                                                                                                     |
| MotherCut        | (BPVDIRA\>0.999)&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>50.0)&(MIPCHI2DV(PRIMARY)\<12.0)& (CHILDCUT(CHILDCUT(ISLONG, 2), 1)) & (CHILDCUT(CHILDCUT(ISDOWN, 2), 2))            |
| DecayDescriptor  | None                                                                                                                                                                    |
| DecayDescriptors | [ 'Xi_b- -\> KS0 Lambda0 pi-' ]                                                                                                                                       |
| Output           | Phys/Hb2V0V0h_KSLzhLD_Line/Particles                                                                                                                                    |

AddRelatedInfo/RelatedInfo1_Hb2V0V0h_KSLzhLD_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Hb2V0V0h_KSLzhLD_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_Hb2V0V0h_KSLzhLD_Line/Particles |

AddRelatedInfo/RelatedInfo2_Hb2V0V0h_KSLzhLD_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Hb2V0V0h_KSLzhLD_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_Hb2V0V0h_KSLzhLD_Line/Particles |

AddRelatedInfo/RelatedInfo3_Hb2V0V0h_KSLzhLD_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Hb2V0V0h_KSLzhLD_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_Hb2V0V0h_KSLzhLD_Line/Particles |

AddRelatedInfo/RelatedInfo4_Hb2V0V0h_KSLzhLD_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Hb2V0V0h_KSLzhLD_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo4_Hb2V0V0h_KSLzhLD_Line/Particles |
