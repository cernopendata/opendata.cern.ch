[[stripping21 lines]](./stripping21-index)

# StrippingK0s2MuMuNoMuIDLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/K0s2MuMuNoMuIDLine/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 0.0010000000                      |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsPions](./stripping21-stdnopidspions) /Particles')\>0 |

**CombineParticles/K0s2MuMuNoMuIDLine**

|                  |                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdNoPIDsPions](./stripping21-stdnopidspions) ' ]                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY)\> 100.)&(TRCHI2DOF \< 5 ) & (PT \>0 \* MeV )' , 'pi-' : '(MIPCHI2DV(PRIMARY)\> 100.)&(TRCHI2DOF \< 5 ) & (PT \>0 \* MeV )' } |
| CombinationCut   | (ADAMASS('KS0')\<100\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                                                      |
| MotherCut        | ((BPVDIRA\>0) & ((BPVVDSIGN\*M/P) \> 0.1\*89.53\*2.9979e-01) & (MIPDV(PRIMARY)\<0.4\*mm) & (M\>400) & (M\<600) & (PT \> 0 \* MeV))                                       |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                                                          |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                                                                  |
| Output           | Phys/K0s2MuMuNoMuIDLine/Particles                                                                                                                                        |

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
