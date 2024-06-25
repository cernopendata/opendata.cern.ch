[[stripping21 lines]](./stripping21-index)

# StrippingLowMultCEP_PHI2KK_line

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/LowMultCEP_PHI2KK_line/Particles                  |
| Postscale      | 1.0000000                                              |
| HLT            | HLT_PASS_RE('Hlt2LowMult(D.\*\|C.\*\|Hadron)Decision') |
| Prescale       | 1.0000000                                              |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

**LoKi::VoidFilter/StrippingLowMultCEP_PHI2KK_lineVOIDFilter**

|      |                                                                                                                                                                    |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \> 1) & (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) & (CONTAINS ('Rec/Track/Best') \< 8) |

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

**CombineParticles/LowMultCEP_PHI2KK_line**

|                  |                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForLowMult' ]                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                     |
| CombinationCut   | (APT \> 0.0) & (APT \< 1500.0) & (AM \> 990.0) & (AM \< 1050.0) & (ADOCAMAX('LoKi::DistanceCalculator') \< 0.1) & (AP \> 4000.0) |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 3.0)                                                                                                       |
| DecayDescriptor  | None                                                                                                                             |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                      |
| Output           | Phys/LowMultCEP_PHI2KK_line/Particles                                                                                            |
