[[stripping21 lines]](./stripping21-index)

# StrippingRareStrangeKPiPiPiMassMeasDownLine

## Properties:

|                |                                                   |
|----------------|---------------------------------------------------|
| OutputLocation | Phys/RareStrangeKPiPiPiMassMeasDownLine/Particles |
| Postscale      | 1.0000000                                         |
| HLT            | None                                              |
| Prescale       | 1.0000000                                         |
| L0DU           | None                                              |
| ODIN           | None                                              |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsDownPions_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsDownPions](./stripping21-stdnopidsdownpions) /Particles')\>0 |

**CombineParticles/RareStrangeKPiPiPiMassMeasDownLine**

|                  |                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdNoPIDsDownPions](./stripping21-stdnopidsdownpions) ' ]                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(TRCHI2DOF\<5) & (TRGHOSTPROB \< 0.3) & (MIPCHI2DV(PRIMARY)\>4.0)' , 'pi-' : '(TRCHI2DOF\<5) & (TRGHOSTPROB \< 0.3) & (MIPCHI2DV(PRIMARY)\>4.0)' } |
| CombinationCut   | (ADAMASS('K+') \< 100.0 \*MeV) & (AMAXDOCA('')\< 9999.0 \*mm)                                                                                                              |
| MotherCut        | (PT\> 250.0) & (ADMASS('K+') \< 100.0 \*MeV) & (BPVDIRA \> 0.999)& (VFASPF(VCHI2) \< 20.0) & (BPVVDCHI2 \> 64.0) & (BPVVDZ \> 900.0\*mm) & (BPVVDZ \< 2200.0\*mm)          |
| DecayDescriptor  | [K+ -\> pi+ pi+ pi-]cc                                                                                                                                                   |
| DecayDescriptors | [ '[K+ -\> pi+ pi+ pi-]cc' ]                                                                                                                                           |
| Output           | Phys/RareStrangeKPiPiPiMassMeasDownLine/Particles                                                                                                                          |

**AddRelatedInfo/RelatedInfo1_RareStrangeKPiPiPiMassMeasDownLine**

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiMassMeasDownLine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo1_RareStrangeKPiPiPiMassMeasDownLine/Particles |

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
| ConeAngle :              | 0.90000000                                                                                                |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| TrackType :              | 3                                                                                                         |
| Variables :              | [ 'CONEANGLE' , 'CONEMULT' , 'CONEPTASYM' ]                                                             |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**AddRelatedInfo/RelatedInfo2_RareStrangeKPiPiPiMassMeasDownLine**

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiMassMeasDownLine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo2_RareStrangeKPiPiPiMassMeasDownLine/Particles |

****Tools:****

**Tool2**

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
| Variables :              | [ 'CONEANGLE' , 'CONEMULT' , 'CONEPTASYM' ]                                                             |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**AddRelatedInfo/RelatedInfo3_RareStrangeKPiPiPiMassMeasDownLine**

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiMassMeasDownLine' ]                |
| DecayDescriptor | None                                                           |
| Output          | Phys/RelatedInfo3_RareStrangeKPiPiPiMassMeasDownLine/Particles |

****Tools:****

**Tool3**

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
| ConeAngle :              | 1.1000000                                                                                                 |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| TrackType :              | 3                                                                                                         |
| Variables :              | [ 'CONEANGLE' , 'CONEMULT' , 'CONEPTASYM' ]                                                             |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |
