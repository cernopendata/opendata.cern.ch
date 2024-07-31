[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingXB2DPiPBd2DstarPiPLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/XB2DPiPBd2DstarPiPLine/Particles |
| Postscale      | 1.0000000                             |
| HLT1           | None                                  |
| HLT2           | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

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

LoKi::VoidFilter/SelFilterPhys_StdLooseDstarWithD02KPi_Particles

|      |                                                                                                                         |
|------|-------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseDstarWithD02KPi](./stripping21r0p1-commonparticles-stdloosedstarwithd02kpi)/Particles',True)\>0 |

FilterDesktop/DstarForXB2DPiPXB2DPiP

|                 |                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------|
| Code            | ((MAXTREE(TRGHOSTPROB, ISBASIC) \< 0.5))                                                          |
| Inputs          | [ 'Phys/[StdLooseDstarWithD02KPi](./stripping21r0p1-commonparticles-stdloosedstarwithd02kpi)' ] |
| DecayDescriptor | None                                                                                              |
| Output          | Phys/DstarForXB2DPiPXB2DPiP/Particles                                                             |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

FilterDesktop/PionsForXB2DPiPXB2DPiP

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 9 ) & (TRCHI2DOF \< 5 ) & (TRGHOSTPROB \< 0.5)         |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/PionsForXB2DPiPXB2DPiP/Particles                                         |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                         |
|------|---------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21r0p1-commonparticles-stdlooseprotons)/Particles',True)\>0 |

FilterDesktop/ProtonsForXB2DPiPXB2DPiP

|                 |                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY) \> 9 ) & (TRCHI2DOF \< 5 ) & (PIDp\> 5) & ((PIDp-PIDK)\> -3)& (P\>10.0\*GeV) & (TRGHOSTPROB \< 0.5) |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r0p1-commonparticles-stdlooseprotons)' ]                                       |
| DecayDescriptor | None                                                                                                                    |
| Output          | Phys/ProtonsForXB2DPiPXB2DPiP/Particles                                                                                 |

CombineParticles/XB2DPiPBd2DstarPiPLine

|                  |                                                                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DstarForXB2DPiPXB2DPiP' , 'Phys/PionsForXB2DPiPXB2DPiP' , 'Phys/ProtonsForXB2DPiPXB2DPiP' ]                                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'D\*(2010)+' : 'ALL' , 'D\*(2010)-' : 'ALL' , 'p+' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' , 'p~-' : 'ALL' }                                                                                                                  |
| CombinationCut   | in_range(4200,AM,7250) & ( ACHI2DOCA(2,3)\<20 )                                                                                                                                                                                              |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10.) & (BPVDIRA\> 0.9999) & (BPVIPCHI2()\<25) & (BPVVDCHI2\>250) & (BPVVDRHO\>0.1\*mm) & (BPVVDZ\>2.0\*mm) & (MINTREE(((ABSID=='D+') \| (ABSID=='D0') \| (ABSID=='Lambda_c+')) , VFASPF(VZ))-VFASPF(VZ) \> 0.0 \*mm ) |
| DecayDescriptor  | None                                                                                                                                                                                                                                         |
| DecayDescriptors | [ '[B+ -\> D\*(2010)- pi+ p+]cc' , '[B- -\> D\*(2010)- pi+ p~-]cc' ]                                                                                                                                                                   |
| Output           | Phys/XB2DPiPBd2DstarPiPLine/Particles                                                                                                                                                                                                        |

AddRelatedInfo/RelatedInfo1_XB2DPiPBd2DstarPiPLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/XB2DPiPBd2DstarPiPLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_XB2DPiPBd2DstarPiPLine/Particles |

AddRelatedInfo/RelatedInfo2_XB2DPiPBd2DstarPiPLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/XB2DPiPBd2DstarPiPLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_XB2DPiPBd2DstarPiPLine/Particles |

AddRelatedInfo/RelatedInfo3_XB2DPiPBd2DstarPiPLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/XB2DPiPBd2DstarPiPLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_XB2DPiPBd2DstarPiPLine/Particles |

AddRelatedInfo/RelatedInfo4_XB2DPiPBd2DstarPiPLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/XB2DPiPBd2DstarPiPLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_XB2DPiPBd2DstarPiPLine/Particles |

AddRelatedInfo/RelatedInfo5_XB2DPiPBd2DstarPiPLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/XB2DPiPBd2DstarPiPLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo5_XB2DPiPBd2DstarPiPLine/Particles |
