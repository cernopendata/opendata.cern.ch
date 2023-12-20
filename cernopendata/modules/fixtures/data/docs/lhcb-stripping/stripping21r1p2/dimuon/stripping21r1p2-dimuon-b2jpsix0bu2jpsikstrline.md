[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2JpsiX0Bu2JpsiKstRLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2JpsiX0Bu2JpsiKstRLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionDimuon

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamDimuonBadEvent') & ~ALG_PASSED('StrippingStreamDimuonBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdMassConstrainedJpsi2MuMu

|      |                                               |
|------|-----------------------------------------------|
| Code | 0StdMassConstrainedJpsi2MuMu/Particles',True) |

FilterDesktop/DetachedJpsiB2JpsiX0

|                 |                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('J/psi(1S)')) \< 80 \* MeV) & (BPVLTIME() \> 0.2 \*ps)                                     |
| Inputs          | [ 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1p2-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DecayDescriptor | None                                                                                                      |
| Output          | Phys/DetachedJpsiB2JpsiX0/Particles                                                                       |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

CombineParticles/Kst2KPi0RB2JpsiX0

|                  |                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' , 'Phys/[StdLooseResolvedPi0](./stripping21r1p2-commonparticles-stdlooseresolvedpi0)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PROBNNk\>0.1)' , 'K-' : '(PROBNNk\>0.1)' , 'pi0' : '(CHILD(CL,1)\>0.05) & (CHILD(CL,2)\>0.05) & (PT\>800\*MeV)' }                           |
| CombinationCut   | (ADAMASS('K\*(892)+')\< 150\*MeV)                                                                                                                                   |
| MotherCut        | ALL                                                                                                                                                                 |
| DecayDescriptor  | [K\*(892)+ -\> K+ pi0]cc                                                                                                                                          |
| DecayDescriptors | [ '[K\*(892)+ -\> K+ pi0]cc' ]                                                                                                                                  |
| Output           | Phys/Kst2KPi0RB2JpsiX0/Particles                                                                                                                                    |

CombineParticles/Bu2JpsiKstRB2JpsiX0

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedJpsiB2JpsiX0' , 'Phys/Kst2KPi0RB2JpsiX0' ]                              |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' }          |
| CombinationCut   | in_range(4500,AM,6500)                                                                    |
| MotherCut        | (BPVDIRA \> 0.9995) & (BPVIP() \< 0.2) & (BPVIPCHI2() \< 20) & (VFASPF(VCHI2PDOF) \< 10 ) |
| DecayDescriptor  | [B+ -\> J/psi(1S) K\*(892)+]cc                                                          |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) K\*(892)+]cc' ]                                                  |
| Output           | Phys/Bu2JpsiKstRB2JpsiX0/Particles                                                        |

FilterDesktop/B2JpsiX0Bu2JpsiKstRLine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2JpsiX0MvaBu2JpsiKstR')\>-1.10 |
| Inputs          | [ 'Phys/Bu2JpsiKstRB2JpsiX0' ]                               |
| DecayDescriptor | None                                                           |
| Output          | Phys/B2JpsiX0Bu2JpsiKstRLine/Particles                         |
