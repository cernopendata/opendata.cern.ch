[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingD2hhPromptD2KPiLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/D2hhPromptD2KPiLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 0.10000000                         |
| L0DU           | None                               |
| ODIN           | None                               |

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

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

CombineParticles/D2hhPromptD2KPiLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \> 5.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'K-' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \> 5.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi-' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' } |
| CombinationCut   | (APT \> 2000.0\* MeV)& (AHASCHILD( PT \> 1500.0\* MeV ) )& (ADOCA(1,2)\< 0.07\* mm)& (AP \> 5000.0\* MeV)& (DAMASS(1865.0\* MeV) \> -100.0\* MeV)& (DAMASS(1865.0\* MeV) \< 200.0\* MeV)                                                                                                                                                                                                                                                                                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10.0)& (BPVVDCHI2 \> 40.0)& (BPVLTIME() \> 0.0)& (BPVDIRA \> 0.9999)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptor  | [D0 -\> K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/D2hhPromptD2KPiLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
