[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingCcbar2PPPiPiLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/Ccbar2PPPiPiLine/Particles |
| Postscale      | 1.0000000                       |
| HLT1           | None                            |
| HLT2           | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

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

FilterDesktop/Ccbar2PPPiPiSelProtons

|                 |                                                                                               |
|-----------------|-----------------------------------------------------------------------------------------------|
| Code            | (PROBNNp \> 0.05) & (PT \> 400\*MeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY) \> 1.)        |
| Inputs          | [ 'Phys/[StdAllLooseANNProtons](./stripping21r1p2-commonparticles-stdalllooseannprotons)' ] |
| DecayDescriptor | None                                                                                          |
| Output          | Phys/Ccbar2PPPiPiSelProtons/Particles                                                         |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNPions

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNPions/Particles',True) |

FilterDesktop/Ccbar2PPPiPiSelPions

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.2 ) & (PT \> 150\*MeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY) \> 2.)   |
| Inputs          | [ 'Phys/[StdAllLooseANNPions](./stripping21r1p2-commonparticles-stdalllooseannpions)' ] |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/Ccbar2PPPiPiSelPions/Particles                                                       |

DaVinci::N4BodyDecays/Ccbar2PPPiPiSelCcbar2PPPiPi

|                  |                                                                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Ccbar2PPPiPiSelPions' , 'Phys/Ccbar2PPPiPiSelProtons' ]                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                                                      |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (AM \> 2.7 \*GeV) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.5 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>30) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (MM\>2.8 \*GeV) & (BPVDLS\>5)                                                                                                                                                                                                                         |
| DecayDescriptor  | J/psi(1S) -\> p+ p~- pi+ pi-                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ 'J/psi(1S) -\> p+ p~- pi+ pi-' ]                                                                                                                                                                                                                                               |
| Output           | Phys/Ccbar2PPPiPiSelCcbar2PPPiPi/Particles                                                                                                                                                                                                                                         |

FilterDesktop/Ccbar2PPPiPiLine

|                 |                                                                    |
|-----------------|--------------------------------------------------------------------|
| Code            | VALUE('LoKi::Hybrid::DictValue/Ccbar2PPPiPiMvaCcbar2PPPiPi')\>0.19 |
| Inputs          | [ 'Phys/Ccbar2PPPiPiSelCcbar2PPPiPi' ]                           |
| DecayDescriptor | None                                                               |
| Output          | Phys/Ccbar2PPPiPiLine/Particles                                    |
