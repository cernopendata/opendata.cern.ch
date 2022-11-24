[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2LLXBDT_Bd2eeKsLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/B2LLXBDT_Bd2eeKsLine/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

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

**LoKi::VoidFilter/SelFilterPhys_StdDiElectronFromTracks_Particles**

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdDiElectronFromTracks](./stripping21r1p1-stddielectronfromtracks) /Particles',True)\>0 |

**FilterDesktop/B2LLXBDTSelDiElectron**

|                 |                                                                                                                                                                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<5.0\*GeV) & (INTREE( (ID=='e+') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (PIDe\>-2) & (TRGHOSTPROB\<0.5) )) & (INTREE( (ID=='e-') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (PIDe\>-2) & (TRGHOSTPROB\<0.5) )) |
| Inputs          | [ 'Phys/ [StdDiElectronFromTracks](./stripping21r1p1-stddielectronfromtracks) ' ]                                                                                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                                                                                                             |
| Output          | Phys/B2LLXBDTSelDiElectron/Particles                                                                                                                                                                                                                             |

**GaudiSequencer/SeqB2LLXBDTSelKs**

**Members:**

**GaudiSequencer/SEQ:B2LLXBDTSelKsDD**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles**

|      |                                                                                     |
|------|-------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKsDD](./stripping21r1p1-stdlooseksdd) /Particles',True)\>0 |

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

**FilterDesktop/B2LLXBDTSelKsDD**

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.\*MeV) & (BPVVDCHI2\>25)                 |
| Inputs          | [ 'Phys/ [StdLooseKsDD](./stripping21r1p1-stdlooseksdd) ' ] |
| DecayDescriptor | None                                                          |
| Output          | Phys/B2LLXBDTSelKsDD/Particles                                |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IB2LLXBDTSelKsDD                                                                                          |
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
| OutputPlotsPath :              | OB2LLXBDTSelKsDD                                                                                          |
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

**GaudiSequencer/SEQ:B2LLXBDTSelKsLL**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseANNPions](./stripping21r1p1-stdalllooseannpions) /Particles',True)\>0 |

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

**FilterDesktop/B2LLXBDTSelPions4LP**

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (PROBNNpi\> 0.2) & (PT\>100\*MeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY)\>9.) |
| Inputs          | [ 'Phys/ [StdAllLooseANNPions](./stripping21r1p1-stdalllooseannpions) ' ]       |
| DecayDescriptor | None                                                                              |
| Output          | Phys/B2LLXBDTSelPions4LP/Particles                                                |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IB2LLXBDTSelPions4LP                                                                                      |
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
| OutputPlotsPath :              | OB2LLXBDTSelPions4LP                                                                                      |
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

**CombineParticles/B2LLXBDTSelKsLL**

|                  |                                                                        |
|------------------|------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelPions4LP' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                         |
| CombinationCut   | (ADAMASS('KS0') \< 50.\*MeV) & (ADOCACHI2CUT(25, ''))                  |
| MotherCut        | (ADMASS('KS0') \< 30.\*MeV) & (BPVVDCHI2\>25) & (VFASPF(VCHI2) \< 25.) |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                        |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                |
| Output           | Phys/B2LLXBDTSelKsLL/Particles                                         |

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

**FilterDesktop/B2LLXBDTSelKs**

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Code            | ALL                                                   |
| Inputs          | [ 'Phys/B2LLXBDTSelKsDD' , 'Phys/B2LLXBDTSelKsLL' ] |
| DecayDescriptor | None                                                  |
| Output          | Phys/B2LLXBDTSelKs/Particles                          |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IB2LLXBDTSelKs                                                                                            |
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
| OutputPlotsPath :              | OB2LLXBDTSelKs                                                                                            |
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

**CombineParticles/B2LLXBDTSelBd2eeKs**

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelDiElectron' , 'Phys/B2LLXBDTSelKs' ]                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'KS0' : 'ALL' }                                                                   |
| CombinationCut   | (in_range(3.7\*GeV, AM, 6.8\*GeV))                                                                                     |
| MotherCut        | (in_range(4.0\*GeV, M, 6.5\*GeV)) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.999) & (BPVDLS\>0) & (BPVIPCHI2()\<400) |
| DecayDescriptor  | B0 -\> J/psi(1S) KS0                                                                                                   |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) KS0' ]                                                                                           |
| Output           | Phys/B2LLXBDTSelBd2eeKs/Particles                                                                                      |

