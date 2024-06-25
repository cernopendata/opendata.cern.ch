[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingXB2DPiPBd2DPiLine

## Properties:

|                |                                  |
|----------------|----------------------------------|
| OutputLocation | Phys/XB2DPiPBd2DPiLine/Particles |
| Postscale      | 1.0000000                        |
| HLT1           | None                             |
| HLT2           | None                             |
| Prescale       | 1.0000000                        |
| L0DU           | None                             |
| ODIN           | None                             |

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

GaudiSequencer/SeqXB2DPiPSelDpDs

LoKi::VoidFilter/SelFilterPhys_StdLooseDplus2KPiPi_Particles

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDplus2KPiPi](./stripping21r1p1-commonparticles-stdloosedplus2kpipi)/Particles',True)\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseDplusKKPi_Particles

|      |                                                      |
|------|------------------------------------------------------|
| Code | CONTAINS('Phys/StdLooseDplusKKPi/Particles',True)\>0 |

FilterDesktop/XB2DPiPSelDpDs

|                 |                                                                                                                      |
|-----------------|----------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                  |
| Inputs          | [ 'Phys/[StdLooseDplus2KPiPi](./stripping21r1p1-commonparticles-stdloosedplus2kpipi)' , 'Phys/StdLooseDplusKKPi' ] |
| DecayDescriptor | None                                                                                                                 |
| Output          | Phys/XB2DPiPSelDpDs/Particles                                                                                        |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/DpDsForXB2DPiPXB2DPiP

|                 |                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MIPDV(PRIMARY) \> 0.05\*mm) & ((CHILD(MIPCHI2DV(), 1) + CHILD(MIPCHI2DV(), 2) + CHILD(MIPCHI2DV(), 3) ) \> 100.) & ((MAXTREE(TRGHOSTPROB, ISBASIC) \< 0.5)) |
| Inputs          | [ 'Phys/XB2DPiPSelDpDs' ]                                                                                                                                  |
| DecayDescriptor | None                                                                                                                                                         |
| Output          | Phys/DpDsForXB2DPiPXB2DPiP/Particles                                                                                                                         |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForXB2DPiPXB2DPiP

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 9 ) & (TRCHI2DOF \< 5 ) & (TRGHOSTPROB \< 0.5)         |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/PionsForXB2DPiPXB2DPiP/Particles                                         |

CombineParticles/XB2DPiPBd2DPiLine

|                  |                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DpDsForXB2DPiPXB2DPiP' , 'Phys/PionsForXB2DPiPXB2DPiP' ]                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'D+' : 'ALL' , 'D-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                 |
| CombinationCut   | in_range(4200,AM,6750)                                                                                                                                                                                                                       |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10.) & (BPVDIRA\> 0.9999) & (BPVIPCHI2()\<25) & (BPVVDCHI2\>250) & (BPVVDRHO\>0.1\*mm) & (BPVVDZ\>2.0\*mm) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0.0 \*mm ) |
| DecayDescriptor  | [B0 -\> D- pi+]cc                                                                                                                                                                                                                          |
| DecayDescriptors | [ '[B0 -\> D- pi+]cc' ]                                                                                                                                                                                                                  |
| Output           | Phys/XB2DPiPBd2DPiLine/Particles                                                                                                                                                                                                             |

AddRelatedInfo/RelatedInfo1_XB2DPiPBd2DPiLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XB2DPiPBd2DPiLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo1_XB2DPiPBd2DPiLine/Particles |

AddRelatedInfo/RelatedInfo2_XB2DPiPBd2DPiLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XB2DPiPBd2DPiLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo2_XB2DPiPBd2DPiLine/Particles |

AddRelatedInfo/RelatedInfo3_XB2DPiPBd2DPiLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XB2DPiPBd2DPiLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo3_XB2DPiPBd2DPiLine/Particles |

AddRelatedInfo/RelatedInfo4_XB2DPiPBd2DPiLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XB2DPiPBd2DPiLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo4_XB2DPiPBd2DPiLine/Particles |

AddRelatedInfo/RelatedInfo5_XB2DPiPBd2DPiLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/XB2DPiPBd2DPiLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo5_XB2DPiPBd2DPiLine/Particles |
