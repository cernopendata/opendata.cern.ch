[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2KpiX2EESSDarkBosonLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/B2KpiX2EESSDarkBosonLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 0.10000000                              |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**LoKi::VoidFilter/StrippingB2KpiX2EESSDarkBosonLineVOIDFilter**

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250 ) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**DiElectronMaker/EESSDarkBosonSel**

|                 |                                 |
|-----------------|---------------------------------|
| Inputs          | [ 'Rec/ProtoP/Charged' ]      |
| DecayDescriptor | J/psi(1S)                       |
| Output          | Phys/EESSDarkBosonSel/Particles |

****Tools:****

**CaloElectron**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| MaxSlope :               | 10.000000                                                                                                 |
| MinStep :                | 10.000000                                                                                                 |
| RKScheme :               | CashKarp                                                                                                  |
| MaxNumSteps :            | 1000                                                                                                      |
| CorrectNumSteps :        | False                                                                                                     |
| Tolerance :              | 0.0010000000                                                                                              |
| ErrorsPrint :            | True                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
| RootInTES :              | None                                                                                                      |
| RelToleranceTx :         | 5.0000000e-05                                                                                             |
| AuditFinalize :          | False                                                                                                     |
| MinStepScale :           | 0.12500000                                                                                                |
| TypePrint :              | True                                                                                                      |
| UseEfficiencyRowFormat : | True                                                                                                      |
| ContextService :         | AlgContextSvc                                                                                             |
| AuditTools :             | False                                                                                                     |
| MaxStep :                | 1000.0000                                                                                                 |
| zOffset :                | 0.0000000                                                                                                 |
| MonitorService :         | MonitorSvc                                                                                                |
| AuditInitialize :        | False                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| FieldSvc :               | MagneticFieldSvc                                                                                          |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| Sigma :                  | 5.5000000                                                                                                 |
| MaxStepScale :           | 4.0000000                                                                                                 |
| MaxCurvature :           | 0.0010000000                                                                                              |
| StepScaleSafetyFactor :  | 1.0000000                                                                                                 |
| AuditStart :             | False                                                                                                     |
| ExtrapolatorType :       | TrackRungeKuttaExtrapolator                                                                               |
| UseGridInterpolation :   | True                                                                                                      |
| Iterations :             | 5                                                                                                         |
| InitialStep :            | 1000.0000                                                                                                 |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| NumericalJacobian :      | False                                                                                                     |
| CounterList :            | [ '.\*' ]                                                                                               |

**Electron**

|                           |                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| MaxPhiCut :               | 1.7976931e+308                                                                                            |
| StatTableHeader :         | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| MaxNTHoles :              | 999                                                                                                       |
| MinChi2Cut :              | -1.0000000                                                                                                |
| MinNOTHits :              | 0                                                                                                         |
| MinNTTHits :              | 0                                                                                                         |
| MaxChi2PerDoFDownstream : | -1.0000000                                                                                                |
| AcceptClones :            | True                                                                                                      |
| ErrorsPrint :             | True                                                                                                      |
| StatEntityList :          | [ ]                                                                                                     |
| MinNVeloRHits :           | 0                                                                                                         |
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
| MinPhiCut :               | -1.7976931e+308                                                                                           |
| MinNVeloPhiHits :         | 0                                                                                                         |
| MinPCut :                 | 0.0000000                                                                                                 |
| AuditStop :               | False                                                                                                     |
| Context :                 | None                                                                                                      |
| PropertiesPrint :         | False                                                                                                     |
| GlobalTimeOffset :        | 0.0000000                                                                                                 |
| MinLikelihoodCut :        | -1.7976931e+308                                                                                           |
| Selection :               | [ "RequiresDet='CALO' CombDLL(e-pi)\>-2" ]                                                              |
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

**TrackSelector**

