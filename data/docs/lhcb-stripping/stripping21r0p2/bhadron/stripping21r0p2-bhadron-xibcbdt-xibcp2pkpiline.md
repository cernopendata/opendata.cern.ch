[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingXibcBDT_XibcP2pKpiLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/XibcBDT_XibcP2pKpiLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

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

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNPions

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNPions/Particles',True) |

FilterDesktop/XibcBDTSelPions

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PROBNNpi\> 0.2) & (PT\>200\*MeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY)\>1.)         |
| Inputs          | [ 'Phys/[StdAllLooseANNPions](./stripping21r0p2-commonparticles-stdalllooseannpions)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/XibcBDTSelPions/Particles                                                            |

CombineParticles/XibcBDTSelXibcP2pKpi

|                  |                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibcBDTSelHighPTKaons' , 'Phys/XibcBDTSelHighPTProtons' , 'Phys/XibcBDTSelPions' ]                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' } |
| CombinationCut   | (AM\>4.8\*GeV)                                                                                              |
| MotherCut        | (M\>5.0\*GeV) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVIPCHI2()\<25) & (BPVDIRA\> 0.99)                          |
| DecayDescriptor  | [ Xi_bc+ -\> p+ K- pi+ ]cc                                                                                |
| DecayDescriptors | [ '[ Xi_bc+ -\> p+ K- pi+ ]cc' ]                                                                        |
| Output           | Phys/XibcBDTSelXibcP2pKpi/Particles                                                                         |

FilterDesktop/XibcBDT_XibcP2pKpiLine

|                 |                                                             |
|-----------------|-------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/XibcBDTMvaXibcP2pKpi')\>0.14 |
| Inputs          | [ 'Phys/XibcBDTSelXibcP2pKpi' ]                           |
| DecayDescriptor | None                                                        |
| Output          | Phys/XibcBDT_XibcP2pKpiLine/Particles                       |
