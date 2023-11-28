[[stripping21 lines]](./stripping21-index)

# StrippingCcbar2PhiPiPiDetachedLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/Ccbar2PhiPiPiDetachedLine/Particles |
| Postscale      | 1.0000000                                |
| HLT            | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

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

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionForCcbar2Phi

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT\>0.7\*GeV) & (TRCHI2DOF\<5) & (MIPCHI2DV(PRIMARY)\>36.) & (PIDK\<10)  |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/PionForCcbar2Phi/Particles                                           |

CombineParticles/Ccbar2PhiPiPiDetachedLine

|                  |                                                                                                                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedPhiForCcbar2Phi' , 'Phys/PionForCcbar2Phi' ]                                                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : " \n (INTREE( (ID=='K+') & (PT\>500\*MeV) & (TRCHI2DOF\<5) & (MIPCHI2DV(PRIMARY)\>25.) & (PIDK\>5)))\n & (INTREE( (ID=='K-') & (PT\>500\*MeV) & (TRCHI2DOF\<5) & (MIPCHI2DV(PRIMARY)\>25.) & (PIDK\>5)))\n " , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | AM\>2.65\*GeV                                                                                                                                                                                                                                                               |
| MotherCut        | (MM\>2.7\*GeV) & (VFASPF(VCHI2PDOF)\<16) & (BPVDLS\>10)                                                                                                                                                                                                                     |
| DecayDescriptor  | J/psi(1S) -\> phi(1020) pi+ pi-                                                                                                                                                                                                                                             |
| DecayDescriptors | [ ' J/psi(1S) -\> phi(1020) pi+ pi-' ]                                                                                                                                                                                                                                    |
| Output           | Phys/Ccbar2PhiPiPiDetachedLine/Particles                                                                                                                                                                                                                                    |
