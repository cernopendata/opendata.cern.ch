[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSPsi2SMuMu_Bu2Psi2SKMuMuPrescaledLine

## Properties:

|                |                                                          |
|----------------|----------------------------------------------------------|
| OutputLocation | Phys/BetaSPsi2SMuMu_Bu2Psi2SKMuMuPrescaledLine/Particles |
| Postscale      | 1.0000000                                                |
| HLT            | None                                                     |
| Prescale       | 0.10000000                                               |
| L0DU           | None                                                     |
| ODIN           | None                                                     |

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

**CombineParticles/BetaSPsi2SMuMu_Psi2SToMuMu**

|                  |                                                                     |
|------------------|---------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'PIDmu \> 0.0' , 'mu-' : 'PIDmu\>0.0' }      |
| CombinationCut   | (ADAMASS('psi(2S)')\<60.0\*MeV) & (ADOCACHI2CUT( 30.0 ,''))         |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 16) & (MFIT)                                 |
| DecayDescriptor  | psi(2S) -\> mu+ mu-                                                 |
| DecayDescriptors | [ 'psi(2S) -\> mu+ mu-' ]                                         |
| Output           | Phys/BetaSPsi2SMuMu_Psi2SToMuMu/Particles                           |

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

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseKaons](./stripping21r1-stdallloosekaons) /Particles')\>0 |

**FilterDesktop/BetaSPsi2SMuMu_ChKForPsi2SToMuMu**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (PIDK \> 0)                                      |
| Inputs          | [ 'Phys/ [StdAllLooseKaons](./stripping21r1-stdallloosekaons) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/BetaSPsi2SMuMu_ChKForPsi2SToMuMu/Particles                     |

**CombineParticles/BetaSPsi2SMuMu_Bu2Psi2SKMuMuPrescaledLine**

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSPsi2SMuMu_ChKForPsi2SToMuMu' , 'Phys/BetaSPsi2SMuMu_Psi2SToMuMu' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 500)' , 'K-' : '(PT \> 500)' , 'psi(2S)' : 'ALL' }  |
| CombinationCut   | in_range(5000,AM,5650)                                                            |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF)\<20)                                   |
| DecayDescriptor  | [B+ -\> psi(2S) K+]cc                                                           |
| DecayDescriptors | [ '[B+ -\> psi(2S) K+]cc' ]                                                   |
| Output           | Phys/BetaSPsi2SMuMu_Bu2Psi2SKMuMuPrescaledLine/Particles                          |
