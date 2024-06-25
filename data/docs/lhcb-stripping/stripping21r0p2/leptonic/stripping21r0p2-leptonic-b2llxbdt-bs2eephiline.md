[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2LLXBDT_Bs2eePhiLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2LLXBDT_Bs2eePhiLine/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdDiElectronFromTracks

|      |                                           |
|------|-------------------------------------------|
| Code | 0StdDiElectronFromTracks/Particles',True) |

FilterDesktop/B2LLXBDTSelDiElectron

|                 |                                                                                                                                                                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<5.0\*GeV) & (INTREE( (ID=='e+') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (PIDe\>-2) & (TRGHOSTPROB\<0.5) )) & (INTREE( (ID=='e-') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (PIDe\>-2) & (TRGHOSTPROB\<0.5) )) |
| Inputs          | [ 'Phys/[StdDiElectronFromTracks](./stripping21r0p2-commonparticles-stddielectronfromtracks)' ]                                                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                                                             |
| Output          | Phys/B2LLXBDTSelDiElectron/Particles                                                                                                                                                                                                                             |

LoKi::VoidFilter/SELECT:Phys/StdLoosePhi2KK

|      |                                  |
|------|----------------------------------|
| Code | 0StdLoosePhi2KK/Particles',True) |

FilterDesktop/B2LLXBDTSelPhi

|                 |                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<1.05\*GeV) & (MIPCHI2DV(PRIMARY)\>2.) & (INTREE( (ID=='K+') & (PT\>200\*MeV) & (TRGHOSTPROB\<0.4) )) & (INTREE( (ID=='K-') & (PT\>200\*MeV) & (TRGHOSTPROB\<0.4) )) |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21r0p2-commonparticles-stdloosephi2kk)' ]                                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                                                         |
| Output          | Phys/B2LLXBDTSelPhi/Particles                                                                                                                                                                                |

CombineParticles/B2LLXBDTSelBs2eePhi

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelDiElectron' , 'Phys/B2LLXBDTSelPhi' ]                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'phi(1020)' : 'ALL' }                                                             |
| CombinationCut   | (in_range(3.7\*GeV, AM, 6.8\*GeV))                                                                                     |
| MotherCut        | (in_range(4.0\*GeV, M, 6.5\*GeV)) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.999) & (BPVDLS\>0) & (BPVIPCHI2()\<400) |
| DecayDescriptor  | B_s0 -\> J/psi(1S) phi(1020)                                                                                           |
| DecayDescriptors | [ 'B_s0 -\> J/psi(1S) phi(1020)' ]                                                                                   |
| Output           | Phys/B2LLXBDTSelBs2eePhi/Particles                                                                                     |

FilterDesktop/B2LLXBDT_Bs2eePhiLine

|                 |                                                             |
|-----------------|-------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2LLXBDTMvaBs2eePhi')\>-0.06 |
| Inputs          | [ 'Phys/B2LLXBDTSelBs2eePhi' ]                            |
| DecayDescriptor | None                                                        |
| Output          | Phys/B2LLXBDT_Bs2eePhiLine/Particles                        |

AddRelatedInfo/RelatedInfo1_B2LLXBDT_Bs2eePhiLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_B2LLXBDT_Bs2eePhiLine/Particles |

AddRelatedInfo/RelatedInfo2_B2LLXBDT_Bs2eePhiLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_B2LLXBDT_Bs2eePhiLine/Particles |

AddRelatedInfo/RelatedInfo3_B2LLXBDT_Bs2eePhiLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_B2LLXBDT_Bs2eePhiLine/Particles |

AddRelatedInfo/RelatedInfo4_B2LLXBDT_Bs2eePhiLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo4_B2LLXBDT_Bs2eePhiLine/Particles |

AddRelatedInfo/RelatedInfo5_B2LLXBDT_Bs2eePhiLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo5_B2LLXBDT_Bs2eePhiLine/Particles |

AddRelatedInfo/RelatedInfo6_B2LLXBDT_Bs2eePhiLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo6_B2LLXBDT_Bs2eePhiLine/Particles |

AddRelatedInfo/RelatedInfo7_B2LLXBDT_Bs2eePhiLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo7_B2LLXBDT_Bs2eePhiLine/Particles |

AddRelatedInfo/RelatedInfo8_B2LLXBDT_Bs2eePhiLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo8_B2LLXBDT_Bs2eePhiLine/Particles |

AddRelatedInfo/RelatedInfo9_B2LLXBDT_Bs2eePhiLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo9_B2LLXBDT_Bs2eePhiLine/Particles |

AddRelatedInfo/RelatedInfo10_B2LLXBDT_Bs2eePhiLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                 |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo10_B2LLXBDT_Bs2eePhiLine/Particles |

AddRelatedInfo/RelatedInfo11_B2LLXBDT_Bs2eePhiLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2eePhiLine' ]                 |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo11_B2LLXBDT_Bs2eePhiLine/Particles |
