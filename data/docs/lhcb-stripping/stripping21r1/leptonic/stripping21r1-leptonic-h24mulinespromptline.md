[[stripping21r1 lines]](./stripping21r1-index)

# StrippingH24MuLinesPromptLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/H24MuLinesPromptLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1-commonparticles-stdallloosemuons)/Particles')\>0 |

CombineParticles/SelA1H24MuLinesPrompt

|                  |                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21r1-commonparticles-stdallloosemuons)' ]                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 3 ) & ( TRGHOSTPROB \< 0.4 ) & (PT \> 350 \* MeV ) & (MIPCHI2DV(PRIMARY)\< 4 )' , 'mu-' : '(TRCHI2DOF \< 3 ) & ( TRGHOSTPROB \< 0.4 ) & (PT \> 350 \* MeV ) & (MIPCHI2DV(PRIMARY)\< 4 )' } |
| CombinationCut   | (AM \< 2000 \* MeV ) & (AMAXDOCA('')\<0.3 \* mm)                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2)\< 10 ) & (MM \< 2000 \* MeV)                                                                                                                                                                                      |
| DecayDescriptor  | KS0 -\> mu+ mu-                                                                                                                                                                                                                  |
| DecayDescriptors | [ 'KS0 -\> mu+ mu-' ]                                                                                                                                                                                                          |
| Output           | Phys/SelA1H24MuLinesPrompt/Particles                                                                                                                                                                                             |

CombineParticles/H24MuLinesPromptLine

|                  |                                              |
|------------------|----------------------------------------------|
| Inputs           | [ 'Phys/SelA1H24MuLinesPrompt' ]           |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }               |
| CombinationCut   | (AMAXDOCA('')\< 1 \* mm )                    |
| MotherCut        | (PT \> 1000 \* MeV ) & (VFASPF(VCHI2)\< 15 ) |
| DecayDescriptor  | H_10 -\> KS0 KS0                             |
| DecayDescriptors | [ 'H_10 -\> KS0 KS0' ]                     |
| Output           | Phys/H24MuLinesPromptLine/Particles          |

AddExtraInfo/ExtraInfo_StrippingH24MuLinesPromptLine

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/SelA1H24MuLinesPrompt' ]                                                                    |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/ExtraInfo_StrippingH24MuLinesPromptLine/Particles                                                |
| Tools           | [ 'ConeVariables/Tool1' , 'ConeVariables/Tool2' , 'ConeVariables/Tool3' , 'VertexIsolation/Tool4' ] |
