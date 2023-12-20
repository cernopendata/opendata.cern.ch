[[stripping21r0p1 lines]](./stripping21r0p1-index)

# StrippingBc2hhh_pipipi_exclLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/Bc2hhh_pipipi_exclLine/Particles |
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

LoKi::VoidFilter/StrippingBc2hhh_pipipi_exclLineVOIDFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 200 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                             |
|------|-------------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)/Particles',True)\>0 |

CombineParticles/Bc2hhh_pipipi_exclLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p1-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT \> 300.0\*MeV) & (P \> 2500.0\*MeV) & (MIPCHI2DV(PRIMARY) \> 1.0) & (TRCHI2DOF \< 4.0) & (TRGHOSTPROB \< 0.5)' , 'pi-' : '(PT \> 300.0\*MeV) & (P \> 2500.0\*MeV) & (MIPCHI2DV(PRIMARY) \> 1.0) & (TRCHI2DOF \< 4.0) & (TRGHOSTPROB \< 0.5)' }                                                                                                                                                                                                                                                  |
| CombinationCut   | (((AM \< 6502.0\*MeV) & (AM \> 5998.0\*MeV)) \| ((AM \< 5502.0\*MeV) & (AM \> 5098.0\*MeV))) & (AMAXDOCA('LoKi::TrgDistanceCalculator') \< 0.2)                                                                                                                                                                                                                                                                                                                                                                             |
| MotherCut        | (MAXTREE(((ABSID=='pi+') \| (ABSID=='pi-')),PT) \> 1500\*MeV) & (BPVDIRA \> 0.9999) & (BPVVDCHI2 \> 150.0) & (VFASPF(VMINVDDV(PRIMARY)) \> 1.5) & (VFASPF(VCHI2) \< 40.0) & (MIPCHI2DV(PRIMARY) \< 10.0) & (PT \> 1000.0\*MeV) & (SUMTREE(PT,(('pi+'==ABSID) \| ('pi-'==ABSID)),0.0) \> 4500.0\*MeV) & (SUMTREE(P,(('pi+'==ABSID) \| ('pi-'==ABSID)),0.0) \> 22000.0\*MeV) & (SUMTREE(MIPCHI2DV(PRIMARY),(('pi+'==ABSID) \| ('pi-'==ABSID)),0.0) \> 200.0) & (MINTREE((('pi+'==ABSID) \| ('pi-'==ABSID)),TRCHI2DOF) \< 3.0) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ '[B_c+ -\> pi+ pi- pi+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Output           | Phys/Bc2hhh_pipipi_exclLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

AddRelatedInfo/RelatedInfo1_Bc2hhh_pipipi_exclLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bc2hhh_pipipi_exclLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo1_Bc2hhh_pipipi_exclLine/Particles |

AddRelatedInfo/RelatedInfo2_Bc2hhh_pipipi_exclLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bc2hhh_pipipi_exclLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo2_Bc2hhh_pipipi_exclLine/Particles |

AddRelatedInfo/RelatedInfo3_Bc2hhh_pipipi_exclLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bc2hhh_pipipi_exclLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo3_Bc2hhh_pipipi_exclLine/Particles |

AddRelatedInfo/RelatedInfo4_Bc2hhh_pipipi_exclLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bc2hhh_pipipi_exclLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo4_Bc2hhh_pipipi_exclLine/Particles |

AddRelatedInfo/RelatedInfo5_Bc2hhh_pipipi_exclLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bc2hhh_pipipi_exclLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo5_Bc2hhh_pipipi_exclLine/Particles |

AddRelatedInfo/RelatedInfo6_Bc2hhh_pipipi_exclLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bc2hhh_pipipi_exclLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo6_Bc2hhh_pipipi_exclLine/Particles |

AddRelatedInfo/RelatedInfo7_Bc2hhh_pipipi_exclLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bc2hhh_pipipi_exclLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo7_Bc2hhh_pipipi_exclLine/Particles |

AddRelatedInfo/RelatedInfo8_Bc2hhh_pipipi_exclLine

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Inputs          | [ 'Phys/Bc2hhh_pipipi_exclLine' ]                |
| DecayDescriptor | None                                               |
| Output          | Phys/RelatedInfo8_Bc2hhh_pipipi_exclLine/Particles |
