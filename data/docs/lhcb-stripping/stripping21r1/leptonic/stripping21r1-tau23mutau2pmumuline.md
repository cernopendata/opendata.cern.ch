[[stripping21r1 lines]](./stripping21r1-index)

# StrippingTau23MuTau2PMuMuLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/Tau23MuTau2PMuMuLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21r1-stdloosemuons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21r1-stdlooseprotons) /Particles')\>0 |

**CombineParticles/Tau23MuTau2PMuMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21r1-stdloosemuons) ' , 'Phys/ [StdLooseProtons](./stripping21r1-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & ( PIDmu \> -5 ) & ( (PIDmu - PIDK) \> 0 ) & ( TRGHOSTPROB \< 0.3 )' , 'mu-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & ( PIDmu \> -5 ) & ( (PIDmu - PIDK) \> 0 ) & ( TRGHOSTPROB \< 0.3 )' , 'p+' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (PIDp\>10) & ( TRGHOSTPROB \< 0.3 )' , 'p\~-' : ' ( PT \> 300 \* MeV ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) & (PIDp\>10) & ( TRGHOSTPROB \< 0.3 )' } |
| CombinationCut   | ( (ADAMASS('tau+')\<150\*MeV) \| (ADAMASS('Lambda_c+')\<150\*MeV) )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME () \* c_light) \> 100 \* micrometer ) & ( BPVIPCHI2() \< 225 )                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ ' [ tau+ -\> p+ mu+ mu- ]cc' , ' [ tau+ -\> p\~- mu+ mu+ ]cc' , ' [ Lambda_c+ -\> p+ mu+ mu- ]cc' , ' [ Lambda_c+ -\> p\~- mu+ mu+ ]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/Tau23MuTau2PMuMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

**AddRelatedInfo/RelatedInfo1_Tau23MuTau2PMuMuLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau2PMuMuLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_Tau23MuTau2PMuMuLine/Particles |

****Tools:****

**Tool1**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| TracksLocation :         | None                                                                                                      |
| ErrorsPrint :            | True                                                                                                      |
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
| ConeAngle :              | 1.0000000                                                                                                 |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| TrackType :              | 3                                                                                                         |
| Variables :              | [ 'CONEANGLE' , 'CONEMULT' , 'CONEPT' , 'CONEPTASYM' ]                                                  |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**AddRelatedInfo/RelatedInfo2_Tau23MuTau2PMuMuLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau2PMuMuLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_Tau23MuTau2PMuMuLine/Particles |

****Tools:****

**Tool2**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| ErrorsPrint :            | True                                                                                                      |
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
| InputParticles :         | [ '/Event/Phys/StdNoPIDsPions' ]                                                                        |
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| MaxChi2 :                | 9.0000000                                                                                                 |
| Variables :              | [ ]                                                                                                     |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**AddRelatedInfo/RelatedInfo3_Tau23MuTau2PMuMuLine**

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuTau2PMuMuLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_Tau23MuTau2PMuMuLine/Particles |

****Tools:****

**Tool3**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| Transporter :            | ParticleTransporter:PUBLIC                                                                                |
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| GammaCDecays :           | gamma -\> e+ e-                                                                                           |
| TrackExtrapolator :      | TrackMasterExtrapolator:PUBLIC                                                                            |
| ErrorsPrint :            | True                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
| MaxPrints :              | 2                                                                                                         |
| RootOnTES :              | None                                                                                                      |
| DeltaPath :              | 0.0020000000                                                                                              |
| PrintMyAlg :             | True                                                                                                      |
| RootInTES :              | None                                                                                                      |
| ParticlePath :           | /Event/Phys/StdAllNoPIDsPions/Particles                                                                   |
| AuditFinalize :          | False                                                                                                     |
| TypePrint :              | True                                                                                                      |
| UseEfficiencyRowFormat : | True                                                                                                      |
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
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| WeightsFile :            | BsMuMu_TrackIsolationBDT6varsA_v1r4.xml                                                                   |
| MaxIterations :          | 10                                                                                                        |
| TrackType :              | 3                                                                                                         |
| Variables :              | 0                                                                                                         |
| DiGammaDecays :          | [ ( pi0 -\> ) , ( eta -\> ) , ]                                                                         |
| AuditStart :             | False                                                                                                     |
| PVInputLocation :        | Rec/Vertex/Primary                                                                                        |
| ToleranceInZ :           | 0.0020000000                                                                                              |
| MVATransform :           | None                                                                                                      |
| StateProvider :          | TrackStateProvider:PUBLIC                                                                                 |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |
