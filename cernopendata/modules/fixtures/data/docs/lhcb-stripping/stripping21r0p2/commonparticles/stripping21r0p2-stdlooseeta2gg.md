[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StdLooseEta2gg

**ResolvedPi0Maker/StdLooseEta2gg**

|                 |                    |
|-----------------|--------------------|
| Inputs          | []               |
| Input           | Rec/ProtoP/Charged |
| DecayDescriptor | Eta                |
| Output          | None               |
| Particle        | eta                |

****Tools:****

**PhotonMaker/StdLooseEta2gg.PhotonMaker**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| AddHcalEnergy :          | False                                                                                                     |
| AuditFinalize :          | False                                                                                                     |
| AuditInitialize :        | False                                                                                                     |
| AuditStart :             | False                                                                                                     |
| AuditStop :              | False                                                                                                     |
| AuditTools :             | False                                                                                                     |
| ClusterCodeMasks :       | {}                                                                                                        |
| ConfLevelCut :           | -99.0                                                                                                     |
| ConfidenceLevelBase :    | ['IsNotH']                                                                                              |
| ConfidenceLevelSwitch :  | ['PhotonDLL']                                                                                           |
| Context :                | None                                                                                                      |
| ContextService :         | AlgContextSvc                                                                                             |
| ConvertedPhotons :       | True                                                                                                      |
| CounterList :            | ['.\*']                                                                                                 |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ErrorsPrint :            | True                                                                                                      |
| GlobalTimeOffset :       | 0.0                                                                                                       |
| Input :                  | Rec/ProtoP/Neutrals                                                                                       |
| MaxHcalRatio :           | -1.0                                                                                                      |
| MaxPrsEnergy :           | -1.0                                                                                                      |
| MinHcalRatio :           | -1.0                                                                                                      |
| MonitorService :         | MonitorSvc                                                                                                |
| OutputLevel :            | 7                                                                                                         |
| Particle :               | gamma                                                                                                     |
| PropertiesPrint :        | False                                                                                                     |
| PrsThreshold :           | -1.0                                                                                                      |
| PtCut :                  | 200.0                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| RootInTES :              | None                                                                                                      |
| StatEntityList :         | []                                                                                                      |
| StatPrint :              | True                                                                                                      |
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| TypePrint :              | True                                                                                                      |
| UnconvertedPhotons :     | True                                                                                                      |
| UseEfficiencyRowFormat : | True                                                                                                      |
