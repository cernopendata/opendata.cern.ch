[[stripping21 lines]](./stripping21-index)

# StrippingH24MuLinesLooseLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/H24MuLinesLooseLine/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 0.010000000                        |
| L0DU           | None                               |
| ODIN           | None                               |

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

CombineParticles/SelA1H24MuLinesLoose

|                  |                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' ]                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 10 ) & (PT \> 0 \* MeV ) & (MIPCHI2DV(PRIMARY)\< 1000000 )' , 'mu-' : '(TRCHI2DOF \< 10 ) & (PT \> 0 \* MeV ) & (MIPCHI2DV(PRIMARY)\< 1000000 )' } |
| CombinationCut   | (AM \< 5000 \* MeV ) & (AMAXDOCA('')\<10 \* mm)                                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2)\< 20 ) & (MM \< 5000 \* MeV)                                                                                                                                              |
| DecayDescriptor  | KS0 -\> mu+ mu-                                                                                                                                                                          |
| DecayDescriptors | [ 'KS0 -\> mu+ mu-' ]                                                                                                                                                                  |
| Output           | Phys/SelA1H24MuLinesLoose/Particles                                                                                                                                                      |

CombineParticles/H24MuLinesLooseLine

|                  |                                             |
|------------------|---------------------------------------------|
| Inputs           | [ 'Phys/SelA1H24MuLinesLoose' ]           |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }              |
| CombinationCut   | (AMAXDOCA('')\< 1000000 \* mm )             |
| MotherCut        | (PT \> 300 \* MeV ) & (VFASPF(VCHI2)\< 50 ) |
| DecayDescriptor  | H_10 -\> KS0 KS0                            |
| DecayDescriptors | [ 'H_10 -\> KS0 KS0' ]                    |
| Output           | Phys/H24MuLinesLooseLine/Particles          |

AddExtraInfo/ExtraInfo_StrippingH24MuLinesLooseLine

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/SelA1H24MuLinesLoose' ]                                                                     |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/ExtraInfo_StrippingH24MuLinesLooseLine/Particles                                                 |
| Tools           | [ 'ConeVariables/Tool1' , 'ConeVariables/Tool2' , 'ConeVariables/Tool3' , 'VertexIsolation/Tool4' ] |
