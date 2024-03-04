[[stripping21 lines]](./stripping21-index)

# StrippingCharmedAndCharmedStrangeSpectroscopy_DstarpKs

## Properties:

|                |                                                              |
|----------------|--------------------------------------------------------------|
| OutputLocation | Phys/CharmedAndCharmedStrangeSpectroscopy_DstarpKs/Particles |
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

|      |                                                                                                                |
|------|----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDstarWithD02KPi](./stripping21-commonparticles-stdloosedstarwithd02kpi)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyDstar

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((M-MAXTREE('D0'==ABSID,M)\<160\*MeV) & (PT\>2.5\*GeV) & (VFASPF(VCHI2/VDOF)\<20) & CHILDCUT( (PT\>150\*MeV) & (P\>1\*GeV) & (MIPCHI2DV(PRIMARY)\<16.0) , 1 ) & CHILDCUT( (BPVDIRA \> 0.999) & (VFASPF(VCHI2/VDOF)\<10) & (PT\>2.\*GeV) & (BPVVDCHI2 \> 25) & (ADMASS('D0')\<100\*MeV), 2 ) & CHILDCUT( CHILDCUT((PT\>250\*MeV) & (P\>2.5\*GeV) & (P \< 100\*GeV) & (TRPCHI2\>0.0001) & (HASRICH),1) & CHILDCUT((PT\>250\*MeV) & (P\>2.5\*GeV) & (P \< 100\*GeV) & (TRPCHI2\>0.0001) & (HASRICH),2),2)) |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21-commonparticles-stdloosedstarwithd02kpi)' ]                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyDstar/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                |

GaudiSequencer/SeqCharmedAndCharmedStrangeSpectroscopyKS0

GaudiSequencer/SEQ:CharmedAndCharmedStrangeSpectroscopyKSLongLong

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyKSLongLong

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((BPVVDZ \> -20 \*cm) & (BPVVDZ \< 65 \*cm) & (BPVVD \> 1.5\*cm) & (BPVDIRA \> 0.9999) & (CHILDIP(1) \< 0.5\*mm) & (CHILDIP(2) \< 0.5 \*mm) & (VFASPF(VPCHI2) \> 0.1\*perCent)& CHILDCUT((TRPCHI2 \> 0.0001) & (PT \> 250\*MeV) & (P \< 100\*GeV) & (MIPDV(PRIMARY) \> 0.5\*mm) & (HASRICH), 1) & CHILDCUT((TRPCHI2 \> 0.0001) & (PT \> 250\*MeV) & (P \< 100\*GeV) & (MIPDV(PRIMARY) \> 0.5\*mm) & (HASRICH), 2) ) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ]                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/CharmedAndCharmedStrangeSpectroscopyKSLongLong/Particles                                                                                                                                                                                                                                                                                                                                                       |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:CharmedAndCharmedStrangeSpectroscopyKSDownDown

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

FilterDesktop/CharmedAndCharmedStrangeSpectroscopyKSDownDown

|                 |                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ((BPVVDZ \> 0.0\*cm) & (BPVVDZ \< 230.0\*cm) & (BPVVD \> 20.0\*cm) & (BPVDIRA \> 0.9999) & (CHILDIP(1) \< 6.0\*mm) & (CHILDIP(2) \< 6.0 \*mm)& CHILDCUT((TRPCHI2 \> 0.0001) & (PT \> 250\*MeV) & (P \< 100\*GeV) & (MIPDV(PRIMARY) \> 0.5\*mm) & (HASRICH), 1) & CHILDCUT((TRPCHI2 \> 0.0001) & (PT \> 250\*MeV) & (P \< 100\*GeV) & (MIPDV(PRIMARY) \> 0.5\*mm) & (HASRICH), 2) ) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' ]                                                                                                                                                                                                                                                                                                            |
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

CombineParticles/CharmedAndCharmedStrangeSpectroscopy_DstarpKs

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/CharmedAndCharmedStrangeSpectroscopyDstar' , 'Phys/CharmedAndCharmedStrangeSpectroscopyKS0' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'KS0' : 'ALL' }                            |
| CombinationCut   | ATRUE                                                                                                   |
| MotherCut        | (M \> 0.0\*GeV) & ~INTREE( (HASTRACK)&(THASINFO( LHCb.Track.CloneDist )) )                              |
| DecayDescriptor  | [D_s1(2536)+ -\> D\*(2010)+ KS0]cc                                                                    |
| DecayDescriptors | [ '[D_s1(2536)+ -\> D\*(2010)+ KS0]cc' ]                                                            |
| Output           | Phys/CharmedAndCharmedStrangeSpectroscopy_DstarpKs/Particles                                            |
