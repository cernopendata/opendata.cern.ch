[[stripping21 lines]](./stripping21-index)

# StrippingLb2PhipKLine

## Properties:

|                |                             |
|----------------|-----------------------------|
| OutputLocation | Phys/Lb2PhipKLine/Particles |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

CombineParticles/Lb2PhipK_LoosePhi2KK

|                  |                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ]                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>4.0)' , 'K-' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>4.0)' } |
| CombinationCut   | (AM\<(1090+30)\*MeV)&(ADOCACHI2CUT(40, ''))                                                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<15)&(ADMASS('phi(1020)')\<25\*MeV)                                                                                                              |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                                                                                                                  |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                                                          |
| Output           | Phys/Lb2PhipK_LoosePhi2KK/Particles                                                                                                                                  |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)/Particles')\>0 |

CombineParticles/Lb2PhipK_LoosepK

|                  |                                                                                                                                                                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' , 'Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)' ]                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>4.0)' , 'K-' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>4.0)' , 'p+' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>4.0)' , 'p~-' : '(TRGHOSTPROB \< 0.5) & (PT\>400\*MeV)&(MIPCHI2DV(PRIMARY)\>4.0)' } |
| CombinationCut   | (AM\<(4600)\*MeV)&(ADOCACHI2CUT(40, ''))                                                                                                                                                                                                                                                                                    |
| MotherCut        | (VFASPF(VCHI2/VDOF)\<15)                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | [Lambda(1520)0 -\> p+ K-]cc                                                                                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Lambda(1520)0 -\> p+ K-]cc' ]                                                                                                                                                                                                                                                                                       |
| Output           | Phys/Lb2PhipK_LoosepK/Particles                                                                                                                                                                                                                                                                                             |

CombineParticles/Lb2PhipKLine

|                  |                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lb2PhipK_LoosePhi2KK' , 'Phys/Lb2PhipK_LoosepK' ]                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda(1520)0' : '(PT\>0\*MeV)' , 'Lambda(1520)~0' : '(PT\>0\*MeV)' , 'phi(1020)' : '(PT\>0\*MeV)' } |
| CombinationCut   | (ADAMASS('Lambda_b0')\<((300+30)\*MeV))&(ACHILD(PT,1)\*ACHILD(PT,2)\>2.0\*GeV\*GeV)                                  |
| MotherCut        | (BPVDIRA \> 0.999) & (VFASPF(VCHI2/VDOF)\<15)&(ADMASS('Lambda_b0')\<300\*MeV)                                        |
| DecayDescriptor  | [Lambda_b0 -\> Lambda(1520)0 phi(1020)]cc                                                                          |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda(1520)0 phi(1020)]cc' ]                                                                  |
| Output           | Phys/Lb2PhipKLine/Particles                                                                                          |
