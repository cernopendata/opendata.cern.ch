[[stripping21 lines]](./stripping21-index)

# StrippingLowMultCEP_Dstar2D0Pi_KPi_Dstar2D0Pi_KsPiPiLL_line

## Properties:

|                |                                                                   |
|----------------|-------------------------------------------------------------------|
| OutputLocation | Phys/LowMultCEP_Dstar2D0Pi_KPi_Dstar2D0Pi_KsPiPiLL_line/Particles |
| Postscale      | 1.0000000                                                         |
| HLT            | HLT_PASS_RE('Hlt2LowMult(D.\*\|C.\*\|Hadron)Decision')            |
| Prescale       | 1.0000000                                                         |
| L0DU           | None                                                              |
| ODIN           | None                                                              |

## Filter sequence:

**LoKi::VoidFilter/StrippingLowMultCEP_Dstar2D0Pi_KPi_Dstar2D0Pi_KsPiPiLL_lineVOIDFilter**

|      |                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \> 1) & (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) & (CONTAINS ('Rec/Track/Best') \< 12) |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsKaons](./stripping21-stdallnopidskaons) /Particles')\>0 |

**FilterDesktop/KaonsForLowMult**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (PT \> 100.0) & (P \> 5000.0) & (TRCHI2DOF \< 3.0) & (PIDK \> 0.0)  |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21-stdallnopidskaons) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/KaonsForLowMult/Particles                                      |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) /Particles')\>0 |

**FilterDesktop/PionsForLowMult**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (PT \> 100.0) & (P \> 5000.0) & (TRCHI2DOF \< 3.0)                  |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/PionsForLowMult/Particles                                      |

**CombineParticles/selD2KPi**

|                  |                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForLowMult' , 'Phys/PionsForLowMult' ]                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                             |
| CombinationCut   | (APT \> 0.0) & (ADAMASS('D0') \< 80.0) & (ADOCAMAX('LoKi::DistanceCalculator') \< 0.5) & (AP \> 10000.0) |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 15.0)                                                                              |
| DecayDescriptor  | None                                                                                                     |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                              |
| Output           | Phys/selD2KPi/Particles                                                                                  |

**FilterDesktop/AllPionsForLowMult**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (PT \> 0) & (P \> 0) & (TRCHI2DOF \< 10)                            |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/AllPionsForLowMult/Particles                                   |

**CombineParticles/selDstar2D0Pi_KPi**

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/AllPionsForLowMult' , 'Phys/selD2KPi' ]                              |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D\~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (APT \> 0.0) & (ADAMASS('D\*(2010)+') \< 100.0)                                |
| MotherCut        | ((M - M1) \> 135.0) & ((M - M1) \< 200.0) & (VFASPF(VCHI2PDOF) \< 15.0)        |
| DecayDescriptor  | None                                                                           |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' , '[D\*(2010)+ -\> D\~0 pi+]cc' ]          |
| Output           | Phys/selDstar2D0Pi_KPi/Particles                                               |

**LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles**

|      |                                                                            |
|------|----------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKsLL](./stripping21-stdlooseksll) /Particles')\>0 |

**FilterDesktop/KsLLForLowMult**

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 50.0)                                   |
| Inputs          | [ 'Phys/ [StdLooseKsLL](./stripping21-stdlooseksll) ' ] |
| DecayDescriptor | None                                                      |
| Output          | Phys/KsLLForLowMult/Particles                             |

**CombineParticles/selD2KsPiPiLL**

|                  |                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KsLLForLowMult' , 'Phys/PionsForLowMult' ]                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                           |
| CombinationCut   | (APT \> 0.0) & (ADAMASS('D0') \< 80.0) & (ADOCAMAX('LoKi::DistanceCalculator') \< 0.5) & (AP \> 10000.0) |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 15.0)                                                                              |
| DecayDescriptor  | None                                                                                                     |
| DecayDescriptors | [ 'D0 -\> KS0 pi+ pi-' ]                                                                               |
| Output           | Phys/selD2KsPiPiLL/Particles                                                                             |

**CombineParticles/selDstar2D0Pi_KsPiPiLL**

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/AllPionsForLowMult' , 'Phys/selD2KsPiPiLL' ]                         |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D\~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (APT \> 0.0) & (ADAMASS('D\*(2010)+') \< 100.0)                                |
| MotherCut        | ((M - M1) \> 135.0) & ((M - M1) \< 200.0) & (VFASPF(VCHI2PDOF) \< 15.0)        |
| DecayDescriptor  | None                                                                           |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' , '[D\*(2010)+ -\> D\~0 pi+]cc' ]          |
| Output           | Phys/selDstar2D0Pi_KsPiPiLL/Particles                                          |

**CombineParticles/LowMultCEP_Dstar2D0Pi_KPi_Dstar2D0Pi_KsPiPiLL_line**

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/selDstar2D0Pi_KPi' , 'Phys/selDstar2D0Pi_KsPiPiLL' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' }                              |
| CombinationCut   | AALL                                                                                      |
| MotherCut        | ALL                                                                                       |
| DecayDescriptor  | None                                                                                      |
| DecayDescriptors | [ 'psi(4040) -\> D\*(2010)+ D\*(2010)-' , '[psi(4040) -\> D\*(2010)+ D\*(2010)+]cc' ] |
| Output           | Phys/LowMultCEP_Dstar2D0Pi_KPi_Dstar2D0Pi_KsPiPiLL_line/Particles                         |
