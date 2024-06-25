[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine/Particles                     |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingDstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21r1-commonparticles-stdnopidsuppions)/Particles')\>0 |

FilterDesktop/PiUPInputsBeauty2CharmFilter

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)    |
| Inputs          | [ 'Phys/[StdNoPIDsUpPions](./stripping21r1-commonparticles-stdnopidsuppions)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/PiUPInputsBeauty2CharmFilter/Particles                                       |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]           |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                        |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                             |

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

FilterDesktop/HHHPionsInputsBeauty2CharmFilter

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | (PT\>100\*MeV) & (P\>2000\*MeV) & (PIDK\<10)    |
| Inputs          | [ 'Phys/PiInputsBeauty2CharmFilter' ]         |
| DecayDescriptor | None                                            |
| Output          | Phys/HHHPionsInputsBeauty2CharmFilter/Particles |

CombineParticles/X2PiPiPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/HHHPionsInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                        |
| CombinationCut   | (ASUM(PT)\>1250\*MeV) & (AM \< 3000\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.40\*mm,'LoKi::DistanceCalculator')) & (ANUM(PT \< 300\*MeV) \<= 1) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<8) & (BPVVDCHI2\>16) & (BPVDIRA\>0.98) & (MIPCHI2DV(PRIMARY)\>0.0) & (BPVVDRHO\>0.1\*mm) & (BPVVDZ\>2.0\*mm)                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[a_1(1260)+ -\> pi+ pi- pi+]cc' ]                                                                                                                                                                                                                                                              |
| Output           | Phys/X2PiPiPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                   |

CombineParticles/B2D0PiPiPiD2KSHHLLBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KsHHLLBeauty2CharmFilter' , 'Phys/X2PiPiPiBeauty2Charm' ]                                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'a_1(1260)+' : 'ALL' , 'a_1(1260)-' : 'ALL' }                                                                                                                                                                                                                                                                                                              |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'B+ -\> D0 a_1(1260)+' , 'B- -\> D0 a_1(1260)-' ]                                                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/B2D0PiPiPiD2KSHHLLBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                            |

TisTosParticleTagger/B2D0PiPiPiD2KSHHLLBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0PiPiPiD2KSHHLLBeauty2Charm' ]                                                                                           |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B2D0PiPiPiD2KSHHLLBeauty2CharmTISTOS/Particles                                                                                   |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                        |
|-----------------|------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                        |
| Inputs          | [ 'Phys/B2D0PiPiPiD2KSHHLLBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                   |
| Output          | Phys/B2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

SubstitutePID/B2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Code            | DECTREE('Beauty -\> Charm ...')                                                  |
| Inputs          | [ 'Phys/B2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter' ]             |
| DecayDescriptor | None                                                                             |
| Output          | Phys/B2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel/Particles |
| Substitutions   | { 'Beauty -\> Charm ...' : 'J/psi(1S)' }                                         |

FilterDesktop/B2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | INTREE(ID=='J/psi(1S)')                                                                               |
| Inputs          | [ 'Phys/B2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel' ]                        |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/B2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter/Particles |

CombineParticles/DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter

|                  |                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter' , 'Phys/PiUPInputsBeauty2CharmFilter' ]                     |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                          |
| CombinationCut   | (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) & ((((IDD1==421)\|(IDD1==411)) & ((MD1PI-MD1) \< 180)) \| (((IDD2==421)\|(IDD2==411)) & ((MD2PI-MD2) \< 180))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVDIRA\>0.999)                                                                                                                   |
| DecayDescriptor  | [B+ -\> J/psi(1S) pi+]cc                                                                                                                                    |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) pi+]cc' ]                                                                                                                            |
| Output           | Phys/DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles                                                                                 |

FilterDesktop/DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | ALL                                                                         |
| Inputs          | [ 'Phys/DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                  |
| Output          | Phys/RelatedInfo1_DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                  |
| Output          | Phys/RelatedInfo2_DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                  |
| Output          | Phys/RelatedInfo3_DstarUPB2D0PiPiPiD2KSHHLLBeauty2CharmLine/Particles |
