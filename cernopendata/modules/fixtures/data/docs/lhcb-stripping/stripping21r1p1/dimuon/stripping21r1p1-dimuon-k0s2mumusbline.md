[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingK0s2MuMuSBLine

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/K0s2MuMuSBLine/Particles |
| Postscale      | 1.0000000                     |
| HLT1           | None                          |
| HLT2           | None                          |
| Prescale       | 0.10000000                    |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionDimuon

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamDimuonBadEvent') & ~ALG_PASSED('StrippingStreamDimuonBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)/Particles',True)\>0 |

FilterDesktop/MuonsForRnS

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 36)                                                    |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p1-commonparticles-stdloosemuons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/MuonsForRnS/Particles                                                    |

CombineParticles/K0s2MuMuSBLine

|                  |                                                                                                |
|------------------|------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuonsForRnS' ]                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 100.)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 100.)' } |
| CombinationCut   | (ADAMASS('KS0')\<100\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                            |
| MotherCut        | ((M\<465)& (BPVDIRA\>0) & ((BPVVDSIGN\*M/P) \> 1.610411922) & (MIPDV(PRIMARY)\<0.4\*mm))       |
| DecayDescriptor  | KS0 -\> mu+ mu-                                                                                |
| DecayDescriptors | [ 'KS0 -\> mu+ mu-' ]                                                                        |
| Output           | Phys/K0s2MuMuSBLine/Particles                                                                  |
