[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2EtapTauTauLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/B2EtapTauTauLine/Particles |
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

LoKi::VoidFilter/StrippingB2EtapTauTauLineVOIDFilter

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

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseAllPhotons/Particles',True) |

CombineParticles/EtapB2XTauTau_Etap

|                  |                                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseAllPhotons](./stripping21r0p2-commonparticles-stdlooseallphotons)' , 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : '(PT \> 400.0) & (CL \> 0.2)' , 'pi+' : '(MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 6) & (TRGHOSTPROB \< 0.5) & (PROBNNpi\>0.2)' , 'pi-' : '(MIPCHI2DV(PRIMARY) \> 16) & (TRCHI2DOF \< 6) & (TRGHOSTPROB \< 0.5) & (PROBNNpi\>0.2)' } |
| CombinationCut   | (APT \> 800.0) & (in_range ( 800.0, AM, 1100.0))                                                                                                                                                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9)                                                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ 'eta_prime -\> pi+ pi- gamma' ]                                                                                                                                                                                                                            |
| Output           | Phys/EtapB2XTauTau_Etap/Particles                                                                                                                                                                                                                              |

DaVinci::N3BodyDecays/B2EtapTauTauLine

|                  |                                                                          |
|------------------|--------------------------------------------------------------------------|
| Inputs           | [ 'Phys/EtapB2XTauTau_Etap' , 'Phys/TauB2XTauTau' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'eta_prime' : 'ALL' , 'tau+' : 'ALL' , 'tau-' : 'ALL' }   |
| CombinationCut   | in_range ( 2000.0, AM, 6000.0 )                                          |
| MotherCut        | ( BPVVDCHI2 \> 16 ) & ( BPVVD \< 100 ) & (PT \> 2000.0) & (P \> 10000.0) |
| DecayDescriptor  | None                                                                     |
| DecayDescriptors | [ 'B_s0 -\> eta_prime tau+ tau-' ]                                     |
| Output           | Phys/B2EtapTauTauLine/Particles                                          |

AddRelatedInfo/RelatedInfo1_B2EtapTauTauLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2EtapTauTauLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_B2EtapTauTauLine/Particles |

AddRelatedInfo/RelatedInfo2_B2EtapTauTauLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/B2EtapTauTauLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo2_B2EtapTauTauLine/Particles |
