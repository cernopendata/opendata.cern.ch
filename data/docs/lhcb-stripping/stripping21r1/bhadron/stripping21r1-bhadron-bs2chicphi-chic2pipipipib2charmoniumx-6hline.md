[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBs2ChicPhi_Chic2PiPiPiPiB2CharmoniumX_6HLine

## Properties:

|                |                                                             |
|----------------|-------------------------------------------------------------|
| OutputLocation | Phys/Bs2ChicPhi_Chic2PiPiPiPiB2CharmoniumX_6HLine/Particles |
| Postscale      | 1.0000000                                                   |
| HLT            | HLT_PASS_RE('Hlt2.\*Topo.\*Decision')                       |
| Prescale       | 1.0000000                                                   |
| L0DU           | None                                                        |
| ODIN           | None                                                        |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePhi2KK](./stripping21r1-commonparticles-stdloosephi2kk)/Particles')\>0 |

FilterDesktop/Phi2KKForB2CharmoniumX_6H

|                 |                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('phi(1020)') \< 30.0 \*MeV) & (PT\> 1000.0) & (MIPCHI2DV(PRIMARY) \> 6.0) & (VFASPF(VCHI2) \< 7.0) & (BPVDIRA \> 0.95) |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21r1-commonparticles-stdloosephi2kk)' ]                                                  |
| DecayDescriptor | None                                                                                                                           |
| Output          | Phys/Phi2KKForB2CharmoniumX_6H/Particles                                                                                       |

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

CombineParticles/Chic2PiPiPiPiForB2CharmoniumX_6H

|                  |                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionForB2CharmoniumX_6H' ]                                                                                                                                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                                                                                                   |
| CombinationCut   | (ADAMASS('chi_c0(1P)') \< 60.0 \*MeV) & (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) \> 3600.0 \*MeV) & (AMAXDOCA('') \< 0.1) & (AMAXCHILD(MAXTREE(((ABSID=='pi+') \| (ABSID=='K+')),PT)) \> 1300.0) & (AMAXCHILD(MAXTREE(((ABSID=='pi+') \| (ABSID=='K+')),MIPCHI2DV(PRIMARY))) \> 9.0) |
| MotherCut        | (BPVDIRA\> 0.9) & (MIPCHI2DV(PRIMARY) \> 4.0) & (VFASPF(VCHI2/VDOF) \< 9.0)                                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ 'chi_c0(1P) -\> pi+ pi- pi+ pi-' ]                                                                                                                                                                                                                                                           |
| Output           | Phys/Chic2PiPiPiPiForB2CharmoniumX_6H/Particles                                                                                                                                                                                                                                                  |

CombineParticles/Bs2ChicPhi_Chic2PiPiPiPiB2CharmoniumX_6HLine

|                  |                                                                                  |
|------------------|----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Chic2PiPiPiPiForB2CharmoniumX_6H' , 'Phys/Phi2KKForB2CharmoniumX_6H' ] |
| DaughtersCuts    | { '' : 'ALL' , 'chi_c0(1P)' : 'ALL' , 'phi(1020)' : 'ALL' }                      |
| CombinationCut   | (ADAMASS('B_s0') \< 500 \*MeV)                                                   |
| MotherCut        | (VFASPF(VZ) \> 0.0 \*mm) & (BPVDIRA\> 0.9) & (VFASPF(VCHI2/VDOF) \< 25.0)        |
| DecayDescriptor  | None                                                                             |
| DecayDescriptors | [ 'B_s0 -\> chi_c0(1P) phi(1020)' ]                                            |
| Output           | Phys/Bs2ChicPhi_Chic2PiPiPiPiB2CharmoniumX_6HLine/Particles                      |
