[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB02DKWSD2Pi0HHHMergedBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/B02DKWSD2Pi0HHHMergedBeauty2CharmLine/Particles                         |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 0.10000000                                                                   |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB02DKWSD2Pi0HHHMergedBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqD2Pi0HHHBeauty2Charm_Merged

GaudiSequencer/SEQ:D+2Pi0HHHMergedBeauty2CharmFilter

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

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)/Particles')\>0 |

FilterDesktop/Pi0MergedInputsBeauty2CharmFilter

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV)                                      |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Pi0MergedInputsBeauty2CharmFilter/Particles                                    |

CombineParticles/ProtoD+2Pi0HHH_MergedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0MergedInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('pi0','pi+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','pi+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','K+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','K+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','pi+','K+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','pi+','K+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','K+','K+','pi-'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'D+ -\> pi0 pi+ pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/ProtoD+2Pi0HHH_MergedBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

SubPIDMMFilter/D+2Pi0HHHSubPIDSelBeauty2CharmMerged

|                 |                                                                                                                                                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                  |
| Inputs          | [ 'Phys/ProtoD+2Pi0HHH_MergedBeauty2Charm' ]                                                                                                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                                                                                 |
| Output          | Phys/D+2Pi0HHHSubPIDSelBeauty2CharmMerged/Particles                                                                                                                                                                                                                  |
| MaxMM           | 2068.4900                                                                                                                                                                                                                                                            |
| MinMM           | 1769.6200                                                                                                                                                                                                                                                            |
| PIDs            | [ [ 'pi0' , 'pi+' , 'pi+' , 'pi-' ] , [ 'pi0' , 'pi+' , 'pi+' , 'K-' ] , [ 'pi0' , 'K+' , 'pi+' , 'pi-' ] , [ 'pi0' , 'K+' , 'pi+' , 'K-' ] , [ 'pi0' , 'pi+' , 'K+' , 'pi-' ] , [ 'pi0' , 'pi+' , 'K+' , 'K-' ] , [ 'pi0' , 'K+' , 'K+' , 'pi-' ] ] |

FilterDesktop/D+2Pi0HHHMergedBeauty2CharmFilter

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | in_range(1769.62,MM,2068.49)                      |
| Inputs          | [ 'Phys/D+2Pi0HHHSubPIDSelBeauty2CharmMerged' ] |
| DecayDescriptor | None                                              |
| Output          | Phys/D+2Pi0HHHMergedBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D-2Pi0HHHMergedBeauty2CharmFilter

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

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)/Particles')\>0 |

FilterDesktop/Pi0MergedInputsBeauty2CharmFilter

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV)                                      |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Pi0MergedInputsBeauty2CharmFilter/Particles                                    |

CombineParticles/ProtoD-2Pi0HHH_MergedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0MergedInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1769.62\*MeV,AWM('pi0','pi+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','pi+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','K+','pi+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','K+','pi+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','pi+','K+','pi-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','pi+','K+','K-'),2068.49\*MeV)\|in_range(1769.62\*MeV,AWM('pi0','K+','K+','pi-'),2068.49\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'D- -\> pi0 pi- pi- pi+' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/ProtoD-2Pi0HHH_MergedBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

SubPIDMMFilter/D-2Pi0HHHSubPIDSelBeauty2CharmMerged

|                 |                                                                                                                                                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                  |
| Inputs          | [ 'Phys/ProtoD-2Pi0HHH_MergedBeauty2Charm' ]                                                                                                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                                                                                 |
| Output          | Phys/D-2Pi0HHHSubPIDSelBeauty2CharmMerged/Particles                                                                                                                                                                                                                  |
| MaxMM           | 2068.4900                                                                                                                                                                                                                                                            |
| MinMM           | 1769.6200                                                                                                                                                                                                                                                            |
| PIDs            | [ [ 'pi0' , 'pi-' , 'pi-' , 'pi+' ] , [ 'pi0' , 'pi-' , 'pi-' , 'K+' ] , [ 'pi0' , 'K-' , 'pi-' , 'pi+' ] , [ 'pi0' , 'K-' , 'pi-' , 'K+' ] , [ 'pi0' , 'pi-' , 'K-' , 'pi+' ] , [ 'pi0' , 'pi-' , 'K-' , 'K+' ] , [ 'pi0' , 'K-' , 'K-' , 'pi+' ] ] |

FilterDesktop/D-2Pi0HHHMergedBeauty2CharmFilter

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | in_range(1769.62,MM,2068.49)                      |
| Inputs          | [ 'Phys/D-2Pi0HHHSubPIDSelBeauty2CharmMerged' ] |
| DecayDescriptor | None                                              |
| Output          | Phys/D-2Pi0HHHMergedBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2Pi0HHHBeauty2Charm_Merged

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                       |
| Inputs          | [ 'Phys/D+2Pi0HHHMergedBeauty2CharmFilter' , 'Phys/D-2Pi0HHHMergedBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/D2Pi0HHHBeauty2Charm_Merged/Particles                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

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

CombineParticles/B02DKWSD2Pi0HHHMergedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2Pi0HHHBeauty2Charm_Merged' , 'Phys/KTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                                                                                               |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[B0 -\> D- K-]cc' ]                                                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/B02DKWSD2Pi0HHHMergedBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                         |

TisTosParticleTagger/B02DKWSD2Pi0HHHMergedBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DKWSD2Pi0HHHMergedBeauty2Charm' ]                                                                                        |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B02DKWSD2Pi0HHHMergedBeauty2CharmTISTOS/Particles                                                                                |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B02DKWSD2Pi0HHHMergedBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                           |
| Inputs          | [ 'Phys/B02DKWSD2Pi0HHHMergedBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                      |
| Output          | Phys/B02DKWSD2Pi0HHHMergedBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B02DKWSD2Pi0HHHMergedBeauty2CharmLine

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | ALL                                                                     |
| Inputs          | [ 'Phys/B02DKWSD2Pi0HHHMergedBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/B02DKWSD2Pi0HHHMergedBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B02DKWSD2Pi0HHHMergedBeauty2CharmLine

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DKWSD2Pi0HHHMergedBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                              |
| Output          | Phys/RelatedInfo1_B02DKWSD2Pi0HHHMergedBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B02DKWSD2Pi0HHHMergedBeauty2CharmLine

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DKWSD2Pi0HHHMergedBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                              |
| Output          | Phys/RelatedInfo2_B02DKWSD2Pi0HHHMergedBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B02DKWSD2Pi0HHHMergedBeauty2CharmLine

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DKWSD2Pi0HHHMergedBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                              |
| Output          | Phys/RelatedInfo3_B02DKWSD2Pi0HHHMergedBeauty2CharmLine/Particles |
