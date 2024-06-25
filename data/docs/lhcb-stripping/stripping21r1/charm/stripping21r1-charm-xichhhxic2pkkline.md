[[stripping21r1 lines]](./stripping21r1-index)

# StrippingXicHHHXic2PKKLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/XicHHHXic2PKKLine/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNKaons](./stripping21r1-commonparticles-stdlooseannkaons)/Particles')\>0 |

FilterDesktop/KaonsforXicHHH

|                 |                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | HASRICH & (CLONEDIST \> 5000) & (TRGHOSTPROB \< 0.5) & (PROBNNk \> 0.1) &(TRGHP \< 0.4) & (MIPCHI2DV(PRIMARY) \> 9.0) & (P\>3000\*MeV) & (PT\>300\*MeV) &(TRCHI2DOF \< 4.0) |
| Inputs          | [ 'Phys/[StdLooseANNKaons](./stripping21r1-commonparticles-stdlooseannkaons)' ]                                                                                           |
| DecayDescriptor | None                                                                                                                                                                        |
| Output          | Phys/KaonsforXicHHH/Particles                                                                                                                                               |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNProtons_Particles

|      |                                                                                                              |
|------|--------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNProtons](./stripping21r1-commonparticles-stdalllooseannprotons)/Particles')\>0 |

FilterDesktop/ProtonsforXicHHH

|                 |                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------|
| Code            | HASRICH & (CLONEDIST \> 5000) & (TRGHOSTPROB \< 0.5) & (PROBNNp \> 0.5) &(TRGHP \< 0.4) & (P\> 3000.0\*MeV) & (TRCHI2DOF \< 4.0) |
| Inputs          | [ 'Phys/[StdAllLooseANNProtons](./stripping21r1-commonparticles-stdalllooseannprotons)' ]                                      |
| DecayDescriptor | None                                                                                                                             |
| Output          | Phys/ProtonsforXicHHH/Particles                                                                                                  |

CombineParticles/XicHHHXic2PKKLine

|                  |                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsforXicHHH' , 'Phys/ProtonsforXicHHH' ]                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                                                                            |
| CombinationCut   | (AM \> 2215.0)& (AM \< 2800.0)& (AMINCHILD(PT) \> 300.0)& (AMINCHILD(P) \> 3000.0)& ( ACHI2DOCA(1,3) \< 16 )& ( ACHI2DOCA(2,3) \< 16 )                 |
| MotherCut        | (PT \> 2000.0)& (VFASPF(VCHI2/VDOF) \< 12.0)& (BPVIPCHI2() \< 20.0)& (BPVVDCHI2 \> 0.0)& (BPVDIRA \> 0.99)& (BPVLTIME() \> 0.0)& (BPVLTIME() \< 0.005) |
| DecayDescriptor  | None                                                                                                                                                   |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ K- K+]cc' ]                                                                                                                   |
| Output           | Phys/XicHHHXic2PKKLine/Particles                                                                                                                       |

AddRelatedInfo/RelatedInfo1_XicHHHXic2PKKLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XicHHHXic2PKKLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo1_XicHHHXic2PKKLine/Particles |

AddRelatedInfo/RelatedInfo2_XicHHHXic2PKKLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XicHHHXic2PKKLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo2_XicHHHXic2PKKLine/Particles |

AddRelatedInfo/RelatedInfo3_XicHHHXic2PKKLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XicHHHXic2PKKLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo3_XicHHHXic2PKKLine/Particles |

AddRelatedInfo/RelatedInfo4_XicHHHXic2PKKLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XicHHHXic2PKKLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo4_XicHHHXic2PKKLine/Particles |

AddRelatedInfo/RelatedInfo5_XicHHHXic2PKKLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XicHHHXic2PKKLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo5_XicHHHXic2PKKLine/Particles |
