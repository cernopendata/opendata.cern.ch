[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingBs2PhiKstNominalLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/Bs2PhiKstNominalLine/Particles |
| Postscale      | 1.0000000                           |
| HLT1           | None                                |
| HLT2           | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)/Particles',True)\>0 |

CombineParticles/Phi2KKForBs2PhiKst

|                  |                                                                                                                                                        |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)' ]                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT\>500.0\*MeV)&(MIPCHI2DV(PRIMARY)\>9.0)&(PIDK \> 0.0)' , 'K-' : '(PT\>500.0\*MeV)&(MIPCHI2DV(PRIMARY)\>9.0)&(PIDK \> 0.0)' } |
| CombinationCut   | (ADAMASS('phi(1020)') \< 25.0 \*MeV)                                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 9.0) & (PT \> 900.0 \*MeV)                                                                                                       |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                                                                                                    |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                                                                                                            |
| Output           | Phys/Phi2KKForBs2PhiKst/Particles                                                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

CombineParticles/Kst2KpiForBs2PhiKst

|                  |                                                                                                                                                                                                                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseKaons](./stripping21r0p1-commonparticles-stdloosekaons)' , 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ]                                                                                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 500.0 \*MeV) & (PIDK \> 0.0) & (MIPCHI2DV(PRIMARY)\> 9.0)' , 'K-' : '(PT \> 500.0 \*MeV) & (PIDK \> 0.0) & (MIPCHI2DV(PRIMARY)\> 9.0)' , 'pi+' : '(PT \> 500.0 \*MeV) & (PIDK \< 10.0) & (MIPCHI2DV(PRIMARY)\> 9.0)' , 'pi-' : '(PT \> 500.0 \*MeV) & (PIDK \< 10.0) & (MIPCHI2DV(PRIMARY)\> 9.0)' } |
| CombinationCut   | (ADAMASS('K\*(892)0') \< 150.0 \*MeV)                                                                                                                                                                                                                                                                                              |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 9.0) & (PT \> 900.0 \*MeV)                                                                                                                                                                                                                                                                                   |
| DecayDescriptor  | [K\*(892)0 -\> K+ pi-]cc                                                                                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[K\*(892)0 -\> K+ pi-]cc' ]                                                                                                                                                                                                                                                                                                 |
| Output           | Phys/Kst2KpiForBs2PhiKst/Particles                                                                                                                                                                                                                                                                                                 |

CombineParticles/Bs2PhiKstNominalLine

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kst2KpiForBs2PhiKst' , 'Phys/Phi2KKForBs2PhiKst' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | (ADAMASS('B_s0') \< 500.0 \*MeV) & (AMAXDOCA('',False)\< 0.3 \*mm)                |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 15.0) & (BPVDIRA \> 0.99)                                  |
| DecayDescriptor  | [B_s0 -\> phi(1020) K\*(892)~0]cc                                               |
| DecayDescriptors | [ '[B_s0 -\> phi(1020) K\*(892)~0]cc' ]                                       |
| Output           | Phys/Bs2PhiKstNominalLine/Particles                                               |
