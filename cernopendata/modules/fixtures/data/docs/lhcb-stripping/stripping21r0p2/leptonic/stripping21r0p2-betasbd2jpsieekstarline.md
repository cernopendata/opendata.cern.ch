[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBetaSBd2JpsieeKstarLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/BetaSBd2JpsieeKstarLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 0.050000000                            |
| L0DU           | None                                   |
| ODIN           | None                                   |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseKstar2Kpi**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdLooseKstar2Kpi /Particles',True) |

**FilterDesktop/SelKst2KpiForBetaSBd2JpsieeKstar**

|                 |                                                                                                                                                                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('K\*(892)0')) \< 150.0 \* MeV) & (PT \> 1000.0 \*MeV) & (MINTREE('K+'==ABSID,PIDK-PIDpi) \> -3.0 ) & (MAXTREE('K+'==ABSID,TRCHI2DOF) \< 5.0) & (MINTREE('pi+'==ABSID,PIDK-PIDpi) \< 10.0 ) & (MAXTREE('pi+'==ABSID,TRCHI2DOF) \< 5.0) & (VFASPF(VCHI2/VDOF) \< 15.0) |
| Inputs          | [ 'Phys/ [StdLooseKstar2Kpi](./stripping21r0p2-stdloosekstar2kpi) ' ]                                                                                                                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                |
| Output          | Phys/SelKst2KpiForBetaSBd2JpsieeKstar/Particles                                                                                                                                                                                                                                     |

**LoKi::VoidFilter/SELECT:Phys/StdLooseDiElectron**

|      |                                        |
|------|----------------------------------------|
| Code | 0 StdLooseDiElectron /Particles',True) |

**FilterDesktop/SelJpsi2eeForBetaSBd2JpsieeKstar**

|                 |                                                                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MM \> 1900.0 \*MeV) & (MM \< 3600.0 \*MeV) & (PT \> 400.0 \*MeV) & (MINTREE('e+'==ABSID,PIDe-PIDpi) \> 0.0 ) & (MINTREE('e+'==ABSID,PT) \> 500.0 \*MeV) & (MAXTREE('e+'==ABSID,TRCHI2DOF) \< 5.0) & (VFASPF(VCHI2/VDOF) \< 15.0) |
| Inputs          | [ 'Phys/ [StdLooseDiElectron](./stripping21r0p2-stdloosedielectron) ' ]                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                                              |
| Output          | Phys/SelJpsi2eeForBetaSBd2JpsieeKstar/Particles                                                                                                                                                                                   |

**CombineParticles/BetaSBd2JpsieeKstarLine**

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelJpsi2eeForBetaSBd2JpsieeKstar' , 'Phys/SelKst2KpiForBetaSBd2JpsieeKstar' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' }      |
| CombinationCut   | (AM \> 4000.0 \*MeV) & (AM \< 6000.0 \*MeV)                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10.0) & (BPVDIRA \> 0.99)                                        |
| DecayDescriptor  | B0 -\> J/psi(1S) K\*(892)0                                                              |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) K\*(892)0' ]                                                      |
| Output           | Phys/BetaSBd2JpsieeKstarLine/Particles                                                  |
