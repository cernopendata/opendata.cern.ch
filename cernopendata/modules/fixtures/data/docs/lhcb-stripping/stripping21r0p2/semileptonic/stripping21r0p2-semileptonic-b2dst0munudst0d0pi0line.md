[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2Dst0MuNuDst0D0Pi0Line

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2Dst0MuNuDst0D0Pi0Line/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

CombineParticles/D0ForB2Dst0MuNu

|                  |                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' , 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PIDK \> 0) & (PT \> 250\*MeV)' , 'K-' : '(PIDK \> 0) & (PT \> 250\*MeV)' , 'pi+' : '(PIDK \< 2) & (PT \> 250\*MeV)' , 'pi-' : '(PIDK \< 2) & (PT \> 250\*MeV)' } |
| CombinationCut   | (AM \> 1700\*MeV) & (AM \< 2000\*MeV) & (ADOCACHI2CUT(10, ''))                                                                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 4) & (BPVVDCHI2 \> 100.) & (BPVDIRA\> 0.99) & (ADMASS('D0') \< 100\*MeV)                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                     |
| DecayDescriptors | [ '[D0 -\> K- pi+]cc' ]                                                                                                                                                              |
| Output           | Phys/D0ForB2Dst0MuNu/Particles                                                                                                                                                           |

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

CombineParticles/DstD0Pi0ForB2Dst0MuNu

|                  |                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D0ForB2Dst0MuNu' , 'Phys/[StdLooseMergedPi0](./stripping21r0p2-commonparticles-stdloosemergedpi0)' , 'Phys/[StdLooseResolvedPi0](./stripping21r0p2-commonparticles-stdlooseresolvedpi0)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi0' : '(PT \> 500\*MeV)' }                                                                                                                           |
| CombinationCut   | (AM - ACHILD(1,M) \< 350\*MeV)                                                                                                                                                                       |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6)                                                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                 |
| DecayDescriptors | [ '[D\*(2007)0 -\> D0 pi0]cc' ]                                                                                                                                                                  |
| Output           | Phys/DstD0Pi0ForB2Dst0MuNu/Particles                                                                                                                                                                 |

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

CombineParticles/B2Dst0MuNuDst0D0Pi0Line

|                  |                                                                                                                                                                                                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DstD0Pi0ForB2Dst0MuNu' , 'Phys/[StdLooseMuons](./stripping21r0p2-commonparticles-stdloosemuons)' ]                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2007)0' : 'ALL' , 'D\*(2007)~0' : 'ALL' , 'mu+' : '(PT \> 1200\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (PIDmu \> 0)' , 'mu-' : '(PT \> 1200\*MeV) & (MIPCHI2DV(PRIMARY) \> 16) & (PIDmu \> 0)' } |
| CombinationCut   | (AM \> 2200\*MeV) & (AM \< 6000\*MeV)                                                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6) & (BPVVDCHI2 \> 25.) & (BPVDIRA\> 0.99)                                                                                                                                                 |
| DecayDescriptor  | None                                                                                                                                                                                                              |
| DecayDescriptors | [ '[B- -\> D\*(2007)0 mu-]cc' ]                                                                                                                                                                               |
| Output           | Phys/B2Dst0MuNuDst0D0Pi0Line/Particles                                                                                                                                                                            |
