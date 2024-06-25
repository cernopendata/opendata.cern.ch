[[stripping21r0p1 lines]](./stripping21r0p1-index)

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

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles

|      |                                                                                                                                 |
|------|---------------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r0p1-commonparticles-stdmassconstrainedjpsi2mumu)/Particles',True)\>0 |

FilterDesktop/BetaSNarrowJpsiForBetaSPi0

|                 |                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Code            | (PFUNA(ADAMASS('J/psi(1S)')) \< 80 \* MeV) & (BPVLTIME() \> 0.2 \*ps)                                     |
| Inputs          | [ 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r0p1-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DecayDescriptor | None                                                                                                      |
| Output          | Phys/BetaSNarrowJpsiForBetaSPi0/Particles                                                                 |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)/Particles',True)\>0 |

FilterDesktop/BetaSResolvedPi0ForBetaS

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000.\*MeV) & (MINTREE('gamma'==ABSID, CL) \> 0.05 )                               |
| Inputs          | [ 'Phys/[StdLooseResolvedPi0](./stripping21r0p1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/BetaSResolvedPi0ForBetaS/Particles                                                   |

CombineParticles/BetaSBd2JpsiPi0R

|                  |                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSNarrowJpsiForBetaSPi0' , 'Phys/BetaSResolvedPi0ForBetaS' ]                                   |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi0' : 'ALL' }                                                        |
| CombinationCut   | in_range(4500,AM,6000)                                                                                      |
| MotherCut        | in_range(4700,M,5900) & (VFASPF(VCHI2PDOF) \< 10) & (BPVDIRA\>0.99755) & (BPVIP()\<0.2) & (BPVIPCHI2()\<20) |
| DecayDescriptor  | B0 -\> J/psi(1S) pi0                                                                                        |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) pi0' ]                                                                                |
| Output           | Phys/BetaSBd2JpsiPi0R/Particles                                                                             |

FilterDesktop/BetaSBd2JpsiPi0DetachedLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/BetaSMvaBd2JpsiPi0')\>-0.4 |
| Inputs          | [ 'Phys/BetaSBd2JpsiPi0R' ]                             |
| DecayDescriptor | None                                                      |
| Output          | Phys/BetaSBd2JpsiPi0DetachedLine/Particles                |
