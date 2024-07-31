[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingBd2JpsieeKSBd2JpsieeKstarFromTracksPrescaledLine

## Properties:

|                |                                                                 |
|----------------|-----------------------------------------------------------------|
| OutputLocation | Phys/Bd2JpsieeKSBd2JpsieeKstarFromTracksPrescaledLine/Particles |
| Postscale      | 1.0000000                                                       |
| HLT1           | None                                                            |
| HLT2           | None                                                            |
| Prescale       | 0.10000000                                                      |
| L0DU           | None                                                            |
| ODIN           | None                                                            |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdDiElectronFromTracks_Particles**

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdDiElectronFromTracks](./stripping21r1p1-stddielectronfromtracks) /Particles',True)\>0 |

**FilterDesktop/SelJpsi2eeFromTracksForBd2JpsieeKS**

|                 |                                                                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MM \> 2300.0 \*MeV) & (MM \< 3300.0 \*MeV) & (MINTREE('e+'==ABSID,PIDe-PIDpi) \> 0.0 ) & (MINTREE('e+'==ABSID,PT) \> 500.0 \*MeV) & (MAXTREE('e+'==ABSID,TRCHI2DOF) \< 5.0) & (VFASPF(VCHI2/VDOF) \< 15.0) |
| Inputs          | [ 'Phys/ [StdDiElectronFromTracks](./stripping21r1p1-stddielectronfromtracks) ' ]                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                        |
| Output          | Phys/SelJpsi2eeFromTracksForBd2JpsieeKS/Particles                                                                                                                                                           |

**LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles**

|      |                                                                                               |
|------|-----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKstar2Kpi](./stripping21r1p1-stdloosekstar2kpi) /Particles',True)\>0 |

**FilterDesktop/Kstar2KpiForBetaSNoBiasBd2JpsieeKS**

|                 |                                                                                                                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (in_range(826.0,M,966.0))& (PT \> 1500.0 \*MeV) & (VFASPF(VCHI2) \< 20.0 )& (MAXTREE('K+'==ABSID, TRCHI2DOF) \< 3.0 )& (MAXTREE('pi-'==ABSID, TRCHI2DOF) \< 3.0 )& (MINTREE('K+'==ABSID, PIDK) \> 0.0 ) |
| Inputs          | [ 'Phys/ [StdLooseKstar2Kpi](./stripping21r1p1-stdloosekstar2kpi) ' ]                                                                                                                                 |
| DecayDescriptor | None                                                                                                                                                                                                    |
| Output          | Phys/Kstar2KpiForBetaSNoBiasBd2JpsieeKS/Particles                                                                                                                                                       |

**CombineParticles/Bd2JpsieeKSBd2JpsieeKstarFromTracksPrescaledLine**

|                  |                                                                                             |
|------------------|---------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kstar2KpiForBetaSNoBiasBd2JpsieeKS' , 'Phys/SelJpsi2eeFromTracksForBd2JpsieeKS' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' }          |
| CombinationCut   | in_range(4400.0,AM,6000.0)                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20.0)                                                                |
| DecayDescriptor  | [B0 -\> J/psi(1S) K\*(892)0]cc                                                            |
| DecayDescriptors | [ '[B0 -\> J/psi(1S) K\*(892)0]cc' ]                                                    |
| Output           | Phys/Bd2JpsieeKSBd2JpsieeKstarFromTracksPrescaledLine/Particles                             |
