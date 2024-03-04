[[stripping21 lines]](./stripping21-index)

# StrippingXb2phhhLine

## Properties:

|                |                            |
|----------------|----------------------------|
| OutputLocation | Phys/Xb2phhhLine/Particles |
| Postscale      | 1.0000000                  |
| HLT            | None                       |
| Prescale       | 1.0000000                  |
| L0DU           | None                       |
| ODIN           | None                       |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNProtons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNProtons](./stripping21-commonparticles-stdlooseannprotons)/Particles')\>0 |

FilterDesktop/ProtonsForXb2p2hOrXb2p3h

|                 |                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.4) & (TRCHI2DOF \< 3.0) & (P \> 1500.0) & (PROBNNp \> 0.05) |
| Inputs          | [ 'Phys/[StdLooseANNProtons](./stripping21-commonparticles-stdlooseannprotons)' ]                          |
| DecayDescriptor | None                                                                                                         |
| Output          | Phys/ProtonsForXb2p2hOrXb2p3h/Particles                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)/Particles')\>0 |

FilterDesktop/PionsForXb2p2hOrXb2p3h

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.4) & (TRCHI2DOF \< 3.0) & (P \> 1500.0) |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)' ]              |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/PionsForXb2p2hOrXb2p3h/Particles                                                    |

DaVinci::N4BodyDecays/Xb2phhhLine

|                  |                                                                                                                                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForXb2p2hOrXb2p3h' , 'Phys/ProtonsForXb2p2hOrXb2p3h' ]                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                                           |
| CombinationCut   | (AM \< 6405.0\*MeV) & (AWM('p+','K-','K+','K-') \> 5195.0\*MeV) & ( (APT1 + APT2 + APT3 + APT4) \> 3500.0\*MeV) & (APT \> 1500.0\*MeV) & (ACHI2DOCA(1,4) \< 20.0) & (ACHI2DOCA(2,4) \< 20.0) & (ACHI2DOCA(3,4) \< 20.0) |
| MotherCut        | (VFASPF(VCHI2) \< 20.0) & (BPVVDCHI2 \> 50.0) & (BPVDIRA \> 0.9999) & (BPVIPCHI2() \< 16.0)                                                                                                                             |
| DecayDescriptor  | [Lambda_b0 -\> p+ pi- pi+ pi-]cc                                                                                                                                                                                      |
| DecayDescriptors | [ '[Lambda_b0 -\> p+ pi- pi+ pi-]cc' ]                                                                                                                                                                              |
| Output           | Phys/Xb2phhhLine/Particles                                                                                                                                                                                              |

AddRelatedInfo/RelatedInfo1_Xb2phhhLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/Xb2phhhLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo1_Xb2phhhLine/Particles |

AddRelatedInfo/RelatedInfo2_Xb2phhhLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/Xb2phhhLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo2_Xb2phhhLine/Particles |

AddRelatedInfo/RelatedInfo3_Xb2phhhLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/Xb2phhhLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo3_Xb2phhhLine/Particles |

AddRelatedInfo/RelatedInfo4_Xb2phhhLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/Xb2phhhLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo4_Xb2phhhLine/Particles |

AddRelatedInfo/RelatedInfo5_Xb2phhhLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/Xb2phhhLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo5_Xb2phhhLine/Particles |
