[[stripping21 lines]](./stripping21-index)

# StrippingLowMultCEP_Dstar2D0Pi_KsPiPiDD_line

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/LowMultCEP_Dstar2D0Pi_KsPiPiDD_line/Particles     |
| Postscale      | 1.0000000                                              |
| HLT            | HLT_PASS_RE('Hlt2LowMult(D.\*\|C.\*\|Hadron)Decision') |
| Prescale       | 1.0000000                                              |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

**LoKi::VoidFilter/StrippingLowMultCEP_Dstar2D0Pi_KsPiPiDD_lineVOIDFilter**

|      |                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \> 1) & (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) & (CONTAINS ('Rec/Track/Best') \< 12) |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

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

**LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles**

|      |                                                                            |
|------|----------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKsDD](./stripping21-stdlooseksdd) /Particles')\>0 |

**FilterDesktop/KsDDForLowMult**

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 50.0)                                   |
| Inputs          | [ 'Phys/ [StdLooseKsDD](./stripping21-stdlooseksdd) ' ] |
| DecayDescriptor | None                                                      |
| Output          | Phys/KsDDForLowMult/Particles                             |

**CombineParticles/selD2KsPiPiDD**

|                  |                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KsDDForLowMult' , 'Phys/PionsForLowMult' ]                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                           |
| CombinationCut   | (APT \> 0.0) & (ADAMASS('D0') \< 80.0) & (ADOCAMAX('LoKi::DistanceCalculator') \< 0.5) & (AP \> 10000.0) |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 15.0)                                                                              |
| DecayDescriptor  | None                                                                                                     |
| DecayDescriptors | [ 'D0 -\> KS0 pi+ pi-' ]                                                                               |
| Output           | Phys/selD2KsPiPiDD/Particles                                                                             |

**FilterDesktop/AllPionsForLowMult**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (PT \> 0) & (P \> 0) & (TRCHI2DOF \< 10)                            |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/AllPionsForLowMult/Particles                                   |

**CombineParticles/LowMultCEP_Dstar2D0Pi_KsPiPiDD_line**

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/AllPionsForLowMult' , 'Phys/selD2KsPiPiDD' ]                         |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D\~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (APT \> 0.0) & (ADAMASS('D\*(2010)+') \< 100.0)                                |
| MotherCut        | ((M - M1) \> 135.0) & ((M - M1) \< 200.0) & (VFASPF(VCHI2PDOF) \< 15.0)        |
| DecayDescriptor  | None                                                                           |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' , '[D\*(2010)+ -\> D\~0 pi+]cc' ]          |
| Output           | Phys/LowMultCEP_Dstar2D0Pi_KsPiPiDD_line/Particles                             |
