[[stripping21r1 lines]](./stripping21r1-index)

# StrippingDisplVerticesLinesJetSingleLowMass

## Properties:

|                |                                                   |
|----------------|---------------------------------------------------|
| OutputLocation | Phys/DisplVerticesLinesJetSingleLowMass/Particles |
| Postscale      | 1.0000000                                         |
| HLT            | None                                              |
| Prescale       | 1.0000000                                         |
| L0DU           | None                                              |
| ODIN           | None                                              |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterRec_Track_Best**

|      |                               |
|------|-------------------------------|
| Code | CONTAINS('Rec/Track/Best')\>0 |

**VeloEventShapeCutsS20p3/DisplVerticesLinesVeloGEC**

**SelectVeloTracksNotFromPVS20p3/DisplVerticesLinesVeloFilteredTracks**

|        |                                                     |
|--------|-----------------------------------------------------|
| Inputs | [ 'Rec/Track/Best' ]                              |
| Output | Phys/DisplVerticesLinesVeloFilteredTracks/Particles |

****Tools:****

**TrackUniqueSegmentSelectorS20p3**

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| TrackSelector :          | None                                                                                                      |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**PatPV3D/DisplVerticesLinesWithVeloVertexing**

****Tools:****

**PVOfflineTool**

|                                 |                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| ApplyEnergyLossCorr :           | True                                                                                                      |
| AuditTools :                    | False                                                                                                     |
| StatTableHeader :               | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| MaxSlope :                      | 10.000000                                                                                                 |
| LongDistanceExtrapolatorType :  | TrackRungeKuttaExtrapolator                                                                               |
| UseBeamSpotRCut :               | False                                                                                                     |
| MaxTransverse :                 | 10000.000                                                                                                 |
| PropertiesPrint :               | False                                                                                                     |
| TrackErrorScaleFactor :         | 1.0000000                                                                                                 |
| AuditStart :                    | False                                                                                                     |
| ExtraSelector :                 | TrackDistanceExtraSelector                                                                                |
| AddMultipleScattering :         | True                                                                                                      |
| MaxStep :                       | 1000.0000                                                                                                 |
| RKScheme :                      | CashKarp                                                                                                  |
| MaxNumSteps :                   | 1000                                                                                                      |
| MinStep :                       | 10.000000                                                                                                 |
| CorrectNumSteps :               | False                                                                                                     |
| minTrackWeight :                | 1.0000000e-05                                                                                             |
| MaxStepSize :                   | 1000.0000                                                                                                 |
| ApplyElectronEnergyLossCorr :   | True                                                                                                      |
| MinTracks :                     | 4                                                                                                         |
| StatEntityList :                | [ ]                                                                                                     |
| MinRadThickness :               | 0.00010000000                                                                                             |
| BeamSpotRCut :                  | 0.30000000                                                                                                |
| RootOnTES :                     | None                                                                                                      |
| Sigma :                         | 5.5000000                                                                                                 |
| Tolerance :                     | 0.0010000000                                                                                              |
| zMaxSpread :                    | 3.0000000                                                                                                 |
| RootInTES :                     | None                                                                                                      |
| RelToleranceTx :                | 5.0000000e-05                                                                                             |
| AuditFinalize :                 | False                                                                                                     |
| TimingMeasurement :             | False                                                                                                     |
| MinStepScale :                  | 0.12500000                                                                                                |
| RegularRowFormat :              | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| InputVerticesName :             | Hlt/Vertex/PV3D                                                                                           |
| MinCloseTracks :                | 3                                                                                                         |
| maxIP2PV :                      | 2.0000000                                                                                                 |
| ContextService :                | AlgContextSvc                                                                                             |
| ApplyMultScattCorr :            | True                                                                                                      |
| PVsChi2SeparationLowMult :      | 0.0000000                                                                                                 |
| PVsChi2Separation :             | 0.0000000                                                                                                 |
| trackMaxChi2Remove :            | 25.000000                                                                                                 |
| CalculateMultipleScattering :   | True                                                                                                      |
| MonitorService :                | MonitorSvc                                                                                                |
| AuditInitialize :               | False                                                                                                     |
| TypePrint :                     | True                                                                                                      |
| shortDist :                     | 100.00000                                                                                                 |
| OutputLevel :                   | 3                                                                                                         |
| StatPrint :                     | True                                                                                                      |
| MaterialLocator :               | DetailedMaterialLocator                                                                                   |
| Geometry :                      | /dd/Structure/LHCb                                                                                        |
| InputTracks :                   | [ 'Phys/DisplVerticesLinesVeloFilteredTracks/Particles' ]                                               |
| AuditStop :                     | False                                                                                                     |
| RequireVelo :                   | True                                                                                                      |
| Context :                       | None                                                                                                      |
| ErrorsPrint :                   | True                                                                                                      |
| x0MS :                          | 0.020000000                                                                                               |
| FieldSvc :                      | MagneticFieldSvc                                                                                          |
| GlobalTimeOffset :              | 0.0000000                                                                                                 |
| TrackPairMaxDistance :          | 0.30000000                                                                                                |
| trackMaxChi2 :                  | 9.0000000                                                                                                 |
| MaxStepScale :                  | 4.0000000                                                                                                 |
| LookForDisplaced :              | False                                                                                                     |
| MaximumEnergyLoss :             | 100.00000                                                                                                 |
| maxDeltaZ :                     | 0.0010000000                                                                                              |
| MaxCurvature :                  | 0.0010000000                                                                                              |
| StepScaleSafetyFactor :         | 1.0000000                                                                                                 |
| ShortDistanceExtrapolatorType : | TrackParabolicExtrapolator                                                                                |
| minIter :                       | 5                                                                                                         |
| SaveSeedsAsPV :                 | False                                                                                                     |
| UseEfficiencyRowFormat :        | True                                                                                                      |
| PVSeedingName :                 | PVSeed3DTool/PVSeed3DTool                                                                                 |
| InitialStep :                   | 1000.0000                                                                                                 |
| UpdatePVTracks :                | False                                                                                                     |
| EnergyLossFactor :              | 1.0000000                                                                                                 |
| UseGridInterpolation :          | True                                                                                                      |
| Iterations :                    | 5                                                                                                         |
| PVFitterName :                  | LSAdaptPV3DFitter/LSAdaptPV3DFitter                                                                       |
| zVtxShift :                     | 0.0000000                                                                                                 |
| EfficiencyRowFormat :           | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| NumericalJacobian :             | False                                                                                                     |
| GeneralDedxToolName :           | StateDetailedBetheBlochEnergyCorrectionTool                                                               |
| CounterList :                   | [ '.\*' ]                                                                                               |

