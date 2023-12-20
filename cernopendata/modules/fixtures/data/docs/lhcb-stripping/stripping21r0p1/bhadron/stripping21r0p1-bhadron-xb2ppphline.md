[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingXb2ppphLine

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/Xb2ppphLine/Particles |
| Postscale      | 1.0000000                  |
| HLT1           | None                       |
| HLT2           | None                       |
| Prescale       | 1.0000000                  |
| L0DU           | None                       |
| ODIN           | None                       |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseANNProtons_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNProtons](./stripping21r0p1-commonparticles-stdlooseannprotons)/Particles',True)\>0 |

FilterDesktop/ProtonsForXb23ph

|                 |                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.4) & (TRCHI2DOF \< 4.0) & (P \> 1500.0) & (PROBNNp \> 0.05) |
| Inputs          | [ 'Phys/[StdLooseANNProtons](./stripping21r0p1-commonparticles-stdlooseannprotons)' ]                      |
| DecayDescriptor | None                                                                                                         |
| Output          | Phys/ProtonsForXb23ph/Particles                                                                              |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                                       |
|------|-------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21r0p1-commonparticles-stdnopidspions)/Particles',True)\>0 |

FilterDesktop/PionsForXb23ph

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.4) & (TRCHI2DOF \< 4.0) & (P \> 1500.0) |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r0p1-commonparticles-stdnopidspions)' ]          |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/PionsForXb23ph/Particles                                                            |

DaVinci::N4BodyDecays/Xb2ppphLine

|                  |                                                                                                                                                                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForXb23ph' , 'Phys/ProtonsForXb23ph' ]                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                            |
| CombinationCut   | (AM \< 6405.0\*MeV) & (AWM('p+','p~-','p+','K-') \> 5195.0\*MeV) & ( (APT1 + APT2 + APT3 + APT4) \> 3500.0\*MeV) & (APT \> 1500.0\*MeV) & (ACHI2DOCA(1,4) \< 20.0) & (ACHI2DOCA(2,4) \< 20.0) & (ACHI2DOCA(3,4) \< 20.0) |
| MotherCut        | (VFASPF(VCHI2) \< 20.0) & (BPVVDCHI2 \> 50.0) & (BPVDIRA \> 0.9999) & (BPVIPCHI2() \< 16.0)                                                                                                                              |
| DecayDescriptor  | [Lambda_b0 -\> p+ p~- p+ pi-]cc                                                                                                                                                                                        |
| DecayDescriptors | [ '[Lambda_b0 -\> p+ p~- p+ pi-]cc' ]                                                                                                                                                                                |
| Output           | Phys/Xb2ppphLine/Particles                                                                                                                                                                                               |

AddRelatedInfo/RelatedInfo1_Xb2ppphLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/Xb2ppphLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo1_Xb2ppphLine/Particles |

AddRelatedInfo/RelatedInfo2_Xb2ppphLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/Xb2ppphLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo2_Xb2ppphLine/Particles |

AddRelatedInfo/RelatedInfo3_Xb2ppphLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/Xb2ppphLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo3_Xb2ppphLine/Particles |

AddRelatedInfo/RelatedInfo4_Xb2ppphLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/Xb2ppphLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo4_Xb2ppphLine/Particles |

AddRelatedInfo/RelatedInfo5_Xb2ppphLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/Xb2ppphLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo5_Xb2ppphLine/Particles |
