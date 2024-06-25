[[stripping21 lines]](./stripping21-index)

# StrippingB2KShh_LL_2012a_OS_Line

## Properties:

|                |                                                                                                                                                                                            |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/B2KShh_MVAFilter_LL_2012a_OS/Particles                                                                                                                                                |
| Postscale      | 1.0000000                                                                                                                                                                                  |
| HLT            | (HLT_PASS_RE('Hlt1TrackAllL0Decision') & HLT_PASS_RE('Hlt2Topo[234]Body.\*Decision')) & ((in_range( 0x007E003A, HLT_TCK, 0x0097003D )) \| (in_range( 0x407E003A, HLT_TCK, 0x4097003D ))) |
| Prescale       | 1.0000000                                                                                                                                                                                  |
| L0DU           | None                                                                                                                                                                                       |
| ODIN           | None                                                                                                                                                                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingB2KShh_LL_2012a_OS_LineVOIDFilter

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

FilterDesktop/KSforB2KShhLL

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0')\<20.0\*MeV)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(CHILDCUT((TRGHOSTPROB\<0.3),1))&(CHILDCUT((TRGHOSTPROB\<0.3),2))&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>80.0) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ]                                                                                                                            |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/KSforB2KShhLL/Particles                                                                                                                                                                       |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/B2KShh_LL_2012a_OS_Line

|                  |                                                                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KSforB2KShhLL' , 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.3)' , 'pi-' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.3)' }                                                            |
| CombinationCut   | ((APT1+APT2+APT3)\>3000.0\*MeV)&(AM\>(5279-1279.0)\*MeV)&(AM\<(5279+921.0)\*MeV)&(ACUTDOCACHI2(5.0,''))&(APT\>1000.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(AVAL_MAX(MIPDV(PRIMARY),PT)\>0.05) |
| MotherCut        | (BPVDIRA\>0.999)&((CHILD(VFASPF(VZ),3) - VFASPF(VZ)) \> 15.0\*mm)                                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                                      |
| DecayDescriptors | [ 'B0 -\> pi+ pi- KS0' ]                                                                                                                                                                |
| Output           | Phys/B2KShh_LL_2012a_OS_Line/Particles                                                                                                                                                    |

AddRelatedInfo/RelatedInfo1_B2KShh_LL_2012a_OS_Line

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_LL_2012a_OS_Line' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo1_B2KShh_LL_2012a_OS_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2KShh_LL_2012a_OS_Line

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_LL_2012a_OS_Line' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo2_B2KShh_LL_2012a_OS_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2KShh_LL_2012a_OS_Line

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_LL_2012a_OS_Line' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo3_B2KShh_LL_2012a_OS_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2KShh_LL_2012a_OS_Line

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_LL_2012a_OS_Line' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo4_B2KShh_LL_2012a_OS_Line/Particles |

FilterDesktop/B2KShh_MVAFilter_LL_2012a_OS

|                 |                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VALUE('LoKi::Hybrid::DictValue/MVA1Response_LL_2012a_OS')\>-0.2) \| (VALUE('LoKi::Hybrid::DictValue/MVA2Response_LL_2012a_OS')\>-0.2) |
| Inputs          | [ 'Phys/B2KShh_LL_2012a_OS_Line' ]                                                                                                   |
| DecayDescriptor | None                                                                                                                                   |
| Output          | Phys/B2KShh_MVAFilter_LL_2012a_OS/Particles                                                                                            |

AddRelatedInfo/RelatedInfo1_B2KShh_MVAFilter_LL_2012a_OS

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_MVAFilter_LL_2012a_OS' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo1_B2KShh_MVAFilter_LL_2012a_OS/Particles |

AddRelatedInfo/RelatedInfo2_B2KShh_MVAFilter_LL_2012a_OS

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_MVAFilter_LL_2012a_OS' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo2_B2KShh_MVAFilter_LL_2012a_OS/Particles |

AddRelatedInfo/RelatedInfo3_B2KShh_MVAFilter_LL_2012a_OS

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_MVAFilter_LL_2012a_OS' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo3_B2KShh_MVAFilter_LL_2012a_OS/Particles |

AddRelatedInfo/RelatedInfo4_B2KShh_MVAFilter_LL_2012a_OS

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_MVAFilter_LL_2012a_OS' ]                |
| DecayDescriptor | None                                                     |
| Output          | Phys/RelatedInfo4_B2KShh_MVAFilter_LL_2012a_OS/Particles |
