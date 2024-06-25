[[stripping21 lines]](./stripping21-index)

# StrippingD2XMuMu_Lambdac2PPiPiLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/D2XMuMu_Lambdac2PPiPiLine/Particles |
| Postscale      | 1.0000000                                |
| HLT            | None                                     |
| Prescale       | 0.010000000                              |
| L0DU           | None                                     |
| ODIN           | None                                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsProtons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsProtons](./stripping21-commonparticles-stdallnopidsprotons)/Particles')\>0 |

FilterDesktop/ProtonsFor3bodyCSAndForD2XMuMu

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 2000.0 \*MeV) & (PT \> 300.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 6) |
| Inputs          | [ 'Phys/[StdAllNoPIDsProtons](./stripping21-commonparticles-stdallnopidsprotons)' ]    |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/ProtonsFor3bodyCSAndForD2XMuMu/Particles                                            |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/PionsFor3bodyCSAndForD2XMuMu

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 2000.0 \*MeV) & (PT \> 300.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 6) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]        |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/PionsFor3bodyCSAndForD2XMuMu/Particles                                              |

CombineParticles/D2XMuMu_Lambdac2PPiPiLine

|                  |                                                                                      |
|------------------|--------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsFor3bodyCSAndForD2XMuMu' , 'Phys/ProtonsFor3bodyCSAndForD2XMuMu' ]    |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }        |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 100.0 \*MeV) & (AMAXDOCA('')\<0.15) & (AM23 \> 250.0 \*MeV) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5) & (BPVIPCHI2()\< 25) & (BPVDIRA \> 0.9999)                 |
| DecayDescriptor  | [Lambda_c+ -\> p+ pi+ pi-]cc                                                       |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ pi+ pi-]cc' ]                                               |
| Output           | Phys/D2XMuMu_Lambdac2PPiPiLine/Particles                                             |

AddRelatedInfo/RelatedInfo1_D2XMuMu_Lambdac2PPiPiLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/D2XMuMu_Lambdac2PPiPiLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo1_D2XMuMu_Lambdac2PPiPiLine/Particles |
