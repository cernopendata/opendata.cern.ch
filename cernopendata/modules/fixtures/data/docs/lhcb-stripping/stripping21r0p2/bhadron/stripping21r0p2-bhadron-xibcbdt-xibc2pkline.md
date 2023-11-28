[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingXibcBDT_Xibc2pKLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/XibcBDT_Xibc2pKLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

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

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNProtons

|      |                                         |
|------|-----------------------------------------|
| Code | 0StdAllLooseANNProtons/Particles',True) |

FilterDesktop/XibcBDTSelHighPTProtons

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (PROBNNp\> 0.05) & (PT\>1.0\*GeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY)\>1.)             |
| Inputs          | [ 'Phys/[StdAllLooseANNProtons](./stripping21r0p2-commonparticles-stdalllooseannprotons)' ] |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/XibcBDTSelHighPTProtons/Particles                                                        |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNKaons

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNKaons/Particles',True) |

FilterDesktop/XibcBDTSelHighPTKaons

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT\>1.0\*GeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY)\>1.)         |
| Inputs          | [ 'Phys/[StdAllLooseANNKaons](./stripping21r0p2-commonparticles-stdalllooseannkaons)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/XibcBDTSelHighPTKaons/Particles                                                      |

CombineParticles/XibcBDTSelXibc2pK

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibcBDTSelHighPTKaons' , 'Phys/XibcBDTSelHighPTProtons' ]                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }        |
| CombinationCut   | (AM\>4.8\*GeV)                                                                     |
| MotherCut        | (M\>5.0\*GeV) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVIPCHI2()\<25) & (BPVDIRA\> 0.99) |
| DecayDescriptor  | [ Xi_bc0 -\> p+ K- ]cc                                                           |
| DecayDescriptors | [ '[ Xi_bc0 -\> p+ K- ]cc' ]                                                   |
| Output           | Phys/XibcBDTSelXibc2pK/Particles                                                   |

FilterDesktop/XibcBDT_Xibc2pKLine

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/XibcBDTMvaXibc2pK')\>0. |
| Inputs          | [ 'Phys/XibcBDTSelXibc2pK' ]                         |
| DecayDescriptor | None                                                   |
| Output          | Phys/XibcBDT_Xibc2pKLine/Particles                     |