|                           |                                                                                                           |
|---------------------------|-----------------------------------------------------------------------------------------------------------|
| MaxPhiCut :               | 1.7976931e+308                                                                                            |
| StatTableHeader :         | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| MaxNTHoles :              | 999                                                                                                       |
| MinChi2Cut :              | 0.0000000                                                                                                 |
| MinNOTHits :              | 0                                                                                                         |
| MinNTTHits :              | 0                                                                                                         |
| MaxChi2PerDoFDownstream : | -1.0000000                                                                                                |
| AcceptClones :            | False                                                                                                     |
| MinEtaCut :               | -1.7976931e+308                                                                                           |
| RegularRowFormat :        | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| StatEntityList :          | [ ]                                                                                                     |
| MinNVeloRHits :           | 0                                                                                                         |
| TrackTypes :              | [ 'Long' ]                                                                                              |
| MinPtCut :                | 0.0000000                                                                                                 |
| oWeight :                 | 0.50000000                                                                                                |
| RootInTES :               | None                                                                                                      |
| MaxNVeloHoles :           | 999                                                                                                       |
| MaxChi2PerDoFUpstream :   | -1.0000000                                                                                                |
| AuditFinalize :           | False                                                                                                     |
| MaxEtaCut :               | 1.7976931e+308                                                                                            |
| MaxNDoF :                 | 2147483647                                                                                                |
| UseEfficiencyRowFormat :  | True                                                                                                      |
| MinNDoF :                 | 0                                                                                                         |
| ContextService :          | AlgContextSvc                                                                                             |
| MaxHitCut :               | 1.7976931e+308                                                                                            |
| MinGhostProbCut :         | -1.7976931e+308                                                                                           |
| AuditTools :              | False                                                                                                     |
| MaxChi2PerDoFVelo :       | -1.0000000                                                                                                |
| MonitorService :          | MonitorSvc                                                                                                |
| AuditInitialize :         | False                                                                                                     |
| vWeight :                 | 1.0000000                                                                                                 |
| TypePrint :               | True                                                                                                      |
| MaxGhostProbCut :         | 1.7976931e+308                                                                                            |
| StatPrint :               | True                                                                                                      |
| MinPhiCut :               | -1.7976931e+308                                                                                           |
| MinNVeloPhiHits :         | 0                                                                                                         |
| AuditStop :               | False                                                                                                     |
| Context :                 | None                                                                                                      |
| PropertiesPrint :         | False                                                                                                     |
| ErrorsPrint :             | True                                                                                                      |
| GlobalTimeOffset :        | 0.0000000                                                                                                 |
| MinLikelihoodCut :        | -1.7976931e+308                                                                                           |
| MinPCut :                 | 0.0000000                                                                                                 |
| OutputLevel :             | 3                                                                                                         |
| MaxPtCut :                | -1.0000000                                                                                                |
| MaxPCut :                 | -1.0000000                                                                                                |
| MaxCloneDistCut :         | 9.0000000e+99                                                                                             |
| MaxChi2PerDoFMatch :      | -1.0000000                                                                                                |
| MaxLikelihoodCut :        | 1.7976931e+308                                                                                            |
| AuditStart :              | False                                                                                                     |
| MaxChi2Cut :              | 3.0000000                                                                                                 |
| MinHitCut :               | 0.0000000                                                                                                 |
| MinCloneDistCut :         | 5000.0000                                                                                                 |
| iWeight :                 | 1.0000000                                                                                                 |
| EfficiencyRowFormat :     | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :             | [ '.\*' ]                                                                                               |

**BremAdder**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| MaxSlope :               | 10.000000                                                                                                 |
| PhotonPT :               | 75.000000                                                                                                 |
| BremChi2Cut :            | 300.00000                                                                                                 |
| BremInput :              | /Event/Phys/StdVeryLooseAllPhotons/Particles                                                              |
| AuditStart :             | False                                                                                                     |
| RKScheme :               | CashKarp                                                                                                  |
| MaxNumSteps :            | 1000                                                                                                      |
| MinStep :                | 10.000000                                                                                                 |
| CorrectNumSteps :        | False                                                                                                     |
| Tolerance :              | 0.0010000000                                                                                              |
| StatEntityList :         | [ ]                                                                                                     |
| RootInTES :              | None                                                                                                      |
| RelToleranceTx :         | 5.0000000e-05                                                                                             |
| AuditFinalize :          | False                                                                                                     |
| PhotonCL :               | 0.10000000                                                                                                |
| MinStepScale :           | 0.12500000                                                                                                |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| ErrorsPrint :            | True                                                                                                      |
| ContextService :         | AlgContextSvc                                                                                             |
| AuditTools :             | False                                                                                                     |
| MaxStep :                | 1000.0000                                                                                                 |
| MonitorService :         | MonitorSvc                                                                                                |
| AuditInitialize :        | False                                                                                                     |
| TypePrint :              | True                                                                                                      |
| BremDllCut :             | -999999.00                                                                                                |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| FieldSvc :               | MagneticFieldSvc                                                                                          |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| Sigma :                  | 5.5000000                                                                                                 |
| MaxStepScale :           | 4.0000000                                                                                                 |
| MaxCurvature :           | 0.0010000000                                                                                              |
| PosTolerance :           | 2.0000000                                                                                                 |
| OutputLevel :            | 3                                                                                                         |
| StepScaleSafetyFactor :  | 1.0000000                                                                                                 |
| UseEfficiencyRowFormat : | True                                                                                                      |
| ExtrapolatorType :       | TrackRungeKuttaExtrapolator                                                                               |
| UseGridInterpolation :   | True                                                                                                      |
| Iterations :             | 5                                                                                                         |
| InitialStep :            | 1000.0000                                                                                                 |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| NumericalJacobian :      | False                                                                                                     |
| BremCorrectionMethod :   | 3                                                                                                         |
| CounterList :            | [ '.\*' ]                                                                                               |

