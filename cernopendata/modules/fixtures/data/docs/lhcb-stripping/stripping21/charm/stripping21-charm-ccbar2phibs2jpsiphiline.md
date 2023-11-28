[[stripping21 lines]](./stripping21-index)

# StrippingCcbar2PhiBs2JpsiPhiLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/Ccbar2PhiBs2JpsiPhiLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseDetachedPhi2KK_Particles

|      |                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDetachedPhi2KK](./stripping21-commonparticles-stdloosedetachedphi2kk)/Particles')\>0 |

FilterDesktop/DetachedPhiForCcbar2Phi

|                 |                                                                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF)\<16.0) & (ADMASS('phi(1020)')\<12.0\*MeV ) & (MAXTREE('K+'==ABSID, TRCHI2DOF) \< 5.0 ) & (MINTREE('K+'==ABSID, PIDK)\>0) |
| Inputs          | [ 'Phys/[StdLooseDetachedPhi2KK](./stripping21-commonparticles-stdloosedetachedphi2kk)' ]                                                  |
| DecayDescriptor | None                                                                                                                                         |
| Output          | Phys/DetachedPhiForCcbar2Phi/Particles                                                                                                       |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KaonForCcbar2Phi

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT\>0.5\*GeV) & (TRCHI2DOF\<5) & (MIPCHI2DV(PRIMARY)\>25.) & (PIDK\>5)   |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/KaonForCcbar2Phi/Particles                                           |

CombineParticles/DetachedJpsi2PhiKKCcbar2Phi

|                  |                                                                                                                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedPhiForCcbar2Phi' , 'Phys/KaonForCcbar2Phi' ]                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'phi(1020)' : "\n (INTREE( (ID=='K+') & (PT\>500\*MeV) & (TRCHI2DOF\<5) & (MIPCHI2DV(PRIMARY)\>25.) & (PIDK\>5)))\n & (INTREE( (ID=='K-') & (PT\>500\*MeV) & (TRCHI2DOF\<5) & (MIPCHI2DV(PRIMARY)\>25.) & (PIDK\>5)))\n " } |
| CombinationCut   | AM\>2.65\*GeV                                                                                                                                                                                                                                                            |
| MotherCut        | (MM\>2.7\*GeV) & (VFASPF(VCHI2PDOF)\<16) & (BPVDLS\>10)                                                                                                                                                                                                                  |
| DecayDescriptor  | J/psi(1S) -\> phi(1020) K+ K-                                                                                                                                                                                                                                            |
| DecayDescriptors | [ ' J/psi(1S) -\> phi(1020) K+ K-' ]                                                                                                                                                                                                                                   |
| Output           | Phys/DetachedJpsi2PhiKKCcbar2Phi/Particles                                                                                                                                                                                                                               |

CombineParticles/Ccbar2PhiBs2JpsiPhiLine

|                  |                                                                           |
|------------------|---------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedJpsi2PhiKKCcbar2Phi' , 'Phys/DetachedPhiForCcbar2Phi' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'phi(1020)' : 'ALL' }                |
| CombinationCut   | AALL                                                                      |
| MotherCut        | (VFASPF(VCHI2PDOF)\<16)                                                   |
| DecayDescriptor  | B_s0 -\> J/psi(1S) phi(1020)                                              |
| DecayDescriptors | [ ' B_s0 -\> J/psi(1S) phi(1020)' ]                                     |
| Output           | Phys/Ccbar2PhiBs2JpsiPhiLine/Particles                                    |
