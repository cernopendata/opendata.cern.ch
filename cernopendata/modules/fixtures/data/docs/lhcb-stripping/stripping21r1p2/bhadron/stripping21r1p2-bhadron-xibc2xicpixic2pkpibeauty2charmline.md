[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingXibc2XicPiXic2PKPiBeauty2CharmLine

## Properties:

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| OutputLocation | Phys/Xibc2XicPiXic2PKPiBeauty2CharmLine/Particles                               |
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

LoKi::VoidFilter/StrippingXibc2XicPiXic2PKPiBeauty2CharmLineVOIDFilter

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

FilterDesktop/Pi_Xc_XibcInputsBeauty2CharmFilter

|                 |                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>1.0) & (PIDK\<10.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]                        |
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
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' ]                        |
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
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r1p2-commonparticles-stdallnopidsprotons)' ]                    |
| DecayDescriptor | None                                                                                                         |
| Output          | Phys/P_Xc_XibcInputsBeauty2CharmFilter/Particles                                                             |

DaVinci::N3BodyDecays/LooseXic2PKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K_Xc_XibcInputsBeauty2CharmFilter' , 'Phys/P_Xc_XibcInputsBeauty2CharmFilter' , 'Phys/Pi_Xc_XibcInputsBeauty2CharmFilter' ]                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                                                           |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Xi_c+') \< 60\*MeV) & (ANUM(MIPCHI2DV(PRIMARY)\>4) \>= 2) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,3)\<0.5\*mm) & (ADOCA(2,3)\<0.5\*mm) |
| MotherCut        | (ADMASS('Xi_c+') \< 50\*MeV) & (VFASPF(VCHI2/VDOF)\<8) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[Xi_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                                                                                     |
| Output           | Phys/LooseXic2PKPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                              |

LoKi::VoidFilter/Xibc2XicPiXic2PKPiBeauty2CharmCombCutLooseXic2PKPiBeauty2Charm

|      |                                                              |
|------|--------------------------------------------------------------|
| Code | (CONTAINS('Phys/LooseXic2PKPiBeauty2Charm/Particles')\<2000) |

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

FilterDesktop/Pi_PIDTopoInputsBeauty2CharmFilter

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/Pi_PIDInputsBeauty2CharmFilter' ]                      |
| DecayDescriptor | None                                                             |
| Output          | Phys/Pi_PIDTopoInputsBeauty2CharmFilter/Particles                |

LoKi::VoidFilter/Xibc2XicPiXic2PKPiBeauty2CharmCombCutPi_PIDTopoInputsBeauty2CharmFilter

|      |                                                                       |
|------|-----------------------------------------------------------------------|
| Code | (CONTAINS('Phys/Pi_PIDTopoInputsBeauty2CharmFilter/Particles')\<2000) |

CombineParticles/Xibc2XicPiXic2PKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LooseXic2PKPiBeauty2Charm' , 'Phys/Pi_PIDTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c+' : 'ALL' , 'Xi_c~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                   |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<9000\*MeV) & (AM\>5500\*MeV)                                                                                                                                                                                                                                                                                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<8) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<4.) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.05\*ps) & (BPVIPCHI2()\<20) & (BPVDIRA\>0.99) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[Xi_bc0 -\> Xi_c+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/Xibc2XicPiXic2PKPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                         |

TisTosParticleTagger/Xibc2XicPiXic2PKPiBeauty2CharmTISTOS

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Xibc2XicPiXic2PKPiBeauty2Charm' ]                                                                                                 |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/Xibc2XicPiXic2PKPiBeauty2CharmTISTOS/Particles                                                                                         |
| TisTosSpecs     | { 'Hlt2.\*IncPhi.\*Decision%TIS' : 0 , 'Hlt2.\*IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/Xibc2XicPiXic2PKPiBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                        |
|-----------------|------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                        |
| Inputs          | [ 'Phys/Xibc2XicPiXic2PKPiBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                   |
| Output          | Phys/Xibc2XicPiXic2PKPiBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/Xibc2XicPiXic2PKPiBeauty2CharmLine

|                 |                                                                      |
|-----------------|----------------------------------------------------------------------|
| Code            | ALL                                                                  |
| Inputs          | [ 'Phys/Xibc2XicPiXic2PKPiBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                 |
| Output          | Phys/Xibc2XicPiXic2PKPiBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_Xibc2XicPiXic2PKPiBeauty2CharmLine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/Xibc2XicPiXic2PKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo1_Xibc2XicPiXic2PKPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_Xibc2XicPiXic2PKPiBeauty2CharmLine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/Xibc2XicPiXic2PKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo2_Xibc2XicPiXic2PKPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_Xibc2XicPiXic2PKPiBeauty2CharmLine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/Xibc2XicPiXic2PKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo3_Xibc2XicPiXic2PKPiBeauty2CharmLine/Particles |
