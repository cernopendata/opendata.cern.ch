[[stripping21r1 lines]](./stripping21r1-index)

# StrippingCharmedAndCharmedStrangeSpectroscopy_DstarD02K3PiKs

## Properties:

|                |                                                                    |
|----------------|--------------------------------------------------------------------|
| OutputLocation | Phys/CharmedAndCharmedStrangeSpectroscopy_DstarD02K3PiKs/Particles |
| Postscale      | 1.0000000                                                          |
| HLT            | None                                                               |
| Prescale       | 1.0000000                                                          |
| L0DU           | None                                                               |
| ODIN           | None                                                               |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyLoosePromptPi

|                 |                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------|
| Code            | (ISLONG) & (PT\>250\*MeV) & (P\>1\*GeV) & (MIPCHI2DV(PRIMARY)\<16.0) & (TRPCHI2\>0.0001) & (HASRICH) |
| Inputs          | [ 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ]                    |
| DecayDescriptor | None                                                                                                 |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyLoosePromptPi/Particles                                     |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyLoosePi

|                 |                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ISLONG) & (PT\>400\*MeV) & (P\>1\*GeV) & (MIPCHI2DV(PRIMARY)\>25.0) & (TRPCHI2\>0.0001) & (HASRICH) & (TRCHI2DOF\<3) & ((PIDK-PIDpi)\<7) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                                                               |
| DecayDescriptor | None                                                                                                                                      |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyLoosePi/Particles                                                                                |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyLooseK

|                 |                                                                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ISLONG) & (PT\>400\*MeV) & (P\>1\*GeV) & (MIPCHI2DV(PRIMARY)\>25.0) & (TRPCHI2\>0.0001) & (HASRICH) & (TRCHI2DOF\<3) & ((PIDK-PIDpi)\>0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ]                                                               |
| DecayDescriptor | None                                                                                                                                      |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyLooseK/Particles                                                                                 |

CombineParticles/CharmedAndCharmedStrangeSpectroscopyD02K3Pi

|                  |                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmedAndCharmedStrangeSpectroscopyLooseK' , 'Phys/CharmedAndCharmedStrangeSpectroscopyLoosePi' ]                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                |
| CombinationCut   | (ADAMASS('D0')\<100.0\*MeV) & (APT\>800.0\*MeV) & (AMAXDOCA('')\<0.15\*mm)                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (MIPCHI2DV(PRIMARY) \< 16.0) & (BPVDIRA\>0.9999) & (ADMASS('D0')\<100.0\*MeV) & (PT\>2.0\*GeV) |
| DecayDescriptor  | [D0 -\> K- pi+ pi- pi+]cc                                                                                                                 |
| DecayDescriptors | [ '[D0 -\> K- pi+ pi- pi+]cc' ]                                                                                                         |
| Output           | Phys/CharmedAndCharmedStrangeSpectroscopyD02K3Pi/Particles                                                                                  |

CombineParticles/CharmedAndCharmedStrangeSpectroscopyDstarD02K3Pi

|                  |                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmedAndCharmedStrangeSpectroscopyD02K3Pi' , 'Phys/CharmedAndCharmedStrangeSpectroscopyLoosePromptPi' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                       |
| CombinationCut   | (APT\>3.0\*GeV) & (AMAXDOCA('')\<0.2\*mm)                                                                           |
| MotherCut        | (M-MAXTREE('D0'==ABSID,M)\<160\*MeV) & (VFASPF(VCHI2/VDOF)\<20)                                                     |
| DecayDescriptor  | [D\*(2010)+ -\> pi+ D0]cc                                                                                         |
| DecayDescriptors | [ '[D\*(2010)+ -\> pi+ D0]cc' ]                                                                                 |
| Output           | Phys/CharmedAndCharmedStrangeSpectroscopyDstarD02K3Pi/Particles                                                     |

GaudiSequencer/SeqCharmedAndCharmedStrangeSpectroscopyKS0

GaudiSequencer/SEQ:CharmedAndCharmedStrangeSpectroscopyKSLongLong

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyKSLongLong

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((BPVVDZ \> -20 \*cm) & (BPVVDZ \< 65 \*cm) & (BPVVD \> 1.5\*cm) & (BPVDIRA \> 0.9999) & (CHILDIP(1) \< 0.5\*mm) & (CHILDIP(2) \< 0.5 \*mm) & (VFASPF(VPCHI2) \> 0.1\*perCent)& CHILDCUT((TRPCHI2 \> 0.0001) & (PT \> 250\*MeV) & (P \< 100\*GeV) & (MIPDV(PRIMARY) \> 0.5\*mm) & (HASRICH), 1) & CHILDCUT((TRPCHI2 \> 0.0001) & (PT \> 250\*MeV) & (P \< 100\*GeV) & (MIPDV(PRIMARY) \> 0.5\*mm) & (HASRICH), 2) ) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)' ]                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyKSLongLong/Particles                                                                                                                                                                                                                                                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:CharmedAndCharmedStrangeSpectroscopyKSDownDown

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyKSDownDown

|                 |                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((BPVVDZ \> 0.0\*cm) & (BPVVDZ \< 230.0\*cm) & (BPVVD \> 20.0\*cm) & (BPVDIRA \> 0.9999) & (CHILDIP(1) \< 6.0\*mm) & (CHILDIP(2) \< 6.0 \*mm)& CHILDCUT((TRPCHI2 \> 0.0001) & (PT \> 250\*MeV) & (P \< 100\*GeV) & (MIPDV(PRIMARY) \> 0.5\*mm) & (HASRICH), 1) & CHILDCUT((TRPCHI2 \> 0.0001) & (PT \> 250\*MeV) & (P \< 100\*GeV) & (MIPDV(PRIMARY) \> 0.5\*mm) & (HASRICH), 2) ) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1-commonparticles-stdlooseksdd)' ]                                                                                                                                                                                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                               |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyKSDownDown/Particles                                                                                                                                                                                                                                                                                                                      |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyKS0

|                 |                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                 |
| Inputs          | [ 'Phys/CharmedAndCharmedStrangeSpectroscopyKSDownDown' , 'Phys/CharmedAndCharmedStrangeSpectroscopyKSLongLong' ] |
| DecayDescriptor | None                                                                                                                |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyKS0/Particles                                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/CharmedAndCharmedStrangeSpectroscopy_DstarD02K3PiKs

|                  |                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmedAndCharmedStrangeSpectroscopyDstarD02K3Pi' , 'Phys/CharmedAndCharmedStrangeSpectroscopyKS0' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'KS0' : 'ALL' }                                   |
| CombinationCut   | ATRUE                                                                                                          |
| MotherCut        | (M \> 0.0\*GeV) & ~INTREE( (HASTRACK)&(THASINFO( LHCb.Track.CloneDist )) )                                     |
| DecayDescriptor  | [D_s1(2536)+ -\> D\*(2010)+ KS0]cc                                                                           |
| DecayDescriptors | [ '[D_s1(2536)+ -\> D\*(2010)+ KS0]cc' ]                                                                   |
| Output           | Phys/CharmedAndCharmedStrangeSpectroscopy_DstarD02K3PiKs/Particles                                             |
