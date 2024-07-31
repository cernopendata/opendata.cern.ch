[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSPsi2S_Bd2Psi2SKsJpsiPiPiLine

## Properties:

|                |                                                  |
|----------------|--------------------------------------------------|
| OutputLocation | Phys/BetaSPsi2S_Bd2Psi2SKsJpsiPiPiLine/Particles |
| Postscale      | 1.0000000                                        |
| HLT            | None                                             |
| Prescale       | 1.0000000                                        |
| L0DU           | None                                             |
| ODIN           | None                                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)/Particles')\>0 |

FilterDesktop/BetaSPsi2S_JpsiForPsi2SJpsiPiPi

|                 |                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                     |
| Inputs          | [ 'Phys/[StdMassConstrainedJpsi2MuMu](./stripping21r1-commonparticles-stdmassconstrainedjpsi2mumu)' ] |
| DecayDescriptor | None                                                                                                    |
| Output          | Phys/BetaSPsi2S_JpsiForPsi2SJpsiPiPi/Particles                                                          |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

FilterDesktop/BetaSPsi2S_PionsForPsi2SJpsiPiPi

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5)                                                                  |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/BetaSPsi2S_PionsForPsi2SJpsiPiPi/Particles                                   |

CombineParticles/BetaSPsi2S_Psi2SJpsiPiPi

|                  |                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSPsi2S_JpsiForPsi2SJpsiPiPi' , 'Phys/BetaSPsi2S_PionsForPsi2SJpsiPiPi' ]                       |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi+' : 'MIPCHI2DV(PRIMARY) \> 9' , 'pi-' : 'MIPCHI2DV(PRIMARY) \> 9' } |
| CombinationCut   | (AM23\>400\*MeV) & (AM23\<800\*MeV)&(APT\>500\*MeV) & (ADAMASS('psi(2S)') \< 30\*MeV)                        |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 16) & (MINTREE('pi-'==ABSID, PIDK) \< 10) & (MINTREE('pi+'==ABSID, PIDK) \< 10)       |
| DecayDescriptor  | psi(2S) -\> J/psi(1S) pi+ pi-                                                                                |
| DecayDescriptors | [ 'psi(2S) -\> J/psi(1S) pi+ pi-' ]                                                                        |
| Output           | Phys/BetaSPsi2S_Psi2SJpsiPiPi/Particles                                                                      |

GaudiSequencer/SeqBetaSPsi2S_KsLooseForPsi2SJpsiPiPi

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/BetaSPsi2S_KsLooseForPsi2SJpsiPiPi

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                             |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/BetaSPsi2S_KsLooseForPsi2SJpsiPiPi/Particles                                                                                               |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/BetaSPsi2S_KsForPsi2SJpsiPiPi

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | (VFASPF(VCHI2)\<20) & (BPVDLS\>5)               |
| Inputs          | [ 'Phys/BetaSPsi2S_KsLooseForPsi2SJpsiPiPi' ] |
| DecayDescriptor | None                                            |
| Output          | Phys/BetaSPsi2S_KsForPsi2SJpsiPiPi/Particles    |

CombineParticles/BetaSPsi2S_Bd2Psi2SKsJpsiPiPiLine

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSPsi2S_KsForPsi2SJpsiPiPi' , 'Phys/BetaSPsi2S_Psi2SJpsiPiPi' ] |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'psi(2S)' : 'ALL' }                           |
| CombinationCut   | in_range(5000,AM,5650)                                                       |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF)\<10)                              |
| DecayDescriptor  | B0 -\> psi(2S) KS0                                                           |
| DecayDescriptors | [ 'B0 -\> psi(2S) KS0' ]                                                   |
| Output           | Phys/BetaSPsi2S_Bd2Psi2SKsJpsiPiPiLine/Particles                             |
