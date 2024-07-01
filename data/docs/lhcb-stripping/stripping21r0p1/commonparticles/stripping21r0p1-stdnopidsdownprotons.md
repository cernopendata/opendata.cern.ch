[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StdNoPIDsDownProtons

**NoPIDsParticleMaker/StdNoPIDsDownProtons**

|                 |                    |
|-----------------|--------------------|
| Inputs          | []               |
| Input           | Rec/ProtoP/Charged |
| DecayDescriptor | Proton             |
| Output          | None               |
| Particle        | proton             |

****Tools:****

**TrackSelector/StdNoPIDsDownProtons.TrackSelector**

|                           |                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| AcceptClones :            | True                                                                                                      |
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
| MaxChi2Cut :              | 10.0                                                                                                      |
| MaxChi2PerDoFDownstream : | -1.0                                                                                                      |
| MaxChi2PerDoFMatch :      | -1.0                                                                                                      |
| MaxChi2PerDoFUpstream :   | -1.0                                                                                                      |
| MaxChi2PerDoFVelo :       | -1.0                                                                                                      |
| MaxCloneDistCut :         | 1.7976931e+308                                                                                            |
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
| MinCloneDistCut :         | -10000000000.0                                                                                            |
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
| TrackTypes :              | ['Downstream']                                                                                          |
| TypePrint :               | True                                                                                                      |
| UseEfficiencyRowFormat :  | True                                                                                                      |
| iWeight :                 | 1.0                                                                                                       |
| oWeight :                 | 0.5                                                                                                       |
| vWeight :                 | 1.0                                                                                                       |
