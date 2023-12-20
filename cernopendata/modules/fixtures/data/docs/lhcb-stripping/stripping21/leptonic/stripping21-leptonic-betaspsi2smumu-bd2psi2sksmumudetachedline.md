[[stripping21 lines]](./stripping21-index)

# StrippingBetaSPsi2SMuMu_Bd2Psi2SKsMuMuDetachedLine

## Properties:

|                |                                                          |
|----------------|----------------------------------------------------------|
| OutputLocation | Phys/BetaSPsi2SMuMu_Bd2Psi2SKsMuMuDetachedLine/Particles |
| Postscale      | 1.0000000                                                |
| HLT            | None                                                     |
| Prescale       | 1.0000000                                                |
| L0DU           | None                                                     |
| ODIN           | None                                                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

CombineParticles/BetaSPsi2SMuMu_Psi2SToMuMu

|                  |                                                                                 |
|------------------|---------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'PIDmu \> 0.0' , 'mu-' : 'PIDmu\>0.0' }                  |
| CombinationCut   | (ADAMASS('psi(2S)')\<60.0\*MeV) & (ADOCACHI2CUT( 30.0 ,''))                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 16) & (MFIT)                                             |
| DecayDescriptor  | psi(2S) -\> mu+ mu-                                                             |
| DecayDescriptors | [ 'psi(2S) -\> mu+ mu-' ]                                                     |
| Output           | Phys/BetaSPsi2SMuMu_Psi2SToMuMu/Particles                                       |

GaudiSequencer/SeqBetaSPsi2SMuMu_KsLooseForPsi2SToMuMu

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/BetaSPsi2SMuMu_KsLooseForPsi2SToMuMu

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/BetaSPsi2SMuMu_KsLooseForPsi2SToMuMu/Particles                                                                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/BetaSPsi2SMuMu_KsForPsi2SToMuMu

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Code            | (VFASPF(VCHI2)\<20) & (BPVDLS\>5)                 |
| Inputs          | [ 'Phys/BetaSPsi2SMuMu_KsLooseForPsi2SToMuMu' ] |
| DecayDescriptor | None                                              |
| Output          | Phys/BetaSPsi2SMuMu_KsForPsi2SToMuMu/Particles    |

CombineParticles/BetaSPsi2SMuMu_Bd2Psi2SKsMuMuDetachedLine

|                  |                                                                                  |
|------------------|----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/BetaSPsi2SMuMu_KsForPsi2SToMuMu' , 'Phys/BetaSPsi2SMuMu_Psi2SToMuMu' ] |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'psi(2S)' : 'ALL' }                               |
| CombinationCut   | in_range(5000,AM,5650)                                                           |
| MotherCut        | in_range(5150,M,5550) & (VFASPF(VCHI2PDOF)\<10)& (BPVLTIME()\> 0.2\*ps)          |
| DecayDescriptor  | B0 -\> psi(2S) KS0                                                               |
| DecayDescriptors | [ 'B0 -\> psi(2S) KS0' ]                                                       |
| Output           | Phys/BetaSPsi2SMuMu_Bd2Psi2SKsMuMuDetachedLine/Particles                         |
