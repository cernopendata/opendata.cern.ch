[[stripping21r1 lines]](./stripping21r1-index)

# StrippingOmegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine

## Properties:

|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| OutputLocation | Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine/Particles             |
| Postscale      | 1.0000000                                                                    |
| HLT            | (HLT_PASS_RE('Hlt2Topo.\*Decision') \| HLT_PASS_RE('Hlt2IncPhi.\*Decision')) |
| Prescale       | 1.0000000                                                                    |
| L0DU           | None                                                                         |
| ODIN           | None                                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingOmegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLineVOIDFilter

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

CombineParticles/Omegac02PKKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KInputsBeauty2CharmFilter' , 'Phys/PInputsBeauty2CharmFilter' , 'Phys/PiInputsBeauty2CharmFilter' ]                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                           |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Omega_c0') \< 110\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator')) |
| MotherCut        | (ADMASS('Omega_c0') \< 100\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[Omega_c0 -\> p+ K- K- pi+]cc' ]                                                                                                                                                                                                                                               |
| Output           | Phys/Omegac02PKKPiBeauty2Charm/Particles                                                                                                                                                                                                                                              |

FilterDesktop/Omegac02pKKPiPIDBeauty2CharmFilter

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< -10),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 20), 1) == 0) |
| Inputs          | [ 'Phys/Omegac02PKKPiBeauty2Charm' ]                                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/Omegac02pKKPiPIDBeauty2CharmFilter/Particles                                                                                                                       |

FilterDesktop/PiTopoInputsBeauty2CharmFilter

|                 |                                                                   |
|-----------------|-------------------------------------------------------------------|
| Code            | HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV) |
| Inputs          | [ 'Phys/PiInputsBeauty2CharmFilter' ]                           |
| DecayDescriptor | None                                                              |
| Output          | Phys/PiTopoInputsBeauty2CharmFilter/Particles                     |

CombineParticles/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Omegac02pKKPiPIDBeauty2CharmFilter' , 'Phys/PiTopoInputsBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'Omega_c0' : 'ALL' , 'Omega_c~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                                         |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<6000\*MeV) & (AM\>5200\*MeV)                                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<2.5) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptors | [ '[Omega_b- -\> Omega_c0 pi-]cc' ]                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                      |

TisTosParticleTagger/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmTISTOS

|                 |                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2Charm' ]                                                                            |
| DecayDescriptor | None                                                                                                                                  |
| Output          | Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmTISTOS/Particles                                                                    |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                                       |
| Inputs          | [ 'Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | ALL                                                                                 |
| Inputs          | [ 'Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                          |
| Output          | Phys/RelatedInfo1_Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                          |
| Output          | Phys/RelatedInfo2_Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                          |
| Output          | Phys/RelatedInfo3_Omegab2Omegac0PiNoIPOmegac02PKKPiBeauty2CharmLine/Particles |
