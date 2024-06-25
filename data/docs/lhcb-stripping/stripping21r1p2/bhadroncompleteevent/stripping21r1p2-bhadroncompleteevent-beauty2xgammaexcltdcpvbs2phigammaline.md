[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBeauty2XGammaExclTDCPVBs2PhiGammaLine

## Properties:

|                |                                                      |
|----------------|------------------------------------------------------|
| OutputLocation | Phys/Beauty2XGammaExclTDCPVBs2PhiGammaLine/Particles |
| Postscale      | 1.0000000                                            |
| HLT1           | None                                                 |
| HLT2           | None                                                 |
| Prescale       | 1.0000000                                            |
| L0DU           | None                                                 |
| ODIN           | None                                                 |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseAllPhotons/Particles',True) |

FilterDesktop/PhotonSelBeauty2XGammaExclTDCPV

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ( PT\> 2500.0\*MeV )                                                                    |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r1p2-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/PhotonSelBeauty2XGammaExclTDCPV/Particles                                          |

LoKi::VoidFilter/SELECT:Phys/StdLoosePhi2KK

|      |                                  |
|------|----------------------------------|
| Code | 0StdLoosePhi2KK/Particles',True) |

FilterDesktop/PhiSelBeauty2XGammaExclTDCPV

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | goodPhi & (NINTREE( ('K+'==ABSID) & goodKaon ) == 2)                            |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21r1p2-commonparticles-stdloosephi2kk)' ] |
| DecayDescriptor | None                                                                            |
| Output          | Phys/PhiSelBeauty2XGammaExclTDCPV/Particles                                     |

CombineParticles/Bs2PhiG_init

|                  |                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PhiSelBeauty2XGammaExclTDCPV' , 'Phys/PhotonSelBeauty2XGammaExclTDCPV' ]                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'phi(1020)' : 'ALL' }                                                                                                |
| CombinationCut   | ((AM \> 0.5\*4000.0) & (AM \< 2\*7000.0))                                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF) \<16.0) & (BPVIPCHI2() \< 16.0) & (PT \> 2500.0) & (M \> 0.5\*4000.0) & (M \< 2.\*7000.0) & (SUMTREE(PT, ISBASIC, 0.0) \> 3000.0) |
| DecayDescriptor  | B_s0 -\> phi(1020) gamma                                                                                                                              |
| DecayDescriptors | [ 'B_s0 -\> phi(1020) gamma' ]                                                                                                                      |
| Output           | Phys/Bs2PhiG_init/Particles                                                                                                                           |

FilterDesktop/Beauty2XGammaExclTDCPVBs2PhiGamma

|                 |                                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| Code            | ( (dtf_prob \> 1e-10) & (in_range(4000.0,mB,7000.0)) & (abs(mX-1020) \< 15.0) ) |
| Inputs          | [ 'Phys/Bs2PhiG_init' ]                                                       |
| DecayDescriptor | None                                                                            |
| Output          | Phys/Beauty2XGammaExclTDCPVBs2PhiGamma/Particles                                |

TisTosParticleTagger/Beauty2XGammaExclTDCPVBs2PhiGammaHlt1TISTOS

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammaExclTDCPVBs2PhiGamma' ]                           |
| DecayDescriptor | None                                                                     |
| Output          | Phys/Beauty2XGammaExclTDCPVBs2PhiGammaHlt1TISTOS/Particles               |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 , 'Hlt1TrackPhotonDecision%TOS' : 0 } |

TisTosParticleTagger/Beauty2XGammaExclTDCPVBs2PhiGammaLine

|                 |                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammaExclTDCPVBs2PhiGammaHlt1TISTOS' ]                                                              |
| DecayDescriptor | None                                                                                                                  |
| Output          | Phys/Beauty2XGammaExclTDCPVBs2PhiGammaLine/Particles                                                                  |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Radiative.\*Decision%TOS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
