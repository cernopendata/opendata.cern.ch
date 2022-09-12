[[stripping21 lines]](./stripping21-index)

# StrippingBetaSPsi2SMuMu_InclPsi2SToMuMuLine

## Properties:

|                |                                                   |
|----------------|---------------------------------------------------|
| OutputLocation | Phys/BetaSPsi2SMuMu_InclPsi2SToMuMuLine/Particles |
| Postscale      | 1.0000000                                         |
| HLT            | None                                              |
| Prescale       | 0.10000000                                        |
| L0DU           | None                                              |
| ODIN           | None                                              |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) /Particles')\>0 |

**CombineParticles/BetaSPsi2SMuMu_Psi2SToMuMu**

|                  |                                                                   |
|------------------|-------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'PIDmu \> 0.0' , 'mu-' : 'PIDmu\>0.0' }    |
| CombinationCut   | (ADAMASS('psi(2S)')\<60.0\*MeV) & (ADOCACHI2CUT( 30.0 ,''))       |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 16) & (MFIT)                               |
| DecayDescriptor  | psi(2S) -\> mu+ mu-                                               |
| DecayDescriptors | [ 'psi(2S) -\> mu+ mu-' ]                                       |
| Output           | Phys/BetaSPsi2SMuMu_Psi2SToMuMu/Particles                         |

****Tools:****

**LoKi::MassFitter**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| Tolerance :              | 0.020000000                                                                                               |
| ErrorsPrint :            | True                                                                                                      |
| ChangeVertex :           | True                                                                                                      |
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
| MaxIterations :          | 20                                                                                                        |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**FilterDesktop/BetaSPsi2SMuMu_InclPsi2SToMuMu**

|                 |                                               |
|-----------------|-----------------------------------------------|
| Code            | ALL                                           |
| Inputs          | [ 'Phys/BetaSPsi2SMuMu_Psi2SToMuMu' ]       |
| DecayDescriptor | None                                          |
| Output          | Phys/BetaSPsi2SMuMu_InclPsi2SToMuMu/Particles |

**TisTosParticleTagger/BetaSPsi2SMuMu_InclPsi2SToMuMuHlt1TOS_SelTisTos**

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/BetaSPsi2SMuMu_InclPsi2SToMuMu' ]                    |
| DecayDescriptor | None                                                           |
| Output          | Phys/BetaSPsi2SMuMu_InclPsi2SToMuMuHlt1TOS_SelTisTos/Particles |
| TisTosSpecs     | { 'Hlt1DiMuonHighMassDecision%TOS' : 0 }                       |

****Tools:****

**TriggerTisTosTool**

|                                 |                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :               | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| UseParticle2LHCbIDsMap :        | 1                                                                                                         |
| AllowIntermediateSelections :   | False                                                                                                     |
| Particle2LHCbIDsMapLocation :   | None                                                                                                      |
| CompositeTPSviaPartialTOSonly : | False                                                                                                     |
| TriggerInputWarnings :          | False                                                                                                     |
| StatEntityList :                | [ ]                                                                                                     |
| RootOnTES :                     | None                                                                                                      |
| CaloClustForCharged :           | False                                                                                                     |
| TOSFracTT :                     | 0.0000000                                                                                                 |
| TISFracEcal :                   | 0.0099000000                                                                                              |
| TOSFracHcal :                   | 0.0000000                                                                                                 |
| RootInTES :                     | None                                                                                                      |
| HltSelReportsLocation :         | Hlt/SelReports                                                                                            |
| AuditFinalize :                 | False                                                                                                     |
| TISFracVelo :                   | 0.010000000                                                                                               |
| ProjectTracksToCalo :           | False                                                                                                     |
| ErrorsPrint :                   | True                                                                                                      |
| ContextService :                | AlgContextSvc                                                                                             |
| AuditTools :                    | False                                                                                                     |
| HltDecReportsLocation :         | Hlt/DecReports                                                                                            |
| TISFracTT :                     | 0.010000000                                                                                               |
| MonitorService :                | MonitorSvc                                                                                                |
| AuditInitialize :               | False                                                                                                     |
| RegularRowFormat :              | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| CaloClustForNeutral :           | False                                                                                                     |
| TypePrint :                     | True                                                                                                      |
| StatPrint :                     | True                                                                                                      |
| TISFracMuon :                   | 0.00010000000                                                                                             |
| TISFracHcal :                   | 0.0099000000                                                                                              |
| AuditStop :                     | False                                                                                                     |
| Context :                       | None                                                                                                      |
| PropertiesPrint :               | False                                                                                                     |
| GlobalTimeOffset :              | 0.0000000                                                                                                 |
| UseEfficiencyRowFormat :        | True                                                                                                      |
| OutputLevel :                   | 3                                                                                                         |
| TOSFracEcal :                   | 0.0000000                                                                                                 |
| TOSFracMuon :                   | 0.00010000000                                                                                             |
| AuditStart :                    | False                                                                                                     |
| NoHitTypes :                    | False                                                                                                     |
| TISFracOTIT :                   | 0.010000000                                                                                               |
| TOSFracOTIT :                   | 0.70000000                                                                                                |
| TOSFracVelo :                   | 0.70000000                                                                                                |
| EfficiencyRowFormat :           | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| FullAnalysisReport :            | True                                                                                                      |
| CounterList :                   | [ '.\*' ]                                                                                               |

