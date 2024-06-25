[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBs2GammaGamma_DDLine

## Properties:

|                |                                                      |
|----------------|------------------------------------------------------|
| OutputLocation | Phys/Bs2GammaGamma_DDLine/Particles                  |
| Postscale      | 1.0000000                                            |
| HLT            | None                                                 |
| Prescale       | 1.0000000                                            |
| L0DU           | L0_CHANNEL_RE('Electron') \| L0_CHANNEL_RE('Photon') |
| ODIN           | None                                                 |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaDD_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseGammaDD](./stripping21r1-commonparticles-stdallloosegammadd)/Particles')\>0 |

FilterDesktop/PhotonConvFilterDDBs2GammaGamma

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT\>1400\*MeV) & (MIPCHI2DV(PRIMARY)\>(2.0/3.0)\*1.5)                                |
| Inputs          | [ 'Phys/[StdAllLooseGammaDD](./stripping21r1-commonparticles-stdallloosegammadd)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/PhotonConvFilterDDBs2GammaGamma/Particles                                        |

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21r1-commonparticles-stdlooseallphotons)/Particles')\>0 |

FilterDesktop/PhotonFilterBs2GammaGamma

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PT\>1250\*MeV) & (CL\>0.0)                                                           |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r1-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/PhotonFilterBs2GammaGamma/Particles                                              |

CombineParticles/Bs2GammaGamma_DD

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PhotonConvFilterDDBs2GammaGamma' , 'Phys/PhotonFilterBs2GammaGamma' ]         |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : '(P\>11000\*MeV)' }                                            |
| CombinationCut   | (in_range(4600\*MeV, AM, 5800\*MeV))                                                    |
| MotherCut        | (PT\>1000\*MeV) & (INTREE( (ID=='gamma') & (ISBASIC) )) & (INTREE( HASTRACK & ISDOWN )) |
| DecayDescriptor  | B_s0 -\> gamma gamma                                                                    |
| DecayDescriptors | [ 'B_s0 -\> gamma gamma' ]                                                            |
| Output           | Phys/Bs2GammaGamma_DD/Particles                                                         |

TisTosParticleTagger/Bs2GammaGamma_DDLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2GammaGamma_DD' ]              |
| DecayDescriptor | None                                       |
| Output          | Phys/Bs2GammaGamma_DDLine/Particles        |
| TisTosSpecs     | { 'L0(Photon\|Electron)Decision%TOS' : 0 } |
