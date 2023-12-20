[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2hhh_KKK_samesignLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2hhh_KKK_samesignLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/B2hhhGlobalEventCutFilter

|      |                                                                |
|------|----------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 200 ) |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsKaons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)/Particles')\>0 |

CombineParticles/B2hhh_KKK_samesignLine

|                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsKaons](./stripping21r1-commonparticles-stdallnopidskaons)' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(PT \> 100.0\*MeV) & (P \> 1500.0\*MeV) & (MIPCHI2DV(PRIMARY) \> 1.0) & (TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.5)' , 'K-' : '(PT \> 100.0\*MeV) & (P \> 1500.0\*MeV) & (MIPCHI2DV(PRIMARY) \> 1.0) & (TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.5)' }                                                                                                                                                                                                                                                                                                    |
| CombinationCut   | (AM \< 6300.0\*MeV) & (AM \> 5050.0\*MeV) & (AMAXDOCA('LoKi::TrgDistanceCalculator') \< 0.2)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| MotherCut        | (MAXTREE(((ABSID=='K+') \| (ABSID=='K-')),PT) \> 1500\*MeV) & (BPVDIRA \> 0.99998) & (BPVVDCHI2 \> 500.0) & (VFASPF(VMINVDDV(PRIMARY)) \> 3.0) & (VFASPF(VCHI2) \< 12.0) & (MIPCHI2DV(PRIMARY) \< 10.0) & (PT \> 1000.0\*MeV) & (SUMTREE(PT,((ABSID=='K+') \| (ABSID=='K-')),0.0) \> 4500.0\*MeV) & (SUMTREE(P,((ABSID=='K+') \| (ABSID=='K-')),0.0) \> 20000.0\*MeV) & (SUMTREE(MIPCHI2DV(PRIMARY),((ABSID=='K+') \| (ABSID=='K-')),0.0) \> 500.0) & (MINTREE((('K+'==ABSID) \| ('K-'==ABSID)),TRCHI2DOF) \< 3.0) & (BPVCORRM \< 7000.0 \* MeV)& (BPVCORRM \> 4000.0\*MeV) |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| DecayDescriptors | [ '[B+ -\> K+ K+ K+]cc' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Output           | Phys/B2hhh_KKK_samesignLine/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
