[[stripping21 lines]](./stripping21-index)

# StrippingB2D0KD2KSHHLLBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/B2D0KD2KSHHLLBeauty2CharmLine/Particles                                 |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB2D0KD2KSHHLLBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]             |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                      |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                           |

CombineParticles/ProtoD2KSHHLLBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_LLInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                          |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('KS0','pi+','pi-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('KS0','pi+','K-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('KS0','K+','pi-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('KS0','K+','K-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'D0 -\> KS0 pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/ProtoD2KSHHLLBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                |

SubPIDMMFilter/D2KsHHSubPIDSelBeauty2CharmLL

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                     |
| Inputs          | [ 'Phys/ProtoD2KSHHLLBeauty2Charm' ]                                                                                  |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/D2KsHHSubPIDSelBeauty2CharmLL/Particles                                                                            |
| MaxMM           | 1964.8400                                                                                                               |
| MinMM           | 1764.8400                                                                                                               |
| PIDs            | [ [ 'KS0' , 'pi+' , 'pi-' ] , [ 'KS0' , 'pi+' , 'K-' ] , [ 'KS0' , 'K+' , 'pi-' ] , [ 'KS0' , 'K+' , 'K-' ] ] |

FilterDesktop/D2KsHHLLBeauty2CharmFilter

|                 |                                            |
|-----------------|--------------------------------------------|
| Code            | in_range(1764.84,MM,1964.84)               |
| Inputs          | [ 'Phys/D2KsHHSubPIDSelBeauty2CharmLL' ] |
| DecayDescriptor | None                                       |
| Output          | Phys/D2KsHHLLBeauty2CharmFilter/Particles  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' ]             |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

FilterDesktop/KTopoInputsBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/KInputsBeauty2CharmFilter' ]                            |
| DecayDescriptor | None                                                              |
| Output          | Phys/KTopoInputsBeauty2CharmFilter/Particles                      |

CombineParticles/B2D0KD2KSHHLLBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KsHHLLBeauty2CharmFilter' , 'Phys/KTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                                                                                              |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'B+ -\> D0 K+' , 'B- -\> D0 K-' ]                                                                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/B2D0KD2KSHHLLBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                 |

TisTosParticleTagger/B2D0KD2KSHHLLBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0KD2KSHHLLBeauty2Charm' ]                                                                                                |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B2D0KD2KSHHLLBeauty2CharmTISTOS/Particles                                                                                        |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B2D0KD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                   |
| Inputs          | [ 'Phys/B2D0KD2KSHHLLBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                              |
| Output          | Phys/B2D0KD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B2D0KD2KSHHLLBeauty2CharmLine

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Code            | ALL                                                             |
| Inputs          | [ 'Phys/B2D0KD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                            |
| Output          | Phys/B2D0KD2KSHHLLBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B2D0KD2KSHHLLBeauty2CharmLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0KD2KSHHLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo1_B2D0KD2KSHHLLBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B2D0KD2KSHHLLBeauty2CharmLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0KD2KSHHLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo2_B2D0KD2KSHHLLBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B2D0KD2KSHHLLBeauty2CharmLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0KD2KSHHLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo3_B2D0KD2KSHHLLBeauty2CharmLine/Particles |
