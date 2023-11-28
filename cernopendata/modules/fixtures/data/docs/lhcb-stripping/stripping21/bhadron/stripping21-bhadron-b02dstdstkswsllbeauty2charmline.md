[[stripping21 lines]](./stripping21-index)

# StrippingB02DstDstKSWSLLBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/B02DstDstKSWSLLBeauty2CharmLine/Particles                               |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 0.10000000                                                                   |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB02DstDstKSWSLLBeauty2CharmLineVOIDFilter

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

CombineParticles/ProtoD2HHBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi+','K-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('K+','pi-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('K+','K-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'D0 -\> pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/ProtoD2HHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                     |

SubPIDMMFilter/D2HHSubPIDSelBeauty2Charm

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ALL                                                                                     |
| Inputs          | [ 'Phys/ProtoD2HHBeauty2Charm' ]                                                      |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/D2HHSubPIDSelBeauty2Charm/Particles                                                |
| MaxMM           | 1964.8400                                                                               |
| MinMM           | 1764.8400                                                                               |
| PIDs            | [ [ 'pi+' , 'pi-' ] , [ 'pi+' , 'K-' ] , [ 'K+' , 'pi-' ] , [ 'K+' , 'K-' ] ] |

FilterDesktop/D2HHBeauty2CharmFilter

|                 |                                        |
|-----------------|----------------------------------------|
| Code            | in_range(1764.84,MM,1964.84)           |
| Inputs          | [ 'Phys/D2HHSubPIDSelBeauty2Charm' ] |
| DecayDescriptor | None                                   |
| Output          | Phys/D2HHBeauty2CharmFilter/Particles  |

CombineParticles/Dstar2D0PiBeauty2Charm

|                  |                                                                                     |
|------------------|-------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2HHBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }       |
| CombinationCut   | (ADAMASS('D\*(2010)+') \< 50\*MeV) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                           |
| DecayDescriptor  | None                                                                                |
| DecayDescriptors | [ 'D\*(2010)+ -\> pi+ D0' , 'D\*(2010)- -\> pi- D0' ]                             |
| Output           | Phys/Dstar2D0PiBeauty2Charm/Particles                                               |

FilterDesktop/Dstar2D0PiPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),2) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 2) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 2) == 0) |
| Inputs          | [ 'Phys/Dstar2D0PiBeauty2Charm' ]                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/Dstar2D0PiPIDBeauty2CharmFilter/Particles                                                                                                                          |

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

CombineParticles/B02DstDstKSWSLLBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Dstar2D0PiPIDBeauty2CharmFilter' , 'Phys/KS0_LLInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                                                                                                                                                             |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[B0 -\> D\*(2010)- D\*(2010)- KS0]cc' ]                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/B02DstDstKSWSLLBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                               |

TisTosParticleTagger/B02DstDstKSWSLLBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DstDstKSWSLLBeauty2Charm' ]                                                                                              |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B02DstDstKSWSLLBeauty2CharmTISTOS/Particles                                                                                      |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B02DstDstKSWSLLBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                     |
| Inputs          | [ 'Phys/B02DstDstKSWSLLBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                |
| Output          | Phys/B02DstDstKSWSLLBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B02DstDstKSWSLLBeauty2CharmLine

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | ALL                                                               |
| Inputs          | [ 'Phys/B02DstDstKSWSLLBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                              |
| Output          | Phys/B02DstDstKSWSLLBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B02DstDstKSWSLLBeauty2CharmLine

|                 |                                                             |
|-----------------|-------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DstDstKSWSLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                        |
| Output          | Phys/RelatedInfo1_B02DstDstKSWSLLBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B02DstDstKSWSLLBeauty2CharmLine

|                 |                                                             |
|-----------------|-------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DstDstKSWSLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                        |
| Output          | Phys/RelatedInfo2_B02DstDstKSWSLLBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B02DstDstKSWSLLBeauty2CharmLine

|                 |                                                             |
|-----------------|-------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DstDstKSWSLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                        |
| Output          | Phys/RelatedInfo3_B02DstDstKSWSLLBeauty2CharmLine/Particles |
