[[stripping21 lines]](./stripping21-index)

# StrippingBs2PhiKstNominalLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/Bs2PhiKstNominalLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePhi2KK_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePhi2KK](./stripping21-commonparticles-stdloosephi2kk)/Particles')\>0 |

FilterDesktop/Phi2KKForBs2PhiKst

|                 |                                                                                                                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MINTREE('K+'==ABSID,PIDK)\> 0.0)& (MINTREE(ABSID=='K+',PT)\> 500.0 \*MeV)& (MINTREE(ABSID=='K+',MIPCHI2DV(PRIMARY))\> 9.0)& (ADMASS('phi(1020)') \< 25.0 \*MeV)& (PT \> 900.0 \*MeV)& (VFASPF(VCHI2/VDOF) \< 9.0) |
| Inputs          | [ 'Phys/[StdLoosePhi2KK](./stripping21-commonparticles-stdloosephi2kk)' ]                                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                                               |
| Output          | Phys/Phi2KKForBs2PhiKst/Particles                                                                                                                                                                                  |

LoKi::VoidFilter/SelFilterPhys_StdVeryLooseDetachedKst2Kpi_Particles

|      |                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdVeryLooseDetachedKst2Kpi](./stripping21-commonparticles-stdveryloosedetachedkst2kpi)/Particles')\>0 |

FilterDesktop/Kst2KpiForBs2PhiKst

|                 |                                                                                                                                                                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (INTREE((ABSID=='K+') & (PT \> 500.0 \*MeV) & (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK \> 0.0) ))& (INTREE((ABSID=='pi-') & (PT \> 500.0 \*MeV) & (MIPCHI2DV(PRIMARY)\> 9.0) & (PIDK \< 10.0) ))& (ADMASS('K\*(892)0') \< 150.0 \*MeV)& (BPVDIRA \> 0) & (VFASPF(VCHI2/VDOF)\< 9.0) & (PT \> 900.0 \*MeV) |
| Inputs          | [ 'Phys/[StdVeryLooseDetachedKst2Kpi](./stripping21-commonparticles-stdveryloosedetachedkst2kpi)' ]                                                                                                                                                                                               |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                |
| Output          | Phys/Kst2KpiForBs2PhiKst/Particles                                                                                                                                                                                                                                                                  |

CombineParticles/Bs2PhiKstNominalLine

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kst2KpiForBs2PhiKst' , 'Phys/Phi2KKForBs2PhiKst' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'phi(1020)' : 'ALL' } |
| CombinationCut   | (ADAMASS('B_s0') \< 500.0 \*MeV) & (AMAXDOCA('')\< 0.3 \*mm)                      |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 15.0) & (BPVDIRA \> 0.99)                                  |
| DecayDescriptor  | [B_s0 -\> phi(1020) K\*(892)~0]cc                                               |
| DecayDescriptors | [ '[B_s0 -\> phi(1020) K\*(892)~0]cc' ]                                       |
| Output           | Phys/Bs2PhiKstNominalLine/Particles                                               |
