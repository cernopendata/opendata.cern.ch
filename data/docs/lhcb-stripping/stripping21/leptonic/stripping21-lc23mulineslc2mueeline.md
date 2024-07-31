[[stripping21 lines]](./stripping21-index)

# StrippingLc23MuLinesLc2mueeLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/Lc23MuLinesLc2mueeLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

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

**LoKi::VoidFilter/SelFilterPhys_StdLooseElectrons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseElectrons](./stripping21-stdlooseelectrons) /Particles')\>0 |

**DaVinci::N3BodyDecays/Lc23MuLinesLc2mueeLine**

|                  |                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ [StdLooseElectrons](./stripping21-stdlooseelectrons) ' , 'Phys/ [StdLooseMuons](./stripping21-stdloosemuons) ' ]                                                                                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDe-PIDpi)\>2)' , 'e-' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3) & ((PIDe-PIDpi)\>2)' , 'mu+' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' , 'mu-' : '(PT \> 300\*MeV) & (BPVIPCHI2()\>9.0) & (TRCHI2DOF\<3.0) & (TRGHP\<0.3)' } |
| CombinationCut   | (ADAMASS('Lambda_c+')\<200\*MeV) & (ADOCA(1,3)\<0.3\*mm) & (ADOCA(2,3)\<0.3\*mm)                                                                                                                                                                                                                                                                                                                     |
| MotherCut        | ( VFASPF(VCHI2) \< 15 ) & ( (BPVLTIME()\*c_light) \> 70\*micrometer ) & ( BPVIPCHI2() \< 100 )                                                                                                                                                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Lambda_c+ -\> mu+ e+ e-]cc' , '[Lambda_c+ -\> mu- e+ e+]cc' , '[Lambda_c+ -\> mu+ e+ e+]cc' ]                                                                                                                                                                                                                                                                                            |
| Output           | Phys/Lc23MuLinesLc2mueeLine/Particles                                                                                                                                                                                                                                                                                                                                                                |
