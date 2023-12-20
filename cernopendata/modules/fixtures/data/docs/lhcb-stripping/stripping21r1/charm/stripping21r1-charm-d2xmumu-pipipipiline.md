[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2XMuMu_PiPiPiPiLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/D2XMuMu_PiPiPiPiLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 0.010000000                         |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

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

CombineParticles/D2XMuMu_PiPiPiPiLine

|                  |                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsFor4bodyCSAndForD2XMuMu' ]                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                        |
| CombinationCut   | (ADAMASS('D0') \< 100.0 \*MeV) & (AMAXDOCA('')\<0.2) & (AM \> 1763.0 \*MeV) &(AHASCHILD( (MIPCHI2DV(PRIMARY)\>15) ) ) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 8) & (BPVVDCHI2\>36) & (BPVIPCHI2()\< 16) & (PT \> 2500.0 \*MeV) &(BPVDIRA \> 0.9999)          |
| DecayDescriptor  | D0 -\> pi+ pi- pi+ pi-                                                                                                |
| DecayDescriptors | [ 'D0 -\> pi+ pi- pi+ pi-' ]                                                                                        |
| Output           | Phys/D2XMuMu_PiPiPiPiLine/Particles                                                                                   |

AddRelatedInfo/RelatedInfo1_D2XMuMu_PiPiPiPiLine

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/D2XMuMu_PiPiPiPiLine' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_D2XMuMu_PiPiPiPiLine/Particles |
