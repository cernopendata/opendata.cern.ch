[[stripping21r1 lines]](./stripping21r1-index)

# StrippingSbarSCorrelationsLambdaCplusLine

## Properties:

|                |                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/SbarSCorrelationsLambdaCplusLine/Particles                                                                                                                                                                                    |
| Postscale      | 1.0000000                                                                                                                                                                                                                          |
| HLT            | HLT_PASS('Hlt1MBNoBiasDecision')\|HLT_PASS('Hlt1MBMicroBiasTStationDecision')\|HLT_PASS('Hlt1MBMicroBiasVeloDecision')\|HLT_PASS('Hlt1MBMicroBiasTStationRateLimitedDecision')\|HLT_PASS('Hlt1MBMicroBiasVeloRateLimitedDecision') |
| Prescale       | 1.0000000                                                                                                                                                                                                                          |
| L0DU           | None                                                                                                                                                                                                                               |
| ODIN           | None                                                                                                                                                                                                                               |

## Filter sequence:

**LoKi::VoidFilter/StrippingSbarSCorrelationsLambdaCplusLineVOIDFilter**

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 1000 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsPions](./stripping21r1-stdallnopidspions) /Particles')\>0 |

**FilterDesktop/PiForSbarSCorrelations**

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | ((ISLONG)&(BPVIPCHI2() \> 9)&(P \> 2000))                             |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21r1-stdallnopidspions) ' ] |
| DecayDescriptor | None                                                                  |
| Output          | Phys/PiForSbarSCorrelations/Particles                                 |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles**

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsProtons](./stripping21r1-stdallnopidsprotons) /Particles')\>0 |

**FilterDesktop/ProtonForSbarSCorrelations**

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | ((ISLONG)&(BPVIPCHI2() \> 9)&(P \> 2000))                                 |
| Inputs          | [ 'Phys/ [StdAllNoPIDsProtons](./stripping21r1-stdallnopidsprotons) ' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/ProtonForSbarSCorrelations/Particles                                 |

**CombineParticles/LambdaSbarSCorrelations**

|                  |                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiForSbarSCorrelations' , 'Phys/ProtonForSbarSCorrelations' ]                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p\~-' : 'ALL' }                                           |
| CombinationCut   | ((ADAMASS('Lambda0')\<50\*MeV))                                                                                          |
| MotherCut        | (( (CHILD(MIPDV(PRIMARY),1)\*CHILD(MIPDV(PRIMARY),2)/MIPDV(PRIMARY))\>10)&(VFASPF(VCHI2PDOF) \< 9)&( BPVIPCHI2() \< 49)) |
| DecayDescriptor  | None                                                                                                                     |
| DecayDescriptors | [ 'Lambda0 -\> p+ pi-' ]                                                                                               |
| Output           | Phys/LambdaSbarSCorrelations/Particles                                                                                   |

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

**CombineParticles/SbarSCorrelationsLambdaCplusLine**

|                  |                                                                                        |
|------------------|----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KForSbarSCorrelations' , 'Phys/LambdaSbarSCorrelations' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda\~0' : 'ALL' } |
| CombinationCut   | (AALLSAMEBPV)                                                                          |
| MotherCut        | PZ\>0                                                                                  |
| DecayDescriptor  | None                                                                                   |
| DecayDescriptors | [ 'Lambda_c+ -\> Lambda0 K+' ]                                                       |
| Output           | Phys/SbarSCorrelationsLambdaCplusLine/Particles                                        |
