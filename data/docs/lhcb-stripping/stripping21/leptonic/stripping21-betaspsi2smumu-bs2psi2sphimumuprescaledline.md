[[stripping21 lines]](./stripping21-index)

# StrippingBetaSPsi2SMuMu_Bs2Psi2SPhiMuMuPrescaledLine

## Properties:

|                |                                                            |
|----------------|------------------------------------------------------------|
| OutputLocation | Phys/BetaSPsi2SMuMu_Bs2Psi2SPhiMuMuPrescaledLine/Particles |
| Postscale      | 1.0000000                                                  |
| HLT            | None                                                       |
| Prescale       | 0.50000000                                                 |
| L0DU           | None                                                       |
| ODIN           | None                                                       |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) /Particles')\>0 |

**CombineParticles/BetaSPsi2SMuMu_Psi2SToMuMu**

|                  |                                                                   |
|------------------|-------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21-stdallloosemuons) ' ] |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'PIDmu \> 0.0' , 'mu-' : 'PIDmu\>0.0' }    |
| CombinationCut   | (ADAMASS('psi(2S)')\<60.0\*MeV) & (ADOCACHI2CUT( 30.0 ,''))       |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 16) & (MFIT)                               |
| DecayDescriptor  | psi(2S) -\> mu+ mu-                                               |
| DecayDescriptors | [ 'psi(2S) -\> mu+ mu-' ]                                       |
| Output           | Phys/BetaSPsi2SMuMu_Psi2SToMuMu/Particles                         |

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

**LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePhi2KK](./stripping21-stdloosephi2kk) /Particles')\>0 |

**FilterDesktop/BetaSPsi2SMuMu_PhiForPsi2SToMuMu**

|                 |                                                                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('phi(1020)') \< 20) & (PT \> 1000 \*MeV) & (VFASPF(VCHI2) \< 25) & (MAXTREE('K+'==ABSID, TRCHI2DOF) \< 5) & (MINTREE('K+'==ABSID, PIDK) \> -2) |
| Inputs          | [ 'Phys/ [StdLoosePhi2KK](./stripping21-stdloosephi2kk) ' ]                                                                                          |
| DecayDescriptor | None                                                                                                                                                   |
| Output          | Phys/BetaSPsi2SMuMu_PhiForPsi2SToMuMu/Particles                                                                                                        |

**CombineParticles/BetaSPsi2SMuMu_Bs2Psi2SPhiMuMuPrescaledLine**

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSPsi2SMuMu_PhiForPsi2SToMuMu' , 'Phys/BetaSPsi2SMuMu_Psi2SToMuMu' ] |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : 'ALL' , 'psi(2S)' : 'ALL' }                          |
| CombinationCut   | in_range(5000,AM,5650)                                                            |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF)\<20)                                   |
| DecayDescriptor  | B_s0 -\> psi(2S) phi(1020)                                                        |
| DecayDescriptors | [ 'B_s0 -\> psi(2S) phi(1020)' ]                                                |
| Output           | Phys/BetaSPsi2SMuMu_Bs2Psi2SPhiMuMuPrescaledLine/Particles                        |
