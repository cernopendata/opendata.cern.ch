[[stripping21r1 lines]](./stripping21r1-index)

# StrippingJets_4jets_Pt5_0sv_Prescaled

## Properties:

|                |                                             |
|----------------|---------------------------------------------|
| OutputLocation | Phys/Jets_4jets_Pt5_0sv_Prescaled/Particles |
| Postscale      | 1.0000000                                   |
| HLT            | HLT_PASS_RE('Hlt2Topo.\*Decision')          |
| Prescale       | 0.010000000                                 |
| L0DU           | None                                        |
| ODIN           | None                                        |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdJets_Particles**

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdJets](./stripping21r1-stdjets) /Particles')\>0 |

**FilterDesktop/Jets5000.0GeVJets**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | (PT \> 5000.0)                                    |
| Inputs          | [ 'Phys/ [StdJets](./stripping21r1-stdjets) ' ] |
| DecayDescriptor | None                                              |
| Output          | Phys/Jets5000.0GeVJets/Particles                  |

**GaudiSequencer/SeqJetsmerged**

**Members:**

**GaudiSequencer/SEQ:Jets5000.0GeVJets**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdJets_Particles**

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdJets](./stripping21r1-stdjets) /Particles')\>0 |

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

**FilterDesktop/Jets5000.0GeVJets**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | (PT \> 5000.0)                                    |
| Inputs          | [ 'Phys/ [StdJets](./stripping21r1-stdjets) ' ] |
| DecayDescriptor | None                                              |
| Output          | Phys/Jets5000.0GeVJets/Particles                  |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IJets5000.0GeVJets                                                                                        |
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
| OutputPlotsPath :              | OJets5000.0GeVJets                                                                                        |
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
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| AuditReinitialize :         | True                                                                                                      |
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
| UseEfficiencyRowFormat :    | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| ErrorCount :                | 0                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :               | 3                                                                                                         |
| StatPrint :                 | True                                                                                                      |
| ShortCircuit :              | True                                                                                                      |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| MeasureTime :               | False                                                                                                     |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| ReturnOK :                  | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :               | [ '.\*' ]                                                                                               |

**GaudiSequencer/SEQ:JetsSvrsSelection**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllNoPIDsPions](./stripping21r1-stdallnopidspions) /Particles')\>0 |

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

**FilterDesktop/JetsTrksSelection**

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 500.0) & (P \> 5000.0) & (MIPCHI2DV(PRIMARY) \> 16) & (TRGHP \< 0.4) & (PPINFO(705,-1) \< 0.7) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21r1-stdallnopidspions) ' ]                                 |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/JetsTrksSelection/Particles                                                                      |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IJetsTrksSelection                                                                                        |
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
| OutputPlotsPath :              | OJetsTrksSelection                                                                                        |
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

**CombineParticles/JetsSvrsSelection**

