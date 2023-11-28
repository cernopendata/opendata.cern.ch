[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2PiPi0_eegammaSemiLeptonicLine

## Properties:

|                |                                                |
|----------------|------------------------------------------------|
| OutputLocation | Phys/D2PiPi0_eegammaSemiLeptonicLine/Particles |
| Postscale      | 1.0000000                                      |
| HLT            | None                                           |
| Prescale       | 1.0000000                                      |
| L0DU           | None                                           |
| ODIN           | None                                           |

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

CombineParticles/ResforSLPi0+PiForD2PiPi0_eegamma

|                  |                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/GammaForD2PiPi0_eegamma' , 'Phys/[StdDiElectronFromTracks](./stripping21r1-commonparticles-stddielectronfromtracks)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'gamma' : 'ALL' }                                                                           |
| CombinationCut   | (in_range( 70.0,AM,210.0 ))                                                                                                      |
| MotherCut        | ALL                                                                                                                              |
| DecayDescriptor  | pi0 -\> J/psi(1S) gamma                                                                                                          |
| DecayDescriptors | [ 'pi0 -\> J/psi(1S) gamma' ]                                                                                                  |
| Output           | Phys/ResforSLPi0+PiForD2PiPi0_eegamma/Particles                                                                                  |

CombineParticles/DpforD2PiPi0_eegammaPiPi0SLSelection

|                  |                                                                                              |
|------------------|----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionForD2PiPi0_eegamma' , 'Phys/ResforSLPi0+PiForD2PiPi0_eegamma' ]                |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'pi0' : 'ALL' }                               |
| CombinationCut   | (APT \> 1000.0) & (in_range( 1600.0,AM,2500.0 ))                                             |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 15) & ((BPVLTIME(25) \* c_light) \> 0.05) & (DTF_CHI2NDOF(True) \< 10) |
| DecayDescriptor  | [D+ -\> pi+ pi0]cc                                                                         |
| DecayDescriptors | [ '[D+ -\> pi+ pi0]cc' ]                                                                 |
| Output           | Phys/DpforD2PiPi0_eegammaPiPi0SLSelection/Particles                                          |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuonD2PiPi0_eegamma

|                 |                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------|
| Code            | (P \> 1000.0) & (PT \> 350.0) & (TRCHI2DOF \< 5) & (MIPCHI2DV(PRIMARY) \> 25)&(PIDmu-PIDpi \> 0) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                      |
| DecayDescriptor | None                                                                                             |
| Output          | Phys/MuonD2PiPi0_eegamma/Particles                                                               |

CombineParticles/D2PiPi0_eegammaSemiLeptonicLine

|                  |                                                                                |
|------------------|--------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DpforD2PiPi0_eegammaPiPi0SLSelection' , 'Phys/MuonD2PiPi0_eegamma' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }   |
| CombinationCut   | in_range( 2200.0,AM,6300.0 )                                                   |
| MotherCut        | ((BPVLTIME(25) \* c_light) \> 0.05)& (DTF_CHI2NDOF(True) \< 10)                |
| DecayDescriptor  | None                                                                           |
| DecayDescriptors | [ '[B0 -\> D+ mu-]cc' , '[B+ -\> D+ mu+]cc' ]                            |
| Output           | Phys/D2PiPi0_eegammaSemiLeptonicLine/Particles                                 |
