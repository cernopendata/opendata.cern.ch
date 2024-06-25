[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2XMuMu_PiSSLine

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/D2XMuMu_PiSSLine/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuonsForD2XMuMu

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 3000.0 \*MeV) & (PT \> 500.0\* MeV) & (MIPCHI2DV(PRIMARY) \> 6) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ]              |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/MuonsForD2XMuMu/Particles                                                           |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/PionsForD2XMuMu

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 2000.0 \*MeV) & (PT \> 300.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 6) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ]              |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/PionsForD2XMuMu/Particles                                                           |

CombineParticles/D2XMuMu_PiSSLine

|                  |                                                                                                     |
|------------------|-----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuonsForD2XMuMu' , 'Phys/PionsForD2XMuMu' ]                                               |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                      |
| CombinationCut   | (ADAMASS('D-') \< 200.0 \*MeV) & (AMAXDOCA('')\<0.15) & (AM \> 1763.0 \*MeV) &(AM23 \> 250.0 \*MeV) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5) & (BPVIPCHI2()\< 25) & (BPVDIRA \> 0.9999)                                |
| DecayDescriptor  | [D- -\> pi+ mu- mu-]cc                                                                            |
| DecayDescriptors | [ '[D- -\> pi+ mu- mu-]cc' ]                                                                    |
| Output           | Phys/D2XMuMu_PiSSLine/Particles                                                                     |

AddRelatedInfo/RelatedInfo1_D2XMuMu_PiSSLine

|                 |                                              |
|-----------------|----------------------------------------------|
| Inputs          | [ 'Phys/D2XMuMu_PiSSLine' ]                |
| DecayDescriptor | None                                         |
| Output          | Phys/RelatedInfo1_D2XMuMu_PiSSLine/Particles |
