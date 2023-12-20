[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB24pB24pLine

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/B24pB24pLine/Particles |
| Postscale      | 1.0000000                   |
| HLT1           | None                        |
| HLT2           | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r0p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

DaVinci::N4BodyDecays/B24pB24pLine

|                  |                                                                                                                                                                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseProtons](./stripping21r0p1-commonparticles-stdlooseprotons)' ]                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : '\n ( MIPCHI2DV(PRIMARY) \> 25.0 )\n & ( TRCHI2DOF \< 4.0 )\n & ( TRGHP \< 0.3 )\n & ((PIDp-PIDpi)\>0) & ((PIDp-PIDK)\>-5)' , 'p~-' : '\n ( MIPCHI2DV(PRIMARY) \> 25.0 )\n & ( TRCHI2DOF \< 4.0 )\n & ( TRGHP \< 0.3 )\n & ((PIDp-PIDpi)\>0) & ((PIDp-PIDK)\>-5)' } |
| CombinationCut   | (ADAMASS(5323\*MeV) \< 400\*MeV) & (ADOCA(1,4) \< 0.3\*mm) & (ADOCA(2,4) \< 0.3\*mm) & (ADOCA(3,4) \< 0.3\*mm)                                                                                                                                                                            |
| MotherCut        | (BPVIPCHI2() \< 25 ) & (BPVVDCHI2 \> 225 ) & (VFASPF(VCHI2/VDOF) \< 9 ) & (BPVDIRA \> 0.0 ) & (BPVLTIME() \> 1.0\*ps )                                                                                                                                                                    |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                      |
| DecayDescriptors | [ 'B0 -\> p+ p+ p~- p~-' , '[B0 -\> p+ p+ p+ p~-]cc' ]                                                                                                                                                                                                                                |
| Output           | Phys/B24pB24pLine/Particles                                                                                                                                                                                                                                                               |

AddRelatedInfo/RelatedInfo1_B24pB24pLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B24pB24pLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo1_B24pB24pLine/Particles |

AddRelatedInfo/RelatedInfo2_B24pB24pLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B24pB24pLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo2_B24pB24pLine/Particles |

AddRelatedInfo/RelatedInfo3_B24pB24pLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B24pB24pLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo3_B24pB24pLine/Particles |

AddRelatedInfo/RelatedInfo4_B24pB24pLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B24pB24pLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo4_B24pB24pLine/Particles |

AddRelatedInfo/RelatedInfo5_B24pB24pLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B24pB24pLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo5_B24pB24pLine/Particles |

AddRelatedInfo/RelatedInfo6_B24pB24pLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B24pB24pLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo6_B24pB24pLine/Particles |

AddRelatedInfo/RelatedInfo7_B24pB24pLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B24pB24pLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo7_B24pB24pLine/Particles |

AddRelatedInfo/RelatedInfo8_B24pB24pLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/B24pB24pLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo8_B24pB24pLine/Particles |
