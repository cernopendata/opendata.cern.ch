[[stripping21 lines]](./stripping21-index)

# StrippingB2D0PiPi0ResolvedD2K3PiBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine/Particles                       |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB2D0PiPi0ResolvedD2K3PiBeauty2CharmLineVOIDFilter

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

FilterDesktop/D2K3PIPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2K3PIBeauty2CharmFilter' ]                                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2K3PIPIDBeauty2CharmFilter/Particles                                                                                                                              |

FilterDesktop/PiTopoInputsBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/PiInputsBeauty2CharmFilter' ]                           |
| DecayDescriptor | None                                                              |
| Output          | Phys/PiTopoInputsBeauty2CharmFilter/Particles                     |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

FilterDesktop/Pi0ResolvedInputsBeauty2CharmFilter

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV) & (CHILD(CL,1)\>0.25) & (CHILD(CL,2)\>0.25) |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21-commonparticles-stdlooseresolvedpi0)' ]      |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/Pi0ResolvedInputsBeauty2CharmFilter/Particles                                         |

FilterDesktop/Pi0FromBResolvedBeauty2CharmFilter

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | P \> 2000\*MeV                                    |
| Inputs          | [ 'Phys/Pi0ResolvedInputsBeauty2CharmFilter' ]  |
| DecayDescriptor | None                                              |
| Output          | Phys/Pi0FromBResolvedBeauty2CharmFilter/Particles |

CombineParticles/B2D0PiPi0ResolvedD2K3PiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2K3PIPIDBeauty2CharmFilter' , 'Phys/Pi0FromBResolvedBeauty2CharmFilter' , 'Phys/PiTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                                                                                                                                                                                                                                                                                                            |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<5800\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'B+ -\> D0 pi+ pi0' , 'B- -\> D0 pi- pi0' ]                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/B2D0PiPi0ResolvedD2K3PiBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                       |

TisTosParticleTagger/B2D0PiPi0ResolvedD2K3PiBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0PiPi0ResolvedD2K3PiBeauty2Charm' ]                                                                                      |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B2D0PiPi0ResolvedD2K3PiBeauty2CharmTISTOS/Particles                                                                              |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B2D0PiPi0ResolvedD2K3PiBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                             |
| Inputs          | [ 'Phys/B2D0PiPi0ResolvedD2K3PiBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2D0PiPi0ResolvedD2K3PiBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | ALL                                                                       |
| Inputs          | [ 'Phys/B2D0PiPi0ResolvedD2K3PiBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                |
| Output          | Phys/RelatedInfo1_B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                |
| Output          | Phys/RelatedInfo2_B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                |
| Output          | Phys/RelatedInfo3_B2D0PiPi0ResolvedD2K3PiBeauty2CharmLine/Particles |
