[[stripping21r1 lines]](./stripping21r1-index)

# StrippingCharmFromBSemiForHadronAsy_B2DstarMuD0to3piWS

## Properties:

|                |                                                              |
|----------------|--------------------------------------------------------------|
| OutputLocation | Phys/CharmFromBSemiForHadronAsy_B2DstarMuD0to3piWS/Particles |
| Postscale      | 1.0000000                                                    |
| HLT            | None                                                         |
| Prescale       | 0.20000000                                                   |
| L0DU           | None                                                         |
| ODIN           | None                                                         |

## Filter sequence:

LoKi::VoidFilter/StrippingCharmFromBSemiForHadronAsy_B2DstarMuD0to3piWSVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseMuons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)/Particles')\>0 |

FilterDesktop/MuforCharmFromBSemiForHadronAsy

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT \> 800.0 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDmu \> 0)                  |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1-commonparticles-stdloosemuons)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/MuforCharmFromBSemiForHadronAsy/Particles                              |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/SlowpiforCharmFromBSemiForHadronAsy

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT \> 200.0\*MeV) & (TRGHOSTPROB \< 0.35) & (PIDe \< 99.0)& (PIDK \< 10.0) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/SlowpiforCharmFromBSemiForHadronAsy/Particles                          |

CombineParticles/SelMuPiWSForCharmFromBSemiForHadronAsy

|                  |                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuforCharmFromBSemiForHadronAsy' , 'Phys/SlowpiforCharmFromBSemiForHadronAsy' ]                                           |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                      |
| CombinationCut   | (ACHILD(PT,1)+ACHILD(PT,2) \> 1300.0 \*MeV)& (ADOCACHI2CUT(8.0, ''))                                                                |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 3.0)& (BPVDIRA\> -99.0)& (BPVVDCHI2 \> 20.0)                                                                 |
| DecayDescriptor  | None                                                                                                                                |
| DecayDescriptors | [ '[K\*(892)+ -\> mu+ pi-]cc' , '[K\*(892)+ -\> mu- pi+]cc' , '[K\*(892)+ -\> mu+ pi+]cc' , '[K\*(892)+ -\> mu- pi-]cc' ] |
| Output           | Phys/SelMuPiWSForCharmFromBSemiForHadronAsy/Particles                                                                               |

FilterDesktop/PiforCharmFromBSemiForHadronAsy

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PT \> 250.0 \*MeV) & (TRGHOSTPROB \< 0.35) & (PIDK \< 6.0)                 |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/PiforCharmFromBSemiForHadronAsy/Particles                              |

CombineParticles/SelD0To3piWSForCharmFromBSemiForHadronAsy

|                  |                                                                                                                                    |
|------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/PiforCharmFromBSemiForHadronAsy' ]                                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                     |
| CombinationCut   | (AM+10 \> 900.0 \*MeV) & (AM-10 \< 1400.0 \*MeV)& (ADOCACHI2CUT(10.0, ''))& (ACHILD(PT,1) + ACHILD(PT,2) + ACHILD(PT,3) \> 1800.0) |
| MotherCut        | (M \> 900.0 \*MeV) & (M \< 1400.0 \*MeV)& (VFASPF(VCHI2/VDOF)\< 3.0)                                                               |
| DecayDescriptor  | None                                                                                                                               |
| DecayDescriptors | [ '[D0 -\> pi+ pi- pi+]cc' , '[D0 -\> pi+ pi+ pi+]cc' ]                                                                      |
| Output           | Phys/SelD0To3piWSForCharmFromBSemiForHadronAsy/Particles                                                                           |

CombineParticles/SelBtoDstarMuD0to3pi_WSForCharmFromBSemiForHadronAsy

|                  |                                                                                                                                                                                        |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelD0To3piWSForCharmFromBSemiForHadronAsy' , 'Phys/SelMuPiWSForCharmFromBSemiForHadronAsy' ]                                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' }                                                                                              |
| CombinationCut   | (DELTA_MASS \< 350.0 \*MeV)& (ADOCACHI2CUT(50.0, ''))                                                                                                                                  |
| MotherCut        | (M \> 1800.0 \*MeV) & (M \< 4900.0 \*MeV)& (MINTREE((ABSID=='D0'),VFASPF(VZ)) - MINTREE((ABSID=='K\*(892)+'),VFASPF(VZ)) \> 2.0 \*mm )& (VFASPF(VCHI2/VDOF) \< 15.0)& (BPVDIRA\> 0.99) |
| DecayDescriptor  | None                                                                                                                                                                                   |
| DecayDescriptors | [ '[B0 -\> D~0 K\*(892)+]cc' ]                                                                                                                                                     |
| Output           | Phys/SelBtoDstarMuD0to3pi_WSForCharmFromBSemiForHadronAsy/Particles                                                                                                                    |

TisTosParticleTagger/SelBtoDstarMuD0to3pi_WSForCharmFromBSemiForHadronAsy_Hlt1TOS

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/SelBtoDstarMuD0to3pi_WSForCharmFromBSemiForHadronAsy' ]           |
| DecayDescriptor | None                                                                        |
| Output          | Phys/SelBtoDstarMuD0to3pi_WSForCharmFromBSemiForHadronAsy_Hlt1TOS/Particles |
| TisTosSpecs     | { 'Hlt1.\*Decision%TOS' : 0 }                                               |

TisTosParticleTagger/CharmFromBSemiForHadronAsy_B2DstarMuD0to3piWS

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Inputs          | [ 'Phys/SelBtoDstarMuD0to3pi_WSForCharmFromBSemiForHadronAsy_Hlt1TOS' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/CharmFromBSemiForHadronAsy_B2DstarMuD0to3piWS/Particles              |
| TisTosSpecs     | { 'Hlt2.\*Decision%TOS' : 0 }                                             |
