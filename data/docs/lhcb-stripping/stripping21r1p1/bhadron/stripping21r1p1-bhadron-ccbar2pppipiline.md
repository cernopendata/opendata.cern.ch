[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingCcbar2PPPiPiLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/Ccbar2PPPiPiLine/Particles      |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | (HLT_PASS_RE('Hlt2Topo.\*Decision')) |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseANNProtons_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNProtons](./stripping21r1p1-commonparticles-stdlooseannprotons)/Particles',True)\>0 |

FilterDesktop/Ccbar2PPPiPiSelProtons

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (PROBNNp \> 0.1) & (PT \> 300\*MeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY) \> 9.)   |
| Inputs          | [ 'Phys/[StdLooseANNProtons](./stripping21r1p1-commonparticles-stdlooseannprotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/Ccbar2PPPiPiSelProtons/Particles                                                   |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/Ccbar2PPPiPiSelPions

|                 |                                                                                        |
|-----------------|----------------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.2) & (PT \> 250\*MeV) & (TRGHOSTPROB\<0.4) & (MIPCHI2DV(PRIMARY) \> 9.) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]          |
| DecayDescriptor | None                                                                                   |
| Output          | Phys/Ccbar2PPPiPiSelPions/Particles                                                    |

DaVinci::N4BodyDecays/Ccbar2PPPiPiLine

|                  |                                                                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Ccbar2PPPiPiSelPions' , 'Phys/Ccbar2PPPiPiSelProtons' ]                                                                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                                                                                      |
| CombinationCut   | ( ACHI2DOCA(1,4)\<20 ) & ( ACHI2DOCA(2,4)\<20 ) & ( ACHI2DOCA(3,4)\<20 ) & (AM \> 2.7 \*GeV) & ( (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3)+ACHILD(PT,4) ) \> 2.5 \*GeV) & ( (ACHILD(MIPCHI2DV(), 1) + ACHILD(MIPCHI2DV(), 2) + ACHILD(MIPCHI2DV(), 3) + ACHILD(MIPCHI2DV(), 4))\>30) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.) & (in_range(2.8\*GeV, MM, 4.2\*GeV)) & (BPVDLS\>5)                                                                                                                                                                                                      |
| DecayDescriptor  | J/psi(1S) -\> p+ p~- pi+ pi-                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ 'J/psi(1S) -\> p+ p~- pi+ pi-' ]                                                                                                                                                                                                                                               |
| Output           | Phys/Ccbar2PPPiPiLine/Particles                                                                                                                                                                                                                                                    |
