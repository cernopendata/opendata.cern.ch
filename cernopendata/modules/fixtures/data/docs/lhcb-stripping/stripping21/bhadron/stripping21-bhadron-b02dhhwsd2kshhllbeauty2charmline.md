[[stripping21 lines]](./stripping21-index)

# StrippingB02DHHWSD2KSHHLLBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/B02DHHWSD2KSHHLLBeauty2CharmLine/Particles                              |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 0.10000000                                                                   |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB02DHHWSD2KSHHLLBeauty2CharmLineVOIDFilter

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

GaudiSequencer/SeqX2HHWSBeauty2Charm

GaudiSequencer/SEQ:X2HHWSPlusBeauty2CharmFilter

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

FilterDesktop/HHPionsInputsBeauty2CharmFilter

|                 |                                                |
|-----------------|------------------------------------------------|
| Code            | (PT\>100\*MeV) & (P\>2000\*MeV)                |
| Inputs          | [ 'Phys/PiInputsBeauty2CharmFilter' ]        |
| DecayDescriptor | None                                           |
| Output          | Phys/HHPionsInputsBeauty2CharmFilter/Particles |

CombineParticles/X2PiPiWSPlusBeauty2Charm

|                  |                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/HHPionsInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                       |
| CombinationCut   | (ASUM(PT)\>1000\*MeV) & (AM \< 5.2\*GeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<16) & (BPVVDCHI2\>16) & (BPVDIRA\>0)                                                                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ 'rho(770)+ -\> pi+ pi+' ]                                                                                                                                                                                                                                        |
| Output           | Phys/X2PiPiWSPlusBeauty2Charm/Particles                                                                                                                                                                                                                              |

SubPIDMMFilter/X2HHWSPlusSubPIDSelBeauty2Charm

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ALL                                                                                     |
| Inputs          | [ 'Phys/X2PiPiWSPlusBeauty2Charm' ]                                                   |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/X2HHWSPlusSubPIDSelBeauty2Charm/Particles                                          |
| MaxMM           | 5200.0000                                                                               |
| MinMM           | 0.0000000                                                                               |
| PIDs            | [ [ 'pi+' , 'pi+' ] , [ 'pi+' , 'K+' ] , [ 'K+' , 'pi+' ] , [ 'K+' , 'K+' ] ] |

FilterDesktop/X2HHWSPlusBeauty2CharmFilter

|                 |                                              |
|-----------------|----------------------------------------------|
| Code            | in_range(0.0,MM,5200.0)                      |
| Inputs          | [ 'Phys/X2HHWSPlusSubPIDSelBeauty2Charm' ] |
| DecayDescriptor | None                                         |
| Output          | Phys/X2HHWSPlusBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:X2HHWSMinusBeauty2CharmFilter

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

FilterDesktop/HHPionsInputsBeauty2CharmFilter

|                 |                                                |
|-----------------|------------------------------------------------|
| Code            | (PT\>100\*MeV) & (P\>2000\*MeV)                |
| Inputs          | [ 'Phys/PiInputsBeauty2CharmFilter' ]        |
| DecayDescriptor | None                                           |
| Output          | Phys/HHPionsInputsBeauty2CharmFilter/Particles |

CombineParticles/X2PiPiWSMinusBeauty2Charm

|                  |                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/HHPionsInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                       |
| CombinationCut   | (ASUM(PT)\>1000\*MeV) & (AM \< 5.2\*GeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<16) & (BPVVDCHI2\>16) & (BPVDIRA\>0)                                                                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ 'rho(770)- -\> pi- pi-' ]                                                                                                                                                                                                                                        |
| Output           | Phys/X2PiPiWSMinusBeauty2Charm/Particles                                                                                                                                                                                                                             |

SubPIDMMFilter/X2HHWSMinusSubPIDSelBeauty2Charm

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ALL                                                                                     |
| Inputs          | [ 'Phys/X2PiPiWSMinusBeauty2Charm' ]                                                  |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/X2HHWSMinusSubPIDSelBeauty2Charm/Particles                                         |
| MaxMM           | 5200.0000                                                                               |
| MinMM           | 0.0000000                                                                               |
| PIDs            | [ [ 'pi-' , 'pi-' ] , [ 'pi-' , 'K-' ] , [ 'K-' , 'pi-' ] , [ 'K-' , 'K-' ] ] |

FilterDesktop/X2HHWSMinusBeauty2CharmFilter

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | in_range(0.0,MM,5200.0)                       |
| Inputs          | [ 'Phys/X2HHWSMinusSubPIDSelBeauty2Charm' ] |
| DecayDescriptor | None                                          |
| Output          | Phys/X2HHWSMinusBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/X2HHWSBeauty2Charm

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Code            | ALL                                                                              |
| Inputs          | [ 'Phys/X2HHWSMinusBeauty2CharmFilter' , 'Phys/X2HHWSPlusBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                             |
| Output          | Phys/X2HHWSBeauty2Charm/Particles                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/B02DHHWSD2KSHHLLBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KsHHLLBeauty2CharmFilter' , 'Phys/X2HHWSBeauty2Charm' ]                                                                                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'rho(770)+' : 'ALL' , 'rho(770)-' : 'ALL' }                                                                                                                                                                                                                                                                                                                |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'B0 -\> D0 rho(770)-' , 'B0 -\> D0 rho(770)+' ]                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/B02DHHWSD2KSHHLLBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                              |

TisTosParticleTagger/B02DHHWSD2KSHHLLBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DHHWSD2KSHHLLBeauty2Charm' ]                                                                                             |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B02DHHWSD2KSHHLLBeauty2CharmTISTOS/Particles                                                                                     |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B02DHHWSD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                      |
|-----------------|----------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                      |
| Inputs          | [ 'Phys/B02DHHWSD2KSHHLLBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                 |
| Output          | Phys/B02DHHWSD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B02DHHWSD2KSHHLLBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Code            | ALL                                                                |
| Inputs          | [ 'Phys/B02DHHWSD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                               |
| Output          | Phys/B02DHHWSD2KSHHLLBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B02DHHWSD2KSHHLLBeauty2CharmLine

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DHHWSD2KSHHLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                         |
| Output          | Phys/RelatedInfo1_B02DHHWSD2KSHHLLBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B02DHHWSD2KSHHLLBeauty2CharmLine

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DHHWSD2KSHHLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                         |
| Output          | Phys/RelatedInfo2_B02DHHWSD2KSHHLLBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B02DHHWSD2KSHHLLBeauty2CharmLine

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DHHWSD2KSHHLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                         |
| Output          | Phys/RelatedInfo3_B02DHHWSD2KSHHLLBeauty2CharmLine/Particles |
