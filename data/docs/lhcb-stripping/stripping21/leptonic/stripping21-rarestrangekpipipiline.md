[[stripping21 lines]](./stripping21-index)

# StrippingRareStrangeKPiPiPiLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/RareStrangeKPiPiPiLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 0.010000000                           |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLoosePions](./stripping21-stdallloosepions) /Particles')\>0 |

**CombineParticles/RareStrangeKPiPiPiLine**

|                  |                                                                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLoosePions](./stripping21-stdallloosepions) ' ]                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(P\>1000) & (TRCHI2DOF\<3.0) & (TRGHOSTPROB \< 0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'pi-' : '(P\>1000) & (TRCHI2DOF\<3.0) & (TRGHOSTPROB \< 0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' } |
| CombinationCut   | (ADAMASS('K+') \< 100.0 \*MeV) & (AMAXDOCA('')\< 3.0 \*mm)                                                                                                                                             |
| MotherCut        | (PT\> 100.0) & (ADMASS('K+') \< 100.0 \*MeV) & (BPVDIRA \> 0.98)& (VFASPF(VCHI2) \< 25.0) & (BPVVDCHI2 \> 36.0) & (BPVIPCHI2()\< 25.0 )                                                                |
| DecayDescriptor  | [K+ -\> pi+ pi+ pi-]cc                                                                                                                                                                               |
| DecayDescriptors | [ '[K+ -\> pi+ pi+ pi-]cc' ]                                                                                                                                                                       |
| Output           | Phys/RareStrangeKPiPiPiLine/Particles                                                                                                                                                                  |

**AddRelatedInfo/RelatedInfo1_RareStrangeKPiPiPiLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_RareStrangeKPiPiPiLine/Particles |

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

**AddRelatedInfo/RelatedInfo2_RareStrangeKPiPiPiLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_RareStrangeKPiPiPiLine/Particles |

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

**AddRelatedInfo/RelatedInfo3_RareStrangeKPiPiPiLine**

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeKPiPiPiLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_RareStrangeKPiPiPiLine/Particles |

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
