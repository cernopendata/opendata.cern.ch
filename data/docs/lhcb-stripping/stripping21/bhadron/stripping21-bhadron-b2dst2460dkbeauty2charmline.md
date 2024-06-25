[[stripping21 lines]](./stripping21-index)

# StrippingB2Dst2460DKBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/B2Dst2460DKBeauty2CharmLine/Particles                                   |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB2Dst2460DKBeauty2CharmLineVOIDFilter

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

FilterDesktop/D2HHPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2HHBeauty2CharmFilter' ]                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2HHPIDBeauty2CharmFilter/Particles                                                                                                                                |

FilterDesktop/D2KPIPIDBeauty2CharmFilter

|                 |                                           |
|-----------------|-------------------------------------------|
| Code            | NINTREE(ABSID=='K+') == 1                 |
| Inputs          | [ 'Phys/D2HHPIDBeauty2CharmFilter' ]    |
| DecayDescriptor | None                                      |
| Output          | Phys/D2KPIPIDBeauty2CharmFilter/Particles |

CombineParticles/Dstar24602D0PiBeauty2Charm

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KPIPIDBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }           |
| CombinationCut   | (ADAMASS('D\*\_2(2460)+') \< 100\*MeV) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                               |
| DecayDescriptor  | None                                                                                    |
| DecayDescriptors | [ 'D\*\_2(2460)+ -\> pi+ D0' , 'D\*\_2(2460)- -\> pi- D0' ]                           |
| Output           | Phys/Dstar24602D0PiBeauty2Charm/Particles                                               |

FilterDesktop/Dstar24602D0PiPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),2) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 2) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 2) == 0) |
| Inputs          | [ 'Phys/Dstar24602D0PiBeauty2Charm' ]                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/Dstar24602D0PiPIDBeauty2CharmFilter/Particles                                                                                                                      |

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

FilterDesktop/D2HHHPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2HHHBeauty2Charm' ]                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2HHHPIDBeauty2CharmFilter/Particles                                                                                                                               |

FilterDesktop/D2HHHCFPIDBeauty2CharmFilter

|                 |                                                                                                                                                                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((((ID=='D+') & (NINTREE(ID=='K-')==1) & (NINTREE(ABSID=='K+') == 1)) \| ((ID=='D-') & (NINTREE(ID=='K+')==1) & (NINTREE(ABSID=='K+') == 1))) & (in_range(1769.62\*MeV,MM,1969.62\*MeV))) \| (((NINTREE(ID=='K-')==1) & (NINTREE(ID=='K+')==1)) & (in_range(1868.49\*MeV,MM,2068.49\*MeV))) |
| Inputs          | [ 'Phys/D2HHHPIDBeauty2CharmFilter' ]                                                                                                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                        |
| Output          | Phys/D2HHHCFPIDBeauty2CharmFilter/Particles                                                                                                                                                                                                                                                 |

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

CombineParticles/B2Dst2460DKBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2HHHCFPIDBeauty2CharmFilter' , 'Phys/Dstar24602D0PiPIDBeauty2CharmFilter' , 'Phys/KTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'D\*\_2(2460)+' : 'ALL' , 'D\*\_2(2460)-' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                                           |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[B+ -\> D\*\_2(2460)+ D- K+]cc' , '[B+ -\> D\*\_2(2460)- D+ K+]cc' ]                                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/B2Dst2460DKBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                   |

TisTosParticleTagger/B2Dst2460DKBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2Dst2460DKBeauty2Charm' ]                                                                                                  |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B2Dst2460DKBeauty2CharmTISTOS/Particles                                                                                          |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B2Dst2460DKBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                 |
| Inputs          | [ 'Phys/B2Dst2460DKBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                            |
| Output          | Phys/B2Dst2460DKBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B2Dst2460DKBeauty2CharmLine

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | ALL                                                           |
| Inputs          | [ 'Phys/B2Dst2460DKBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                          |
| Output          | Phys/B2Dst2460DKBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B2Dst2460DKBeauty2CharmLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2Dst2460DKBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo1_B2Dst2460DKBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B2Dst2460DKBeauty2CharmLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2Dst2460DKBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo2_B2Dst2460DKBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B2Dst2460DKBeauty2CharmLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2Dst2460DKBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo3_B2Dst2460DKBeauty2CharmLine/Particles |
