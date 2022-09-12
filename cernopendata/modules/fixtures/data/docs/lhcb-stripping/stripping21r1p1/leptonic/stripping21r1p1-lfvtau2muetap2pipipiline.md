[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingLFVTau2MuEtaP2pipipiLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/LFVTau2MuEtaP2pipipiLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

**LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePions](./stripping21r1p1-stdloosepions) /Particles',True)\>0 |

**GaudiSequencer/SeqPi0ForselEtap_pi0**

**Members:**

**LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseResolvedPi0](./stripping21r1p1-stdlooseresolvedpi0) /Particles',True)\>0 |

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

**LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles**

|      |                                                                                               |
|------|-----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMergedPi0](./stripping21r1p1-stdloosemergedpi0) /Particles',True)\>0 |

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

**FilterDesktop/Pi0ForselEtap_pi0**

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                             |
| Inputs          | [ 'Phys/ [StdLooseMergedPi0](./stripping21r1p1-stdloosemergedpi0) ' , 'Phys/ [StdLooseResolvedPi0](./stripping21r1p1-stdlooseresolvedpi0) ' ] |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/Pi0ForselEtap_pi0/Particles                                                                                                                |

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| InputPlotsPath :               | IPi0ForselEtap_pi0                                                                                        |
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
| OutputPlotsPath :              | OPi0ForselEtap_pi0                                                                                        |
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

**CombineParticles/selEtap_pi0**

|                  |                                                                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi0ForselEtap_pi0' , 'Phys/ [StdLoosePions](./stripping21r1p1-stdloosepions) ' ]                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3.0) & (MIPCHI2DV(PRIMARY) \> 9.)' , 'pi-' : '(PROBNNpi \> 0.1) & (PT \> 250\*MeV) & (TRGHOSTPROB \< 0.3) & (TRCHI2DOF \< 3.0) & (MIPCHI2DV(PRIMARY) \> 9.)' , 'pi0' : '(PT \> 250\*MeV)' } |
| CombinationCut   | (ADAMASS('eta') \< 80\*MeV) \| (ADAMASS('eta_prime') \< 80\*MeV)                                                                                                                                                                                                                                |
| MotherCut        | (PT \> 500\*MeV) & (VFASPF(VCHI2/VDOF) \< 6.0)                                                                                                                                                                                                                                                  |
| DecayDescriptor  | eta_prime -\> pi+ pi- pi0                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ 'eta_prime -\> pi+ pi- pi0' ]                                                                                                                                                                                                                                                               |
| Output           | Phys/selEtap_pi0/Particles                                                                                                                                                                                                                                                                      |

**LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21r1p1-stdloosemuons) /Particles',True)\>0 |

**CombineParticles/LFVTau2MuEtaP2pipipiLine**

|                  |                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r1p1-stdloosemuons) ' , 'Phys/selEtap_pi0' ]                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'eta_prime' : 'ALL' , 'mu+' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY) \> 9.) & (PT \> 300\*MeV) & (TRGHOSTPROB \< 0.3)' , 'mu-' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY) \> 9.) & (PT \> 300\*MeV) & (TRGHOSTPROB \< 0.3)' } |
| CombinationCut   | (ADAMASS('tau+')\<150\*MeV)                                                                                                                                                                                                                                          |
| MotherCut        | (BPVIPCHI2()\< 100) & (VFASPF(VCHI2/VDOF)\<6.) & (BPVLTIME()\*c_light \> 50.\*micrometer) & (BPVLTIME()\*c_light \< 400.\*micrometer) & (PT\>500\*MeV) & (D2DVVD(2) \< 80\*micrometer)                                                                               |
| DecayDescriptor  | [tau+ -\> mu+ eta_prime]cc                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[tau+ -\> mu+ eta_prime]cc ' ]                                                                                                                                                                                                                                |
| Output           | Phys/LFVTau2MuEtaP2pipipiLine/Particles                                                                                                                                                                                                                              |

**AddRelatedInfo/RelatedInfo1_LFVTau2MuEtaP2pipipiLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2MuEtaP2pipipiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_LFVTau2MuEtaP2pipipiLine/Particles |

**AddRelatedInfo/RelatedInfo2_LFVTau2MuEtaP2pipipiLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2MuEtaP2pipipiLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo2_LFVTau2MuEtaP2pipipiLine/Particles |
