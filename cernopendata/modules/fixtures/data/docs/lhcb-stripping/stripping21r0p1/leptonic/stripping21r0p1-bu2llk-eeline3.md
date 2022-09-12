[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingBu2LLK_eeLine3

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/Bu2LLK_eeLine3/Particles |
| Postscale      | 1.0000000                     |
| HLT1           | None                          |
| HLT2           | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**LoKi::VoidFilter/StrippingBu2LLK_eeLine3VOIDFilter**

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**GaudiSequencer/SeqMergeBu2LLK_ee3**

**Members:**

**GaudiSequencer/SEQ:KstarsForBu2LLK**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles**

|      |                                                                                               |
|------|-----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKstar2Kpi](./stripping21r0p1-stdloosekstar2kpi) /Particles',True)\>0 |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| DataOutputs :               | None                                                                                                      |
| DataInputs :                | None                                                                                                      |
| Preambulo :                 | [ ]                                                                                                     |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| Factory :                   | LoKi::Hybrid::CoreFactory/CoreFactory:PUBLIC                                                              |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**FilterDesktop/KstarsForBu2LLK**

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/ [StdLooseKstar2Kpi](./stripping21r0p1-stdloosekstar2kpi) ' ]                                                                        |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/KstarsForBu2LLK/Particles                                                                                                                 |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IKstarsForBu2LLK                                                                                          |
| Monitor :                      | False                                                                                                     |
| AuditExecute :                 | True                                                                                                      |
| DataOutputs :                  | None                                                                                                      |
| ReFitPVs :                     | False                                                                                                     |
| ParticleCombiners :            | { }                                                                                                       |
| Preambulo :                    | [ ]                                                                                                     |
| PVReFitters :                  | { }                                                                                                       |
| VetoObjects :                  | [ ]                                                                                                     |
| AuditRestart :                 | True                                                                                                      |
| CheckOverlapTool :             | CheckOverlap:PUBLIC                                                                                       |
| StatEntityList :               | [ ]                                                                                                     |
| InputPlotsTool :               | LoKi::Hybrid::PlotTool/InputPlots                                                                         |
| Enable :                       | True                                                                                                      |
| VertexFitters :                | { }                                                                                                       |
| ParticleFilters :              | { }                                                                                                       |
| RequireObjects :               | [ ]                                                                                                     |
| WriteP2PVRelations :           | True                                                                                                      |
| ParticleReFitters :            | { }                                                                                                       |
| RootInTES :                    | None                                                                                                      |
| DecayTreeFitters :             | { }                                                                                                       |
| UseEfficiencyRowFormat :       | True                                                                                                      |
| AuditFinalize :                | True                                                                                                      |
| EfficiencyRowFormat :          | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| GlobalTimeOffset :             | 0.0000000                                                                                                 |
| OutputPlotsTool :              | LoKi::Hybrid::PlotTool/OutputPlots                                                                        |
| ErrorsPrint :                  | True                                                                                                      |
| AuditBeginRun :                | True                                                                                                      |
| Cardinality :                  | 1                                                                                                         |
| PrimaryVertexRelator :         | GenericParticle2PVRelator\<\_p2PVWithIPChi2, OfflineDistanceCalculatorName\>/P2PVWithIPChi2:PUBLIC        |
| PostMonitor :                  | None                                                                                                      |
| ErrorMax :                     | 1                                                                                                         |
| MassFitters :                  | { }                                                                                                       |
| MonitorService :               | MonitorSvc                                                                                                |
| AuditInitialize :              | True                                                                                                      |
| RegularRowFormat :             | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                    | True                                                                                                      |
| StatPrint :                    | True                                                                                                      |
| Factory :                      | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                   |
| AuditEndRun :                  | True                                                                                                      |
| DistanceCalculators :          | { }                                                                                                       |
| AuditStop :                    | True                                                                                                      |
| PreMonitor :                   | None                                                                                                      |
| P2PVInputLocations :           | [ ]                                                                                                     |
| PropertiesPrint :              | False                                                                                                     |
| PreloadTools :                 | False                                                                                                     |
| ForceP2PVBuild :               | True                                                                                                      |
| OutputPlotsPath :              | OKstarsForBu2LLK                                                                                          |
| NeededResources :              | [ ]                                                                                                     |
| Context :                      | None                                                                                                      |
| OutputLevel :                  | 3                                                                                                         |
| ForceOutput :                  | True                                                                                                      |
| DataInputs :                   | None                                                                                                      |
| LifetimeFitters :              | { }                                                                                                       |
| AuditStart :                   | True                                                                                                      |
| HistoProduce :                 | False                                                                                                     |
| InputPrimaryVertices :         | Rec/Vertex/Primary                                                                                        |
| AuditAlgorithms :              | True                                                                                                      |
| DirectionFitters :             | { }                                                                                                       |
| IgnoreP2PVFromInputLocations : | False                                                                                                     |
| CloneFilteredParticles :       | False                                                                                                     |
| IsClonable :                   | False                                                                                                     |
| RegisterForContextService :    | True                                                                                                      |
| CounterList :                  | [ '.\*' ]                                                                                               |
| UseP2PVRelations :             | True                                                                                                      |
| ErrorCounter :                 | 0                                                                                                         |
| AuditReinitialize :            | True                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| DataOutputs :               | None                                                                                                      |
| AuditStart :                | True                                                                                                      |
| DataInputs :                | None                                                                                                      |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| ReturnOK :                  | False                                                                                                     |
| ShortCircuit :              | True                                                                                                      |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| MeasureTime :               | False                                                                                                     |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**GaudiSequencer/SEQ:PhisForBu2LLK**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles**

