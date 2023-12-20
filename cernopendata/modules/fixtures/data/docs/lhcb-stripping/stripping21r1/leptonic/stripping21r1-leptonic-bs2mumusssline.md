[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBs2MuMusSSLine

## Properties:

|                |                               |
|----------------|-------------------------------|
| OutputLocation | Phys/Bs2MuMusSSLine/Particles |
| Postscale      | 1.0000000                     |
| HLT            | None                          |
| Prescale       | 1.0000000                     |
| L0DU           | None                          |
| ODIN           | None                          |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

CombineParticles/Bs2MuMusSSLine

|                  |                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 9 )&(TRCHI2DOF \< 3 )' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 9 )&(TRCHI2DOF \< 3 )' } |
| CombinationCut   | (ADAMASS('B_s0')\<200\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                           |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 200\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 121)& (BPVIPCHI2()\< 25)                |
| DecayDescriptor  | [B_s0 -\> mu+ mu+]cc                                                                                                         |
| DecayDescriptors | [ '[B_s0 -\> mu+ mu+]cc' ]                                                                                                 |
| Output           | Phys/Bs2MuMusSSLine/Particles                                                                                                  |

AddRelatedInfo/RelatedInfo1_Bs2MuMusSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo1_Bs2MuMusSSLine/Particles |

AddRelatedInfo/RelatedInfo2_Bs2MuMusSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo2_Bs2MuMusSSLine/Particles |

AddRelatedInfo/RelatedInfo3_Bs2MuMusSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo3_Bs2MuMusSSLine/Particles |

AddRelatedInfo/RelatedInfo4_Bs2MuMusSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo4_Bs2MuMusSSLine/Particles |

AddRelatedInfo/RelatedInfo5_Bs2MuMusSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo5_Bs2MuMusSSLine/Particles |

AddRelatedInfo/RelatedInfo6_Bs2MuMusSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo6_Bs2MuMusSSLine/Particles |

AddRelatedInfo/RelatedInfo7_Bs2MuMusSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo7_Bs2MuMusSSLine/Particles |

AddRelatedInfo/RelatedInfo8_Bs2MuMusSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo8_Bs2MuMusSSLine/Particles |

AddRelatedInfo/RelatedInfo9_Bs2MuMusSSLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMusSSLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo9_Bs2MuMusSSLine/Particles |
