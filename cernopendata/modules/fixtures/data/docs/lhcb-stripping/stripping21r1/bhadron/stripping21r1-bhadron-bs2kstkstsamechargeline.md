[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBs2KstKstSameChargeLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/Bs2KstKstSameChargeLine/Particles |
| Postscale      | 1.0000000                              |
| HLT            | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdVeryLooseDetachedKst2Kpi_Particles

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdVeryLooseDetachedKst2Kpi](./stripping21r1-commonparticles-stdveryloosedetachedkst2kpi)/Particles')\>0 |

FilterDesktop/Kst2KpiForBs2KstKst

|                 |                                                                                                                                                                                                                                                                                                                                  |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (INTREE((ABSID=='K+') & (PT \> 500.0 \*MeV) & (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK \> -5.0) & (TRGHOSTPROB\< 0.8) ))& (INTREE((ABSID=='pi-') & (PT \> 500.0 \*MeV) & (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK \< 10.0 ) & (TRGHOSTPROB\< 0.8) ))& (ADMASS('K\*(892)0') \< 150.0 \*MeV)& (VFASPF(VCHI2/VDOF)\< 9.0) & (PT \> 900.0 \*MeV) |
| Inputs          | [ 'Phys/[StdVeryLooseDetachedKst2Kpi](./stripping21r1-commonparticles-stdveryloosedetachedkst2kpi)' ]                                                                                                                                                                                                                          |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                             |
| Output          | Phys/Kst2KpiForBs2KstKst/Particles                                                                                                                                                                                                                                                                                               |

CombineParticles/Bs2KstKstSameChargeLine

|                  |                                                                              |
|------------------|------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kst2KpiForBs2KstKst' ]                                             |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' }                  |
| CombinationCut   | (ADAMASS('B_s0') \< 500.0 \*MeV) & (AMAXDOCA('')\< 0.3 \*mm)                 |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 15.0) & (MIPCHI2DV(PRIMARY)\< 25) & (BPVDIRA \> 0.99) |
| DecayDescriptor  | [B_s0 -\> K\*(892)0 K\*(892)0]cc                                           |
| DecayDescriptors | [ '[B_s0 -\> K\*(892)0 K\*(892)0]cc' ]                                   |
| Output           | Phys/Bs2KstKstSameChargeLine/Particles                                       |
