[[stripping21 lines]](./stripping21-index)

# StrippingTau23MuDs2PhiPiLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/Tau23MuDs2PhiPiLine/Particles |
| Postscale      | 1.0000000                          |
| HLT            | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

CombineParticles/Tau23MuDs2PhiPiLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' , 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]                                                                                                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : ' ( PT \> 300 \* MeV ) & ( TRGHOSTPROB \< 0.3 ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) ' , 'mu-' : ' ( PT \> 300 \* MeV ) & ( TRGHOSTPROB \< 0.3 ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) ' , 'pi+' : ' ( PT \> 300 \* MeV ) & ( TRGHOSTPROB \< 0.3 ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) ' , 'pi-' : ' ( PT \> 300 \* MeV ) & ( TRGHOSTPROB \< 0.3 ) & ( TRCHI2DOF \< 3 ) & ( BPVIPCHI2 () \> 9 ) ' } |
| CombinationCut   | (ADAMASS('D_s+')\<250\*MeV) & in_range ( 970 \* MeV , AM23 , 1070 \* MeV )                                                                                                                                                                                                                                                                                                                                                                         |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME () \* c_light) \>100 \* micrometer ) & ( BPVIPCHI2() \< 225 )                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | [ D_s+ -\> pi+ mu+ mu- ]cc                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ ' [ D_s+ -\> pi+ mu+ mu- ]cc ' ]                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output           | Phys/Tau23MuDs2PhiPiLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                 |

AddRelatedInfo/RelatedInfo1_Tau23MuDs2PhiPiLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuDs2PhiPiLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo1_Tau23MuDs2PhiPiLine/Particles |

AddRelatedInfo/RelatedInfo2_Tau23MuDs2PhiPiLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuDs2PhiPiLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo2_Tau23MuDs2PhiPiLine/Particles |

AddRelatedInfo/RelatedInfo3_Tau23MuDs2PhiPiLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Tau23MuDs2PhiPiLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo3_Tau23MuDs2PhiPiLine/Particles |
