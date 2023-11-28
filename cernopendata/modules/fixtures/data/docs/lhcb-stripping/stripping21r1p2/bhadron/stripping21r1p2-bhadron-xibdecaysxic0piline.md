[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingXibDecaysXic0piLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/XibDecaysXic0piLine/Particles |
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

LoKi::VoidFilter/SELECT:Phys/StdLooseANNKaons

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseANNKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseANNPions

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseANNPions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseANNProtons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseANNProtons/Particles',True) |

CombineParticles/Xic0ForXibDecays

|                  |                                                                                                                                                                                                                                                                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseANNKaons](./stripping21r1p2-commonparticles-stdlooseannkaons)' , 'Phys/[StdLooseANNPions](./stripping21r1p2-commonparticles-stdlooseannpions)' , 'Phys/[StdLooseANNProtons](./stripping21r1p2-commonparticles-stdlooseannprotons)' ]                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PROBNNk \> 0.1) & (MIPCHI2DV(PRIMARY)\>4)' , 'K-' : '(PROBNNk \> 0.1) & (MIPCHI2DV(PRIMARY)\>4)' , 'p+' : '(PROBNNp \> 0.1) & (MIPCHI2DV(PRIMARY)\>4)' , 'pi+' : '(PROBNNpi \> 0.1) & (MIPCHI2DV(PRIMARY)\>4)' , 'pi-' : '(PROBNNpi \> 0.1) & (MIPCHI2DV(PRIMARY)\>4)' , 'p~-' : '(PROBNNp \> 0.1) & (MIPCHI2DV(PRIMARY)\>4)' } |
| CombinationCut   | (ASUM(PT)\> 1800\*MeV) & (ADAMASS('Xi_c0') \< 1.25\*100\*MeV) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator'))                                                                                                                                                                                                                                          |
| MotherCut        | (ADMASS('Xi_c0') \< 100\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0.0)                                                                                                                                                                                                                                                             |
| DecayDescriptor  | [Xi_c0 -\> p+ K- K- pi+]cc                                                                                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ '[Xi_c0 -\> p+ K- K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                    |
| Output           | Phys/Xic0ForXibDecays/Particles                                                                                                                                                                                                                                                                                                                         |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNPions

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNPions/Particles',True) |

CombineParticles/XibDecaysXic0piLine

|                  |                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNPions](./stripping21r1p2-commonparticles-stdalllooseannpions)' , 'Phys/Xic0ForXibDecays' ]                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'Xi_c0' : 'ALL' , 'Xi_c~0' : 'ALL' , 'pi+' : '(PROBNNpi \> 0.1) & (MIPCHI2DV(PRIMARY)\>4)' , 'pi-' : '(PROBNNpi \> 0.1) & (MIPCHI2DV(PRIMARY)\>4)' } |
| CombinationCut   | (AM \< 6500.0\*MeV+500\*MeV) & (AM \> 5300.0\*MeV-500\*MeV)                                                                                                         |
| MotherCut        | (M \< 6500.0\*MeV) & (M \> 5300.0\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVIPCHI2() \< 25) & (BPVLTIME()\>0.2\*ps) & (PT\>3500.0\*MeV) & (BPVDIRA\>0.999)             |
| DecayDescriptor  | [Xi_b- -\> Xi_c0 pi-]cc                                                                                                                                           |
| DecayDescriptors | [ '[Xi_b- -\> Xi_c0 pi-]cc' ]                                                                                                                                   |
| Output           | Phys/XibDecaysXic0piLine/Particles                                                                                                                                  |
