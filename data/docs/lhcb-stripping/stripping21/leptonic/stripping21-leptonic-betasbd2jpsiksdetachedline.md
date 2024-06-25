[[stripping21 lines]](./stripping21-index)

# StrippingBetaSBd2JpsiKsDetachedLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/BetaSBd2JpsiKsDetachedLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT            | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles

|      |                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdMassConstrainedJpsi2MuMu](./stripping21-commonparticles-stdmassconstrainedjpsi2mumu)/Particles')\>0 |

GaudiSequencer/SeqStdLooseKsMergedForBetaSBetaS

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/StdLooseKsMergedForBetaSBetaS

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/StdLooseKsMergedForBetaSBetaS/Particles                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/KsForBetaSBetaS

|                 |                                            |
|-----------------|--------------------------------------------|
| Code            | (VFASPF(VCHI2)\<20) & (BPVDLS\>5)          |
| Inputs          | [ 'Phys/StdLooseKsMergedForBetaSBetaS' ] |
| DecayDescriptor | None                                       |
| Output          | Phys/KsForBetaSBetaS/Particles             |

CombineParticles/Bd2JpsiKSBetaS

|                  |                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KsForBetaSBetaS' , 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'KS0' : 'ALL' }                                                                           |
| CombinationCut   | in_range(5000,AM,5650)                                                                                                         |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF) \< 10)                                                                              |
| DecayDescriptor  | B0 -\> J/psi(1S) KS0                                                                                                           |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) KS0' ]                                                                                                   |
| Output           | Phys/Bd2JpsiKSBetaS/Particles                                                                                                  |

FilterDesktop/BetaSBd2JpsiKsDetachedLine

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | (CHILD('Beauty -\> ^J/psi(1S) X', PFUNA(ADAMASS('J/psi(1S)'))) \< 80 \* MeV) & (BPVLTIME() \> 0.2\*ps) |
| Inputs          | [ 'Phys/Bd2JpsiKSBetaS' ]                                                                            |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/BetaSBd2JpsiKsDetachedLine/Particles                                                              |