|      |                                                                                         |
|------|-----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePhi2KK](./stripping21r0p1-stdloosephi2kk) /Particles',True)\>0 |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| DataOutputs :               | None                                                                                                      |
| DataInputs :                | None                                                                                                      |
| Preambulo :                 | [ ]                                                                                                     |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| Factory :                   | LoKi::Hybrid::CoreFactory/CoreFactory:PUBLIC                                                              |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**FilterDesktop/PhisForBu2LLK**

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/ [StdLoosePhi2KK](./stripping21r0p1-stdloosephi2kk) ' ]                                                                              |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/PhisForBu2LLK/Particles                                                                                                                   |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IPhisForBu2LLK                                                                                            |
| Monitor :                      | False                                                                                                     |
| AuditExecute :                 | True                                                                                                      |
| DataOutputs :                  | None                                                                                                      |
| ReFitPVs :                     | False                                                                                                     |
| ParticleCombiners :            | { }                                                                                                       |
| Preambulo :                    | [ ]                                                                                                     |
| PVReFitters :                  | { }                                                                                                       |
| VetoObjects :                  | [ ]                                                                                                     |
| AuditRestart :                 | True                                                                                                      |
| CheckOverlapTool :             | CheckOverlap:PUBLIC                                                                                       |
| StatEntityList :               | [ ]                                                                                                     |
| InputPlotsTool :               | LoKi::Hybrid::PlotTool/InputPlots                                                                         |
| Enable :                       | True                                                                                                      |
| VertexFitters :                | { }                                                                                                       |
| ParticleFilters :              | { }                                                                                                       |
| RequireObjects :               | [ ]                                                                                                     |
| WriteP2PVRelations :           | True                                                                                                      |
| ParticleReFitters :            | { }                                                                                                       |
| RootInTES :                    | None                                                                                                      |
| DecayTreeFitters :             | { }                                                                                                       |
| UseEfficiencyRowFormat :       | True                                                                                                      |
| AuditFinalize :                | True                                                                                                      |
| EfficiencyRowFormat :          | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| GlobalTimeOffset :             | 0.0000000                                                                                                 |
| OutputPlotsTool :              | LoKi::Hybrid::PlotTool/OutputPlots                                                                        |
| ErrorsPrint :                  | True                                                                                                      |
| AuditBeginRun :                | True                                                                                                      |
| Cardinality :                  | 1                                                                                                         |
| PrimaryVertexRelator :         | GenericParticle2PVRelator\<\_p2PVWithIPChi2, OfflineDistanceCalculatorName\>/P2PVWithIPChi2:PUBLIC        |
| PostMonitor :                  | None                                                                                                      |
| ErrorMax :                     | 1                                                                                                         |
| MassFitters :                  | { }                                                                                                       |
| MonitorService :               | MonitorSvc                                                                                                |
| AuditInitialize :              | True                                                                                                      |
| RegularRowFormat :             | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                    | True                                                                                                      |
| StatPrint :                    | True                                                                                                      |
| Factory :                      | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                   |
| AuditEndRun :                  | True                                                                                                      |
| DistanceCalculators :          | { }                                                                                                       |
| AuditStop :                    | True                                                                                                      |
| PreMonitor :                   | None                                                                                                      |
| P2PVInputLocations :           | [ ]                                                                                                     |
| PropertiesPrint :              | False                                                                                                     |
| PreloadTools :                 | False                                                                                                     |
| ForceP2PVBuild :               | True                                                                                                      |
| OutputPlotsPath :              | OPhisForBu2LLK                                                                                            |
| NeededResources :              | [ ]                                                                                                     |
| Context :                      | None                                                                                                      |
| OutputLevel :                  | 3                                                                                                         |
| ForceOutput :                  | True                                                                                                      |
| DataInputs :                   | None                                                                                                      |
| LifetimeFitters :              | { }                                                                                                       |
| AuditStart :                   | True                                                                                                      |
| HistoProduce :                 | False                                                                                                     |
| InputPrimaryVertices :         | Rec/Vertex/Primary                                                                                        |
| AuditAlgorithms :              | True                                                                                                      |
| DirectionFitters :             | { }                                                                                                       |
| IgnoreP2PVFromInputLocations : | False                                                                                                     |
| CloneFilteredParticles :       | False                                                                                                     |
| IsClonable :                   | False                                                                                                     |
| RegisterForContextService :    | True                                                                                                      |
| CounterList :                  | [ '.\*' ]                                                                                               |
| UseP2PVRelations :             | True                                                                                                      |
| ErrorCounter :                 | 0                                                                                                         |
| AuditReinitialize :            | True                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| DataOutputs :               | None                                                                                                      |
| AuditStart :                | True                                                                                                      |
| DataInputs :                | None                                                                                                      |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| ReturnOK :                  | False                                                                                                     |
| ShortCircuit :              | True                                                                                                      |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| MeasureTime :               | False                                                                                                     |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**GaudiSequencer/SEQ:LambdasLLForBu2LLK**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles**

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseLambdaLL](./stripping21r0p1-stdlooselambdall) /Particles',True)\>0 |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| DataOutputs :               | None                                                                                                      |
| DataInputs :                | None                                                                                                      |
| Preambulo :                 | [ ]                                                                                                     |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| Factory :                   | LoKi::Hybrid::CoreFactory/CoreFactory:PUBLIC                                                              |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**FilterDesktop/LambdasLLForBu2LLK**

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/ [StdLooseLambdaLL](./stripping21r0p1-stdlooselambdall) ' ]                                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/LambdasLLForBu2LLK/Particles                                                                                                              |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | ILambdasLLForBu2LLK                                                                                       |
| Monitor :                      | False                                                                                                     |
| AuditExecute :                 | True                                                                                                      |
| DataOutputs :                  | None                                                                                                      |
| ReFitPVs :                     | False                                                                                                     |
| ParticleCombiners :            | { }                                                                                                       |
| Preambulo :                    | [ ]                                                                                                     |
| PVReFitters :                  | { }                                                                                                       |
| VetoObjects :                  | [ ]                                                                                                     |
| AuditRestart :                 | True                                                                                                      |
| CheckOverlapTool :             | CheckOverlap:PUBLIC                                                                                       |
| StatEntityList :               | [ ]                                                                                                     |
| InputPlotsTool :               | LoKi::Hybrid::PlotTool/InputPlots                                                                         |
| Enable :                       | True                                                                                                      |
| VertexFitters :                | { }                                                                                                       |
| ParticleFilters :              | { }                                                                                                       |
| RequireObjects :               | [ ]                                                                                                     |
| WriteP2PVRelations :           | True                                                                                                      |
| ParticleReFitters :            | { }                                                                                                       |
| RootInTES :                    | None                                                                                                      |
| DecayTreeFitters :             | { }                                                                                                       |
| UseEfficiencyRowFormat :       | True                                                                                                      |
| AuditFinalize :                | True                                                                                                      |
| EfficiencyRowFormat :          | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| GlobalTimeOffset :             | 0.0000000                                                                                                 |
| OutputPlotsTool :              | LoKi::Hybrid::PlotTool/OutputPlots                                                                        |
| ErrorsPrint :                  | True                                                                                                      |
| AuditBeginRun :                | True                                                                                                      |
| Cardinality :                  | 1                                                                                                         |
| PrimaryVertexRelator :         | GenericParticle2PVRelator\<\_p2PVWithIPChi2, OfflineDistanceCalculatorName\>/P2PVWithIPChi2:PUBLIC        |
| PostMonitor :                  | None                                                                                                      |
| ErrorMax :                     | 1                                                                                                         |
| MassFitters :                  | { }                                                                                                       |
| MonitorService :               | MonitorSvc                                                                                                |
| AuditInitialize :              | True                                                                                                      |
| RegularRowFormat :             | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                    | True                                                                                                      |
| StatPrint :                    | True                                                                                                      |
| Factory :                      | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                   |
| AuditEndRun :                  | True                                                                                                      |
| DistanceCalculators :          | { }                                                                                                       |
| AuditStop :                    | True                                                                                                      |
| PreMonitor :                   | None                                                                                                      |
| P2PVInputLocations :           | [ ]                                                                                                     |
| PropertiesPrint :              | False                                                                                                     |
| PreloadTools :                 | False                                                                                                     |
| ForceP2PVBuild :               | True                                                                                                      |
| OutputPlotsPath :              | OLambdasLLForBu2LLK                                                                                       |
| NeededResources :              | [ ]                                                                                                     |
| Context :                      | None                                                                                                      |
| OutputLevel :                  | 3                                                                                                         |
| ForceOutput :                  | True                                                                                                      |
| DataInputs :                   | None                                                                                                      |
| LifetimeFitters :              | { }                                                                                                       |
| AuditStart :                   | True                                                                                                      |
| HistoProduce :                 | False                                                                                                     |
| InputPrimaryVertices :         | Rec/Vertex/Primary                                                                                        |
| AuditAlgorithms :              | True                                                                                                      |
| DirectionFitters :             | { }                                                                                                       |
| IgnoreP2PVFromInputLocations : | False                                                                                                     |
| CloneFilteredParticles :       | False                                                                                                     |
| IsClonable :                   | False                                                                                                     |
| RegisterForContextService :    | True                                                                                                      |
| CounterList :                  | [ '.\*' ]                                                                                               |
| UseP2PVRelations :             | True                                                                                                      |
| ErrorCounter :                 | 0                                                                                                         |
| AuditReinitialize :            | True                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| DataOutputs :               | None                                                                                                      |
| AuditStart :                | True                                                                                                      |
| DataInputs :                | None                                                                                                      |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| ReturnOK :                  | False                                                                                                     |
| ShortCircuit :              | True                                                                                                      |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| MeasureTime :               | False                                                                                                     |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**GaudiSequencer/SEQ:LambdasDDForBu2LLK**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles**

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseLambdaDD](./stripping21r0p1-stdlooselambdadd) /Particles',True)\>0 |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| DataOutputs :               | None                                                                                                      |
| DataInputs :                | None                                                                                                      |
| Preambulo :                 | [ ]                                                                                                     |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| Factory :                   | LoKi::Hybrid::CoreFactory/CoreFactory:PUBLIC                                                              |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**FilterDesktop/LambdasDDForBu2LLK**

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/ [StdLooseLambdaDD](./stripping21r0p1-stdlooselambdadd) ' ]                                                                          |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/LambdasDDForBu2LLK/Particles                                                                                                              |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | ILambdasDDForBu2LLK                                                                                       |
| Monitor :                      | False                                                                                                     |
| AuditExecute :                 | True                                                                                                      |
| DataOutputs :                  | None                                                                                                      |
| ReFitPVs :                     | False                                                                                                     |
| ParticleCombiners :            | { }                                                                                                       |
| Preambulo :                    | [ ]                                                                                                     |
| PVReFitters :                  | { }                                                                                                       |
| VetoObjects :                  | [ ]                                                                                                     |
| AuditRestart :                 | True                                                                                                      |
| CheckOverlapTool :             | CheckOverlap:PUBLIC                                                                                       |
| StatEntityList :               | [ ]                                                                                                     |
| InputPlotsTool :               | LoKi::Hybrid::PlotTool/InputPlots                                                                         |
| Enable :                       | True                                                                                                      |
| VertexFitters :                | { }                                                                                                       |
| ParticleFilters :              | { }                                                                                                       |
| RequireObjects :               | [ ]                                                                                                     |
| WriteP2PVRelations :           | True                                                                                                      |
| ParticleReFitters :            | { }                                                                                                       |
| RootInTES :                    | None                                                                                                      |
| DecayTreeFitters :             | { }                                                                                                       |
| UseEfficiencyRowFormat :       | True                                                                                                      |
| AuditFinalize :                | True                                                                                                      |
| EfficiencyRowFormat :          | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| GlobalTimeOffset :             | 0.0000000                                                                                                 |
| OutputPlotsTool :              | LoKi::Hybrid::PlotTool/OutputPlots                                                                        |
| ErrorsPrint :                  | True                                                                                                      |
| AuditBeginRun :                | True                                                                                                      |
| Cardinality :                  | 1                                                                                                         |
| PrimaryVertexRelator :         | GenericParticle2PVRelator\<\_p2PVWithIPChi2, OfflineDistanceCalculatorName\>/P2PVWithIPChi2:PUBLIC        |
| PostMonitor :                  | None                                                                                                      |
| ErrorMax :                     | 1                                                                                                         |
| MassFitters :                  | { }                                                                                                       |
| MonitorService :               | MonitorSvc                                                                                                |
| AuditInitialize :              | True                                                                                                      |
| RegularRowFormat :             | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                    | True                                                                                                      |
| StatPrint :                    | True                                                                                                      |
| Factory :                      | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                   |
| AuditEndRun :                  | True                                                                                                      |
| DistanceCalculators :          | { }                                                                                                       |
| AuditStop :                    | True                                                                                                      |
| PreMonitor :                   | None                                                                                                      |
| P2PVInputLocations :           | [ ]                                                                                                     |
| PropertiesPrint :              | False                                                                                                     |
| PreloadTools :                 | False                                                                                                     |
| ForceP2PVBuild :               | True                                                                                                      |
| OutputPlotsPath :              | OLambdasDDForBu2LLK                                                                                       |
| NeededResources :              | [ ]                                                                                                     |
| Context :                      | None                                                                                                      |
| OutputLevel :                  | 3                                                                                                         |
| ForceOutput :                  | True                                                                                                      |
| DataInputs :                   | None                                                                                                      |
| LifetimeFitters :              | { }                                                                                                       |
| AuditStart :                   | True                                                                                                      |
| HistoProduce :                 | False                                                                                                     |
| InputPrimaryVertices :         | Rec/Vertex/Primary                                                                                        |
| AuditAlgorithms :              | True                                                                                                      |
| DirectionFitters :             | { }                                                                                                       |
| IgnoreP2PVFromInputLocations : | False                                                                                                     |
| CloneFilteredParticles :       | False                                                                                                     |
| IsClonable :                   | False                                                                                                     |
| RegisterForContextService :    | True                                                                                                      |
| CounterList :                  | [ '.\*' ]                                                                                               |
| UseP2PVRelations :             | True                                                                                                      |
| ErrorCounter :                 | 0                                                                                                         |
| AuditReinitialize :            | True                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| DataOutputs :               | None                                                                                                      |
| AuditStart :                | True                                                                                                      |
| DataInputs :                | None                                                                                                      |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| ReturnOK :                  | False                                                                                                     |
| ShortCircuit :              | True                                                                                                      |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| MeasureTime :               | False                                                                                                     |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**GaudiSequencer/SEQ:LambdastarsForBu2LLK**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseLambdastar2pK_Particles**

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseLambdastar2pK](./stripping21r0p1-stdlooselambdastar2pk) /Particles',True)\>0 |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| DataOutputs :               | None                                                                                                      |
| DataInputs :                | None                                                                                                      |
| Preambulo :                 | [ ]                                                                                                     |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| Factory :                   | LoKi::Hybrid::CoreFactory/CoreFactory:PUBLIC                                                              |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**FilterDesktop/LambdastarsForBu2LLK**

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 2600\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE(ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/ [StdLooseLambdastar2pK](./stripping21r0p1-stdlooselambdastar2pk) ' ]                                                                |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/LambdastarsForBu2LLK/Particles                                                                                                            |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | ILambdastarsForBu2LLK                                                                                     |
| Monitor :                      | False                                                                                                     |
| AuditExecute :                 | True                                                                                                      |
| DataOutputs :                  | None                                                                                                      |
| ReFitPVs :                     | False                                                                                                     |
| ParticleCombiners :            | { }                                                                                                       |
| Preambulo :                    | [ ]                                                                                                     |
| PVReFitters :                  | { }                                                                                                       |
| VetoObjects :                  | [ ]                                                                                                     |
| AuditRestart :                 | True                                                                                                      |
| CheckOverlapTool :             | CheckOverlap:PUBLIC                                                                                       |
| StatEntityList :               | [ ]                                                                                                     |
| InputPlotsTool :               | LoKi::Hybrid::PlotTool/InputPlots                                                                         |
| Enable :                       | True                                                                                                      |
| VertexFitters :                | { }                                                                                                       |
| ParticleFilters :              | { }                                                                                                       |
| RequireObjects :               | [ ]                                                                                                     |
| WriteP2PVRelations :           | True                                                                                                      |
| ParticleReFitters :            | { }                                                                                                       |
| RootInTES :                    | None                                                                                                      |
| DecayTreeFitters :             | { }                                                                                                       |
| UseEfficiencyRowFormat :       | True                                                                                                      |
| AuditFinalize :                | True                                                                                                      |
| EfficiencyRowFormat :          | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| GlobalTimeOffset :             | 0.0000000                                                                                                 |
| OutputPlotsTool :              | LoKi::Hybrid::PlotTool/OutputPlots                                                                        |
| ErrorsPrint :                  | True                                                                                                      |
| AuditBeginRun :                | True                                                                                                      |
| Cardinality :                  | 1                                                                                                         |
| PrimaryVertexRelator :         | GenericParticle2PVRelator\<\_p2PVWithIPChi2, OfflineDistanceCalculatorName\>/P2PVWithIPChi2:PUBLIC        |
| PostMonitor :                  | None                                                                                                      |
| ErrorMax :                     | 1                                                                                                         |
| MassFitters :                  | { }                                                                                                       |
| MonitorService :               | MonitorSvc                                                                                                |
| AuditInitialize :              | True                                                                                                      |
| RegularRowFormat :             | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                    | True                                                                                                      |
| StatPrint :                    | True                                                                                                      |
| Factory :                      | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                   |
| AuditEndRun :                  | True                                                                                                      |
| DistanceCalculators :          | { }                                                                                                       |
| AuditStop :                    | True                                                                                                      |
| PreMonitor :                   | None                                                                                                      |
| P2PVInputLocations :           | [ ]                                                                                                     |
| PropertiesPrint :              | False                                                                                                     |
| PreloadTools :                 | False                                                                                                     |
| ForceP2PVBuild :               | True                                                                                                      |
| OutputPlotsPath :              | OLambdastarsForBu2LLK                                                                                     |
| NeededResources :              | [ ]                                                                                                     |
| Context :                      | None                                                                                                      |
| OutputLevel :                  | 3                                                                                                         |
| ForceOutput :                  | True                                                                                                      |
| DataInputs :                   | None                                                                                                      |
| LifetimeFitters :              | { }                                                                                                       |
| AuditStart :                   | True                                                                                                      |
| HistoProduce :                 | False                                                                                                     |
| InputPrimaryVertices :         | Rec/Vertex/Primary                                                                                        |
| AuditAlgorithms :              | True                                                                                                      |
| DirectionFitters :             | { }                                                                                                       |
| IgnoreP2PVFromInputLocations : | False                                                                                                     |
| CloneFilteredParticles :       | False                                                                                                     |
| IsClonable :                   | False                                                                                                     |
| RegisterForContextService :    | True                                                                                                      |
| CounterList :                  | [ '.\*' ]                                                                                               |
| UseP2PVRelations :             | True                                                                                                      |
| ErrorCounter :                 | 0                                                                                                         |
| AuditReinitialize :            | True                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| DataOutputs :               | None                                                                                                      |
| AuditStart :                | True                                                                                                      |
| DataInputs :                | None                                                                                                      |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| ReturnOK :                  | False                                                                                                     |
| ShortCircuit :              | True                                                                                                      |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| MeasureTime :               | False                                                                                                     |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**GaudiSequencer/SEQ:K1ForBu2LLK**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKaons](./stripping21r0p1-stdloosekaons) /Particles',True)\>0 |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| DataOutputs :               | None                                                                                                      |
| DataInputs :                | None                                                                                                      |
| Preambulo :                 | [ ]                                                                                                     |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| Factory :                   | LoKi::Hybrid::CoreFactory/CoreFactory:PUBLIC                                                              |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePions](./stripping21r0p1-stdloosepions) /Particles',True)\>0 |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| DataOutputs :               | None                                                                                                      |
| DataInputs :                | None                                                                                                      |
| Preambulo :                 | [ ]                                                                                                     |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| Factory :                   | LoKi::Hybrid::CoreFactory/CoreFactory:PUBLIC                                                              |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**CombineParticles/K1ForBu2LLK**

