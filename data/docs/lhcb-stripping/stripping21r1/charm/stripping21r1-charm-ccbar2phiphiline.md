[[stripping21r1 lines]](./stripping21r1-index)

# StrippingCcbar2PhiPhiLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/Ccbar2PhiPhiLine/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdTightPhi2KK_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightPhi2KK](./stripping21r1-commonparticles-stdtightphi2kk)/Particles')\>0 |

FilterDesktop/PhiForCcbar2Phi

|                 |                                                                                                                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (VFASPF(VCHI2/VDOF)\<16.0) & (ADMASS('phi(1020)')\<12.0\*MeV) & (INTREE( ('K+'==ID) & (PT\> 650.0\*MeV) & (TRCHI2DOF \< 5.0) & (PIDK\> 5.0) )) & (INTREE( ('K-'==ID) & (PT\> 650.0\*MeV) & (TRCHI2DOF \< 5.0) & (PIDK\> 5.0) )) |
| Inputs          | [ 'Phys/[StdTightPhi2KK](./stripping21r1-commonparticles-stdtightphi2kk)' ]                                                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                                            |
| Output          | Phys/PhiForCcbar2Phi/Particles                                                                                                                                                                                                  |

TisTosParticleTagger/TisPhiForCcbar2Phi_SelTisTos

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/PhiForCcbar2Phi' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/TisPhiForCcbar2Phi_SelTisTos/Particles |
| TisTosSpecs     | { 'Hlt1Global%TIS' : 0 }                    |

CombineParticles/Ccbar2PhiPhiLine

|                  |                                                                          |
|------------------|--------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TisPhiForCcbar2Phi_SelTisTos' ]                                |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : 'ALL' }                                     |
| CombinationCut   | (in_range( 2750.0 \*MeV, AM, 4100.0 \*MeV))                              |
| MotherCut        | (in_range( 2800.0 \*MeV, MM, 4000.0 \*MeV)) & (VFASPF(VCHI2PDOF) \< 16 ) |
| DecayDescriptor  | J/psi(1S) -\> phi(1020) phi(1020)                                        |
| DecayDescriptors | [ ' J/psi(1S) -\> phi(1020) phi(1020)' ]                               |
| Output           | Phys/Ccbar2PhiPhiLine/Particles                                          |