|                  |                                                              |
|------------------|--------------------------------------------------------------|
| Inputs           | [ 'Phys/JetsTrksSelection' ]                               |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }               |
| CombinationCut   | (ADOCACHI2CUT(8,'')) & (AM \< 7000.0) & (ASUM(PT) \> 2000.0) |
| MotherCut        | (BPVDIRA \> 0) & (BPVVDCHI2 \> 100) & (VFASPF(VCHI2) \< 8)   |
| DecayDescriptor  | None                                                         |
| DecayDescriptors | [ 'D0 -\> pi- pi+' , 'D0 -\> pi- pi-' , 'D0 -\> pi+ pi+' ] |
| Output           | Phys/JetsSvrsSelection/Particles                             |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| Monitor :                      | False                                                                                                     |
| AuditExecute :                 | True                                                                                                      |
| Factory :                      | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                   |
| ReFitPVs :                     | False                                                                                                     |
| ParticleCombiners :            | { }                                                                                                       |
| Preambulo :                    | [ ]                                                                                                     |
| PVReFitters :                  | { }                                                                                                       |
| VetoObjects :                  | [ ]                                                                                                     |
| AuditRestart :                 | True                                                                                                      |
| CheckOverlapTool :             | CheckOverlap:PUBLIC                                                                                       |
| MonitorService :               | MonitorSvc                                                                                                |
| Enable :                       | True                                                                                                      |
| RootOnTES :                    | None                                                                                                      |
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
| RegularRowFormat :             | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| AuditEndRun :                  | True                                                                                                      |
| ErrorsPrint :                  | True                                                                                                      |
| AuditBeginRun :                | True                                                                                                      |
| DaughtersMonitors :            | { }                                                                                                       |
| ErrorCount :                   | 0                                                                                                         |
| ErrorMax :                     | 1                                                                                                         |
| MotherMonitor :                | None                                                                                                      |
| MassFitters :                  | { }                                                                                                       |
| MaxCandidates :                | 2000                                                                                                      |
| MotherPlots :                  | LoKi::Hybrid::PlotTool/MotherPlots                                                                        |
| StatEntityList :               | [ ]                                                                                                     |
| AuditInitialize :              | True                                                                                                      |
| PrimaryVertexRelator :         | GenericParticle2PVRelator\<\_p2PVWithIPChi2, OfflineDistanceCalculatorName\>/P2PVWithIPChi2:PUBLIC        |
| TypePrint :                    | True                                                                                                      |
| MotherPlotsPath :              | None                                                                                                      |
| StatPrint :                    | True                                                                                                      |
| CombinationMonitor :           | None                                                                                                      |
| DaughtersPlots :               | LoKi::Hybrid::PlotTool/DaughtersPlots                                                                     |
| ForceOutput :                  | True                                                                                                      |
| DistanceCalculators :          | { }                                                                                                       |
| AuditStop :                    | True                                                                                                      |
| P2PVInputLocations :           | [ ]                                                                                                     |
| PropertiesPrint :              | False                                                                                                     |
| PreloadTools :                 | False                                                                                                     |
| ForceP2PVBuild :               | True                                                                                                      |
| GlobalTimeOffset :             | 0.0000000                                                                                                 |
| CombinationPlotsPath :         | None                                                                                                      |
| Context :                      | None                                                                                                      |
| StopAtMaxCombinations :        | False                                                                                                     |
| UseEfficiencyRowFormat :       | True                                                                                                      |
| OutputLevel :                  | 3                                                                                                         |
| StopAtMaxCandidates :          | True                                                                                                      |
| AuditReinitialize :            | True                                                                                                      |
| LifetimeFitters :              | { }                                                                                                       |
| AuditStart :                   | True                                                                                                      |
| StopIncidentType :             | ExceedsCombinatoricsLimit                                                                                 |
| InputPrimaryVertices :         | Rec/Vertex/Primary                                                                                        |
| AuditAlgorithms :              | True                                                                                                      |
| ParticleFilters :              | { }                                                                                                       |
| IgnoreP2PVFromInputLocations : | False                                                                                                     |
| MaxCombinations :              | 0                                                                                                         |
| RegisterForContextService :    | True                                                                                                      |
| EfficiencyRowFormat :          | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| UseP2PVRelations :             | True                                                                                                      |
| DaughtersPlotsPath :           | None                                                                                                      |
| CounterList :                  | [ '.\*' ]                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                             |                                                                                                           |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :           | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| AuditExecute :              | True                                                                                                      |
| PropertiesPrint :           | False                                                                                                     |
| AuditReinitialize :         | True                                                                                                      |
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
| UseEfficiencyRowFormat :    | True                                                                                                      |
| AuditBeginRun :             | True                                                                                                      |
| ErrorCount :                | 0                                                                                                         |
| ErrorMax :                  | 1                                                                                                         |
| MonitorService :            | MonitorSvc                                                                                                |
| AuditInitialize :           | True                                                                                                      |
| RegularRowFormat :          | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :               | 3                                                                                                         |
| StatPrint :                 | True                                                                                                      |
| ShortCircuit :              | True                                                                                                      |
| AuditStop :                 | True                                                                                                      |
| Context :                   | None                                                                                                      |
| ErrorsPrint :               | True                                                                                                      |
| GlobalTimeOffset :          | 0.0000000                                                                                                 |
| MeasureTime :               | False                                                                                                     |
| AuditStart :                | True                                                                                                      |
| RegisterForContextService : | True                                                                                                      |
| AuditAlgorithms :           | True                                                                                                      |
| ReturnOK :                  | False                                                                                                     |
| EfficiencyRowFormat :       | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :               | [ '.\*' ]                                                                                               |

**FilterDesktop/Jetsmerged**

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | ALL                                                       |
| Inputs          | [ 'Phys/Jets5000.0GeVJets' , 'Phys/JetsSvrsSelection' ] |
| DecayDescriptor | None                                                      |
| Output          | Phys/Jetsmerged/Particles                                 |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IJetsmerged                                                                                               |
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
| OutputPlotsPath :              | OJetsmerged                                                                                               |
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

