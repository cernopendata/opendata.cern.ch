[[stripping21r1 lines]](./stripping21r1-index)

# StrippingRareStrangeKPiPiPiMassMeasLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/RareStrangeKPiPiPiMassMeasLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT            | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLoosePions](./stripping21r1-stdallloosepions) /Particles')\>0 |

**CombineParticles/RareStrangeKPiPiPiMassMeasLine**

|                  |                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLoosePions](./stripping21r1-stdallloosepions) ' ]                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(P\>1000) & (MIPCHI2DV(PRIMARY) \> 25.0) & (TRCHI2DOF\<5) & (TRGHOSTPROB \< 0.3)' , 'pi-' : '(P\>1000) & (MIPCHI2DV(PRIMARY) \> 25.0) & (TRCHI2DOF\<5) & (TRGHOSTPROB \< 0.3)' } |
| CombinationCut   | (ADAMASS('K+') \< 50.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                                                |
| MotherCut        | (PT\> 300.0) & (ADMASS('K+') \< 50.0 \*MeV) & (BPVDIRA \> 0.9998)& (VFASPF(VCHI2) \< 10.0) & (BPVVDCHI2 \> 100.0) & (BPVIPCHI2()\< 25.0 )                                                                |
| DecayDescriptor  | [K+ -\> pi+ pi+ pi-]cc                                                                                                                                                                                 |
| DecayDescriptors | [ '[K+ -\> pi+ pi+ pi-]cc' ]                                                                                                                                                                         |
| Output           | Phys/RareStrangeKPiPiPiMassMeasLine/Particles                                                                                                                                                            |

**AddRelatedInfo/RelatedInfo1_RareStrangeKPiPiPiMassMeasLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiMassMeasLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo1_RareStrangeKPiPiPiMassMeasLine/Particles |

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

**AddRelatedInfo/RelatedInfo2_RareStrangeKPiPiPiMassMeasLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiMassMeasLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo2_RareStrangeKPiPiPiMassMeasLine/Particles |

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

**AddRelatedInfo/RelatedInfo3_RareStrangeKPiPiPiMassMeasLine**

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiMassMeasLine' ]                |
| DecayDescriptor | None                                                       |
| Output          | Phys/RelatedInfo3_RareStrangeKPiPiPiMassMeasLine/Particles |

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
