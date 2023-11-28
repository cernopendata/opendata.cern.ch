[[stripping21 lines]](./stripping21-index)

# StrippingCcbar2PhiBs2TriPhiLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/Ccbar2PhiBs2TriPhiLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

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

CombineParticles/Ccbar2PhiBs2TriPhiLine

|                  |                                                 |
|------------------|-------------------------------------------------|
| Inputs           | [ 'Phys/DetachedPhiForCcbar2Phi' ]            |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : 'ALL' }            |
| CombinationCut   | AM\>2.65\*GeV                                   |
| MotherCut        | (MM\>2.7\*GeV) & (VFASPF(VCHI2PDOF)\<16)        |
| DecayDescriptor  | B_s0 -\> phi(1020) phi(1020) phi(1020)          |
| DecayDescriptors | [ ' B_s0 -\> phi(1020) phi(1020) phi(1020)' ] |
| Output           | Phys/Ccbar2PhiBs2TriPhiLine/Particles           |
