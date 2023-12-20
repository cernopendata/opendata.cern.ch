[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2KTauTauLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/B2KTauTauLine/Particles |
| Postscale      | 1.0000000                    |
| HLT1           | None                         |
| HLT2           | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2KTauTauLineVOIDFilter

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
| Inputs          | [ 'Phys/[StdTightDetachedTau3pi](./stripping21r0p2-commonparticles-stdtightdetachedtau3pi)' ] |
| DecayDescriptor | None                                                                                            |
| Output          | Phys/TauB2XTauTau/Particles                                                                     |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/KaonB2XTauTau

|                 |                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 6) & (TRGHOSTPROB \< 0.5) & (PT \> 800.0) & (P \> 3000.0) & (PROBNNk\>0.2) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' ]                                         |
| DecayDescriptor | None                                                                                                                  |
| Output          | Phys/KaonB2XTauTau/Particles                                                                                          |

DaVinci::N3BodyDecays/B2KTauTauLine

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonB2XTauTau' , 'Phys/TauB2XTauTau' ]                               |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' } |
| CombinationCut   | in_range ( 3000.0, AM, 6000.0 )                                                |
| MotherCut        | ( BPVVDCHI2 \> 16 ) & ( BPVVD \< 100 ) & (PT \> 2000.0) & (P \> 10000.0)       |
| DecayDescriptor  | None                                                                           |
| DecayDescriptors | [ '[B+ -\> K+ tau+ tau-]cc' ]                                              |
| Output           | Phys/B2KTauTauLine/Particles                                                   |

AddRelatedInfo/RelatedInfo1_B2KTauTauLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/B2KTauTauLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo1_B2KTauTauLine/Particles |

AddRelatedInfo/RelatedInfo2_B2KTauTauLine

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/B2KTauTauLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo2_B2KTauTauLine/Particles |
