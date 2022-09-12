[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBeauty2XGamma2pi_2Ks_Line

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/Beauty2XGamma2pi_2Ks_Line/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsPions /Particles',True) |

**FilterDesktop/TrackListBeauty2XGamma**

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (HASTRACK) & (TRCHI2DOF \< 3.0)& (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.4) & (PT \> 300.0) & (P \> 1000) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21r0p2-stdallnopidspions) ' ]                                            |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/TrackListBeauty2XGamma/Particles                                                                              |

**GaudiSequencer/MERGED:MergedKshorts**

**Members:**

**GaudiSequencer/MERGEDINPUTS:MergedKshorts**

**Members:**

**GaudiSequencer/INPUT:Phys/StdLooseKsDD**

**Members:**

**LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD**

|      |                                  |
|------|----------------------------------|
| Code | 0 StdLooseKsDD /Particles',True) |

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

**GaudiSequencer/INPUT:Phys/StdLooseKsLL**

**Members:**

**LoKi::VoidFilter/SELECT:Phys/StdLooseKsLL**

|      |                                  |
|------|----------------------------------|
| Code | 0 StdLooseKsLL /Particles',True) |

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

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
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
| ShortCircuit :              | False                                                                                                     |
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

**FilterDesktop/MergedKshorts**

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                     |
| Inputs          | [ 'Phys/ [StdLooseKsDD](./stripping21r0p2-stdlooseksdd) ' , 'Phys/ [StdLooseKsLL](./stripping21r0p2-stdlooseksll) ' ] |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/MergedKshorts/Particles                                                                                            |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IMergedKshorts                                                                                            |
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
| OutputPlotsPath :              | OMergedKshorts                                                                                            |
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

**FilterDesktop/KS0SelBeauty2XGamma**

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000) & (MM \> 480\*MeV) & (MM \< 515\*MeV) & (HASVERTEX) & (VFASPF(VCHI2/VDOF)\<9) |
| Inputs          | [ 'Phys/MergedKshorts' ]                                                                 |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/KS0SelBeauty2XGamma/Particles                                                         |

**CombineParticles/Track_wKs0ForRadiativeBBeauty2XGamma**

|                  |                                                                          |
|------------------|--------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS0SelBeauty2XGamma' , 'Phys/TrackListBeauty2XGamma' ]         |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }           |
| CombinationCut   | (ASUM(PT) \> 1000.0) & in_range( 0.0 , AM ,7900.0)                       |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 10.0) & (MIPCHI2DV(PRIMARY) \> 0.0) |
| DecayDescriptor  | [rho(770)+ -\> pi+ KS0]cc                                              |
| DecayDescriptors | [ '[rho(770)+ -\> pi+ KS0]cc' ]                                      |
| Output           | Phys/Track_wKs0ForRadiativeBBeauty2XGamma/Particles                      |

**CombineParticles/DiTracks_w2KS0ForRadiativeBBeauty2XGamma**

|                  |                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Track_wKs0ForRadiativeBBeauty2XGamma' ]                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'rho(770)+' : 'ALL' , 'rho(770)-' : 'ALL' }                                                    |
| CombinationCut   | (ASUM(PT) \> 1000.0) & in_range( 0.0 , AM ,7900.0)                                                            |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 10.0) & (PT \> 150.0) & (BPVVDCHI2 \> 0.0) & (MIPCHI2DV(PRIMARY) \> 0.0) |
| DecayDescriptor  | f_2(1270) -\> rho(770)+ rho(770)-                                                                             |
| DecayDescriptors | [ 'f_2(1270) -\> rho(770)+ rho(770)-' ]                                                                     |
| Output           | Phys/DiTracks_w2KS0ForRadiativeBBeauty2XGamma/Particles                                                       |

**LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons**

|      |                                        |
|------|----------------------------------------|
| Code | 0 StdLooseAllPhotons /Particles',True) |

