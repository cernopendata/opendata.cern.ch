[[stripping21 lines]](./stripping21-index)

# StrippingD2XGammaStripping_Dst2D0Pi

## Properties:

|                |                                           |
|----------------|-------------------------------------------|
| OutputLocation | Phys/D2XGammaStripping_Dst2D0Pi/Particles |
| Postscale      | 1.0000000                                 |
| HLT            | None                                      |
| Prescale       | 1.0000000                                 |
| L0DU           | None                                      |
| ODIN           | None                                      |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePhi2KK](./stripping21-commonparticles-stdloosephi2kk)/Particles')\>0 |

FilterDesktop/PhiForD2XGamma

|                 |                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ( (VFASPF(VCHI2/VDOF) \< 16.0) & (ADMASS('phi(1020)') \< 50.0\*MeV) & (MM \> 1000.0\*MeV) ) & CHILDCUT( ( ((PIDK-PIDpi)\>2.0) & (MIPCHI2DV(PRIMARY) \> 25.0) & (TRCHI2DOF \< 2.5) & (PT \> 500.0)) & ( TRGHOSTPROB \< 0.3 ) , 1 ) & CHILDCUT( ( ((PIDK-PIDpi)\>2.0) & (MIPCHI2DV(PRIMARY) \> 25.0) & (TRCHI2DOF \< 2.5) & (PT \> 500.0)) & ( TRGHOSTPROB \< 0.3 ) , 2 ) |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21-commonparticles-stdloosephi2kk)' ]                                                                                                                                                                                                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                    |
| Output          | Phys/PhiForD2XGamma/Particles                                                                                                                                                                                                                                                                                                                                           |

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21-commonparticles-stdlooseallphotons)/Particles')\>0 |

FilterDesktop/GammaForD2XGamma

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT\> 1700.0\*MeV)                                                                  |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/GammaForD2XGamma/Particles                                                     |

CombineParticles/D02PhiGammaForD2XGamma

|                  |                                                        |
|------------------|--------------------------------------------------------|
| Inputs           | [ 'Phys/GammaForD2XGamma' , 'Phys/PhiForD2XGamma' ]  |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | (ADAMASS('D0')\<1.1\*200.0\*MeV)                       |
| MotherCut        | ( (ADMASS('D0')\<200.0\*MeV) & (PT\> 1000.0) )         |
| DecayDescriptor  | D0 -\> phi(1020) gamma                                 |
| DecayDescriptors | [ 'D0 -\> phi(1020) gamma' ]                         |
| Output           | Phys/D02PhiGammaForD2XGamma/Particles                  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/SlowPiForD2XGamma

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5)                                                                  |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/SlowPiForD2XGamma/Particles                                                  |

CombineParticles/D2XGammaStripping_Dst2D0Pi

|                  |                                                                                        |
|------------------|----------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D02PhiGammaForD2XGamma' , 'Phys/SlowPiForD2XGamma' ]                         |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }          |
| CombinationCut   | ((AM - AM1) \< 1.1\*160.0\*MeV)                                                        |
| MotherCut        | ( (VFASPF(VCHI2/VDOF) \< 25.0) & ((M - M1) \< 160.0\*MeV) & ((M - M1) \> 130.0\*MeV) ) |
| DecayDescriptor  | None                                                                                   |
| DecayDescriptors | [ 'D\*(2010)+ -\> D0 pi+' , 'D\*(2010)- -\> D0 pi-' ]                                |
| Output           | Phys/D2XGammaStripping_Dst2D0Pi/Particles                                              |