**TopologicalTagging/JetsbJets**

|                 |                          |
|-----------------|--------------------------|
| Inputs          | [ 'Phys/Jetsmerged' ]  |
| DecayDescriptor | None                     |
| Output          | Phys/JetsbJets/Particles |

****Tools:****

**TriggerTisTos**

|                                 |                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :               | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| UseParticle2LHCbIDsMap :        | 1                                                                                                         |
| AllowIntermediateSelections :   | False                                                                                                     |
| Particle2LHCbIDsMapLocation :   | None                                                                                                      |
| CompositeTPSviaPartialTOSonly : | False                                                                                                     |
| TriggerInputWarnings :          | False                                                                                                     |
| StatEntityList :                | [ ]                                                                                                     |
| RootOnTES :                     | None                                                                                                      |
| CaloClustForCharged :           | True                                                                                                      |
| TOSFracTT :                     | 0.0000000                                                                                                 |
| TISFracEcal :                   | 0.0099000000                                                                                              |
| TOSFracHcal :                   | 0.010000000                                                                                               |
| RootInTES :                     | None                                                                                                      |
| HltSelReportsLocation :         | Hlt/SelReports                                                                                            |
| AuditFinalize :                 | False                                                                                                     |
| TISFracVelo :                   | 0.010000000                                                                                               |
| ProjectTracksToCalo :           | True                                                                                                      |
| ErrorsPrint :                   | True                                                                                                      |
| ContextService :                | AlgContextSvc                                                                                             |
| AuditTools :                    | False                                                                                                     |
| HltDecReportsLocation :         | Hlt/DecReports                                                                                            |
| TISFracTT :                     | 0.010000000                                                                                               |
| MonitorService :                | MonitorSvc                                                                                                |
| AuditInitialize :               | False                                                                                                     |
| RegularRowFormat :              | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| CaloClustForNeutral :           | True                                                                                                      |
| TypePrint :                     | True                                                                                                      |
| StatPrint :                     | True                                                                                                      |
| TISFracMuon :                   | 0.00010000000                                                                                             |
| TISFracHcal :                   | 0.0099000000                                                                                              |
| AuditStop :                     | False                                                                                                     |
| Context :                       | None                                                                                                      |
| PropertiesPrint :               | False                                                                                                     |
| GlobalTimeOffset :              | 0.0000000                                                                                                 |
| UseEfficiencyRowFormat :        | True                                                                                                      |
| OutputLevel :                   | 3                                                                                                         |
| TOSFracEcal :                   | 0.010000000                                                                                               |
| TOSFracMuon :                   | 0.00010000000                                                                                             |
| AuditStart :                    | False                                                                                                     |
| NoHitTypes :                    | False                                                                                                     |
| TISFracOTIT :                   | 0.010000000                                                                                               |
| TOSFracOTIT :                   | 0.70000000                                                                                                |
| TOSFracVelo :                   | 0.70000000                                                                                                |
| EfficiencyRowFormat :           | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| FullAnalysisReport :            | True                                                                                                      |
| CounterList :                   | [ '.\*' ]                                                                                               |

**CombineParticles/Jets_4jets_Pt5_0sv_Prescaled**

|                  |                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Jets5000.0GeVJets' , 'Phys/JetsbJets' ]                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : '(PT \> 5000.0)' }                                                                                                             |
| CombinationCut   | (abs(ACHILD(BPV(VZ),1)-ACHILD(BPV(VZ),2))\<1\*mm) & (abs(ACHILD(BPV(VZ),1)-ACHILD(BPV(VZ),3))\<1\*mm) & (abs(ACHILD(BPV(VZ),1)-ACHILD(BPV(VZ),4))\<1\*mm) |
| MotherCut        | ((INTREE((ABSID=='CELLjet')&(PT\>0.0)))&(INTREE((ABSID=='CELLjet')&(PINFO(9990,0)\>0)))&(-0.5 \< NINTREE((ABSID=='CELLjet')&(PINFO(9991,0) \> 5 ))))      |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet CELLjet CELLjet                                                                                                                  |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet CELLjet CELLjet' ]                                                                                                          |
| Output           | Phys/Jets_4jets_Pt5_0sv_Prescaled/Particles                                                                                                               |
