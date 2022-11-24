[[stripping21 lines]](./stripping21-index)

# StrippingBetaSBd2JpsieeKSBd2JpsieeKSDetachedLine

## Properties:

|                |                                                        |
|----------------|--------------------------------------------------------|
| OutputLocation | Phys/BetaSBd2JpsieeKSBd2JpsieeKSDetachedLine/Particles |
| Postscale      | 1.0000000                                              |
| HLT            | None                                                   |
| Prescale       | 1.0000000                                              |
| L0DU           | None                                                   |
| ODIN           | None                                                   |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseDiElectron_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseDiElectron](./stripping21-stdloosedielectron) /Particles')\>0 |

**FilterDesktop/SelJpsi2eeForBetaSBd2JpsieeKS**

|                 |                                                                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MM \> 2500.0 \*MeV) & (MM \< 3300.0 \*MeV) & (MINTREE('e+'==ABSID,PIDe-PIDpi) \> 0.0 ) & (MINTREE('e+'==ABSID,PT) \> 500.0 \*MeV) & (MAXTREE('e+'==ABSID,TRCHI2DOF) \< 5.0) & (VFASPF(VCHI2/VDOF) \< 15.0) |
| Inputs          | [ 'Phys/ [StdLooseDiElectron](./stripping21-stdloosedielectron) ' ]                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                        |
| Output          | Phys/SelJpsi2eeForBetaSBd2JpsieeKS/Particles                                                                                                                                                                |

**GaudiSequencer/SeqStdLooseKsMergedForBetaSBetaSBd2JpsieeKS**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles**

|      |                                                                            |
|------|----------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKsDD](./stripping21-stdlooseksdd) /Particles')\>0 |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| Factory :                   | LoKi::Hybrid::CoreFactory/CoreFactory:PUBLIC                                                              |
| AuditReinitialize :         | True                                                                                                      |
| Preambulo :                 | [ ]                                                                                                     |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RootOnTES :                 | None                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| TypePrint :                 | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| ErrorCount :                | 0                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :               | 3                                                                                                         |
| StatPrint :                 | True                                                                                                      |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :               | [ '.\*' ]                                                                                               |

**LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles**

|      |                                                                            |
|------|----------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKsLL](./stripping21-stdlooseksll) /Particles')\>0 |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| Factory :                   | LoKi::Hybrid::CoreFactory/CoreFactory:PUBLIC                                                              |
| AuditReinitialize :         | True                                                                                                      |
| Preambulo :                 | [ ]                                                                                                     |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RootOnTES :                 | None                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| TypePrint :                 | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| ErrorCount :                | 0                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :               | 3                                                                                                         |
| StatPrint :                 | True                                                                                                      |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :               | [ '.\*' ]                                                                                               |

**FilterDesktop/StdLooseKsMergedForBetaSBetaSBd2JpsieeKS**

