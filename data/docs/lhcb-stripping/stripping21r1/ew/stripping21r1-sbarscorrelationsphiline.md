[[stripping21r1 lines]](./stripping21r1-index)

# StrippingSbarSCorrelationsPhiLine

## Properties:

|                |                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/SbarSCorrelationsPhiLine/Particles                                                                                                                                                                                            |
| Postscale      | 1.0000000                                                                                                                                                                                                                          |
| HLT            | HLT_PASS('Hlt1MBNoBiasDecision')\|HLT_PASS('Hlt1MBMicroBiasTStationDecision')\|HLT_PASS('Hlt1MBMicroBiasVeloDecision')\|HLT_PASS('Hlt1MBMicroBiasTStationRateLimitedDecision')\|HLT_PASS('Hlt1MBMicroBiasVeloRateLimitedDecision') |
| Prescale       | 0.050000000                                                                                                                                                                                                                        |
| L0DU           | None                                                                                                                                                                                                                               |
| ODIN           | None                                                                                                                                                                                                                               |

## Filter sequence:

**LoKi::VoidFilter/StrippingSbarSCorrelationsPhiLineVOIDFilter**

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 1000 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdTightKaons_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdTightKaons](./stripping21r1-stdtightkaons) /Particles')\>0 |

**FilterDesktop/KForSbarSCorrelations**

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Code            | ((ISLONG)&(P \> 5000)&(PIDK \> 8)&( (PIDK-PIDp) \> 0)&(BPVIPCHI2() \< 49)) |
| Inputs          | [ 'Phys/ [StdTightKaons](./stripping21r1-stdtightkaons) ' ]              |
| DecayDescriptor | None                                                                       |
| Output          | Phys/KForSbarSCorrelations/Particles                                       |

**CombineParticles/SbarSCorrelationsPhiLine**

|                  |                                              |
|------------------|----------------------------------------------|
| Inputs           | [ 'Phys/KForSbarSCorrelations' ]           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' } |
| CombinationCut   | (AALLSAMEBPV)                                |
| MotherCut        | PZ\>0                                        |
| DecayDescriptor  | None                                         |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                  |
| Output           | Phys/SbarSCorrelationsPhiLine/Particles      |
