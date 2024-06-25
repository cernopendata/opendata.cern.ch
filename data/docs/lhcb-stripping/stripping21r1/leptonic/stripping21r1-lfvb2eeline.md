[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLFVB2eeLine

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/LFVB2eeLine/Particles |
| Postscale      | 1.0000000                  |
| HLT            | None                       |
| Prescale       | 1.0000000                  |
| L0DU           | None                       |
| ODIN           | None                       |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseElectrons](./stripping21r1-stdlooseelectrons) /Particles')\>0 |

**CombineParticles/LFVB2eeLine**

|                  |                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r1-stdlooseelectrons) ' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 )' , 'e-' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 )' } |
| CombinationCut   | (ADAMASS('B_s0')\<1200\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 1200\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 225)& (BPVIPCHI2()\< 25)               |
| DecayDescriptor  | None                                                                                                                           |
| DecayDescriptors | [ 'B_s0 -\> e+ e-' , '[B_s0 -\> e+ e+]cc' ]                                                                                |
| Output           | Phys/LFVB2eeLine/Particles                                                                                                     |

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

**AddRelatedInfo/RelatedInfo1_LFVB2eeLine**

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/LFVB2eeLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo1_LFVB2eeLine/Particles |

****Tools:****

**Tool1**

|                          |                                                                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AuditTools :             | False                                                                                                                                                                                    |
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                                                                                                    |
| clone_cut :              | -9999.0000                                                                                                                                                                               |
| PropertiesPrint :        | False                                                                                                                                                                                    |
| AuditStart :             | False                                                                                                                                                                                    |
| ips :                    | 3.0000000                                                                                                                                                                                |
| GammaCDecays :           | gamma -\> e+ e-                                                                                                                                                                          |
| TrackContainer :         | Rec/Track/Best                                                                                                                                                                           |
| trchi2_cut :             | 3.0000000                                                                                                                                                                                |
| TrackExtrapolator :      | TrackMasterExtrapolator:PUBLIC                                                                                                                                                           |
| ErrorsPrint :            | True                                                                                                                                                                                     |
| svdis_h :                | 30.000000                                                                                                                                                                                |
| StatEntityList :         | [ ]                                                                                                                                                                                    |
| MaxPrints :              | 2                                                                                                                                                                                        |
| angle :                  | 0.27000000                                                                                                                                                                               |
| DeltaPath :              | 0.0020000000                                                                                                                                                                             |
| PrintMyAlg :             | True                                                                                                                                                                                     |
| RootInTES :              | None                                                                                                                                                                                     |
| ParticlePath :           | /Event/Phys/StdAllNoPIDsPions/Particles                                                                                                                                                  |
| AuditFinalize :          | False                                                                                                                                                                                    |
| pvdis :                  | 0.50000000                                                                                                                                                                               |
| IsoTwoBody :             | False                                                                                                                                                                                    |
| ContextService :         | AlgContextSvc                                                                                                                                                                            |
| DeltaChi2 :              | 0.050000000                                                                                                                                                                              |
| svdis :                  | -0.15000000                                                                                                                                                                              |
| Transporter :            | ParticleTransporter:PUBLIC                                                                                                                                                               |
| MonitorService :         | MonitorSvc                                                                                                                                                                               |
| AuditInitialize :        | False                                                                                                                                                                                    |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \|                                                                                |
| OutputLevel :            | 3                                                                                                                                                                                        |
| StatPrint :              | True                                                                                                                                                                                     |
| TypePrint :              | True                                                                                                                                                                                     |
| makeTrackCuts :          | False                                                                                                                                                                                    |
| fc :                     | 0.60000000                                                                                                                                                                               |
| AuditStop :              | False                                                                                                                                                                                    |
| Context :                | None                                                                                                                                                                                     |
| ghost_cut :              | 0.30000000                                                                                                                                                                               |
| RootOnTES :              | None                                                                                                                                                                                     |
| GlobalTimeOffset :       | 0.0000000                                                                                                                                                                                |
| MaxIterations :          | 10                                                                                                                                                                                       |
| doca_iso :               | 0.13000000                                                                                                                                                                               |
| Variables :              | [ 'BSMUMUCDFISO' , 'BSMUMUOTHERBMAG' , 'BSMUMUOTHERBANGLE' , 'BSMUMUOTHERBBOOSTMAG' , 'BSMUMUOTHERBBOOSTANGLE' , 'BSMUMUTRACKPLUSISO' , 'BSMUMUTRACKMINUSISO' , 'BSMUMUOTHERBTRACKS' ] |
| DiGammaDecays :          | [ ( pi0 -\> ) , ( eta -\> ) , ]                                                                                                                                                        |
| UseEfficiencyRowFormat : | True                                                                                                                                                                                     |
| PVInputLocation :        | Rec/Vertex/Primary                                                                                                                                                                       |
| ToleranceInZ :           | 0.0020000000                                                                                                                                                                             |
| pvdis_h :                | 40.000000                                                                                                                                                                                |
| StateProvider :          | TrackStateProvider:PUBLIC                                                                                                                                                                |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|                                                                                  |
| tracktype :              | 3                                                                                                                                                                                        |
| CounterList :            | [ '.\*' ]                                                                                                                                                                              |
