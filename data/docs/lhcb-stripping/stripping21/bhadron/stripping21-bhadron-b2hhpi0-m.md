[[stripping21 lines]](./stripping21-index)

# StrippingB2HHPi0_M

## Properties:

|                |                          |
|----------------|--------------------------|
| OutputLocation | Phys/B2HHPi0_M/Particles |
| Postscale      | 1.0000000                |
| HLT            | None                     |
| Prescale       | 1.0000000                |
| L0DU           | None                     |
| ODIN           | None                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21-commonparticles-stdloosemergedpi0)/Particles')\>0 |

CombineParticles/B2HHPi0_M

|                  |                                                                                                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMergedPi0](./stripping21-commonparticles-stdloosemergedpi0)' , 'Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)' ]                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT\>500 \*MeV) & (P\>5000 \*MeV) & (TRPCHI2\>1e-06) & (TRGHOSTPROB\<0.5) & (MIPCHI2DV(PRIMARY)\>25)' , 'pi-' : '(PT\>500 \*MeV) & (P\>5000 \*MeV) & (TRPCHI2\>1e-06) & (TRGHOSTPROB\<0.5) & (MIPCHI2DV(PRIMARY)\>25)' , 'pi0' : '(PT\>2500 \*MeV)' } |
| CombinationCut   | (AM\>4200 \*MeV) & (AM\<6400 \*MeV)                                                                                                                                                                                                                                           |
| MotherCut        | (PT\>3000 \*MeV) & (VFASPF(VPCHI2)\>0.001) & (BPVVDCHI2\>64) & (BPVIPCHI2()\<9) & (BPVDIRA\>0.99995)                                                                                                                                                                          |
| DecayDescriptor  | B0 -\> pi+ pi- pi0                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'B0 -\> pi+ pi- pi0' ]                                                                                                                                                                                                                                                    |
| Output           | Phys/B2HHPi0_M/Particles                                                                                                                                                                                                                                                      |

AddExtraInfo/ExtraInfo_StrippingB2HHPi0_M

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/B2HHPi0_M' ]                      |
| DecayDescriptor | None                                        |
| Output          | Phys/ExtraInfo_StrippingB2HHPi0_M/Particles |
| Tools           | [ 'VertexIsolation/Tool1' ]               |
