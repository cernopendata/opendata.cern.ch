[[stripping21r1 lines]](./stripping21r1-index)

# StrippingK0s2Pi0MuMuSignalLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/K0s2Pi0MuMuSignalLine/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

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

**CombineParticles/K0s2Pi0MuMuPseudoJPsi**

|                  |                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdAllLooseMuons](./stripping21r1-stdallloosemuons) ' ]                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 36 )&(TRCHI2DOF \< 5 )' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 36 )&(TRCHI2DOF \< 5 )' } |
| CombinationCut   | (AMAXDOCA('')\<0.3\*mm)                                                                                                          |
| MotherCut        | ALL                                                                                                                              |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                            |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                    |
| Output           | Phys/K0s2Pi0MuMuPseudoJPsi/Particles                                                                                             |

**LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles**

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseResolvedPi0](./stripping21r1-stdlooseresolvedpi0) /Particles')\>0 |

**CombineParticles/K0s2Pi0MuMuSignalLine**

|                  |                                                                                                                                   |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K0s2Pi0MuMuPseudoJPsi' , 'Phys/ [StdLooseResolvedPi0](./stripping21r1-stdlooseresolvedpi0) ' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi0' : 'ALL' }                                                                              |
| CombinationCut   | (AM \> 300 \* MeV)& (AM \< 600 \* MeV)                                                                                            |
| MotherCut        | ((BPVDIRA\> 0 ) & ((BPVVDSIGN\*M/P) \> 5.3718\*2.9979e-01) & (MIPDV(PRIMARY)\<0.9\*mm) & (M\> 300 \* MeV) & ( (M\< 600 \* MeV) )) |
| DecayDescriptor  | KS0 -\> pi0 J/psi(1S)                                                                                                             |
| DecayDescriptors | [ 'KS0 -\> pi0 J/psi(1S)' ]                                                                                                     |
| Output           | Phys/K0s2Pi0MuMuSignalLine/Particles                                                                                              |

****Tools:****

**OfflineVertexFitter**

|                          |                                                                                                           |
|--------------------------|-----------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                     |
| maxDeltaChi2 :           | 0.0010000000                                                                                              |
| applyMomMassConstraint : | False                                                                                                     |
| PropertiesPrint :        | False                                                                                                     |
| applyDauMassConstraint : | False                                                                                                     |
| AuditStart :             | False                                                                                                     |
| useResonanceVertex :     | False                                                                                                     |
| maxIter :                | 10                                                                                                        |
| includeDauVertexChi2 :   | True                                                                                                      |
| StatEntityList :         | [ ]                                                                                                     |
| RootOnTES :              | None                                                                                                      |
| PrintMyAlg :             | True                                                                                                      |
| RootInTES :              | None                                                                                                      |
| AuditFinalize :          | False                                                                                                     |
| TypePrint :              | True                                                                                                      |
| Transporter :            | ParticleTransporter:PUBLIC                                                                                |
| widthThreshold :         | 2.0000000                                                                                                 |
| ContextService :         | AlgContextSvc                                                                                             |
| AuditTools :             | False                                                                                                     |
| MonitorService :         | MonitorSvc                                                                                                |
| AuditInitialize :        | False                                                                                                     |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \| |
| OutputLevel :            | 3                                                                                                         |
| StatPrint :              | True                                                                                                      |
| AuditStop :              | False                                                                                                     |
| Context :                | None                                                                                                      |
| ErrorsPrint :            | True                                                                                                      |
| GlobalTimeOffset :       | 0.0000000                                                                                                 |
| maxDeltaZ :              | 1.0000000                                                                                                 |
| UseEfficiencyRowFormat : | True                                                                                                      |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|   |
| CounterList :            | [ '.\*' ]                                                                                               |
