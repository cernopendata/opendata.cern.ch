[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingRareStrangeSigmaPPi0CalLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaPPi0CalLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

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

**GaudiSequencer/SeqPi0ForRareStrangeSigmaPPi0Cal**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles**

|      |                                                                                               |
|------|-----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMergedPi0](./stripping21r0p1-stdloosemergedpi0) /Particles',True)\>0 |

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

**LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseResolvedPi0](./stripping21r0p1-stdlooseresolvedpi0) /Particles',True)\>0 |

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

**FilterDesktop/Pi0ForRareStrangeSigmaPPi0Cal**

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                             |
| Inputs          | [ 'Phys/ [StdLooseMergedPi0](./stripping21r0p1-stdloosemergedpi0) ' , 'Phys/ [StdLooseResolvedPi0](./stripping21r0p1-stdlooseresolvedpi0) ' ] |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/Pi0ForRareStrangeSigmaPPi0Cal/Particles                                                                                                    |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IPi0ForRareStrangeSigmaPPi0Cal                                                                            |
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
| OutputPlotsPath :              | OPi0ForRareStrangeSigmaPPi0Cal                                                                            |
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

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                           |
|------|-------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21r0p1-stdlooseprotons) /Particles',True)\>0 |

**CombineParticles/RareStrangeSigmaPPi0CalLine**

|                  |                                                                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0ForRareStrangeSigmaPPi0Cal' , 'Phys/ [StdLooseProtons](./stripping21r0p1-stdlooseprotons) ' ]                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT \> 500.0) & (TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp \> 0.5 )' , 'pi0' : '(PT \> 700.0)' , 'p\~-' : '(PT \> 500.0) & (TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PROBNNp \> 0.5 )' } |
| CombinationCut   | (ADAMASS('Sigma+')\<150.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 36.0) & (PT\> 500.0 \*MeV)& (ADMASS('Sigma+') \< 150.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 6.0 \* ps)                                                          |
| DecayDescriptor  | [Sigma+ -\> p+ pi0]cc                                                                                                                                                                                          |
| DecayDescriptors | [ '[Sigma+ -\> p+ pi0]cc' ]                                                                                                                                                                                  |
| Output           | Phys/RareStrangeSigmaPPi0CalLine/Particles                                                                                                                                                                       |

**AddRelatedInfo/RelatedInfo1_RareStrangeSigmaPPi0CalLine**

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPPi0CalLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaPPi0CalLine/Particles |

**AddRelatedInfo/RelatedInfo2_RareStrangeSigmaPPi0CalLine**

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPPi0CalLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaPPi0CalLine/Particles |

**AddRelatedInfo/RelatedInfo3_RareStrangeSigmaPPi0CalLine**

|                 |                                                         |
|-----------------|---------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPPi0CalLine' ]                |
| DecayDescriptor | None                                                    |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaPPi0CalLine/Particles |
