[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingCharmWeakDecaysDs12D0stKWSLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/CharmWeakDecaysDs12D0stKWSLine/Particles |
| Postscale      | 1.0000000                                     |
| HLT1           | None                                          |
| HLT2           | None                                          |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNKaons

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseANNPions

|      |                                       |
|------|---------------------------------------|
| Code | 0StdAllLooseANNPions/Particles',True) |

CombineParticles/D0stForCharmWeakDecays

|                  |                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseANNKaons](./stripping21r1p2-commonparticles-stdalllooseannkaons)' , 'Phys/[StdAllLooseANNPions](./stripping21r1p2-commonparticles-stdalllooseannpions)' ]                                                                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(TRGHOSTPROB\<0.3) & (PT \> 800.0) & (MIPCHI2DV(PRIMARY) \< 9) & (PIDK \> 7.0)' , 'K-' : '(TRGHOSTPROB\<0.3) & (PT \> 800.0) & (MIPCHI2DV(PRIMARY) \< 9) & (PIDK \> 7.0)' , 'pi+' : '(TRGHOSTPROB\<0.3) & (PT \> 800.0) & (MIPCHI2DV(PRIMARY) \< 9) & (PIDK \< 0.0)' , 'pi-' : '(TRGHOSTPROB\<0.3) & (PT \> 800.0) & (MIPCHI2DV(PRIMARY) \< 9) & (PIDK \< 0.0)' } |
| CombinationCut   | (in_range( (1750\*MeV-100\*MeV), AM, (2120\*MeV+100\*MeV))) & (APT \> (2000\*MeV-500\*MeV)) & (AHASCHILD( PT \> 1500.0\* MeV))                                                                                                                                                                                                                                                           |
| MotherCut        | (in_range( 1750\*MeV, M, 2120\*MeV)) & (PT \> 2000\*MeV) & (VFASPF(VCHI2/VDOF) \< 16)                                                                                                                                                                                                                                                                                                    |
| DecayDescriptor  | [D\*(2007)0 -\> K- pi+]cc                                                                                                                                                                                                                                                                                                                                                              |
| DecayDescriptors | [ '[D\*(2007)0 -\> K- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                      |
| Output           | Phys/D0stForCharmWeakDecays/Particles                                                                                                                                                                                                                                                                                                                                                    |

CombineParticles/CharmWeakDecaysDs12D0stKWSLine

|                  |                                                                                                                                                                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/D0stForCharmWeakDecays' , 'Phys/[StdAllLooseANNKaons](./stripping21r1p2-commonparticles-stdalllooseannkaons)' ]                                                                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2007)0' : 'ALL' , 'D\*(2007)~0' : 'ALL' , 'K+' : '(TRGHOSTPROB\<0.3) & (PT \> 250) & (MIPCHI2DV(PRIMARY) \< 9) & (PIDK \> 7.0)' , 'K-' : '(TRGHOSTPROB\<0.3) & (PT \> 250) & (MIPCHI2DV(PRIMARY) \< 9) & (PIDK \> 7.0)' } |
| CombinationCut   | ((AM-AM1-AM2) \< (1.5\*80\*MeV)) & (APT \> (0.75\*4000\*MeV))                                                                                                                                                                                 |
| MotherCut        | ((M-M1-M2) \< 80\*MeV) & (VFASPF(VCHI2/VDOF) \< 9) & (PT \> 4000\*MeV)                                                                                                                                                                        |
| DecayDescriptor  | [D_s1(2536)+ -\> D\*(2007)~0 K+]cc                                                                                                                                                                                                          |
| DecayDescriptors | [ '[D_s1(2536)+ -\> D\*(2007)~0 K+]cc' ]                                                                                                                                                                                                  |
| Output           | Phys/CharmWeakDecaysDs12D0stKWSLine/Particles                                                                                                                                                                                                 |
