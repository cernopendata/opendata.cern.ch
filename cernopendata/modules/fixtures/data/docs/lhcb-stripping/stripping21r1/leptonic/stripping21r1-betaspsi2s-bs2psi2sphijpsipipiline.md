[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSPsi2S_Bs2Psi2SPhiJpsiPiPiLine

## Properties:

|                |                                                   |
|----------------|---------------------------------------------------|
| OutputLocation | Phys/BetaSPsi2S_Bs2Psi2SPhiJpsiPiPiLine/Particles |
| Postscale      | 1.0000000                                         |
| HLT            | None                                              |
| Prescale       | 1.0000000                                         |
| L0DU           | None                                              |
| ODIN           | None                                              |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdMassConstrainedJpsi2MuMu_Particles**

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21r1-stdmassconstrainedjpsi2mumu) /Particles')\>0 |

**FilterDesktop/BetaSPsi2S_JpsiForPsi2SJpsiPiPi**

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                       |
| Inputs          | [ 'Phys/ [StdMassConstrainedJpsi2MuMu](./stripping21r1-stdmassconstrainedjpsi2mumu) ' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/BetaSPsi2S_JpsiForPsi2SJpsiPiPi/Particles                                            |

**LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdAllLoosePions](./stripping21r1-stdallloosepions) /Particles')\>0 |

**FilterDesktop/BetaSPsi2S_PionsForPsi2SJpsiPiPi**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5)                                                    |
| Inputs          | [ 'Phys/ [StdAllLoosePions](./stripping21r1-stdallloosepions) ' ] |
| DecayDescriptor | None                                                                |
| Output          | Phys/BetaSPsi2S_PionsForPsi2SJpsiPiPi/Particles                     |

**CombineParticles/BetaSPsi2S_Psi2SJpsiPiPi**

|                  |                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSPsi2S_JpsiForPsi2SJpsiPiPi' , 'Phys/BetaSPsi2S_PionsForPsi2SJpsiPiPi' ]                       |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'pi+' : 'MIPCHI2DV(PRIMARY) \> 9' , 'pi-' : 'MIPCHI2DV(PRIMARY) \> 9' } |
| CombinationCut   | (AM23\>400\*MeV) & (AM23\<800\*MeV)&(APT\>500\*MeV) & (ADAMASS('psi(2S)') \< 30\*MeV)                        |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 16) & (MINTREE('pi-'==ABSID, PIDK) \< 10) & (MINTREE('pi+'==ABSID, PIDK) \< 10)       |
| DecayDescriptor  | psi(2S) -\> J/psi(1S) pi+ pi-                                                                                |
| DecayDescriptors | [ 'psi(2S) -\> J/psi(1S) pi+ pi-' ]                                                                        |
| Output           | Phys/BetaSPsi2S_Psi2SJpsiPiPi/Particles                                                                      |

**LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLoosePhi2KK](./stripping21r1-stdloosephi2kk) /Particles')\>0 |

**FilterDesktop/BetaSPsi2S_PhiForPsi2SJpsiPiPi**

|                 |                                                                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('phi(1020)') \< 20) & (PT \> 1000 \*MeV) & (VFASPF(VCHI2) \< 25) & (MAXTREE('K+'==ABSID, TRCHI2DOF) \< 5) & (MINTREE('K+'==ABSID, PIDK) \> -2) |
| Inputs          | [ 'Phys/ [StdLoosePhi2KK](./stripping21r1-stdloosephi2kk) ' ]                                                                                        |
| DecayDescriptor | None                                                                                                                                                   |
| Output          | Phys/BetaSPsi2S_PhiForPsi2SJpsiPiPi/Particles                                                                                                          |

**CombineParticles/BetaSPsi2S_Bs2Psi2SPhiJpsiPiPiLine**

|                  |                                                                               |
|------------------|-------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSPsi2S_PhiForPsi2SJpsiPiPi' , 'Phys/BetaSPsi2S_Psi2SJpsiPiPi' ] |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : 'ALL' , 'psi(2S)' : 'ALL' }                      |
| CombinationCut   | in_range(5000,AM,5650)                                                        |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF)\<20) & (BPVLTIME()\> 0.15\*ps)     |
| DecayDescriptor  | B_s0 -\> psi(2S) phi(1020)                                                    |
| DecayDescriptors | [ 'B_s0 -\> psi(2S) phi(1020)' ]                                            |
| Output           | Phys/BetaSPsi2S_Bs2Psi2SPhiJpsiPiPiLine/Particles                             |