**FilterDesktop/PhotonSelBeauty2XGamma**

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 2000.0) & (CL \> 0.0)                                              |
| Inputs          | [ 'Phys/ [StdLooseAllPhotons](./stripping21r0p2-stdlooseallphotons) ' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/PhotonSelBeauty2XGamma/Particles                                     |

**CombineParticles/Beauty2XGamma2pi_2Ks\_**

|                  |                                                                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DiTracks_w2KS0ForRadiativeBBeauty2XGamma' , 'Phys/PhotonSelBeauty2XGamma' ]                                                                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'f_2(1270)' : 'ALL' , 'gamma' : 'ALL' }                                                                                                                                                                              |
| CombinationCut   | in_range( 2000.0 ,AM, 9000 ) & (ASUM(PT) \> 3000 )                                                                                                                                                                                  |
| MotherCut        | INTREE(ISBASIC & ((HASTRACK) & (P\>5000\*MeV) & (PT\>1000\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 9.0 ) & (BPVIPCHI2() \< 9.0 ) & (BPVDIRA \> 0.0) |
| DecayDescriptor  | B0 -\> f_2(1270) gamma                                                                                                                                                                                                              |
| DecayDescriptors | [ 'B0 -\> f_2(1270) gamma' ]                                                                                                                                                                                                      |
| Output           | Phys/Beauty2XGamma2pi_2Ks\_/Particles                                                                                                                                                                                               |

**TisTosParticleTagger/Beauty2XGamma2pi_2Ks_Line**

|                 |                                                                                                                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_2Ks\_' ]                                                                                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                                                      |
| Output          | Phys/Beauty2XGamma2pi_2Ks_Line/Particles                                                                                                                                                                                                  |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Radiative.\*Decision%TIS' : 0 , 'Hlt2Radiative.\*Decision%TOS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |

****Tools:****

**TriggerTisTosTool**

|                                 |                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :               | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| UseParticle2LHCbIDsMap :        | 1                                                                                                         |
| AllowIntermediateSelections :   | False                                                                                                     |
| Particle2LHCbIDsMapLocation :   | None                                                                                                      |
| CompositeTPSviaPartialTOSonly : | False                                                                                                     |
| TriggerInputWarnings :          | False                                                                                                     |
| StatEntityList :                | [ ]                                                                                                     |
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

**Hlt2TriggerTisTosTool**

|                                 |                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :               | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| UseParticle2LHCbIDsMap :        | 1                                                                                                         |
| AllowIntermediateSelections :   | False                                                                                                     |
| Particle2LHCbIDsMapLocation :   | None                                                                                                      |
| CompositeTPSviaPartialTOSonly : | False                                                                                                     |
| TriggerInputWarnings :          | False                                                                                                     |
| StatEntityList :                | [ ]                                                                                                     |
| CaloClustForCharged :           | True                                                                                                      |
| TOSFracTT :                     | 0.0000000                                                                                                 |
| TISFracEcal :                   | 0.0099000000                                                                                              |
| TOSFracHcal :                   | 0.010000000                                                                                               |
| RootInTES :                     | None                                                                                                      |
| HltSelReportsLocation :         | Hlt2/SelReports                                                                                           |
| AuditFinalize :                 | False                                                                                                     |
| TISFracVelo :                   | 0.010000000                                                                                               |
| ProjectTracksToCalo :           | True                                                                                                      |
| ErrorsPrint :                   | True                                                                                                      |
| ContextService :                | AlgContextSvc                                                                                             |
| AuditTools :                    | False                                                                                                     |
| HltDecReportsLocation :         | Hlt2/DecReports                                                                                           |
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

**AddRelatedInfo/RelatedInfo1_Beauty2XGamma2pi_2Ks_Line**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_2Ks_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo1_Beauty2XGamma2pi_2Ks_Line/Particles |

**AddRelatedInfo/RelatedInfo2_Beauty2XGamma2pi_2Ks_Line**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_2Ks_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo2_Beauty2XGamma2pi_2Ks_Line/Particles |

**AddRelatedInfo/RelatedInfo3_Beauty2XGamma2pi_2Ks_Line**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_2Ks_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo3_Beauty2XGamma2pi_2Ks_Line/Particles |

**AddRelatedInfo/RelatedInfo4_Beauty2XGamma2pi_2Ks_Line**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_2Ks_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo4_Beauty2XGamma2pi_2Ks_Line/Particles |

**AddRelatedInfo/RelatedInfo5_Beauty2XGamma2pi_2Ks_Line**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_2Ks_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo5_Beauty2XGamma2pi_2Ks_Line/Particles |

**AddRelatedInfo/RelatedInfo6_Beauty2XGamma2pi_2Ks_Line**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_2Ks_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo6_Beauty2XGamma2pi_2Ks_Line/Particles |

**AddRelatedInfo/RelatedInfo7_Beauty2XGamma2pi_2Ks_Line**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_2Ks_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo7_Beauty2XGamma2pi_2Ks_Line/Particles |

**AddRelatedInfo/RelatedInfo8_Beauty2XGamma2pi_2Ks_Line**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_2Ks_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo8_Beauty2XGamma2pi_2Ks_Line/Particles |

**AddRelatedInfo/RelatedInfo9_Beauty2XGamma2pi_2Ks_Line**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma2pi_2Ks_Line' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo9_Beauty2XGamma2pi_2Ks_Line/Particles |
