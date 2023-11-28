[[stripping21 lines]](./stripping21-index)

# StrippingB02DKWSD2PhiMuNuBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/B02DKWSD2PhiMuNuBeauty2CharmLine/Particles                              |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 0.10000000                                                                   |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingB02DKWSD2PhiMuNuBeauty2CharmLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 500 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

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

FilterDesktop/KTopoInputsBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/KInputsBeauty2CharmFilter' ]                            |
| DecayDescriptor | None                                                              |
| Output          | Phys/KTopoInputsBeauty2CharmFilter/Particles                      |

CombineParticles/B02DKWSD2PhiMuNuBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KTopoInputsBeauty2CharmFilter' , 'Phys/ProtoD2PhiMuNuBeauty2Charm' ]                                                                                                                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                                                                           |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>4000\*MeV) & (AM\>4000\*MeV) & (AM\<6000\*MeV)                                                                                                                                                                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[B0 -\> D- K-]cc' ]                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/B02DKWSD2PhiMuNuBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                          |

TisTosParticleTagger/B02DKWSD2PhiMuNuBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DKWSD2PhiMuNuBeauty2Charm' ]                                                                                             |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/B02DKWSD2PhiMuNuBeauty2CharmTISTOS/Particles                                                                                     |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/B02DKWSD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                      |
|-----------------|----------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                      |
| Inputs          | [ 'Phys/B02DKWSD2PhiMuNuBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                 |
| Output          | Phys/B02DKWSD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/B02DKWSD2PhiMuNuBeauty2CharmLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Code            | ALL                                                                |
| Inputs          | [ 'Phys/B02DKWSD2PhiMuNuBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                               |
| Output          | Phys/B02DKWSD2PhiMuNuBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_B02DKWSD2PhiMuNuBeauty2CharmLine

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DKWSD2PhiMuNuBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                         |
| Output          | Phys/RelatedInfo1_B02DKWSD2PhiMuNuBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_B02DKWSD2PhiMuNuBeauty2CharmLine

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DKWSD2PhiMuNuBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                         |
| Output          | Phys/RelatedInfo2_B02DKWSD2PhiMuNuBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_B02DKWSD2PhiMuNuBeauty2CharmLine

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/B02DKWSD2PhiMuNuBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                         |
| Output          | Phys/RelatedInfo3_B02DKWSD2PhiMuNuBeauty2CharmLine/Particles |
