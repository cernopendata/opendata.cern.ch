[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBs2MuMusBd2JPsiKstLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/Bs2MuMusBd2JPsiKstLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

CombineParticles/Bs2MuMusBd2JPsiKstSelJpsi

|                  |                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 25.)' , 'mu-' : '(TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 25.)' } |
| CombinationCut   | (ADAMASS('J/psi(1S)')\<100\*MeV) & (AMAXDOCA('')\<0.3\*mm)                                                                           |
| MotherCut        | (VFASPF(VCHI2)\<9) & (ADMASS('J/psi(1S)') \< 100\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 121)                                          |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                                |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                        |
| Output           | Phys/Bs2MuMusBd2JPsiKstSelJpsi/Particles                                                                                             |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21r1-commonparticles-stdnopidskaons)/Particles')\>0 |

CombineParticles/Bs2MuMusBd2JPsiKstSelKst

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsKaons](./stripping21r1-commonparticles-stdnopidskaons)' , 'Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)' ]                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(ISLONG) & (TRCHI2DOF \< 3 ) & ( TRGHOSTPROB \< 0.3 ) & (MIPCHI2DV(PRIMARY)\> 4.)& (PT\>250\*MeV)' , 'K-' : '(ISLONG) & (TRCHI2DOF \< 3 ) & ( TRGHOSTPROB \< 0.3 ) & (MIPCHI2DV(PRIMARY)\> 4.)& (PT\>250\*MeV)' , 'pi+' : '(ISLONG) & (TRCHI2DOF \< 3 ) & ( TRGHOSTPROB \< 0.3 )& (MIPCHI2DV(PRIMARY)\> 4.)& (PT\>250\*MeV)' , 'pi-' : '(ISLONG) & (TRCHI2DOF \< 3 ) & ( TRGHOSTPROB \< 0.3 )& (MIPCHI2DV(PRIMARY)\> 4.)& (PT\>250\*MeV)' } |
| CombinationCut   | (ADAMASS('K\*(892)0')\<2000\*MeV)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | (MIPCHI2DV(PRIMARY)\> 9)                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptor  | [K\*(892)0 -\> K+ pi-]cc                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/Bs2MuMusBd2JPsiKstSelKst/Particles                                                                                                                                                                                                                                                                                                                                                                                                                            |

CombineParticles/Bs2MuMusBd2JPsiKstLine

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2MuMusBd2JPsiKstSelJpsi' , 'Phys/Bs2MuMusBd2JPsiKstSelKst' ]          |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' } |
| CombinationCut   | (ADAMASS('B0') \< 500\*MeV)                                                       |
| MotherCut        | (BPVIPCHI2()\< 25) & (VFASPF(VCHI2)\<75)                                          |
| DecayDescriptor  | [B0 -\> J/psi(1S) K\*(892)0]cc                                                  |
| DecayDescriptors | [ '[B0 -\> J/psi(1S) K\*(892)0]cc' ]                                          |
| Output           | Phys/Bs2MuMusBd2JPsiKstLine/Particles                                             |

AddRelatedInfo/RelatedInfo1_Bs2MuMusBd2JPsiKstLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_Bs2MuMusBd2JPsiKstLine/Particles |

AddRelatedInfo/RelatedInfo2_Bs2MuMusBd2JPsiKstLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_Bs2MuMusBd2JPsiKstLine/Particles |

AddRelatedInfo/RelatedInfo3_Bs2MuMusBd2JPsiKstLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_Bs2MuMusBd2JPsiKstLine/Particles |

AddRelatedInfo/RelatedInfo4_Bs2MuMusBd2JPsiKstLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_Bs2MuMusBd2JPsiKstLine/Particles |

AddRelatedInfo/RelatedInfo5_Bs2MuMusBd2JPsiKstLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo5_Bs2MuMusBd2JPsiKstLine/Particles |

AddRelatedInfo/RelatedInfo6_Bs2MuMusBd2JPsiKstLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo6_Bs2MuMusBd2JPsiKstLine/Particles |

AddRelatedInfo/RelatedInfo7_Bs2MuMusBd2JPsiKstLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo7_Bs2MuMusBd2JPsiKstLine/Particles |

AddRelatedInfo/RelatedInfo8_Bs2MuMusBd2JPsiKstLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBd2JPsiKstSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo8_Bs2MuMusBd2JPsiKstLine/Particles |