**Hlt1TriggerTisTosTool**

|                                 |                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :               | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| UseParticle2LHCbIDsMap :        | 1                                                                                                         |
| AllowIntermediateSelections :   | False                                                                                                     |
| Particle2LHCbIDsMapLocation :   | None                                                                                                      |
| CompositeTPSviaPartialTOSonly : | False                                                                                                     |
| TriggerInputWarnings :          | False                                                                                                     |
| StatEntityList :                | [ ]                                                                                                     |
| RootOnTES :                     | None                                                                                                      |
| CaloClustForCharged :           | True                                                                                                      |
| TOSFracTT :                     | 0.0000000                                                                                                 |
| TISFracEcal :                   | 0.0099000000                                                                                              |
| TOSFracHcal :                   | 0.0000000                                                                                                 |
| RootInTES :                     | None                                                                                                      |
| HltSelReportsLocation :         | Hlt1/SelReports                                                                                           |
| AuditFinalize :                 | False                                                                                                     |
| TISFracVelo :                   | 0.010000000                                                                                               |
| ProjectTracksToCalo :           | True                                                                                                      |
| ErrorsPrint :                   | True                                                                                                      |
| ContextService :                | AlgContextSvc                                                                                             |
| AuditTools :                    | False                                                                                                     |
| HltDecReportsLocation :         | Hlt1/DecReports                                                                                           |
| TISFracTT :                     | 0.010000000                                                                                               |
| MonitorService :                | MonitorSvc                                                                                                |
| AuditInitialize :               | False                                                                                                     |
| RegularRowFormat :              | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| CaloClustForNeutral :           | True                                                                                                      |
| TypePrint :                     | True                                                                                                      |
| StatPrint :                     | True                                                                                                      |
| TISFracMuon :                   | 0.00010000000                                                                                             |
| TISFracHcal :                   | 0.0099000000                                                                                              |
| AuditStop :                     | False                                                                                                     |
| Context :                       | None                                                                                                      |
| PropertiesPrint :               | False                                                                                                     |
| GlobalTimeOffset :              | 0.0000000                                                                                                 |
| UseEfficiencyRowFormat :        | True                                                                                                      |
| OutputLevel :                   | 3                                                                                                         |
| TOSFracEcal :                   | 0.0000000                                                                                                 |
| TOSFracMuon :                   | 0.00010000000                                                                                             |
| AuditStart :                    | False                                                                                                     |
| NoHitTypes :                    | False                                                                                                     |
| TISFracOTIT :                   | 0.010000000                                                                                               |
| TOSFracOTIT :                   | 0.70000000                                                                                                |
| TOSFracVelo :                   | 0.70000000                                                                                                |
| EfficiencyRowFormat :           | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| FullAnalysisReport :            | True                                                                                                      |
| CounterList :                   | [ '.\*' ]                                                                                               |

**TisTosParticleTagger/BetaSPsi2SMuMu_InclPsi2SToMuMuLine**

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Phys/BetaSPsi2SMuMu_InclPsi2SToMuMuHlt1TOS_SelTisTos' ] |
| DecayDescriptor | None                                                         |
| Output          | Phys/BetaSPsi2SMuMu_InclPsi2SToMuMuLine/Particles            |
| TisTosSpecs     | { 'Hlt2DiMuonPsi2SDecision%TOS' : 0 }                        |

****Tools:****

**TriggerTisTosTool**

