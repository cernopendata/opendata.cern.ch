[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingLb2V0hhLDSSLine

## Properties:

|                |                                               |
|----------------|-----------------------------------------------|
| OutputLocation | Phys/Lb2V0hhLDSSLine/Particles                |
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

LoKi::VoidFilter/StrippingLb2V0hhLDSSLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseLambdaLD

|      |                                    |
|------|------------------------------------|
| Code | 0StdLooseLambdaLD/Particles',True) |

FilterDesktop/Lambda0LDLbLines

|                 |                                                                                          |
|-----------------|------------------------------------------------------------------------------------------|
| Code            | (P\>5000.0\*MeV)&(ADMASS('Lambda0')\<25.0\*MeV)&(VFASPF(VCHI2)\<15.0) &(BPVVDCHI2\>50.0) |
| Inputs          | [ 'Phys/[StdLooseLambdaLD](./stripping21r1p2-commonparticles-stdlooselambdald)' ]      |
| DecayDescriptor | None                                                                                     |
| Output          | Phys/Lambda0LDLbLines/Particles                                                          |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

CombineParticles/Lb2V0hhLDSSLine

|                  |                                                                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Lambda0LDLbLines' , 'Phys/[StdNoPIDsPions](./stripping21r1p2-commonparticles-stdnopidspions)' ]                                               |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.5)' , 'pi-' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.5)' } |
| CombinationCut   | (APT\>1000.0\*MeV)&((APT1+APT2+APT3)\>4200.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(AM\>(5619-1319.0)\*MeV)&(AM\<(5619+600.0)\*MeV)&(ACUTDOCACHI2(5.0,''))   |
| MotherCut        | (PT\>800.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVDIRA\>0.995)&(MIPCHI2DV(PRIMARY)\<15.0)&(BPVVDCHI2\>30.0)                                                    |
| DecayDescriptor  | None                                                                                                                                                    |
| DecayDescriptors | [ 'Lambda_b0 -\> pi+ pi+ Lambda0' , 'Lambda_b~0 -\> pi+ pi+ Lambda~0' , 'Lambda_b0 -\> pi- pi- Lambda0' , 'Lambda_b~0 -\> pi- pi- Lambda~0' ]         |
| Output           | Phys/Lb2V0hhLDSSLine/Particles                                                                                                                          |

AddRelatedInfo/RelatedInfo1_Lb2V0hhLDSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hhLDSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo1_Lb2V0hhLDSSLine/Particles |

AddRelatedInfo/RelatedInfo2_Lb2V0hhLDSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hhLDSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo2_Lb2V0hhLDSSLine/Particles |

AddRelatedInfo/RelatedInfo3_Lb2V0hhLDSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hhLDSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo3_Lb2V0hhLDSSLine/Particles |

AddRelatedInfo/RelatedInfo4_Lb2V0hhLDSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hhLDSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo4_Lb2V0hhLDSSLine/Particles |

AddRelatedInfo/RelatedInfo5_Lb2V0hhLDSSLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Lb2V0hhLDSSLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo5_Lb2V0hhLDSSLine/Particles |
