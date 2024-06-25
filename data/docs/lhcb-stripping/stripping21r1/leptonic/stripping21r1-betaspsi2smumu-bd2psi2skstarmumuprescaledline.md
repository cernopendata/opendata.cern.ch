[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSPsi2SMuMu_Bd2Psi2SKstarMuMuPrescaledLine

## Properties:

|                |                                                              |
|----------------|--------------------------------------------------------------|
| OutputLocation | Phys/BetaSPsi2SMuMu_Bd2Psi2SKstarMuMuPrescaledLine/Particles |
| Postscale      | 1.0000000                                                    |
| HLT            | None                                                         |
| Prescale       | 0.070000000                                                  |
| L0DU           | None                                                         |
| ODIN           | None                                                         |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) /Particles')\>0 |

**CombineParticles/BetaSPsi2SMuMu_Psi2SToMuMu**

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'PIDmu \> 0.0' , 'mu-' : 'PIDmu\>0.0' }      |
| CombinationCut   | (ADAMASS('psi(2S)')\<60.0\*MeV) & (ADOCACHI2CUT( 30.0 ,''))         |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 16) & (MFIT)                                 |
| DecayDescriptor  | psi(2S) -\> mu+ mu-                                                 |
| DecayDescriptors | [ 'psi(2S) -\> mu+ mu-' ]                                         |
| Output           | Phys/BetaSPsi2SMuMu_Psi2SToMuMu/Particles                           |

****Tools:****

**LoKi::MassFitter**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| Tolerance :              | 0.020000000                                                                                               |
| ErrorsPrint :            | True                                                                                                      |
| ChangeVertex :           | True                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
| RootOnTES :              | None                                                                                                      |
| RootInTES :              | None                                                                                                      |
| AuditFinalize :          | False                                                                                                     |
| TypePrint :              | True                                                                                                      |
| UseEfficiencyRowFormat : | True                                                                                                      |
| ContextService :         | AlgContextSvc                                                                                             |
| AuditTools :             | False                                                                                                     |
| MonitorService :         | MonitorSvc                                                                                                |
| AuditInitialize :        | False                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| MaxIterations :          | 20                                                                                                        |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKstar2Kpi](./stripping21r1-stdloosekstar2kpi) /Particles')\>0 |

**FilterDesktop/BetaSPsi2SMuMu_KstarForPsi2SToMuMu**

|                 |                                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (in_range(826,M,966)) & (PT \> 1200\*MeV) & (VFASPF(VCHI2) \< 16)& (MAXTREE('K+'==ABSID, TRCHI2DOF) \< 4 )& (MAXTREE('pi-'==ABSID, TRCHI2DOF) \< 4 )& (MINTREE('K+'==ABSID, PIDK) \> 0)& (MINTREE('pi-'==ABSID, PIDK) \< 10) |
| Inputs          | [ 'Phys/ [StdLooseKstar2Kpi](./stripping21r1-stdloosekstar2kpi) ' ]                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                                         |
| Output          | Phys/BetaSPsi2SMuMu_KstarForPsi2SToMuMu/Particles                                                                                                                                                                            |

**CombineParticles/BetaSPsi2SMuMu_Bd2Psi2SKstarMuMuPrescaledLine**

|                  |                                                                                     |
|------------------|-------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSPsi2SMuMu_KstarForPsi2SToMuMu' , 'Phys/BetaSPsi2SMuMu_Psi2SToMuMu' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' , 'psi(2S)' : 'ALL' }    |
| CombinationCut   | in_range(5000,AM,5650)                                                              |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF)\<20)                                     |
| DecayDescriptor  | [B0 -\> psi(2S) K\*(892)0]cc                                                      |
| DecayDescriptors | [ '[B0 -\> psi(2S) K\*(892)0]cc' ]                                              |
| Output           | Phys/BetaSPsi2SMuMu_Bd2Psi2SKstarMuMuPrescaledLine/Particles                        |
