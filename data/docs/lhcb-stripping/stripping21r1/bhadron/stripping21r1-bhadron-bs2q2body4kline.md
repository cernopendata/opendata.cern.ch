[[stripping21r1 lines]](./stripping21r1-index)

# StrippingBs2Q2Body4KLine

## Properties:

|                |                                                                                            |
|----------------|--------------------------------------------------------------------------------------------|
| OutputLocation | Phys/Bs2Q2Body4KLine/Particles                                                             |
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

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/TrackListBs2Q2Body4K

|                 |                                                                                           |
|-----------------|-------------------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.4) & (PT\>500.\*MeV) & (TRCHI2DOF \< 4.0) & (MIPCHI2DV(PRIMARY) \> 4.0) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ]               |
| DecayDescriptor | None                                                                                      |
| Output          | Phys/TrackListBs2Q2Body4K/Particles                                                       |

CombineParticles/DiTracksBs2Q2Body4K

|                  |                                                                        |
|------------------|------------------------------------------------------------------------|
| Inputs           | [ 'Phys/TrackListBs2Q2Body4K' ]                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                           |
| CombinationCut   | (APT\> 900.0 \*MeV) & (AP\> 1.0 \*GeV) & in_range( 990.0 ,AM, 2500.0 ) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.0)                                            |
| DecayDescriptor  | phi(1020) -\> K+ K-                                                    |
| DecayDescriptors | [ 'phi(1020) -\> K+ K-' ]                                            |
| Output           | Phys/DiTracksBs2Q2Body4K/Particles                                     |

CombineParticles/Bs2Q2Body4KLine

|                  |                                                                                 |
|------------------|---------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DiTracksBs2Q2Body4K' ]                                                |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : 'ALL' }                                            |
| CombinationCut   | in_range( 5200.0 ,AM, 5500.0 )                                                  |
| MotherCut        | (BPVDIRA \> 0.9995) & (MIPCHI2DV(PRIMARY) \< 20) & (VFASPF(VCHI2/VDOF) \< 9.0 ) |
| DecayDescriptor  | B_s0 -\> phi(1020) phi(1020)                                                    |
| DecayDescriptors | [ 'B_s0 -\> phi(1020) phi(1020)' ]                                            |
| Output           | Phys/Bs2Q2Body4KLine/Particles                                                  |

AddRelatedInfo/RelatedInfo1_Bs2Q2Body4KLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/TrackListBs2Q2Body4K' ]           |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo1_Bs2Q2Body4KLine/Particles |

AddRelatedInfo/RelatedInfo2_Bs2Q2Body4KLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/TrackListBs2Q2Body4K' ]           |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo2_Bs2Q2Body4KLine/Particles |

AddRelatedInfo/RelatedInfo3_Bs2Q2Body4KLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/TrackListBs2Q2Body4K' ]           |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo3_Bs2Q2Body4KLine/Particles |

AddRelatedInfo/RelatedInfo4_Bs2Q2Body4KLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/TrackListBs2Q2Body4K' ]           |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo4_Bs2Q2Body4KLine/Particles |

AddRelatedInfo/RelatedInfo5_Bs2Q2Body4KLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Inputs          | [ 'Phys/Bs2Q2Body4KLine' ]                |
| DecayDescriptor | None                                        |
| Output          | Phys/RelatedInfo5_Bs2Q2Body4KLine/Particles |
