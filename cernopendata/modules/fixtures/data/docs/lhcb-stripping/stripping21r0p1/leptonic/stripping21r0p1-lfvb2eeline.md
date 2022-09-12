[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingLFVB2eeLine

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/LFVB2eeLine/Particles |
| Postscale      | 1.0000000                  |
| HLT1           | None                       |
| HLT2           | None                       |
| Prescale       | 1.0000000                  |
| L0DU           | None                       |
| ODIN           | None                       |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles**

|      |                                                                                               |
|------|-----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseElectrons](./stripping21r0p1-stdlooseelectrons) /Particles',True)\>0 |

**CombineParticles/LFVB2eeLine**

|                  |                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r0p1-stdlooseelectrons) ' ]                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 )' , 'e-' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 )' } |
| CombinationCut   | (ADAMASS('B_s0')\<1200\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 1200\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 225)& (BPVIPCHI2()\< 25)               |
| DecayDescriptor  | None                                                                                                                           |
| DecayDescriptors | [ 'B_s0 -\> e+ e-' , '[B_s0 -\> e+ e+]cc' ]                                                                                |
| Output           | Phys/LFVB2eeLine/Particles                                                                                                     |

**AddRelatedInfo/RelatedInfo1_LFVB2eeLine**

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/LFVB2eeLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo1_LFVB2eeLine/Particles |

**AddRelatedInfo/RelatedInfo2_LFVB2eeLine**

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/LFVB2eeLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo2_LFVB2eeLine/Particles |

**AddRelatedInfo/RelatedInfo3_LFVB2eeLine**

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/LFVB2eeLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo3_LFVB2eeLine/Particles |

**AddRelatedInfo/RelatedInfo4_LFVB2eeLine**

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/LFVB2eeLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo4_LFVB2eeLine/Particles |

**AddRelatedInfo/RelatedInfo5_LFVB2eeLine**

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/LFVB2eeLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo5_LFVB2eeLine/Particles |

**AddRelatedInfo/RelatedInfo6_LFVB2eeLine**

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/LFVB2eeLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo6_LFVB2eeLine/Particles |
