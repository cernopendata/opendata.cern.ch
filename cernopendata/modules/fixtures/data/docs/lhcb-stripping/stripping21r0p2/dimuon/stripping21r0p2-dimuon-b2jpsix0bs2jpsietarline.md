[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2JpsiX0Bs2JpsiEtaRLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2JpsiX0Bs2JpsiEtaRLine/Particles |
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
| Inputs          | [ 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r0p2-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DecayDescriptor | None                                                                                                      |
| Output          | Phys/DetachedJpsiB2JpsiX0/Particles                                                                       |

LoKi::VoidFilter/SELECT:Phys/StdLooseEta2gg

|      |                                  |
|------|----------------------------------|
| Code | 0StdLooseEta2gg/Particles',True) |

CombineParticles/Bs2JpsiEtaRB2JpsiX0

|                  |                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedJpsiB2JpsiX0' , 'Phys/[StdLooseEta2gg](./stripping21r0p2-commonparticles-stdlooseeta2gg)' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'eta' : '(CHILD(CL,1) \> 0.05) & (CHILD(CL,2) \> 0.05) & (PT\>1500\*MeV) & in_range(475,M,625)' } |
| CombinationCut   | in_range(4500,AM,6500)                                                                                                                 |
| MotherCut        | (BPVDIRA \> 0.9995) & (BPVIP() \< 0.2) & (BPVIPCHI2() \< 20) & (VFASPF(VCHI2PDOF) \< 10 )                                              |
| DecayDescriptor  | B_s0 -\> J/psi(1S) eta                                                                                                                 |
| DecayDescriptors | [ 'B_s0 -\> J/psi(1S) eta' ]                                                                                                         |
| Output           | Phys/Bs2JpsiEtaRB2JpsiX0/Particles                                                                                                     |

FilterDesktop/B2JpsiX0Bs2JpsiEtaRLine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2JpsiX0MvaBs2JpsiEtaR')\>-0.69 |
| Inputs          | [ 'Phys/Bs2JpsiEtaRB2JpsiX0' ]                               |
| DecayDescriptor | None                                                           |
| Output          | Phys/B2JpsiX0Bs2JpsiEtaRLine/Particles                         |
