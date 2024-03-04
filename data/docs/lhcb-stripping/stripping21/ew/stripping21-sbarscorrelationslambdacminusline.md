[[stripping21 lines]](./stripping21-index)

# StrippingSbarSCorrelationsLambdaCminusLine

## Properties:

|                |                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OutputLocation | Phys/SbarSCorrelationsLambdaCminusLine/Particles                                                                                                                                                                                   |
| Postscale      | 1.0000000                                                                                                                                                                                                                          |
| HLT            | HLT_PASS('Hlt1MBNoBiasDecision')\|HLT_PASS('Hlt1MBMicroBiasTStationDecision')\|HLT_PASS('Hlt1MBMicroBiasVeloDecision')\|HLT_PASS('Hlt1MBMicroBiasTStationRateLimitedDecision')\|HLT_PASS('Hlt1MBMicroBiasVeloRateLimitedDecision') |
| Prescale       | 1.0000000                                                                                                                                                                                                                          |
| L0DU           | None                                                                                                                                                                                                                               |
| ODIN           | None                                                                                                                                                                                                                               |

## Filter sequence:

**LoKi::VoidFilter/StrippingSbarSCorrelationsLambdaCminusLineVOIDFilter**

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 1000 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) /Particles')\>0 |

**FilterDesktop/PiForSbarSCorrelations**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | ((ISLONG)&(BPVIPCHI2() \> 9)&(P \> 2000))                           |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21-stdallnopidspions) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/PiForSbarSCorrelations/Particles                               |

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles**

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsProtons](./stripping21-stdallnopidsprotons) /Particles')\>0 |

**FilterDesktop/ProtonForSbarSCorrelations**

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | ((ISLONG)&(BPVIPCHI2() \> 9)&(P \> 2000))                               |
| Inputs          | [ 'Phys/ [StdAllNoPIDsProtons](./stripping21-stdallnopidsprotons) ' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/ProtonForSbarSCorrelations/Particles                               |

**CombineParticles/LambdabarSbarSCorrelations**

|                  |                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiForSbarSCorrelations' , 'Phys/ProtonForSbarSCorrelations' ]                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p\~-' : 'ALL' }                                           |
| CombinationCut   | ((ADAMASS('Lambda0')\<50\*MeV))                                                                                          |
| MotherCut        | (( (CHILD(MIPDV(PRIMARY),1)\*CHILD(MIPDV(PRIMARY),2)/MIPDV(PRIMARY))\>10)&(VFASPF(VCHI2PDOF) \< 9)&( BPVIPCHI2() \< 49)) |
| DecayDescriptor  | None                                                                                                                     |
| DecayDescriptors | [ 'Lambda\~0 -\> p\~- pi+' ]                                                                                           |
| Output           | Phys/LambdabarSbarSCorrelations/Particles                                                                                |

**LoKi::VoidFilter/SelFilterPhys_StdTightKaons_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdTightKaons](./stripping21-stdtightkaons) /Particles')\>0 |

**FilterDesktop/KForSbarSCorrelations**

|                 |                                                                            |
|-----------------|----------------------------------------------------------------------------|
| Code            | ((ISLONG)&(P \> 5000)&(PIDK \> 8)&( (PIDK-PIDp) \> 0)&(BPVIPCHI2() \< 49)) |
| Inputs          | [ 'Phys/ [StdTightKaons](./stripping21-stdtightkaons) ' ]                |
| DecayDescriptor | None                                                                       |
| Output          | Phys/KForSbarSCorrelations/Particles                                       |

**CombineParticles/SbarSCorrelationsLambdaCminusLine**

|                  |                                                                                        |
|------------------|----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KForSbarSCorrelations' , 'Phys/LambdabarSbarSCorrelations' ]                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda\~0' : 'ALL' } |
| CombinationCut   | (AALLSAMEBPV)                                                                          |
| MotherCut        | PZ\>0                                                                                  |
| DecayDescriptor  | None                                                                                   |
| DecayDescriptors | [ 'Lambda_c\~- -\> Lambda\~0 K-' ]                                                   |
| Output           | Phys/SbarSCorrelationsLambdaCminusLine/Particles                                       |
