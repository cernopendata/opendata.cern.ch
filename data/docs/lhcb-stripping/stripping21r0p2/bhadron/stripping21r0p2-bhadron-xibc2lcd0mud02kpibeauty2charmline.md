[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingXibc2LcD0MuD02KPiBeauty2CharmLine

## Properties:

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| OutputLocation | Phys/Xibc2LcD0MuD02KPiBeauty2CharmLine/Particles                                |
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

LoKi::VoidFilter/StrippingXibc2LcD0MuD02KPiBeauty2CharmLineVOIDFilter

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
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]         |
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
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]         |
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
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p2-commonparticles-stdallnopidskaons)' ]         |
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
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p2-commonparticles-stdallnopidskaons)' ]         |
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
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]         |
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
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p2-commonparticles-stdallnopidskaons)' ]         |
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

FilterDesktop/D2KPIPIDBeauty2CharmFilter

|                 |                                           |
|-----------------|-------------------------------------------|
| Code            | NINTREE(ABSID=='K+') == 1                 |
| Inputs          | [ 'Phys/D2HHPIDBeauty2CharmFilter' ]    |
| DecayDescriptor | None                                      |
| Output          | Phys/D2KPIPIDBeauty2CharmFilter/Particles |

FilterDesktop/D2KPITIGHTER1PIDBeauty2CharmFilter

|                 |                                                                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< 0),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -1), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 10), 1) == 0) |
| Inputs          | [ 'Phys/D2KPIPIDBeauty2CharmFilter' ]                                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                 |
| Output          | Phys/D2KPITIGHTER1PIDBeauty2CharmFilter/Particles                                                                                                                    |

FilterDesktop/D2KPITIGHTER1PIDNARROWMWBeauty2CharmFilter

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | in_range(1824.84\*MeV,MM,1904.84\*MeV)                    |
| Inputs          | [ 'Phys/D2KPITIGHTER1PIDBeauty2CharmFilter' ]           |
| DecayDescriptor | None                                                      |
| Output          | Phys/D2KPITIGHTER1PIDNARROWMWBeauty2CharmFilter/Particles |

LoKi::VoidFilter/Xibc2LcD0MuD02KPiBeauty2CharmCombCutD2KPITIGHTER1PIDNARROWMWBeauty2CharmFilter

|      |                                                                               |
|------|-------------------------------------------------------------------------------|
| Code | (CONTAINS('Phys/D2KPITIGHTER1PIDNARROWMWBeauty2CharmFilter/Particles')\<2000) |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Pi_Xc_XibcInputsBeauty2CharmFilter

|                 |                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>1.0) & (PIDK\<10.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]                        |
| DecayDescriptor | None                                                                                                         |
| Output          | Phys/Pi_Xc_XibcInputsBeauty2CharmFilter/Particles                                                            |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

FilterDesktop/K_Xc_XibcInputsBeauty2CharmFilter

|                 |                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>150\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>1.0) & (PIDK\>-5.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p2-commonparticles-stdallnopidskaons)' ]                        |
| DecayDescriptor | None                                                                                                         |
| Output          | Phys/K_Xc_XibcInputsBeauty2CharmFilter/Particles                                                             |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsProtons

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllNoPIDsProtons/Particles',True) |

FilterDesktop/P_Xc_XibcInputsBeauty2CharmFilter

|                 |                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>400\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>1.0) & (PIDp\>-5.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r0p2-commonparticles-stdallnopidsprotons)' ]                    |
| DecayDescriptor | None                                                                                                         |
| Output          | Phys/P_Xc_XibcInputsBeauty2CharmFilter/Particles                                                             |

DaVinci::N3BodyDecays/LooseLc2PKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K_Xc_XibcInputsBeauty2CharmFilter' , 'Phys/P_Xc_XibcInputsBeauty2CharmFilter' , 'Phys/Pi_Xc_XibcInputsBeauty2CharmFilter' ]                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                                                               |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Lambda_c+') \< 60\*MeV) & (ANUM(MIPCHI2DV(PRIMARY)\>4) \>= 2) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,3)\<0.5\*mm) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (ADMASS('Lambda_c+') \< 50\*MeV) & (VFASPF(VCHI2/VDOF)\<8) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                                                                                     |
| Output           | Phys/LooseLc2PKPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                                   |

LoKi::VoidFilter/Xibc2LcD0MuD02KPiBeauty2CharmCombCutLooseLc2PKPiBeauty2Charm

|      |                                                             |
|------|-------------------------------------------------------------|
| Code | (CONTAINS('Phys/LooseLc2PKPiBeauty2Charm/Particles')\<2000) |

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

FilterDesktop/MUInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p2-commonparticles-stdloosemuons)' ]                 |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/MUInputsBeauty2CharmFilter/Particles                                                     |

LoKi::VoidFilter/Xibc2LcD0MuD02KPiBeauty2CharmCombCutMUInputsBeauty2CharmFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (CONTAINS('Phys/MUInputsBeauty2CharmFilter/Particles')\<2000) |

CombineParticles/Xibc2LcD0MuD02KPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KPITIGHTER1PIDNARROWMWBeauty2CharmFilter' , 'Phys/LooseLc2PKPiBeauty2Charm' , 'Phys/MUInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                                                                                                                                                                                             |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>4000\*MeV) & (AM\<8000\*MeV) & (AM\>3000\*MeV)                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<4.) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.0\*ps) & (BPVIPCHI2()\<200) & (BPVDIRA\>0.99) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ 'Xi_bc0 -\> Lambda_c+ D0 mu-' , 'Xi_bc0 -\> Lambda_c~- D0 mu+' ]                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/Xibc2LcD0MuD02KPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                           |

TisTosParticleTagger/Xibc2LcD0MuD02KPiBeauty2CharmTISTOS

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Xibc2LcD0MuD02KPiBeauty2Charm' ]                                                                                                  |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/Xibc2LcD0MuD02KPiBeauty2CharmTISTOS/Particles                                                                                          |
| TisTosSpecs     | { 'Hlt2.\*IncPhi.\*Decision%TIS' : 0 , 'Hlt2.\*IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/Xibc2LcD0MuD02KPiBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                       |
| Inputs          | [ 'Phys/Xibc2LcD0MuD02KPiBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                  |
| Output          | Phys/Xibc2LcD0MuD02KPiBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/Xibc2LcD0MuD02KPiBeauty2CharmLine

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | ALL                                                                 |
| Inputs          | [ 'Phys/Xibc2LcD0MuD02KPiBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/Xibc2LcD0MuD02KPiBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_Xibc2LcD0MuD02KPiBeauty2CharmLine

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Inputs          | [ 'Phys/Xibc2LcD0MuD02KPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                          |
| Output          | Phys/RelatedInfo1_Xibc2LcD0MuD02KPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_Xibc2LcD0MuD02KPiBeauty2CharmLine

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Inputs          | [ 'Phys/Xibc2LcD0MuD02KPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                          |
| Output          | Phys/RelatedInfo2_Xibc2LcD0MuD02KPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_Xibc2LcD0MuD02KPiBeauty2CharmLine

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Inputs          | [ 'Phys/Xibc2LcD0MuD02KPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                          |
| Output          | Phys/RelatedInfo3_Xibc2LcD0MuD02KPiBeauty2CharmLine/Particles |