**LLParticlesFromRecVertices/DisplVerticesLinesWithVeloCandidates**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ ]                                               |
| DecayDescriptor | None                                                |
| Output          | Phys/DisplVerticesLinesWithVeloCandidates/Particles |

****Tools:****

**muon**

|                           |                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :         | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| MinChi2Cut :              | -1.0000000                                                                                                |
| MinNOTHits :              | 0                                                                                                         |
| MinNTTHits :              | 0                                                                                                         |
| MaxChi2PerDoFDownstream : | -1.0000000                                                                                                |
| AcceptClones :            | True                                                                                                      |
| ErrorsPrint :             | True                                                                                                      |
| StatEntityList :          | [ ]                                                                                                     |
| MinNVeloRHits :           | 0                                                                                                         |
| RootOnTES :               | None                                                                                                      |
| MaxPtCut :                | -1.0000000                                                                                                |
| MinPtCut :                | 0.0000000                                                                                                 |
| oWeight :                 | 0.50000000                                                                                                |
| RootInTES :               | None                                                                                                      |
| MinEtaCut :               | -1.7976931e+308                                                                                           |
| MaxNVeloHoles :           | 999                                                                                                       |
| MaxChi2PerDoFUpstream :   | -1.0000000                                                                                                |
| AuditFinalize :           | False                                                                                                     |
| TypePrint :               | True                                                                                                      |
| MaxNDoF :                 | 2147483647                                                                                                |
| UseEfficiencyRowFormat :  | True                                                                                                      |
| MinNDoF :                 | 0                                                                                                         |
| ContextService :          | AlgContextSvc                                                                                             |
| MaxHitCut :               | 1.7976931e+308                                                                                            |
| MinGhostProbCut :         | -1.7976931e+308                                                                                           |
| AuditTools :              | False                                                                                                     |
| MaxChi2PerDoFVelo :       | -1.0000000                                                                                                |
| vWeight :                 | 1.0000000                                                                                                 |
| MonitorService :          | MonitorSvc                                                                                                |
| AuditInitialize :         | False                                                                                                     |
| RegularRowFormat :        | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| MaxEtaCut :               | 1.7976931e+308                                                                                            |
| OutputLevel :             | 3                                                                                                         |
| MaxGhostProbCut :         | 1.7976931e+308                                                                                            |
| StatPrint :               | True                                                                                                      |
| MinNVeloPhiHits :         | 0                                                                                                         |
| MinPCut :                 | 0.0000000                                                                                                 |
| AuditStop :               | False                                                                                                     |
| Context :                 | None                                                                                                      |
| PropertiesPrint :         | False                                                                                                     |
| GlobalTimeOffset :        | 0.0000000                                                                                                 |
| MinLikelihoodCut :        | -1.7976931e+308                                                                                           |
| Selection :               | [ "RequiresDet='MUON' IsMuon=True CombDLL(mu-pi)\>'-8.0'" ]                                             |
| TrackTypes :              | [ 'Velo' , 'VeloR' , 'Long' , 'Upstream' , 'Downstream' , 'Ttrack' , 'Backward' , 'TT' ]                |
| MaxPCut :                 | -1.0000000                                                                                                |
| MaxCloneDistCut :         | 1.7976931e+308                                                                                            |
| MaxChi2PerDoFMatch :      | -1.0000000                                                                                                |
| MaxLikelihoodCut :        | 1.7976931e+308                                                                                            |
| AuditStart :              | False                                                                                                     |
| MaxChi2Cut :              | -1.0000000                                                                                                |
| MinHitCut :               | 0.0000000                                                                                                 |
| MinCloneDistCut :         | -1.0000000e+10                                                                                            |
| iWeight :                 | 1.0000000                                                                                                 |
| EfficiencyRowFormat :     | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :             | [ '.\*' ]                                                                                               |

