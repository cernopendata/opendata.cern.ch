[[stripping21 lines]](./stripping21-index)

# StrippingBu2LLK_meLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/Bu2LLK_meLine/Particles |
| Postscale      | 1.0000000                    |
| HLT            | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

## Filter sequence:

**LoKi::VoidFilter/StrippingBu2LLK_meLineVOIDFilter**

|      |                                                                  |
|------|------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 600 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21-stdloosemuons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseElectrons](./stripping21-stdlooseelectrons) /Particles')\>0 |

**CombineParticles/MuEForBu2LLK**

|                  |                                                                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21-stdlooseelectrons) ' , 'Phys/ [StdLooseMuons](./stripping21-stdloosemuons) ' ]                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(PT \> 300) & (MIPCHI2DV(PRIMARY)\>9)&(PIDe\> 0)' , 'e-' : '(PT \> 300) & (MIPCHI2DV(PRIMARY)\>9)&(PIDe\> 0)' , 'mu+' : '(PT \> 300) & (MIPCHI2DV(PRIMARY)\>9)&(HASMUON)&(ISMUON)' , 'mu-' : '(PT \> 300) & (MIPCHI2DV(PRIMARY)\>9)&(HASMUON)&(ISMUON)' } |
| CombinationCut   | (AM \> 100\*MeV)                                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9)                                                                                                                                                                                                                                                        |
| DecayDescriptor  | [J/psi(1S) -\> mu+ e-]cc                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[J/psi(1S) -\> mu+ e-]cc' ]                                                                                                                                                                                                                                               |
| Output           | Phys/MuEForBu2LLK/Particles                                                                                                                                                                                                                                                      |

**FilterDesktop/SelMuEForBu2LLK**

|                 |                                                                                                                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 0 \*MeV) & (MM \< 5500 \*MeV) & (MINTREE(ABSID\<14,PT)\>300 \*MeV) & (MINTREE(ABSID\<14,MIPCHI2DV(PRIMARY))\>9) & (VFASPF(VCHI2/VDOF)\<9) & (BPVVDCHI2\> 16) & (MIPCHI2DV(PRIMARY) \> 0 ) |
| Inputs          | [ 'Phys/MuEForBu2LLK' ]                                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                             |
| Output          | Phys/SelMuEForBu2LLK/Particles                                                                                                                                                                   |

**GaudiSequencer/SeqMergeBu2LLK_me**

**Members:**

**GaudiSequencer/SEQ:KaonsForBu2LLK**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKaons](./stripping21-stdloosekaons) /Particles')\>0 |

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

**FilterDesktop/KaonsForBu2LLK**

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 1200\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/ [StdLooseKaons](./stripping21-stdloosekaons) ' ]                                                                                     |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/KaonsForBu2LLK/Particles                                                                                                                   |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IKaonsForBu2LLK                                                                                           |
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
| OutputPlotsPath :              | OKaonsForBu2LLK                                                                                           |
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

**GaudiSequencer/SEQ:KstarsForBu2LLK**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKstar2Kpi](./stripping21-stdloosekstar2kpi) /Particles')\>0 |

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

**FilterDesktop/KstarsForBu2LLK**

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 1200\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/ [StdLooseKstar2Kpi](./stripping21-stdloosekstar2kpi) ' ]                                                                             |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/KstarsForBu2LLK/Particles                                                                                                                  |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IKstarsForBu2LLK                                                                                          |
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
| OutputPlotsPath :              | OKstarsForBu2LLK                                                                                          |
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

**GaudiSequencer/SEQ:PhisForBu2LLK**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePhi2KK](./stripping21-stdloosephi2kk) /Particles')\>0 |

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

**FilterDesktop/PhisForBu2LLK**

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 400 \*MeV) & (M \< 1200\*MeV) & ((ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)) \| (NDAUGHTERS == NINTREE( ISBASIC & (MIPCHI2DV(PRIMARY) \> 9)))) |
| Inputs          | [ 'Phys/ [StdLoosePhi2KK](./stripping21-stdloosephi2kk) ' ]                                                                                   |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/PhisForBu2LLK/Particles                                                                                                                    |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IPhisForBu2LLK                                                                                            |
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
| OutputPlotsPath :              | OPhisForBu2LLK                                                                                            |
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

