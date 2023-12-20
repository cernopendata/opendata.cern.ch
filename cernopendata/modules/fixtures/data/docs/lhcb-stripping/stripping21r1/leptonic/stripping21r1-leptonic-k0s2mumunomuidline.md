[[stripping21r1 lines]](./stripping21r1-index)

# StrippingK0s2MuMuNoMuIDLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/K0s2MuMuNoMuIDLine/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 0.0010000000                      |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)/Particles')\>0 |

CombineParticles/K0s2MuMuNoMuIDLine

|                  |                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdNoPIDsPions](./stripping21r1-commonparticles-stdnopidspions)' ]                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY)\> 100.)&(TRCHI2DOF \< 5 ) & (PT \>0 \* MeV )' , 'pi-' : '(MIPCHI2DV(PRIMARY)\> 100.)&(TRCHI2DOF \< 5 ) & (PT \>0 \* MeV )' } |
| CombinationCut   | (ADAMASS('KS0')\<100\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                                                      |
| MotherCut        | ((BPVDIRA\>0) & ((BPVVDSIGN\*M/P) \> 0.1\*89.53\*2.9979e-01) & (MIPDV(PRIMARY)\<0.4\*mm) & (M\>400) & (M\<600) & (PT \> 0 \* MeV))                                       |
| DecayDescriptor  | KS0 -\> pi+ pi-                                                                                                                                                          |
| DecayDescriptors | [ 'KS0 -\> pi+ pi-' ]                                                                                                                                                  |
| Output           | Phys/K0s2MuMuNoMuIDLine/Particles                                                                                                                                        |
