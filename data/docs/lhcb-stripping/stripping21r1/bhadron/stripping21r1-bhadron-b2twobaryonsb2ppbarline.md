[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2TwoBaryonsB2PPbarLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2TwoBaryonsB2PPbarLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)/Particles')\>0 |

CombineParticles/B2TwoBaryonsB2PPbarLine

|                  |                                                                                                                                                                                                                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '(PT \> 900 \* MeV) & (P \< 300000 \* MeV) & ((PIDp-PIDpi) \> -1) & ( (PIDp-PIDK) \> -2 ) & (MIPCHI2DV(PRIMARY) \> 10) & (TRGHP \< 0.4 )' , 'p~-' : '(PT \> 900 \* MeV) & (P \< 300000 \* MeV) & ((PIDp-PIDpi) \> -1) & ( (PIDp-PIDK) \> -2 ) & (MIPCHI2DV(PRIMARY) \> 10) & (TRGHP \< 0.4 )' } |
| CombinationCut   | ( (ADAMASS('B0') \< 200 \* MeV) \| (ADAMASS('B_s0') \< 200 \* MeV) ) & ( AMAXCHILD(MAXTREE('p+'==ABSID,PT)) \> 2100 \* MeV ) & ( AMAXCHILD(MAXTREE('p+'==ABSID,MIPCHI2DV(PRIMARY))) \> 25 )                                                                                                                           |
| MotherCut        | (PT \> 1100 \* MeV) & ( VFASPF(VCHI2PDOF) \< 9 ) & ( BPVDIRA \> 0.9997 ) & ( BPVIPCHI2() \< 16 )                                                                                                                                                                                                                      |
| DecayDescriptor  | B0 -\> p+ p~-                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'B0 -\> p+ p~-' ]                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/B2TwoBaryonsB2PPbarLine/Particles                                                                                                                                                                                                                                                                                |

AddRelatedInfo/RelatedInfo1_B2TwoBaryonsB2PPbarLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PPbarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo1_B2TwoBaryonsB2PPbarLine/Particles |

AddRelatedInfo/RelatedInfo2_B2TwoBaryonsB2PPbarLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PPbarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo2_B2TwoBaryonsB2PPbarLine/Particles |

AddRelatedInfo/RelatedInfo3_B2TwoBaryonsB2PPbarLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PPbarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo3_B2TwoBaryonsB2PPbarLine/Particles |

AddRelatedInfo/RelatedInfo4_B2TwoBaryonsB2PPbarLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PPbarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo4_B2TwoBaryonsB2PPbarLine/Particles |

AddRelatedInfo/RelatedInfo5_B2TwoBaryonsB2PPbarLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PPbarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo5_B2TwoBaryonsB2PPbarLine/Particles |

AddRelatedInfo/RelatedInfo6_B2TwoBaryonsB2PPbarLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Inputs          | [ 'Phys/B2TwoBaryonsB2PPbarLine' ]                |
| DecayDescriptor | None                                                |
| Output          | Phys/RelatedInfo6_B2TwoBaryonsB2PPbarLine/Particles |
