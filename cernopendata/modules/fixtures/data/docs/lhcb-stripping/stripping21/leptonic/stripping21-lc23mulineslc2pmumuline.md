[[stripping21 lines]](./stripping21-index)

# StrippingLc23MuLinesLc2pmumuLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/Lc23MuLinesLc2pmumuLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles**

|      |                                                                              |
|------|------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseMuons](./stripping21-stdloosemuons) /Particles')\>0 |

**DaVinci::N3BodyDecays/Lc23MuLinesLc2pmumuLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseMuons](./stripping21-stdloosemuons) ' , 'Phys/ [StdLooseProtons](./stripping21-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDmu-PIDpi)\>-5) & ((PIDmu-PIDK)\>-5)' , 'mu-' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDmu-PIDpi)\>-5) & ((PIDmu-PIDK)\>-5)' , 'p+' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' , 'p\~-' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' } |
| CombinationCut   | (ADAMASS('Lambda_c+')\<200\*MeV) & (ADOCA(1,3)\<0.3\*mm) & (ADOCA(2,3)\<0.3\*mm)                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME()\*c_light) \> 70\*micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ mu+ mu-]cc' , '[Lambda_c+ -\> p\~- mu+ mu+]cc' , '[Lambda_c+ -\> p+ mu+ mu+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Output           | Phys/Lc23MuLinesLc2pmumuLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
