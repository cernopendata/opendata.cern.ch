[[stripping21 lines]](./stripping21-index)

# StrippingBs2GammaGamma_doubleLine

## Properties:

|                |                                                      |
|----------------|------------------------------------------------------|
| OutputLocation | Phys/Bs2GammaGamma_doubleLine/Particles              |
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

LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaDD_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseGammaDD](./stripping21-commonparticles-stdallloosegammadd)/Particles')\>0 |

CombineParticles/Bs2GammaGamma_double

|                  |                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseGammaDD](./stripping21-commonparticles-stdallloosegammadd)' , 'Phys/[StdAllLooseGammaLL](./stripping21-commonparticles-stdallloosegammall)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : '(PT\>0.5\*1400\*MeV) & (P\>0.5\*11000\*MeV)' }                                                                                            |
| CombinationCut   | (in_range(4300\*MeV, AM, 5800\*MeV))                                                                                                                                |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<20)                                                                                                                                            |
| DecayDescriptor  | B_s0 -\> gamma gamma                                                                                                                                                |
| DecayDescriptors | [ 'B_s0 -\> gamma gamma' ]                                                                                                                                        |
| Output           | Phys/Bs2GammaGamma_double/Particles                                                                                                                                 |

TisTosParticleTagger/Bs2GammaGamma_doubleLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2GammaGamma_double' ]          |
| DecayDescriptor | None                                       |
| Output          | Phys/Bs2GammaGamma_doubleLine/Particles    |
| TisTosSpecs     | { 'L0(Photon\|Electron)Decision%TOS' : 0 } |
