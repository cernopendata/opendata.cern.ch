[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLFVBu2KJPsieeLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/LFVBu2KJPsieeLine/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseElectrons](./stripping21r1-commonparticles-stdlooseelectrons)/Particles')\>0 |

CombineParticles/LFVBu2KJPsiee

|                  |                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseElectrons](./stripping21r1-commonparticles-stdlooseelectrons)' ]                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 25.) & (PIDe \> 2) ' , 'e-' : '(TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 25.) & (PIDe \> 2) ' } |
| CombinationCut   | (ADAMASS('J/psi(1S)')\<1000\*MeV) & (AMAXDOCA('')\<0.3\*mm)                                                                                                      |
| MotherCut        | (VFASPF(VCHI2)\<9) & (ADMASS('J/psi(1S)') \< 1000\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\>169)                                                                      |
| DecayDescriptor  | J/psi(1S) -\> e+ e-                                                                                                                                              |
| DecayDescriptors | [ 'J/psi(1S) -\> e+ e-' ]                                                                                                                                      |
| Output           | Phys/LFVBu2KJPsiee/Particles                                                                                                                                     |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21r1-commonparticles-stdnopidskaons)/Particles')\>0 |

CombineParticles/LFVBu2KJPsieeLine

|                  |                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/LFVBu2KJPsiee' , 'Phys/[StdNoPIDsKaons](./stripping21r1-commonparticles-stdnopidskaons)' ]                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : '(ISLONG) & (TRCHI2DOF \< 3 ) &(MIPCHI2DV(PRIMARY)\>25)& (PT\>250\*MeV) & (TRGHOSTPROB\<0.3) ' , 'K-' : '(ISLONG) & (TRCHI2DOF \< 3 ) &(MIPCHI2DV(PRIMARY)\>25)& (PT\>250\*MeV) & (TRGHOSTPROB\<0.3) ' } |
| CombinationCut   | (ADAMASS('B+') \< 600\*MeV)                                                                                                                                                                                                                          |
| MotherCut        | (BPVIPCHI2()\< 25)& (VFASPF(VCHI2)\<45)                                                                                                                                                                                                              |
| DecayDescriptor  | [B+ -\> J/psi(1S) K+]cc                                                                                                                                                                                                                            |
| DecayDescriptors | [ ' [B+ -\> J/psi(1S) K+]cc ' ]                                                                                                                                                                                                                  |
| Output           | Phys/LFVBu2KJPsieeLine/Particles                                                                                                                                                                                                                     |
