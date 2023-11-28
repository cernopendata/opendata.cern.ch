[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2JpsiX0Bu2JpsiKLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/B2JpsiX0Bu2JpsiKLine/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 0.10000000                          |
| L0DU           | None                                |
| ODIN           | None                                |

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

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

CombineParticles/B2JpsiX0Bu2JpsiKLine

|                  |                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedJpsiB2JpsiX0' , 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                          |
| CombinationCut   | in_range(5100,AM,5500)                                                                                      |
| MotherCut        | (BPVDIRA \> 0.9995) & (BPVIP() \< 0.2) & (BPVIPCHI2() \< 20) & (VFASPF(VCHI2PDOF) \< 10 )                   |
| DecayDescriptor  | [B+ -\> J/psi(1S) K+]cc                                                                                   |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) K+]cc' ]                                                                           |
| Output           | Phys/B2JpsiX0Bu2JpsiKLine/Particles                                                                         |