|                 |                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                             |
| Inputs          | [ 'Phys/ [StdLooseKsDD](./stripping21-stdlooseksdd) ' , 'Phys/ [StdLooseKsLL](./stripping21-stdlooseksll) ' ] |
| DecayDescriptor | None                                                                                                            |
| Output          | Phys/StdLooseKsMergedForBetaSBetaSBd2JpsieeKS/Particles                                                         |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IStdLooseKsMergedForBetaSBetaSBd2JpsieeKS                                                                 |
| Monitor :                      | False                                                                                                     |
| AuditExecute :                 | True                                                                                                      |
| Factory :                      | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                   |
| AuditStart :                   | True                                                                                                      |
| ReFitPVs :                     | False                                                                                                     |
| ParticleCombiners :            | { }                                                                                                       |
| InputPlotsTool :               | LoKi::Hybrid::PlotTool/InputPlots                                                                         |
| PVReFitters :                  | { }                                                                                                       |
| VetoObjects :                  | [ ]                                                                                                     |
| AuditRestart :                 | True                                                                                                      |
| CheckOverlapTool :             | CheckOverlap:PUBLIC                                                                                       |
| StatEntityList :               | [ ]                                                                                                     |
| Enable :                       | True                                                                                                      |
| RootOnTES :                    | None                                                                                                      |
| VertexFitters :                | { }                                                                                                       |
| ParticleFilters :              | { }                                                                                                       |
| RequireObjects :               | [ ]                                                                                                     |
| WriteP2PVRelations :           | True                                                                                                      |
| ParticleReFitters :            | { }                                                                                                       |
| RootInTES :                    | None                                                                                                      |
| DecayTreeFitters :             | { }                                                                                                       |
| AuditFinalize :                | True                                                                                                      |
| RegularRowFormat :             | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputPlotsTool :              | LoKi::Hybrid::PlotTool/OutputPlots                                                                        |
| ErrorsPrint :                  | True                                                                                                      |
| AuditBeginRun :                | True                                                                                                      |
| ErrorCount :                   | 0                                                                                                         |
| PostMonitor :                  | None                                                                                                      |
| ErrorMax :                     | 1                                                                                                         |
| MassFitters :                  | { }                                                                                                       |
| MonitorService :               | MonitorSvc                                                                                                |
| AuditInitialize :              | True                                                                                                      |
| PrimaryVertexRelator :         | GenericParticle2PVRelator\<\_p2PVWithIPChi2, OfflineDistanceCalculatorName\>/P2PVWithIPChi2:PUBLIC        |
| TypePrint :                    | True                                                                                                      |
| StatPrint :                    | True                                                                                                      |
| AuditEndRun :                  | True                                                                                                      |
| DistanceCalculators :          | { }                                                                                                       |
| AuditStop :                    | True                                                                                                      |
| PreMonitor :                   | None                                                                                                      |
| P2PVInputLocations :           | [ ]                                                                                                     |
| PropertiesPrint :              | False                                                                                                     |
| PreloadTools :                 | False                                                                                                     |
| ForceP2PVBuild :               | True                                                                                                      |
| OutputPlotsPath :              | OStdLooseKsMergedForBetaSBetaSBd2JpsieeKS                                                                 |
| Context :                      | None                                                                                                      |
| OutputLevel :                  | 3                                                                                                         |
| ForceOutput :                  | True                                                                                                      |
| AuditReinitialize :            | True                                                                                                      |
| LifetimeFitters :              | { }                                                                                                       |
| UseEfficiencyRowFormat :       | True                                                                                                      |
| HistoProduce :                 | False                                                                                                     |
| InputPrimaryVertices :         | Rec/Vertex/Primary                                                                                        |
| AuditAlgorithms :              | True                                                                                                      |
| DirectionFitters :             | { }                                                                                                       |
| IgnoreP2PVFromInputLocations : | False                                                                                                     |
| CloneFilteredParticles :       | True                                                                                                      |
| Preambulo :                    | [ ]                                                                                                     |
| RegisterForContextService :    | True                                                                                                      |
| EfficiencyRowFormat :          | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| UseP2PVRelations :             | True                                                                                                      |
| GlobalTimeOffset :             | 0.0000000                                                                                                 |
| CounterList :                  | [ '.\*' ]                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

**FilterDesktop/KsForBetaSBetaSBd2JpsieeKS**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Code            | (VFASPF(VCHI2)\<20) & (BPVDLS\>5)                     |
| Inputs          | [ 'Phys/StdLooseKsMergedForBetaSBetaSBd2JpsieeKS' ] |
| DecayDescriptor | None                                                  |
| Output          | Phys/KsForBetaSBetaSBd2JpsieeKS/Particles             |

**CombineParticles/Bd2JpsiKSBetaSBd2JpsieeKSDetached**

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KsForBetaSBetaSBd2JpsieeKS' , 'Phys/SelJpsi2eeForBetaSBd2JpsieeKS' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'KS0' : 'ALL' }                           |
| CombinationCut   | in_range(4500.0,AM,6000.0)                                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10.0)                                                   |
| DecayDescriptor  | B0 -\> J/psi(1S) KS0                                                           |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) KS0' ]                                                   |
| Output           | Phys/Bd2JpsiKSBetaSBd2JpsieeKSDetached/Particles                               |

**FilterDesktop/BetaSBd2JpsieeKSBd2JpsieeKSDetachedLine**

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Code            | (BPVLTIME() \> 0.2\*ps)                                |
| Inputs          | [ 'Phys/Bd2JpsiKSBetaSBd2JpsieeKSDetached' ]         |
| DecayDescriptor | None                                                   |
| Output          | Phys/BetaSBd2JpsieeKSBd2JpsieeKSDetachedLine/Particles |
