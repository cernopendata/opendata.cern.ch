[[stripping21r1 lines]](./stripping21r1-index)

# StrippingXicHHHTheta2PKS0Line

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/XicHHHTheta2PKS0Line/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/KSforXicHHH

|                 |                                                                                                                                                                                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MIPDV(PRIMARY)\<5.\*mm)&(BPVDIRA\>0)&(MM\>487.\*MeV)&(MM\<507.\*MeV)&(VFASPF(VCHI2PDOF)\<10.)&(P\>4000.\*MeV)&(PT\>1500.\*MeV)&(BPVLTIME()\>0.01\*ns)&CHILDCUT((MIPCHI2DV(PRIMARY)\>50.),1)&CHILDCUT((MIPCHI2DV(PRIMARY)\>50.),2)&CHILDCUT((TRCHI2DOF\<4.),1)&CHILDCUT((TRCHI2DOF\<4.),2) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r1-commonparticles-stdlooseksll)' ]                                                                                                                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                       |
| Output          | Phys/KSforXicHHH/Particles                                                                                                                                                                                                                                                                 |

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

CombineParticles/XicHHHTheta2PKS0Line

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KSforXicHHH' , 'Phys/ProtonsforXicHHH' ]                                 |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                      |
| CombinationCut   | (AM \> 1440.0)& (AM \< 1800.0)& (AMINCHILD(P) \> 3000.0)& (AMINCHILD(PT) \> 300.0) |
| MotherCut        | (PT \> 1500\*MeV) & (MIPDV(PRIMARY)\< 1.0 \* mm)                                   |
| DecayDescriptor  | None                                                                               |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ KS0]cc' ]                                                 |
| Output           | Phys/XicHHHTheta2PKS0Line/Particles                                                |

AddRelatedInfo/RelatedInfo1_XicHHHTheta2PKS0Line

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/XicHHHTheta2PKS0Line' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_XicHHHTheta2PKS0Line/Particles |

AddRelatedInfo/RelatedInfo2_XicHHHTheta2PKS0Line

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/XicHHHTheta2PKS0Line' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo2_XicHHHTheta2PKS0Line/Particles |

AddRelatedInfo/RelatedInfo3_XicHHHTheta2PKS0Line

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/XicHHHTheta2PKS0Line' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo3_XicHHHTheta2PKS0Line/Particles |

AddRelatedInfo/RelatedInfo4_XicHHHTheta2PKS0Line

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/XicHHHTheta2PKS0Line' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo4_XicHHHTheta2PKS0Line/Particles |

AddRelatedInfo/RelatedInfo5_XicHHHTheta2PKS0Line

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/XicHHHTheta2PKS0Line' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo5_XicHHHTheta2PKS0Line/Particles |
