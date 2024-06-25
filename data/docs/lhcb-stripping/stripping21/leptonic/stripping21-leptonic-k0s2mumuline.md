[[stripping21 lines]](./stripping21-index)

# StrippingK0s2MuMuLine

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/K0s2MuMuLine/Particles |
| Postscale      | 1.0000000                   |
| HLT            | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

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

CombineParticles/K0s2MuMuLine

|                  |                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 100.)&(TRCHI2DOF \< 5 ) & (PT \>0 \* MeV)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 100.)&(TRCHI2DOF \< 5 ) & (PT \>0 \* MeV)' } |
| CombinationCut   | (ADAMASS('KS0')\<1000\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                                                   |
| MotherCut        | ((BPVDIRA\>0) & ((BPVVDSIGN\*M/P) \> 0.1\*89.53\*2.9979e-01) & (MIPDV(PRIMARY)\<0.4\*mm) & (M\>465) & (PT \> 0 \* MeV))                                                |
| DecayDescriptor  | KS0 -\> mu+ mu-                                                                                                                                                        |
| DecayDescriptors | [ 'KS0 -\> mu+ mu-' ]                                                                                                                                                |
| Output           | Phys/K0s2MuMuLine/Particles                                                                                                                                            |
