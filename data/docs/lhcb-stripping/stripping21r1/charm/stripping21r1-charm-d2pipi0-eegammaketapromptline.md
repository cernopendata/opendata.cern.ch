[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2PiPi0_eegammaKEtaPromptLine

## Properties:

|                |                                              |
|----------------|----------------------------------------------|
| OutputLocation | Phys/D2PiPi0_eegammaKEtaPromptLine/Particles |
| Postscale      | 1.0000000                                    |
| HLT            | None                                         |
| Prescale       | 1.0000000                                    |
| L0DU           | None                                         |
| ODIN           | None                                         |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KaonForD2PiPi0_eegamma

|                 |                                                                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 1000.0) & (PT \> 350.0) & (TRCHI2DOF \< 5) & (MIPCHI2DV(PRIMARY) \> 25)&(HASRICH) & (in_range( 2, ETA, 5)) & (TRGHOSTPROB \< 0.5)&(PIDK-PIDpi \> -1) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ]                                                                                |
| DecayDescriptor | None                                                                                                                                                       |
| Output          | Phys/KaonForD2PiPi0_eegamma/Particles                                                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21r1-commonparticles-stdlooseallphotons)/Particles')\>0 |

FilterDesktop/GammaForD2PiPi0_eegamma

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (P \> 1000.0) & (PT \> 350.0) & (TRCHI2DOF \< 5) & (MIPCHI2DV(PRIMARY) \> 25)         |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r1-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/GammaForD2PiPi0_eegamma/Particles                                                |

FilterDesktop/highPTGammaForD2PiPi0_eegamma

|                 |                                              |
|-----------------|----------------------------------------------|
| Code            | (PT \> 600.0)                                |
| Inputs          | [ 'Phys/GammaForD2PiPi0_eegamma' ]         |
| DecayDescriptor | None                                         |
| Output          | Phys/highPTGammaForD2PiPi0_eegamma/Particles |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionForD2PiPi0_eegamma

|                 |                                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (P \> 1000.0) & (PT \> 350.0) & (TRCHI2DOF \< 5) & (MIPCHI2DV(PRIMARY) \> 25)&(HASRICH) & (in_range( 2, ETA, 5)) & (TRGHOSTPROB \< 0.5) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                                                             |
| DecayDescriptor | None                                                                                                                                    |
| Output          | Phys/PionForD2PiPi0_eegamma/Particles                                                                                                   |

CombineParticles/ResforEta+KForD2PiPi0_eegamma

|                  |                                                                            |
|------------------|----------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionForD2PiPi0_eegamma' , 'Phys/highPTGammaForD2PiPi0_eegamma' ] |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }           |
| CombinationCut   | (in_range( 500.0,AM,600.0 ))                                               |
| MotherCut        | ALL                                                                        |
| DecayDescriptor  | eta -\> pi+ pi- gamma                                                      |
| DecayDescriptors | [ 'eta -\> pi+ pi- gamma' ]                                              |
| Output           | Phys/ResforEta+KForD2PiPi0_eegamma/Particles                               |

CombineParticles/D2PiPi0_eegammaKEtaPromptLine

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonForD2PiPi0_eegamma' , 'Phys/ResforEta+KForD2PiPi0_eegamma' ]                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'eta' : 'ALL' }                               |
| CombinationCut   | (APT \> 2000.0) & (in_range( 1600.0,AM,2500.0 ))                                           |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 5) & ((BPVLTIME(25) \* c_light) \> 0.05) & (DTF_CHI2NDOF(True) \< 5) |
| DecayDescriptor  | [D+ -\> K+ eta]cc                                                                        |
| DecayDescriptors | [ '[D+ -\> K+ eta]cc' ]                                                                |
| Output           | Phys/D2PiPi0_eegammaKEtaPromptLine/Particles                                               |
