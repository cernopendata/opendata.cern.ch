[[stripping21 lines]](./stripping21-index)

# StrippingBs2MuMusLTUBLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/Bs2MuMusLTUBLine/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

CombineParticles/Bs2MuMusLTUBLine

|                  |                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' ]                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(PT \> 500\*MeV) & (TRCHI2DOF \< 3 ) & (0.5 500\*MeV) & (TRCHI2DOF \< 3 ) & (0.5                                        |
| CombinationCut   | (ADAMASS('B_s0')\<500\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 500\*MeV )& (BPVIPCHI2()\< 25) & (BPVLTIME()\>0.6\*ps)& (BPVLTIME()\<13.248\*ps)& (PT \> 500\*MeV) |
| DecayDescriptor  | B_s0 -\> mu+ mu-                                                                                                                                |
| DecayDescriptors | [ 'B_s0 -\> mu+ mu-' ]                                                                                                                        |
| Output           | Phys/Bs2MuMusLTUBLine/Particles                                                                                                                 |

AddRelatedInfo/RelatedInfo1_Bs2MuMusLTUBLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusLTUBLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_Bs2MuMusLTUBLine/Particles |

AddRelatedInfo/RelatedInfo2_Bs2MuMusLTUBLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusLTUBLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo2_Bs2MuMusLTUBLine/Particles |

AddRelatedInfo/RelatedInfo3_Bs2MuMusLTUBLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusLTUBLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo3_Bs2MuMusLTUBLine/Particles |

AddRelatedInfo/RelatedInfo4_Bs2MuMusLTUBLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusLTUBLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo4_Bs2MuMusLTUBLine/Particles |

AddRelatedInfo/RelatedInfo5_Bs2MuMusLTUBLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusLTUBLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo5_Bs2MuMusLTUBLine/Particles |

AddRelatedInfo/RelatedInfo6_Bs2MuMusLTUBLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusLTUBLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo6_Bs2MuMusLTUBLine/Particles |

AddRelatedInfo/RelatedInfo7_Bs2MuMusLTUBLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusLTUBLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo7_Bs2MuMusLTUBLine/Particles |

AddRelatedInfo/RelatedInfo8_Bs2MuMusLTUBLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusLTUBLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo8_Bs2MuMusLTUBLine/Particles |

AddRelatedInfo/RelatedInfo9_Bs2MuMusLTUBLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusLTUBLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo9_Bs2MuMusLTUBLine/Particles |
