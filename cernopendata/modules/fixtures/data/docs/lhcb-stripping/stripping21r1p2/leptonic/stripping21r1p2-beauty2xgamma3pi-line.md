[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBeauty2XGamma3pi_Line

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/Beauty2XGamma3pi_Line/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

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

**LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions**

|      |                                       |
|------|---------------------------------------|
| Code | 0 StdAllNoPIDsPions /Particles',True) |

**FilterDesktop/TrackListBeauty2XGamma**

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (HASTRACK) & (TRCHI2DOF \< 3.0)& (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.4) & (PT \> 300.0) & (P \> 1000) |
| Inputs          | [ 'Phys/ [StdAllNoPIDsPions](./stripping21r1p2-stdallnopidspions) ' ]                                            |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/TrackListBeauty2XGamma/Particles                                                                              |

**DaVinci::N3BodyDecays/TriTracks_NBodyDecay_ForRadiativeBBeauty2XGamma**

|                  |                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TrackListBeauty2XGamma' ]                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                        |
| CombinationCut   | AHASCHILD((ISBASIC & (HASTRACK) & (TRCHI2DOF\<3) & (PT \> 500\*MeV) & (P \> 5000\*MeV))\|((ABSID=='KS0') & (PT \> 500\*MeV) & (P \> 5000\*MeV))) & (ASUM(PT) \> 1000.0) & in_range( 0.0 , AM ,7900.0) |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 10.0) & (PT \> 150.0) & (BPVVDCHI2 \> 0.0) & (MIPCHI2DV(PRIMARY) \> 0.0)                                                                                         |
| DecayDescriptor  | [K_1(1270)+ -\> pi+ pi- pi+]cc                                                                                                                                                                      |
| DecayDescriptors | [ '[K_1(1270)+ -\> pi+ pi- pi+]cc' ]                                                                                                                                                              |
| Output           | Phys/TriTracks_NBodyDecay_ForRadiativeBBeauty2XGamma/Particles                                                                                                                                        |

**LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons**

|      |                                        |
|------|----------------------------------------|
| Code | 0 StdLooseAllPhotons /Particles',True) |

**FilterDesktop/PhotonSelBeauty2XGamma**

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 2000.0) & (CL \> 0.0)                                              |
| Inputs          | [ 'Phys/ [StdLooseAllPhotons](./stripping21r1p2-stdlooseallphotons) ' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/PhotonSelBeauty2XGamma/Particles                                     |

**CombineParticles/Beauty2XGamma3pi\_**

|                  |                                                                                              |
|------------------|----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PhotonSelBeauty2XGamma' , 'Phys/TriTracks_NBodyDecay_ForRadiativeBBeauty2XGamma' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K_1(1270)+' : 'ALL' , 'K_1(1270)-' : 'ALL' , 'gamma' : 'ALL' }               |
| CombinationCut   | in_range( 2400.0 ,AM, 9000 ) & (ASUM(PT) \> 3000 )                                           |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 9.0 ) & (BPVIPCHI2() \< 9.0 ) & (BPVDIRA \> 0.0)        |
| DecayDescriptor  | [B+ -\> K_1(1270)+ gamma]cc                                                                |
| DecayDescriptors | [ '[B+ -\> K_1(1270)+ gamma]cc' ]                                                        |
| Output           | Phys/Beauty2XGamma3pi\_/Particles                                                            |

**TisTosParticleTagger/Beauty2XGamma3pi_Line**

|                 |                                                                                                                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma3pi\_' ]                                                                                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                                                                                      |
| Output          | Phys/Beauty2XGamma3pi_Line/Particles                                                                                                                                                                                                      |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Radiative.\*Decision%TIS' : 0 , 'Hlt2Radiative.\*Decision%TOS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |

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
| CaloClustForCharged :           | True                                                                                                      |
| TOSFracTT :                     | 0.0000000                                                                                                 |
| TISFracEcal :                   | 0.0099000000                                                                                              |
| TOSFracHcal :                   | 0.010000000                                                                                               |
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

**AddRelatedInfo/RelatedInfo1_Beauty2XGamma3pi_Line**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma3pi_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_Beauty2XGamma3pi_Line/Particles |

**AddRelatedInfo/RelatedInfo2_Beauty2XGamma3pi_Line**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma3pi_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_Beauty2XGamma3pi_Line/Particles |

**AddRelatedInfo/RelatedInfo3_Beauty2XGamma3pi_Line**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma3pi_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_Beauty2XGamma3pi_Line/Particles |

**AddRelatedInfo/RelatedInfo4_Beauty2XGamma3pi_Line**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma3pi_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo4_Beauty2XGamma3pi_Line/Particles |

**AddRelatedInfo/RelatedInfo5_Beauty2XGamma3pi_Line**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma3pi_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo5_Beauty2XGamma3pi_Line/Particles |

**AddRelatedInfo/RelatedInfo6_Beauty2XGamma3pi_Line**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma3pi_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo6_Beauty2XGamma3pi_Line/Particles |

**AddRelatedInfo/RelatedInfo7_Beauty2XGamma3pi_Line**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma3pi_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo7_Beauty2XGamma3pi_Line/Particles |

**AddRelatedInfo/RelatedInfo8_Beauty2XGamma3pi_Line**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma3pi_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo8_Beauty2XGamma3pi_Line/Particles |

**AddRelatedInfo/RelatedInfo9_Beauty2XGamma3pi_Line**

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGamma3pi_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo9_Beauty2XGamma3pi_Line/Particles |
