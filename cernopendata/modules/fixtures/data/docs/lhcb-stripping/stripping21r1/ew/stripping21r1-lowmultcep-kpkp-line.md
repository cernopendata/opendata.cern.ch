[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLowMultCEP_KpKp_line

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/LowMultCEP_KpKp_line/Particles                    |
| Postscale      | 1.0000000                                              |
| HLT            | HLT_PASS_RE('Hlt2LowMult(D.\*\|C.\*\|Hadron)Decision') |
| Prescale       | 0.10000000                                             |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

**LoKi::VoidFilter/StrippingLowMultCEP_KpKp_lineVOIDFilter**

|      |                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \> 1) & (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) & (CONTAINS ('Rec/Track/Best') \< 12) |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsKaons](./stripping21r1-stdallnopidskaons) /Particles')\>0 |

**FilterDesktop/KaonsForKKForLowMult**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (PT \> 100.0) & (P \> 10000.0) & (TRCHI2DOF \< 3.0) & (PIDK \> 5.0)   |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21r1-stdallnopidskaons) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/KaonsForKKForLowMult/Particles                                   |

**CombineParticles/LowMultCEP_KpKp_line**

|                  |                                              |
|------------------|----------------------------------------------|
| Inputs           | [ 'Phys/KaonsForKKForLowMult' ]            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' } |
| CombinationCut   | AALL                                         |
| MotherCut        | ALL                                          |
| DecayDescriptor  | None                                         |
| DecayDescriptors | [ '[D0 -\> K+ K+]cc' ]                   |
| Output           | Phys/LowMultCEP_KpKp_line/Particles          |
