[[stripping21r1 lines]](./stripping21r1-index)

# StrippingTrackEffD0ToK3PiMissingPion4Body

## Properties:

|                |                                                    |
|----------------|----------------------------------------------------|
| OutputLocation | Phys/TrackEffD0ToK3PiMissingPion4Body/Particles    |
| Postscale      | 1.0000000                                          |
| HLT            | HLT_PASS_RE('Hlt2.\*CharmHadD02HHXDst.\*Decision') |
| Prescale       | 1.0000000                                          |
| L0DU           | None                                               |
| ODIN           | None                                               |

## Filter sequence:

LoKi::VoidFilter/StrippingTrackEffD0ToK3PiMissingPion4BodyVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 180 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/SelLongKaonsForTrackEffD0ToK3Pi

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | (PIDK \> 7) & (TRGHOSTPROB \< 0.35)                                         |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/SelLongKaonsForTrackEffD0ToK3Pi/Particles                              |

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

CombineParticles/ForTrackEffD0ToK3PiMissingPion4BodySelKst

|                  |                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/SelLongKaonsForTrackEffD0ToK3Pi' , 'Phys/SelLongPionsForTrackEffD0ToK3Pi' ]                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                                                                                 |
| CombinationCut   | (APT \> 2000\*MeV) & (AM \< 1800\*MeV)& (AM - ACHILD(M,1) - ACHILD(M,2) - ACHILD(M,3) \> 100\*MeV)& (ANUM(PT \> 500\*MeV)\>=2)& (AMAXCHILD(MIPCHI2DV(PRIMARY)) \> 30)& (ADOCACHI2CUT(10,'')) |
| MotherCut        | (VFASPF(VZ) \> 5.0) & (BPVDIRA \> 0.99) & (VFASPF(VCHI2/VDOF)\< 3.0)                                                                                                                         |
| DecayDescriptor  | None                                                                                                                                                                                         |
| DecayDescriptors | [ '[K\*(892)+ -\> K- pi+ pi+]cc' , '[K\*(892)+ -\> K- pi+ pi-]cc' , '[K\*(892)+ -\> K- pi- pi-]cc' ]                                                                                 |
| Output           | Phys/ForTrackEffD0ToK3PiMissingPion4BodySelKst/Particles                                                                                                                                     |

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

NoPIDsParticleMaker/ForTrackEffD0ToK3PiSelAllVeloPartsVeloPions

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/VeloProtosForTrackEffD0ToK3Pi' ]           |
| DecayDescriptor | pion                                                       |
| Output          | Phys/ForTrackEffD0ToK3PiSelAllVeloPartsVeloPions/Particles |

FilterDesktop/ForTrackEffD0ToK3PiSelVeloPartsVeloPions

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Code            | (MIPDV(PRIMARY) \> 0.05)                                 |
| Inputs          | [ 'Phys/ForTrackEffD0ToK3PiSelAllVeloPartsVeloPions' ] |
| DecayDescriptor | None                                                     |
| Output          | Phys/ForTrackEffD0ToK3PiSelVeloPartsVeloPions/Particles  |

CombineParticles/ForTrackEffD0ToK3PiMissingPion4BodySelD0

|                  |                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ForTrackEffD0ToK3PiMissingPion4BodySelKst' , 'Phys/ForTrackEffD0ToK3PiSelVeloPartsVeloPions' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }               |
| CombinationCut   | (AMAXDOCA('') \< 0.05 )                                                                                  |
| MotherCut        | (abs(DTF_FUN(M,True) - 1865) \< 250\*MeV)                                                                |
| DecayDescriptor  | None                                                                                                     |
| DecayDescriptors | [ '[D0 -\> K\*(892)+ pi+]cc' , '[D0 -\> K\*(892)+ pi-]cc' ]                                        |
| Output           | Phys/ForTrackEffD0ToK3PiMissingPion4BodySelD0/Particles                                                  |

LoKi::VoidFilter/SelFilterPhys_StdAllLoosePions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)/Particles')\>0 |

CombineParticles/ForTrackEffD0ToK3PiMissingPion4BodySelDstarf

|                  |                                                                                                                                                                                             |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ForTrackEffD0ToK3PiMissingPion4BodySelD0' , 'Phys/[StdAllLoosePions](./stripping21r1-commonparticles-stdallloosepions)' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'D0' : 'ALL' , 'D~0' : 'ALL' , 'pi+' : '(MIPCHI2DV(PRIMARY) \< 9) & (PIDe \< 5) & (PT \> 300\*MeV)' , 'pi-' : '(MIPCHI2DV(PRIMARY) \< 9) & (PIDe \< 5) & (PT \> 300\*MeV)' } |
| CombinationCut   | (APT \> 3500\*MeV) & (AALLSAMEBPV)                                                                                                                                                          |
| MotherCut        | (in_range ( 2 \* GeV , mfit , 2035.0 )) & (DTF_CHI2NDOF(True,'D0') \< 3.0)                                                                                                                  |
| DecayDescriptor  | None                                                                                                                                                                                        |
| DecayDescriptors | [ '[D\*(2010)+ -\> D0 pi+]cc' , '[D\*(2010)+ -\> D~0 pi+]cc' ]                                                                                                                        |
| Output           | Phys/ForTrackEffD0ToK3PiMissingPion4BodySelDstarf/Particles                                                                                                                                 |

TisTosParticleTagger/TrackEffD0ToK3PiMissingPion4Body

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Phys/ForTrackEffD0ToK3PiMissingPion4BodySelDstarf' ] |
| DecayDescriptor | None                                                      |
| Output          | Phys/TrackEffD0ToK3PiMissingPion4Body/Particles           |
| TisTosSpecs     | { 'Hlt2.\*CharmHadD02HHXDst.\*Decision%TOS' : 0 }         |
