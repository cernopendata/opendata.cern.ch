[[stripping21r1 lines]](./stripping21r1-index)

# StrippingPromptD2hhPromptD2PiPiTISLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/PromptD2hhPromptD2PiPiTISLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT            | None                                         |
| Prescale       | 0.050000000                                  |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/PromptD2hhPromptD2PiPiTISSel

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi-' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' } |
| CombinationCut   | (APT \> 2000.0\* MeV)& (AHASCHILD( PT \> 1500.0\* MeV ) )& (ADOCA(1,2)\< 0.07\* mm)& (AP \> 5000.0\* MeV)& (DAMASS(1865.0\* MeV) \> -75.0\* MeV)& (DAMASS(1865.0\* MeV) \< 200.0\* MeV)                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10.0)& (BPVVDCHI2 \> 40.0)& (BPVDIRA \> 0.9999)                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | D0 -\> pi+ pi-                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'D0 -\> pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/PromptD2hhPromptD2PiPiTISSel/Particles                                                                                                                                                                                                                                                                                                                                                                                             |

TisTosParticleTagger/PromptD2hhPromptD2PiPiTISD2hhHlt1TOS

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/PromptD2hhPromptD2PiPiTISSel' ]           |
| DecayDescriptor | None                                                |
| Output          | Phys/PromptD2hhPromptD2PiPiTISD2hhHlt1TOS/Particles |
| TisTosSpecs     | { 'Hlt1Global%TIS' : 0 }                            |

TisTosParticleTagger/PromptD2hhPromptD2PiPiTISLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/PromptD2hhPromptD2PiPiTISD2hhHlt1TOS' ] |
| DecayDescriptor | None                                              |
| Output          | Phys/PromptD2hhPromptD2PiPiTISLine/Particles      |
| TisTosSpecs     | { 'Hlt2Global%TIS' : 0 }                          |
