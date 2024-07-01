[[stripping21 lines]](./stripping21-index)

# StrippingLFVB2hMuLine

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/LFVB2hMuLine/Particles |
| Postscale      | 1.0000000                   |
| HLT            | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21-stdloosemuons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsPions](./stripping21-stdnopidspions) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles**

|      |                                                                                |
|------|--------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsKaons](./stripping21-stdnopidskaons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdNoPIDsProtons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdNoPIDsProtons](./stripping21-stdnopidsprotons) /Particles')\>0 |

**CombineParticles/LFVB2hMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21-stdloosemuons) ' , 'Phys/ [StdNoPIDsKaons](./stripping21-stdnopidskaons) ' , 'Phys/ [StdNoPIDsPions](./stripping21-stdnopidspions) ' , 'Phys/ [StdNoPIDsProtons](./stripping21-stdnopidsprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (PIDK\>5) & (TRGHOSTPROB\<0.3)' , 'K-' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (PIDK\>5) & (TRGHOSTPROB\<0.3)' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3)' , 'p+' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 )& (PIDp\>5) & (TRGHOSTPROB\<0.3)' , 'pi+' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3)&(TRGHOSTPROB\<0.3)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3)&(TRGHOSTPROB\<0.3)' , 'p\~-' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 )& (PIDp\>5) & (TRGHOSTPROB\<0.3)' } |
| CombinationCut   | (ADAMASS('B_s0')\<300\*MeV)& (AMAXDOCA('')\<0.1\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 600\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 225)& (BPVIPCHI2()\< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| DecayDescriptors | [ '[B_s0 -\> p+ mu-]cc' , '[B_s0 -\> p+ mu+]cc' , '[B_s0 -\> pi+ mu-]cc' , '[B_s0 -\> pi+ mu+]cc' , '[B_s0 -\> K+ mu-]cc' , '[B_s0 -\> K+ mu+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/LFVB2hMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
