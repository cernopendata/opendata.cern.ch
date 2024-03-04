[[stripping21 lines]](./stripping21-index)

# StrippingRareStrangeSigmaPMuMuLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/RareStrangeSigmaPMuMuLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdAllLooseMuons_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)/Particles')\>0 |

CombineParticles/RareStrangeSigmaPMuMuLine

|                  |                                                                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseMuons](./stripping21-commonparticles-stdallloosemuons)' , 'Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)' ]                                                                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'mu-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (MIPCHI2DV(PRIMARY)\>9.0)' , 'p+' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PIDp \> 5.0)' , 'p~-' : '(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3) & (PIDp \> 5.0)' } |
| CombinationCut   | (ADAMASS('Sigma+')\<500.0 \*MeV) & (AMAXDOCA('')\< 2.0 \*mm)                                                                                                                                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 36.0) & (PT\> 500.0 \*MeV)& (ADMASS('Sigma+') \< 500.0 \*MeV )& (BPVDIRA \> 0.9) & (BPVIPCHI2()\< 36.0)& (BPVLTIME()\> 6.0 \* ps)                                                                                                                                               |
| DecayDescriptor  | [Sigma+ -\> p+ mu+ mu-]cc                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ '[Sigma+ -\> p+ mu+ mu-]cc' ]                                                                                                                                                                                                                                                                   |
| Output           | Phys/RareStrangeSigmaPMuMuLine/Particles                                                                                                                                                                                                                                                              |

AddRelatedInfo/RelatedInfo1_RareStrangeSigmaPMuMuLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo1_RareStrangeSigmaPMuMuLine/Particles |

AddRelatedInfo/RelatedInfo2_RareStrangeSigmaPMuMuLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo2_RareStrangeSigmaPMuMuLine/Particles |

AddRelatedInfo/RelatedInfo3_RareStrangeSigmaPMuMuLine

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Inputs          | [ 'Phys/RareStrangeSigmaPMuMuLine' ]                |
| DecayDescriptor | None                                                  |
| Output          | Phys/RelatedInfo3_RareStrangeSigmaPMuMuLine/Particles |
