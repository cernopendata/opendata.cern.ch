[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingDetachedMuMuKstarPairLine

## Properties:

|                |                                          |
|----------------|------------------------------------------|
| OutputLocation | Phys/DetachedMuMuKstarPairLine/Particles |
| Postscale      | 1.0000000                                |
| HLT1           | None                                     |
| HLT2           | None                                     |
| Prescale       | 1.0000000                                |
| L0DU           | None                                     |
| ODIN           | None                                     |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

LoKi::VoidFilter/StrippingDetachedMuMuKstarPairLineVOIDFilter

|      |                                                                 |
|------|-----------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 150 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdAllLooseKaons

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLooseKaons/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdAllLoosePions

|      |                                    |
|------|------------------------------------|
| Code | 0StdAllLoosePions/Particles',True) |

CombineParticles/DetachedKstars_For_ElectronRecoEff

|                  |                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21r0p2-commonparticles-stdallloosekaons)' , 'Phys/[StdAllLoosePions](./stripping21r0p2-commonparticles-stdallloosepions)' ]                                                                                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(MIPCHI2DV(PRIMARY)\>8) & (PROBNNk\>0.1) & (PT\>250.0)' , 'K-' : '(MIPCHI2DV(PRIMARY)\>8) & (PROBNNk\>0.1) & (PT\>250.0)' , 'pi+' : '(MIPCHI2DV(PRIMARY)\>8) & (PROBNNpi\>0.1) & (PT\>250.0)' , 'pi-' : '(MIPCHI2DV(PRIMARY)\>8) & (PROBNNpi\>0.1) & (PT\>250.0)' } |
| CombinationCut   | in_range(600.0, AM, 1050.0) & (APT\>500)                                                                                                                                                                                                                                                   |
| MotherCut        | in_range(750.0, M, 1000.0) & (VFASPF(VCHI2/VDOF) \< 20) & (MIPCHI2DV(PRIMARY)\>4)                                                                                                                                                                                                          |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                                       |
| DecayDescriptors | [ '[K\*(892)0 -\> K- pi+]cc' ]                                                                                                                                                                                                                                                         |
| Output           | Phys/DetachedKstars_For_ElectronRecoEff/Particles                                                                                                                                                                                                                                          |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsMuons

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsMuons/Particles',True) |

FilterDesktop/DetachedMuons_For_ElectronRecoEff

|                 |                                                                                                                                 |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MIPDV(PRIMARY)\>0.0) & (MIPCHI2DV(PRIMARY)\>12) & (PT\> 1200.0) & (TRCHI2DOF\<5) & in_range(1.8, ETA, 5.1) & (PROBNNmu \> 0.5) |
| Inputs          | [ 'Phys/[StdNoPIDsMuons](./stripping21r0p2-commonparticles-stdnopidsmuons)' ]                                                 |
| DecayDescriptor | None                                                                                                                            |
| Output          | Phys/DetachedMuons_For_ElectronRecoEff/Particles                                                                                |

LoKi::L0Filter/MuKstar_L0Selection

|      |                               |
|------|-------------------------------|
| Code | L0_CHANNEL_RE('Muon\|Hadron') |

CombineParticles/SelMuKstar_for_DetachedMuKstarPair

|                  |                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedKstars_For_ElectronRecoEff' , 'Phys/DetachedMuons_For_ElectronRecoEff' ]                |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }               |
| CombinationCut   | (AM \< 5400.0)                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10) & (BPVDIRA \> 0.95) & (BPVVDCHI2 \> 100) & (VFASPF(VMINVDDV(PRIMARY)) \> 2.0 ) |
| DecayDescriptor  | None                                                                                                      |
| DecayDescriptors | [ '[J/psi(1S) -\> mu+ K\*(892)0]cc' , '[J/psi(1S) -\> mu- K\*(892)0]cc' ]                           |
| Output           | Phys/SelMuKstar_for_DetachedMuKstarPair/Particles                                                         |

FilterDesktop/MuKstar_HLT1Selection

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | Hlt1TOS('Hlt1Track\*.\*Decision')               |
| Inputs          | [ 'Phys/SelMuKstar_for_DetachedMuKstarPair' ] |
| DecayDescriptor | None                                            |
| Output          | Phys/MuKstar_HLT1Selection/Particles            |

FilterDesktop/MuKstar_HLT2Selection

|                 |                                                |
|-----------------|------------------------------------------------|
| Code            | Hlt2TOS('Hlt2Topo(Mu)?(2\|3)BodyBBDTDecision') |
| Inputs          | [ 'Phys/MuKstar_HLT1Selection' ]             |
| DecayDescriptor | None                                           |
| Output          | Phys/MuKstar_HLT2Selection/Particles           |

GaudiSequencer/ForElectronRecoEffMakeVeloTracksGS

FastVeloTracking/ForElectronRecoEffFastVelo

TrackStateInitAlg/ForElectronRecoEffInitSeedFit

TrackContainerCopy/ForElectronRecoEffCopyVelo

TrackEventFitter/ForElectronRecoEffVeloRefitterAlg

ChargedProtoParticleMaker/ForElectronRecoEffVeloProtoMaker

|        |                                                  |
|--------|--------------------------------------------------|
| Inputs | [ 'Rec/Track/PreparedVeloForElectronRecoEff' ] |
| Output | Rec/ProtoP/VeloProtosForElectronRecoEff          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

NoPIDsParticleMaker/ForElectronRecoEffSelAllVeloPartsVeloMuons

|                 |                                                           |
|-----------------|-----------------------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/VeloProtosForElectronRecoEff' ]           |
| DecayDescriptor | muons                                                     |
| Output          | Phys/ForElectronRecoEffSelAllVeloPartsVeloMuons/Particles |

FilterDesktop/ForElectronRecoEffSelVeloPartsVeloMuons

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (MIPDV(PRIMARY) \> 0.04) & (TRCHI2DOF\<5.0) & in_range(1.9, ETA, 5.1) |
| Inputs          | [ 'Phys/ForElectronRecoEffSelAllVeloPartsVeloMuons' ]               |
| DecayDescriptor | None                                                                  |
| Output          | Phys/ForElectronRecoEffSelVeloPartsVeloMuons/Particles                |

CombineParticles/SelMuMuKstar_for_DetachedMuMuKstarPair

|                  |                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ForElectronRecoEffSelVeloPartsVeloMuons' , 'Phys/MuKstar_HLT2Selection' ]                                                                                             |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                            |
| CombinationCut   | (AM \< 6000.0)                                                                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20) & (log(B_MASS_CONSTRAINT_IP) \< -2.5) & in_range(5000.0, BMassFromConstraint, 5700.0) & in_range(750.0,Probe_Momentum_From_Mass_constraint,150000.0) |
| DecayDescriptor  | None                                                                                                                                                                            |
| DecayDescriptors | [ 'B+ -\> J/psi(1S) mu+' , 'B- -\> J/psi(1S) mu-' ]                                                                                                                           |
| Output           | Phys/SelMuMuKstar_for_DetachedMuMuKstarPair/Particles                                                                                                                           |

FilterDesktop/DetachedMuMuKstarPairLine

|                 |                                                     |
|-----------------|-----------------------------------------------------|
| Code            | (in_range(3500.0, B_MM_FROM_FD, 7000.0))            |
| Inputs          | [ 'Phys/SelMuMuKstar_for_DetachedMuMuKstarPair' ] |
| DecayDescriptor | None                                                |
| Output          | Phys/DetachedMuMuKstarPairLine/Particles            |
