[[stripping21 lines]](./stripping21-index)

# StrippingLowMultCEP_ChiC2PPWS_line

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/LowMultCEP_ChiC2PPWS_line/Particles               |
| Postscale      | 1.0000000                                              |
| HLT            | HLT_PASS_RE('Hlt2LowMult(D.\*\|C.\*\|Hadron)Decision') |
| Prescale       | 0.10000000                                             |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

**LoKi::VoidFilter/StrippingLowMultCEP_ChiC2PPWS_lineVOIDFilter**

|      |                                                                                                                                                                    |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \> 1) & (recSummaryTrack(LHCb.RecSummary.nBackTracks, TrBACKWARD) \< 1) & (CONTAINS ('Rec/Track/Best') \< 6) |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles**

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsProtons](./stripping21-stdallnopidsprotons) /Particles')\>0 |

**FilterDesktop/ProtonsForLowMult**

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | (PT \> 100.0) & (P \> 5000.0) & (TRCHI2DOF \< 3.0) & (PIDp \> 0.0)      |
| Inputs          | [ 'Phys/ [StdAllNoPIDsProtons](./stripping21-stdallnopidsprotons) ' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/ProtonsForLowMult/Particles                                        |

**CombineParticles/LowMultCEP_ChiC2PPWS_line**

|                  |                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ProtonsForLowMult' ]                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'p\~-' : 'ALL' }                                                                                     |
| CombinationCut   | (APT \> 0.0) & (APT \< 5000.0) & (AM \> 2850.0) & (AM \< 3650.0) & (ADOCAMAX('LoKi::DistanceCalculator') \< 0.5) & (AP \> 10000.0) |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 15.0)                                                                                                        |
| DecayDescriptor  | None                                                                                                                               |
| DecayDescriptors | [ '[chi_c1(1P) -\> p+ p+]cc' ]                                                                                                 |
| Output           | Phys/LowMultCEP_ChiC2PPWS_line/Particles                                                                                           |
