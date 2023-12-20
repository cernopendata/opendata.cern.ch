[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2EtacKst_Etac2PiPiPiPiB2CharmoniumX_6HLine

## Properties:

|                |                                                            |
|----------------|------------------------------------------------------------|
| OutputLocation | Phys/B2EtacKst_Etac2PiPiPiPiB2CharmoniumX_6HLine/Particles |
| Postscale      | 1.0000000                                                  |
| HLT            | HLT_PASS_RE('Hlt2.\*Topo.\*Decision')                      |
| Prescale       | 1.0000000                                                  |
| L0DU           | None                                                       |
| ODIN           | None                                                       |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNKaons](./stripping21r1-commonparticles-stdlooseannkaons)/Particles')\>0 |

FilterDesktop/KaonForB2CharmoniumX_6H

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3.0) & (PT \> 250.0 \*MeV)& (MIPCHI2DV(PRIMARY) \> 4.0)             |
| Inputs          | [ 'Phys/[StdLooseANNKaons](./stripping21r1-commonparticles-stdlooseannkaons)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/KaonForB2CharmoniumX_6H/Particles                                            |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNPions](./stripping21r1-commonparticles-stdlooseannpions)/Particles')\>0 |

FilterDesktop/PionForB2CharmoniumX_6H

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3.0) & (PT \> 250.0 \*MeV)& (MIPCHI2DV(PRIMARY) \> 4.0)             |
| Inputs          | [ 'Phys/[StdLooseANNPions](./stripping21r1-commonparticles-stdlooseannpions)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/PionForB2CharmoniumX_6H/Particles                                            |

CombineParticles/Kst2KPiForB2CharmoniumX_6H

|                  |                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonForB2CharmoniumX_6H' , 'Phys/PionForB2CharmoniumX_6H' ]                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                         |
| CombinationCut   | (ADAMASS('K\*(892)0') \< 100.0 \*MeV) & (APT \> 1000.0)                                              |
| MotherCut        | (VFASPF(VZ) \> 0.0 \*mm) & (BPVDIRA \> 0.93) & (MIPCHI2DV(PRIMARY) \> 4.0) & (VFASPF(VCHI2) \< 12.0) |
| DecayDescriptor  | [K\*(892)0 -\> K+ pi-]cc                                                                           |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                                                   |
| Output           | Phys/Kst2KPiForB2CharmoniumX_6H/Particles                                                            |

CombineParticles/Etac2PiPiPiPiForB2CharmoniumX_6H

|                  |                                                                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionForB2CharmoniumX_6H' ]                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                  |
| CombinationCut   | (ADAMASS('eta_c(1S)') \< 90.0 \*MeV) & (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) \> 4000.0 \*MeV) & (AMAXDOCA('') \< 0.1) & (AMAXCHILD(MAXTREE(((ABSID=='pi+') \| (ABSID=='K+')),PT)) \> 1400.0) & (AMAXCHILD(MAXTREE(((ABSID=='pi+') \| (ABSID=='K+')),MIPCHI2DV(PRIMARY))) \> 9.0) |
| MotherCut        | (BPVDIRA\> 0.9) & (MIPCHI2DV(PRIMARY) \> 4.0) & (VFASPF(VCHI2/VDOF) \< 9.0)                                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'eta_c(1S) -\> pi+ pi- pi+ pi-' ]                                                                                                                                                                                                                                                           |
| Output           | Phys/Etac2PiPiPiPiForB2CharmoniumX_6H/Particles                                                                                                                                                                                                                                                 |

CombineParticles/B2EtacKst_Etac2PiPiPiPiB2CharmoniumX_6HLine

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Etac2PiPiPiPiForB2CharmoniumX_6H' , 'Phys/Kst2KPiForB2CharmoniumX_6H' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'eta_c(1S)' : 'ALL' } |
| CombinationCut   | (ADAMASS('B0') \< 500 \*MeV)                                                      |
| MotherCut        | (VFASPF(VZ) \> 0.0 \*mm) & (BPVDIRA\> 0.9) & (VFASPF(VCHI2/VDOF) \< 25.0)         |
| DecayDescriptor  | None                                                                              |
| DecayDescriptors | [ 'B0 -\> eta_c(1S) K\*(892)0' ]                                                |
| Output           | Phys/B2EtacKst_Etac2PiPiPiPiB2CharmoniumX_6HLine/Particles                        |
