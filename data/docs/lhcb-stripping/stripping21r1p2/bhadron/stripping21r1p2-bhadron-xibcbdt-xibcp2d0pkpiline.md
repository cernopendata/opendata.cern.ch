[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingXibcBDT_XibcP2D0pKpiLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/XibcBDT_XibcP2D0pKpiLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

LoKi::VoidFilter/SELECT:Phys/StdLooseD02KPi

|      |                                  |
|------|----------------------------------|
| Code | 0StdLooseD02KPi/Particles',True) |

FilterDesktop/XibcBDTSelD0

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (ADMASS('D0')\<75\*MeV) & (VFASPF(VCHI2/VDOF) \< 25.) & (PT\>1.0\*GeV) & (BPVVDCHI2\>64) |
| Inputs          | [ 'Phys/[StdLooseD02KPi](./stripping21r1p2-commonparticles-stdloosed02kpi)' ]          |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/XibcBDTSelD0/Particles                                                              |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNProtons

|      |                                         |
|------|-----------------------------------------|
| Code | 0StdAllLooseANNProtons/Particles',True) |

FilterDesktop/XibcBDTSelUnProtons

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (PROBNNp\> 0.05) & (PT\>300\*MeV) & (TRGHOSTPROB\<0.4)                                        |
| Inputs          | [ 'Phys/[StdAllLooseANNProtons](./stripping21r1p2-commonparticles-stdalllooseannprotons)' ] |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/XibcBDTSelUnProtons/Particles                                                            |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNKaons

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNKaons/Particles',True) |

FilterDesktop/XibcBDTSelUnKaons

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT\>250\*MeV) & (TRGHOSTPROB\<0.4)                                    |
| Inputs          | [ 'Phys/[StdAllLooseANNKaons](./stripping21r1p2-commonparticles-stdalllooseannkaons)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/XibcBDTSelUnKaons/Particles                                                          |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNPions

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNPions/Particles',True) |

FilterDesktop/XibcBDTSelHighPTPions

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PROBNNpi\> 0.2) & (PT\>0.5\*GeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY)\>1.)         |
| Inputs          | [ 'Phys/[StdAllLooseANNPions](./stripping21r1p2-commonparticles-stdalllooseannpions)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/XibcBDTSelHighPTPions/Particles                                                      |

CombineParticles/XibcBDTSelXibcP2D0pKpi

|                  |                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibcBDTSelD0' , 'Phys/XibcBDTSelHighPTPions' , 'Phys/XibcBDTSelUnKaons' , 'Phys/XibcBDTSelUnProtons' ]                           |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' } |
| CombinationCut   | (AM\>4.8\*GeV)                                                                                                                             |
| MotherCut        | (M\>5.0\*GeV) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVIPCHI2()\<25) & (BPVDIRA\> 0.99)                                                         |
| DecayDescriptor  | [ Xi_bc+ -\> D0 p+ K- pi+ ]cc                                                                                                            |
| DecayDescriptors | [ '[ Xi_bc+ -\> D0 p+ K- pi+ ]cc' ]                                                                                                    |
| Output           | Phys/XibcBDTSelXibcP2D0pKpi/Particles                                                                                                      |

FilterDesktop/XibcBDT_XibcP2D0pKpiLine

|                 |                                                                |
|-----------------|----------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/XibcBDTMvaXibcP2D0pKpi')\>-0.05 |
| Inputs          | [ 'Phys/XibcBDTSelXibcP2D0pKpi' ]                            |
| DecayDescriptor | None                                                           |
| Output          | Phys/XibcBDT_XibcP2D0pKpiLine/Particles                        |
