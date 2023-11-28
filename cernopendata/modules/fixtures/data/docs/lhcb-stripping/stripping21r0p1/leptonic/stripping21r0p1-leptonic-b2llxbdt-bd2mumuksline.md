[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB2LLXBDT_Bd2mumuKsLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2LLXBDT_Bd2mumuKsLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

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
| Code | CONTAINS('Phys/[StdLooseDiMuon](./stripping21r0p1-commonparticles-stdloosedimuon)/Particles',True)\>0 |

FilterDesktop/B2LLXBDTSelDiMuon

|                 |                                                                                                                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (HASVERTEX) & (VFASPF(VCHI2)\<16) & (MM\<5.0\*GeV) & (INTREE( (ID=='mu+') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (TRGHOSTPROB\<0.5) )) & (INTREE( (ID=='mu-') & (PT\>200\*MeV) & (MIPCHI2DV(PRIMARY)\>1.) & (TRGHOSTPROB\<0.5) )) |
| Inputs          | [ 'Phys/[StdLooseDiMuon](./stripping21r0p1-commonparticles-stdloosedimuon)' ]                                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                                                     |
| Output          | Phys/B2LLXBDTSelDiMuon/Particles                                                                                                                                                                                                         |

GaudiSequencer/SeqB2LLXBDTSelKs

GaudiSequencer/SEQ:B2LLXBDTSelKsDD

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/B2LLXBDTSelKsDD

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.\*MeV) & (BPVVDCHI2\>25)                               |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p1-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/B2LLXBDTSelKsDD/Particles                                              |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/SEQ:B2LLXBDTSelKsLL

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)/Particles',True)\>0 |

FilterDesktop/B2LLXBDTSelPions4LP

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PROBNNpi\> 0.2) & (PT\>100\*MeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY)\>9.)         |
| Inputs          | [ 'Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/B2LLXBDTSelPions4LP/Particles                                                        |

CombineParticles/B2LLXBDTSelKsLL

|                  |                                                                        |
|------------------|------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelPions4LP' ]                                       |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                         |
| CombinationCut   | (ADAMASS('KS0') \< 50.\*MeV) & (ADOCACHI2CUT(25, ''))                  |
| MotherCut        | (ADMASS('KS0') \< 30.\*MeV) & (BPVVDCHI2\>25) & (VFASPF(VCHI2) \< 25.) |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                        |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                |
| Output           | Phys/B2LLXBDTSelKsLL/Particles                                         |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/B2LLXBDTSelKs

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Code            | ALL                                                   |
| Inputs          | [ 'Phys/B2LLXBDTSelKsDD' , 'Phys/B2LLXBDTSelKsLL' ] |
| DecayDescriptor | None                                                  |
| Output          | Phys/B2LLXBDTSelKs/Particles                          |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

CombineParticles/B2LLXBDTSelBd2mumuKs

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/B2LLXBDTSelDiMuon' , 'Phys/B2LLXBDTSelKs' ]                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'KS0' : 'ALL' }                                                                   |
| CombinationCut   | (in_range(3.7\*GeV, AM, 6.8\*GeV))                                                                                     |
| MotherCut        | (in_range(4.0\*GeV, M, 6.5\*GeV)) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVDIRA\> 0.999) & (BPVDLS\>0) & (BPVIPCHI2()\<400) |
| DecayDescriptor  | B0 -\> J/psi(1S) KS0                                                                                                   |
| DecayDescriptors | [ 'B0 -\> J/psi(1S) KS0' ]                                                                                           |
| Output           | Phys/B2LLXBDTSelBd2mumuKs/Particles                                                                                    |

FilterDesktop/B2LLXBDT_Bd2mumuKsLine

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/B2LLXBDTMvaBd2mumuKs')\>-0.07 |
| Inputs          | [ 'Phys/B2LLXBDTSelBd2mumuKs' ]                            |
| DecayDescriptor | None                                                         |
| Output          | Phys/B2LLXBDT_Bd2mumuKsLine/Particles                        |

AddRelatedInfo/RelatedInfo1_B2LLXBDT_Bd2mumuKsLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2mumuKsLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_B2LLXBDT_Bd2mumuKsLine/Particles |

AddRelatedInfo/RelatedInfo2_B2LLXBDT_Bd2mumuKsLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2mumuKsLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_B2LLXBDT_Bd2mumuKsLine/Particles |

AddRelatedInfo/RelatedInfo3_B2LLXBDT_Bd2mumuKsLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2mumuKsLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_B2LLXBDT_Bd2mumuKsLine/Particles |

AddRelatedInfo/RelatedInfo4_B2LLXBDT_Bd2mumuKsLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2mumuKsLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_B2LLXBDT_Bd2mumuKsLine/Particles |

AddRelatedInfo/RelatedInfo5_B2LLXBDT_Bd2mumuKsLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2mumuKsLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo5_B2LLXBDT_Bd2mumuKsLine/Particles |

AddRelatedInfo/RelatedInfo6_B2LLXBDT_Bd2mumuKsLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2LLXBDT_Bd2mumuKsLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo6_B2LLXBDT_Bd2mumuKsLine/Particles |
