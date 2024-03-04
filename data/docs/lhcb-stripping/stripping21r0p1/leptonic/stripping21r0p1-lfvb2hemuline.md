[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingLFVB2heMuLine

## Properties:

|                |                              |
|----------------|------------------------------|
| OutputLocation | Phys/LFVB2heMuLine/Particles |
| Postscale      | 1.0000000                    |
| HLT1           | None                         |
| HLT2           | None                         |
| Prescale       | 1.0000000                    |
| L0DU           | None                         |
| ODIN           | None                         |

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

**LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21r0p1-stdloosemuons) /Particles',True)\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles**

|      |                                                                                               |
|------|-----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseElectrons](./stripping21r0p1-stdlooseelectrons) /Particles',True)\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles**

|      |                                                                                         |
|------|-----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsPions](./stripping21r0p1-stdnopidspions) /Particles',True)\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles**

|      |                                                                                         |
|------|-----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsKaons](./stripping21r0p1-stdnopidskaons) /Particles',True)\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsProtons_Particles**

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsProtons](./stripping21r0p1-stdnopidsprotons) /Particles',True)\>0 |

**CombineParticles/LFVB2heMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r0p1-stdlooseelectrons) ' , 'Phys/ [StdLooseMuons](./stripping21r0p1-stdloosemuons) ' , 'Phys/ [StdNoPIDsKaons](./stripping21r0p1-stdnopidskaons) ' , 'Phys/ [StdNoPIDsPions](./stripping21r0p1-stdnopidspions) ' , 'Phys/ [StdNoPIDsProtons](./stripping21r0p1-stdnopidsprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3)&(PIDK\>5) & (TRGHOSTPROB\<0.3)' , 'K-' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3)&(PIDK\>5) & (TRGHOSTPROB\<0.3)' , 'e+' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (PIDe \> 2)' , 'e-' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (PIDe \> 2)' , 'mu+' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3)' , 'p+' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3)&(PIDp\>5) & (TRGHOSTPROB\<0.3)' , 'pi+' : '(MIPCHI2DV(PRIMARY)\>25.)&( TRCHI2DOF \< 3 )& (TRGHOSTPROB\<0.3)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>25.)&( TRCHI2DOF \< 3 )& (TRGHOSTPROB\<0.3)' , 'p\~-' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3)&(PIDp\>5) & (TRGHOSTPROB\<0.3)' } |
| CombinationCut   | (ADAMASS('B+')\<600\*MeV)& (AMAXDOCA('')\<0.3\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 600\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 225)& (BPVIPCHI2()\< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DecayDescriptors | [ '[B+ -\> K+ e+ mu-]cc' , '[B+ -\> K- e+ mu+]cc' , '[B+ -\> K+ e- mu+]cc' , '[B+ -\> pi+ e+ mu-]cc' , '[B+ -\> pi- e+ mu+]cc' , '[B+ -\> pi+ e- mu+]cc' , '[B+ -\> p+ e+ mu-]cc' , '[B- -\> p+ e- mu-]cc' , '[B+ -\> p+ e- mu+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/LFVB2heMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
