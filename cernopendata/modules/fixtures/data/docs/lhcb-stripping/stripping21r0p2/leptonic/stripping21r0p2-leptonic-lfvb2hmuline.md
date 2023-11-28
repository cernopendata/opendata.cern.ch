[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLFVB2hMuLine

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/LFVB2hMuLine/Particles |
| Postscale      | 1.0000000                   |
| HLT1           | None                        |
| HLT2           | None                        |
| Prescale       | 1.0000000                   |
| L0DU           | None                        |
| ODIN           | None                        |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionLeptonic

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & ~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsKaons

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsProtons

|      |                                    |
|------|------------------------------------|
| Code | 0StdNoPIDsProtons/Particles',True) |

CombineParticles/LFVB2hMuLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMuons](./stripping21r0p2-commonparticles-stdloosemuons)' , 'Phys/[StdNoPIDsKaons](./stripping21r0p2-commonparticles-stdnopidskaons)' , 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' , 'Phys/[StdNoPIDsProtons](./stripping21r0p2-commonparticles-stdnopidsprotons)' ]                                                                                                                                                                                                                                                                                                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (PIDK\>5) & (TRGHOSTPROB\<0.3)' , 'K-' : '(MIPCHI2DV(PRIMARY)\>25.)&(TRCHI2DOF\<3) & (PIDK\>5) & (TRGHOSTPROB\<0.3)' , 'mu+' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 ) & (TRGHOSTPROB\<0.3)' , 'p+' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 )& (PIDp\>5) & (TRGHOSTPROB\<0.3)' , 'pi+' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3)&(TRGHOSTPROB\<0.3)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3)&(TRGHOSTPROB\<0.3)' , 'p~-' : '(MIPCHI2DV(PRIMARY)\> 25.)&(TRCHI2DOF \< 3 )& (PIDp\>5) & (TRGHOSTPROB\<0.3)' } |
| CombinationCut   | (ADAMASS('B_s0')\<300\*MeV)& (AMAXDOCA('')\<0.1\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (ADMASS('B_s0') \< 600\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 225)& (BPVIPCHI2()\< 25)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DecayDescriptors | [ '[B_s0 -\> p+ mu-]cc' , '[B_s0 -\> p+ mu+]cc' , '[B_s0 -\> pi+ mu-]cc' , '[B_s0 -\> pi+ mu+]cc' , '[B_s0 -\> K+ mu-]cc' , '[B_s0 -\> K+ mu+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Output           | Phys/LFVB2hMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
