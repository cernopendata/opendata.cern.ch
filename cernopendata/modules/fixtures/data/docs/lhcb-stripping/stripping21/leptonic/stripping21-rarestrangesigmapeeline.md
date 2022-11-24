[[stripping21 lines]](./stripping21-index)

# StrippingRareStrangeSigmaPEELine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaPEELine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseElectrons_Particles**

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseElectrons](./stripping21-stdalllooseelectrons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) /Particles')\>0 |

**CombineParticles/RareStrangeSigmaPEELine**

|                  |                                                                                                                                                                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseElectrons](./stripping21-stdalllooseelectrons) ' , 'Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) ' ]                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PIDe \> 2.0 ) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'e-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PIDe \> 2.0 ) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'p+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PIDp \> 5.0)' , 'p\~-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PIDp \> 5.0)' } |
| CombinationCut   | (ADAMASS('Sigma+')\<500.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                                                                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 36.0) & (PT\> 500.0 \*MeV)& (ADMASS('Sigma+') \< 500.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 6.0 \* ps)                                                                                                                                                                                |
| DecayDescriptor  | [Sigma+ -\> p+ e+ e-]cc                                                                                                                                                                                                                                                                                                              |
| DecayDescriptors | [ '[Sigma+ -\> p+ e+ e-]cc' ]                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/RareStrangeSigmaPEELine/Particles                                                                                                                                                                                                                                                                                                 |

**AddRelatedInfo/RelatedInfo1_RareStrangeSigmaPEELine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPEELine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaPEELine/Particles |

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

**AddRelatedInfo/RelatedInfo2_RareStrangeSigmaPEELine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPEELine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaPEELine/Particles |

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

**AddRelatedInfo/RelatedInfo3_RareStrangeSigmaPEELine**

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPEELine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaPEELine/Particles |

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
