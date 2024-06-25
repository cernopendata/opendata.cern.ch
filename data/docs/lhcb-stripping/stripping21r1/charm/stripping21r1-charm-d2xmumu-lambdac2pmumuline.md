[[stripping21r1 lines]](./stripping21r1-index)

# StrippingD2XMuMu_Lambdac2PMuMuLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/D2XMuMu_Lambdac2PMuMuLine/Particles |
| Postscale      | 1.0000000                                |
| HLT            | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)/Particles')\>0 |

FilterDesktop/ProtonsForD2XMuMu

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 5) & (P \> 2000.0 \*MeV) & (PT \> 300.0 \*MeV) & (MIPCHI2DV(PRIMARY) \> 6) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r1-commonparticles-stdlooseprotons)' ]          |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/ProtonsForD2XMuMu/Particles                                                         |

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

CombineParticles/D2XMuMu_Lambdac2PMuMuLine

|                  |                                                                                      |
|------------------|--------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuonsForD2XMuMu' , 'Phys/ProtonsForD2XMuMu' ]                              |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }        |
| CombinationCut   | (ADAMASS('Lambda_c+') \< 100.0 \*MeV) & (AMAXDOCA('')\<0.15) & (AM23 \> 250.0 \*MeV) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 5) & (BPVIPCHI2()\< 25) & (BPVDIRA \> 0.9999)                 |
| DecayDescriptor  | [Lambda_c+ -\> p+ mu+ mu-]cc                                                       |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ mu+ mu-]cc' ]                                               |
| Output           | Phys/D2XMuMu_Lambdac2PMuMuLine/Particles                                             |

AddRelatedInfo/RelatedInfo1_D2XMuMu_Lambdac2PMuMuLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/D2XMuMu_Lambdac2PMuMuLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo1_D2XMuMu_Lambdac2PMuMuLine/Particles |