**FilterDesktop/SSFilterEEDarkBosonFilter**

|                 |                                                                                                                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ID=='J/psi(1S)') & (PT \> 250\*MeV) & (MINTREE('e+'==ABSID,PIDe) \> 0) & (MINTREE('e+'==ABSID,MIPCHI2DV(PRIMARY)) \> 9) & (MINTREE('e+'==ABSID,PT) \> 100\*MeV) & (MAXTREE('e+'==ABSID,TRGHP) \< 0.4) & (BPVVDCHI2\>25) & (VFASPF(VCHI2/VDOF)\<10) |
| Inputs          | [ 'Phys/EESSDarkBosonSel' ]                                                                                                                                                                                                                       |
| DecayDescriptor | None                                                                                                                                                                                                                                                |
| Output          | Phys/SSFilterEEDarkBosonFilter/Particles                                                                                                                                                                                                            |

**SubstitutePID/SSEESubPIDDarkBosonSel**

|                 |                                           |
|-----------------|-------------------------------------------|
| Code            | DECTREE('[ J/psi(1S) -\> e+ e+ ]CC')    |
| Inputs          | [ 'Phys/SSFilterEEDarkBosonFilter' ]    |
| DecayDescriptor | None                                      |
| Output          | Phys/SSEESubPIDDarkBosonSel/Particles     |
| Substitutions   | { '[ J/psi(1S) -\> e+ e+ ]CC' : 'KS0' } |

****Tools:****

**SubstitutePIDTool**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| Substitutions :          | { '[ J/psi(1S) -\> e+ e+ ]CC' : 'KS0' }                                                                 |
| ErrorsPrint :            | True                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
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

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsKaons /Particles',True) |

**FilterDesktop/KBDarkBosonFilter**

|                 |                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (PROBNNK\>0.1) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsKaons](./stripping21r0p2-stdallnopidskaons) ' ]                                                                                                               |
| DecayDescriptor | None                                                                                                                                                                                  |
| Output          | Phys/KBDarkBosonFilter/Particles                                                                                                                                                      |

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsPions /Particles',True) |

**FilterDesktop/PiBDarkBosonFilter**

|                 |                                                                                                                                                                                        |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (NINGENERATION( (ID=='gamma') & ((PT \< 500\*MeV) \| (CL \< 0.3)),1)==0) & (TRGHP\<0.3) & (TRCHI2DOF\<3) & (P\>2000\*MeV) & (MIPCHI2DV(PRIMARY)\>9) & (PT\>250\*MeV) & (PROBNNpi\>0.2) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21r0p2-stdallnopidspions) ' ]                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                   |
| Output          | Phys/PiBDarkBosonFilter/Particles                                                                                                                                                      |

**DaVinci::N3BodyDecays/B2KpiX2EESSDarkBosonLine**

|                  |                                                                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KBDarkBosonFilter' , 'Phys/PiBDarkBosonFilter' , 'Phys/SSEESubPIDDarkBosonSel' ]                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                          |
| CombinationCut   | (AM\>4800\*MeV) & (AM\<5800\*MeV) & (ASUM(SUMTREE(PT,(ISBASIC \| (ID=='gamma')),0.0))\>0\*MeV)                                                                                                                        |
| MotherCut        | (PT\>800\*MeV) & (VFASPF(VCHI2/VDOF)\<15) & (BPVLTIME()\>0.2\*ps) & (BPVIPCHI2()\<10) & (BPVDIRA \> 0) & (NINGENERATION(ISBASIC & HASTRACK & (MIPCHI2DV(PRIMARY) \< 9),1)==0) & (MM \> 4800\*MeV) & (MM \< 5800\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[B0 -\> K+ pi- KS0]cc' ]                                                                                                                                                                                       |
| Output           | Phys/B2KpiX2EESSDarkBosonLine/Particles                                                                                                                                                                               |

**AddRelatedInfo/RelatedInfo1_B2KpiX2EESSDarkBosonLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EESSDarkBosonLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo1_B2KpiX2EESSDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo2_B2KpiX2EESSDarkBosonLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EESSDarkBosonLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo2_B2KpiX2EESSDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo3_B2KpiX2EESSDarkBosonLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EESSDarkBosonLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo3_B2KpiX2EESSDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo4_B2KpiX2EESSDarkBosonLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EESSDarkBosonLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo4_B2KpiX2EESSDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo5_B2KpiX2EESSDarkBosonLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EESSDarkBosonLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo5_B2KpiX2EESSDarkBosonLine/Particles |

**AddRelatedInfo/RelatedInfo6_B2KpiX2EESSDarkBosonLine**

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2KpiX2EESSDarkBosonLine' ]                |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo6_B2KpiX2EESSDarkBosonLine/Particles |
