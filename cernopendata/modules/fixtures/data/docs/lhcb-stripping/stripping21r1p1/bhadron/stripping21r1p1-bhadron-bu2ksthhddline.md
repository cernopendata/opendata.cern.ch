[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingBu2KsthhDDLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/Bu2KsthhDDLine/Particles                 |
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

LoKi::VoidFilter/StrippingBu2KsthhDDLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)/Particles',True)\>0 |

FilterDesktop/KSforBu2KsthhDD

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0')\<30.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>50.0)&(CHILDCUT((TRCHI2DOF\<4.0),1))&(CHILDCUT((TRCHI2DOF\<4.0),2))&(CHILDCUT((TRGHOSTPROB\<0.5),1))&(CHILDCUT((TRGHOSTPROB\<0.5),2)) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p1-commonparticles-stdlooseksdd)' ]                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/KSforBu2KsthhDD/Particles                                                                                                                                                                     |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)/Particles',True)\>0 |

CombineParticles/KstforBu2KsthhDD

|                  |                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KSforBu2KsthhDD' , 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                         |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<4.0)&(TRGHOSTPROB\<0.4)' , 'pi-' : '(TRCHI2DOF\<4.0)&(TRGHOSTPROB\<0.4)' } |
| CombinationCut   | (AM \> 0.0\*MeV)&(AM \< 5000.0\*MeV)                                                                                           |
| MotherCut        | ALL                                                                                                                            |
| DecayDescriptor  | [K\*(892)+ -\> KS0 pi+]cc                                                                                                    |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                            |
| Output           | Phys/KstforBu2KsthhDD/Particles                                                                                                |

CombineParticles/Bu2KsthhDDLine

|                  |                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KstforBu2KsthhDD' , 'Phys/[StdLoosePions](./stripping21r1p1-commonparticles-stdloosepions)' ]                                                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'pi+' : '(TRCHI2DOF\<4.0)&(TRGHOSTPROB\<0.4)' , 'pi-' : '(TRCHI2DOF\<4.0)&(TRGHOSTPROB\<0.4)' }                                                         |
| CombinationCut   | (APT\>1000.0\*MeV)&((APT1+APT2+APT3)\>3000.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(AM\>(5279-1279.0)\*MeV)&(AM\<(5279+921.0)\*MeV)&(AVAL_MAX(MIPDV(PRIMARY),PT)\>0.05)&(ACUTDOCACHI2(5.0,''))                          |
| MotherCut        | (PT\>1500.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVDIRA\>0.999)&(MIPCHI2DV(PRIMARY)\<8.0)&(VFASPF(VMINVDDV(PRIMARY))\>1.0)&(BPVVDCHI2\>50.0)&(SUMTREE(MIPCHI2DV(PRIMARY),((ABSID=='pi+') \| (ABSID=='pi-')),0.0) \> 50.0) |
| DecayDescriptor  | None                                                                                                                                                                                                               |
| DecayDescriptors | [ '[B+ -\> pi+ pi- K\*(892)+]cc' ]                                                                                                                                                                             |
| Output           | Phys/Bu2KsthhDDLine/Particles                                                                                                                                                                                      |

AddRelatedInfo/RelatedInfo1_Bu2KsthhDDLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2KsthhDDLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo1_Bu2KsthhDDLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2KsthhDDLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2KsthhDDLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo2_Bu2KsthhDDLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2KsthhDDLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2KsthhDDLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo3_Bu2KsthhDDLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2KsthhDDLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2KsthhDDLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo4_Bu2KsthhDDLine/Particles |
