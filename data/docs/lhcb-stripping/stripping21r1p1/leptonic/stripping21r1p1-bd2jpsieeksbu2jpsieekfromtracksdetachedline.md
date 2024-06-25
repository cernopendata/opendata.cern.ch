[[stripping21r1p1 lines]](./stripping21r1p1-index)

# StrippingBd2JpsieeKSBu2JpsieeKFromTracksDetachedLine

## Properties:

|                |                                                            |
|----------------|------------------------------------------------------------|
| OutputLocation | Phys/Bd2JpsieeKSBu2JpsieeKFromTracksDetachedLine/Particles |
| Postscale      | 1.0000000                                                  |
| HLT1           | None                                                       |
| HLT2           | None                                                       |
| Prescale       | 1.0000000                                                  |
| L0DU           | None                                                       |
| ODIN           | None                                                       |

## Filter sequence:

**LoKi::VoidFilter/StrippingGoodEventConditionLeptonic**

|      |                                                                                                   |
|------|---------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamLeptonicBadEvent') & \~ALG_PASSED('StrippingStreamLeptonicBadEvent') |

**CheckPV/checkPVmin1**

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

**LoKi::VoidFilter/SelFilterPhys_StdDiElectronFromTracks_Particles**

|      |                                                                                                           |
|------|-----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdDiElectronFromTracks](./stripping21r1p1-stddielectronfromtracks) /Particles',True)\>0 |

**FilterDesktop/SelJpsi2eeFromTracksForBd2JpsieeKS**

|                 |                                                                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MM \> 2300.0 \*MeV) & (MM \< 3300.0 \*MeV) & (MINTREE('e+'==ABSID,PIDe-PIDpi) \> 0.0 ) & (MINTREE('e+'==ABSID,PT) \> 500.0 \*MeV) & (MAXTREE('e+'==ABSID,TRCHI2DOF) \< 5.0) & (VFASPF(VCHI2/VDOF) \< 15.0) |
| Inputs          | [ 'Phys/ [StdDiElectronFromTracks](./stripping21r1p1-stddielectronfromtracks) ' ]                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                        |
| Output          | Phys/SelJpsi2eeFromTracksForBd2JpsieeKS/Particles                                                                                                                                                           |

**LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles**

|      |                                                                                       |
|------|---------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/ [StdLooseKaons](./stripping21r1p1-stdloosekaons) /Particles',True)\>0 |

**FilterDesktop/KaonsForBetaSBd2JpsieeKS**

|                 |                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 3.0 ) & (PIDK \> 0.0 )& (INTREE((ABSID=='K+') & (MIPCHI2DV(PRIMARY) \> 9.0 ))) |
| Inputs          | [ 'Phys/ [StdLooseKaons](./stripping21r1p1-stdloosekaons) ' ]                              |
| DecayDescriptor | None                                                                                         |
| Output          | Phys/KaonsForBetaSBd2JpsieeKS/Particles                                                      |

**CombineParticles/Bu2JpsieeKFromTracksBd2JpsieeKS**

|                  |                                                                                                    |
|------------------|----------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KaonsForBetaSBd2JpsieeKS' , 'Phys/SelJpsi2eeFromTracksForBd2JpsieeKS' ]                  |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'K+' : '(PT \> 800.0 \*MeV)' , 'K-' : '(PT \> 800.0 \*MeV)' } |
| CombinationCut   | in_range(4400.0,AM,6000.0)                                                                         |
| MotherCut        | (VFASPF(VCHI2PDOF) \< 7.0)                                                                         |
| DecayDescriptor  | [B+ -\> J/psi(1S) K+]cc                                                                          |
| DecayDescriptors | [ '[B+ -\> J/psi(1S) K+]cc' ]                                                                  |
| Output           | Phys/Bu2JpsieeKFromTracksBd2JpsieeKS/Particles                                                     |

**FilterDesktop/Bd2JpsieeKSBu2JpsieeKFromTracksDetachedLine**

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | (BPVLTIME() \> 0.2\*ps) & (MINTREE('K+'==ABSID, PT) \> 800.0 \*MeV) |
| Inputs          | [ 'Phys/Bu2JpsieeKFromTracksBd2JpsieeKS' ]                        |
| DecayDescriptor | None                                                                |
| Output          | Phys/Bd2JpsieeKSBu2JpsieeKFromTracksDetachedLine/Particles          |
