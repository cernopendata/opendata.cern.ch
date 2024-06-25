[[stripping21 lines]](./stripping21-index)

# StrippingB2MuMuMuMuLinesB24MuLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/B2MuMuMuMuLinesB24MuLine/Particles |
| Postscale      | 1.0000000                               |
| HLT            | None                                    |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

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

CombineParticles/B2MuMuMuMuLinesB24MuLine

|                  |                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF \< 2.5 ) & (MIPCHI2DV(PRIMARY)\> 9.)' , 'mu-' : '(TRCHI2DOF \< 2.5 ) & (MIPCHI2DV(PRIMARY)\> 9.)' } |
| CombinationCut   | (ADAMASS('B_s0')\<1000\*MeV) & (AMAXDOCA('')\<0.3\*mm)                                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9)& (BPVDIRA \> 0) & (BPVVDCHI2\>100)& (BPVIPCHI2()\< 25) & (ADMASS('B_s0')\<1000\*MeV)                           |
| DecayDescriptor  | B_s0 -\> mu+ mu- mu+ mu-                                                                                                               |
| DecayDescriptors | [ 'B_s0 -\> mu+ mu- mu+ mu-' ]                                                                                                       |
| Output           | Phys/B2MuMuMuMuLinesB24MuLine/Particles                                                                                                |
