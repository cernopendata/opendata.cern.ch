[[stripping21 lines]](./stripping21-index)

# StrippingB02D0DKBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/B02D0DKBeauty2CharmLine/Particles                                       |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB02D0DKBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

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

CombineParticles/B02D0DKBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2HHHPIDBeauty2CharmFilter' , 'Phys/D2HHPIDBeauty2CharmFilter' , 'Phys/KTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                                                                |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'B0 -\> D0 D- K+' , 'B0 -\> D0 D+ K-' ]                                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/B02D0DKBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                       |

TisTosParticleTagger/B02D0DKBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02D0DKBeauty2Charm' ]                                                                                                      |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B02D0DKBeauty2CharmTISTOS/Particles                                                                                              |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B02D0DKBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                             |
|-----------------|-------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                             |
| Inputs          | [ 'Phys/B02D0DKBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                        |
| Output          | Phys/B02D0DKBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B02D0DKBeauty2CharmLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | ALL                                                       |
| Inputs          | [ 'Phys/B02D0DKBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                      |
| Output          | Phys/B02D0DKBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B02D0DKBeauty2CharmLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B02D0DKBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo1_B02D0DKBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B02D0DKBeauty2CharmLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B02D0DKBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo2_B02D0DKBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B02D0DKBeauty2CharmLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B02D0DKBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo3_B02D0DKBeauty2CharmLine/Particles |
