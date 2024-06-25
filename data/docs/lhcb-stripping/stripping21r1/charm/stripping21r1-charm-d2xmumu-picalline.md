[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2XMuMu_PiCalLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/D2XMuMu_PiCalLine/Particles |
| Postscale      | 1.0000000                        |
| HLT            | None                             |
| Prescale       | 0.010000000                      |
| L0DU           | None                             |
| ODIN           | None                             |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsAsMuonsForD2XMuMu

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 3000.0 \*MeV) & (PT \> 500.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 6) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]              |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/PionsAsMuonsForD2XMuMu/Particles                                                    |

CombineParticles/preD2XMuMu_PiCal

|                  |                                                |
|------------------|------------------------------------------------|
| Inputs           | [ 'Phys/PionsAsMuonsForD2XMuMu' ]            |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | ATRUE                                          |
| MotherCut        | ALL                                            |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                          |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                  |
| Output           | Phys/preD2XMuMu_PiCal/Particles                |

FilterDesktop/PionsForD2XMuMu

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 2000.0 \*MeV) & (PT \> 300.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 6) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]              |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/PionsForD2XMuMu/Particles                                                           |

CombineParticles/D2XMuMu_PiCalLine

|                  |                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PionsForD2XMuMu' , 'Phys/preD2XMuMu_PiCal' ]                                              |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'rho(770)0' : 'ALL' }                                |
| CombinationCut   | (ADAMASS('D+') \< 200.0 \*MeV) & (AMAXDOCA('')\<0.15) & (AM \> 1763.0 \*MeV) &(AM23 \> 250.0 \*MeV) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5) & (BPVIPCHI2()\< 25) & (BPVDIRA \> 0.9999)                                |
| DecayDescriptor  | [D+ -\> pi+ rho(770)0]cc                                                                          |
| DecayDescriptors | [ '[D+ -\> pi+ rho(770)0]cc' ]                                                                  |
| Output           | Phys/D2XMuMu_PiCalLine/Particles                                                                    |

AddRelatedInfo/RelatedInfo1_D2XMuMu_PiCalLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/D2XMuMu_PiCalLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo1_D2XMuMu_PiCalLine/Particles |
