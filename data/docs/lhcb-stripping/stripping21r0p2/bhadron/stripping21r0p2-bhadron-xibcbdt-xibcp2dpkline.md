[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingXibcBDT_XibcP2DpKLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/XibcBDT_XibcP2DpKLine/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNPions

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNPions/Particles',True) |

FilterDesktop/XibcBDTSelUnPions_comb

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (P\>3\*GeV) & (PT\>250\*MeV) & (MIPCHI2DV(PRIMARY)\>4.)                                   |
| Inputs          | [ 'Phys/[StdAllLooseANNPions](./stripping21r0p2-commonparticles-stdalllooseannpions)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/XibcBDTSelUnPions_comb/Particles                                                     |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNKaons

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNKaons/Particles',True) |

FilterDesktop/XibcBDTSelUnKaons_comb

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (P\>3\*GeV) & (PT\>250\*MeV) & (MIPCHI2DV(PRIMARY)\>4.)                                   |
| Inputs          | [ 'Phys/[StdAllLooseANNKaons](./stripping21r0p2-commonparticles-stdalllooseannkaons)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/XibcBDTSelUnKaons_comb/Particles                                                     |

CombineParticles/XibcBDTSelDplus_comb

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibcBDTSelUnKaons_comb' , 'Phys/XibcBDTSelUnPions_comb' ]                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                            |
| CombinationCut   | (AM\>1760.\*MeV) & (AM\<2080.\*MeV) & ((APT\>2.\*GeV) \| (ASUM(PT)\>2.\*GeV)) & (ADOCAMAX('')\<0.5\*mm) |
| MotherCut        | (VFASPF(VCHI2) \< 30 ) & (M\>1770.\*MeV) & (M \< 2070.\*MeV) & (BPVVDCHI2\>36)                          |
| DecayDescriptor  | [ D+ -\> K- pi+ pi+ ]cc                                                                               |
| DecayDescriptors | [ '[ D+ -\> K- pi+ pi+ ]cc' ]                                                                       |
| Output           | Phys/XibcBDTSelDplus_comb/Particles                                                                     |

FilterDesktop/XibcBDTSelDplus

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (ADMASS('D+')\<75\*MeV) & (VFASPF(VCHI2/VDOF) \< 25.) & (PT\>1.0\*GeV) & (BPVVDCHI2\>100) |
| Inputs          | [ 'Phys/XibcBDTSelDplus_comb' ]                                                         |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/XibcBDTSelDplus/Particles                                                            |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNProtons

|      |                                         |
|------|-----------------------------------------|
| Code | 0StdAllLooseANNProtons/Particles',True) |

FilterDesktop/XibcBDTSelUnProtons

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (PROBNNp\> 0.05) & (PT\>300\*MeV) & (TRGHOSTPROB\<0.4)                                        |
| Inputs          | [ 'Phys/[StdAllLooseANNProtons](./stripping21r0p2-commonparticles-stdalllooseannprotons)' ] |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/XibcBDTSelUnProtons/Particles                                                            |

FilterDesktop/XibcBDTSelUnKaons

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT\>250\*MeV) & (TRGHOSTPROB\<0.4)                                    |
| Inputs          | [ 'Phys/[StdAllLooseANNKaons](./stripping21r0p2-commonparticles-stdalllooseannkaons)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/XibcBDTSelUnKaons/Particles                                                          |

CombineParticles/XibcBDTSelXibcP2DpK

|                  |                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibcBDTSelDplus' , 'Phys/XibcBDTSelUnKaons' , 'Phys/XibcBDTSelUnProtons' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' } |
| CombinationCut   | (AM\>4.8\*GeV)                                                                                            |
| MotherCut        | (M\>5.0\*GeV) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVIPCHI2()\<25) & (BPVDIRA\> 0.99)                        |
| DecayDescriptor  | [ Xi_bc+ -\> D+ p+ K- ]cc                                                                               |
| DecayDescriptors | [ '[ Xi_bc+ -\> D+ p+ K- ]cc' ]                                                                       |
| Output           | Phys/XibcBDTSelXibcP2DpK/Particles                                                                        |

FilterDesktop/XibcBDT_XibcP2DpKLine

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/XibcBDTMvaXibcP2DpK')\>0.02 |
| Inputs          | [ 'Phys/XibcBDTSelXibcP2DpK' ]                           |
| DecayDescriptor | None                                                       |
| Output          | Phys/XibcBDT_XibcP2DpKLine/Particles                       |
