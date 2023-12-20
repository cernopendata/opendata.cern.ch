[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingBd2JpsieeKSBd2JpsieeKSDetachedLine

## Properties:

|                |                                                   |
|----------------|---------------------------------------------------|
| OutputLocation | Phys/Bd2JpsieeKSBd2JpsieeKSDetachedLine/Particles |
| Postscale      | 1.0000000                                         |
| HLT1           | None                                              |
| HLT2           | None                                              |
| Prescale       | 1.0000000                                         |
| L0DU           | None                                              |
| ODIN           | None                                              |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDiElectron_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiElectron](./stripping21r0p1-commonparticles-stdloosedielectron)/Particles',True)\>0 |

FilterDesktop/SelJpsi2eeForBd2JpsieeKS

|                 |                                                                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MM \> 2300.0 \*MeV) & (MM \< 3300.0 \*MeV) & (MINTREE('e+'==ABSID,PIDe-PIDpi) \> 0.0 ) & (MINTREE('e+'==ABSID,PT) \> 500.0 \*MeV) & (MAXTREE('e+'==ABSID,TRCHI2DOF) \< 5.0) & (VFASPF(VCHI2/VDOF) \< 15.0) |
| Inputs          | [ 'Phys/[StdLooseDiElectron](./stripping21r0p1-commonparticles-stdloosedielectron)' ]                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                        |
| Output          | Phys/SelJpsi2eeForBd2JpsieeKS/Particles                                                                                                                                                                     |

GaudiSequencer/SeqStdLooseKsMergedForBetaSBd2JpsieeKS

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/StdLooseKsMergedForBetaSBd2JpsieeKS

|                 |                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                 |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                                                                                                |
| Output          | Phys/StdLooseKsMergedForBetaSBd2JpsieeKS/Particles                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/KsForBetaSBd2JpsieeKS

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Code            | (VFASPF(VCHI2) \< 20.0) & (BPVDLS \> 5.0)        |
| Inputs          | [ 'Phys/StdLooseKsMergedForBetaSBd2JpsieeKS' ] |
| DecayDescriptor | None                                             |
| Output          | Phys/KsForBetaSBd2JpsieeKS/Particles             |

CombineParticles/Bd2JpsiKS

|                  |                                                                      |
|------------------|----------------------------------------------------------------------|
| Inputs           | [ 'Phys/KsForBetaSBd2JpsieeKS' , 'Phys/SelJpsi2eeForBd2JpsieeKS' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'KS0' : 'ALL' }                 |
| CombinationCut   | in_range(4400.0,AM,6000.0)                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 7.0)                                          |
| DecayDescriptor  | B0 -\> J/psi(1S) KS0                                                 |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) KS0' ]                                         |
| Output           | Phys/Bd2JpsiKS/Particles                                             |

FilterDesktop/Bd2JpsieeKSBd2JpsieeKSDetachedLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | (BPVLTIME() \> 0.2\*ps)                           |
| Inputs          | [ 'Phys/Bd2JpsiKS' ]                            |
| DecayDescriptor | None                                              |
| Output          | Phys/Bd2JpsieeKSBd2JpsieeKSDetachedLine/Particles |
