[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingKshort2Leptons2mu2piVVLine

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/Kshort2Leptons2mu2piVVLine/Particles |
| Postscale      | 1.0000000                                 |
| HLT1           | None                                      |
| HLT2           | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllLooseMuons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdAllLooseMuons /Particles',True) |

**FilterDesktop/Kshort2LeptonsMuonsL**

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PT \> 50.0) &(MIPCHI2DV(PRIMARY) \> 20) &(TRGHOSTPROB \< 0.5) &(PIDmu \> -5) |
| Inputs          | [ 'Phys/ [StdAllLooseMuons](./stripping21r1p2-stdallloosemuons) ' ]         |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Kshort2LeptonsMuonsL/Particles                                           |

**ChargedProtoParticleMaker/MyProtoParticlesVeloKshort2Leptons**

|        |                                       |
|--------|---------------------------------------|
| Inputs | [ 'Rec/Track/Best' ]                |
| Output | Rec/ProtoP/MyProtosVeloKshort2Leptons |

****Tools:****

**TrackSelector**

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
| TrackTypes :              | [ 'Velo' , 'VeloR' , 'Long' , 'Upstream' , 'Downstream' , 'Ttrack' , 'Backward' , 'TT' ]                |
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
| AuditStop :               | False                                                                                                     |
| Context :                 | None                                                                                                      |
| PropertiesPrint :         | False                                                                                                     |
| GlobalTimeOffset :        | 0.0000000                                                                                                 |
| MinLikelihoodCut :        | -1.7976931e+308                                                                                           |
| MinPCut :                 | 0.0000000                                                                                                 |
| MaxPtCut :                | -1.0000000                                                                                                |
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

**NoPIDsParticleMaker/StdNoPIDsVeloPionsKshort2Leptons**

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/MyProtosVeloKshort2Leptons' ]   |
| DecayDescriptor | Pion                                            |
| Output          | Phys/StdNoPIDsVeloPionsKshort2Leptons/Particles |

****Tools:****

**TrackSelector**

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
| MinEtaCut :               | -1.7976931e+308                                                                                           |
| RegularRowFormat :        | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| StatEntityList :          | [ ]                                                                                                     |
| MinNVeloRHits :           | 0                                                                                                         |
| TrackTypes :              | [ 'Velo' , 'VeloR' , 'Long' , 'Upstream' , 'Downstream' , 'Ttrack' , 'Backward' , 'TT' ]                |
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

**FilterDesktop/Kshort2LeptonsPionsV**

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PT \> 50) &(MIPCHI2DV(PRIMARY) \> 10) &(TRGHOSTPROB \< 0.35) &(PIDK \< -3.5) |
| Inputs          | [ 'Phys/StdNoPIDsVeloPionsKshort2Leptons' ]                                 |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Kshort2LeptonsPionsV/Particles                                           |

**CombineParticles/Kshort2Leptons2mu2piVVLine**

|                  |                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kshort2LeptonsMuonsL' , 'Phys/Kshort2LeptonsPionsV' ]                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                           |
| CombinationCut   | (AM \< 900.0 \*MeV) & (AMAXDOCA('') \< 1.0 \*mm) & ( ( ANUM( ( TRTYPE == 3 ) & ( ABSID == 'mu+' ) ) == 2 ) ) & ( ( ANUM( ( TRTYPE == 1 ) & ( ABSID == 'pi+' ) ) == 2 ) ) |
| MotherCut        | ( M \< 900.0 \*MeV) &( MIPDV(PRIMARY) \< 8 \*mm) & ( BPVVDCHI2 \> 2500) & ( VFASPF(VCHI2/VDOF) \< 40)                                                                    |
| DecayDescriptor  | None                                                                                                                                                                     |
| DecayDescriptors | [ 'KS0 -\> mu+ mu- pi+ pi+' , 'KS0 -\> mu+ mu- pi+ pi-' , 'KS0 -\> mu+ mu- pi- pi+' , 'KS0 -\> mu+ mu- pi- pi-' ]                                                      |
| Output           | Phys/Kshort2Leptons2mu2piVVLine/Particles                                                                                                                                |
