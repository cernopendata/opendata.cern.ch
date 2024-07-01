[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBu2Kpi0ResolvedLine

## Properties:

|                |                                                 |
|----------------|-------------------------------------------------|
| OutputLocation | Phys/Bu2Kpi0ResolvedLine/Particles              |
| Postscale      | 1.0000000                                       |
| HLT            | HLT_PASS_RE('Hlt1Track(AllL0\|Photon)Decision') |
| Prescale       | 1.0000000                                       |
| L0DU           | None                                            |
| ODIN           | None                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingBu2Kpi0ResolvedLineVOIDFilter

|      |                                                                                                            |
|------|------------------------------------------------------------------------------------------------------------|
| Code | (CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsKaons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsKaons](./stripping21r1-commonparticles-stdnopidskaons)/Particles')\>0 |

FilterDesktop/FilteredKaons

|                 |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Code            | (~ISMUON) &(TRCHI2DOF \< 3.0) & (TRGHOSTPROB \< 0.5) & (PROBNNk \> 0.08) & ( ((PT - ptC1) / (ptC1 + PT)) \> -0.7) |
| Inputs          | [ 'Phys/[StdNoPIDsKaons](./stripping21r1-commonparticles-stdnopidskaons)' ]                                     |
| DecayDescriptor | None                                                                                                              |
| Output          | Phys/FilteredKaons/Particles                                                                                      |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

CombineParticles/Bu2Kpi0ResolvedSel

|                  |                                                                                                                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/FilteredKaons' , 'Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)' ]                                                                                                |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(MIPCHI2DV(PRIMARY)\>25) & (PT\>1300)' , 'K-' : '(MIPCHI2DV(PRIMARY)\>25) & (PT\>1300)' , 'pi0' : '(P\>8000 \*MeV) & (PT\>1400 \*MeV) & (CHILD(CL,1)\>-1000) & (CHILD(CL,2)\>-1000)' } |
| CombinationCut   | (AM\>4800 \*MeV) & (AM\<5800 \*MeV)                                                                                                                                                                           |
| MotherCut        | (MTDOCACHI2(1) \< 7) & (PT\>0 \*MeV)                                                                                                                                                                          |
| DecayDescriptor  | [B+ -\> K+ pi0]cc                                                                                                                                                                                           |
| DecayDescriptors | [ '[B+ -\> K+ pi0]cc' ]                                                                                                                                                                                   |
| Output           | Phys/Bu2Kpi0ResolvedSel/Particles                                                                                                                                                                             |

TisTosParticleTagger/Bu2Kpi0ResolvedLine

|                 |                                                |
|-----------------|------------------------------------------------|
| Inputs          | [ 'Phys/Bu2Kpi0ResolvedSel' ]                |
| DecayDescriptor | None                                           |
| Output          | Phys/Bu2Kpi0ResolvedLine/Particles             |
| TisTosSpecs     | { 'Hlt1Track(AllL0\|Photon)Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_Bu2Kpi0ResolvedLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2Kpi0ResolvedLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo1_Bu2Kpi0ResolvedLine/Particles |

AddRelatedInfo/RelatedInfo2_Bu2Kpi0ResolvedLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2Kpi0ResolvedLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo2_Bu2Kpi0ResolvedLine/Particles |

AddRelatedInfo/RelatedInfo3_Bu2Kpi0ResolvedLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2Kpi0ResolvedLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo3_Bu2Kpi0ResolvedLine/Particles |

AddRelatedInfo/RelatedInfo4_Bu2Kpi0ResolvedLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Inputs          | [ 'Phys/Bu2Kpi0ResolvedLine' ]                |
| DecayDescriptor | None                                            |
| Output          | Phys/RelatedInfo4_Bu2Kpi0ResolvedLine/Particles |
