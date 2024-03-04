[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB02LcpbarKSWSLLLc2PKPiBeauty2CharmLine

## Properties:

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| OutputLocation | Phys/B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine/Particles                           |
| Postscale      | 1.0000000                                                                       |
| HLT1           | None                                                                            |
| HLT2           | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2.\*IncPhi.\*Decision')) |
| Prescale       | 0.10000000                                                                      |
| L0DU           | None                                                                            |
| ODIN           | None                                                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB02LcpbarKSWSLLLc2PKPiBeauty2CharmLineVOIDFilter

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
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]         |
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
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p2-commonparticles-stdallnopidskaons)' ]         |
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
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r0p2-commonparticles-stdallnopidsprotons)' ]     |
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

LoKi::VoidFilter/B02LcpbarKSWSLLLc2PKPiBeauty2CharmCombCutLc2PKPiBeauty2Charm

|      |                                                        |
|------|--------------------------------------------------------|
| Code | (CONTAINS('Phys/Lc2PKPiBeauty2Charm/Particles')\<2000) |

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/KS0_LLInputsBeauty2CharmFilter

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\>0\*MeV) & (MM\>467.\*MeV) & (MM\<527.\*MeV)                                    |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r0p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/KS0_LLInputsBeauty2CharmFilter/Particles                                       |

LoKi::VoidFilter/B02LcpbarKSWSLLLc2PKPiBeauty2CharmCombCutKS0_LLInputsBeauty2CharmFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | (CONTAINS('Phys/KS0_LLInputsBeauty2CharmFilter/Particles')\<2000) |

FilterDesktop/PTopoInputsBeauty2CharmFilter

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/PInputsBeauty2CharmFilter' ]                           |
| DecayDescriptor | None                                                             |
| Output          | Phys/PTopoInputsBeauty2CharmFilter/Particles                     |

LoKi::VoidFilter/B02LcpbarKSWSLLLc2PKPiBeauty2CharmCombCutPTopoInputsBeauty2CharmFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | (CONTAINS('Phys/PTopoInputsBeauty2CharmFilter/Particles')\<2000) |

CombineParticles/B02LcpbarKSWSLLLc2PKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0_LLInputsBeauty2CharmFilter' , 'Phys/Lc2PKPiBeauty2Charm' , 'Phys/PTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                                                                                                                                             |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6000\*MeV) & (AM\>4750.\*MeV)                                                                                                                                                                                                                                                                                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<4.) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[B0 -\> Lambda_c+ p+ KS0]cc' ]                                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/B02LcpbarKSWSLLLc2PKPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                      |

TisTosParticleTagger/B02LcpbarKSWSLLLc2PKPiBeauty2CharmTISTOS

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02LcpbarKSWSLLLc2PKPiBeauty2Charm' ]                                                                                             |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/B02LcpbarKSWSLLLc2PKPiBeauty2CharmTISTOS/Particles                                                                                     |
| TisTosSpecs     | { 'Hlt2.\*IncPhi.\*Decision%TIS' : 0 , 'Hlt2.\*IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B02LcpbarKSWSLLLc2PKPiBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                            |
| Inputs          | [ 'Phys/B02LcpbarKSWSLLLc2PKPiBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                       |
| Output          | Phys/B02LcpbarKSWSLLLc2PKPiBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Code            | ALL                                                                      |
| Inputs          | [ 'Phys/B02LcpbarKSWSLLLc2PKPiBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                     |
| Output          | Phys/B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                               |
| Output          | Phys/RelatedInfo1_B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                               |
| Output          | Phys/RelatedInfo2_B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                               |
| Output          | Phys/RelatedInfo3_B02LcpbarKSWSLLLc2PKPiBeauty2CharmLine/Particles |
