[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2HHPi0_M

## Properties:

|                |                          |
|----------------|--------------------------|
| OutputLocation | Phys/B2HHPi0_M/Particles |
| Postscale      | 1.0000000                |
| HLT1           | None                     |
| HLT2           | None                     |
| Prescale       | 1.0000000                |
| L0DU           | None                     |
| ODIN           | None                     |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

CombineParticles/B2HHPi0_M

|                  |                                                                                                                                                                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p2-commonparticles-stdloosemergedpi0)' , 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ]                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT\>500 \*MeV) & (P\>5000 \*MeV) & (TRPCHI2\>1e-06) & (TRGHOSTPROB\<0.5) & (MIPCHI2DV(PRIMARY)\>25)' , 'pi-' : '(PT\>500 \*MeV) & (P\>5000 \*MeV) & (TRPCHI2\>1e-06) & (TRGHOSTPROB\<0.5) & (MIPCHI2DV(PRIMARY)\>25)' , 'pi0' : '(PT\>2500 \*MeV)' } |
| CombinationCut   | (AM\>4200 \*MeV) & (AM\<6400 \*MeV)                                                                                                                                                                                                                                           |
| MotherCut        | (PT\>3000 \*MeV) & (VFASPF(VPCHI2)\>0.001) & (BPVVDCHI2\>64) & (BPVIPCHI2()\<9) & (BPVDIRA\>0.99995)                                                                                                                                                                          |
| DecayDescriptor  | B0 -\> pi+ pi- pi0                                                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'B0 -\> pi+ pi- pi0' ]                                                                                                                                                                                                                                                    |
| Output           | Phys/B2HHPi0_M/Particles                                                                                                                                                                                                                                                      |

AddRelatedInfo/RelatedInfo1_B2HHPi0_M

|                 |                                       |
|-----------------|---------------------------------------|
| Inputs          | [ 'Phys/B2HHPi0_M' ]                |
| DecayDescriptor | None                                  |
| Output          | Phys/RelatedInfo1_B2HHPi0_M/Particles |

AddRelatedInfo/RelatedInfo2_B2HHPi0_M

|                 |                                       |
|-----------------|---------------------------------------|
| Inputs          | [ 'Phys/B2HHPi0_M' ]                |
| DecayDescriptor | None                                  |
| Output          | Phys/RelatedInfo2_B2HHPi0_M/Particles |

AddRelatedInfo/RelatedInfo3_B2HHPi0_M

|                 |                                       |
|-----------------|---------------------------------------|
| Inputs          | [ 'Phys/B2HHPi0_M' ]                |
| DecayDescriptor | None                                  |
| Output          | Phys/RelatedInfo3_B2HHPi0_M/Particles |

AddRelatedInfo/RelatedInfo4_B2HHPi0_M

|                 |                                       |
|-----------------|---------------------------------------|
| Inputs          | [ 'Phys/B2HHPi0_M' ]                |
| DecayDescriptor | None                                  |
| Output          | Phys/RelatedInfo4_B2HHPi0_M/Particles |

AddRelatedInfo/RelatedInfo5_B2HHPi0_M

|                 |                                       |
|-----------------|---------------------------------------|
| Inputs          | [ 'Phys/B2HHPi0_M' ]                |
| DecayDescriptor | None                                  |
| Output          | Phys/RelatedInfo5_B2HHPi0_M/Particles |
