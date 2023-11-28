[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2DstD0KSLLBeauty2CharmLine

## Properties:

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| OutputLocation | Phys/B2DstD0KSLLBeauty2CharmLine/Particles                                      |
| Postscale      | 1.0000000                                                                       |
| HLT1           | None                                                                            |
| HLT2           | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2.\*IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                       |
| L0DU           | None                                                                            |
| ODIN           | None                                                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2DstD0KSLLBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:D2HHBeauty2Charm

GaudiSequencer/MERGEDINPUTS:D2HHBeauty2Charm

GaudiSequencer/INPUT:ProtoD2pi+pi-Beauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

CombineParticles/ProtoD2pi+pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('pi+','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'D0 -\> pi+ pi-' ]                                                                                                                                                                                                                                                           |
| Output           | Phys/ProtoD2pi+pi-Beauty2Charm/Particles                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K+pi-Beauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

CombineParticles/ProtoD2K+pi-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                    |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','pi-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D0 -\> K+ pi-' ]                                                                                                                                                                                                                                                           |
| Output           | Phys/ProtoD2K+pi-Beauty2Charm/Particles                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K+K-Beauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

CombineParticles/ProtoD2K+K-Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K+','K-'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'D0 -\> K+ K-' ]                                                                                                                                                                                                                                                           |
| Output           | Phys/ProtoD2K+K-Beauty2Charm/Particles                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:ProtoD2K-pi+Beauty2Charm

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

CombineParticles/ProtoD2K-pi+Beauty2Charm

|                  |                                                                                                                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                    |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (in_range(1764.84\*MeV,AWM('K-','pi+'),1964.84\*MeV)) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,2)\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'D0 -\> K- pi+' ]                                                                                                                                                                                                                                                           |
| Output           | Phys/ProtoD2K-pi+Beauty2Charm/Particles                                                                                                                                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHBeauty2Charm

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                         |
| Inputs          | [ 'Phys/ProtoD2K+K-Beauty2Charm' , 'Phys/ProtoD2K+pi-Beauty2Charm' , 'Phys/ProtoD2K-pi+Beauty2Charm' , 'Phys/ProtoD2pi+pi-Beauty2Charm' ] |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/D2HHBeauty2Charm/Particles                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/D2HHPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/D2HHBeauty2Charm' ]                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/D2HHPIDBeauty2CharmFilter/Particles                                                                                                                                |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/PiInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]         |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PiInputsBeauty2CharmFilter/Particles                                                     |

CombineParticles/DstarD2HHPID2D0PiBeauty2Charm

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2HHPIDBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                         |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                      |
| CombinationCut   | (ADAMASS('D\*(2010)+') \< 600\*MeV) & (ADOCA(1,2)\<0.5\*mm)                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0) & (M-MAXTREE(ABSID=='D0',M) \< 200\*MeV) |
| DecayDescriptor  | None                                                                                               |
| DecayDescriptors | [ 'D\*(2010)+ -\> pi+ D0' , 'D\*(2010)- -\> pi- D0' ]                                            |
| Output           | Phys/DstarD2HHPID2D0PiBeauty2Charm/Particles                                                       |

FilterDesktop/Dstar2D0PiPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),2) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 2) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 2) == 0) |
| Inputs          | [ 'Phys/DstarD2HHPID2D0PiBeauty2Charm' ]                                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/Dstar2D0PiPIDBeauty2CharmFilter/Particles                                                                                                                          |

LoKi::VoidFilter/B2DstD0KSLLBeauty2CharmCombCutDstar2D0PiPIDBeauty2CharmFilter

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | (CONTAINS('Phys/Dstar2D0PiPIDBeauty2CharmFilter/Particles')\<2000) |

FilterDesktop/D2HHPIDTIGHTBeauty2CharmFilter

|                 |                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -5),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -5), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 10), 1) == 0) |
| Inputs          | [ 'Phys/D2HHPIDBeauty2CharmFilter' ]                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                  |
| Output          | Phys/D2HHPIDTIGHTBeauty2CharmFilter/Particles                                                                                                                         |

LoKi::VoidFilter/B2DstD0KSLLBeauty2CharmCombCutD2HHPIDTIGHTBeauty2CharmFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | (CONTAINS('Phys/D2HHPIDTIGHTBeauty2CharmFilter/Particles')\<2000) |

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\>0\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                                    |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                                       |

LoKi::VoidFilter/B2DstD0KSLLBeauty2CharmCombCutKS0_LLInputsBeauty2CharmFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | (CONTAINS('Phys/KS0_LLInputsBeauty2CharmFilter/Particles')\<2000) |

CombineParticles/B2DstD0KSLLBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2HHPIDTIGHTBeauty2CharmFilter' , 'Phys/Dstar2D0PiPIDBeauty2CharmFilter' , 'Phys/KS0_LLInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'KS0' : 'ALL' }                                                                                                                                                                                                                                                                                            |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>4750\*MeV)                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<4.) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ 'B+ -\> D\*(2010)+ D0 KS0' , 'B- -\> D\*(2010)- D0 KS0' ]                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/B2DstD0KSLLBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                                 |

TisTosParticleTagger/B2DstD0KSLLBeauty2CharmTISTOS

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2DstD0KSLLBeauty2Charm' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/B2DstD0KSLLBeauty2CharmTISTOS/Particles                                                                                                |
| TisTosSpecs     | { 'Hlt2.\*IncPhi.\*Decision%TIS' : 0 , 'Hlt2.\*IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B2DstD0KSLLBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                 |
| Inputs          | [ 'Phys/B2DstD0KSLLBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                            |
| Output          | Phys/B2DstD0KSLLBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B2DstD0KSLLBeauty2CharmLine

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | ALL                                                           |
| Inputs          | [ 'Phys/B2DstD0KSLLBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                          |
| Output          | Phys/B2DstD0KSLLBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B2DstD0KSLLBeauty2CharmLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2DstD0KSLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo1_B2DstD0KSLLBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B2DstD0KSLLBeauty2CharmLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2DstD0KSLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo2_B2DstD0KSLLBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B2DstD0KSLLBeauty2CharmLine

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/B2DstD0KSLLBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo3_B2DstD0KSLLBeauty2CharmLine/Particles |
