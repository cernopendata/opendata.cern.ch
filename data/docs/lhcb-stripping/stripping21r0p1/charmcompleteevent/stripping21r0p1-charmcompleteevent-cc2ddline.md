[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingCC2DDLine

## Properties:

|                |                          |
|----------------|--------------------------|
| OutputLocation | Phys/CC2DDLine/Particles |
| Postscale      | 1.0000000                |
| HLT1           | None                     |
| HLT2           | None                     |
| Prescale       | 1.0000000                |
| L0DU           | None                     |
| ODIN           | None                     |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharmCompleteEvent

|      |                                                                                                                      |
|------|----------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamCharmCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqCC2DDMergedDSelection

GaudiSequencer/SEQ:D0ForCC2DD

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)/Particles',True)\>0 |

CombineParticles/D0ForCC2DD

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)' , 'Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)' ]                                                                                                                                                                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\> 600\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNk\>0.1)' , 'K-' : '(PT\> 600\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNk\>0.1)' , 'pi+' : '(PT\> 600\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNpi\>0.1)' , 'pi-' : '(PT\> 600\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNpi\>0.1)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | (ADMASS('D0')\<60\*MeV) & (PT\>1000\*MeV) & (VFASPF(VCHI2PDOF)\<8) & (BPVDIRA\>-10.0) & (BPVDLS\>4.0)                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptor  | [D0 -\> K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/D0ForCC2DD/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DpForCC2DD

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)/Particles',True)\>0 |

CombineParticles/DpForCC2DD

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)' , 'Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)' ]                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNk\>0.1)' , 'K-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNk\>0.1)' , 'pi+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNpi\>0.1)' , 'pi-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNpi\>0.1)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| MotherCut        | (ADMASS('D+')\<60\*MeV) & (PT\> 1000\*MeV) & (VFASPF(VCHI2PDOF) \< 8) & (BPVDIRA\>-10.0) & (BPVDLS \> 4.0)                                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptor  | [D+ -\> K- pi+ pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[D+ -\> K- pi+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/DpForCC2DD/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DsForCC2DD

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)/Particles',True)\>0 |

CombineParticles/DsForCC2DD

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)' , 'Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)' ]                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNk\>0.1)' , 'K-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNk\>0.1)' , 'pi+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNpi\>0.1)' , 'pi-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNpi\>0.1)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| MotherCut        | (ADMASS('D_s+')\<60\*MeV) & (PT\> 1000\*MeV) & (VFASPF(VCHI2PDOF) \< 8) & (BPVDIRA\>-10.0) & (BPVDLS \> 4.0)                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | [D_s+ -\> K- K+ pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ '[D_s+ -\> K- K+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Output           | Phys/DsForCC2DD/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:LcForCC2DD

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNProtons_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNProtons](./stripping21r0p1-commonparticles-stdalllooseannprotons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)/Particles',True)\>0 |

CombineParticles/LcForCC2DD

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)' , 'Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)' , 'Phys/[StdAllLooseANNProtons](./stripping21r0p1-commonparticles-stdalllooseannprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNk\>0.1)' , 'K-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNk\>0.1)' , 'p+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNp\>0.15)' , 'pi+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNpi\>0.1)' , 'pi-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNpi\>0.1)' , 'p~-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>4.0)&(PROBNNp\>0.15)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| MotherCut        | ( (ADMASS('Lambda_c+')\<60\*MeV) \| (ADMASS('Xi_c+')\<60\*MeV) ) & (PT\> 1000\*MeV) & (VFASPF(VCHI2PDOF) \< 8) & (BPVDIRA\>-10.0) & (BPVDLS \> 4.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptor  | [Lambda_c+ -\> p+ K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Output           | Phys/LcForCC2DD/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:XcForCC2DD

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNProtons_Particles

|      |                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNProtons](./stripping21r0p1-commonparticles-stdalllooseannprotons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)/Particles',True)\>0 |

CombineParticles/XcForCC2DD

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)' , 'Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)' , 'Phys/[StdAllLooseANNProtons](./stripping21r0p1-commonparticles-stdalllooseannprotons)' ]                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>2.0)&(PROBNNk\>0.1)' , 'K-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>2.0)&(PROBNNk\>0.1)' , 'p+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>2.0)&(PROBNNp\>0.15)' , 'pi+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>2.0)&(PROBNNpi\>0.1)' , 'pi-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>2.0)&(PROBNNpi\>0.1)' , 'p~-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3) & (TRGHP\<0.3) & (BPVIPCHI2()\>2.0)&(PROBNNp\>0.15)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| MotherCut        | ( (ADMASS('Xi_c0')\<60\*MeV) \| (ADMASS('Omega_c0')\<60\*MeV) ) & (PT\> 1000\*MeV) & (VFASPF(VCHI2PDOF) \< 8) & (BPVDIRA\>-10.0) & (BPVDLS \> -10.0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptor  | [Xi_c0 -\> p+ K- K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[Xi_c0 -\> p+ K- K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/XcForCC2DD/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/CC2DDMergedDSelection

|                 |                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                     |
| Inputs          | [ 'Phys/D0ForCC2DD' , 'Phys/DpForCC2DD' , 'Phys/DsForCC2DD' , 'Phys/LcForCC2DD' , 'Phys/XcForCC2DD' ] |
| DecayDescriptor | None                                                                                                    |
| Output          | Phys/CC2DDMergedDSelection/Particles                                                                    |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/CC2DDLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CC2DDMergedDSelection' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'D~0' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'Xi_c0' : 'ALL' , 'Xi_c~0' : 'ALL' }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| CombinationCut   | (AALL)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MotherCut        | (ALL)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'psi(3770) -\> D0 D~0' , '[psi(3770) -\> D0 D0]cc' , 'psi(3770) -\> D+ D-' , '[psi(3770) -\> D+ D+]cc' , 'psi(3770) -\> D_s+ D_s-' , '[psi(3770) -\> D_s+ D_s+]cc' , '[psi(3770) -\> D0 D-]cc' , '[psi(3770) -\> D0 D+]cc' , '[psi(3770) -\> D0 D_s-]cc' , '[psi(3770) -\> D+ D_s-]cc' , '[psi(3770) -\> D0 D_s+]cc' , '[psi(3770) -\> D+ D_s+]cc' , '[psi(3770) -\> Lambda_c+ D0]cc' , '[psi(3770) -\> Lambda_c+ D~0]cc' , '[psi(3770) -\> Lambda_c+ D+]cc' , '[psi(3770) -\> Lambda_c+ D-]cc' , '[psi(3770) -\> Lambda_c+ D_s+]cc' , '[psi(3770) -\> Lambda_c+ D_s-]cc' , '[psi(3770) -\> Xi_c0 D0]cc' , '[psi(3770) -\> Xi_c0 D~0]cc' , '[psi(3770) -\> Xi_c0 D+]cc' , '[psi(3770) -\> Xi_c0 D-]cc' , '[psi(3770) -\> Xi_c0 D_s+]cc' , '[psi(3770) -\> Xi_c0 D_s-]cc' , 'psi(3770) -\> Lambda_c+ Lambda_c~-' , '[psi(3770) -\> Lambda_c+ Lambda_c+]cc' , 'psi(3770) -\> Xi_c0 Xi_c~0' , '[psi(3770) -\> Xi_c0 Xi_c0]cc' , '[psi(3770) -\> Lambda_c+ Xi_c0]cc' , '[psi(3770) -\> Lambda_c+ Xi_c~0]cc' ] |
| Output           | Phys/CC2DDLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
