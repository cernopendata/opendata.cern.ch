[[stripping21 lines]](./stripping21-index)

# StrippingX2D0D0Line

## Properties:

|                |                           |
|----------------|---------------------------|
| OutputLocation | Phys/X2D0D0Line/Particles |
| Postscale      | 1.0000000                 |
| HLT            | None                      |
| Prescale       | 1.0000000                 |
| L0DU           | None                      |
| ODIN           | None                      |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseKaons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/D0ForX2D0D0

|                  |                                                                                                                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\> 900.0) & (P\>5000.0) & (TRCHI2DOF \< 5.0)&(PIDK\>8.0)' , 'K-' : '(PT\> 900.0) & (P\>5000.0) & (TRCHI2DOF \< 5.0)&(PIDK\>8.0)' , 'pi+' : '(PT\> 900.0) & (P\>5000.0) & (TRCHI2DOF \< 5.0)&(PIDK\<0.0)' , 'pi-' : '(PT\> 900.0) & (P\>5000.0) & (TRCHI2DOF \< 5.0)&(PIDK\<0.0)' } |
| CombinationCut   | ATRUE                                                                                                                                                                                                                                                                                                        |
| MotherCut        | (ADMASS('D0')\<60.0) & (PT\> 3300.0) & (VFASPF(VCHI2PDOF) \< 8.0)                                                                                                                                                                                                                                            |
| DecayDescriptor  | [D0 -\> K- pi+]cc                                                                                                                                                                                                                                                                                          |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                                                                                                                                                                                                                                  |
| Output           | Phys/D0ForX2D0D0/Particles                                                                                                                                                                                                                                                                                   |

CombineParticles/X2D0D0Line

|                  |                                                  |
|------------------|--------------------------------------------------|
| Inputs           | [ 'Phys/D0ForX2D0D0' ]                         |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' }    |
| CombinationCut   | ATRUE                                            |
| MotherCut        | (ADMASS('B_s0')\>0.0)                            |
| DecayDescriptor  | None                                             |
| DecayDescriptors | [ 'B_s0 -\> D0 D~0' , '[B_s0 -\> D0 D0]cc' ] |
| Output           | Phys/X2D0D0Line/Particles                        |
