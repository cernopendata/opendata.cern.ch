[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingOmegab2XicKpiWSLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/Omegab2XicKpiWSLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseANNKaons_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNKaons](./stripping21r0p1-commonparticles-stdlooseannkaons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNPions_Particles

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNPions](./stripping21r0p1-commonparticles-stdlooseannpions)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseANNProtons_Particles

|      |                                                                                                               |
|------|---------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseANNProtons](./stripping21r0p1-commonparticles-stdlooseannprotons)/Particles',True)\>0 |

CombineParticles/XicForOmegab2XicKpi

|                  |                                                                                                                                                                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseANNKaons](./stripping21r0p1-commonparticles-stdlooseannkaons)' , 'Phys/[StdLooseANNPions](./stripping21r0p1-commonparticles-stdlooseannpions)' , 'Phys/[StdLooseANNProtons](./stripping21r0p1-commonparticles-stdlooseannprotons)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PROBNNk \> 0.1)' , 'K-' : '(PROBNNk \> 0.1)' , 'p+' : '(PROBNNp \> 0.1)' , 'pi+' : '(PROBNNpi \> 0.1)' , 'pi-' : '(PROBNNpi \> 0.1)' , 'p~-' : '(PROBNNp \> 0.1)' }                                                             |
| CombinationCut   | (ASUM(PT)\> 1800\*MeV) & (ADAMASS('Xi_c+') \< 1.25\*100\*MeV) & (ACUTDOCA(0.5\*mm,'LoKi::DistanceCalculator'))                                                                                                                                          |
| MotherCut        | (ADMASS('Xi_c+') \< 100\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVVDCHI2\>36) & (BPVDIRA\>0.0)                                                                                                                                                             |
| DecayDescriptor  | [Xi_c+ -\> p+ K- pi+]cc                                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Xi_c+ -\> p+ K- pi+]cc' ]                                                                                                                                                                                                                       |
| Output           | Phys/XicForOmegab2XicKpi/Particles                                                                                                                                                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNKaons_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseANNPions_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)/Particles',True)\>0 |

CombineParticles/Omegab2XicKpiWSLine

|                  |                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21r0p1-commonparticles-stdalllooseannkaons)' , 'Phys/[StdAllLooseANNPions](./stripping21r0p1-commonparticles-stdalllooseannpions)' , 'Phys/XicForOmegab2XicKpi' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PROBNNk \> 0.1)' , 'K-' : '(PROBNNk \> 0.1)' , 'Xi_c+' : 'ALL' , 'Xi_c~-' : 'ALL' , 'pi+' : '(PROBNNpi \> 0.1)' , 'pi-' : '(PROBNNpi \> 0.1)' }                                      |
| CombinationCut   | (AM \< 6700.0\*MeV+500\*MeV) & (AM \> 5500.0\*MeV-500\*MeV)                                                                                                                                                  |
| MotherCut        | (M \< 6700.0\*MeV) & (M \> 5500.0\*MeV) & (VFASPF(VCHI2/VDOF)\<10) & (BPVIPCHI2() \< 25) & (BPVLTIME()\>0.2\*ps) & (PT\>3500.0\*MeV) & (BPVDIRA\>0.999)                                                      |
| DecayDescriptor  | [Omega_b- -\> Xi_c+ K- pi+]cc                                                                                                                                                                              |
| DecayDescriptors | [ '[Omega_b- -\> Xi_c+ K- pi+]cc' ]                                                                                                                                                                      |
| Output           | Phys/Omegab2XicKpiWSLine/Particles                                                                                                                                                                           |
