[[stripping21r1 lines]](./stripping21r1-index)

# StrippingCC2DDLine

## Properties:

|                |                          |
|----------------|--------------------------|
| OutputLocation | Phys/CC2DDLine/Particles |
| Postscale      | 1.0000000                |
| HLT            | None                     |
| Prescale       | 1.0000000                |
| L0DU           | None                     |
| ODIN           | None                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqCC2DDMergedDSelection

GaudiSequencer/SEQ:D0ForCC2DD

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21r1-commonparticles-stdalllooseannkaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r1-commonparticles-stdalllooseannpions)/Particles')\>0 |

CombineParticles/D0ForCC2DD

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21r1-commonparticles-stdalllooseannkaons)' , 'Phys/[StdAllLooseANNPions](./stripping21r1-commonparticles-stdalllooseannpions)' ]                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\> 600\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNk\>0.1)' , 'K-' : '(PT\> 600\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNk\>0.1)' , 'pi+' : '(PT\> 600\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNpi\>0.1)' , 'pi-' : '(PT\> 600\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNpi\>0.1)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MotherCut        | (ADMASS('D0')\<60\*MeV) & (PT\>0\*MeV) & (VFASPF(VCHI2PDOF)\<10.0) & (BPVDIRA\>-10.0) & (BPVDLS\>4.0)                                                                                                                                                                                                                                                                                                                                                                          |
| DecayDescriptor  | [D0 -\> K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/D0ForCC2DD/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DpForCC2DD

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21r1-commonparticles-stdalllooseannkaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r1-commonparticles-stdalllooseannpions)/Particles')\>0 |

CombineParticles/DpForCC2DD

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21r1-commonparticles-stdalllooseannkaons)' , 'Phys/[StdAllLooseANNPions](./stripping21r1-commonparticles-stdalllooseannpions)' ]                                                                                                                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNk\>0.1)' , 'K-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNk\>0.1)' , 'pi+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNpi\>0.1)' , 'pi-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNpi\>0.1)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (ADMASS('D+')\<60\*MeV) & (PT\> 0\*MeV) & (VFASPF(VCHI2PDOF) \< 10.0) & (BPVDIRA\>-10.0) & (BPVDLS \> 4.0)                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptor  | [D+ -\> K- pi+ pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ '[D+ -\> K- pi+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Output           | Phys/DpForCC2DD/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:DsForCC2DD

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21r1-commonparticles-stdallloosekaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/DsForCC2DD

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21r1-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ]                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNk\>0.1)' , 'K-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNk\>0.1)' , 'pi+' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNpi\>0.1)' , 'pi-' : '(PT\>500\*MeV) & (P\>5\*GeV) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & (BPVIPCHI2()\>6.0)&(PROBNNpi\>0.1)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| MotherCut        | (ADMASS('D+')\<60\*MeV) & (PT\> 0\*MeV) & (VFASPF(VCHI2PDOF) \< 10.0) & (BPVDIRA\>-10.0) & (BPVDLS \> 4.0)                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptor  | [D_s+ -\> K- K+ pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[D_s+ -\> K- K+ pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/DsForCC2DD/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/CC2DDMergedDSelection

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Code            | ALL                                                             |
| Inputs          | [ 'Phys/D0ForCC2DD' , 'Phys/DpForCC2DD' , 'Phys/DsForCC2DD' ] |
| DecayDescriptor | None                                                            |
| Output          | Phys/CC2DDMergedDSelection/Particles                            |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/CC2DDLine

|                  |                                                                                                                                                                                                                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CC2DDMergedDSelection' ]                                                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'D0' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'D~0' : 'ALL' }                                                                                                                                                                                                                                                              |
| CombinationCut   | (AM\>0)&(AMAXCHILD(PT)\>1500\*MeV)                                                                                                                                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2PDOF)\<10)&(MAXTREE(ISBASIC,PT)\>1200\*MeV)                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ 'psi(3770) -\> D0 D~0' , '[psi(3770) -\> D0 D0]cc' , 'psi(3770) -\> D+ D-' , '[psi(3770) -\> D+ D+]cc' , 'psi(3770) -\> D_s+ D_s-' , '[psi(3770) -\> D_s+ D_s+]cc' , '[psi(3770) -\> D0 D-]cc' , '[psi(3770) -\> D0 D+]cc' , '[psi(3770) -\> D0 D_s-]cc' , '[psi(3770) -\> D+ D_s-]cc' , '[psi(3770) -\> D0 D_s+]cc' , '[psi(3770) -\> D+ D_s+]cc' ] |
| Output           | Phys/CC2DDLine/Particles                                                                                                                                                                                                                                                                                                                                                   |
