[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StdTightProtons

**CombinedParticleMaker/StdTightProtons**

|                 |                    |
|-----------------|--------------------|
| Inputs          | []               |
| Input           | Rec/ProtoP/Charged |
| DecayDescriptor | None               |
| Output          | None               |
| Particle        | proton             |

****Tools:****

**ProtoParticleCALOFilter/StdTightProtons.Proton**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| AuditFinalize :          | False                                                                                                     |
| AuditInitialize :        | False                                                                                                     |
| AuditStart :             | False                                                                                                     |
| AuditStop :              | False                                                                                                     |
| AuditTools :             | False                                                                                                     |
| Context :                | None                                                                                                      |
| ContextService :         | AlgContextSvc                                                                                             |
| CounterList :            | ['.\*']                                                                                                 |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorsPrint :            | True                                                                                                      |
| GlobalTimeOffset :       | 0.0                                                                                                       |
| MonitorService :         | MonitorSvc                                                                                                |
| OutputLevel :            | 7                                                                                                         |
| PropertiesPrint :        | False                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| RootInTES :              | None                                                                                                      |
| Selection :              | ["RequiresDet='RICH' CombDLL(p-pi)\>'0.0'"]                                                             |
| StatEntityList :         | []                                                                                                      |
| StatPrint :              | True                                                                                                      |
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| TypePrint :              | True                                                                                                      |
| UseEfficiencyRowFormat : | True                                                                                                      |

**TrackSelector/StdTightProtons.TrackSelector**

|                           |                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| AcceptClones :            | False                                                                                                     |
| AuditFinalize :           | False                                                                                                     |
| AuditInitialize :         | False                                                                                                     |
| AuditStart :              | False                                                                                                     |
| AuditStop :               | False                                                                                                     |
| AuditTools :              | False                                                                                                     |
| Context :                 | None                                                                                                      |
| ContextService :          | AlgContextSvc                                                                                             |
| CounterList :             | ['.\*']                                                                                                 |
| EfficiencyRowFormat :     | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorsPrint :             | True                                                                                                      |
| GlobalTimeOffset :        | 0.0                                                                                                       |
| MaxChi2Cut :              | 5.0                                                                                                       |
| MaxChi2PerDoFDownstream : | -1.0                                                                                                      |
| MaxChi2PerDoFMatch :      | -1.0                                                                                                      |
| MaxChi2PerDoFUpstream :   | -1.0                                                                                                      |
| MaxChi2PerDoFVelo :       | -1.0                                                                                                      |
| MaxCloneDistCut :         | 9e+99                                                                                                     |
| MaxEtaCut :               | 1.7976931e+308                                                                                            |
| MaxGhostProbCut :         | 1.7976931e+308                                                                                            |
| MaxHitCut :               | 1.7976931e+308                                                                                            |
| MaxLikelihoodCut :        | 1.7976931e+308                                                                                            |
| MaxNDoF :                 | 2147483647                                                                                                |
| MaxNTHoles :              | 999                                                                                                       |
| MaxNVeloHoles :           | 999                                                                                                       |
| MaxPCut :                 | -1.0                                                                                                      |
| MaxPhiCut :               | 1.7976931e+308                                                                                            |
| MaxPtCut :                | -1.0                                                                                                      |
| MinChi2Cut :              | 0.0                                                                                                       |
| MinCloneDistCut :         | 5000.0                                                                                                    |
| MinEtaCut :               | -1.7976931e+308                                                                                           |
| MinGhostProbCut :         | -1.7976931e+308                                                                                           |
| MinHitCut :               | 0.0                                                                                                       |
| MinLikelihoodCut :        | -1.7976931e+308                                                                                           |
| MinNDoF :                 | 0                                                                                                         |
| MinNOTHits :              | 0                                                                                                         |
| MinNTTHits :              | 0                                                                                                         |
| MinNVeloPhiHits :         | 0                                                                                                         |
| MinNVeloRHits :           | 0                                                                                                         |
| MinPCut :                 | 0.0                                                                                                       |
| MinPhiCut :               | -1.7976931e+308                                                                                           |
| MinPtCut :                | 0.0                                                                                                       |
| MonitorService :          | MonitorSvc                                                                                                |
| OutputLevel :             | 7                                                                                                         |
| PropertiesPrint :         | False                                                                                                     |
| RegularRowFormat :        | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| RootInTES :               | None                                                                                                      |
| StatEntityList :          | []                                                                                                      |
| StatPrint :               | True                                                                                                      |
| StatTableHeader :         | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| TrackTypes :              | ['Long']                                                                                                |
| TypePrint :               | True                                                                                                      |
| UseEfficiencyRowFormat :  | True                                                                                                      |
| iWeight :                 | 1.0                                                                                                       |
| oWeight :                 | 0.5                                                                                                       |
| vWeight :                 | 1.0                                                                                                       |
