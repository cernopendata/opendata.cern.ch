[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2D0PiD2Pi0HHWSResolvedBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine/Particles                       |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 0.10000000                                                                   |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB2D0PiD2Pi0HHWSResolvedBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqD2Pi0HHWSBeauty2CharmResolved

GaudiSequencer/SEQ:D2Pi0HHWSPlusResolvedBeauty2CharmFilter

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

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

FilterDesktop/Pi0ResolvedInputsBeauty2CharmFilter

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV) & (CHILD(CL,1)\>0.25) & (CHILD(CL,2)\>0.25) |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)' ]    |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/Pi0ResolvedInputsBeauty2CharmFilter/Particles                                         |

CombineParticles/ProtoD2Pi0HHWSPlusResolvedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0ResolvedInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                          |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi0','pi+','pi+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi0','pi+','K+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi0','K+','pi+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi0','K+','K+'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'D0 -\> pi0 pi+ pi+' ]                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/ProtoD2Pi0HHWSPlusResolvedBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                   |

SubPIDMMFilter/D2Pi0HHWSPlusSubPIDSelBeauty2CharmResolved

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                     |
| Inputs          | [ 'Phys/ProtoD2Pi0HHWSPlusResolvedBeauty2Charm' ]                                                                     |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/D2Pi0HHWSPlusSubPIDSelBeauty2CharmResolved/Particles                                                               |
| MaxMM           | 1964.8400                                                                                                               |
| MinMM           | 1764.8400                                                                                                               |
| PIDs            | [ [ 'pi0' , 'pi+' , 'pi+' ] , [ 'pi0' , 'pi+' , 'K+' ] , [ 'pi0' , 'K+' , 'pi+' ] , [ 'pi0' , 'K+' , 'K+' ] ] |

FilterDesktop/D2Pi0HHWSPlusResolvedBeauty2CharmFilter

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Code            | in_range(1764.84,MM,1964.84)                            |
| Inputs          | [ 'Phys/D2Pi0HHWSPlusSubPIDSelBeauty2CharmResolved' ] |
| DecayDescriptor | None                                                    |
| Output          | Phys/D2Pi0HHWSPlusResolvedBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D2Pi0HHWSMinusResolvedBeauty2CharmFilter

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

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

FilterDesktop/Pi0ResolvedInputsBeauty2CharmFilter

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (ABSID==111) & (PT\>500\*MeV) & (P\>1000\*MeV) & (CHILD(CL,1)\>0.25) & (CHILD(CL,2)\>0.25) |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)' ]    |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/Pi0ResolvedInputsBeauty2CharmFilter/Particles                                         |

CombineParticles/ProtoD2Pi0HHWSMinusResolvedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0ResolvedInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                          |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi0','pi+','pi+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi0','pi+','K+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi0','K+','pi+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi0','K+','K+'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'D0 -\> pi0 pi- pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/ProtoD2Pi0HHWSMinusResolvedBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                  |

SubPIDMMFilter/D2Pi0HHWSMinusSubPIDSelBeauty2CharmResolved

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                     |
| Inputs          | [ 'Phys/ProtoD2Pi0HHWSMinusResolvedBeauty2Charm' ]                                                                    |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/D2Pi0HHWSMinusSubPIDSelBeauty2CharmResolved/Particles                                                              |
| MaxMM           | 1964.8400                                                                                                               |
| MinMM           | 1764.8400                                                                                                               |
| PIDs            | [ [ 'pi0' , 'pi-' , 'pi-' ] , [ 'pi0' , 'pi-' , 'K-' ] , [ 'pi0' , 'K-' , 'pi-' ] , [ 'pi0' , 'K-' , 'K-' ] ] |

FilterDesktop/D2Pi0HHWSMinusResolvedBeauty2CharmFilter

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Code            | in_range(1764.84,MM,1964.84)                             |
| Inputs          | [ 'Phys/D2Pi0HHWSMinusSubPIDSelBeauty2CharmResolved' ] |
| DecayDescriptor | None                                                     |
| Output          | Phys/D2Pi0HHWSMinusResolvedBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2Pi0HHWSBeauty2CharmResolved

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                    |
| Inputs          | [ 'Phys/D2Pi0HHWSMinusResolvedBeauty2CharmFilter' , 'Phys/D2Pi0HHWSPlusResolvedBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/D2Pi0HHWSBeauty2CharmResolved/Particles                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

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

FilterDesktop/PiTopoInputsBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/PiInputsBeauty2CharmFilter' ]                           |
| DecayDescriptor | None                                                              |
| Output          | Phys/PiTopoInputsBeauty2CharmFilter/Particles                     |

CombineParticles/B2D0PiD2Pi0HHWSResolvedBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2Pi0HHWSBeauty2CharmResolved' , 'Phys/PiTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                            |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'B+ -\> D0 pi+' , 'B- -\> D0 pi-' ]                                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/B2D0PiD2Pi0HHWSResolvedBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                       |

TisTosParticleTagger/B2D0PiD2Pi0HHWSResolvedBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0PiD2Pi0HHWSResolvedBeauty2Charm' ]                                                                                      |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B2D0PiD2Pi0HHWSResolvedBeauty2CharmTISTOS/Particles                                                                              |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B2D0PiD2Pi0HHWSResolvedBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                             |
| Inputs          | [ 'Phys/B2D0PiD2Pi0HHWSResolvedBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2D0PiD2Pi0HHWSResolvedBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | ALL                                                                       |
| Inputs          | [ 'Phys/B2D0PiD2Pi0HHWSResolvedBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                |
| Output          | Phys/RelatedInfo1_B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                |
| Output          | Phys/RelatedInfo2_B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                |
| Output          | Phys/RelatedInfo3_B2D0PiD2Pi0HHWSResolvedBeauty2CharmLine/Particles |
