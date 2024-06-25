[[stripping21r1 lines]](./stripping21r1-index)

# StrippingCharmedAndCharmedStrangeSpectroscopy_DzPWS

## Properties:

|                |                                                           |
|----------------|-----------------------------------------------------------|
| OutputLocation | Phys/CharmedAndCharmedStrangeSpectroscopy_DzPWS/Particles |
| Postscale      | 1.0000000                                                 |
| HLT            | None                                                      |
| Prescale       | 1.0000000                                                 |
| L0DU           | None                                                      |
| ODIN           | None                                                      |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseD02KPi_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseD02KPi](./stripping21r1-commonparticles-stdloosed02kpi)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyD0

|                 |                                                                                                                                                                                                                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CHILDCUT((PT\>250\*MeV) & (P\>3\*GeV) & (P \< 100\*GeV) & (TRPCHI2\>0.0001) & (HASRICH),1) & CHILDCUT((PT\>250\*MeV) & (P\>3\*GeV) & (P \< 100\*GeV) & (TRPCHI2\>0.0001) & (HASRICH),2) & (BPVDIRA \> 0.99999) & (VFASPF(VCHI2/VDOF)\<8) & (PT\>2.\*GeV) & (ADMASS('D0')\<100\*MeV) & (MIPCHI2DV(PRIMARY) \< 16.0) & (BPVVDCHI2 \> 25)) |
| Inputs          | [ 'Phys/[StdLooseD02KPi](./stripping21r1-commonparticles-stdloosed02kpi)' ]                                                                                                                                                                                                                                                            |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                     |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyD0/Particles                                                                                                                                                                                                                                                                                    |

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

CombineParticles/CharmedAndCharmedStrangeSpectroscopy_DzPWS

|                  |                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmedAndCharmedStrangeSpectroscopyD0' , 'Phys/CharmedAndCharmedStrangeSpectroscopyP' ]     |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                           |
| CombinationCut   | ATRUE                                                                                                  |
| MotherCut        | (M \> 0.0\*GeV) & ~INTREE( (HASTRACK)&(THASINFO( LHCb.Track.CloneDist )) ) & (LV02\>0.0) & (M\<4\*GeV) |
| DecayDescriptor  | [Lambda_c(2625)+ -\> D0 p~-]cc                                                                       |
| DecayDescriptors | [ '[Lambda_c(2625)+ -\> D0 p~-]cc' ]                                                               |
| Output           | Phys/CharmedAndCharmedStrangeSpectroscopy_DzPWS/Particles                                              |
