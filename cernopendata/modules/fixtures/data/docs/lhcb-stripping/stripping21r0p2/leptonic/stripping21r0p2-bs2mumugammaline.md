[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBs2MuMuGammaLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/Bs2MuMuGammaLine/Particles |
| Postscale      | 1.0000000                       |
| HLT1           | None                            |
| HLT2           | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseMuons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseMuons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons**

|      |                                        |
|------|----------------------------------------|
| Code | 0 StdLooseAllPhotons /Particles',True) |

**DaVinci::N3BodyDecays/Bs2MuMuGammaLine**

|                  |                                                                                                                                                                                                                                                |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseAllPhotons](./stripping21r0p2-stdlooseallphotons) ' , 'Phys/ [StdLooseMuons](./stripping21r0p2-stdloosemuons) ' ]                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : '(PT \> 500\*MeV) & (E \> 1500\*MeV) & (CL \> 0.2)' , 'mu+' : '(MIPCHI2DV(PRIMARY) \> 9) & (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.4)' , 'mu-' : '(MIPCHI2DV(PRIMARY) \> 9) & (TRCHI2DOF \< 3) & (TRGHOSTPROB \< 0.4)' } |
| CombinationCut   | (AM \< 7000\*MeV) & (APT \> 500\*MeV)                                                                                                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 15) & (ADMASS('B_s0') \< 1500\*MeV) & (BPVDIRA \> 0.995) & (PT \> 350\*MeV) & (BPVIPCHI2() \< 20)                                                                                                                       |
| DecayDescriptor  | B_s0 -\> mu+ mu- gamma                                                                                                                                                                                                                         |
| DecayDescriptors | [ 'B_s0 -\> mu+ mu- gamma' ]                                                                                                                                                                                                                 |
| Output           | Phys/Bs2MuMuGammaLine/Particles                                                                                                                                                                                                                |

**AddRelatedInfo/RelatedInfo1_Bs2MuMuGammaLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuGammaLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_Bs2MuMuGammaLine/Particles |

**AddRelatedInfo/RelatedInfo2_Bs2MuMuGammaLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuGammaLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo2_Bs2MuMuGammaLine/Particles |

**AddRelatedInfo/RelatedInfo3_Bs2MuMuGammaLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuGammaLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo3_Bs2MuMuGammaLine/Particles |

**AddRelatedInfo/RelatedInfo4_Bs2MuMuGammaLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuGammaLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo4_Bs2MuMuGammaLine/Particles |

**AddRelatedInfo/RelatedInfo5_Bs2MuMuGammaLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuGammaLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo5_Bs2MuMuGammaLine/Particles |

**AddRelatedInfo/RelatedInfo6_Bs2MuMuGammaLine**

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/Bs2MuMuGammaLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo6_Bs2MuMuGammaLine/Particles |
