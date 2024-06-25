[[stripping21 lines]](./stripping21-index)

# StrippingDstarUPB2DKSDDD2HHHBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/DstarUPB2DKSDDD2HHHBeauty2CharmLine/Particles                           |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingDstarUPB2DKSDDD2HHHBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)/Particles')\>0 |

FilterDesktop/PiUPInputsBeauty2CharmFilter

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)  |
| Inputs          | [ 'Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/PiUPInputsBeauty2CharmFilter/Particles                                     |

GaudiSequencer/SeqD2HHHBeauty2Charm

GaudiSequencer/SEQ:D+2HHHBeauty2CharmFilter

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

CombineParticles/ProtoD+2HHHBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('pi+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','K+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','K+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','K+','pi-'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D+ -\> pi+ pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD+2HHHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

SubPIDMMFilter/D+2HHHSubPIDSelBeauty2Charm

|                 |                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                          |
| Inputs          | [ 'Phys/ProtoD+2HHHBeauty2Charm' ]                                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                         |
| Output          | Phys/D+2HHHSubPIDSelBeauty2Charm/Particles                                                                                                                                                                   |
| MaxMM           | 2068.4900                                                                                                                                                                                                    |
| MinMM           | 1769.6200                                                                                                                                                                                                    |
| PIDs            | [ [ 'pi+' , 'pi+' , 'pi-' ] , [ 'pi+' , 'pi+' , 'K-' ] , [ 'K+' , 'pi+' , 'pi-' ] , [ 'K+' , 'pi+' , 'K-' ] , [ 'pi+' , 'K+' , 'pi-' ] , [ 'pi+' , 'K+' , 'K-' ] , [ 'K+' , 'K+' , 'pi-' ] ] |

FilterDesktop/D+2HHHBeauty2CharmFilter

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | in_range(1769.62,MM,2068.49)             |
| Inputs          | [ 'Phys/D+2HHHSubPIDSelBeauty2Charm' ] |
| DecayDescriptor | None                                     |
| Output          | Phys/D+2HHHBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D-2HHHBeauty2CharmFilter

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

CombineParticles/ProtoD-2HHHBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('pi+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','K+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi+','K+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('K+','K+','pi-'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D- -\> pi- pi- pi+' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/ProtoD-2HHHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

SubPIDMMFilter/D-2HHHSubPIDSelBeauty2Charm

|                 |                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                          |
| Inputs          | [ 'Phys/ProtoD-2HHHBeauty2Charm' ]                                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                         |
| Output          | Phys/D-2HHHSubPIDSelBeauty2Charm/Particles                                                                                                                                                                   |
| MaxMM           | 2068.4900                                                                                                                                                                                                    |
| MinMM           | 1769.6200                                                                                                                                                                                                    |
| PIDs            | [ [ 'pi-' , 'pi-' , 'pi+' ] , [ 'pi-' , 'pi-' , 'K+' ] , [ 'K-' , 'pi-' , 'pi+' ] , [ 'K-' , 'pi-' , 'K+' ] , [ 'pi-' , 'K-' , 'pi+' ] , [ 'pi-' , 'K-' , 'K+' ] , [ 'K-' , 'K-' , 'pi+' ] ] |

FilterDesktop/D-2HHHBeauty2CharmFilter

|                 |                                          |
|-----------------|------------------------------------------|
| Code            | in_range(1769.62,MM,2068.49)             |
| Inputs          | [ 'Phys/D-2HHHSubPIDSelBeauty2Charm' ] |
| DecayDescriptor | None                                     |
| Output          | Phys/D-2HHHBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHHBeauty2Charm

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | ALL                                                                     |
| Inputs          | [ 'Phys/D+2HHHBeauty2CharmFilter' , 'Phys/D-2HHHBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/D2HHHBeauty2Charm/Particles                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/KS0_DDInputsBeauty2CharmFilter

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | (PT\>250\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                      |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/KS0_DDInputsBeauty2CharmFilter/Particles                           |

CombineParticles/B2DKSDDD2HHHBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2HHHBeauty2Charm' , 'Phys/KS0_DDInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                                                                                                                                                                             |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[B+ -\> D+ KS0]cc' ]                                                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/B2DKSDDD2HHHBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                  |

TisTosParticleTagger/B2DKSDDD2HHHBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2DKSDDD2HHHBeauty2Charm' ]                                                                                                 |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B2DKSDDD2HHHBeauty2CharmTISTOS/Particles                                                                                         |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                  |
| Inputs          | [ 'Phys/B2DKSDDD2HHHBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                             |
| Output          | Phys/B2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

SubstitutePID/B2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Code            | DECTREE('Beauty -\> Charm ...')                                            |
| Inputs          | [ 'Phys/B2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilter' ]             |
| DecayDescriptor | None                                                                       |
| Output          | Phys/B2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel/Particles |
| Substitutions   | { 'Beauty -\> Charm ...' : 'J/psi(1S)' }                                   |

FilterDesktop/B2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | INTREE(ID=='J/psi(1S)')                                                                         |
| Inputs          | [ 'Phys/B2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel' ]                        |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/B2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter/Particles |

CombineParticles/DstarUPB2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilter

|                  |                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter' , 'Phys/PiUPInputsBeauty2CharmFilter' ]                           |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                          |
| CombinationCut   | (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) & ((((IDD1==421)\|(IDD1==411)) & ((MD1PI-MD1) \< 180)) \| (((IDD2==421)\|(IDD2==411)) & ((MD2PI-MD2) \< 180))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVDIRA\>0.999)                                                                                                                   |
| DecayDescriptor  | [B+ -\> J/psi(1S) pi+]cc                                                                                                                                    |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) pi+]cc' ]                                                                                                                            |
| Output           | Phys/DstarUPB2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles                                                                                       |

FilterDesktop/DstarUPB2DKSDDD2HHHBeauty2CharmLine

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | ALL                                                                   |
| Inputs          | [ 'Phys/DstarUPB2DKSDDD2HHHBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/DstarUPB2DKSDDD2HHHBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_DstarUPB2DKSDDD2HHHBeauty2CharmLine

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB2DKSDDD2HHHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                            |
| Output          | Phys/RelatedInfo1_DstarUPB2DKSDDD2HHHBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_DstarUPB2DKSDDD2HHHBeauty2CharmLine

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB2DKSDDD2HHHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                            |
| Output          | Phys/RelatedInfo2_DstarUPB2DKSDDD2HHHBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_DstarUPB2DKSDDD2HHHBeauty2CharmLine

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB2DKSDDD2HHHBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                            |
| Output          | Phys/RelatedInfo3_DstarUPB2DKSDDD2HHHBeauty2CharmLine/Particles |
