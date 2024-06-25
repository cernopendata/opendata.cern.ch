[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2LLXBDT_Lb2eePKLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/B2LLXBDT_Lb2eePKLine/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

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
| Inputs          | [ 'Phys/[StdDiElectronFromTracks](./stripping21r1p2-commonparticles-stddielectronfromtracks)' ]                                                                                                                                                                |
| DecayDescriptor | None                                                                                                                                                                                                                                                             |
| Output          | Phys/B2LLXBDTSelDiElectron/Particles                                                                                                                                                                                                                             |

LoKi::VoidFilter/SELECT:Phys/StdLooseANNProtons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseANNProtons/Particles',True) |

FilterDesktop/B2LLXBDTSelProtons

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PROBNNp\> 0.05) & (PT\>300\*MeV) & (TRGHOSTPROB\<0.4)                                  |
| Inputs          | [ 'Phys/[StdLooseANNProtons](./stripping21r1p2-commonparticles-stdlooseannprotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/B2LLXBDTSelProtons/Particles                                                       |

LoKi::VoidFilter/SELECT:Phys/StdLooseANNKaons

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseANNKaons/Particles',True) |

FilterDesktop/B2LLXBDTSelKaons

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT\>300\*MeV) & (TRGHOSTPROB\<0.4)                              |
| Inputs          | [ 'Phys/[StdLooseANNKaons](./stripping21r1p2-commonparticles-stdlooseannkaons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/B2LLXBDTSelKaons/Particles                                                     |

CombineParticles/B2LLXBDTSelLambdastar

|                  |                                                                             |
|------------------|-----------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelKaons' , 'Phys/B2LLXBDTSelProtons' ]                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' } |
| CombinationCut   | (AM \< 5.6\*GeV)                                                            |
| MotherCut        | (VFASPF(VCHI2) \< 25.)                                                      |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K-]cc                                               |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K-]cc' ]                                       |
| Output           | Phys/B2LLXBDTSelLambdastar/Particles                                        |

CombineParticles/B2LLXBDTSelLb2eePK

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelDiElectron' , 'Phys/B2LLXBDTSelLambdastar' ]                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'Lambda(1520)0' : 'ALL' , 'Lambda(1520)~0' : 'ALL' }                              |
| CombinationCut   | (in_range(3.7\*GeV, AM, 7.1\*GeV))                                                                                     |
| MotherCut        | (in_range(4.0\*GeV, M, 6.8\*GeV)) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.999) & (BPVDLS\>0) & (BPVIPCHI2()\<400) |
| DecayDescriptor  | [Lambda_b0 -\> J/psi(1S) Lambda(1520)0]cc                                                                            |
| DecayDescriptors | [ '[Lambda_b0 -\> J/psi(1S) Lambda(1520)0]cc' ]                                                                    |
| Output           | Phys/B2LLXBDTSelLb2eePK/Particles                                                                                      |

FilterDesktop/B2LLXBDT_Lb2eePKLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2LLXBDTMvaLb2eePK')\>-0.05 |
| Inputs          | [ 'Phys/B2LLXBDTSelLb2eePK' ]                            |
| DecayDescriptor | None                                                       |
| Output          | Phys/B2LLXBDT_Lb2eePKLine/Particles                        |

AddRelatedInfo/RelatedInfo1_B2LLXBDT_Lb2eePKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_B2LLXBDT_Lb2eePKLine/Particles |

AddRelatedInfo/RelatedInfo2_B2LLXBDT_Lb2eePKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_B2LLXBDT_Lb2eePKLine/Particles |

AddRelatedInfo/RelatedInfo3_B2LLXBDT_Lb2eePKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_B2LLXBDT_Lb2eePKLine/Particles |

AddRelatedInfo/RelatedInfo4_B2LLXBDT_Lb2eePKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_B2LLXBDT_Lb2eePKLine/Particles |

AddRelatedInfo/RelatedInfo5_B2LLXBDT_Lb2eePKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo5_B2LLXBDT_Lb2eePKLine/Particles |

AddRelatedInfo/RelatedInfo6_B2LLXBDT_Lb2eePKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo6_B2LLXBDT_Lb2eePKLine/Particles |

AddRelatedInfo/RelatedInfo7_B2LLXBDT_Lb2eePKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo7_B2LLXBDT_Lb2eePKLine/Particles |

AddRelatedInfo/RelatedInfo8_B2LLXBDT_Lb2eePKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo8_B2LLXBDT_Lb2eePKLine/Particles |

AddRelatedInfo/RelatedInfo9_B2LLXBDT_Lb2eePKLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo9_B2LLXBDT_Lb2eePKLine/Particles |

AddRelatedInfo/RelatedInfo10_B2LLXBDT_Lb2eePKLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                 |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo10_B2LLXBDT_Lb2eePKLine/Particles |

AddRelatedInfo/RelatedInfo11_B2LLXBDT_Lb2eePKLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Lb2eePKLine' ]                 |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo11_B2LLXBDT_Lb2eePKLine/Particles |