**FilterDesktop/B2LLXBDT_Bd2eeKsLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2LLXBDTMvaBd2eeKs')\>-0.07 |
| Inputs          | [ 'Phys/B2LLXBDTSelBd2eeKs' ]                            |
| DecayDescriptor | None                                                       |
| Output          | Phys/B2LLXBDT_Bd2eeKsLine/Particles                        |

****Tools:****

**B2LLXBDTMvaBd2eeKs**

|                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Factory :                | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Source :                 | LoKi::Hybrid::DictOfFunctors/MVAdict                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Preambulo :              | [ ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ErrorsPrint :            | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| StatEntityList :         | [ ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| RootInTES :              | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| AuditFinalize :          | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Key :                    | BDT                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| TypePrint :              | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| UseEfficiencyRowFormat : | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ContextService :         | AlgContextSvc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| AuditTools :             | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MonitorService :         | MonitorSvc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| AuditInitialize :        | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| OutputLevel :            | 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| StatPrint :              | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| AuditStop :              | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Context :                | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PropertiesPrint :        | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Options :                | { 'KeepVars' : '0' , 'Name' : 'BDT' , 'XMLFile' : '/afs/cern.ch/lhcb/software/releases/PARAM/TMVAWeights/v1r7/data/Bd2eeKs_BDT_v1r0.xml' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Variables :              | { 'B_DIRA_OWNPV' : 'BPVDIRA' , 'log(B_PT)' : 'log(PT)' , 'log(H1_PT)' : 'log(CHILD(PT, 2, 1))' , 'log(H2_PT)' : 'log(CHILD(PT, 2, 2))' , 'log(Jpsi_PT)' : 'log(CHILD(PT, 1))' , 'log(L1_PT)' : 'log(CHILD(PT, 1, 1))' , 'log(L2_PT)' : 'log(CHILD(PT, 1, 2))' , 'log(X_PT)' : 'log(CHILD(PT, 2))' , 'sqrt(B_FDCHI2_OWNPV)' : 'sqrt(BPVVDCHI2)' , 'sqrt(B_IPCHI2_OWNPV)' : 'sqrt(BPVIPCHI2())' , 'sqrt(H1_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 2, 1))' , 'sqrt(H2_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 2, 2))' , 'sqrt(Jpsi_FDCHI2_OWNPV)' : 'sqrt(CHILD(BPVVDCHI2,1))' , 'sqrt(Jpsi_IPCHI2_OWNPV}' : 'sqrt(CHILD(MIPCHI2DV(), 1 ))' , 'sqrt(L1_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 1, 1))' , 'sqrt(L2_IPCHI2_OWNPV)' : 'sqrt(CHILD(MIPCHI2DV(), 1, 2))' , 'sqrt(X_FDCHI2_OWNPV)' : 'sqrt(CHILD(BPVVDCHI2,2))' , 'sqrt(X_IPCHI2_OWNPV}' : 'sqrt(CHILD(MIPCHI2DV(), 2 ))' } |
| AuditStart :             | False                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| CounterList :            | [ '.\*' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

**AddRelatedInfo/RelatedInfo1_B2LLXBDT_Bd2eeKsLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKsLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_B2LLXBDT_Bd2eeKsLine/Particles |

**AddRelatedInfo/RelatedInfo2_B2LLXBDT_Bd2eeKsLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKsLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_B2LLXBDT_Bd2eeKsLine/Particles |

**AddRelatedInfo/RelatedInfo3_B2LLXBDT_Bd2eeKsLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKsLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_B2LLXBDT_Bd2eeKsLine/Particles |

**AddRelatedInfo/RelatedInfo4_B2LLXBDT_Bd2eeKsLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKsLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_B2LLXBDT_Bd2eeKsLine/Particles |

**AddRelatedInfo/RelatedInfo5_B2LLXBDT_Bd2eeKsLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKsLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo5_B2LLXBDT_Bd2eeKsLine/Particles |

**AddRelatedInfo/RelatedInfo6_B2LLXBDT_Bd2eeKsLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2eeKsLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo6_B2LLXBDT_Bd2eeKsLine/Particles |
