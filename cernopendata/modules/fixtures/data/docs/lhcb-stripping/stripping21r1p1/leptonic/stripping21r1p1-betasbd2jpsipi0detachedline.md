[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingBetaSBd2JpsiPi0DetachedLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/BetaSBd2JpsiPi0DetachedLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles**

|      |                                                                                                                   |
|------|-------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21r1p1-stdmassconstrainedjpsi2mumu) /Particles',True)\>0 |

**FilterDesktop/BetaSNarrowJpsiForBetaSPi0**

|                 |                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('J/psi(1S)')) \< 80 \* MeV) & (BPVLTIME() \> 0.2 \*ps)                       |
| Inputs          | [ 'Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21r1p1-stdmassconstrainedjpsi2mumu) ' ] |
| DecayDescriptor | None                                                                                        |
| Output          | Phys/BetaSNarrowJpsiForBetaSPi0/Particles                                                   |

**LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseResolvedPi0](./stripping21r1p1-stdlooseresolvedpi0) /Particles',True)\>0 |

**FilterDesktop/BetaSResolvedPi0ForBetaS**

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT \> 1000.\*MeV) & (MINTREE('gamma'==ABSID, CL) \> 0.05 )                 |
| Inputs          | [ 'Phys/ [StdLooseResolvedPi0](./stripping21r1p1-stdlooseresolvedpi0) ' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/BetaSResolvedPi0ForBetaS/Particles                                     |

**CombineParticles/BetaSBd2JpsiPi0R**

|                  |                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSNarrowJpsiForBetaSPi0' , 'Phys/BetaSResolvedPi0ForBetaS' ]                                   |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi0' : 'ALL' }                                                        |
| CombinationCut   | in_range(4500,AM,6000)                                                                                      |
| MotherCut        | in_range(4700,M,5900) & (VFASPF(VCHI2PDOF) \< 10) & (BPVDIRA\>0.99755) & (BPVIP()\<0.2) & (BPVIPCHI2()\<20) |
| DecayDescriptor  | B0 -\> J/psi(1S) pi0                                                                                        |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) pi0' ]                                                                                |
| Output           | Phys/BetaSBd2JpsiPi0R/Particles                                                                             |

**FilterDesktop/BetaSBd2JpsiPi0DetachedLine**

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/BetaSMvaBd2JpsiPi0')\>-0.4 |
| Inputs          | [ 'Phys/BetaSBd2JpsiPi0R' ]                             |
| DecayDescriptor | None                                                      |
| Output          | Phys/BetaSBd2JpsiPi0DetachedLine/Particles                |

****Tools:****

**BetaSMvaBd2JpsiPi0**

|                          |                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| StatTableHeader :        | \| Counter \| \# \| sum \| mean/eff^\* \| rms/err^\* \| min \| max \|                                                                                                                                                                                                                                                                            |
| Factory :                | LoKi::Hybrid::Tool/HybridFactory:PUBLIC                                                                                                                                                                                                                                                                                                          |
| Source :                 | LoKi::Hybrid::DictOfFunctors/MVAdict                                                                                                                                                                                                                                                                                                             |
| Preambulo :              | [ ]                                                                                                                                                                                                                                                                                                                                            |
| ErrorsPrint :            | True                                                                                                                                                                                                                                                                                                                                             |
| StatEntityList :         | [ ]                                                                                                                                                                                                                                                                                                                                            |
| RootInTES :              | None                                                                                                                                                                                                                                                                                                                                             |
| AuditFinalize :          | False                                                                                                                                                                                                                                                                                                                                            |
| Key :                    | BDT                                                                                                                                                                                                                                                                                                                                              |
| TypePrint :              | True                                                                                                                                                                                                                                                                                                                                             |
| UseEfficiencyRowFormat : | True                                                                                                                                                                                                                                                                                                                                             |
| ContextService :         | AlgContextSvc                                                                                                                                                                                                                                                                                                                                    |
| AuditTools :             | False                                                                                                                                                                                                                                                                                                                                            |
| MonitorService :         | MonitorSvc                                                                                                                                                                                                                                                                                                                                       |
| AuditInitialize :        | False                                                                                                                                                                                                                                                                                                                                            |
| RegularRowFormat :       | \| %\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.7g\| \|%\|#11.5g\| \|%\|#11.5g\| \|%\|#12.5g\| \|%\|#12.5g\| \|                                                                                                                                                                                                                                        |
| OutputLevel :            | 3                                                                                                                                                                                                                                                                                                                                                |
| StatPrint :              | True                                                                                                                                                                                                                                                                                                                                             |
| AuditStop :              | False                                                                                                                                                                                                                                                                                                                                            |
| Context :                | None                                                                                                                                                                                                                                                                                                                                             |
| PropertiesPrint :        | False                                                                                                                                                                                                                                                                                                                                            |
| GlobalTimeOffset :       | 0.0000000                                                                                                                                                                                                                                                                                                                                        |
| Options :                | { 'KeepVars' : '0' , 'Name' : 'BDT' , 'XMLFile' : '/afs/cern.ch/lhcb/software/releases/PARAM/TMVAWeights/v1r7/data/B2JpsiPi0_Fisher_v1r2.xml' }                                                                                                                                                                                                  |
| Variables :              | { '-log(J_psi_1S_IP_OWNPV)' : '-log(CHILD(MIPDV(PRIMARY),1))' , 'log(1/(1-fabs(B0_DIRA_OWNPV))-400)' : 'log(1/(1-abs( CHILD(BPVDIRA,0) ))-400)' , 'log(1/B0_IP_OWNPV-5)' : 'log(1/(CHILD(MIPDV(PRIMARY),0)) - 5)' , 'log(J_psi_1S_PT\*1e-3)' : 'log( CHILD(PT,1) \*1e-3)' , 'log(pow(pi0_PT\*1e-3,5)-1)' : 'log(pow( CHILD(PT,2) \*1e-3,5)-1)' } |
| AuditStart :             | False                                                                                                                                                                                                                                                                                                                                            |
| EfficiencyRowFormat :    | \|\*%\|-48.48s\|%\|50t\|\|%\|10d\| \|%\|11.5g\| \|(%\|#9.6g\| +- %\|-#9.6g\|)%%\| ------- \| ------- \|                                                                                                                                                                                                                                          |
| CounterList :            | [ '.\*' ]                                                                                                                                                                                                                                                                                                                                      |
