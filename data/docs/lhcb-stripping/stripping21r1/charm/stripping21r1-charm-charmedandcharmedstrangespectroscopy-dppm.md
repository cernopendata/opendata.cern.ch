[[stripping21r1 lines]](./stripping21r1-index)

# StrippingCharmedAndCharmedStrangeSpectroscopy_DpPm

## Properties:

|                |                                                          |
|----------------|----------------------------------------------------------|
| OutputLocation | Phys/CharmedAndCharmedStrangeSpectroscopy_DpPm/Particles |
| Postscale      | 1.0000000                                                |
| HLT            | None                                                     |
| Prescale       | 1.0000000                                                |
| L0DU           | None                                                     |
| ODIN           | None                                                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDplus2KPiPi_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDplus2KPiPi](./stripping21r1-commonparticles-stdloosedplus2kpipi)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyDplus

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((BPVDIRA \> 0.99999) & (MIPCHI2DV(PRIMARY) \< 16) & (BPVVDCHI2 \> 25) & (VFASPF(VCHI2/VDOF)\<8) & (PT \> 2.5\*GeV) & ((CHILDCUT(MIPCHI2DV(PRIMARY) \> 25.0, 1)) \| (CHILDCUT(MIPCHI2DV(PRIMARY) \> 25.0,2)) \| (CHILDCUT(MIPCHI2DV(PRIMARY) \> 25.0,3))) & ((CHILDCUT(PT \> 0.6\*GeV,1) & CHILDCUT(PT \> 0.6\*GeV,2)) \| (CHILDCUT(PT \> 0.6\*GeV,3) & CHILDCUT(PT \> 0.6\*GeV,2)) \| (CHILDCUT(PT \> 0.6\*GeV,3) & CHILDCUT(PT \> 0.6\*GeV,1)))& CHILDCUT((PT \> 250\*MeV) & (P \> 3\*GeV) & (P \< 100\*GeV) & (TRPCHI2 \> 0.0001) & (HASRICH),1) & CHILDCUT((PT \> 250\*MeV) & (P \> 3\*GeV) & (P \< 100\*GeV) & (TRPCHI2 \> 0.0001) & (HASRICH),2) & CHILDCUT((PT \> 250\*MeV) & (P \> 3\*GeV) & (P \< 100\*GeV) & (TRPCHI2 \> 0.0001) & (HASRICH),3)) |
| Inputs          | [ 'Phys/[StdLooseDplus2KPiPi](./stripping21r1-commonparticles-stdloosedplus2kpipi)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyDplus/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

LoKi::VoidFilter/SelFilterPhys_StdTightProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightProtons](./stripping21r1-commonparticles-stdtightprotons)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyP

|                 |                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------|
| Code            | (ISLONG) & (PT\>500\*MeV) & (P\>3\*GeV) & (MIPCHI2DV(PRIMARY)\<16.0) & (TRPCHI2\>0.0001) & (HASRICH) |
| Inputs          | [ 'Phys/[StdTightProtons](./stripping21r1-commonparticles-stdtightprotons)' ]                      |
| DecayDescriptor | None                                                                                                 |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyP/Particles                                                 |

CombineParticles/CharmedAndCharmedStrangeSpectroscopy_DpPm

|                  |                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmedAndCharmedStrangeSpectroscopyDplus' , 'Phys/CharmedAndCharmedStrangeSpectroscopyP' ]  |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                            |
| CombinationCut   | ATRUE                                                                                                  |
| MotherCut        | (M \> 0.0\*GeV) & ~INTREE( (HASTRACK)&(THASINFO( LHCb.Track.CloneDist )) ) & (LV02\>0.0) & (M\<4\*GeV) |
| DecayDescriptor  | [Lambda_c(2625)+ -\> D+ p~-]cc                                                                       |
| DecayDescriptors | [ '[Lambda_c(2625)+ -\> D+ p~-]cc' ]                                                               |
| Output           | Phys/CharmedAndCharmedStrangeSpectroscopy_DpPm/Particles                                               |
