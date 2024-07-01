[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBs2EtacPhi_Etac2KKKKB2CharmoniumX_6HLine

## Properties:

|                |                                                         |
|----------------|---------------------------------------------------------|
| OutputLocation | Phys/Bs2EtacPhi_Etac2KKKKB2CharmoniumX_6HLine/Particles |
| Postscale      | 1.0000000                                               |
| HLT            | HLT_PASS_RE('Hlt2.\*Topo.\*Decision')                   |
| Prescale       | 1.0000000                                               |
| L0DU           | None                                                    |
| ODIN           | None                                                    |

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

CombineParticles/Etac2KKKKForB2CharmoniumX_6H

|                  |                                                                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonForB2CharmoniumX_6H' ]                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                                                                                                                                                                                                                    |
| CombinationCut   | (ADAMASS('eta_c(1S)') \< 90.0 \*MeV) & (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) \> 4000.0 \*MeV) & (AMAXDOCA('') \< 0.1) & (AMAXCHILD(MAXTREE(((ABSID=='pi+') \| (ABSID=='K+')),PT)) \> 1400.0) & (AMAXCHILD(MAXTREE(((ABSID=='pi+') \| (ABSID=='K+')),MIPCHI2DV(PRIMARY))) \> 9.0) |
| MotherCut        | (BPVDIRA\> 0.9) & (MIPCHI2DV(PRIMARY) \> 4.0) & (VFASPF(VCHI2/VDOF) \< 9.0)                                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'eta_c(1S) -\> K+ K- K+ K-' ]                                                                                                                                                                                                                                                               |
| Output           | Phys/Etac2KKKKForB2CharmoniumX_6H/Particles                                                                                                                                                                                                                                                     |

CombineParticles/Bs2EtacPhi_Etac2KKKKB2CharmoniumX_6HLine

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Etac2KKKKForB2CharmoniumX_6H' , 'Phys/Phi2KKForB2CharmoniumX_6H' ] |
| DaughtersCuts    | { '' : 'ALL' , 'eta_c(1S)' : 'ALL' , 'phi(1020)' : 'ALL' }                   |
| CombinationCut   | (ADAMASS('B_s0') \< 500 \*MeV)                                               |
| MotherCut        | (VFASPF(VZ) \> 0.0 \*mm) & (BPVDIRA\> 0.9) & (VFASPF(VCHI2/VDOF) \< 25.0)    |
| DecayDescriptor  | None                                                                         |
| DecayDescriptors | [ 'B_s0 -\> eta_c(1S) phi(1020)' ]                                         |
| Output           | Phys/Bs2EtacPhi_Etac2KKKKB2CharmoniumX_6HLine/Particles                      |
