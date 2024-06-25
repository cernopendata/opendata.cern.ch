[[stripping21 lines]](./stripping21-index)

# StrippingD2XMuMu_K2PiLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/D2XMuMu_K2PiLine/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 0.0050000000                    |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)/Particles')\>0 |

FilterDesktop/HadFor3bodyCSAndForD2XMuMu

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 2000.0 \*MeV) & (PT \> 300.0 \*MeV) &(MIPCHI2DV(PRIMARY) \> 6) |
| Inputs          | [ 'Phys/[StdAllNoPIDsKaons](./stripping21-commonparticles-stdallnopidskaons)' ]       |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/HadFor3bodyCSAndForD2XMuMu/Particles                                               |

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

CombineParticles/D2XMuMu_K2PiLine

|                  |                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/HadFor3bodyCSAndForD2XMuMu' , 'Phys/PionsFor3bodyCSAndForD2XMuMu' ]                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                             |
| CombinationCut   | (ADAMASS('D+') \< 200.0 \*MeV) & (AMAXDOCA('')\<0.15) & (AM \> 1763.0 \*MeV) &(AM23 \> 250.0 \*MeV) &(AHASCHILD( (ABSID=='K+') & (PIDK-PIDpi \> -1.0) )) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5) & (BPVIPCHI2()\< 25) & (BPVDIRA \> 0.9999)                                                                                     |
| DecayDescriptor  | [D+ -\> K- pi+ pi+]cc                                                                                                                                  |
| DecayDescriptors | [ '[D+ -\> K- pi+ pi+]cc' ]                                                                                                                          |
| Output           | Phys/D2XMuMu_K2PiLine/Particles                                                                                                                          |

AddRelatedInfo/RelatedInfo1_D2XMuMu_K2PiLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/D2XMuMu_K2PiLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_D2XMuMu_K2PiLine/Particles |
