[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingB2KsthhLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/B2KsthhLine/Particles                    |
| Postscale      | 1.0000000                                     |
| HLT1           | HLT_PASS_RE('Hlt1TrackAllL0Decision')         |
| HLT2           | HLT_PASS_RE('Hlt2Topo[234]Body.\*Decision') |
| Prescale       | 1.0000000                                     |
| L0DU           | None                                          |
| ODIN           | None                                          |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadron

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronBadEvent') & ~ALG_PASSED('StrippingStreamBhadronBadEvent') |

LoKi::VoidFilter/StrippingB2KsthhLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdVeryLooseDetachedKst2Kpi_Particles

|      |                                                                                                                                 |
|------|---------------------------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdVeryLooseDetachedKst2Kpi](./stripping21r0p1-commonparticles-stdveryloosedetachedkst2kpi)/Particles',True)\>0 |

FilterDesktop/KstforB2Ksthh

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(CHILDCUT((TRGHOSTPROB\<0.3),1))&(CHILDCUT((TRGHOSTPROB\<0.3),2)) |
| Inputs          | [ 'Phys/[StdVeryLooseDetachedKst2Kpi](./stripping21r0p1-commonparticles-stdveryloosedetachedkst2kpi)' ]                       |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/KstforB2Ksthh/Particles                                                                                                    |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

CombineParticles/B2KsthhLine

|                  |                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KstforB2Ksthh' , 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ]                                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.3)' , 'pi-' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.3)' }                                                         |
| CombinationCut   | (APT\>1000.0\*MeV)&((APT1+APT2+APT3)\>3200.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(AM\>(5279-1279.0)\*MeV)&(AM\<(5279+921.0)\*MeV)&(AVAL_MAX(MIPDV(PRIMARY),PT)\>0.05)                                                  |
| MotherCut        | (PT\>1500.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVDIRA\>0.9995)&(MIPCHI2DV(PRIMARY)\<8.0)&(VFASPF(VMINVDDV(PRIMARY))\>1.0)&(BPVVDCHI2\>50.0)&(SUMTREE(MIPCHI2DV(PRIMARY),((ABSID=='pi+') \| (ABSID=='pi-')),0.0) \> 50.0) |
| DecayDescriptor  | None                                                                                                                                                                                                                |
| DecayDescriptors | [ '[B0 -\> pi+ pi- K\*(892)0]cc' ]                                                                                                                                                                              |
| Output           | Phys/B2KsthhLine/Particles                                                                                                                                                                                          |

AddRelatedInfo/RelatedInfo1_B2KsthhLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/B2KsthhLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo1_B2KsthhLine/Particles |

AddRelatedInfo/RelatedInfo2_B2KsthhLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/B2KsthhLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo2_B2KsthhLine/Particles |

AddRelatedInfo/RelatedInfo3_B2KsthhLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/B2KsthhLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo3_B2KsthhLine/Particles |

AddRelatedInfo/RelatedInfo4_B2KsthhLine

|                 |                                         |
|-----------------|-----------------------------------------|
| Inputs          | [ 'Phys/B2KsthhLine' ]                |
| DecayDescriptor | None                                    |
| Output          | Phys/RelatedInfo4_B2KsthhLine/Particles |
