[[stripping21 lines]](./stripping21-index)

# StrippingBs2GammaGamma_LLLine

## Properties:

|                |                                                      |
|----------------|------------------------------------------------------|
| OutputLocation | Phys/Bs2GammaGamma_LLLine/Particles                  |
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

LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaLL_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseGammaLL](./stripping21-commonparticles-stdallloosegammall)/Particles')\>0 |

FilterDesktop/PhotonConvFilterLLBs2GammaGamma

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\>(1400-200.0)\*MeV) & (MIPCHI2DV(PRIMARY)\>1.5)                                 |
| Inputs          | [ 'Phys/[StdAllLooseGammaLL](./stripping21-commonparticles-stdallloosegammall)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/PhotonConvFilterLLBs2GammaGamma/Particles                                      |

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21-commonparticles-stdlooseallphotons)/Particles')\>0 |

FilterDesktop/PhotonFilterBs2GammaGamma

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\>1250\*MeV) & (CL\>0.0)                                                         |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/PhotonFilterBs2GammaGamma/Particles                                            |

CombineParticles/Bs2GammaGamma_LL

|                  |                                                                                         |
|------------------|-----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PhotonConvFilterLLBs2GammaGamma' , 'Phys/PhotonFilterBs2GammaGamma' ]         |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : '(P\>(11000-2000.0)\*MeV)' }                                   |
| CombinationCut   | (in_range(4600\*MeV, AM, 5800\*MeV))                                                    |
| MotherCut        | (PT\>1000\*MeV) & (INTREE( (ID=='gamma') & (ISBASIC) )) & (INTREE( HASTRACK & ISLONG )) |
| DecayDescriptor  | B_s0 -\> gamma gamma                                                                    |
| DecayDescriptors | [ 'B_s0 -\> gamma gamma' ]                                                            |
| Output           | Phys/Bs2GammaGamma_LL/Particles                                                         |

TisTosParticleTagger/Bs2GammaGamma_LLLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2GammaGamma_LL' ]              |
| DecayDescriptor | None                                       |
| Output          | Phys/Bs2GammaGamma_LLLine/Particles        |
| TisTosSpecs     | { 'L0(Photon\|Electron)Decision%TOS' : 0 } |
