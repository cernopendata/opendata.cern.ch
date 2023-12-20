[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingBs2MuMuLinesBsstLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/Bs2MuMuLinesBsstLine/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

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

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)/Particles',True)\>0 |

CombineParticles/Bs2MuMuLinesBsstLine

|                  |                                                                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21r1p1-commonparticles-stdallloosemuons)' ]                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(PT \> 500\*MeV) & (TRCHI2DOF \< 3 ) & (0.5 0.4) & (P \< 500\*GeV) & ( TRGHOSTPROB \< 0.3 )' , 'mu-' : '(PT \> 500\*MeV) & (TRCHI2DOF \< 3 ) & (0.5 0.4) & (P \< 500\*GeV) & ( TRGHOSTPROB \< 0.3 )' } |
| CombinationCut   | (ADAMASS('B_s0')\<500\*MeV) & (ASUM(PT) \> 4500)& (AMAXDOCA('')\<0.3\*mm)                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 500\*MeV )& (BPVIPCHI2()\< 25) & (BPVLTIME()\>0.0\*ps)& (BPVLTIME()\<0.2\*ps)& (PT \> 500\*MeV)                                                                                   |
| DecayDescriptor  | B\*\_s0 -\> mu+ mu-                                                                                                                                                                                                            |
| DecayDescriptors | [ 'B\*\_s0 -\> mu+ mu-' ]                                                                                                                                                                                                    |
| Output           | Phys/Bs2MuMuLinesBsstLine/Particles                                                                                                                                                                                            |

AddRelatedInfo/RelatedInfo1_Bs2MuMuLinesBsstLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBsstLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_Bs2MuMuLinesBsstLine/Particles |

AddRelatedInfo/RelatedInfo2_Bs2MuMuLinesBsstLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBsstLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_Bs2MuMuLinesBsstLine/Particles |

AddRelatedInfo/RelatedInfo3_Bs2MuMuLinesBsstLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBsstLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_Bs2MuMuLinesBsstLine/Particles |

AddRelatedInfo/RelatedInfo4_Bs2MuMuLinesBsstLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBsstLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_Bs2MuMuLinesBsstLine/Particles |

AddRelatedInfo/RelatedInfo5_Bs2MuMuLinesBsstLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBsstLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo5_Bs2MuMuLinesBsstLine/Particles |

AddRelatedInfo/RelatedInfo6_Bs2MuMuLinesBsstLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBsstLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo6_Bs2MuMuLinesBsstLine/Particles |

AddRelatedInfo/RelatedInfo7_Bs2MuMuLinesBsstLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBsstLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo7_Bs2MuMuLinesBsstLine/Particles |

AddRelatedInfo/RelatedInfo8_Bs2MuMuLinesBsstLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBsstLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo8_Bs2MuMuLinesBsstLine/Particles |

AddRelatedInfo/RelatedInfo9_Bs2MuMuLinesBsstLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuLinesBsstLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo9_Bs2MuMuLinesBsstLine/Particles |
