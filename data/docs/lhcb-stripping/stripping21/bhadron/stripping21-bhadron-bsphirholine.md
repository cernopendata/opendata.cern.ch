[[stripping21 lines]](./stripping21-index)

# StrippingBsPhiRhoLine

## Properties:

|                |                                                                                            |
|----------------|--------------------------------------------------------------------------------------------|
| OutputLocation | Phys/BsPhiRhoLine/Particles                                                                |
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

FilterDesktop/TrackListBsPhiRho

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (TRGHOSTPROB \< 0.45) & (PT\>600.\*MeV) & (TRCHI2DOF \< 3.5) & (MIPCHI2DV(PRIMARY) \> 4.5) |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21-commonparticles-stdnopidspions)' ]                |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/TrackListBsPhiRho/Particles                                                           |

CombineParticles/DiTracksForCharmlessBBsPhiRho

|                  |                                                                       |
|------------------|-----------------------------------------------------------------------|
| Inputs           | [ 'Phys/TrackListBsPhiRho' ]                                        |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                        |
| CombinationCut   | (APT\> 1200.0 \*MeV) & (AP\> 3.0 \*GeV) & in_range( 0.0 ,AM, 4000.0 ) |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 9.0 )                                          |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                                                 |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                         |
| Output           | Phys/DiTracksForCharmlessBBsPhiRho/Particles                          |

LoKi::VoidFilter/SelFilterPhys_StdTightPhi2KK_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdTightPhi2KK](./stripping21-commonparticles-stdtightphi2kk)/Particles')\>0 |

FilterDesktop/KKTracksForCharmlessBBsPhiRho

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (ADMASS('phi(1020)')\< 20.0 \*MeV) & (PT\> 1200.0 \*MeV) & (P\> 3.0 \*GeV)  |
| Inputs          | [ 'Phys/[StdTightPhi2KK](./stripping21-commonparticles-stdtightphi2kk)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/KKTracksForCharmlessBBsPhiRho/Particles                                |

CombineParticles/BsPhiRhoLine

|                  |                                                                                   |
|------------------|-----------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DiTracksForCharmlessBBsPhiRho' , 'Phys/KKTracksForCharmlessBBsPhiRho' ] |
| DaughtersCuts    | { '' : 'ALL' , 'phi(1020)' : 'ALL' , 'rho(770)0' : 'ALL' }                        |
| CombinationCut   | in_range( 4800.0 ,AM, 5600.0 )                                                    |
| MotherCut        | (BPVDIRA \> 0.9999) & (MIPCHI2DV(PRIMARY) \< 20) & (VFASPF(VCHI2/VDOF) \< 9.0 )   |
| DecayDescriptor  | B0 -\> phi(1020) rho(770)0                                                        |
| DecayDescriptors | [ 'B0 -\> phi(1020) rho(770)0' ]                                                |
| Output           | Phys/BsPhiRhoLine/Particles                                                       |

AddRelatedInfo/RelatedInfo1_BsPhiRhoLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/TrackListBsPhiRho' ]           |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo1_BsPhiRhoLine/Particles |

AddRelatedInfo/RelatedInfo2_BsPhiRhoLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/TrackListBsPhiRho' ]           |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo2_BsPhiRhoLine/Particles |

AddRelatedInfo/RelatedInfo3_BsPhiRhoLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/TrackListBsPhiRho' ]           |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo3_BsPhiRhoLine/Particles |

AddRelatedInfo/RelatedInfo4_BsPhiRhoLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/TrackListBsPhiRho' ]           |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo4_BsPhiRhoLine/Particles |

AddRelatedInfo/RelatedInfo5_BsPhiRhoLine

|                 |                                          |
|-----------------|------------------------------------------|
| Inputs          | [ 'Phys/BsPhiRhoLine' ]                |
| DecayDescriptor | None                                     |
| Output          | Phys/RelatedInfo5_BsPhiRhoLine/Particles |
