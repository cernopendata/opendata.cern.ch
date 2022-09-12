[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBc2Ds1Gamma_Line

## Properties:

|                |                                 |
|----------------|---------------------------------|
| OutputLocation | Phys/Bc2Ds1Gamma_Line/Particles |
| Postscale      | 1.0000000                       |
| HLT            | None                            |
| Prescale       | 1.0000000                       |
| L0DU           | None                            |
| ODIN           | None                            |

## Filter sequence:

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdLooseD02KPi_Particles**

|      |                                                                                  |
|------|----------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseD02KPi](./stripping21r1-stdloosed02kpi) /Particles')\>0 |

**FilterDesktop/D0ForBc2Ds1Gamma**

|                 |                                                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MAXTREE(ABSID=='K+',PROBNNk) \> 0.1) & (MAXTREE(ABSID=='pi+',PROBNNpi) \> 0.1) & CHILDCUT( (TRGHOSTPROB\<0.5) , 1 ) & CHILDCUT( (TRGHOSTPROB\<0.5) , 2 ) |
| Inputs          | [ 'Phys/ [StdLooseD02KPi](./stripping21r1-stdloosed02kpi) ' ]                                                                                           |
| DecayDescriptor | None                                                                                                                                                      |
| Output          | Phys/D0ForBc2Ds1Gamma/Particles                                                                                                                           |

**LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles**

|      |                                                                                      |
|------|--------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseANNKaons](./stripping21r1-stdlooseannkaons) /Particles')\>0 |

**CombineParticles/Ds1ForBc2Ds1Gamma**

|                  |                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D0ForBc2Ds1Gamma' , 'Phys/ [StdLooseANNKaons](./stripping21r1-stdlooseannkaons) ' ]                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D\~0' : 'ALL' , 'K+' : '(TRGHOSTPROB\<0.5) & (PROBNNk \> 0.1)' , 'K-' : '(TRGHOSTPROB\<0.5) & (PROBNNk \> 0.1)' } |
| CombinationCut   | ((AM-AM1) \< 1.25\*650\*MeV)                                                                                                                     |
| MotherCut        | ((M-M1) \< 650\*MeV) & (VFASPF(VCHI2/VDOF) \< 10)                                                                                                |
| DecayDescriptor  | [D_s1(2536)+ -\> D0 K+]cc                                                                                                                      |
| DecayDescriptors | [ '[D_s1(2536)+ -\> D0 K+]cc' ]                                                                                                              |
| Output           | Phys/Ds1ForBc2Ds1Gamma/Particles                                                                                                                 |

**LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles**

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseAllPhotons](./stripping21r1-stdlooseallphotons) /Particles')\>0 |

**FilterDesktop/GammaForBc2Ds1Gamma**

|                 |                                                                         |
|-----------------|-------------------------------------------------------------------------|
| Code            | (PT\> 1500.0\*MeV)                                                      |
| Inputs          | [ 'Phys/ [StdLooseAllPhotons](./stripping21r1-stdlooseallphotons) ' ] |
| DecayDescriptor | None                                                                    |
| Output          | Phys/GammaForBc2Ds1Gamma/Particles                                      |

**CombineParticles/Bc2Ds1Gamma_Line**

|                  |                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Ds1ForBc2Ds1Gamma' , 'Phys/GammaForBc2Ds1Gamma' ]                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'D_s1(2536)+' : 'ALL' , 'D_s1(2536)-' : 'ALL' , 'gamma' : 'ALL' }                                            |
| CombinationCut   | (AM \< 7500.0\*MeV+500\*MeV) & (AM \> 4800.0\*MeV-500\*MeV)                                                                 |
| MotherCut        | (M \< 7500.0\*MeV) & (M \> 4800.0\*MeV) & (BPVIPCHI2() \< 16.0) & ((BPVLTIME()\*c_light)\>75\*micrometer) & (PT\>1000\*MeV) |
| DecayDescriptor  | [B_c+ -\> D_s1(2536)+ gamma]cc                                                                                            |
| DecayDescriptors | [ '[B_c+ -\> D_s1(2536)+ gamma]cc' ]                                                                                    |
| Output           | Phys/Bc2Ds1Gamma_Line/Particles                                                                                             |
