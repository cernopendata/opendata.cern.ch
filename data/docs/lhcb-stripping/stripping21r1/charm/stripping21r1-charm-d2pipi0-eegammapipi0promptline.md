[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2PiPi0_eegammaPiPi0PromptLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/D2PiPi0_eegammaPiPi0PromptLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT            | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

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

LoKi::VoidFilter/SelFilterPhys_StdDiElectronFromTracks_Particles

|      |                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdDiElectronFromTracks](./stripping21r1-commonparticles-stddielectronfromtracks)/Particles')\>0 |

CombineParticles/ResforPi0+PiForD2PiPi0_eegamma

|                  |                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/GammaForD2PiPi0_eegamma' , 'Phys/[StdDiElectronFromTracks](./stripping21r1-commonparticles-stddielectronfromtracks)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'gamma' : 'ALL' }                                                                           |
| CombinationCut   | (in_range( 70.0,AM,210.0 ))                                                                                                      |
| MotherCut        | ALL                                                                                                                              |
| DecayDescriptor  | pi0 -\> J/psi(1S) gamma                                                                                                          |
| DecayDescriptors | [ 'pi0 -\> J/psi(1S) gamma' ]                                                                                                  |
| Output           | Phys/ResforPi0+PiForD2PiPi0_eegamma/Particles                                                                                    |

CombineParticles/D2PiPi0_eegammaPiPi0PromptLine

|                  |                                                                                            |
|------------------|--------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionForD2PiPi0_eegamma' , 'Phys/ResforPi0+PiForD2PiPi0_eegamma' ]                |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                             |
| CombinationCut   | (APT \> 2000.0) & (in_range( 1600.0,AM,2500.0 ))                                           |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 5) & ((BPVLTIME(25) \* c_light) \> 0.05) & (DTF_CHI2NDOF(True) \< 5) |
| DecayDescriptor  | [D+ -\> pi+ pi0]cc                                                                       |
| DecayDescriptors | [ '[D+ -\> pi+ pi0]cc' ]                                                               |
| Output           | Phys/D2PiPi0_eegammaPiPi0PromptLine/Particles                                              |
