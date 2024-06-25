[[stripping21 lines]](./stripping21-index)

# StrippingBu2Kpi0MergedLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/Bu2Kpi0MergedLine/Particles                |
| Postscale      | 1.0000000                                       |
| HLT            | HLT_PASS_RE('Hlt1Track(AllL0\|Photon)Decision') |
| Prescale       | 1.0000000                                       |
| L0DU           | None                                            |
| ODIN           | None                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingBu2Kpi0MergedLineVOIDFilter

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | (CONTAINS('Phys/[StdLooseMergedPi0](./stripping21-commonparticles-stdloosemergedpi0)/Particles')\>0) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21-commonparticles-stdnopidskaons)/Particles')\>0 |

FilterDesktop/FilteredKaons

|                 |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Code            | (~ISMUON) &(TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.5) & (PROBNNk \> 0.08) & ( ((PT - ptC1) / (ptC1 + PT)) \> -0.7) |
| Inputs          | [ 'Phys/[StdNoPIDsKaons](./stripping21-commonparticles-stdnopidskaons)' ]                                       |
| DecayDescriptor | None                                                                                                              |
| Output          | Phys/FilteredKaons/Particles                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLooseMergedPi0_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMergedPi0](./stripping21-commonparticles-stdloosemergedpi0)/Particles')\>0 |

CombineParticles/Bu2Kpi0MergedSel

|                  |                                                                                                                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/FilteredKaons' , 'Phys/[StdLooseMergedPi0](./stripping21-commonparticles-stdloosemergedpi0)' ]                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(MIPCHI2DV(PRIMARY)\>30) & (P\>8000) & (PT\>1100)' , 'K-' : '(MIPCHI2DV(PRIMARY)\>30) & (P\>8000) & (PT\>1100)' , 'pi0' : '(P\>0 \*MeV) & (PT\>2400 \*MeV) & (CL\>-1000)' } |
| CombinationCut   | (AM\>4200 \*MeV) & (AM\<6300 \*MeV)                                                                                                                                                                |
| MotherCut        | (MTDOCACHI2(1) \< 10) & (PT\>1800 \*MeV)                                                                                                                                                           |
| DecayDescriptor  | [B+ -\> K+ pi0]cc                                                                                                                                                                                |
| DecayDescriptors | [ '[B+ -\> K+ pi0]cc' ]                                                                                                                                                                        |
| Output           | Phys/Bu2Kpi0MergedSel/Particles                                                                                                                                                                    |

TisTosParticleTagger/Bu2Kpi0MergedLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2Kpi0MergedSel' ]                  |
| DecayDescriptor | None                                           |
| Output          | Phys/Bu2Kpi0MergedLine/Particles               |
| TisTosSpecs     | { 'Hlt1Track(AllL0\|Photon)Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_Bu2Kpi0MergedLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2Kpi0MergedLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo1_Bu2Kpi0MergedLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2Kpi0MergedLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2Kpi0MergedLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo2_Bu2Kpi0MergedLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2Kpi0MergedLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2Kpi0MergedLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo3_Bu2Kpi0MergedLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2Kpi0MergedLine

|                 |                                               |
|-----------------|-----------------------------------------------|
| Inputs          | [ 'Phys/Bu2Kpi0MergedLine' ]                |
| DecayDescriptor | None                                          |
| Output          | Phys/RelatedInfo4_Bu2Kpi0MergedLine/Particles |
