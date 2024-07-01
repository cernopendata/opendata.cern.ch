[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingBu2KsthhLLLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/Bu2KsthhLLLine/Particles                 |
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

LoKi::VoidFilter/StrippingBu2KsthhLLLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)/Particles',True)\>0 |

FilterDesktop/KSforBu2KsthhLL

|                 |                                                                                                                                                                                                    |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0')\<20.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>80.0)&(CHILDCUT((TRCHI2DOF\<4.0),1))&(CHILDCUT((TRCHI2DOF\<4.0),2))&(CHILDCUT((TRGHOSTPROB\<0.4),1))&(CHILDCUT((TRGHOSTPROB\<0.4),2)) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21r0p1-commonparticles-stdlooseksll)' ]                                                                                                                        |
| DecayDescriptor | None                                                                                                                                                                                               |
| Output          | Phys/KSforBu2KsthhLL/Particles                                                                                                                                                                     |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                                     |
|------|-----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)/Particles',True)\>0 |

CombineParticles/KstforBu2KsthhLL

|                  |                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KSforBu2KsthhLL' , 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ]                         |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<4.0)&(TRGHOSTPROB\<0.4)' , 'pi-' : '(TRCHI2DOF\<4.0)&(TRGHOSTPROB\<0.4)' } |
| CombinationCut   | (AM \> 0.0\*MeV)&(AM \< 5000.0\*MeV)                                                                                           |
| MotherCut        | ALL                                                                                                                            |
| DecayDescriptor  | [K\*(892)+ -\> KS0 pi+]cc                                                                                                    |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                            |
| Output           | Phys/KstforBu2KsthhLL/Particles                                                                                                |

CombineParticles/Bu2KsthhLLLine

|                  |                                                                                                                                                                                           |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KstforBu2KsthhLL' , 'Phys/[StdLoosePions](./stripping21r0p1-commonparticles-stdloosepions)' ]                                                                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'pi+' : '(TRCHI2DOF\<4.0)&(TRGHOSTPROB\<0.4)' , 'pi-' : '(TRCHI2DOF\<4.0)&(TRGHOSTPROB\<0.4)' }                                |
| CombinationCut   | (APT\>1000.0\*MeV)&((APT1+APT2+APT3)\>3000.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(AM\>(5279-1279.0)\*MeV)&(AM\<(5279+921.0)\*MeV)&(AVAL_MAX(MIPDV(PRIMARY),PT)\>0.05)&(ACUTDOCACHI2(5.0,'')) |
| MotherCut        | (PT\>1500.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVDIRA\>0.9999)&(MIPCHI2DV(PRIMARY)\<8.0)&(VFASPF(VMINVDDV(PRIMARY))\>1.0)&(BPVVDCHI2\>50.0)                                                    |
| DecayDescriptor  | None                                                                                                                                                                                      |
| DecayDescriptors | [ '[B+ -\> pi+ pi- K\*(892)+]cc' ]                                                                                                                                                    |
| Output           | Phys/Bu2KsthhLLLine/Particles                                                                                                                                                             |

AddRelatedInfo/RelatedInfo1_Bu2KsthhLLLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2KsthhLLLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo1_Bu2KsthhLLLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2KsthhLLLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2KsthhLLLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo2_Bu2KsthhLLLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2KsthhLLLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2KsthhLLLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo3_Bu2KsthhLLLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2KsthhLLLine

|                 |                                            |
|-----------------|--------------------------------------------|
| Inputs          | [ 'Phys/Bu2KsthhLLLine' ]                |
| DecayDescriptor | None                                       |
| Output          | Phys/RelatedInfo4_Bu2KsthhLLLine/Particles |
