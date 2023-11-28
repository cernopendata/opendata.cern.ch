[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2LLXBDT_Bu2mumuKLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2LLXBDT_Bu2mumuKLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseDiMuon_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDiMuon](./stripping21r1p1-commonparticles-stdloosedimuon)/Particles',True)\>0 |

FilterDesktop/B2LLXBDTSelDiMuon

|                 |                                                                                                                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<5.0\*GeV) & (INTREE( (ID=='mu+') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (TRGHOSTPROB\<0.5) )) & (INTREE( (ID=='mu-') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (TRGHOSTPROB\<0.5) )) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21r1p1-commonparticles-stdloosedimuon)' ]                                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                                                     |
| Output          | Phys/B2LLXBDTSelDiMuon/Particles                                                                                                                                                                                                         |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNKaons](./stripping21r1p1-commonparticles-stdlooseannkaons)/Particles',True)\>0 |

FilterDesktop/B2LLXBDTSelKaons

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT\>300\*MeV) & (TRGHOSTPROB\<0.4)                              |
| Inputs          | [ 'Phys/[StdLooseANNKaons](./stripping21r1p1-commonparticles-stdlooseannkaons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/B2LLXBDTSelKaons/Particles                                                     |

CombineParticles/B2LLXBDTSelBu2mumuK

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelDiMuon' , 'Phys/B2LLXBDTSelKaons' ]                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                     |
| CombinationCut   | (in_range(3.7\*GeV, AM, 6.8\*GeV))                                                                                     |
| MotherCut        | (in_range(4.0\*GeV, M, 6.5\*GeV)) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.999) & (BPVDLS\>0) & (BPVIPCHI2()\<400) |
| DecayDescriptor  | [B+ -\> J/psi(1S) K+]cc                                                                                              |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) K+]cc' ]                                                                                      |
| Output           | Phys/B2LLXBDTSelBu2mumuK/Particles                                                                                     |

FilterDesktop/B2LLXBDT_Bu2mumuKLine

|                 |                                                             |
|-----------------|-------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2LLXBDTMvaBu2mumuK')\>-0.05 |
| Inputs          | [ 'Phys/B2LLXBDTSelBu2mumuK' ]                            |
| DecayDescriptor | None                                                        |
| Output          | Phys/B2LLXBDT_Bu2mumuKLine/Particles                        |

AddRelatedInfo/RelatedInfo1_B2LLXBDT_Bu2mumuKLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2mumuKLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_B2LLXBDT_Bu2mumuKLine/Particles |

AddRelatedInfo/RelatedInfo2_B2LLXBDT_Bu2mumuKLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2mumuKLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_B2LLXBDT_Bu2mumuKLine/Particles |

AddRelatedInfo/RelatedInfo3_B2LLXBDT_Bu2mumuKLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2mumuKLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_B2LLXBDT_Bu2mumuKLine/Particles |

AddRelatedInfo/RelatedInfo4_B2LLXBDT_Bu2mumuKLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2mumuKLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo4_B2LLXBDT_Bu2mumuKLine/Particles |

AddRelatedInfo/RelatedInfo5_B2LLXBDT_Bu2mumuKLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2mumuKLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo5_B2LLXBDT_Bu2mumuKLine/Particles |

AddRelatedInfo/RelatedInfo6_B2LLXBDT_Bu2mumuKLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2mumuKLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo6_B2LLXBDT_Bu2mumuKLine/Particles |
