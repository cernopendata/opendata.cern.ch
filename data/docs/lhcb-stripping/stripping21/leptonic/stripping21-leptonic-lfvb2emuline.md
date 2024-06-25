[[stripping21 lines]](./stripping21-index)

# StrippingLFVB2eMuLine

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/LFVB2eMuLine/Particles |
| Postscale      | 1.0000000                   |
| HLT            | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseElectrons](./stripping21-commonparticles-stdlooseelectrons)/Particles')\>0 |

CombineParticles/LFVB2eMuLine

|                  |                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseElectrons](./stripping21-commonparticles-stdlooseelectrons)' , 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ]                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 )' , 'e-' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 )' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3)' } |
| CombinationCut   | (ADAMASS('B_s0')\<1200\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 1200\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 225)& (BPVIPCHI2()\< 25)                                                                                                                                                                           |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[B_s0 -\> e+ mu-]cc' , '[B_s0 -\> e+ mu+]cc' ]                                                                                                                                                                                                                                    |
| Output           | Phys/LFVB2eMuLine/Particles                                                                                                                                                                                                                                                                |

AddRelatedInfo/RelatedInfo1_LFVB2eMuLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/LFVB2eMuLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo1_LFVB2eMuLine/Particles |
