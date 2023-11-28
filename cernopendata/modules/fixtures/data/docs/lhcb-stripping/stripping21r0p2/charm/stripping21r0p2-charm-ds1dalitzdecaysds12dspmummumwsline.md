[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingDs1DalitzDecaysDs12DspmummumWSLine

## Properties:

|                |                                                   |
|----------------|---------------------------------------------------|
| OutputLocation | Phys/Ds1DalitzDecaysDs12DspmummumWSLine/Particles |
| Postscale      | 1.0000000                                         |
| HLT1           | None                                              |
| HLT2           | None                                              |
| Prescale       | 1.0000000                                         |
| L0DU           | None                                              |
| ODIN           | None                                              |

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

CombineParticles/Ds2KKpiForDs1DalitzDecays

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r0p2-commonparticles-stdallnopidskaons)' , 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.4) & (PT \> 250\*MeV) & (P \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (PIDK \> 5)' , 'K-' : '(TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.4) & (PT \> 250\*MeV) & (P \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (PIDK \> 5)' , 'pi+' : '(TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.4) & (PT \> 250\*MeV) & (P \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (PIDK \< 5)' , 'pi-' : '(TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.4) & (PT \> 250\*MeV) & (P \> 1000\*MeV) & (MIPCHI2DV(PRIMARY) \> 4.0) & (PIDK \< 5)' } |
| CombinationCut   | (in_range( 1879\*MeV, AM, 2059\*MeV )) & ((APT1+APT2+APT3) \> 3000\*MeV ) & (AHASCHILD(PT \> 1000.0\*MeV)) & (ANUM(PT \> 400.0\*MeV) \>= 2) & (AHASCHILD((MIPCHI2DV(PRIMARY)) \> 50.0))& (ANUM(MIPCHI2DV(PRIMARY) \> 10.0) \>= 2)                                                                                                                                                                                                                                                                                                                                            |
| MotherCut        | in_range( 1889.0 , M , 2049.0 ) & (VFASPF(VCHI2PDOF) \< 6) & (BPVDIRA \> math.cos( 14.1 )) & (BPVLTIME() \> 0.2\*ps )                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptor  | [D_s+ -\> K+ K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptors | [ '[D_s+ -\> K+ K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Output           | Phys/Ds2KKpiForDs1DalitzDecays/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsMuons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsMuons/Particles',True) |

CombineParticles/Ds1DalitzDecaysDs12DspmummumWSLine

|                  |                                                                                                                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Ds2KKpiForDs1DalitzDecays' , 'Phys/[StdAllNoPIDsMuons](./stripping21r0p2-commonparticles-stdallnopidsmuons)' ]                                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'D_s+' : 'ALL' , 'D_s-' : 'ALL' , 'mu+' : '(ISMUON) & (BPVIPCHI2() \< 9) & (TRGHOSTPROB\<0.3) & (PT\> 200 \* MeV)' , 'mu-' : '(ISMUON) & (BPVIPCHI2() \< 9) & (TRGHOSTPROB\<0.3) & (PT\> 200 \* MeV)' } |
| CombinationCut   | (AM -AM1 \< (1.2\*2000\*MeV))                                                                                                                                                                                          |
| MotherCut        | ((M-M1) \< 2000\*MeV) & (VFASPF(VCHI2PDOF) \< 20)                                                                                                                                                                      |
| DecayDescriptor  | [D_s1(2536)+ -\> D_s+ mu- mu-]cc                                                                                                                                                                                     |
| DecayDescriptors | [ '[D_s1(2536)+ -\> D_s+ mu- mu-]cc' ]                                                                                                                                                                             |
| Output           | Phys/Ds1DalitzDecaysDs12DspmummumWSLine/Particles                                                                                                                                                                      |
