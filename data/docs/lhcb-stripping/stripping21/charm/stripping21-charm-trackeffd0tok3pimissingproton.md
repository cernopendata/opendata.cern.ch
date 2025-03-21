[[stripping21 lines]](./stripping21-index)

# StrippingTrackEffD0ToK3PiMissingProton

## Properties:

|                |                                                    |
|----------------|----------------------------------------------------|
| OutputLocation | Phys/TrackEffD0ToK3PiMissingProton/Particles       |
| Postscale      | 1.0000000                                          |
| HLT            | HLT_PASS_RE('Hlt2.\*CharmHadD02HHXDst.\*Decision') |
| Prescale       | 1.0000000                                          |
| L0DU           | None                                               |
| ODIN           | None                                               |

## Filter sequence:

LoKi::VoidFilter/StrippingTrackEffD0ToK3PiMissingProtonVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 180 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/SelLongKaonsForTrackEffD0ToK3Pi

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PIDK \> 7) & (TRGHOSTPROB \< 0.35)                                       |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/SelLongKaonsForTrackEffD0ToK3Pi/Particles                            |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/SelLongPionsForTrackEffD0ToK3Pi

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PIDK \< 4) & (TRGHOSTPROB \< 0.35)                                       |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/SelLongPionsForTrackEffD0ToK3Pi/Particles                            |

CombineParticles/ForTrackEffD0ToK3PiMissingProtonSelKst

|                  |                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelLongKaonsForTrackEffD0ToK3Pi' , 'Phys/SelLongPionsForTrackEffD0ToK3Pi' ]                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                   |
| CombinationCut   | (APT \> 1500\*MeV) & (AM \< 1500\*MeV)& (AM - ACHILD(M,1) - ACHILD(M,2) \> 100\*MeV)& (ANUM(PT \> 500\*MeV)\>=2)& (AMAXCHILD(MIPCHI2DV(PRIMARY)) \> 30)& (ADOCACHI2CUT(15,'')) |
| MotherCut        | (VFASPF(VZ) \> 2.0) & (BPVDIRA \> 0.99) & (VFASPF(VCHI2/VDOF)\< 3.0)                                                                                                           |
| DecayDescriptor  | None                                                                                                                                                                           |
| DecayDescriptors | [ '[K\*(892)+ -\> K- pi+]cc' , '[K\*(892)+ -\> K- pi-]cc' ]                                                                                                              |
| Output           | Phys/ForTrackEffD0ToK3PiMissingProtonSelKst/Particles                                                                                                                          |

GaudiSequencer/ForTrackEffD0ToK3PiMakeVeloTracksGS

FastVeloTracking/ForTrackEffD0ToK3PiFastVelo

TrackStateInitAlg/ForTrackEffD0ToK3PiInitSeedFit

TrackContainerCopy/ForTrackEffD0ToK3PiCopyVelo

TrackEventFitter/ForTrackEffD0ToK3PiVeloRefitterAlg

ChargedProtoParticleMaker/ForTrackEffD0ToK3PiVeloProtoMaker

|        |                                                   |
|--------|---------------------------------------------------|
| Inputs | [ 'Rec/Track/PreparedVeloForTrackEffD0ToK3Pi' ] |
| Output | Rec/ProtoP/VeloProtosForTrackEffD0ToK3Pi          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

NoPIDsParticleMaker/ForTrackEffD0ToK3PiSelAllVeloPartsVeloProtons

|                 |                                                              |
|-----------------|--------------------------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/VeloProtosForTrackEffD0ToK3Pi' ]             |
| DecayDescriptor | proton                                                       |
| Output          | Phys/ForTrackEffD0ToK3PiSelAllVeloPartsVeloProtons/Particles |

FilterDesktop/ForTrackEffD0ToK3PiSelVeloPartsVeloProtons

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Code            | (MIPDV(PRIMARY) \> 0.05)                                   |
| Inputs          | [ 'Phys/ForTrackEffD0ToK3PiSelAllVeloPartsVeloProtons' ] |
| DecayDescriptor | None                                                       |
| Output          | Phys/ForTrackEffD0ToK3PiSelVeloPartsVeloProtons/Particles  |

CombineParticles/ForTrackEffD0ToK3PiMissingProtonSelD0

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ForTrackEffD0ToK3PiMissingProtonSelKst' , 'Phys/ForTrackEffD0ToK3PiSelVeloPartsVeloProtons' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }               |
| CombinationCut   | (AMAXDOCA('') \< 0.05 )                                                                                 |
| MotherCut        | (abs(DTF_FUN(M,True) - 2286) \< 250\*MeV)                                                               |
| DecayDescriptor  | None                                                                                                    |
| DecayDescriptors | [ '[Lambda_c+ -\> K\*(892)+ p+]cc' , '[Lambda_c+ -\> K\*(892)+ p~-]cc' ]                          |
| Output           | Phys/ForTrackEffD0ToK3PiMissingProtonSelD0/Particles                                                    |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/ForTrackEffD0ToK3PiMissingProtonSelDstarf

|                  |                                                                                                                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ForTrackEffD0ToK3PiMissingProtonSelD0' , 'Phys/[StdAllLoosePions](./stripping21-commonparticles-stdallloosepions)' ]                                                                            |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda_c+' : 'ALL' , 'Lambda_c~-' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY) \< 9) & (PIDe \< 5) & (PT \> 300\*MeV)' , 'pi-' : '(MIPCHI2DV(PRIMARY) \< 9) & (PIDe \< 5) & (PT \> 300\*MeV)' } |
| CombinationCut   | (APT \> 3500\*MeV) & (AALLSAMEBPV)                                                                                                                                                                        |
| MotherCut        | (in_range ( 2.4 \* GeV , mfit , 2500.0 )) & (DTF_CHI2NDOF(True,'Lambda_c+') \< 3.0)                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                      |
| DecayDescriptors | [ '[Sigma_c0 -\> Lambda_c+ pi+]cc' , '[Sigma_c0 -\> Lambda_c+ pi-]cc' ]                                                                                                                             |
| Output           | Phys/ForTrackEffD0ToK3PiMissingProtonSelDstarf/Particles                                                                                                                                                  |

TisTosParticleTagger/TrackEffD0ToK3PiMissingProton

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Inputs          | [ 'Phys/ForTrackEffD0ToK3PiMissingProtonSelDstarf' ] |
| DecayDescriptor | None                                                   |
| Output          | Phys/TrackEffD0ToK3PiMissingProton/Particles           |
| TisTosSpecs     | { 'Hlt2.\*CharmHadD02HHXDst.\*Decision%TOS' : 0 }      |
