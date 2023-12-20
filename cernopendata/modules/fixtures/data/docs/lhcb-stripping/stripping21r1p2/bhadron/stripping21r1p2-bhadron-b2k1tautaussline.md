[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2K1TauTauSSLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/B2K1TauTauSSLine/Particles |
| Postscale      | 1.0000000                       |
| HLT1           | None                            |
| HLT2           | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2K1TauTauSSLineVOIDFilter

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdTightDetachedTau3pi

|      |                                          |
|------|------------------------------------------|
| Code | 0StdTightDetachedTau3pi/Particles',True) |

FilterDesktop/TauB2XTauTau

|                 |                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------|
| Code            | (M \< 1800.0)                                                                                   |
| Inputs          | [ 'Phys/[StdTightDetachedTau3pi](./stripping21r1p2-commonparticles-stdtightdetachedtau3pi)' ] |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/TauB2XTauTau/Particles                                                                     |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

FilterDesktop/TracksB2XTauTau

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 6) & (TRGHOSTPROB \< 0.5)            |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r1p2-commonparticles-stdnopidspions)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/TracksB2XTauTau/Particles                                                  |

DaVinci::N3BodyDecays/K1B2XTauTau_K1

|                  |                                                |
|------------------|------------------------------------------------|
| Inputs           | [ 'Phys/TracksB2XTauTau' ]                   |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | in_range ( 400.0, AM, 1700.0 )                 |
| MotherCut        | (PT \> 800.0) & (VFASPF(VCHI2) \< 9)           |
| DecayDescriptor  | None                                           |
| DecayDescriptors | [ '[K_1(1270)+ -\> pi+ pi- pi+]cc' ]       |
| Output           | Phys/K1B2XTauTau_K1/Particles                  |

DaVinci::N3BodyDecays/B2K1TauTauSSLine

|                  |                                                                                                |
|------------------|------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K1B2XTauTau_K1' , 'Phys/TauB2XTauTau' ]                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K_1(1270)+' : 'ALL' , 'K_1(1270)-' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' } |
| CombinationCut   | in_range ( 2000.0, AM, 6000.0 )                                                                |
| MotherCut        | ( BPVVDCHI2 \> 16 ) & ( BPVVD \< 100 ) & (PT \> 2000.0) & (P \> 10000.0)                       |
| DecayDescriptor  | None                                                                                           |
| DecayDescriptors | [ '[B+ -\> K_1(1270)- tau+ tau+]cc' , '[B+ -\> K_1(1270)+ tau+ tau+]cc' ]                |
| Output           | Phys/B2K1TauTauSSLine/Particles                                                                |

AddRelatedInfo/RelatedInfo1_B2K1TauTauSSLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2K1TauTauSSLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_B2K1TauTauSSLine/Particles |

AddRelatedInfo/RelatedInfo2_B2K1TauTauSSLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2K1TauTauSSLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo2_B2K1TauTauSSLine/Particles |
