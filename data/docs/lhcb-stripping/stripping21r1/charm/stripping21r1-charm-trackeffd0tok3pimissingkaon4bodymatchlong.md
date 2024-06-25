[[stripping21r1 lines]](./stripping21r1-index)

# StrippingTrackEffD0ToK3PiMissingKaon4BodyMatchLong

## Properties:

|                |                                                          |
|----------------|----------------------------------------------------------|
| OutputLocation | Phys/TrackEffD0ToK3PiMissingKaon4BodyMatchLong/Particles |
| Postscale      | 1.0000000                                                |
| HLT            | HLT_PASS_RE('Hlt2.\*CharmHadD02HHXDst.\*Decision')       |
| Prescale       | 1.0000000                                                |
| L0DU           | None                                                     |
| ODIN           | None                                                     |

## Filter sequence:

LoKi::VoidFilter/StrippingTrackEffD0ToK3PiMissingKaon4BodyMatchLongVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 180 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

FilterDesktop/SelLongPionsForTrackEffD0ToK3Pi

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PIDK \< 4) & (TRGHOSTPROB \< 0.35)                                         |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/SelLongPionsForTrackEffD0ToK3Pi/Particles                              |

CombineParticles/ForTrackEffD0ToK3PiMissingKaon4BodySelKst

|                  |                                                                                                                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelLongPionsForTrackEffD0ToK3Pi' ]                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                                                                  |
| CombinationCut   | (APT \> 2000\*MeV) & (AM \< 1800\*MeV)& (AM - ACHILD(M,1) - ACHILD(M,2) - ACHILD(M,3) \> 100\*MeV)& (ANUM(PT \> 500\*MeV)\>=2)& (AMAXCHILD(MIPCHI2DV(PRIMARY)) \> 30)& (ADOCACHI2CUT(10,''))& (AM \< 1400\*MeV) |
| MotherCut        | (VFASPF(VZ) \> 5.0) & (BPVDIRA \> 0.99) & (VFASPF(VCHI2/VDOF)\< 3.0)                                                                                                                                            |
| DecayDescriptor  | None                                                                                                                                                                                                            |
| DecayDescriptors | [ '[K\*(892)+ -\> pi+ pi+ pi-]cc' , '[K\*(892)+ -\> pi+ pi+ pi+]cc' ]                                                                                                                                     |
| Output           | Phys/ForTrackEffD0ToK3PiMissingKaon4BodySelKst/Particles                                                                                                                                                        |

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

NoPIDsParticleMaker/ForTrackEffD0ToK3PiSelAllVeloPartsVeloKaons

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/VeloProtosForTrackEffD0ToK3Pi' ]           |
| DecayDescriptor | kaon                                                       |
| Output          | Phys/ForTrackEffD0ToK3PiSelAllVeloPartsVeloKaons/Particles |

FilterDesktop/ForTrackEffD0ToK3PiSelVeloPartsVeloKaons

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Code            | (MIPDV(PRIMARY) \> 0.05)                                 |
| Inputs          | [ 'Phys/ForTrackEffD0ToK3PiSelAllVeloPartsVeloKaons' ] |
| DecayDescriptor | None                                                     |
| Output          | Phys/ForTrackEffD0ToK3PiSelVeloPartsVeloKaons/Particles  |

CombineParticles/ForTrackEffD0ToK3PiMissingKaon4BodySelD0

|                  |                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ForTrackEffD0ToK3PiMissingKaon4BodySelKst' , 'Phys/ForTrackEffD0ToK3PiSelVeloPartsVeloKaons' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                 |
| CombinationCut   | (AMAXDOCA('') \< 0.05 )                                                                                  |
| MotherCut        | (abs(DTF_FUN(M,True) - 1865) \< 250\*MeV)                                                                |
| DecayDescriptor  | None                                                                                                     |
| DecayDescriptors | [ '[D0 -\> K\*(892)+ K+]cc' , '[D0 -\> K\*(892)+ K-]cc' ]                                          |
| Output           | Phys/ForTrackEffD0ToK3PiMissingKaon4BodySelD0/Particles                                                  |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/ForTrackEffD0ToK3PiMissingKaon4BodySelDstarf

|                  |                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ForTrackEffD0ToK3PiMissingKaon4BodySelD0' , 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY) \< 9) & (PIDe \< 5) & (PT \> 300\*MeV)' , 'pi-' : '(MIPCHI2DV(PRIMARY) \< 9) & (PIDe \< 5) & (PT \> 300\*MeV)' } |
| CombinationCut   | (APT \> 3500\*MeV) & (AALLSAMEBPV)                                                                                                                                                          |
| MotherCut        | (in_range ( 2 \* GeV , mfit , 2035.0 )) & (DTF_CHI2NDOF(True,'D0') \< 3.0)                                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                        |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' , '[D\*(2010)+ -\> D~0 pi+]cc' ]                                                                                                                        |
| Output           | Phys/ForTrackEffD0ToK3PiMissingKaon4BodySelDstarf/Particles                                                                                                                                 |

TisTosParticleTagger/SelForTrackEffD0ToK3PiMissingKaon4BodySelDstarTOS_TriggerTos

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Inputs          | [ 'Phys/ForTrackEffD0ToK3PiMissingKaon4BodySelDstarf' ]                   |
| DecayDescriptor | None                                                                        |
| Output          | Phys/SelForTrackEffD0ToK3PiMissingKaon4BodySelDstarTOS_TriggerTos/Particles |
| TisTosSpecs     | { 'Hlt2.\*CharmHadD02HHXDst.\*Decision%TOS' : 0 }                           |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

CombineParticles/TrackEffD0ToK3PiMissingKaon4BodyMatchLong

|                  |                                                                                                                                                                                                              |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ForTrackEffD0ToK3PiMissingKaon4BodySelKst' , 'Phys/SelForTrackEffD0ToK3PiMissingKaon4BodySelDstarTOS_TriggerTos' , 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'pi+' : '(ISLONG) & (TRGHOSTPROB \< 0.35)' , 'pi-' : '(ISLONG) & (TRGHOSTPROB \< 0.35)' }                                                         |
| CombinationCut   | (AMAXDOCA('') \< 0.10 \* mm )                                                                                                                                                                                |
| MotherCut        | ALL                                                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                         |
| DecayDescriptors | [ '[K\*\_0(1430)0 -\> K\*(892)+ pi-]cc' , '[K\*\_0(1430)0 -\> K\*(892)+ pi+]cc' ]                                                                                                                      |
| Output           | Phys/TrackEffD0ToK3PiMissingKaon4BodyMatchLong/Particles                                                                                                                                                     |
