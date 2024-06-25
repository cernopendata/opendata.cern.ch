[[stripping21 lines]](./stripping21-index)

# StrippingCharmFromBSemiForHadronAsy_LbToLcStarMuLcToKpiRS

## Properties:

|                |                                                                 |
|----------------|-----------------------------------------------------------------|
| OutputLocation | Phys/CharmFromBSemiForHadronAsy_LbToLcStarMuLcToKpiRS/Particles |
| Postscale      | 1.0000000                                                       |
| HLT            | None                                                            |
| Prescale       | 1.0000000                                                       |
| L0DU           | None                                                            |
| ODIN           | None                                                            |

## Filter sequence:

LoKi::VoidFilter/StrippingCharmFromBSemiForHadronAsy_LbToLcStarMuLcToKpiRSVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuforCharmFromBSemiForHadronAsy

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 800.0 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDmu \> 0)                |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21-commonparticles-stdloosemuons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/MuforCharmFromBSemiForHadronAsy/Particles                            |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/SlowpiforCharmFromBSemiForHadronAsy

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT \> 200.0\*MeV) & (TRGHOSTPROB \< 0.35) & (PIDe \< 99.0)& (PIDK \< 10.0) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ]   |
| DecayDescriptor | None                                                                        |
| Output          | Phys/SlowpiforCharmFromBSemiForHadronAsy/Particles                          |

CombineParticles/SelPiPiRSForCharmFromBSemiForHadronAsy

|                  |                                                                                           |
|------------------|-------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SlowpiforCharmFromBSemiForHadronAsy' ]                                          |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                            |
| CombinationCut   | (AM \< 500.0\*MeV)& (ACUTDOCACHI2(15.0,''))& (ACHILD(PT,1) + ACHILD(PT,2) \> 600.0 \*MeV) |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 3.0)                                                                |
| DecayDescriptor  | None                                                                                      |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                             |
| Output           | Phys/SelPiPiRSForCharmFromBSemiForHadronAsy/Particles                                     |

CombineParticles/SelMuPiPiRSForCharmFromBSemiForHadronAsy

|                  |                                                                                              |
|------------------|----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuforCharmFromBSemiForHadronAsy' , 'Phys/SelPiPiRSForCharmFromBSemiForHadronAsy' ] |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'rho(770)0' : 'ALL' }                         |
| CombinationCut   | (ACUTDOCACHI2(15.0,''))                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 3.0)& (BPVVDCHI2 \> 20.0)                                              |
| DecayDescriptor  | None                                                                                         |
| DecayDescriptors | [ '[K\*(892)+ -\> mu+ rho(770)0]cc' ]                                                    |
| Output           | Phys/SelMuPiPiRSForCharmFromBSemiForHadronAsy/Particles                                      |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KforCharmFromBSemiForHadronAsy

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 250.0 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDK \> 6.0)               |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/KforCharmFromBSemiForHadronAsy/Particles                             |

FilterDesktop/PiforCharmFromBSemiForHadronAsy

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT \> 250.0 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDK \< 6.0)               |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/PiforCharmFromBSemiForHadronAsy/Particles                            |

CombineParticles/SelLcToKpiRSForCharmFromBSemiForHadronAsy

|                  |                                                                                                                        |
|------------------|------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KforCharmFromBSemiForHadronAsy' , 'Phys/PiforCharmFromBSemiForHadronAsy' ]                                   |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                           |
| CombinationCut   | (ACHILD(PT,1)+ACHILD(PT,2) \> 1500.0 \*MeV)& (AM+10 \> 800.0 \*MeV)& (AM-10 \< 1350.0 \*MeV)& (ADOCACHI2CUT(10.0, '')) |
| MotherCut        | (M \> 800.0 \*MeV)& (M \< 1350.0 \*MeV)& (VFASPF(VCHI2/VDOF)\< 3.0)& (BPVVDCHI2 \> 20.0)                               |
| DecayDescriptor  | None                                                                                                                   |
| DecayDescriptors | [ '[Lambda_c+ -\> K- pi+]cc' ]                                                                                     |
| Output           | Phys/SelLcToKpiRSForCharmFromBSemiForHadronAsy/Particles                                                               |

CombineParticles/SelLbRSForCharmFromBSemiForHadronAsy

|                  |                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelLcToKpiRSForCharmFromBSemiForHadronAsy' , 'Phys/SelMuPiPiRSForCharmFromBSemiForHadronAsy' ]                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' }                                                                                                            |
| CombinationCut   | (DELTA_MASS_LC \< 700.0 \*MeV)& (AM \> 2200.0 \*MeV) & (AM \< 4300.0 \*MeV)& (ACUTDOCACHI2(50.0,''))                                                                                                               |
| MotherCut        | (M \> 2200.0 \*MeV) & (M \< 4300.0 \*MeV)& (MINTREE((ABSID=='Lambda_c+'),VFASPF(VZ)) - MINTREE((ABSID=='K\*(892)-'),VFASPF(VZ)) \> 1.0 \*mm )& (VFASPF(VCHI2/VDOF) \< 15.0)& (BPVDIRA\> 0.99)& (BPVVDCHI2 \> 20.0) |
| DecayDescriptor  | None                                                                                                                                                                                                               |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda_c+ K\*(892)-]cc' ]                                                                                                                                                                    |
| Output           | Phys/SelLbRSForCharmFromBSemiForHadronAsy/Particles                                                                                                                                                                |

TisTosParticleTagger/SelLbRSForCharmFromBSemiForHadronAsy_Hlt1TOS

|                 |                                                             |
|-----------------|-------------------------------------------------------------|
| Inputs          | [ 'Phys/SelLbRSForCharmFromBSemiForHadronAsy' ]           |
| DecayDescriptor | None                                                        |
| Output          | Phys/SelLbRSForCharmFromBSemiForHadronAsy_Hlt1TOS/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }                               |

TisTosParticleTagger/CharmFromBSemiForHadronAsy_LbToLcStarMuLcToKpiRS

|                 |                                                                 |
|-----------------|-----------------------------------------------------------------|
| Inputs          | [ 'Phys/SelLbRSForCharmFromBSemiForHadronAsy_Hlt1TOS' ]       |
| DecayDescriptor | None                                                            |
| Output          | Phys/CharmFromBSemiForHadronAsy_LbToLcStarMuLcToKpiRS/Particles |
| TisTosSpecs     | { 'Hlt2.\*Decision%TOS' : 0 }                                   |