**electron**

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| Selection :              | [ "RequiresDet='CALO' CombDLL(e-pi)\>'0.0'" ]                                                           |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**proton**

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| Selection :              | [ "RequiresDet='RICH' CombDLL(p-pi)\>'3.0'" ]                                                           |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**pion**

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| Selection :              | [ '' ]                                                                                                  |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**kaon**

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| Selection :              | [ "RequiresDet='RICH' CombDLL(k-pi)\>'2.0' CombDLL(k-p)\>'-2.0'" ]                                      |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**FilterDesktop/DisplVerticesLinesJetSingleLowMassSelectionVertices**

|                 |                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( \~ISBASIC ) & ( \~INMATTER ) & ( MAXFRACTENERGYINSINGLETRACK \< 0.8 ) & ( MM \> 0.0 ) & ( NDAUGS \>= 5 ) & ( SUMPT \> 10000.0 ) & ( FRACTDAUGHTERTRACKSWITHUPSTREAMHIT \< 0.49 ) & ( ENDVERTEXRHO \> 0.4 ) |
| Inputs          | [ 'Phys/DisplVerticesLinesWithVeloCandidates' ]                                                                                                                                                            |
| DecayDescriptor | \~chi_10                                                                                                                                                                                                     |
| Output          | Phys/DisplVerticesLinesJetSingleLowMassSelectionVertices/Particles                                                                                                                                           |

**DisplacedVertexJetCandidateMakerS20p3/DisplVerticesLinesJetSingleLowMassSelectionJets**

|                 |                                                                  |
|-----------------|------------------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesJetSingleLowMassSelectionVertices' ] |
| DecayDescriptor | None                                                             |
| Output          | Phys/DisplVerticesLinesJetSingleLowMassSelectionJets/Particles   |

****Tools:****

**JEC**

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| HistoPath :              | DisplVerticesLines_JEC                                                                                    |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| ShiftJEC :               | 0.00000                                                                                                   |
| AuditStart :             | False                                                                                                     |
| Apply :                  | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**MomentumCombiner**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| Transporter :            | None                                                                                                      |
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| ErrorsPrint :            | True                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
| RootOnTES :              | None                                                                                                      |
| PrintMyAlg :             | True                                                                                                      |
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
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**LoKi\_\_FastJetMaker**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| RParameter :             | 1.2000000                                                                                                 |
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| Strategy :               | 1                                                                                                         |
| Type :                   | 2                                                                                                         |
| Sort :                   | 2                                                                                                         |
| StatEntityList :         | [ ]                                                                                                     |
| RootOnTES :              | None                                                                                                      |
| ParticleCombiner :       | MomentumCombiner                                                                                          |
| RootInTES :              | None                                                                                                      |
| AuditFinalize :          | False                                                                                                     |
| TypePrint :              | True                                                                                                      |
| ErrorsPrint :            | True                                                                                                      |
| ContextService :         | AlgContextSvc                                                                                             |
| AuditTools :             | False                                                                                                     |
| MonitorService :         | MonitorSvc                                                                                                |
| AuditInitialize :        | False                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| Transporter :            | None                                                                                                      |
| JetID :                  | 98                                                                                                        |
| AuditStop :              | False                                                                                                     |
| PtMin :                  | 5000.0000                                                                                                 |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| PrintMyAlg :             | True                                                                                                      |
| UseEfficiencyRowFormat : | True                                                                                                      |
| AuditStart :             | False                                                                                                     |
| Recombination :          | 0                                                                                                         |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**JetIDInfo**

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**FilterDesktop/DisplVerticesLinesJetSingleLowMass**

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Code            | ISLLP & ( MM \> 0.0 )                                        |
| Inputs          | [ 'Phys/DisplVerticesLinesJetSingleLowMassSelectionJets' ] |
| DecayDescriptor | \~chi_10                                                     |
| Output          | Phys/DisplVerticesLinesJetSingleLowMass/Particles            |

**AddRelatedInfo/RelatedInfo1_DisplVerticesLinesJetSingleLowMass**

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/DisplVerticesLinesJetSingleLowMass' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo1_DisplVerticesLinesJetSingleLowMass/Particles |

****Tools:****

**Tool1**

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |
