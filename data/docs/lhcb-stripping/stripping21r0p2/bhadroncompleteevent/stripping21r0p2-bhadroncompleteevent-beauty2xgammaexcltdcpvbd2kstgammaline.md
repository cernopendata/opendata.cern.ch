[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBeauty2XGammaExclTDCPVBd2KstGammaLine

## Properties:

|                |                                                      |
|----------------|------------------------------------------------------|
| OutputLocation | Phys/Beauty2XGammaExclTDCPVBd2KstGammaLine/Particles |
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
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r0p2-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/PhotonSelBeauty2XGammaExclTDCPV/Particles                                          |

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseDetachedKst2Kpi

|      |                                               |
|------|-----------------------------------------------|
| Code | 0StdVeryLooseDetachedKst2Kpi/Particles',True) |

FilterDesktop/KStarSelBeauty2XGammaExclTDCPV

|                 |                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Code            | goodKstar & (NINTREE( ('K+'==ABSID) & goodKaon ) == 1) & ( NINTREE( ('pi+'==ABSID) & goodPion ) == 1 )    |
| Inputs          | [ 'Phys/[StdVeryLooseDetachedKst2Kpi](./stripping21r0p2-commonparticles-stdveryloosedetachedkst2kpi)' ] |
| DecayDescriptor | None                                                                                                      |
| Output          | Phys/KStarSelBeauty2XGammaExclTDCPV/Particles                                                             |

CombineParticles/Bd2KstG_init

|                  |                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KStarSelBeauty2XGammaExclTDCPV' , 'Phys/PhotonSelBeauty2XGammaExclTDCPV' ]                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'gamma' : 'ALL' }                                                                                                  |
| CombinationCut   | ((AM \> 0.3\*4000.0) & (AM \< 2.5\*7000.0))                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF) \<16.0) & (BPVIPCHI2() \< 16.0) & (PT \> 2500.0) & (M \> 0.3\*4000.0) & (M \< 2.\*7000.0) & (SUMTREE(PT, ISBASIC, 0.0) \> 3000.0) & (acos(BPVDIRA) \< 0.2) |
| DecayDescriptor  | [B0 -\> K\*(892)0 gamma]cc                                                                                                                                                   |
| DecayDescriptors | [ '[B0 -\> K\*(892)0 gamma]cc' ]                                                                                                                                           |
| Output           | Phys/Bd2KstG_init/Particles                                                                                                                                                    |

FilterDesktop/Beauty2XGammaExclTDCPVBd2KstGamma

|                 |                                                                                |
|-----------------|--------------------------------------------------------------------------------|
| Code            | ((dtf_prob \> 1e-10) & (in_range(4000.0,mB,7000.0)) & (abs(mX-895) \< 100.0) ) |
| Inputs          | [ 'Phys/Bd2KstG_init' ]                                                      |
| DecayDescriptor | None                                                                           |
| Output          | Phys/Beauty2XGammaExclTDCPVBd2KstGamma/Particles                               |

TisTosParticleTagger/Beauty2XGammaExclTDCPVBd2KstGammaHlt1TISTOS

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammaExclTDCPVBd2KstGamma' ]                           |
| DecayDescriptor | None                                                                     |
| Output          | Phys/Beauty2XGammaExclTDCPVBd2KstGammaHlt1TISTOS/Particles               |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 , 'Hlt1TrackPhotonDecision%TOS' : 0 } |

TisTosParticleTagger/Beauty2XGammaExclTDCPVBd2KstGammaLine

|                 |                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammaExclTDCPVBd2KstGammaHlt1TISTOS' ]                                                              |
| DecayDescriptor | None                                                                                                                  |
| Output          | Phys/Beauty2XGammaExclTDCPVBd2KstGammaLine/Particles                                                                  |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Radiative.\*Decision%TOS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
