[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBs2MuMusBs2JPsiPhiLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/Bs2MuMusBs2JPsiPhiLine/Particles |
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

CombineParticles/Bs2MuMusBs2JPsiPhiSelJpsi

|                  |                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 25.)' , 'mu-' : '(TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 25.)' } |
| CombinationCut   | (ADAMASS('J/psi(1S)')\<100\*MeV) & (AMAXDOCA('')\<0.3\*mm)                                                                           |
| MotherCut        | (VFASPF(VCHI2)\<9) & (ADMASS('J/psi(1S)') \< 100\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 121)                                          |
| DecayDescriptor  | J/psi(1S) -\> mu+ mu-                                                                                                                |
| DecayDescriptors | [ 'J/psi(1S) -\> mu+ mu-' ]                                                                                                        |
| Output           | Phys/Bs2MuMusBs2JPsiPhiSelJpsi/Particles                                                                                             |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21r1-commonparticles-stdnopidskaons)/Particles')\>0 |

CombineParticles/Bs2MuMusBs2JPsiPhiSelPhi

|                  |                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsKaons](./stripping21r1-commonparticles-stdnopidskaons)' ]                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 4.) & (PT\>250\*MeV)' , 'K-' : '(ISLONG) & (TRCHI2DOF \< 3 ) & (MIPCHI2DV(PRIMARY)\> 4.) & (PT\>250\*MeV)' } |
| CombinationCut   | (ADAMASS('phi(1020)')\<20\*MeV)                                                                                                                                                          |
| MotherCut        | (MIPCHI2DV(PRIMARY)\> 9)                                                                                                                                                                 |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                                                                                                                                      |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                                                                              |
| Output           | Phys/Bs2MuMusBs2JPsiPhiSelPhi/Particles                                                                                                                                                  |

CombineParticles/Bs2MuMusBs2JPsiPhiLine

|                  |                                                                          |
|------------------|--------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bs2MuMusBs2JPsiPhiSelJpsi' , 'Phys/Bs2MuMusBs2JPsiPhiSelPhi' ] |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'phi(1020)' : 'ALL' }               |
| CombinationCut   | (ADAMASS('B_s0') \< 500\*MeV)                                            |
| MotherCut        | (BPVIPCHI2()\< 25)& (VFASPF(VCHI2)\<75)                                  |
| DecayDescriptor  | B_s0 -\> J/psi(1S) phi(1020)                                             |
| DecayDescriptors | [ 'B_s0 -\> J/psi(1S) phi(1020)' ]                                     |
| Output           | Phys/Bs2MuMusBs2JPsiPhiLine/Particles                                    |

AddRelatedInfo/RelatedInfo1_Bs2MuMusBs2JPsiPhiLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_Bs2MuMusBs2JPsiPhiLine/Particles |

AddRelatedInfo/RelatedInfo2_Bs2MuMusBs2JPsiPhiLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_Bs2MuMusBs2JPsiPhiLine/Particles |

AddRelatedInfo/RelatedInfo3_Bs2MuMusBs2JPsiPhiLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_Bs2MuMusBs2JPsiPhiLine/Particles |

AddRelatedInfo/RelatedInfo4_Bs2MuMusBs2JPsiPhiLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_Bs2MuMusBs2JPsiPhiLine/Particles |

AddRelatedInfo/RelatedInfo5_Bs2MuMusBs2JPsiPhiLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo5_Bs2MuMusBs2JPsiPhiLine/Particles |

AddRelatedInfo/RelatedInfo6_Bs2MuMusBs2JPsiPhiLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo6_Bs2MuMusBs2JPsiPhiLine/Particles |

AddRelatedInfo/RelatedInfo7_Bs2MuMusBs2JPsiPhiLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo7_Bs2MuMusBs2JPsiPhiLine/Particles |

AddRelatedInfo/RelatedInfo8_Bs2MuMusBs2JPsiPhiLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusBs2JPsiPhiSelJpsi' ]             |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo8_Bs2MuMusBs2JPsiPhiLine/Particles |
