[[stripping21 lines]](./stripping21-index)

# StrippingBetaSBs2Q2Body4piLine

## Properties:

|                |                                                                                            |
|----------------|--------------------------------------------------------------------------------------------|
| OutputLocation | Phys/BetaSBs2Q2Body4piLine/Particles                                                       |
| Postscale      | 1.0000000                                                                                  |
| HLT            | ( HLT_PASS_RE('Hlt1TrackAllL0Decision') & HLT_PASS_RE('Hlt2Topo[234]BodyBBDTDecision') ) |
| Prescale       | 1.0000000                                                                                  |
| L0DU           | None                                                                                       |
| ODIN           | None                                                                                       |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdNoPIDsPions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)/Particles')\>0 |

FilterDesktop/TrackListBetaSBs2Q2Body4pi

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.4) & (PT\>600.\*MeV) & (TRCHI2DOF \< 4) & (MIPCHI2DV(PRIMARY) \> 4.5) |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)' ]             |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/TrackListBetaSBs2Q2Body4pi/Particles                                               |

CombineParticles/DiTracksForCharmlessBBetaSBs2Q2Body4pi

|                  |                                                                       |
|------------------|-----------------------------------------------------------------------|
| Inputs           | [ 'Phys/TrackListBetaSBs2Q2Body4pi' ]                               |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                        |
| CombinationCut   | (APT\> 1200.0 \*MeV) & (AP\> 3.0 \*GeV) & in_range( 0.0 ,AM, 1100.0 ) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.0)                                           |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                                                 |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                         |
| Output           | Phys/DiTracksForCharmlessBBetaSBs2Q2Body4pi/Particles                 |

CombineParticles/BetaSBs2Q2Body4piLine

|                  |                                                                                 |
|------------------|---------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DiTracksForCharmlessBBetaSBs2Q2Body4pi' ]                             |
| DaughtersCuts    | { '' : 'ALL' , 'rho(770)0' : 'ALL' }                                            |
| CombinationCut   | in_range( 4500.0 ,AM, 5700.0 )                                                  |
| MotherCut        | (BPVDIRA \> 0.9999) & (MIPCHI2DV(PRIMARY) \< 20) & (VFASPF(VCHI2/VDOF) \< 9.0 ) |
| DecayDescriptor  | B0 -\> rho(770)0 rho(770)0                                                      |
| DecayDescriptors | [ 'B0 -\> rho(770)0 rho(770)0' ]                                              |
| Output           | Phys/BetaSBs2Q2Body4piLine/Particles                                            |

AddRelatedInfo/RelatedInfo1_BetaSBs2Q2Body4piLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/TrackListBetaSBs2Q2Body4pi' ]           |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_BetaSBs2Q2Body4piLine/Particles |

AddRelatedInfo/RelatedInfo2_BetaSBs2Q2Body4piLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/TrackListBetaSBs2Q2Body4pi' ]           |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo2_BetaSBs2Q2Body4piLine/Particles |

AddRelatedInfo/RelatedInfo3_BetaSBs2Q2Body4piLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/TrackListBetaSBs2Q2Body4pi' ]           |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo3_BetaSBs2Q2Body4piLine/Particles |

AddRelatedInfo/RelatedInfo4_BetaSBs2Q2Body4piLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/TrackListBetaSBs2Q2Body4pi' ]           |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo4_BetaSBs2Q2Body4piLine/Particles |

AddRelatedInfo/RelatedInfo5_BetaSBs2Q2Body4piLine

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/BetaSBs2Q2Body4piLine' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo5_BetaSBs2Q2Body4piLine/Particles |
