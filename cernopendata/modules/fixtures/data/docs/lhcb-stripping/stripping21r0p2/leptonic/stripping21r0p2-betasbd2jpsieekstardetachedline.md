[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBetaSBd2JpsieeKstarDetachedLine

## Properties:

|                |                                                |
|----------------|------------------------------------------------|
| OutputLocation | Phys/BetaSBd2JpsieeKstarDetachedLine/Particles |
| Postscale      | 1.0000000                                      |
| HLT1           | None                                           |
| HLT2           | None                                           |
| Prescale       | 1.0000000                                      |
| L0DU           | None                                           |
| ODIN           | None                                           |

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

**FilterDesktop/SelKst2KpiForBetaSBd2JpsieeKstarDetached**

|                 |                                                                                                                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('K\*(892)0')) \< 100.0 \* MeV) & (PT \> 1000.0 \*MeV) & (MINTREE('K+'==ABSID,PIDK-PIDpi) \> 0.0 ) & (MAXTREE('K+'==ABSID,TRCHI2DOF) \< 3.0) & (MINTREE('pi+'==ABSID,PIDK-PIDpi) \< 5.0 ) & (MAXTREE('pi+'==ABSID,TRCHI2DOF) \< 3.0) & (VFASPF(VCHI2/VDOF) \< 10.0) |
| Inputs          | [ 'Phys/ [StdLooseKstar2Kpi](./stripping21r0p2-stdloosekstar2kpi) ' ]                                                                                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                                                                                                                              |
| Output          | Phys/SelKst2KpiForBetaSBd2JpsieeKstarDetached/Particles                                                                                                                                                                                                                           |

**LoKi::VoidFilter/SELECT:Phys/StdLooseDiElectron**

|      |                                        |
|------|----------------------------------------|
| Code | 0 StdLooseDiElectron /Particles',True) |

**FilterDesktop/SelJpsi2eeForBetaSBd2JpsieeKstarDetached**

|                 |                                                                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MM \> 2300.0 \*MeV) & (MM \< 3500.0 \*MeV) & (PT \> 400.0 \*MeV) & (MINTREE('e+'==ABSID,PIDe-PIDpi) \> 1.0 ) & (MINTREE('e+'==ABSID,PT) \> 500.0 \*MeV) & (MAXTREE('e+'==ABSID,TRCHI2DOF) \< 3.0) & (VFASPF(VCHI2/VDOF) \< 11.0) |
| Inputs          | [ 'Phys/ [StdLooseDiElectron](./stripping21r0p2-stdloosedielectron) ' ]                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                                              |
| Output          | Phys/SelJpsi2eeForBetaSBd2JpsieeKstarDetached/Particles                                                                                                                                                                           |

**CombineParticles/BetaSBd2JpsieeKstarDetachedLine**

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelJpsi2eeForBetaSBd2JpsieeKstarDetached' , 'Phys/SelKst2KpiForBetaSBd2JpsieeKstarDetached' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' }                      |
| CombinationCut   | (AM \> 4350.0 \*MeV) & (AM \< 6000.0 \*MeV)                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10.0) & (BPVLTIME()\>0.3\*ps)                                                    |
| DecayDescriptor  | B0 -\> J/psi(1S) K\*(892)0                                                                              |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) K\*(892)0' ]                                                                      |
| Output           | Phys/BetaSBd2JpsieeKstarDetachedLine/Particles                                                          |