|                  |                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseKaons](./stripping21r0p1-stdloosekaons) ' , 'Phys/ [StdLoosePions](./stripping21r0p1-stdloosepions) ' ]                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.4)' , 'K-' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.4)' , 'pi+' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.4)' , 'pi-' : '(TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.4)' } |
| CombinationCut   | (AM \> 0\*MeV) & (AM \< 6000\*MeV) & ((APT1+APT2+APT3) \> 800\*MeV)                                                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2) \< 12) & (SUMTREE(MIPCHI2DV(PRIMARY),((ABSID=='K+') \| (ABSID=='K-') \| (ABSID=='pi+') \| (ABSID=='pi-')),0.0) \> 48.0)                                                                                       |
| DecayDescriptor  | [K_1(1270)+ -\> K+ pi+ pi-]cc                                                                                                                                                                                              |
| DecayDescriptors | [ '[K_1(1270)+ -\> K+ pi+ pi-]cc' ]                                                                                                                                                                                      |
| Output           | Phys/K1ForBu2LLK/Particles                                                                                                                                                                                                   |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| Monitor :                      | False                                                                                                     |
| AuditExecute :                 | True                                                                                                      |
| PropertiesPrint :              | False                                                                                                     |
| DataOutputs :                  | None                                                                                                      |
| ReFitPVs :                     | False                                                                                                     |
| ParticleCombiners :            | { }                                                                                                       |
| Preambulo :                    | [ ]                                                                                                     |
| PVReFitters :                  | { }                                                                                                       |
| VetoObjects :                  | [ ]                                                                                                     |
| AuditRestart :                 | True                                                                                                      |
| CheckOverlapTool :             | CheckOverlap:PUBLIC                                                                                       |
| MonitorService :               | MonitorSvc                                                                                                |
| Enable :                       | True                                                                                                      |
| VertexFitters :                | { }                                                                                                       |
| DirectionFitters :             | { }                                                                                                       |
| RequireObjects :               | [ ]                                                                                                     |
| WriteP2PVRelations :           | True                                                                                                      |
| ParticleReFitters :            | { }                                                                                                       |
| RootInTES :                    | None                                                                                                      |
| DecayTreeFitters :             | { }                                                                                                       |
| AuditFinalize :                | True                                                                                                      |
| CombinationPlots :             | LoKi::Hybrid::PlotTool/CombinationPlots                                                                   |
| HistoProduce :                 | False                                                                                                     |
| AuditEndRun :                  | True                                                                                                      |
| UseEfficiencyRowFormat :       | True                                                                                                      |
| AuditBeginRun :                | True                                                                                                      |
| Cardinality :                  | 1                                                                                                         |
| IsClonable :                   | False                                                                                                     |
| PrimaryVertexRelator :         | GenericParticle2PVRelator\<\_p2PVWithIPChi2, OfflineDistanceCalculatorName\>/P2PVWithIPChi2:PUBLIC        |
| ErrorMax :                     | 1                                                                                                         |
| MotherMonitor :                | None                                                                                                      |
| MassFitters :                  | { }                                                                                                       |
| MaxCandidates :                | 2000                                                                                                      |
| MotherPlots :                  | LoKi::Hybrid::PlotTool/MotherPlots                                                                        |
| DaughtersPlots :               | LoKi::Hybrid::PlotTool/DaughtersPlots                                                                     |
| StatEntityList :               | [ ]                                                                                                     |
| AuditInitialize :              | True                                                                                                      |
| RegularRowFormat :             | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                    | True                                                                                                      |
| MotherPlotsPath :              | None                                                                                                      |
| StatPrint :                    | True                                                                                                      |
| Factory :                      | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                   |
| ForceOutput :                  | True                                                                                                      |
| DistanceCalculators :          | { }                                                                                                       |
| AuditStop :                    | True                                                                                                      |
| P2PVInputLocations :           | [ ]                                                                                                     |
| ErrorsPrint :                  | True                                                                                                      |
| PreloadTools :                 | False                                                                                                     |
| ForceP2PVBuild :               | True                                                                                                      |
| GlobalTimeOffset :             | 0.0000000                                                                                                 |
| NeededResources :              | [ ]                                                                                                     |
| CombinationMonitor :           | None                                                                                                      |
| CounterList :                  | [ '.\*' ]                                                                                               |
| Context :                      | None                                                                                                      |
| StopAtMaxCombinations :        | False                                                                                                     |
| DaughtersMonitors :            | { }                                                                                                       |
| OutputLevel :                  | 3                                                                                                         |
| StopAtMaxCandidates :          | True                                                                                                      |
| DataInputs :                   | None                                                                                                      |
| LifetimeFitters :              | { }                                                                                                       |
| AuditStart :                   | True                                                                                                      |
| StopIncidentType :             | ExceedsCombinatoricsLimit                                                                                 |
| InputPrimaryVertices :         | Rec/Vertex/Primary                                                                                        |
| AuditAlgorithms :              | True                                                                                                      |
| ParticleFilters :              | { }                                                                                                       |
| IgnoreP2PVFromInputLocations : | False                                                                                                     |
| MaxCombinations :              | 0                                                                                                         |
| DaughtersPlotsPath :           | None                                                                                                      |
| CombinationPlotsPath :         | None                                                                                                      |
| RegisterForContextService :    | True                                                                                                      |
| EfficiencyRowFormat :          | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| UseP2PVRelations :             | True                                                                                                      |
| ErrorCounter :                 | 0                                                                                                         |
| AuditReinitialize :            | True                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| DataOutputs :               | None                                                                                                      |
| AuditStart :                | True                                                                                                      |
| DataInputs :                | None                                                                                                      |
| VetoObjects :               | [ ]                                                                                                     |
| AuditRestart :              | True                                                                                                      |
| StatEntityList :            | [ ]                                                                                                     |
| Enable :                    | True                                                                                                      |
| RequireObjects :            | [ ]                                                                                                     |
| RootInTES :                 | None                                                                                                      |
| AuditFinalize :             | True                                                                                                      |
| AuditEndRun :               | True                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| Cardinality :               | 1                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                 | True                                                                                                      |
| StatPrint :                 | True                                                                                                      |
| ReturnOK :                  | False                                                                                                     |
| ShortCircuit :              | True                                                                                                      |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| NeededResources :           | [ ]                                                                                                     |
| CounterList :               | [ '.\*' ]                                                                                               |
| OutputLevel :               | 3                                                                                                         |
| MeasureTime :               | False                                                                                                     |
| UseEfficiencyRowFormat :    | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| IsClonable :                | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorCounter :              | 0                                                                                                         |
| AuditReinitialize :         | True                                                                                                      |

