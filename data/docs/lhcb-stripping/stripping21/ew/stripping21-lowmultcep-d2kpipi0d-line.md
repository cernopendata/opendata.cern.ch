[[stripping21 lines]](./stripping21-index)

# StrippingLowMultCEP_D2KPiPi0D_line

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/LowMultCEP_D2KPiPi0D_line/Particles               |
| Postscale      | 1.0000000                                              |
| HLT            | HLT_PASS_RE('Hlt2LowMult(D.\*\|C.\*\|Hadron)Decision') |
| Prescale       | 1.0000000                                              |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

**LoKi::VoidFilter/StrippingLowMultCEP_D2KPiPi0D_lineVOIDFilter**

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

**LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseAllPhotons](./stripping21-stdlooseallphotons) /Particles')\>0 |

**FilterDesktop/GammaForLowMult**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | ALL                                                                   |
| Inputs          | [ 'Phys/ [StdLooseAllPhotons](./stripping21-stdlooseallphotons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/GammaForLowMult/Particles                                        |

**LoKi::VoidFilter/SelFilterPhys_StdDiElectronFromTracks_Particles**

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdDiElectronFromTracks](./stripping21-stddielectronfromtracks) /Particles')\>0 |

**FilterDesktop/DiElectronsForLowMult**

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | ALL                                                                             |
| Inputs          | [ 'Phys/ [StdDiElectronFromTracks](./stripping21-stddielectronfromtracks) ' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/DiElectronsForLowMult/Particles                                            |

**CombineParticles/Pi0DForLowMult**

|                  |                                                             |
|------------------|-------------------------------------------------------------|
| Inputs           | [ 'Phys/DiElectronsForLowMult' , 'Phys/GammaForLowMult' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'gamma' : 'ALL' }      |
| CombinationCut   | in_range(70.0, AM, 210.0)                                   |
| MotherCut        | ALL                                                         |
| DecayDescriptor  | None                                                        |
| DecayDescriptors | [ 'pi0 -\> J/psi(1S) gamma' ]                             |
| Output           | Phys/Pi0DForLowMult/Particles                               |

**CombineParticles/LowMultCEP_D2KPiPi0D_line**

|                  |                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForLowMult' , 'Phys/Pi0DForLowMult' , 'Phys/PionsForLowMult' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }             |
| CombinationCut   | (APT \> 0.0) & (ADAMASS('D0') \< 80.0) & (ADOCAMAX('LoKi::DistanceCalculator') \< 0.5) & (AP \> 10000.0) |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 15.0)                                                                              |
| DecayDescriptor  | None                                                                                                     |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi0]cc' ]                                                                          |
| Output           | Phys/LowMultCEP_D2KPiPi0D_line/Particles                                                                 |
