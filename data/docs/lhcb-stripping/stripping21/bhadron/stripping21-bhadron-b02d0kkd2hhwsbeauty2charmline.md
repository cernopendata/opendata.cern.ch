[[stripping21 lines]](./stripping21-index)

# StrippingB02D0KKD2HHWSBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/B02D0KKD2HHWSBeauty2CharmLine/Particles                                 |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 0.10000000                                                                   |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB02D0KKD2HHWSBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqD2HHWSBeauty2Charm

GaudiSequencer/SEQ:D2HHWSPlusBeauty2CharmFilter

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

CombineParticles/ProtoD2HHWSPlusBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi+','K+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('K+','pi+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('K+','K+'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'D0 -\> pi+ pi+' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/ProtoD2HHWSPlusBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                               |

SubPIDMMFilter/D2HHWSPlusSubPIDSelBeauty2Charm

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ALL                                                                                     |
| Inputs          | [ 'Phys/ProtoD2HHWSPlusBeauty2Charm' ]                                                |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/D2HHWSPlusSubPIDSelBeauty2Charm/Particles                                          |
| MaxMM           | 1964.8400                                                                               |
| MinMM           | 1764.8400                                                                               |
| PIDs            | [ [ 'pi+' , 'pi+' ] , [ 'pi+' , 'K+' ] , [ 'K+' , 'pi+' ] , [ 'K+' , 'K+' ] ] |

FilterDesktop/D2HHWSPlusBeauty2CharmFilter

|                 |                                              |
|-----------------|----------------------------------------------|
| Code            | in_range(1764.84,MM,1964.84)                 |
| Inputs          | [ 'Phys/D2HHWSPlusSubPIDSelBeauty2Charm' ] |
| DecayDescriptor | None                                         |
| Output          | Phys/D2HHWSPlusBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:D2HHWSMinusBeauty2CharmFilter

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

CombineParticles/ProtoD2HHWSMinusBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('pi+','K+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('K+','pi+'),1964.84\*MeV)\|in_range(1764.84\*MeV,AWM('K+','K+'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'D0 -\> pi- pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/ProtoD2HHWSMinusBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                                                                              |

SubPIDMMFilter/D2HHWSMinusSubPIDSelBeauty2Charm

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ALL                                                                                     |
| Inputs          | [ 'Phys/ProtoD2HHWSMinusBeauty2Charm' ]                                               |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/D2HHWSMinusSubPIDSelBeauty2Charm/Particles                                         |
| MaxMM           | 1964.8400                                                                               |
| MinMM           | 1764.8400                                                                               |
| PIDs            | [ [ 'pi-' , 'pi-' ] , [ 'pi-' , 'K-' ] , [ 'K-' , 'pi-' ] , [ 'K-' , 'K-' ] ] |

FilterDesktop/D2HHWSMinusBeauty2CharmFilter

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | in_range(1764.84,MM,1964.84)                  |
| Inputs          | [ 'Phys/D2HHWSMinusSubPIDSelBeauty2Charm' ] |
| DecayDescriptor | None                                          |
| Output          | Phys/D2HHWSMinusBeauty2CharmFilter/Particles  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHWSBeauty2Charm

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Code            | ALL                                                                              |
| Inputs          | [ 'Phys/D2HHWSMinusBeauty2CharmFilter' , 'Phys/D2HHWSPlusBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                             |
| Output          | Phys/D2HHWSBeauty2Charm/Particles                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

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

CombineParticles/X2PiPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/HHPionsInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                       |
| CombinationCut   | (ASUM(PT)\>1000\*MeV) & (AM \< 5.2\*GeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<16) & (BPVVDCHI2\>16) & (BPVDIRA\>0)                                                                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                                                                                        |
| Output           | Phys/X2PiPiBeauty2Charm/Particles                                                                                                                                                                                                                                    |

SubstitutePID/X2KKBeauty2CharmSel

|                 |                                                                                    |
|-----------------|------------------------------------------------------------------------------------|
| Code            | DECTREE('X0 -\> X+ X-')                                                            |
| Inputs          | [ 'Phys/X2PiPiBeauty2Charm' ]                                                    |
| DecayDescriptor | None                                                                               |
| Output          | Phys/X2KKBeauty2CharmSel/Particles                                                 |
| Substitutions   | { 'X0 -\> X+ X-' : 'phi(1020)' , 'X0 -\> X+ ^X-' : 'K-' , 'X0 -\> ^X+ X-' : 'K+' } |

FilterDesktop/X2KKBeauty2CharmFilter

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | INTREE(ID=='phi(1020)') & INTREE(ID=='K+') & INTREE(ID=='K-') |
| Inputs          | [ 'Phys/X2KKBeauty2CharmSel' ]                              |
| DecayDescriptor | None                                                          |
| Output          | Phys/X2KKBeauty2CharmFilter/Particles                         |

CombineParticles/B02D0KKD2HHWSBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2HHWSBeauty2Charm' , 'Phys/X2KKBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'phi(1020)' : 'ALL' }                                                                                                                                                                                                                                                                                                                                      |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ 'B0 -\> D0 phi(1020)' ]                                                                                                                                                                                                                                                                                                                                                                              |
| Output           | Phys/B02D0KKD2HHWSBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                 |

TisTosParticleTagger/B02D0KKD2HHWSBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02D0KKD2HHWSBeauty2Charm' ]                                                                                                |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B02D0KKD2HHWSBeauty2CharmTISTOS/Particles                                                                                        |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B02D0KKD2HHWSBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                   |
| Inputs          | [ 'Phys/B02D0KKD2HHWSBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                              |
| Output          | Phys/B02D0KKD2HHWSBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B02D0KKD2HHWSBeauty2CharmLine

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Code            | ALL                                                             |
| Inputs          | [ 'Phys/B02D0KKD2HHWSBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                            |
| Output          | Phys/B02D0KKD2HHWSBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B02D0KKD2HHWSBeauty2CharmLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B02D0KKD2HHWSBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo1_B02D0KKD2HHWSBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B02D0KKD2HHWSBeauty2CharmLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B02D0KKD2HHWSBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo2_B02D0KKD2HHWSBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B02D0KKD2HHWSBeauty2CharmLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/B02D0KKD2HHWSBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                      |
| Output          | Phys/RelatedInfo3_B02D0KKD2HHWSBeauty2CharmLine/Particles |
