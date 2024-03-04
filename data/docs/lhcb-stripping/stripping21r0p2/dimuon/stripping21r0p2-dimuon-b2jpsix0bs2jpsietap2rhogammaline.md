[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2JpsiX0Bs2JpsiEtap2RhoGammaLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/B2JpsiX0Bs2JpsiEtap2RhoGammaLine/Particles |
| Postscale      | 1.0000000                                       |
| HLT1           | None                                            |
| HLT2           | None                                            |
| Prescale       | 1.0000000                                       |
| L0DU           | None                                            |
| ODIN           | None                                            |

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

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

CombineParticles/Rho2PiPiB2JpsiX0

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                |
| CombinationCut   | (AM\>600\*MeV) & (AM\<900\*MeV) & (ADOCACHI2CUT(15, ''))                      |
| MotherCut        | (BPVVDZ\>0) & (VFASPF(VCHI2)\<9) & (BPVDIRA\>0.95) & (BPVVDCHI2\>25)          |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                                                         |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                 |
| Output           | Phys/Rho2PiPiB2JpsiX0/Particles                                               |

LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseAllPhotons/Particles',True) |

CombineParticles/Etap2RhoGammaB2JpsiX0

|                  |                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Rho2PiPiB2JpsiX0' , 'Phys/[StdLooseAllPhotons](./stripping21r0p2-commonparticles-stdlooseallphotons)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : '(CL\>0.05)' , 'rho(770)0' : 'ALL' }                                                     |
| CombinationCut   | (ADAMASS('eta_prime')\<100\*MeV) & (APT\>1500\*MeV)                                                               |
| MotherCut        | ALL                                                                                                               |
| DecayDescriptor  | eta_prime -\> rho(770)0 gamma                                                                                     |
| DecayDescriptors | [ 'eta_prime -\> rho(770)0 gamma' ]                                                                             |
| Output           | Phys/Etap2RhoGammaB2JpsiX0/Particles                                                                              |

CombineParticles/B2JpsiX0Bs2JpsiEtap2RhoGammaLine

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedJpsiB2JpsiX0' , 'Phys/Etap2RhoGammaB2JpsiX0' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'eta_prime' : 'ALL' }                                |
| CombinationCut   | in_range(4500,AM,6500)                                                                    |
| MotherCut        | (BPVDIRA \> 0.9995) & (BPVIP() \< 0.2) & (BPVIPCHI2() \< 20) & (VFASPF(VCHI2PDOF) \< 10 ) |
| DecayDescriptor  | B_s0 -\> J/psi(1S) eta_prime                                                              |
| DecayDescriptors | [ 'B_s0 -\> J/psi(1S) eta_prime' ]                                                      |
| Output           | Phys/B2JpsiX0Bs2JpsiEtap2RhoGammaLine/Particles                                           |
