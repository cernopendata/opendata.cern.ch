[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingDetachedEEPhiPairLine

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/DetachedEEPhiPairLine/Particles |
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

LoKi::VoidFilter/StrippingDetachedEEPhiPairLineVOIDFilter

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

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsElectrons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdNoPIDsElectrons/Particles',True) |

FilterDesktop/DetachedElectrons_For_ElectronRecoEff

|                 |                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------|
| Code            | (MIPCHI2DV(PRIMARY)\>12) & (PT\> 1200.0) & (TRCHI2DOF\<5) & in_range(1.8, ETA, 5.1) & (PROBNNe \> 0.2) |
| Inputs          | [ 'Phys/[StdNoPIDsElectrons](./stripping21r0p2-commonparticles-stdnopidselectrons)' ]                |
| DecayDescriptor | None                                                                                                   |
| Output          | Phys/DetachedElectrons_For_ElectronRecoEff/Particles                                                   |

LoKi::L0Filter/EPhi_L0Selection_for_DetachedEPhiPair

|      |                                         |
|------|-----------------------------------------|
| Code | L0_CHANNEL_RE('Muon\|Electron\|Hadron') |

CombineParticles/SelEPhi_for_DetachedEPhiPair

|                  |                                                                                              |
|------------------|----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedElectrons_For_ElectronRecoEff' , 'Phys/DetachedPhis_For_ElectronRecoEff' ] |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'phi(1020)' : 'ALL' }                           |
| CombinationCut   | (AM \< 5500.0)                                                                               |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10) & (BPVVDCHI2 \> 36) & (VFASPF(VMINVDDV(PRIMARY)) \> 2.0 )         |
| DecayDescriptor  | None                                                                                         |
| DecayDescriptors | [ '[J/psi(1S) -\> e+ phi(1020)]cc' , '[J/psi(1S) -\> e- phi(1020)]cc' ]                |
| Output           | Phys/SelEPhi_for_DetachedEPhiPair/Particles                                                  |

FilterDesktop/EPhi_HLT1Selection_for_DetachedEPhiPair

|                 |                                                        |
|-----------------|--------------------------------------------------------|
| Code            | Hlt1TOS('Hlt1TrackAllL0.\*Decision')                   |
| Inputs          | [ 'Phys/SelEPhi_for_DetachedEPhiPair' ]              |
| DecayDescriptor | None                                                   |
| Output          | Phys/EPhi_HLT1Selection_for_DetachedEPhiPair/Particles |

FilterDesktop/EPhi_HLT2Selection_for_DetachedEPhiPair

|                 |                                                                     |
|-----------------|---------------------------------------------------------------------|
| Code            | Hlt2TOS('(Hlt2Topo(E)?(2\|3)BodyBBDTDecision\|Hlt2IncPhiDecision)') |
| Inputs          | [ 'Phys/EPhi_HLT1Selection_for_DetachedEPhiPair' ]                |
| DecayDescriptor | None                                                                |
| Output          | Phys/EPhi_HLT2Selection_for_DetachedEPhiPair/Particles              |

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

NoPIDsParticleMaker/ForElectronRecoEffSelAllVeloPartsVeloElectrons

|                 |                                                               |
|-----------------|---------------------------------------------------------------|
| Inputs          | [ 'Rec/ProtoP/VeloProtosForElectronRecoEff' ]               |
| DecayDescriptor | electrons                                                     |
| Output          | Phys/ForElectronRecoEffSelAllVeloPartsVeloElectrons/Particles |

FilterDesktop/ForElectronRecoEffSelVeloPartsVeloElectrons

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | (MIPDV(PRIMARY) \> 0.04) & (TRCHI2DOF\<5.0) & in_range(1.9, ETA, 5.1) |
| Inputs          | [ 'Phys/ForElectronRecoEffSelAllVeloPartsVeloElectrons' ]           |
| DecayDescriptor | None                                                                  |
| Output          | Phys/ForElectronRecoEffSelVeloPartsVeloElectrons/Particles            |

CombineParticles/DetachedEEPhiPairLine

|                  |                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/EPhi_HLT2Selection_for_DetachedEPhiPair' , 'Phys/ForElectronRecoEffSelVeloPartsVeloElectrons' ]                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                                                                                                                  |
| CombinationCut   | (AM \< 6000.0)                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 22) & (log(B_MASS_CONSTRAINT_IP) \< -2.0) & (in_range(5000.0, BMassFromConstraint, 5700.0)) & (in_range(750.0,Probe_Momentum_From_Mass_constraint,150000.0)) |
| DecayDescriptor  | None                                                                                                                                                                                |
| DecayDescriptors | [ 'B+ -\> J/psi(1S) e+' , 'B- -\> J/psi(1S) e-' ]                                                                                                                                 |
| Output           | Phys/DetachedEEPhiPairLine/Particles                                                                                                                                                |
