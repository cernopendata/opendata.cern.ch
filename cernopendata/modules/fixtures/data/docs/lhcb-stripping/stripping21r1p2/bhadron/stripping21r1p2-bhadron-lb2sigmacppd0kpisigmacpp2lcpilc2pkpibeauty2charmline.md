[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine

## Properties:

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| OutputLocation | Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine/Particles             |
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

LoKi::VoidFilter/StrippingLb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLineVOIDFilter

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

FilterDesktop/D2KPIPIDBeauty2CharmFilter

|                 |                                           |
|-----------------|-------------------------------------------|
| Code            | NINTREE(ABSID=='K+') == 1                 |
| Inputs          | [ 'Phys/D2HHPIDBeauty2CharmFilter' ]    |
| DecayDescriptor | None                                      |
| Output          | Phys/D2KPIPIDBeauty2CharmFilter/Particles |

LoKi::VoidFilter/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmCombCutD2KPIPIDBeauty2CharmFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (CONTAINS('Phys/D2KPIPIDBeauty2CharmFilter/Particles')\<2000) |

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

FilterDesktop/Pi_PIDInputsBeauty2CharmFilter

|                 |                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (PIDK\<20.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/PiInputsBeauty2CharmFilter' ]                                                                      |
| DecayDescriptor | None                                                                                                         |
| Output          | Phys/Pi_PIDInputsBeauty2CharmFilter/Particles                                                                |

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

FilterDesktop/K_PIDInputsBeauty2CharmFilter

|                 |                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (PIDK\>-10.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/KInputsBeauty2CharmFilter' ]                                                                        |
| DecayDescriptor | None                                                                                                          |
| Output          | Phys/K_PIDInputsBeauty2CharmFilter/Particles                                                                  |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsProtons

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllNoPIDsProtons/Particles',True) |

FilterDesktop/PInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r1p2-commonparticles-stdallnopidsprotons)' ]     |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PInputsBeauty2CharmFilter/Particles                                                      |

FilterDesktop/P_PIDInputsBeauty2CharmFilter

|                 |                                                                                                               |
|-----------------|---------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (PIDp\>-10.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/PInputsBeauty2CharmFilter' ]                                                                        |
| DecayDescriptor | None                                                                                                          |
| Output          | Phys/P_PIDInputsBeauty2CharmFilter/Particles                                                                  |

DaVinci::N3BodyDecays/Lc2PKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K_PIDInputsBeauty2CharmFilter' , 'Phys/P_PIDInputsBeauty2CharmFilter' , 'Phys/Pi_PIDInputsBeauty2CharmFilter' ]                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                          |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Lambda_c+') \< 110\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,3)\<0.5\*mm) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (ADMASS('Lambda_c+') \< 100\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                                                |
| Output           | Phys/Lc2PKPiBeauty2Charm/Particles                                                                                                                                                                                                                                                   |

CombineParticles/Sigmacpp2LcPiLc2PKPiBeauty2Charm

|                  |                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lc2PKPiBeauty2Charm' , 'Phys/Pi_PIDInputsBeauty2CharmFilter' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }   |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Sigma_c++') \< 110\*MeV) & (ADOCA(1,2)\<0.5\*mm)            |
| MotherCut        | (ADMASS('Sigma_c++') \< 100\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0) |
| DecayDescriptor  | None                                                                                          |
| DecayDescriptors | [ '[Sigma_c++ -\> Lambda_c+ pi+]cc' ]                                                     |
| Output           | Phys/Sigmacpp2LcPiLc2PKPiBeauty2Charm/Particles                                               |

LoKi::VoidFilter/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmCombCutSigmacpp2LcPiLc2PKPiBeauty2Charm

|      |                                                                     |
|------|---------------------------------------------------------------------|
| Code | (CONTAINS('Phys/Sigmacpp2LcPiLc2PKPiBeauty2Charm/Particles')\<2000) |

LoKi::VoidFilter/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmCombCutPiInputsBeauty2CharmFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (CONTAINS('Phys/PiInputsBeauty2CharmFilter/Particles')\<2000) |

LoKi::VoidFilter/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmCombCutKInputsBeauty2CharmFilter

|      |                                                              |
|------|--------------------------------------------------------------|
| Code | (CONTAINS('Phys/KInputsBeauty2CharmFilter/Particles')\<2000) |

CombineParticles/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KPIPIDBeauty2CharmFilter' , 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' , 'Phys/Sigmacpp2LcPiLc2PKPiBeauty2Charm' ]                                                                                                                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Sigma_c++' : 'ALL' , 'Sigma_c~--' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                               |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6000\*MeV) & (AM\>4900\*MeV)                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<4.) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ 'Lambda_b0 -\> Sigma_c++ D0 K- pi-' , 'Lambda_b~0 -\> Sigma_c~-- D0 K+ pi+' ]                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                        |

TisTosParticleTagger/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmTISTOS

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2Charm' ]                                                                               |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmTISTOS/Particles                                                                       |
| TisTosSpecs     | { 'Hlt2.\*IncPhi.\*Decision%TIS' : 0 , 'Hlt2.\*IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                                          |
| Inputs          | [ 'Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine

|                 |                                                                                        |
|-----------------|----------------------------------------------------------------------------------------|
| Code            | ALL                                                                                    |
| Inputs          | [ 'Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                                   |
| Output          | Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                             |
| Output          | Phys/RelatedInfo1_Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                             |
| Output          | Phys/RelatedInfo2_Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine

|                 |                                                                                  |
|-----------------|----------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                             |
| Output          | Phys/RelatedInfo3_Lb2sigmacppD0KPiSigmacpp2LcPiLc2PKPiBeauty2CharmLine/Particles |