**FilterDesktop/MergeBu2LLK_ee3**

|                 |                                                                                                                                                                |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                            |
| Inputs          | [ 'Phys/K1ForBu2LLK' , 'Phys/KstarsForBu2LLK' , 'Phys/LambdasDDForBu2LLK' , 'Phys/LambdasLLForBu2LLK' , 'Phys/LambdastarsForBu2LLK' , 'Phys/PhisForBu2LLK' ] |
| DecayDescriptor | None                                                                                                                                                           |
| Output          | Phys/MergeBu2LLK_ee3/Particles                                                                                                                                 |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IMergeBu2LLK_ee3                                                                                          |
| Monitor :                      | False                                                                                                     |
| AuditExecute :                 | True                                                                                                      |
| DataOutputs :                  | None                                                                                                      |
| ReFitPVs :                     | False                                                                                                     |
| ParticleCombiners :            | { }                                                                                                       |
| Preambulo :                    | [ ]                                                                                                     |
| PVReFitters :                  | { }                                                                                                       |
| VetoObjects :                  | [ ]                                                                                                     |
| AuditRestart :                 | True                                                                                                      |
| CheckOverlapTool :             | CheckOverlap:PUBLIC                                                                                       |
| StatEntityList :               | [ ]                                                                                                     |
| InputPlotsTool :               | LoKi::Hybrid::PlotTool/InputPlots                                                                         |
| Enable :                       | True                                                                                                      |
| VertexFitters :                | { }                                                                                                       |
| ParticleFilters :              | { }                                                                                                       |
| RequireObjects :               | [ ]                                                                                                     |
| WriteP2PVRelations :           | True                                                                                                      |
| ParticleReFitters :            | { }                                                                                                       |
| RootInTES :                    | None                                                                                                      |
| DecayTreeFitters :             | { }                                                                                                       |
| UseEfficiencyRowFormat :       | True                                                                                                      |
| AuditFinalize :                | True                                                                                                      |
| EfficiencyRowFormat :          | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| GlobalTimeOffset :             | 0.0000000                                                                                                 |
| OutputPlotsTool :              | LoKi::Hybrid::PlotTool/OutputPlots                                                                        |
| ErrorsPrint :                  | True                                                                                                      |
| AuditBeginRun :                | True                                                                                                      |
| Cardinality :                  | 1                                                                                                         |
| PrimaryVertexRelator :         | GenericParticle2PVRelator\<\_p2PVWithIPChi2, OfflineDistanceCalculatorName\>/P2PVWithIPChi2:PUBLIC        |
| PostMonitor :                  | None                                                                                                      |
| ErrorMax :                     | 1                                                                                                         |
| MassFitters :                  | { }                                                                                                       |
| MonitorService :               | MonitorSvc                                                                                                |
| AuditInitialize :              | True                                                                                                      |
| RegularRowFormat :             | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| TypePrint :                    | True                                                                                                      |
| StatPrint :                    | True                                                                                                      |
| Factory :                      | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                   |
| AuditEndRun :                  | True                                                                                                      |
| DistanceCalculators :          | { }                                                                                                       |
| AuditStop :                    | True                                                                                                      |
| PreMonitor :                   | None                                                                                                      |
| P2PVInputLocations :           | [ ]                                                                                                     |
| PropertiesPrint :              | False                                                                                                     |
| PreloadTools :                 | False                                                                                                     |
| ForceP2PVBuild :               | True                                                                                                      |
| OutputPlotsPath :              | OMergeBu2LLK_ee3                                                                                          |
| NeededResources :              | [ ]                                                                                                     |
| Context :                      | None                                                                                                      |
| OutputLevel :                  | 3                                                                                                         |
| ForceOutput :                  | True                                                                                                      |
| DataInputs :                   | None                                                                                                      |
| LifetimeFitters :              | { }                                                                                                       |
| AuditStart :                   | True                                                                                                      |
| HistoProduce :                 | False                                                                                                     |
| InputPrimaryVertices :         | Rec/Vertex/Primary                                                                                        |
| AuditAlgorithms :              | True                                                                                                      |
| DirectionFitters :             | { }                                                                                                       |
| IgnoreP2PVFromInputLocations : | False                                                                                                     |
| CloneFilteredParticles :       | False                                                                                                     |
| IsClonable :                   | False                                                                                                     |
| RegisterForContextService :    | True                                                                                                      |
| CounterList :                  | [ '.\*' ]                                                                                               |
| UseP2PVRelations :             | True                                                                                                      |
| ErrorCounter :                 | 0                                                                                                         |
| AuditReinitialize :            | True                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaLL_Particles**

