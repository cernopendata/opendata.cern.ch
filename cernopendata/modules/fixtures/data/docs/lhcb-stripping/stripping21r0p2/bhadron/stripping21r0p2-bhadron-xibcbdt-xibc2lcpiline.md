[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingXibcBDT_Xibc2LcPiLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/XibcBDT_Xibc2LcPiLine/Particles |
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

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNProtons

|      |                                         |
|------|-----------------------------------------|
| Code | 0StdAllLooseANNProtons/Particles',True) |

FilterDesktop/XibcBDTSelProtons

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (PROBNNp\> 0.05) & (PT\>300\*MeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY)\>1.)             |
| Inputs          | [ 'Phys/[StdAllLooseANNProtons](./stripping21r0p2-commonparticles-stdalllooseannprotons)' ] |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/XibcBDTSelProtons/Particles                                                              |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNKaons

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNKaons/Particles',True) |

FilterDesktop/XibcBDTSelKaons

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT\>250\*MeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY)\>1.)         |
| Inputs          | [ 'Phys/[StdAllLooseANNKaons](./stripping21r0p2-commonparticles-stdalllooseannkaons)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/XibcBDTSelKaons/Particles                                                            |

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

CombineParticles/XibcBDTSelLambdaC

|                  |                                                                                                             |
|------------------|-------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibcBDTSelKaons' , 'Phys/XibcBDTSelPions' , 'Phys/XibcBDTSelProtons' ]                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' } |
| CombinationCut   | (APT\>1.0\*GeV) & (ADAMASS('Lambda_c+')\<50\*MeV) & (ADOCACHI2CUT(30, ''))                                  |
| MotherCut        | (ADMASS('Lambda_c+')\<30\*MeV) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVVDCHI2\>16)                              |
| DecayDescriptor  | [ Lambda_c+ -\> p+ K- pi+ ]cc                                                                             |
| DecayDescriptors | [ '[ Lambda_c+ -\> p+ K- pi+ ]cc' ]                                                                     |
| Output           | Phys/XibcBDTSelLambdaC/Particles                                                                            |

FilterDesktop/XibcBDTSelUnPions

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PROBNNpi\> 0.2) & (PT\>200\*MeV) & (TRGHOSTPROB\<0.4)                                    |
| Inputs          | [ 'Phys/[StdAllLooseANNPions](./stripping21r0p2-commonparticles-stdalllooseannpions)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/XibcBDTSelUnPions/Particles                                                          |

CombineParticles/XibcBDTSelXibc2LcPi

|                  |                                                                                             |
|------------------|---------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/XibcBDTSelLambdaC' , 'Phys/XibcBDTSelUnPions' ]                                   |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | (AM\>4.8\*GeV)                                                                              |
| MotherCut        | (M\>5.0\*GeV) & (VFASPF(VCHI2/VDOF) \< 25.) & (BPVIPCHI2()\<25) & (BPVDIRA\> 0.99)          |
| DecayDescriptor  | [ Xi_bc0 -\> Lambda_c+ pi- ]cc                                                            |
| DecayDescriptors | [ '[ Xi_bc0 -\> Lambda_c+ pi- ]cc' ]                                                    |
| Output           | Phys/XibcBDTSelXibc2LcPi/Particles                                                          |

FilterDesktop/XibcBDT_Xibc2LcPiLine

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/XibcBDTMvaXibc2LcPi')\>0. |
| Inputs          | [ 'Phys/XibcBDTSelXibc2LcPi' ]                         |
| DecayDescriptor | None                                                     |
| Output          | Phys/XibcBDT_Xibc2LcPiLine/Particles                     |
