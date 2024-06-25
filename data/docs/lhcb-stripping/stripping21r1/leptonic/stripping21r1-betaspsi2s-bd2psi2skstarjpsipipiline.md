[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBetaSPsi2S_Bd2Psi2SKstarJpsiPiPiLine

## Properties:

|                |                                                     |
|----------------|-----------------------------------------------------|
| OutputLocation | Phys/BetaSPsi2S_Bd2Psi2SKstarJpsiPiPiLine/Particles |
| Postscale      | 1.0000000                                           |
| HLT            | None                                                |
| Prescale       | 1.0000000                                           |
| L0DU           | None                                                |
| ODIN           | None                                                |

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

**LoKi::VoidFilter/SelFilterPhys_StdLooseKstar2Kpi_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKstar2Kpi](./stripping21r1-stdloosekstar2kpi) /Particles')\>0 |

**FilterDesktop/BetaSPsi2S_KstarForPsi2SJpsiPiPi**

|                 |                                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (in_range(826,M,966)) & (PT \> 1500\*MeV) & (VFASPF(VCHI2) \< 16)& (MAXTREE('K+'==ABSID, TRCHI2DOF) \< 4 )& (MAXTREE('pi-'==ABSID, TRCHI2DOF) \< 4 )& (MINTREE('K+'==ABSID, PIDK) \> 0)& (MINTREE('pi-'==ABSID, PIDK) \< 10) |
| Inputs          | [ 'Phys/ [StdLooseKstar2Kpi](./stripping21r1-stdloosekstar2kpi) ' ]                                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                                         |
| Output          | Phys/BetaSPsi2S_KstarForPsi2SJpsiPiPi/Particles                                                                                                                                                                              |

**CombineParticles/BetaSPsi2S_Bd2Psi2SKstarJpsiPiPiLine**

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSPsi2S_KstarForPsi2SJpsiPiPi' , 'Phys/BetaSPsi2S_Psi2SJpsiPiPi' ]                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)\~0' : 'ALL' , 'psi(2S)' : 'ALL' }                                          |
| CombinationCut   | in_range(5000,AM,5650)                                                                                                    |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF)\<20) & (MINTREE('K\*(892)0'==ABSID, PT)\> 1000\*MeV) & (BPVLTIME()\> 0.15\*ps) |
| DecayDescriptor  | [B0 -\> psi(2S) K\*(892)0]cc                                                                                            |
| DecayDescriptors | [ '[B0 -\> psi(2S) K\*(892)0]cc' ]                                                                                    |
| Output           | Phys/BetaSPsi2S_Bd2Psi2SKstarJpsiPiPiLine/Particles                                                                       |
