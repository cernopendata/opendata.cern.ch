[[stripping21 lines]](./stripping21-index)

# StrippingDijetsPrescaledLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/DijetsPrescaledLine/Particles      |
| Postscale      | 1.0000000                               |
| HLT            | HLT_PASS_RE('Hlt1TrackMuon.\*Decision') |
| Prescale       | 0.030000000                             |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

**LoKi::VoidFilter/StrippingDijetsPrescaledLineVOIDFilter**

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_PFParticles_Particles**

|      |                                           |
|------|-------------------------------------------|
| Code | CONTAINS('Phys/PFParticles/Particles')\>0 |

**LoKi::PFJetMaker/DijetsJetsSelection**

|                 |                                    |
|-----------------|------------------------------------|
| Inputs          | [ 'Phys/PFParticles' ]           |
| DecayDescriptor | None                               |
| Output          | Phys/DijetsJetsSelection/Particles |

****Tools:****

**LoKi::FastJetMaker**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| RParameter :             | 0.70000000                                                                                                |
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| Strategy :               | 1                                                                                                         |
| Type :                   | 0                                                                                                         |
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
| JetID :                  | 98                                                                                                        |
| AuditStop :              | False                                                                                                     |
| PtMin :                  | 0.0000000                                                                                                 |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| UseEfficiencyRowFormat : | True                                                                                                      |
| AuditStart :             | False                                                                                                     |
| Recombination :          | 0                                                                                                         |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**LoKi::DistanceCalculator**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| GammaCDecays :           | gamma -\> e+ e-                                                                                           |
| PropertiesPrint :        | False                                                                                                     |
| TrackExtrapolator :      | TrackMasterExtrapolator:PUBLIC                                                                            |
| ErrorsPrint :            | True                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
| MaxPrints :              | 2                                                                                                         |
| RootOnTES :              | None                                                                                                      |
| DeltaPath :              | 0.0020000000                                                                                              |
| PrintMyAlg :             | True                                                                                                      |
| RootInTES :              | None                                                                                                      |
| AuditFinalize :          | False                                                                                                     |
| TypePrint :              | True                                                                                                      |
| Transporter :            | ParticleTransporter:PUBLIC                                                                                |
| ContextService :         | AlgContextSvc                                                                                             |
| DeltaChi2 :              | 0.050000000                                                                                               |
| AuditTools :             | False                                                                                                     |
| MonitorService :         | MonitorSvc                                                                                                |
| AuditInitialize :        | False                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| UseEfficiencyRowFormat : | True                                                                                                      |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| MaxIterations :          | 10                                                                                                        |
| DiGammaDecays :          | [ ( pi0 -\> ) , ( eta -\> ) , ]                                                                         |
| AuditStart :             | False                                                                                                     |
| ToleranceInZ :           | 0.0020000000                                                                                              |
| StateProvider :          | TrackStateProvider:PUBLIC                                                                                 |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**CombineParticles/DijetsPrescaledLine**

|                  |                                              |
|------------------|----------------------------------------------|
| Inputs           | [ 'Phys/DijetsJetsSelection' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : 'PT \> 19000.0' } |
| CombinationCut   | COSDPHI \< -0.8                              |
| MotherCut        | ALL                                          |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet                     |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet' ]             |
| Output           | Phys/DijetsPrescaledLine/Particles           |
