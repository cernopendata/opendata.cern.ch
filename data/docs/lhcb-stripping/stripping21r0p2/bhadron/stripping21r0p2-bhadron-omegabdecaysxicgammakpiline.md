[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingOmegabDecaysXicgammaKpiLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/OmegabDecaysXicgammaKpiLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 1.0000000                                  |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseANNKaons

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseANNKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseANNPions

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseANNPions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseANNProtons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseANNProtons/Particles',True) |

CombineParticles/XicForOmegabDecays

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseANNKaons](./stripping21r0p2-commonparticles-stdlooseannkaons)' , 'Phys/[StdLooseANNPions](./stripping21r0p2-commonparticles-stdlooseannpions)' , 'Phys/[StdLooseANNProtons](./stripping21r0p2-commonparticles-stdlooseannprotons)' ]                                                                                                                                                                                                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PROBNNk \> 0.1) & (MIPCHI2DV(PRIMARY)\>4) & (TRGHOSTPROB \< 0.5)' , 'K-' : '(PROBNNk \> 0.1) & (MIPCHI2DV(PRIMARY)\>4) & (TRGHOSTPROB \< 0.5)' , 'p+' : '(PROBNNp \> 0.1) & (MIPCHI2DV(PRIMARY)\>4) & (P\>10000) & (TRGHOSTPROB \< 0.5)' , 'pi+' : '(PROBNNpi \> 0.1) & (MIPCHI2DV(PRIMARY)\>4)& (TRGHOSTPROB \< 0.5)' , 'pi-' : '(PROBNNpi \> 0.1) & (MIPCHI2DV(PRIMARY)\>4)& (TRGHOSTPROB \< 0.5)' , 'p~-' : '(PROBNNp \> 0.1) & (MIPCHI2DV(PRIMARY)\>4) & (P\>10000) & (TRGHOSTPROB \< 0.5)' } |
| CombinationCut   | (ASUM(PT)\> 1800\*MeV) & (ADAMASS('Xi_c+') \< 1.25\*100\*MeV) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator'))                                                                                                                                                                                                                                                                                                                                                                                                            |
| MotherCut        | (ADMASS('Xi_c+') \< 100\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0.0)                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DecayDescriptor  | [Xi_c+ -\> p+ K- pi+]cc                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ '[Xi_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Output           | Phys/XicForOmegabDecays/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseAllPhotons/Particles',True) |

CombineParticles/OmegabDecaysXicgammaKpiLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseANNKaons](./stripping21r0p2-commonparticles-stdlooseannkaons)' , 'Phys/[StdLooseANNPions](./stripping21r0p2-commonparticles-stdlooseannpions)' , 'Phys/[StdLooseAllPhotons](./stripping21r0p2-commonparticles-stdlooseallphotons)' , 'Phys/XicForOmegabDecays' ]                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PROBNNk \> 0.1) & (MIPCHI2DV(PRIMARY)\>4) & (TRGHOSTPROB \< 0.5)' , 'K-' : '(PROBNNk \> 0.1) & (MIPCHI2DV(PRIMARY)\>4) & (TRGHOSTPROB \< 0.5)' , 'Xi_c+' : 'ALL' , 'Xi_c~-' : 'ALL' , 'gamma' : 'ALL' , 'pi+' : '(PROBNNpi \> 0.1) & (MIPCHI2DV(PRIMARY)\>4) & (TRGHOSTPROB \< 0.5)' , 'pi-' : '(PROBNNpi \> 0.1) & (MIPCHI2DV(PRIMARY)\>4) & (TRGHOSTPROB \< 0.5)' } |
| CombinationCut   | (AM \< 6700.0\*MeV+100\*MeV) & (AM \> 5500.0\*MeV-100\*MeV) & (AM12 - AM1 \< 250) & (APT\>3500.0\*MeV-300\*MeV)                                                                                                                                                                                                                                                                               |
| MotherCut        | (M \< 6700.0\*MeV) & (M \> 5500.0\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVIPCHI2() \< 25) & (BPVLTIME()\>0.2\*ps) & (PT\>3500.0\*MeV) & (BPVDIRA\>0.999)                                                                                                                                                                                                                                       |
| DecayDescriptor  | [Omega_b- -\> Xi_c+ gamma K- pi-]cc                                                                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[Omega_b- -\> Xi_c+ gamma K- pi-]cc' ]                                                                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/OmegabDecaysXicgammaKpiLine/Particles                                                                                                                                                                                                                                                                                                                                                    |
