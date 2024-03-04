[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2hhCompleteEventPromptD0D0FromDstarPartialLine

## Properties:

|                |                                                                |
|----------------|----------------------------------------------------------------|
| OutputLocation | Phys/D2hhCompleteEventPromptD0D0FromDstarPartialLine/Particles |
| Postscale      | 1.0000000                                                      |
| HLT            | None                                                           |
| Prescale       | 1.0000000                                                      |
| L0DU           | None                                                           |
| ODIN           | None                                                           |

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

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/D2hhCompleteEventPromptD2KPiSel

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \> 5.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'K-' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \> 5.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi-' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' } |
| CombinationCut   | (APT \> 2000.0\* MeV)& (AHASCHILD( PT \> 1500.0\* MeV ) )& (ADOCA(1,2)\< 0.07\* mm)& (AP \> 5000.0\* MeV)& (DAMASS(1865.0\* MeV) \> -100.0\* MeV)& (DAMASS(1865.0\* MeV) \< 200.0\* MeV)                                                                                                                                                                                                                                                                                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10.0)& (BPVVDCHI2 \> 40.0)& (BPVDIRA \> 0.9999)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | [D0 -\> K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/D2hhCompleteEventPromptD2KPiSel/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

TisTosParticleTagger/D2hhCompleteEventPromptD2KPiD2hhHlt1TOS

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/D2hhCompleteEventPromptD2KPiSel' ]           |
| DecayDescriptor | None                                                   |
| Output          | Phys/D2hhCompleteEventPromptD2KPiD2hhHlt1TOS/Particles |
| TisTosSpecs     | { 'Hlt1TrackAllL0.\*Decision%TOS' : 0 }                |

TisTosParticleTagger/D2hhCompleteEventPromptD2KPiD2hhHlt2TOS

|                 |                                                                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/D2hhCompleteEventPromptD2KPiD2hhHlt1TOS' ]                                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                                                      |
| Output          | Phys/D2hhCompleteEventPromptD2KPiD2hhHlt2TOS/Particles                                                                                                                                    |
| TisTosSpecs     | { 'Hlt2CharmHadD02HH_D02KPiDecision%TOS' : 0 , 'Hlt2CharmHadD02HH_D02KPiWideMassDecision%TOS' : 0 , 'Hlt2CharmHadD02KPiDecision%TOS' : 0 , 'Hlt2CharmHadD02KPiWideMassDecision%TOS' : 0 } |

CombineParticles/D2hhCompleteEventPromptDPartialSel

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '~ISMUON & (PT \> 500.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (PIDK \> 5.0) & (ISLONG) & (P \> 3000.0\* MeV) & (TRCHI2DOF \< 4.0)' , 'K-' : '~ISMUON & (PT \> 500.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (PIDK \> 5.0) & (ISLONG) & (P \> 3000.0\* MeV) & (TRCHI2DOF \< 4.0)' , 'pi+' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' , 'pi-' : '~ISMUON & (PT \> 800.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 9.0) & (PIDK \< 0.0) & (ISLONG) & (P \> 5000.0\* MeV) & (TRCHI2DOF \< 3.0)' } |
| CombinationCut   | (APT \> 1500.0\* MeV)& (AP \> 5000.0\* MeV)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10.0)& (BPVVDCHI2 \> 40.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor  | [D- -\> K- pi- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptors | [ '[D- -\> K- pi- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/D2hhCompleteEventPromptDPartialSel/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

CombineParticles/D2hhCompleteEventPromptDstarPartialSel

|                  |                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2hhCompleteEventPromptDPartialSel' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'pi+' : '(TRCHI2DOF \< 5.0)' , 'pi-' : '(TRCHI2DOF \< 5.0)' }                      |
| CombinationCut   | ((AM - AM1) \< 165.0\* MeV)                                                                                                     |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 100.0)& ((M - M1) \< 160.0\* MeV)                                                                        |
| DecayDescriptor  | [D\*(2010)+ -\> D- pi+]cc                                                                                                     |
| DecayDescriptors | [ '[D\*(2010)+ -\> D- pi+]cc' ]                                                                                             |
| Output           | Phys/D2hhCompleteEventPromptDstarPartialSel/Particles                                                                           |

CombineParticles/D2hhCompleteEventPromptD0D0FromDstarPartialLine

|                  |                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2hhCompleteEventPromptD2KPiD2hhHlt2TOS' , 'Phys/D2hhCompleteEventPromptDstarPartialSel' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'D0' : '(PT\> 1500.0\*MeV)' , 'D~0' : '(PT\> 1500.0\*MeV)' } |
| CombinationCut   | (APT\> 1500.0\*MeV)                                                                                                       |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 10000)                                                                                              |
| DecayDescriptor  | [psi(3770) -\> D0 D\*(2010)+]cc                                                                                         |
| DecayDescriptors | [ '[psi(3770) -\> D0 D\*(2010)+]cc' ]                                                                                 |
| Output           | Phys/D2hhCompleteEventPromptD0D0FromDstarPartialLine/Particles                                                            |