**FilterDesktop/MergeBu2LLK_me**

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | ALL                                                                         |
| Inputs          | [ 'Phys/KaonsForBu2LLK' , 'Phys/KstarsForBu2LLK' , 'Phys/PhisForBu2LLK' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/MergeBu2LLK_me/Particles                                               |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IMergeBu2LLK_me                                                                                           |
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
| OutputPlotsPath :              | OMergeBu2LLK_me                                                                                           |
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

**CombineParticles/Bu2LLK_meLine**

|                  |                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MergeBu2LLK_me' , 'Phys/SelMuEForBu2LLK' ]                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | ADAMASS('B+') \< 1000\*MeV                                                                                                             |
| MotherCut        | ((VFASPF(VCHI2/VDOF)\< 9 ) & (BPVIPCHI2()\< 25 ) & (BPVDIRA\> 0.9995 ) & (BPVVDCHI2\> 100 ))                                           |
| DecayDescriptor  | None                                                                                                                                   |
| DecayDescriptors | [ '[ B+ -\> J/psi(1S) K+ ]cc' , '[ B0 -\> J/psi(1S) K\*(892)0 ]cc' , '[ B_s0 -\> J/psi(1S) phi(1020)]cc' ]                     |
| Output           | Phys/Bu2LLK_meLine/Particles                                                                                                           |

**AddRelatedInfo/RelatedInfo1_Bu2LLK_meLine**

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_meLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo1_Bu2LLK_meLine/Particles |

****Tools:****

**Tool1**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| TracksLocation :         | None                                                                                                      |
| ErrorsPrint :            | True                                                                                                      |
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
| ConeAngle :              | 1.0000000                                                                                                 |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| TrackType :              | 3                                                                                                         |
| Variables :              | [ ]                                                                                                     |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**AddRelatedInfo/RelatedInfo2_Bu2LLK_meLine**

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_meLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo2_Bu2LLK_meLine/Particles |

****Tools:****

**Tool2**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| ErrorsPrint :            | True                                                                                                      |
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
| InputParticles :         | [ '/Event/Phys/StdNoPIDsPions' ]                                                                        |
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| MaxChi2 :                | 9.0000000                                                                                                 |
| Variables :              | [ ]                                                                                                     |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**AddRelatedInfo/RelatedInfo3_Bu2LLK_meLine**

|                 |                                           |
|-----------------|-------------------------------------------|
| Inputs          | [ 'Phys/Bu2LLK_meLine' ]                |
| DecayDescriptor | None                                      |
| Output          | Phys/RelatedInfo3_Bu2LLK_meLine/Particles |

****Tools:****

**Tool3**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| DeltaDistance :          | 0.0010000000                                                                                              |
| AuditStart :             | False                                                                                                     |
| TrackExtrapolator :      | TrackMasterExtrapolator:PUBLIC                                                                            |
| Type :                   | Hard                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
| MaxPrints :              | 2                                                                                                         |
| RootOnTES :              | None                                                                                                      |
| MinChi2Iterations :      | 3                                                                                                         |
| FullReFit :              | False                                                                                                     |
| VeloTrackExtrapolator :  | TrackLinearExtrapolator:PUBLIC                                                                            |
| PrintMyAlg :             | True                                                                                                      |
| RootInTES :              | None                                                                                                      |
| AuditFinalize :          | False                                                                                                     |
| TypePrint :              | True                                                                                                      |
| ErrorsPrint :            | True                                                                                                      |
| ContextService :         | AlgContextSvc                                                                                             |
| DeltaChi2 :              | 0.0010000000                                                                                              |
| AuditTools :             | False                                                                                                     |
| Name :                   | BDTvalue                                                                                                  |
| MonitorService :         | MonitorSvc                                                                                                |
| AuditInitialize :        | False                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| InputParticles :         | [ '/Event/Phys/StdNoPIDsPions' ]                                                                        |
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| CheckTracksByLHCbIDs :   | False                                                                                                     |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| WeightsFile :            | IsolationTools_VertexIsolationHard_v1r4.xml                                                               |
| PropagationTolerance :   | 0.0020000000                                                                                              |
| MaxIterations :          | 16                                                                                                        |
| TrackStateProvider :     | TrackStateProvider:PUBLIC                                                                                 |
| UseEfficiencyRowFormat : | True                                                                                                      |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |
