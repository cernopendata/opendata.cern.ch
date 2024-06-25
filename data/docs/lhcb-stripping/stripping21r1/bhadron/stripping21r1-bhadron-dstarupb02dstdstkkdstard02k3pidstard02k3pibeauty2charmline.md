[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine/Particles    |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingDstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLineVOIDFilter

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

CombineParticles/ProtoD2HHHHBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi+','pi-','pi-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi+','pi+','K-','pi-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi+','pi+','pi-','K-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('K+','pi+','pi-','pi-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi+','K+','pi-','pi-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('K+','pi+','K-','pi-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('K+','pi+','pi-','K-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi+','K+','K-','pi-'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi+','K+','pi-','K-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ 'D0 -\> pi+ pi+ pi- pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output           | Phys/ProtoD2HHHHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

SubPIDMMFilter/D2HHHHSubPIDSelBeauty2Charm

|                 |                                                                                                                                                                                                                                                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                                           |
| Inputs          | [ 'Phys/ProtoD2HHHHBeauty2Charm' ]                                                                                                                                                                                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                          |
| Output          | Phys/D2HHHHSubPIDSelBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                    |
| MaxMM           | 1964.8400                                                                                                                                                                                                                                                                                                                                     |
| MinMM           | 1764.8400                                                                                                                                                                                                                                                                                                                                     |
| PIDs            | [ [ 'pi+' , 'pi+' , 'pi-' , 'pi-' ] , [ 'pi+' , 'pi+' , 'K-' , 'pi-' ] , [ 'pi+' , 'pi+' , 'pi-' , 'K-' ] , [ 'K+' , 'pi+' , 'pi-' , 'pi-' ] , [ 'pi+' , 'K+' , 'pi-' , 'pi-' ] , [ 'K+' , 'pi+' , 'K-' , 'pi-' ] , [ 'K+' , 'pi+' , 'pi-' , 'K-' ] , [ 'pi+' , 'K+' , 'K-' , 'pi-' ] , [ 'pi+' , 'K+' , 'pi-' , 'K-' ] ] |

FilterDesktop/D2HHHHBeauty2CharmFilter

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | in_range(1764.84,MM,1964.84)             |
| Inputs          | [ 'Phys/D2HHHHSubPIDSelBeauty2Charm' ] |
| DecayDescriptor | None                                     |
| Output          | Phys/D2HHHHBeauty2CharmFilter/Particles  |

FilterDesktop/D2K3PIBeauty2CharmFilter

|                 |                                         |
|-----------------|-----------------------------------------|
| Code            | NINTREE(ABSID=='K+') == 1               |
| Inputs          | [ 'Phys/D2HHHHBeauty2CharmFilter' ]   |
| DecayDescriptor | None                                    |
| Output          | Phys/D2K3PIBeauty2CharmFilter/Particles |

CombineParticles/DstarD2K3Pi2D0PiBeauty2Charm

|                  |                                                                                     |
|------------------|-------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2K3PIBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]           |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }       |
| CombinationCut   | (ADAMASS('D\*(2010)+') \< 50\*MeV) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                           |
| DecayDescriptor  | None                                                                                |
| DecayDescriptors | [ 'D\*(2010)+ -\> pi+ D0' , 'D\*(2010)- -\> pi- D0' ]                             |
| Output           | Phys/DstarD2K3Pi2D0PiBeauty2Charm/Particles                                         |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' ]           |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

FilterDesktop/KTopoInputsBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/KInputsBeauty2CharmFilter' ]                            |
| DecayDescriptor | None                                                              |
| Output          | Phys/KTopoInputsBeauty2CharmFilter/Particles                      |

CombineParticles/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DstarD2K3Pi2D0PiBeauty2Charm' , 'Phys/KTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                                                                               |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'B0 -\> D\*(2010)+ D\*(2010)- K+ K-' ]                                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                           |

TisTosParticleTagger/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2Charm' ]                                                                          |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmTISTOS/Particles                                                                  |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                                         |
| Inputs          | [ 'Phys/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

SubstitutePID/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel

|                 |                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------|
| Code            | DECTREE('Beauty -\> Charm ...')                                                                   |
| Inputs          | [ 'Phys/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilter' ]             |
| DecayDescriptor | None                                                                                              |
| Output          | Phys/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel/Particles |
| Substitutions   | { 'Beauty -\> Charm ...' : 'J/psi(1S)' }                                                          |

FilterDesktop/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter

|                 |                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Code            | INTREE(ID=='J/psi(1S)')                                                                                                |
| Inputs          | [ 'Phys/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel' ]                        |
| DecayDescriptor | None                                                                                                                   |
| Output          | Phys/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter/Particles |

CombineParticles/DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilter

|                  |                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter' , 'Phys/PiUPInputsBeauty2CharmFilter' ]    |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                          |
| CombinationCut   | (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) & ((((IDD1==421)\|(IDD1==411)) & ((MD1PI-MD1) \< 180)) \| (((IDD2==421)\|(IDD2==411)) & ((MD2PI-MD2) \< 180))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVDIRA\>0.999)                                                                                                                   |
| DecayDescriptor  | [B+ -\> J/psi(1S) pi+]cc                                                                                                                                    |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) pi+]cc' ]                                                                                                                            |
| Output           | Phys/DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles                                                                |

FilterDesktop/DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine

|                 |                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                          |
| Inputs          | [ 'Phys/DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                                         |
| Output          | Phys/DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine

|                 |                                                                                        |
|-----------------|----------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                                   |
| Output          | Phys/RelatedInfo1_DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine

|                 |                                                                                        |
|-----------------|----------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                                   |
| Output          | Phys/RelatedInfo2_DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine

|                 |                                                                                        |
|-----------------|----------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                                   |
| Output          | Phys/RelatedInfo3_DstarUPB02DstDstKKDstarD02K3PiDstarD02K3PiBeauty2CharmLine/Particles |