|                                 |                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :               | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| UseParticle2LHCbIDsMap :        | 1                                                                                                         |
| AllowIntermediateSelections :   | False                                                                                                     |
| Particle2LHCbIDsMapLocation :   | None                                                                                                      |
| CompositeTPSviaPartialTOSonly : | False                                                                                                     |
| TriggerInputWarnings :          | False                                                                                                     |
| StatEntityList :                | [ ]                                                                                                     |
| RootOnTES :                     | None                                                                                                      |
| CaloClustForCharged :           | False                                                                                                     |
| TOSFracTT :                     | 0.0000000                                                                                                 |
| TISFracEcal :                   | 0.0099000000                                                                                              |
| TOSFracHcal :                   | 0.0000000                                                                                                 |
| RootInTES :                     | None                                                                                                      |
| HltSelReportsLocation :         | Hlt/SelReports                                                                                            |
| AuditFinalize :                 | False                                                                                                     |
| TISFracVelo :                   | 0.010000000                                                                                               |
| ProjectTracksToCalo :           | False                                                                                                     |
| ErrorsPrint :                   | True                                                                                                      |
| ContextService :                | AlgContextSvc                                                                                             |
| AuditTools :                    | False                                                                                                     |
| HltDecReportsLocation :         | Hlt/DecReports                                                                                            |
| TISFracTT :                     | 0.010000000                                                                                               |
| MonitorService :                | MonitorSvc                                                                                                |
| AuditInitialize :               | False                                                                                                     |
| RegularRowFormat :              | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| CaloClustForNeutral :           | False                                                                                                     |
| TypePrint :                     | True                                                                                                      |
| StatPrint :                     | True                                                                                                      |
| TISFracMuon :                   | 0.00010000000                                                                                             |
| TISFracHcal :                   | 0.0099000000                                                                                              |
| AuditStop :                     | False                                                                                                     |
| Context :                       | None                                                                                                      |
| PropertiesPrint :               | False                                                                                                     |
| GlobalTimeOffset :              | 0.0000000                                                                                                 |
| UseEfficiencyRowFormat :        | True                                                                                                      |
| OutputLevel :                   | 3                                                                                                         |
| TOSFracEcal :                   | 0.0000000                                                                                                 |
| TOSFracMuon :                   | 0.00010000000                                                                                             |
| AuditStart :                    | False                                                                                                     |
| NoHitTypes :                    | False                                                                                                     |
| TISFracOTIT :                   | 0.010000000                                                                                               |
| TOSFracOTIT :                   | 0.70000000                                                                                                |
| TOSFracVelo :                   | 0.70000000                                                                                                |
| EfficiencyRowFormat :           | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| FullAnalysisReport :            | True                                                                                                      |
| CounterList :                   | [ '.\*' ]                                                                                               |

**Hlt2TriggerTisTosTool**

|                                 |                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :               | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| UseParticle2LHCbIDsMap :        | 1                                                                                                         |
| AllowIntermediateSelections :   | False                                                                                                     |
| Particle2LHCbIDsMapLocation :   | None                                                                                                      |
| CompositeTPSviaPartialTOSonly : | False                                                                                                     |
| TriggerInputWarnings :          | False                                                                                                     |
| StatEntityList :                | [ ]                                                                                                     |
| RootOnTES :                     | None                                                                                                      |
| CaloClustForCharged :           | True                                                                                                      |
| TOSFracTT :                     | 0.0000000                                                                                                 |
| TISFracEcal :                   | 0.0099000000                                                                                              |
| TOSFracHcal :                   | 0.0000000                                                                                                 |
| RootInTES :                     | None                                                                                                      |
| HltSelReportsLocation :         | Hlt2/SelReports                                                                                           |
| AuditFinalize :                 | False                                                                                                     |
| TISFracVelo :                   | 0.010000000                                                                                               |
| ProjectTracksToCalo :           | True                                                                                                      |
| ErrorsPrint :                   | True                                                                                                      |
| ContextService :                | AlgContextSvc                                                                                             |
| AuditTools :                    | False                                                                                                     |
| HltDecReportsLocation :         | Hlt2/DecReports                                                                                           |
| TISFracTT :                     | 0.010000000                                                                                               |
| MonitorService :                | MonitorSvc                                                                                                |
| AuditInitialize :               | False                                                                                                     |
| RegularRowFormat :              | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| CaloClustForNeutral :           | True                                                                                                      |
| TypePrint :                     | True                                                                                                      |
| StatPrint :                     | True                                                                                                      |
| TISFracMuon :                   | 0.00010000000                                                                                             |
| TISFracHcal :                   | 0.0099000000                                                                                              |
| AuditStop :                     | False                                                                                                     |
| Context :                       | None                                                                                                      |
| PropertiesPrint :               | False                                                                                                     |
| GlobalTimeOffset :              | 0.0000000                                                                                                 |
| UseEfficiencyRowFormat :        | True                                                                                                      |
| OutputLevel :                   | 3                                                                                                         |
| TOSFracEcal :                   | 0.0000000                                                                                                 |
| TOSFracMuon :                   | 0.00010000000                                                                                             |
| AuditStart :                    | False                                                                                                     |
| NoHitTypes :                    | False                                                                                                     |
| TISFracOTIT :                   | 0.010000000                                                                                               |
| TOSFracOTIT :                   | 0.70000000                                                                                                |
| TOSFracVelo :                   | 0.70000000                                                                                                |
| EfficiencyRowFormat :           | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| FullAnalysisReport :            | True                                                                                                      |
| CounterList :                   | [ '.\*' ]                                                                                               |
