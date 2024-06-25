[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSBd2JpsiKstarPrescaledLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/BetaSBd2JpsiKstarPrescaledLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT            | HLT_PASS_RE('Hlt2DiMuonJPsiDecision')         |
| Prescale       | 0.65000000                                    |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles**

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21r1-stdmassconstrainedjpsi2mumu) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKstar2Kpi](./stripping21r1-stdloosekstar2kpi) /Particles')\>0 |

**FilterDesktop/Kstar2KpiForBetaSBetaS**

|                 |                                                                                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (in_range(826,M,966))& (PT \> 1300.\*MeV) & (VFASPF(VCHI2) \< 25)& (MAXTREE('K+'==ABSID, TRCHI2DOF) \< 5 )& (MAXTREE('pi-'==ABSID, TRCHI2DOF) \< 5 )& (MINTREE('K+'==ABSID, PIDK) \> 0) |
| Inputs          | [ 'Phys/ [StdLooseKstar2Kpi](./stripping21r1-stdloosekstar2kpi) ' ]                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                    |
| Output          | Phys/Kstar2KpiForBetaSBetaS/Particles                                                                                                                                                   |

**CombineParticles/BetaSBd2JpsiKstarPrescaledLine**

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kstar2KpiForBetaSBetaS' , 'Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21r1-stdmassconstrainedjpsi2mumu) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' }                                        |
| CombinationCut   | in_range(5050,AM,5550)                                                                                                    |
| MotherCut        | in_range(5150,M,5450) & (VFASPF(VCHI2PDOF) \< 20)                                                                         |
| DecayDescriptor  | [B0 -\> J/psi(1S) K\*(892)0]cc                                                                                          |
| DecayDescriptors | [ '[B0 -\> J/psi(1S) K\*(892)0]cc' ]                                                                                  |
| Output           | Phys/BetaSBd2JpsiKstarPrescaledLine/Particles                                                                             |
