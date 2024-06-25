[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2JpsiX0B02JpsiPi0RLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2JpsiX0B02JpsiPi0RLine/Particles |
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

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

CombineParticles/B02JpsiPi0RB2JpsiX0

|                  |                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedJpsiB2JpsiX0' , 'Phys/[StdLooseResolvedPi0](./stripping21r0p2-commonparticles-stdlooseresolvedpi0)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi0' : '(CHILD(CL,1) \> 0.05) & (CHILD(CL,2) \> 0.05) & (PT\>1500\*MeV)' }        |
| CombinationCut   | in_range(4500,AM,6500)                                                                                                  |
| MotherCut        | (BPVDIRA \> 0.9995) & (BPVIP() \< 0.2) & (BPVIPCHI2() \< 20) & (VFASPF(VCHI2PDOF) \< 10 )                               |
| DecayDescriptor  | B0 -\> J/psi(1S) pi0                                                                                                    |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) pi0' ]                                                                                            |
| Output           | Phys/B02JpsiPi0RB2JpsiX0/Particles                                                                                      |

FilterDesktop/B2JpsiX0B02JpsiPi0RLine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2JpsiX0MvaB02JpsiPi0R')\>-0.52 |
| Inputs          | [ 'Phys/B02JpsiPi0RB2JpsiX0' ]                               |
| DecayDescriptor | None                                                           |
| Output          | Phys/B2JpsiX0B02JpsiPi0RLine/Particles                         |
