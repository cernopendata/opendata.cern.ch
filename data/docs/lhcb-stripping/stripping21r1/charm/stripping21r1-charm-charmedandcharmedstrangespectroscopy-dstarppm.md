[[stripping21r1 lines]](./stripping21r1-index)

# StrippingCharmedAndCharmedStrangeSpectroscopy_DstarpPm

## Properties:

|                |                                                              |
|----------------|--------------------------------------------------------------|
| OutputLocation | Phys/CharmedAndCharmedStrangeSpectroscopy_DstarpPm/Particles |
| Postscale      | 1.0000000                                                    |
| HLT            | None                                                         |
| Prescale       | 1.0000000                                                    |
| L0DU           | None                                                         |
| ODIN           | None                                                         |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDstarWithD02KPi_Particles

|      |                                                                                                                  |
|------|------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDstarWithD02KPi](./stripping21r1-commonparticles-stdloosedstarwithd02kpi)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyDstar

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((M-MAXTREE('D0'==ABSID,M)\<160\*MeV) & (PT\>2.5\*GeV) & (VFASPF(VCHI2/VDOF)\<20) & CHILDCUT( (PT\>150\*MeV) & (P\>1\*GeV) & (MIPCHI2DV(PRIMARY)\<16.0) , 1 ) & CHILDCUT( (BPVDIRA \> 0.999) & (VFASPF(VCHI2/VDOF)\<10) & (PT\>2.\*GeV) & (BPVVDCHI2 \> 25) & (ADMASS('D0')\<100\*MeV), 2 ) & CHILDCUT( CHILDCUT((PT\>250\*MeV) & (P\>2.5\*GeV) & (P \< 100\*GeV) & (TRPCHI2\>0.0001) & (HASRICH),1) & CHILDCUT((PT\>250\*MeV) & (P\>2.5\*GeV) & (P \< 100\*GeV) & (TRPCHI2\>0.0001) & (HASRICH),2),2)) |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21r1-commonparticles-stdloosedstarwithd02kpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyDstar/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                |

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

CombineParticles/CharmedAndCharmedStrangeSpectroscopy_DstarpPm

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmedAndCharmedStrangeSpectroscopyDstar' , 'Phys/CharmedAndCharmedStrangeSpectroscopyP' ]   |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }             |
| CombinationCut   | ATRUE                                                                                                   |
| MotherCut        | (M \> 0.0\*GeV) & ~INTREE( (HASTRACK)&(THASINFO( LHCb.Track.CloneDist )) ) & (M\<3.6\*GeV) & (LV02\>0.) |
| DecayDescriptor  | [Lambda_c(2625)+ -\> D\*(2010)+ p~-]cc                                                                |
| DecayDescriptors | [ '[Lambda_c(2625)+ -\> D\*(2010)+ p~-]cc' ]                                                        |
| Output           | Phys/CharmedAndCharmedStrangeSpectroscopy_DstarpPm/Particles                                            |