|      |                                                                                                 |
|------|-------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseGammaLL](./stripping21r0p1-stdallloosegammall) /Particles',True)\>0 |

**FilterDesktop/SelPhotonForBu2LLK**

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 1000\*MeV) & (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 9)               |
| Inputs          | [ 'Phys/ [StdAllLooseGammaLL](./stripping21r0p1-stdallloosegammall) ' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/SelPhotonForBu2LLK/Particles                                         |

**CombineParticles/Bu2LLK_eeLine3**

|                  |                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_ee3' , 'Phys/SelPhotonForBu2LLK' ]                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)\~0' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda\~0' : 'ALL' , 'gamma' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 1500 \*MeV                                                                                                                                                                          |
| MotherCut        | ((VFASPF(VCHI2/VDOF) \< 9) & (BPVIPCHI2() \< 25) & (BPVDIRA \> 0.9995) & (BPVVDCHI2 \> 100))                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                                                 |
| DecayDescriptors | [ '[ B0 -\> gamma K\*(892)0 ]cc' , '[ B_s0 -\> gamma phi(1020) ]cc' , '[ Lambda_b0 -\> gamma Lambda0 ]cc' , '[ Lambda_b0 -\> gamma Lambda(1520)0 ]cc' ]                                    |
| Output           | Phys/Bu2LLK_eeLine3/Particles                                                                                                                                                                        |

**AddRelatedInfo/RelatedInfo1_Bu2LLK_eeLine3**

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo1_Bu2LLK_eeLine3/Particles |

**AddRelatedInfo/RelatedInfo2_Bu2LLK_eeLine3**

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo2_Bu2LLK_eeLine3/Particles |

**AddRelatedInfo/RelatedInfo3_Bu2LLK_eeLine3**

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo3_Bu2LLK_eeLine3/Particles |

**AddRelatedInfo/RelatedInfo4_Bu2LLK_eeLine3**

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo4_Bu2LLK_eeLine3/Particles |

**AddRelatedInfo/RelatedInfo5_Bu2LLK_eeLine3**

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo5_Bu2LLK_eeLine3/Particles |

**AddRelatedInfo/RelatedInfo6_Bu2LLK_eeLine3**

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_eeLine3' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo6_Bu2LLK_eeLine3/Particles |
