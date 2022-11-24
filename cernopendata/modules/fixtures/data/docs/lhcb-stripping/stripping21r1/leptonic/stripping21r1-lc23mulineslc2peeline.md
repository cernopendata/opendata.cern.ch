[[stripping21r1 lines]](./stripping21r1-index)

# StrippingLc23MuLinesLc2peeLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/Lc23MuLinesLc2peeLine/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles**

|      |                                                                                    |
|------|------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseProtons](./stripping21r1-stdlooseprotons) /Particles')\>0 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles**

|      |                                                                                        |
|------|----------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseElectrons](./stripping21r1-stdlooseelectrons) /Particles')\>0 |

**DaVinci::N3BodyDecays/Lc23MuLinesLc2peeLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21r1-stdlooseelectrons) ' , 'Phys/ [StdLooseProtons](./stripping21r1-stdlooseprotons) ' ]                                                                                                                                                                                                                                                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDe-PIDpi)\>2)' , 'e-' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDe-PIDpi)\>2)' , 'p+' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' , 'p\~-' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDp-PIDpi)\>5) & ((PIDp-PIDK)\>0)' } |
| CombinationCut   | (ADAMASS('Lambda_c+')\<200\*MeV) & (ADOCA(1,3)\<0.3\*mm) & (ADOCA(2,3)\<0.3\*mm)                                                                                                                                                                                                                                                                                                                                                                                                   |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME()\*c_light) \> 70\*micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Lambda_c+ -\> p+ e+ e-]cc' , '[Lambda_c+ -\> p\~- e+ e+]cc' , '[Lambda_c+ -\> p+ e+ e+]cc' ]                                                                                                                                                                                                                                                                                                                                                                           |
| Output           | Phys/Lc23MuLinesLc2peeLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                               |
