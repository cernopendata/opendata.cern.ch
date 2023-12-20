[[stripping21 lines]](./stripping21-index)

# StrippingDstarUPB02DPiD2PhiMuNuBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/DstarUPB02DPiD2PhiMuNuBeauty2CharmLine/Particles                        |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingDstarUPB02DPiD2PhiMuNuBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsUpPions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)/Particles')\>0 |

FilterDesktop/PiUPInputsBeauty2CharmFilter

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<4.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0)  |
| Inputs          | [ 'Phys/[StdNoPIDsUpPions](./stripping21-commonparticles-stdnopidsuppions)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/PiUPInputsBeauty2CharmFilter/Particles                                     |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/KInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' ]             |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/KInputsBeauty2CharmFilter/Particles                                                      |

CombineParticles/PHI2KK4D2PhiMuNuBeauty2Charm

|                  |                                                              |
|------------------|--------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' ]                       |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PIDK\>-10)' , 'K-' : '(PIDK\>-10)' } |
| CombinationCut   | ADAMASS('phi(1020)') \< 150\*MeV                             |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10)                                   |
| DecayDescriptor  | None                                                         |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                  |
| Output           | Phys/PHI2KK4D2PhiMuNuBeauty2Charm/Particles                  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MUInputsBeauty2CharmFilter

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF\<3.0) & (PT\>100\*MeV) & (P\>1000\*MeV) & (MIPCHI2DV(PRIMARY)\>4.0) & (TRGHP\<0.4) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                     |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/MUInputsBeauty2CharmFilter/Particles                                                     |

CombineParticles/ProtoD2PhiMuNuBeauty2Charm

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MUInputsBeauty2CharmFilter' , 'Phys/PHI2KK4D2PhiMuNuBeauty2Charm' ] |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'phi(1020)' : 'ALL' }          |
| CombinationCut   | ATRUE                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (MM \< 2168.49)                                    |
| DecayDescriptor  | None                                                                          |
| DecayDescriptors | [ '[D+ -\> phi(1020) mu+]cc' ]                                            |
| Output           | Phys/ProtoD2PhiMuNuBeauty2Charm/Particles                                     |

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

FilterDesktop/PiTopoInputsBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/PiInputsBeauty2CharmFilter' ]                           |
| DecayDescriptor | None                                                              |
| Output          | Phys/PiTopoInputsBeauty2CharmFilter/Particles                     |

CombineParticles/B02DPiD2PhiMuNuBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiTopoInputsBeauty2CharmFilter' , 'Phys/ProtoD2PhiMuNuBeauty2Charm' ]                                                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                                                         |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>4000\*MeV) & (AM\>4000\*MeV) & (AM\<6000\*MeV)                                                                                                                                                                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[B0 -\> D- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/B02DPiD2PhiMuNuBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                           |

TisTosParticleTagger/B02DPiD2PhiMuNuBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DPiD2PhiMuNuBeauty2Charm' ]                                                                                              |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B02DPiD2PhiMuNuBeauty2CharmTISTOS/Particles                                                                                      |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                     |
| Inputs          | [ 'Phys/B02DPiD2PhiMuNuBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                |
| Output          | Phys/B02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

SubstitutePID/B02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | DECTREE('Beauty -\> Charm ...')                                               |
| Inputs          | [ 'Phys/B02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilter' ]             |
| DecayDescriptor | None                                                                          |
| Output          | Phys/B02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel/Particles |
| Substitutions   | { 'Beauty -\> Charm ...' : 'J/psi(1S)' }                                      |

FilterDesktop/B02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter

|                 |                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------|
| Code            | INTREE(ID=='J/psi(1S)')                                                                            |
| Inputs          | [ 'Phys/B02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPSel' ]                        |
| DecayDescriptor | None                                                                                               |
| Output          | Phys/B02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter/Particles |

CombineParticles/DstarUPB02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilter

|                  |                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilterDstarUPFilterBeauty2CharmFilter' , 'Phys/PiUPInputsBeauty2CharmFilter' ]                        |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                          |
| CombinationCut   | (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) & ((((IDD1==421)\|(IDD1==411)) & ((MD1PI-MD1) \< 180)) \| (((IDD2==421)\|(IDD2==411)) & ((MD2PI-MD2) \< 180))) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVDIRA\>0.999)                                                                                                                   |
| DecayDescriptor  | [B+ -\> J/psi(1S) pi+]cc                                                                                                                                    |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) pi+]cc' ]                                                                                                                            |
| Output           | Phys/DstarUPB02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles                                                                                    |

FilterDesktop/DstarUPB02DPiD2PhiMuNuBeauty2CharmLine

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Code            | ALL                                                                      |
| Inputs          | [ 'Phys/DstarUPB02DPiD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                     |
| Output          | Phys/DstarUPB02DPiD2PhiMuNuBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_DstarUPB02DPiD2PhiMuNuBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB02DPiD2PhiMuNuBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                               |
| Output          | Phys/RelatedInfo1_DstarUPB02DPiD2PhiMuNuBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_DstarUPB02DPiD2PhiMuNuBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB02DPiD2PhiMuNuBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                               |
| Output          | Phys/RelatedInfo2_DstarUPB02DPiD2PhiMuNuBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_DstarUPB02DPiD2PhiMuNuBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Inputs          | [ 'Phys/DstarUPB02DPiD2PhiMuNuBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                               |
| Output          | Phys/RelatedInfo3_DstarUPB02DPiD2PhiMuNuBeauty2CharmLine/Particles |
