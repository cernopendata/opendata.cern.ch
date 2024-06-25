[[stripping21r1 lines]](./stripping21r1-index)

# StrippingPromptD2hhPromptDst2D2PiPiSSLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/PromptD2hhPromptDst2D2PiPiSSLine/Particles |
| Postscale      | 1.0000000                                       |
| HLT            | None                                            |
| Prescale       | 1.0000000                                       |
| L0DU           | None                                            |
| ODIN           | None                                            |

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

CombineParticles/PromptD2hhPromptD2PiPiSSSel

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi-' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' } |
| CombinationCut   | (APT \> 2000.0\* MeV)& (AHASCHILD( PT \> 1500.0\* MeV ) )& (ADOCA(1,2)\< 0.07\* mm)& (AP \> 5000.0\* MeV)& (DAMASS(1865.0\* MeV) \> -75.0\* MeV)& (DAMASS(1865.0\* MeV) \< 200.0\* MeV)                                                                                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10.0)& (BPVVDCHI2 \> 40.0)& (BPVDIRA \> 0.9999)                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | [D0 -\> pi- pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ '[D0 -\> pi- pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/PromptD2hhPromptD2PiPiSSSel/Particles                                                                                                                                                                                                                                                                                                                                                                                              |

CombineParticles/PromptD2hhPromptDst2D2PiPiSSLine

|                  |                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PromptD2hhPromptD2PiPiSSSel' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(TRCHI2DOF \< 5.0)' , 'pi-' : '(TRCHI2DOF \< 5.0)' }              |
| CombinationCut   | ((AM - AM1) \< 165.0\* MeV)                                                                                              |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 100.0)& ((M - M1) \< 160.0\* MeV)                                                                 |
| DecayDescriptor  | [D\*(2010)+ -\> D0 pi+]cc                                                                                              |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' ]                                                                                      |
| Output           | Phys/PromptD2hhPromptDst2D2PiPiSSLine/Particles                                                                          |
