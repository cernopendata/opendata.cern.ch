[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingFullDiJetsLine

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/FullDiJetsLine/Particles |
| Postscale      | 1.0000000                     |
| HLT1           | None                          |
| HLT2           | None                          |
| Prescale       | 0.050000000                   |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionEW**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamEWBadEvent') & \~ALG_PASSED('StrippingStreamEWBadEvent') |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdJets_Particles**

|      |                                                                           |
|------|---------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdJets](./stripping21r1p1-stdjets) /Particles',True)\>0 |

**CombineParticles/FullDiJetsLine**

|                  |                                                     |
|------------------|-----------------------------------------------------|
| Inputs           | [ 'Phys/ [StdJets](./stripping21r1p1-stdjets) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : ' (PT \> 20000.0 ) ' }   |
| CombinationCut   | AALLSAMEBPV                                         |
| MotherCut        | ALL                                                 |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet                            |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet' ]                    |
| Output           | Phys/FullDiJetsLine/Particles                       |

****Tools:****

**LoKi::VertexFitter**

|                                |                                                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| MaxIterForRemove :             | 5                                                                                                         |
| StatTableHeader :              | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| SeedZmax :                     | 3000.0000                                                                                                 |
| PropertiesPrint :              | False                                                                                                     |
| USeShortLivedParticlesAsSeed : | True                                                                                                      |
| SeedZmin :                     | -1000.0000                                                                                                |
| GammaCDecays :                 | gamma -\> e+ e-                                                                                           |
| ErrorsPrint :                  | True                                                                                                      |
| StatEntityList :               | [ ]                                                                                                     |
| MaxPrints :                    | 2                                                                                                         |
| PrintMyAlg :                   | False                                                                                                     |
| RootInTES :                    | None                                                                                                      |
| DeltaDistance :                | 0.0010000000                                                                                              |
| AllowRhoPlusLikeParticle :     | True                                                                                                      |
| TypePrint :                    | True                                                                                                      |
| Jets :                         | None                                                                                                      |
| Transporter :                  | ParticleTransporter:PUBLIC                                                                                |
| ContextService :               | AlgContextSvc                                                                                             |
| DeltaChi2 :                    | 0.010000000                                                                                               |
| AuditTools :                   | False                                                                                                     |
| MonitorService :               | MonitorSvc                                                                                                |
| AuditInitialize :              | False                                                                                                     |
| RegularRowFormat :             | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :                  | 3                                                                                                         |
| StatPrint :                    | True                                                                                                      |
| AuditFinalize :                | False                                                                                                     |
| SeedRhoZmax :                  | 800.00000                                                                                                 |
| AuditStop :                    | False                                                                                                     |
| Context :                      | None                                                                                                      |
| UseEfficiencyRowFormat :       | True                                                                                                      |
| GlobalTimeOffset :             | 0.0000000                                                                                                 |
| SeedRhoZmin :                  | 200.00000                                                                                                 |
| Massage :                      | [ ]                                                                                                     |
| MeasureCPUPerformance :        | False                                                                                                     |
| MaxIterations :                | 10                                                                                                        |
| TransportTolerance :           | 0.010000000                                                                                               |
| DiGammaDecays :                | [ ( pi0 -\> ) , ( eta -\> ) , ]                                                                         |
| AuditStart :                   | False                                                                                                     |
| MaxIterForAdd :                | 5                                                                                                         |
| UseOptimizedAlgorithm :        | True                                                                                                      |
| EfficiencyRowFormat :          | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :                  | [ '.\*' ]                                                                                               |
