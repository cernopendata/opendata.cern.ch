[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingLFVB2hTauMuLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/LFVB2hTauMuLine/Particles |
| Postscale      | 1.0000000                      |
| HLT1           | None                           |
| HLT2           | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

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

**LoKi::VoidFilter/SELECT:Phys/StdLooseMuons**

|      |                                   |
|------|-----------------------------------|
| Code | 0 StdLooseMuons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdLooseDetachedTau3pi**

|      |                                            |
|------|--------------------------------------------|
| Code | 0 StdLooseDetachedTau3pi /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions**

|      |                                    |
|------|------------------------------------|
| Code | 0 StdNoPIDsPions /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsKaons**

|      |                                    |
|------|------------------------------------|
| Code | 0 StdNoPIDsKaons /Particles',True) |

**LoKi::VoidFilter/SELECT:Phys/StdNoPIDsProtons**

|      |                                      |
|------|--------------------------------------|
| Code | 0 StdNoPIDsProtons /Particles',True) |

**CombineParticles/LFVB2hTauMuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseDetachedTau3pi](./stripping21r0p2-stdloosedetachedtau3pi) ' , 'Phys/ [StdLooseMuons](./stripping21r0p2-stdloosemuons) ' , 'Phys/ [StdNoPIDsKaons](./stripping21r0p2-stdnopidskaons) ' , 'Phys/ [StdNoPIDsPions](./stripping21r0p2-stdnopidspions) ' , 'Phys/ [StdNoPIDsProtons](./stripping21r0p2-stdnopidsprotons) ' ]                                                                                                                                                                                                                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3)&(PIDK\>5)& (TRGHOSTPROB\<0.3)' , 'K-' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3)&(PIDK\>5)& (TRGHOSTPROB\<0.3)' , 'mu+' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3)& (TRGHOSTPROB\<0.3)' , 'mu-' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3)& (TRGHOSTPROB\<0.3)' , 'p+' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3)&(PIDp\>5)& (TRGHOSTPROB\<0.3)' , 'pi+' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3) & (TRGHOSTPROB\<0.3)' , 'p\~-' : '(MIPCHI2DV(PRIMARY)\>36.)&(TRCHI2DOF\<3)&(PIDp\>5)& (TRGHOSTPROB\<0.3)' , 'tau+' : 'ALL' , 'tau-' : 'ALL' } |
| CombinationCut   | (ADAMASS('B+')\<400\*MeV)& (AMAXDOCA('')\<0.15\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<9) & (BPVDIRA\>0.999)& (ADMASS('B_s0') \< 400\*MeV )& (BPVDIRA \> 0) & (BPVVDCHI2\> 225)& (BPVIPCHI2()\< 16)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[B+ -\> K+ tau+ mu-]cc' , '[B+ -\> K- tau+ mu+]cc' , '[B+ -\> K+ tau- mu+]cc' , '[B+ -\> pi+ tau+ mu-]cc' , '[B+ -\> pi- tau+ mu+]cc' , '[B+ -\> pi+ tau- mu+]cc' , '[B+ -\> p+ tau+ mu-]cc' , '[B- -\> p+ tau- mu-]cc' , '[B+ -\> p+ tau- mu+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/LFVB2hTauMuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
