[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSBd2JpsiKsPrescaledLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/BetaSBd2JpsiKsPrescaledLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT            | HLT_PASS_RE('Hlt2DiMuonJPsiDecision')      |
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

GaudiSequencer/SeqStdLooseKsMergedForBetaSBetaS

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/StdLooseKsMergedForBetaSBetaS

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                             |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/StdLooseKsMergedForBetaSBetaS/Particles                                                                                                    |

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

CombineParticles/BetaSBd2JpsiKsPrescaledLine

|                  |                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KsForBetaSBetaS' , 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'KS0' : 'ALL' }                                                                             |
| CombinationCut   | in_range(5000,AM,5650)                                                                                                           |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF) \< 10)                                                                                |
| DecayDescriptor  | B0 -\> J/psi(1S) KS0                                                                                                             |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) KS0' ]                                                                                                     |
| Output           | Phys/BetaSBd2JpsiKsPrescaledLine/Particles                                                                                       |
