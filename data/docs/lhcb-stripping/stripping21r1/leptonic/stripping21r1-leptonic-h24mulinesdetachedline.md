[[stripping21r1 lines]](./stripping21r1-index)

# StrippingH24MuLinesDetachedLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/H24MuLinesDetachedLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1-commonparticles-stdallloosemuons)/Particles')\>0 |

CombineParticles/SelA1H24MuLinesDetached

|                  |                                                                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21r1-commonparticles-stdallloosemuons)' ]                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 3 ) & (PT \> 150 \* MeV ) & ( TRGHOSTPROB \< 0.4 ) & (MIPCHI2DV(PRIMARY)\> 1 )' , 'mu-' : '(TRCHI2DOF \< 3 ) & (PT \> 150 \* MeV ) & ( TRGHOSTPROB \< 0.4 ) & (MIPCHI2DV(PRIMARY)\> 1 )' } |
| CombinationCut   | (AM \< 2000 \* MeV ) & (AMAXDOCA('')\<0.3 \* mm)                                                                                                                                                                                 |
| MotherCut        | (VFASPF(VCHI2)\< 10 ) & (MM \< 2000 \* MeV)& (BPVDIRA \> 0 )& (BPVIPCHI2() \< 36 )& (BPVVDCHI2 \> 4 )                                                                                                                            |
| DecayDescriptor  | KS0 -\> mu+ mu-                                                                                                                                                                                                                  |
| DecayDescriptors | [ 'KS0 -\> mu+ mu-' ]                                                                                                                                                                                                          |
| Output           | Phys/SelA1H24MuLinesDetached/Particles                                                                                                                                                                                           |

CombineParticles/H24MuLinesDetachedLine

|                  |                                              |
|------------------|----------------------------------------------|
| Inputs           | [ 'Phys/SelA1H24MuLinesDetached' ]         |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' }               |
| CombinationCut   | (AMAXDOCA('')\< 1 \* mm )                    |
| MotherCut        | (PT \> 1000 \* MeV ) & (VFASPF(VCHI2)\< 15 ) |
| DecayDescriptor  | H_10 -\> KS0 KS0                             |
| DecayDescriptors | [ 'H_10 -\> KS0 KS0' ]                     |
| Output           | Phys/H24MuLinesDetachedLine/Particles        |

AddExtraInfo/ExtraInfo_StrippingH24MuLinesDetachedLine

|                 |                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/SelA1H24MuLinesDetached' ]                                                                  |
| DecayDescriptor | None                                                                                                  |
| Output          | Phys/ExtraInfo_StrippingH24MuLinesDetachedLine/Particles                                              |
| Tools           | [ 'ConeVariables/Tool1' , 'ConeVariables/Tool2' , 'ConeVariables/Tool3' , 'VertexIsolation/Tool4' ] |
