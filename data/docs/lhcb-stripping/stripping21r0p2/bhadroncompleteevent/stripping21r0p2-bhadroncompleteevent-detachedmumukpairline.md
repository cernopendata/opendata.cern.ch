[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingDetachedMuMuKPairLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/DetachedMuMuKPairLine/Particles |
| Postscale      | 1.0000000                            |
| HLT1           | None                                 |
| HLT2           | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

LoKi::VoidFilter/StrippingDetachedMuMuKPairLineVOIDFilter

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

FilterDesktop/DetachedKaons_For_ElectronRecoEff

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY)\>12) & (PT\> 500.0) & (TRCHI2DOF\<5) & (PROBNNk \> 0.2)         |
| Inputs          | [ 'Phys/[StdAllLooseKaons](./stripping21r0p2-commonparticles-stdallloosekaons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/DetachedKaons_For_ElectronRecoEff/Particles                                    |

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

CombineParticles/SelMuK_for_DetachedMuKPair

|                  |                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedKaons_For_ElectronRecoEff' , 'Phys/DetachedMuons_For_ElectronRecoEff' ]                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                              |
| CombinationCut   | (AM \< 5400.0)                                                                                            |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10) & (BPVDIRA \> 0.95) & (BPVVDCHI2 \> 100) & (VFASPF(VMINVDDV(PRIMARY)) \> 2.0 ) |
| DecayDescriptor  | None                                                                                                      |
| DecayDescriptors | [ '[J/psi(1S) -\> mu+ K-]cc' , '[J/psi(1S) -\> mu+ K+]cc' ]                                         |
| Output           | Phys/SelMuK_for_DetachedMuKPair/Particles                                                                 |

FilterDesktop/MuK_L0TOSSelection_for_DetachedMuKPair

|                 |                                                       |
|-----------------|-------------------------------------------------------|
| Code            | L0TOS('L0MuonDecision')                               |
| Inputs          | [ 'Phys/SelMuK_for_DetachedMuKPair' ]               |
| DecayDescriptor | None                                                  |
| Output          | Phys/MuK_L0TOSSelection_for_DetachedMuKPair/Particles |

FilterDesktop/MuK_HLT1Selection_for_DetachedMuKPair

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Code            | Hlt1TOS('Hlt1Track\*.\*Decision')                    |
| Inputs          | [ 'Phys/MuK_L0TOSSelection_for_DetachedMuKPair' ]  |
| DecayDescriptor | None                                                 |
| Output          | Phys/MuK_HLT1Selection_for_DetachedMuKPair/Particles |

FilterDesktop/MuK_HLT2Selection_for_DetachedMuKPair

|                 |                                                      |
|-----------------|------------------------------------------------------|
| Code            | Hlt2TOS('Hlt2Topo(Mu)?2BodyBBDTDecision')            |
| Inputs          | [ 'Phys/MuK_HLT1Selection_for_DetachedMuKPair' ]   |
| DecayDescriptor | None                                                 |
| Output          | Phys/MuK_HLT2Selection_for_DetachedMuKPair/Particles |

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

CombineParticles/SelMuMuK_for_DetachedMuMuKPair

|                  |                                                                                                                                                                                  |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ForElectronRecoEffSelVeloPartsVeloMuons' , 'Phys/MuK_HLT2Selection_for_DetachedMuKPair' ]                                                                              |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                                                                             |
| CombinationCut   | (AM \< 6000.0)                                                                                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 20) & (log(B_MASS_CONSTRAINT_IP) \< -2.75) & in_range(5000.0, BMassFromConstraint, 5700.0) & in_range(750.0,Probe_Momentum_From_Mass_constraint,150000.0) |
| DecayDescriptor  | None                                                                                                                                                                             |
| DecayDescriptors | [ 'B+ -\> J/psi(1S) mu+' , 'B- -\> J/psi(1S) mu-' ]                                                                                                                            |
| Output           | Phys/SelMuMuK_for_DetachedMuMuKPair/Particles                                                                                                                                    |

FilterDesktop/DetachedMuMuKPairLine

|                 |                                             |
|-----------------|---------------------------------------------|
| Code            | (in_range(3200.0, B_MM_FROM_FD, 7200.0))    |
| Inputs          | [ 'Phys/SelMuMuK_for_DetachedMuMuKPair' ] |
| DecayDescriptor | None                                        |
| Output          | Phys/DetachedMuMuKPairLine/Particles        |
