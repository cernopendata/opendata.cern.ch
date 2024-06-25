[[stripping21r1 lines]](./stripping21r1-index)

# StrippingX02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine/Particles                      |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 0.10000000                                                                   |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingX02XiccpPiWSXiccp2Xic0PiBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

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

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsProtons](./stripping21r1-commonparticles-stdallnopidsprotons)/Particles')\>0 |

FilterDesktop/PInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21r1-commonparticles-stdallnopidsprotons)' ]       |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/PInputsBeauty2CharmFilter/Particles                                                      |

CombineParticles/Xic02PKKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                        |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Xi_c0') \< 110\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (ADMASS('Xi_c0') \< 100\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Xi_c0 -\> p+ K- K- pi+]cc' ]                                                                                                                                                                                                                                               |
| Output           | Phys/Xic02PKKPiBeauty2Charm/Particles                                                                                                                                                                                                                                              |

CombineParticles/Xiccp2Xic0PiXic02PKKPiPBeauty2Charm

|                  |                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' , 'Phys/Xic02PKKPiBeauty2Charm' ]                                  |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c0' : 'ALL' , 'Xi_c~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                      |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Xi_cc+') \< 510\*MeV) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (ADMASS('Xi_cc+') \< 500\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)               |
| DecayDescriptor  | None                                                                                                     |
| DecayDescriptors | [ '[Xi_cc+ -\> Xi_c0 pi+]cc' ]                                                                       |
| Output           | Phys/Xiccp2Xic0PiXic02PKKPiPBeauty2Charm/Particles                                                       |

CombineParticles/X02XiccpPiWSXiccp2Xic0PiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiInputsBeauty2CharmFilter' , 'Phys/Xiccp2Xic0PiXic02PKKPiPBeauty2Charm' ]                                                                                                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_cc+' : 'ALL' , 'Xi_cc~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                                    |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>5200\*MeV)                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[B0 -\> Xi_cc+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                                      |

TisTosParticleTagger/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2Charm' ]                                                                                     |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmTISTOS/Particles                                                                             |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                              |
|-----------------|------------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                              |
| Inputs          | [ 'Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                         |
| Output          | Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Code            | ALL                                                                        |
| Inputs          | [ 'Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                       |
| Output          | Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine

|                 |                                                                      |
|-----------------|----------------------------------------------------------------------|
| Inputs          | [ 'Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                 |
| Output          | Phys/RelatedInfo1_X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine

|                 |                                                                      |
|-----------------|----------------------------------------------------------------------|
| Inputs          | [ 'Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                 |
| Output          | Phys/RelatedInfo2_X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine

|                 |                                                                      |
|-----------------|----------------------------------------------------------------------|
| Inputs          | [ 'Phys/X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                 |
| Output          | Phys/RelatedInfo3_X02XiccpPiWSXiccp2Xic0PiBeauty2CharmLine/Particles |
