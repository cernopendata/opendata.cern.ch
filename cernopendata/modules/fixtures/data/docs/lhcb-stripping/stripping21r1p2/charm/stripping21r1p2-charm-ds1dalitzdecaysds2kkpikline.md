[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingDs1DalitzDecaysDs2KKpiKLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/Ds1DalitzDecaysDs2KKpiKLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 0.20000000                                 |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsKaons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

CombineParticles/Ds1DalitzDecaysDs2KKpiKLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1p2-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.4) & (PT \> 250\*MeV) & (P \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (PIDK \> 5)' , 'K-' : '(TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.4) & (PT \> 250\*MeV) & (P \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (PIDK \> 5)' , 'pi+' : '(TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.4) & (PT \> 250\*MeV) & (P \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (PIDK \< 5)' , 'pi-' : '(TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.4) & (PT \> 250\*MeV) & (P \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (PIDK \< 5)' } |
| CombinationCut   | (in_range( 1879\*MeV, AM, 2059\*MeV )) & ((APT1+APT2+APT3) \> 3000\*MeV ) & (AHASCHILD(PT \> 1000.0\*MeV)) & (ANUM(PT \> 400.0\*MeV) \>= 2) & (AHASCHILD((MIPCHI2DV(PRIMARY)) \> 50.0))& (ANUM(MIPCHI2DV(PRIMARY) \> 10.0) \>= 2)                                                                                                                                                                                                                                                                                                                                            |
| MotherCut        | in_range( 1889.0 , M , 2049.0 ) & (VFASPF(VCHI2PDOF) \< 6) & (BPVDIRA \> math.cos( 14.1 )) & (BPVLTIME() \> 0.2\*ps )                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptor  | [D_s+ -\> K+ K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[D_s+ -\> K+ K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output           | Phys/Ds1DalitzDecaysDs2KKpiKLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
