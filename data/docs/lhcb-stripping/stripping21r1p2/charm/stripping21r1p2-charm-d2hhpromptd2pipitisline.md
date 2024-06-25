[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingD2hhPromptD2PiPiTISLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/D2hhPromptD2PiPiTISLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

CombineParticles/D2hhPromptD2PiPiTISSel

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi-' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' } |
| CombinationCut   | (APT \> 2000.0\* MeV)& (AHASCHILD( PT \> 1500.0\* MeV ) )& (ADOCA(1,2)\< 0.07\* mm)& (AP \> 5000.0\* MeV)& (DAMASS(1865.0\* MeV) \> -75.0\* MeV)& (DAMASS(1865.0\* MeV) \< 200.0\* MeV)                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10.0)& (BPVVDCHI2 \> 40.0)& (BPVLTIME() \> 0.0)& (BPVDIRA \> 0.9999)                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptor  | D0 -\> pi+ pi-                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ 'D0 -\> pi+ pi-' ]                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Output           | Phys/D2hhPromptD2PiPiTISSel/Particles                                                                                                                                                                                                                                                                                                                                                                                                   |

TisTosParticleTagger/D2hhPromptD2PiPiTISD2hhHlt1TOS

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/D2hhPromptD2PiPiTISSel' ]           |
| DecayDescriptor | None                                          |
| Output          | Phys/D2hhPromptD2PiPiTISD2hhHlt1TOS/Particles |
| TisTosSpecs     | { 'Hlt1Global%TIS' : 0 }                      |

TisTosParticleTagger/D2hhPromptD2PiPiTISLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/D2hhPromptD2PiPiTISD2hhHlt1TOS' ] |
| DecayDescriptor | None                                        |
| Output          | Phys/D2hhPromptD2PiPiTISLine/Particles      |
| TisTosSpecs     | { 'Hlt2Global%TIS' : 0 }                    |
