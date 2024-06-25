[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2KShh_DD_2011_SS_Line

## Properties:

|                |                                                                                                                                                                                            |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/B2KShh_MVAFilter_DD_2011_SS/Particles                                                                                                                                                 |
| Postscale      | 1.0000000                                                                                                                                                                                  |
| HLT            | (HLT_PASS_RE('Hlt1TrackAllL0Decision') & HLT_PASS_RE('Hlt2Topo[234]Body.\*Decision')) & ((in_range( 0x00470032, HLT_TCK, 0x00790038 )) \| (in_range( 0x40470032, HLT_TCK, 0x40790038 ))) |
| Prescale       | 1.0000000                                                                                                                                                                                  |
| L0DU           | None                                                                                                                                                                                       |
| ODIN           | None                                                                                                                                                                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingB2KShh_DD_2011_SS_LineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/KSforB2KShhDD

|                 |                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0')\<30.0\*MeV)&(P\>6000.0\*MeV)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>50.0) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)' ]                                                                         |
| DecayDescriptor | None                                                                                                                                              |
| Output          | Phys/KSforB2KShhDD/Particles                                                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/B2KShh_DD_2011_SS_Line

|                  |                                                                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KSforB2KShhDD' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.3)' , 'pi-' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.3)' }                                                            |
| CombinationCut   | ((APT1+APT2+APT3)\>4200.0\*MeV)&(AM\>(5279-1279.0)\*MeV)&(AM\<(5279+921.0)\*MeV)&(ACUTDOCACHI2(5.0,''))&(APT\>1000.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(AVAL_MAX(MIPDV(PRIMARY),PT)\>0.05) |
| MotherCut        | (BPVDIRA\>0.999)&((CHILD(VFASPF(VZ),3) - VFASPF(VZ)) \> 15.0\*mm)                                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                                      |
| DecayDescriptors | [ 'B0 -\> pi+ pi+ KS0' , 'B0 -\> pi- pi- KS0' ]                                                                                                                                         |
| Output           | Phys/B2KShh_DD_2011_SS_Line/Particles                                                                                                                                                     |

AddRelatedInfo/RelatedInfo1_B2KShh_DD_2011_SS_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_DD_2011_SS_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_B2KShh_DD_2011_SS_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2KShh_DD_2011_SS_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_DD_2011_SS_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_B2KShh_DD_2011_SS_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2KShh_DD_2011_SS_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_DD_2011_SS_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_B2KShh_DD_2011_SS_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2KShh_DD_2011_SS_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_DD_2011_SS_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_B2KShh_DD_2011_SS_Line/Particles |

FilterDesktop/B2KShh_MVAFilter_DD_2011_SS

|                 |                                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VALUE('LoKi::Hybrid::DictValue/MVA1Response_DD_2011_SS')\>-0.2) \| (VALUE('LoKi::Hybrid::DictValue/MVA2Response_DD_2011_SS')\>-0.2) |
| Inputs          | [ 'Phys/B2KShh_DD_2011_SS_Line' ]                                                                                                  |
| DecayDescriptor | None                                                                                                                                 |
| Output          | Phys/B2KShh_MVAFilter_DD_2011_SS/Particles                                                                                           |

AddRelatedInfo/RelatedInfo1_B2KShh_MVAFilter_DD_2011_SS

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_MVAFilter_DD_2011_SS' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo1_B2KShh_MVAFilter_DD_2011_SS/Particles |

AddRelatedInfo/RelatedInfo2_B2KShh_MVAFilter_DD_2011_SS

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_MVAFilter_DD_2011_SS' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo2_B2KShh_MVAFilter_DD_2011_SS/Particles |

AddRelatedInfo/RelatedInfo3_B2KShh_MVAFilter_DD_2011_SS

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_MVAFilter_DD_2011_SS' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo3_B2KShh_MVAFilter_DD_2011_SS/Particles |

AddRelatedInfo/RelatedInfo4_B2KShh_MVAFilter_DD_2011_SS

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_MVAFilter_DD_2011_SS' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo4_B2KShh_MVAFilter_DD_2011_SS/Particles |
