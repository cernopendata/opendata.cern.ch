[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2RhoTauTauLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/B2RhoTauTauLine/Particles |
| Postscale      | 1.0000000                      |
| HLT1           | None                           |
| HLT2           | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2RhoTauTauLineVOIDFilter

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

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

CombineParticles/RhoB2XTauTau_Rho

|                  |                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ]                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 6) & (TRGHOSTPROB \< 0.5)' , 'pi-' : '(MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 6) & (TRGHOSTPROB \< 0.5)' } |
| CombinationCut   | in_range ( 280.0, AM, 1100.0 )                                                                                                                                                   |
| MotherCut        | (PT \> 800.0) & (VFASPF(VCHI2) \< 9)                                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                             |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                    |
| Output           | Phys/RhoB2XTauTau_Rho/Particles                                                                                                                                                  |

DaVinci::N3BodyDecays/B2RhoTauTauLine

|                  |                                                                          |
|------------------|--------------------------------------------------------------------------|
| Inputs           | [ 'Phys/RhoB2XTauTau_Rho' , 'Phys/TauB2XTauTau' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'rho(770)0' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }   |
| CombinationCut   | in_range ( 2000.0, AM, 6000.0 )                                          |
| MotherCut        | ( BPVVDCHI2 \> 16 ) & ( BPVVD \< 100 ) & (PT \> 2000.0) & (P \> 10000.0) |
| DecayDescriptor  | None                                                                     |
| DecayDescriptors | [ 'B_s0 -\> rho(770)0 tau+ tau-' ]                                     |
| Output           | Phys/B2RhoTauTauLine/Particles                                           |

AddRelatedInfo/RelatedInfo1_B2RhoTauTauLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2RhoTauTauLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo1_B2RhoTauTauLine/Particles |

AddRelatedInfo/RelatedInfo2_B2RhoTauTauLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2RhoTauTauLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo2_B2RhoTauTauLine/Particles |
