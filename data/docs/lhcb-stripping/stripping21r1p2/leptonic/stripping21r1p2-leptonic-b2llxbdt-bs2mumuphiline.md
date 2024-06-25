[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2LLXBDT_Bs2mumuPhiLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2LLXBDT_Bs2mumuPhiLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

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

LoKi::VoidFilter/SELECT:Phys/StdLooseDiMuon

|      |                                  |
|------|----------------------------------|
| Code | 0StdLooseDiMuon/Particles',True) |

FilterDesktop/B2LLXBDTSelDiMuon

|                 |                                                                                                                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<5.0\*GeV) & (INTREE( (ID=='mu+') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (TRGHOSTPROB\<0.5) )) & (INTREE( (ID=='mu-') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (TRGHOSTPROB\<0.5) )) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21r1p2-commonparticles-stdloosedimuon)' ]                                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                                                     |
| Output          | Phys/B2LLXBDTSelDiMuon/Particles                                                                                                                                                                                                         |

LoKi::VoidFilter/SELECT:Phys/StdLoosePhi2KK

|      |                                  |
|------|----------------------------------|
| Code | 0StdLoosePhi2KK/Particles',True) |

FilterDesktop/B2LLXBDTSelPhi

|                 |                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<1.05\*GeV) & (MIPCHI2DV(PRIMARY)\>2.) & (INTREE( (ID=='K+') & (PT\>200\*MeV) & (TRGHOSTPROB\<0.4) )) & (INTREE( (ID=='K-') & (PT\>200\*MeV) & (TRGHOSTPROB\<0.4) )) |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21r1p2-commonparticles-stdloosephi2kk)' ]                                                                                                                              |
| DecayDescriptor | None                                                                                                                                                                                                         |
| Output          | Phys/B2LLXBDTSelPhi/Particles                                                                                                                                                                                |

CombineParticles/B2LLXBDTSelBs2mumuPhi

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelDiMuon' , 'Phys/B2LLXBDTSelPhi' ]                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'phi(1020)' : 'ALL' }                                                             |
| CombinationCut   | (in_range(3.7\*GeV, AM, 6.8\*GeV))                                                                                     |
| MotherCut        | (in_range(4.0\*GeV, M, 6.5\*GeV)) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.999) & (BPVDLS\>0) & (BPVIPCHI2()\<400) |
| DecayDescriptor  | B_s0 -\> J/psi(1S) phi(1020)                                                                                           |
| DecayDescriptors | [ 'B_s0 -\> J/psi(1S) phi(1020)' ]                                                                                   |
| Output           | Phys/B2LLXBDTSelBs2mumuPhi/Particles                                                                                   |

FilterDesktop/B2LLXBDT_Bs2mumuPhiLine

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2LLXBDTMvaBs2mumuPhi')\>-0.08 |
| Inputs          | [ 'Phys/B2LLXBDTSelBs2mumuPhi' ]                            |
| DecayDescriptor | None                                                          |
| Output          | Phys/B2LLXBDT_Bs2mumuPhiLine/Particles                        |

AddRelatedInfo/RelatedInfo1_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo1_B2LLXBDT_Bs2mumuPhiLine/Particles |

AddRelatedInfo/RelatedInfo2_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo2_B2LLXBDT_Bs2mumuPhiLine/Particles |

AddRelatedInfo/RelatedInfo3_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo3_B2LLXBDT_Bs2mumuPhiLine/Particles |

AddRelatedInfo/RelatedInfo4_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo4_B2LLXBDT_Bs2mumuPhiLine/Particles |

AddRelatedInfo/RelatedInfo5_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo5_B2LLXBDT_Bs2mumuPhiLine/Particles |

AddRelatedInfo/RelatedInfo6_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo6_B2LLXBDT_Bs2mumuPhiLine/Particles |

AddRelatedInfo/RelatedInfo7_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo7_B2LLXBDT_Bs2mumuPhiLine/Particles |

AddRelatedInfo/RelatedInfo8_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo8_B2LLXBDT_Bs2mumuPhiLine/Particles |

AddRelatedInfo/RelatedInfo9_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo9_B2LLXBDT_Bs2mumuPhiLine/Particles |

AddRelatedInfo/RelatedInfo10_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                 |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo10_B2LLXBDT_Bs2mumuPhiLine/Particles |

AddRelatedInfo/RelatedInfo11_B2LLXBDT_Bs2mumuPhiLine

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bs2mumuPhiLine' ]                 |
| DecayDescriptor | None                                                 |
| Output          | Phys/RelatedInfo11_B2LLXBDT_Bs2mumuPhiLine/Particles |
