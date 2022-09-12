[[stripping21r1 lines]](./stripping21r1-index)

# StrippingH24MuLinesDetachedLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/H24MuLinesDetachedLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) /Particles')\>0 |

**CombineParticles/SelA1H24MuLinesDetached**

|                  |                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ]                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 3 ) & (PT \> 150 \* MeV ) & ( TRGHOSTPROB \< 0.4 ) & (MIPCHI2DV(PRIMARY)\> 1 )' , 'mu-' : '(TRCHI2DOF \< 3 ) & (PT \> 150 \* MeV ) & ( TRGHOSTPROB \< 0.4 ) & (MIPCHI2DV(PRIMARY)\> 1 )' } |
| CombinationCut   | (AM \< 2000 \* MeV ) & (AMAXDOCA('')\<0.3 \* mm)                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2)\< 10 ) & (MM \< 2000 \* MeV)& (BPVDIRA \> 0 )& (BPVIPCHI2() \< 36 )& (BPVVDCHI2 \> 4 )                                                                                                                            |
| DecayDescriptor  | KS0 -\> mu+ mu-                                                                                                                                                                                                                  |
| DecayDescriptors | [ 'KS0 -\> mu+ mu-' ]                                                                                                                                                                                                          |
| Output           | Phys/SelA1H24MuLinesDetached/Particles                                                                                                                                                                                           |

**CombineParticles/H24MuLinesDetachedLine**

|                  |                                              |
|------------------|----------------------------------------------|
| Inputs           | [ 'Phys/SelA1H24MuLinesDetached' ]         |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }               |
| CombinationCut   | (AMAXDOCA('')\< 1 \* mm )                    |
| MotherCut        | (PT \> 1000 \* MeV ) & (VFASPF(VCHI2)\< 15 ) |
| DecayDescriptor  | H_10 -\> KS0 KS0                             |
| DecayDescriptors | [ 'H_10 -\> KS0 KS0' ]                     |
| Output           | Phys/H24MuLinesDetachedLine/Particles        |

**AddExtraInfo/ExtraInfo_StrippingH24MuLinesDetachedLine**

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/SelA1H24MuLinesDetached' ]                                                                  |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/ExtraInfo_StrippingH24MuLinesDetachedLine/Particles                                              |
| Tools           | [ 'ConeVariables/Tool1' , 'ConeVariables/Tool2' , 'ConeVariables/Tool3' , 'VertexIsolation/Tool4' ] |

****Tools:****

**Tool4**

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
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |

**Tool3**

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| ConeAngle :              | 2.0000000                                                                                                 |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| TrackType :              | 3                                                                                                         |
| Variables :              | [ 'angle' , 'mult' , 'p' , 'pt' , 'ptasy' , 'pasy' ]                                                    |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ConeNumber :             | 3                                                                                                         |
| CounterList :            | [ '.\*' ]                                                                                               |

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| ConeAngle :              | 1.5000000                                                                                                 |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| TrackType :              | 3                                                                                                         |
| Variables :              | [ 'angle' , 'mult' , 'p' , 'pt' , 'ptasy' , 'pasy' ]                                                    |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ConeNumber :             | 2                                                                                                         |
| CounterList :            | [ '.\*' ]                                                                                               |

**Tool1**

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
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| ConeAngle :              | 1.0000000                                                                                                 |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| PropertiesPrint :        | False                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| TrackType :              | 3                                                                                                         |
| Variables :              | [ 'angle' , 'mult' , 'p' , 'pt' , 'ptasy' , 'pasy' ]                                                    |
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| ConeNumber :             | 1                                                                                                         |
| CounterList :            | [ '.\*' ]                                                                                               |
