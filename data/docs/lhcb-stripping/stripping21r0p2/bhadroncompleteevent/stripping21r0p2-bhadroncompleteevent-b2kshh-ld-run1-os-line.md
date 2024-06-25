[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2KShh_LD_Run1_OS_Line

## Properties:

|                |                                                                   |
|----------------|-------------------------------------------------------------------|
| OutputLocation | Phys/B2KShh_LD_Run1_OS_Line/Particles                             |
| Postscale      | 1.0000000                                                         |
| HLT1           | HLT_PASS_RE('Hlt1TrackAllL0Decision')                             |
| HLT2           | HLT_PASS_RE('Hlt2Topo[234]Body.\*Decision\|Hlt2IncPhiDecision') |
| Prescale       | 1.0000000                                                         |
| L0DU           | None                                                              |
| ODIN           | None                                                              |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

LoKi::VoidFilter/StrippingB2KShh_LD_Run1_OS_LineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseKsLD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsLD/Particles',True) |

FilterDesktop/KSforB2KShhLD

|                 |                                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(P\>6000.0\*MeV)&(ADMASS('KS0')\<25.0\*MeV)&(VFASPF(VCHI2)\<12.0)&(BPVVDCHI2\>50.0) |
| Inputs          | [ 'Phys/[StdLooseKsLD](./stripping21r0p2-commonparticles-stdlooseksld)' ]                                                                       |
| DecayDescriptor | None                                                                                                                                              |
| Output          | Phys/KSforB2KShhLD/Particles                                                                                                                      |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

DaVinci::N3BodyDecays/B2KShh_LD_Run1_OS_Line

|                  |                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KSforB2KShhLD' , 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.4)' , 'pi-' : '(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.4)' }                                                                  |
| CombinationCut   | ((APT1+APT2+APT3)\>4500.0\*MeV)&(AM\>(5279-1279.0)\*MeV)&(AM\<(5279+921.0)\*MeV)&(APT\>1000.0\*MeV)&(ANUM(PT\>800.0\*MeV)\>=2)&(ACHI2DOCA(1,3)\<25.0)&(ACHI2DOCA(2,3)\<25.0)                    |
| MotherCut        | (PT\>1500.0\*MeV)&(VFASPF(VCHI2)\<12.0)&((CHILD(VFASPF(VZ),3) - VFASPF(VZ))\>15.0\*mm)&(BPVDIRA\>0.9999)&(BPVIPCHI2()\<7.0)&(BPVVDCHI2\>50.0)&(SUMTREE(BPVIPCHI2(),(ABSID=='pi+'),0.0) \> 50.0) |
| DecayDescriptor  | None                                                                                                                                                                                            |
| DecayDescriptors | [ 'B0 -\> pi+ pi- KS0' ]                                                                                                                                                                      |
| Output           | Phys/B2KShh_LD_Run1_OS_Line/Particles                                                                                                                                                           |

AddRelatedInfo/RelatedInfo1_B2KShh_LD_Run1_OS_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_LD_Run1_OS_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_B2KShh_LD_Run1_OS_Line/Particles |

AddRelatedInfo/RelatedInfo2_B2KShh_LD_Run1_OS_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_LD_Run1_OS_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_B2KShh_LD_Run1_OS_Line/Particles |

AddRelatedInfo/RelatedInfo3_B2KShh_LD_Run1_OS_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_LD_Run1_OS_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_B2KShh_LD_Run1_OS_Line/Particles |

AddRelatedInfo/RelatedInfo4_B2KShh_LD_Run1_OS_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_LD_Run1_OS_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_B2KShh_LD_Run1_OS_Line/Particles |

AddRelatedInfo/RelatedInfo5_B2KShh_LD_Run1_OS_Line

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/B2KShh_LD_Run1_OS_Line' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo5_B2KShh_LD_Run1_OS_Line/Particles |
