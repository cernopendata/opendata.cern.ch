[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingMicroDiJetsLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/MicroDiJetsLine/Particles |
| Postscale      | 1.0000000                      |
| HLT1           | None                           |
| HLT2           | None                           |
| Prescale       | 0.50000000                     |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**CheckPV/checkPVmin0**

|        |     |
|--------|-----|
| MinPVs | 0   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_MDSTJets_Particles**

|      |                                             |
|------|---------------------------------------------|
| Code | CONTAINS('Phys/MDSTJets/Particles',True)\>0 |

**CombineParticles/MicroDiJetsLine**

|                  |                                                   |
|------------------|---------------------------------------------------|
| Inputs           | [ 'Phys/MDSTJets' ]                             |
| DaughtersCuts    | { '' : 'ALL' , 'CELLjet' : ' (PT \> 20000.0 ) ' } |
| CombinationCut   | AALLSAMEBPV                                       |
| MotherCut        | ALL                                               |
| DecayDescriptor  | H_10 -\> CELLjet CELLjet                          |
| DecayDescriptors | [ 'H_10 -\> CELLjet CELLjet' ]                  |
| Output           | Phys/MicroDiJetsLine/Particles                    |

****Tools:****

**MomentumCombiner**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| Transporter :            | None                                                                                                      |
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| ErrorsPrint :            | True                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
| PrintMyAlg :             | True                                                                                                      |
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
| AuditStart :             | False                                                                                                     |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |
