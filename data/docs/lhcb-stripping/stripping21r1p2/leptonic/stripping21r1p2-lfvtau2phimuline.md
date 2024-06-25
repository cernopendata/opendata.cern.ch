[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLFVTau2PhiMuLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/LFVTau2PhiMuLine/Particles |
| Postscale      | 1.0000000                       |
| HLT1           | None                            |
| HLT2           | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseKaons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseKaons /Particles',True) |

**CombineParticles/LFVTau2PhiMuSelPhi**

|                  |                                                                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseKaons](./stripping21r1p2-stdloosekaons) ' ]                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3) & (PT\>300\*MeV) & (PIDK \> 0) & ( BPVIPCHI2 () \> 9 )' , 'K-' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3) & (PT\>300\*MeV) & (PIDK \> 0) & ( BPVIPCHI2 () \> 9 )' } |
| CombinationCut   | (ADAMASS('phi(1020)')\<30\*MeV)                                                                                                                                                                                                                        |
| MotherCut        | ( VFASPF(VCHI2) \< 25 ) & (MIPCHI2DV(PRIMARY)\> 9)                                                                                                                                                                                                     |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                                                                                                                                            |
| Output           | Phys/LFVTau2PhiMuSelPhi/Particles                                                                                                                                                                                                                      |

**LoKi::VoidFilter/SELECT:Phys/StdLooseMuons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseMuons /Particles',True) |

**CombineParticles/LFVTau2PhiMumakeTau**

|                  |                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LFVTau2PhiMuSelPhi' , 'Phys/ [StdLooseMuons](./stripping21r1p2-stdloosemuons) ' ]                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3) & ( BPVIPCHI2 () \> 9 )' , 'mu-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3) & ( BPVIPCHI2 () \> 9 )' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | (ADAMASS('tau-')\<150\*MeV)                                                                                                                                                                                                                  |
| MotherCut        | ( VFASPF(VCHI2) \< 25 ) & ( (BPVLTIME () \* c_light) \> 50 \* micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                          |
| DecayDescriptor  | [ tau+ -\> phi(1020) mu+ ]cc                                                                                                                                                                                                               |
| DecayDescriptors | [ ' [ tau+ -\> phi(1020) mu+ ]cc' ]                                                                                                                                                                                                      |
| Output           | Phys/LFVTau2PhiMumakeTau/Particles                                                                                                                                                                                                           |

**TisTosParticleTagger/LFVTau2PhiMuLine**

|                 |                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMumakeTau' ]                                                                                       |
| DecayDescriptor | None                                                                                                                   |
| Output          | Phys/LFVTau2PhiMuLine/Particles                                                                                        |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 , 'Hlt1TrackMuonDecision%TOS' : 0 , 'L0Global%TIS' : 0 , 'L0MuonDecision%TOS' : 0 } |

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
| CaloClustForCharged :           | True                                                                                                      |
| TOSFracTT :                     | 0.0000000                                                                                                 |
| TISFracEcal :                   | 0.0099000000                                                                                              |
| TOSFracHcal :                   | 0.010000000                                                                                               |
| RootInTES :                     | None                                                                                                      |
| HltSelReportsLocation :         | Hlt/SelReports                                                                                            |
| AuditFinalize :                 | False                                                                                                     |
| TISFracVelo :                   | 0.010000000                                                                                               |
| ProjectTracksToCalo :           | True                                                                                                      |
| ErrorsPrint :                   | True                                                                                                      |
| ContextService :                | AlgContextSvc                                                                                             |
| AuditTools :                    | False                                                                                                     |
| HltDecReportsLocation :         | Hlt/DecReports                                                                                            |
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
| TOSFracEcal :                   | 0.010000000                                                                                               |
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
| CaloClustForCharged :           | True                                                                                                      |
| TOSFracTT :                     | 0.0000000                                                                                                 |
| TISFracEcal :                   | 0.0099000000                                                                                              |
| TOSFracHcal :                   | 0.010000000                                                                                               |
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
| TOSFracEcal :                   | 0.010000000                                                                                               |
| TOSFracMuon :                   | 0.00010000000                                                                                             |
| AuditStart :                    | False                                                                                                     |
| NoHitTypes :                    | False                                                                                                     |
| TISFracOTIT :                   | 0.010000000                                                                                               |
| TOSFracOTIT :                   | 0.70000000                                                                                                |
| TOSFracVelo :                   | 0.70000000                                                                                                |
| EfficiencyRowFormat :           | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| FullAnalysisReport :            | True                                                                                                      |
| CounterList :                   | [ '.\*' ]                                                                                               |

**L0TriggerTisTosTool**

|                                 |                                                                                                           |
|---------------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :               | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| UseParticle2LHCbIDsMap :        | 1                                                                                                         |
| AllowIntermediateSelections :   | False                                                                                                     |
| Particle2LHCbIDsMapLocation :   | None                                                                                                      |
| CompositeTPSviaPartialTOSonly : | False                                                                                                     |
| TriggerInputWarnings :          | False                                                                                                     |
| StatEntityList :                | [ ]                                                                                                     |
| CaloClustForCharged :           | True                                                                                                      |
| TOSFracTT :                     | 0.0000000                                                                                                 |
| TISFracEcal :                   | 0.0099000000                                                                                              |
| TOSFracHcal :                   | 0.010000000                                                                                               |
| RootInTES :                     | None                                                                                                      |
| HltSelReportsLocation :         | HltLikeL0/SelReports                                                                                      |
| AuditFinalize :                 | False                                                                                                     |
| TISFracVelo :                   | 0.010000000                                                                                               |
| ProjectTracksToCalo :           | True                                                                                                      |
| ErrorsPrint :                   | True                                                                                                      |
| ContextService :                | AlgContextSvc                                                                                             |
| AuditTools :                    | False                                                                                                     |
| HltDecReportsLocation :         | HltLikeL0/DecReports                                                                                      |
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
| TOSFracEcal :                   | 0.010000000                                                                                               |
| TOSFracMuon :                   | 0.00010000000                                                                                             |
| AuditStart :                    | False                                                                                                     |
| NoHitTypes :                    | False                                                                                                     |
| TISFracOTIT :                   | 0.010000000                                                                                               |
| TOSFracOTIT :                   | 0.70000000                                                                                                |
| TOSFracVelo :                   | 0.70000000                                                                                                |
| EfficiencyRowFormat :           | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| FullAnalysisReport :            | True                                                                                                      |
| CounterList :                   | [ '.\*' ]                                                                                               |

**AddRelatedInfo/RelatedInfo1_LFVTau2PhiMuLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_LFVTau2PhiMuLine/Particles |

**AddRelatedInfo/RelatedInfo2_LFVTau2PhiMuLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo2_LFVTau2PhiMuLine/Particles |

**AddRelatedInfo/RelatedInfo3_LFVTau2PhiMuLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo3_LFVTau2PhiMuLine/Particles |

**AddRelatedInfo/RelatedInfo4_LFVTau2PhiMuLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo4_LFVTau2PhiMuLine/Particles |

**AddRelatedInfo/RelatedInfo5_LFVTau2PhiMuLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo5_LFVTau2PhiMuLine/Particles |

**AddRelatedInfo/RelatedInfo6_LFVTau2PhiMuLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/LFVTau2PhiMuLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo6_LFVTau2PhiMuLine/Particles |
