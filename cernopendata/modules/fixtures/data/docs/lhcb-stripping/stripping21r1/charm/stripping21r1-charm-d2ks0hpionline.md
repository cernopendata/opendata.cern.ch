[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2KS0HPionLine

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/D2KS0HPionLine/Particles |
| Postscale      | 1.0000000                     |
| HLT            | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/D2KS0HKS0LLForD2KS0H

|                 |                                                                                                                                                                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000\*MeV) & (VFASPF(VCHI2PDOF) \< 10) & CHILDCUT((TRCHI2DOF \< 4),1) & CHILDCUT((TRCHI2DOF \< 4),2) & CHILDCUT((MIPCHI2DV(PRIMARY) \> 40),1) & CHILDCUT((MIPCHI2DV(PRIMARY) \> 40),2) & (MIPCHI2DV(PRIMARY) \> 7) & (BPVVDCHI2\> 300) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)' ]                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                          |
| Output          | Phys/D2KS0HKS0LLForD2KS0H/Particles                                                                                                                                                                                                           |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/D2KS0HBachelorPionsForD2KS0H

|                 |                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------|
| Code            | (PIDK \< 3) & (P \> 2000\*MeV) & (PT \> 200\*MeV) & (TRCHI2DOF \< 3) & (MIPCHI2DV(PRIMARY) \> 15) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]                       |
| DecayDescriptor | None                                                                                              |
| Output          | Phys/D2KS0HBachelorPionsForD2KS0H/Particles                                                       |

CombineParticles/D2KS0HPion

|                  |                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D2KS0HBachelorPionsForD2KS0H' , 'Phys/D2KS0HKS0LLForD2KS0H' ]                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                      |
| CombinationCut   | (APT \> 1000) & (ACUTDOCACHI2(11,'')) & in_range(1760, AM, 2080)                                                                                                                    |
| MotherCut        | (PT \> 1000\*MeV) & (VFASPF(VCHI2PDOF) \< 10) & in_range(1770, MM, 2070) & ((CHILD( VFASPF(VZ) , 'KS0' == ID ) - VFASPF(VZ)) \> 10) & (MIPCHI2DV(PRIMARY) \< 15) & (BPVVDCHI2 \> 5) |
| DecayDescriptor  | [D+ -\> KS0 pi+]cc                                                                                                                                                                |
| DecayDescriptors | [ '[D+ -\> KS0 pi+]cc' ]                                                                                                                                                        |
| Output           | Phys/D2KS0HPion/Particles                                                                                                                                                           |

TisTosParticleTagger/D2KS0HPionLine

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/D2KS0HPion' ]                                                             |
| DecayDescriptor | None                                                                                |
| Output          | Phys/D2KS0HPionLine/Particles                                                       |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 , 'Hlt2CharmHadD2KS0H_D2KS0PiDecision%TOS' : 0 } |
