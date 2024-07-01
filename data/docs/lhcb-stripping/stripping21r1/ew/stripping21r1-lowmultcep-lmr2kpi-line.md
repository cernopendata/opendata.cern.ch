[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLowMultCEP_LMR2KPi_line

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/LowMultCEP_LMR2KPi_line/Particles                 |
| Postscale      | 1.0000000                                              |
| HLT            | HLT_PASS_RE('Hlt2LowMult(D.\*\|C.\*\|Hadron)Decision') |
| Prescale       | 0.20000000                                             |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

**LoKi::VoidFilter/StrippingLowMultCEP_LMR2KPi_lineVOIDFilter**

|      |                                                                                                                                                                    |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \> 1) & (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) & (CONTAINS ('Rec/Track/Best') \< 8) |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsKaons](./stripping21r1-stdallnopidskaons) /Particles')\>0 |

**FilterDesktop/KaonsForLowMult**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PT \> 100.0) & (P \> 5000.0) & (TRCHI2DOF \< 3.0) & (PIDK \> 0.0)    |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21r1-stdallnopidskaons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/KaonsForLowMult/Particles                                        |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsPions](./stripping21r1-stdallnopidspions) /Particles')\>0 |

**FilterDesktop/PionsForLowMult**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PT \> 100.0) & (P \> 5000.0) & (TRCHI2DOF \< 3.0)                    |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21r1-stdallnopidspions) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/PionsForLowMult/Particles                                        |

**CombineParticles/LowMultCEP_LMR2KPi_line**

|                  |                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForLowMult' , 'Phys/PionsForLowMult' ]                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                      |
| CombinationCut   | (APT \> 0.0) & (APT \< 1500.0) & (AM \> 450.0) & (AM \< 1700.0) & (ADOCAMAX('LoKi::DistanceCalculator') \< 0.1) & (AP \> 15000.0) |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 3.0)                                                                                                        |
| DecayDescriptor  | None                                                                                                                              |
| DecayDescriptors | [ '[phi(1020) -\> K+ pi-]cc' ]                                                                                                |
| Output           | Phys/LowMultCEP_LMR2KPi_line/Particles                                                                                            |
