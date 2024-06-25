[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingXib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine

## Properties:

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| OutputLocation | Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine/Particles                    |
| Postscale      | 1.0000000                                                                       |
| HLT1           | None                                                                            |
| HLT2           | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2.\*IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                       |
| L0DU           | None                                                                            |
| ODIN           | None                                                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

LoKi::VoidFilter/StrippingXib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

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

DaVinci::N3BodyDecays/Xic2PKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K_PIDInputsBeauty2CharmFilter' , 'Phys/P_PIDInputsBeauty2CharmFilter' , 'Phys/Pi_PIDInputsBeauty2CharmFilter' ]                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                      |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Xi_c+') \< 110\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,3)\<0.5\*mm) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (ADMASS('Xi_c+') \< 100\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[Xi_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                                                |
| Output           | Phys/Xic2PKPiBeauty2Charm/Particles                                                                                                                                                                                                                                              |

FilterDesktop/XIC2PKPITIGHTER3PIDBeauty2CharmFilter

|                 |                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< 0),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 10), 1) == 0) |
| Inputs          | [ 'Phys/Xic2PKPiBeauty2Charm' ]                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                  |
| Output          | Phys/XIC2PKPITIGHTER3PIDBeauty2CharmFilter/Particles                                                                                                                  |

FilterDesktop/XIC2PKPITIGHTEST3PIDMWINBeauty2CharmFilter

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | ADMASS('Xi_c+') \< 50.0                                   |
| Inputs          | [ 'Phys/XIC2PKPITIGHTER3PIDBeauty2CharmFilter' ]        |
| DecayDescriptor | None                                                      |
| Output          | Phys/XIC2PKPITIGHTEST3PIDMWINBeauty2CharmFilter/Particles |

LoKi::VoidFilter/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmCombCutXIC2PKPITIGHTEST3PIDMWINBeauty2CharmFilter

|      |                                                                               |
|------|-------------------------------------------------------------------------------|
| Code | (CONTAINS('Phys/XIC2PKPITIGHTEST3PIDMWINBeauty2CharmFilter/Particles')\<2000) |

FilterDesktop/HHHPionsInputsBeauty2CharmFilter

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | (PT\>100\*MeV) & (P\>2000\*MeV) & (PIDK\<10)    |
| Inputs          | [ 'Phys/PiInputsBeauty2CharmFilter' ]         |
| DecayDescriptor | None                                            |
| Output          | Phys/HHHPionsInputsBeauty2CharmFilter/Particles |

DaVinci::N3BodyDecays/X2PiPiPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/HHHPionsInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                       |
| CombinationCut   | (ASUM(PT)\>1250\*MeV) & (AM \< 3500\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,3)\<0.40\*mm) & (ADOCA(2,3)\<0.40\*mm) & (ANUM(PT \< 300\*MeV) \<= 1) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<8) & (BPVVDCHI2\>16) & (BPVDIRA\>0.98) & (MIPCHI2DV(PRIMARY)\>0.0) & (BPVVDRHO\>0.1\*mm) & (BPVVDZ\>2.0\*mm)                                                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[a_1(1260)+ -\> pi+ pi- pi+]cc' ]                                                                                                                                                                                                                                                             |
| Output           | Phys/X2PiPiPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                  |

FilterDesktop/X2PiPiPiPIDTIGHTERPIBeauty2CharmFilter

|                 |                                                                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 8), 1) == 0) |
| Inputs          | [ 'Phys/X2PiPiPiBeauty2Charm' ]                                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                                   |
| Output          | Phys/X2PiPiPiPIDTIGHTERPIBeauty2CharmFilter/Particles                                                                                                                  |

FilterDesktop/X2PiPiPiPIDTIGHTER3PISELBeauty2CharmFilter

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY)\>20) & (M\<2800)                      |
| Inputs          | [ 'Phys/X2PiPiPiPIDTIGHTERPIBeauty2CharmFilter' ]       |
| DecayDescriptor | None                                                      |
| Output          | Phys/X2PiPiPiPIDTIGHTER3PISELBeauty2CharmFilter/Particles |

LoKi::VoidFilter/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmCombCutX2PiPiPiPIDTIGHTER3PISELBeauty2CharmFilter

|      |                                                                               |
|------|-------------------------------------------------------------------------------|
| Code | (CONTAINS('Phys/X2PiPiPiPIDTIGHTER3PISELBeauty2CharmFilter/Particles')\<2000) |

CombineParticles/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/X2PiPiPiPIDTIGHTER3PISELBeauty2CharmFilter' , 'Phys/XIC2PKPITIGHTEST3PIDMWINBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c+' : 'ALL' , 'Xi_c~-' : 'ALL' , 'a_1(1260)+' : 'ALL' , 'a_1(1260)-' : 'ALL' }                                                                                                                                                                                                                                                                                                      |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>5200\*MeV)                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<4.) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[Xi_b0 -\> Xi_c+ a_1(1260)-]cc' ]                                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                               |

TisTosParticleTagger/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmTISTOS

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2Charm' ]                                                                                      |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmTISTOS/Particles                                                                              |
| TisTosSpecs     | { 'Hlt2.\*IncPhi.\*Decision%TIS' : 0 , 'Hlt2.\*IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                                   |
| Inputs          | [ 'Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                              |
| Output          | Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | ALL                                                                             |
| Inputs          | [ 'Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                      |
| Output          | Phys/RelatedInfo1_Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                      |
| Output          | Phys/RelatedInfo2_Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                      |
| Output          | Phys/RelatedInfo3_Xib02XicPiPiPiXic2PKPiFullDSTBeauty2CharmLine/Particles |
