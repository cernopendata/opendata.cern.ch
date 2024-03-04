[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingDetachedMuMuPhiPairLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/DetachedMuMuPhiPairLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 1.0000000                              |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

LoKi::VoidFilter/StrippingDetachedMuMuPhiPairLineVOIDFilter

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

CombineParticles/DetachedPhis_For_ElectronRecoEff

|                  |                                                                                                                                      |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllLooseKaons](./stripping21r0p2-commonparticles-stdallloosekaons)' ]                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : '(MIPCHI2DV(PRIMARY)\>7) & (PIDK\>1) & (PT\>200)' , 'K-' : '(MIPCHI2DV(PRIMARY)\>7) & (PIDK\>1) & (PT\>200)' } |
| CombinationCut   | in_range(900,AM,1100) & (APT\>400)                                                                                                   |
| MotherCut        | in_range(980,M,1050) & (VFASPF(VCHI2/VDOF) \< 100) & (MIPCHI2DV(PRIMARY)\>4)                                                         |
| DecayDescriptor  | None                                                                                                                                 |
| DecayDescriptors | [ 'phi(1020) -\> K- K+' ]                                                                                                          |
| Output           | Phys/DetachedPhis_For_ElectronRecoEff/Particles                                                                                      |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsMuons

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsMuons/Particles',True) |

FilterDesktop/LooseDetachedMuons_For_ElectronRecoEff

|                 |                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| Code            | (MIPDV(PRIMARY)\>0.0) & (MIPCHI2DV(PRIMARY)\>8) & (PT\> 1000.0) & (TRCHI2DOF\<5) & in_range(1.8, ETA, 5.1) & (PROBNNmu \> 0.2) |
| Inputs          | [ 'Phys/[StdNoPIDsMuons](./stripping21r0p2-commonparticles-stdnopidsmuons)' ]                                                |
| DecayDescriptor | None                                                                                                                           |
| Output          | Phys/LooseDetachedMuons_For_ElectronRecoEff/Particles                                                                          |

LoKi::L0Filter/MuPhi_L0Selection

|      |                               |
|------|-------------------------------|
| Code | L0_CHANNEL_RE('Muon\|Hadron') |

CombineParticles/SelMuPhi_for_DetachedMuPhiPair

|                  |                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedPhis_For_ElectronRecoEff' , 'Phys/LooseDetachedMuons_For_ElectronRecoEff' ]             |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'phi(1020)' : 'ALL' }                                      |
| CombinationCut   | (AM \< 5400.0)                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10) & (BPVDIRA \> 0.95) & (BPVVDCHI2 \> 100) & (VFASPF(VMINVDDV(PRIMARY)) \> 2.0 ) |
| DecayDescriptor  | None                                                                                                      |
| DecayDescriptors | [ '[J/psi(1S) -\> mu+ phi(1020)]cc' , '[J/psi(1S) -\> mu- phi(1020)]cc' ]                           |
| Output           | Phys/SelMuPhi_for_DetachedMuPhiPair/Particles                                                             |

FilterDesktop/MuPhi_HLT1Selection_for_DetachedMuPhiPair

|                 |                                                          |
|-----------------|----------------------------------------------------------|
| Code            | Hlt1TOS('Hlt1Track\*.\*Decision')                        |
| Inputs          | [ 'Phys/SelMuPhi_for_DetachedMuPhiPair' ]              |
| DecayDescriptor | None                                                     |
| Output          | Phys/MuPhi_HLT1Selection_for_DetachedMuPhiPair/Particles |

FilterDesktop/MuPhi_HLT2Selection_for_DetachedMuPhiPair

|                 |                                                                      |
|-----------------|----------------------------------------------------------------------|
| Code            | Hlt2TOS('(Hlt2Topo(Mu)?(2\|3)BodyBBDTDecision\|Hlt2IncPhiDecision)') |
| Inputs          | [ 'Phys/MuPhi_HLT1Selection_for_DetachedMuPhiPair' ]               |
| DecayDescriptor | None                                                                 |
| Output          | Phys/MuPhi_HLT2Selection_for_DetachedMuPhiPair/Particles             |

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

CombineParticles/SelMuMuPhi_for_DetachedMuMuPhiPair

|                  |                                                                                                                                                                                 |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ForElectronRecoEffSelVeloPartsVeloMuons' , 'Phys/MuPhi_HLT2Selection_for_DetachedMuPhiPair' ]                                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                            |
| CombinationCut   | (AM \< 6000.0)                                                                                                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20) & (log(B_MASS_CONSTRAINT_IP) \< -1.0) & in_range(5000.0, BMassFromConstraint, 5700.0) & in_range(750.0,Probe_Momentum_From_Mass_constraint,150000.0) |
| DecayDescriptor  | None                                                                                                                                                                            |
| DecayDescriptors | [ 'B+ -\> J/psi(1S) mu+' , 'B- -\> J/psi(1S) mu-' ]                                                                                                                           |
| Output           | Phys/SelMuMuPhi_for_DetachedMuMuPhiPair/Particles                                                                                                                               |

FilterDesktop/DetachedMuMuPhiPairLine

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | (in_range(3500.0, B_MM_FROM_FD, 7000.0))        |
| Inputs          | [ 'Phys/SelMuMuPhi_for_DetachedMuMuPhiPair' ] |
| DecayDescriptor | None                                            |
| Output          | Phys/DetachedMuMuPhiPairLine/Particles          |
