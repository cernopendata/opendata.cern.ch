[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingOmegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine

## Properties:

|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| OutputLocation | Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine/Particles         |
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

LoKi::VoidFilter/StrippingOmegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLineVOIDFilter

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

DaVinci::N4BodyDecays/Omegac02PKKPiBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K_PIDInputsBeauty2CharmFilter' , 'Phys/P_PIDInputsBeauty2CharmFilter' , 'Phys/Pi_PIDInputsBeauty2CharmFilter' ]                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                                                 |
| CombinationCut   | (ASUM(PT)\>1800\*MeV) & (ADAMASS('Omega_c0') \< 110\*MeV) & (AHASCHILD((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000)))) & (ADOCA(1,4)\<0.5\*mm) & (ADOCA(2,4)\<0.5\*mm) & (ADOCA(3,4)\<0.5\*mm) |
| MotherCut        | (ADMASS('Omega_c0') \< 100\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0)                                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ '[Omega_c0 -\> p+ K- K- pi+]cc' ]                                                                                                                                                                                                                                                                     |
| Output           | Phys/Omegac02PKKPiBeauty2Charm/Particles                                                                                                                                                                                                                                                                    |

FilterDesktop/OMC02PKKPITIGHTER3PIDBeauty2CharmFilter

|                 |                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION(('p+'==ABSID) & (PIDp \< 0),1) == 0) & (NINGENERATION(('K+'==ABSID) & (PIDK \< -10), 1) == 0) & (NINGENERATION(('pi+'==ABSID) & (PIDK \> 10), 1) == 0) |
| Inputs          | [ 'Phys/Omegac02PKKPiBeauty2Charm' ]                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                  |
| Output          | Phys/OMC02PKKPITIGHTER3PIDBeauty2CharmFilter/Particles                                                                                                                |

FilterDesktop/OMC02PKPITIGHTER3PIDMWINBeauty2CharmFilter

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | ADMASS('Omega_c0') \< 60.0                                |
| Inputs          | [ 'Phys/OMC02PKKPITIGHTER3PIDBeauty2CharmFilter' ]      |
| DecayDescriptor | None                                                      |
| Output          | Phys/OMC02PKPITIGHTER3PIDMWINBeauty2CharmFilter/Particles |

LoKi::VoidFilter/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmCombCutOMC02PKPITIGHTER3PIDMWINBeauty2CharmFilter

|      |                                                                               |
|------|-------------------------------------------------------------------------------|
| Code | (CONTAINS('Phys/OMC02PKPITIGHTER3PIDMWINBeauty2CharmFilter/Particles')\<2000) |

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

LoKi::VoidFilter/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmCombCutX2PiPiPiPIDTIGHTER3PISELBeauty2CharmFilter

|      |                                                                               |
|------|-------------------------------------------------------------------------------|
| Code | (CONTAINS('Phys/X2PiPiPiPIDTIGHTER3PISELBeauty2CharmFilter/Particles')\<2000) |

CombineParticles/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2Charm

|                  |                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/OMC02PKPITIGHTER3PIDMWINBeauty2CharmFilter' , 'Phys/X2PiPiPiPIDTIGHTER3PISELBeauty2CharmFilter' ]                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'Omega_c0' : 'ALL' , 'Omega_c~0' : 'ALL' , 'a_1(1260)+' : 'ALL' , 'a_1(1260)-' : 'ALL' }                                                                                                                                                                                                                                                                                                |
| CombinationCut   | (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>5000\*MeV) & (AM\<7000\*MeV) & (AM\>5200\*MeV)                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (INTREE(HASTRACK & (P\>10000\*MeV) & (PT\>1700\*MeV) & (TRCHI2DOF\<4.) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (NINTREE((ISBASIC & HASTRACK & (TRCHI2DOF\<4.) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV) & (BPVVDCHI2 \> 1000))) \> 1) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<25) & (BPVDIRA\>0.999) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[Omega_b- -\> Omega_c0 a_1(1260)-]cc' ]                                                                                                                                                                                                                                                                                                                                                         |
| Output           | Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2Charm/Particles                                                                                                                                                                                                                                                                                                                                    |

TisTosParticleTagger/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmTISTOS

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2Charm' ]                                                                           |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmTISTOS/Particles                                                                   |
| TisTosSpecs     | { 'Hlt2.\*IncPhi.\*Decision%TIS' : 0 , 'Hlt2.\*IncPhi.\*Decision%TOS' : 0 , 'Hlt2Topo.\*Decision%TIS' : 0 , 'Hlt2Topo.\*Decision%TOS' : 0 } |

FilterDesktop/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmB2CBBDTBeauty2CharmFilter

|                 |                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------|
| Code            | FILTER('BBDecTreeTool/B2CBBDT')                                                              |
| Inputs          | [ 'Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmTISTOS' ]                      |
| DecayDescriptor | None                                                                                         |
| Output          | Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmB2CBBDTBeauty2CharmFilter/Particles |

FilterDesktop/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                        |
| Inputs          | [ 'Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmB2CBBDTBeauty2CharmFilter' ] |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine/Particles                    |

AddRelatedInfo/RelatedInfo1_Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/RelatedInfo1_Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo2_Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/RelatedInfo2_Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine/Particles |

AddRelatedInfo/RelatedInfo3_Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine' ]                |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/RelatedInfo3_Omegab2Omegac0PiPiPiOmegac02PKKPiFullDSTBeauty2CharmLine/Particles |
