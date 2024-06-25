[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2XMuMu_KKPiPiLine

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/D2XMuMu_KKPiPiLine/Particles |
| Postscale      | 1.0000000                         |
| HLT            | None                              |
| Prescale       | 0.010000000                       |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/HadFor4bodyCSAndForD2XMuMu

|                 |                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 2000.0 \*MeV) & (PT \> 300 \*MeV) &(MIPCHI2DV(PRIMARY) \> 3.0) & ( TRGHOSTPROB \< 0.5 ) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' ]                              |
| DecayDescriptor | None                                                                                                             |
| Output          | Phys/HadFor4bodyCSAndForD2XMuMu/Particles                                                                        |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/PionsFor4bodyCSAndForD2XMuMu

|                 |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 2000.0 \*MeV) & (PT \> 300\* MeV) & (MIPCHI2DV(PRIMARY) \> 3.0) & ( TRGHOSTPROB \< 0.5 ) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                               |
| DecayDescriptor | None                                                                                                              |
| Output          | Phys/PionsFor4bodyCSAndForD2XMuMu/Particles                                                                       |

CombineParticles/D2XMuMu_KKPiPiLine

|                  |                                                                                                                                                                            |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/HadFor4bodyCSAndForD2XMuMu' , 'Phys/PionsFor4bodyCSAndForD2XMuMu' ]                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                               |
| CombinationCut   | (ADAMASS('D0') \< 100.0 \*MeV) & (AMAXDOCA('')\<0.2) & (AM \> 1763.0 \*MeV) &(AHASCHILD( (ABSID=='K+') & (PIDK-PIDpi \> -1.0) )) &(AHASCHILD( (MIPCHI2DV(PRIMARY)\>15) ) ) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 8) & (PT \> 2500.0 \*MeV) &(BPVVDCHI2\>36) & (BPVIPCHI2()\< 16) & (BPVDIRA \> 0.9999)                                                               |
| DecayDescriptor  | D0 -\> K+ K- pi+ pi-                                                                                                                                                       |
| DecayDescriptors | [ 'D0 -\> K+ K- pi+ pi-' ]                                                                                                                                               |
| Output           | Phys/D2XMuMu_KKPiPiLine/Particles                                                                                                                                          |

AddRelatedInfo/RelatedInfo1_D2XMuMu_KKPiPiLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/D2XMuMu_KKPiPiLine' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/RelatedInfo1_D2XMuMu_KKPiPiLine/Particles |
