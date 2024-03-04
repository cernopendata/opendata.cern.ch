[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBs2MuMusBu2JPsiKLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/Bs2MuMusBu2JPsiKLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

CombineParticles/Bs2MuMusBu2JPsiKSelJpsi

|                  |                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 25.)' , 'mu-' : '(TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 25.)' } |
| CombinationCut   | (ADAMASS('J/psi(1S)')\<100\*MeV) & (AMAXDOCA('')\<0.3\*mm)                                                                           |
| MotherCut        | (VFASPF(VCHI2)\<9) & (ADMASS('J/psi(1S)') \< 100\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 121)                                          |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                                |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                        |
| Output           | Phys/Bs2MuMusBu2JPsiKSelJpsi/Particles                                                                                               |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21r1-commonparticles-stdnopidskaons)/Particles')\>0 |

CombineParticles/Bs2MuMusBu2JPsiKLine

|                  |                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2MuMusBu2JPsiKSelJpsi' , 'Phys/[StdNoPIDsKaons](./stripping21r1-commonparticles-stdnopidskaons)' ]                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : '(ISLONG) & (TRCHI2DOF \< 3 ) &(MIPCHI2DV(PRIMARY)\>9)& (PT\>250\*MeV) ' , 'K-' : '(ISLONG) & (TRCHI2DOF \< 3 ) &(MIPCHI2DV(PRIMARY)\>9)& (PT\>250\*MeV) ' } |
| CombinationCut   | (ADAMASS('B+') \< 500\*MeV)                                                                                                                                                                              |
| MotherCut        | (BPVIPCHI2()\< 25)& (VFASPF(VCHI2)\<45)                                                                                                                                                                  |
| DecayDescriptor  | [B+ -\> J/psi(1S) K+]cc                                                                                                                                                                                |
| DecayDescriptors | [ ' [B+ -\> J/psi(1S) K+]cc ' ]                                                                                                                                                                      |
| Output           | Phys/Bs2MuMusBu2JPsiKLine/Particles                                                                                                                                                                      |

AddRelatedInfo/RelatedInfo1_Bs2MuMusBu2JPsiKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_Bs2MuMusBu2JPsiKLine/Particles |

AddRelatedInfo/RelatedInfo2_Bs2MuMusBu2JPsiKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_Bs2MuMusBu2JPsiKLine/Particles |

AddRelatedInfo/RelatedInfo3_Bs2MuMusBu2JPsiKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_Bs2MuMusBu2JPsiKLine/Particles |

AddRelatedInfo/RelatedInfo4_Bs2MuMusBu2JPsiKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_Bs2MuMusBu2JPsiKLine/Particles |

AddRelatedInfo/RelatedInfo5_Bs2MuMusBu2JPsiKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo5_Bs2MuMusBu2JPsiKLine/Particles |

AddRelatedInfo/RelatedInfo6_Bs2MuMusBu2JPsiKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo6_Bs2MuMusBu2JPsiKLine/Particles |

AddRelatedInfo/RelatedInfo7_Bs2MuMusBu2JPsiKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo7_Bs2MuMusBu2JPsiKLine/Particles |

AddRelatedInfo/RelatedInfo8_Bs2MuMusBu2JPsiKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBu2JPsiKSelJpsi' ]             |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo8_Bs2MuMusBu2JPsiKLine/Particles |
