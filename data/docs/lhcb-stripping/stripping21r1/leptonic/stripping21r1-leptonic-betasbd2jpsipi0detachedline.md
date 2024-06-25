[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSBd2JpsiPi0DetachedLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/BetaSBd2JpsiPi0DetachedLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT            | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)/Particles')\>0 |

FilterDesktop/NarrowJpsiForBetaSBetaS

|                 |                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('J/psi(1S)')) \< 80 \* MeV)                                                              |
| Inputs          | [ 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DecayDescriptor | None                                                                                                    |
| Output          | Phys/NarrowJpsiForBetaSBetaS/Particles                                                                  |

GaudiSequencer/SeqStdLooseCocktailPi0ForBetaSBetaS

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)/Particles')\>0 |

FilterDesktop/StdLooseCocktailPi0ForBetaSBetaS

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                     |
| Inputs          | [ 'Phys/[StdLooseMergedPi0](./stripping21r1-commonparticles-stdloosemergedpi0)' , 'Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/StdLooseCocktailPi0ForBetaSBetaS/Particles                                                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Pi0ForBetaSBetaS

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | (PT \> 1500.\*MeV)                            |
| Inputs          | [ 'Phys/StdLooseCocktailPi0ForBetaSBetaS' ] |
| DecayDescriptor | None                                          |
| Output          | Phys/Pi0ForBetaSBetaS/Particles               |

CombineParticles/Bd2JpsiPi0BetaS

|                  |                                                                |
|------------------|----------------------------------------------------------------|
| Inputs           | [ 'Phys/NarrowJpsiForBetaSBetaS' , 'Phys/Pi0ForBetaSBetaS' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi0' : 'ALL' }           |
| CombinationCut   | in_range(4500,AM,6000)                                         |
| MotherCut        | in_range(4700,M,5900) & (VFASPF(VCHI2PDOF) \< 10)              |
| DecayDescriptor  | B0 -\> J/psi(1S) pi0                                           |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) pi0' ]                                   |
| Output           | Phys/Bd2JpsiPi0BetaS/Particles                                 |

FilterDesktop/BetaSBd2JpsiPi0DetachedLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Code            | (BPVLTIME() \> 0.2\*ps)                    |
| Inputs          | [ 'Phys/Bd2JpsiPi0BetaS' ]               |
| DecayDescriptor | None                                       |
| Output          | Phys/BetaSBd2JpsiPi0DetachedLine/Particles |
