[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingB2LLXBDT_Bu2eeKLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B2LLXBDT_Bu2eeKLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

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

LoKi::VoidFilter/SelFilterPhys_StdDiElectronFromTracks_Particles

|      |                                                                                                                         |
|------|-------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdDiElectronFromTracks](./stripping21r1p1-commonparticles-stddielectronfromtracks)/Particles',True)\>0 |

FilterDesktop/B2LLXBDTSelDiElectron

|                 |                                                                                                                                                                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<5.0\*GeV) & (INTREE( (ID=='e+') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (PIDe\>-2) & (TRGHOSTPROB\<0.5) )) & (INTREE( (ID=='e-') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (PIDe\>-2) & (TRGHOSTPROB\<0.5) )) |
| Inputs          | [ 'Phys/[StdDiElectronFromTracks](./stripping21r1p1-commonparticles-stddielectronfromtracks)' ]                                                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                                                             |
| Output          | Phys/B2LLXBDTSelDiElectron/Particles                                                                                                                                                                                                                             |

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

CombineParticles/B2LLXBDTSelBu2eeK

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelDiElectron' , 'Phys/B2LLXBDTSelKaons' ]                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                     |
| CombinationCut   | (in_range(3.7\*GeV, AM, 6.8\*GeV))                                                                                     |
| MotherCut        | (in_range(4.0\*GeV, M, 6.5\*GeV)) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.999) & (BPVDLS\>0) & (BPVIPCHI2()\<400) |
| DecayDescriptor  | [B+ -\> J/psi(1S) K+]cc                                                                                              |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) K+]cc' ]                                                                                      |
| Output           | Phys/B2LLXBDTSelBu2eeK/Particles                                                                                       |

FilterDesktop/B2LLXBDT_Bu2eeKLine

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2LLXBDTMvaBu2eeK')\>-0.05 |
| Inputs          | [ 'Phys/B2LLXBDTSelBu2eeK' ]                            |
| DecayDescriptor | None                                                      |
| Output          | Phys/B2LLXBDT_Bu2eeKLine/Particles                        |

AddRelatedInfo/RelatedInfo1_B2LLXBDT_Bu2eeKLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2eeKLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo1_B2LLXBDT_Bu2eeKLine/Particles |

AddRelatedInfo/RelatedInfo2_B2LLXBDT_Bu2eeKLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2eeKLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo2_B2LLXBDT_Bu2eeKLine/Particles |

AddRelatedInfo/RelatedInfo3_B2LLXBDT_Bu2eeKLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2eeKLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo3_B2LLXBDT_Bu2eeKLine/Particles |

AddRelatedInfo/RelatedInfo4_B2LLXBDT_Bu2eeKLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2eeKLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo4_B2LLXBDT_Bu2eeKLine/Particles |

AddRelatedInfo/RelatedInfo5_B2LLXBDT_Bu2eeKLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2eeKLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo5_B2LLXBDT_Bu2eeKLine/Particles |

AddRelatedInfo/RelatedInfo6_B2LLXBDT_Bu2eeKLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bu2eeKLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo6_B2LLXBDT_Bu2eeKLine/Particles |
