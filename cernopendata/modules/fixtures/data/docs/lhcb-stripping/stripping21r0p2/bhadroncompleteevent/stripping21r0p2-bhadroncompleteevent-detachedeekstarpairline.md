[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingDetachedEEKstarPairLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/DetachedEEKstarPairLine/Particles |
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

LoKi::VoidFilter/StrippingDetachedEEKstarPairLineVOIDFilter

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

LoKi::L0Filter/EKstar_L0Selection_for_DetachedEKstarPair

|      |                           |
|------|---------------------------|
| Code | L0_CHANNEL_RE('Electron') |

CombineParticles/SelEKstar_for_DetachedEKstarPair

|                  |                                                                                                |
|------------------|------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedElectrons_For_ElectronRecoEff' , 'Phys/DetachedKstars_For_ElectronRecoEff' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)0' : 'ALL' , 'K\*(892)~0' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }      |
| CombinationCut   | (AM \< 5500.0)                                                                                 |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10) & (BPVVDCHI2 \> 36) & (VFASPF(VMINVDDV(PRIMARY)) \> 2.0 )           |
| DecayDescriptor  | None                                                                                           |
| DecayDescriptors | [ '[J/psi(1S) -\> e+ K\*(892)0]cc' , '[J/psi(1S) -\> e- K\*(892)0]cc' ]                  |
| Output           | Phys/SelEKstar_for_DetachedEKstarPair/Particles                                                |

FilterDesktop/EKstar_HLT1Selection_for_DetachedEKstarPair

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Code            | Hlt1TOS('Hlt1TrackAllL0.\*Decision')                       |
| Inputs          | [ 'Phys/SelEKstar_for_DetachedEKstarPair' ]              |
| DecayDescriptor | None                                                       |
| Output          | Phys/EKstar_HLT1Selection_for_DetachedEKstarPair/Particles |

FilterDesktop/EKstar_HLT2Selection_for_DetachedEKstarPair

|                 |                                                            |
|-----------------|------------------------------------------------------------|
| Code            | Hlt2TOS('Hlt2Topo(E)?(2\|3)BodyBBDTDecision')              |
| Inputs          | [ 'Phys/EKstar_HLT1Selection_for_DetachedEKstarPair' ]   |
| DecayDescriptor | None                                                       |
| Output          | Phys/EKstar_HLT2Selection_for_DetachedEKstarPair/Particles |

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

CombineParticles/DetachedEEKstarPairLine

|                  |                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/EKstar_HLT2Selection_for_DetachedEKstarPair' , 'Phys/ForElectronRecoEffSelVeloPartsVeloElectrons' ]                                                                       |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                                                                                                                  |
| CombinationCut   | (AM \< 6000.0)                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 22) & (log(B_MASS_CONSTRAINT_IP) \< -2.0) & (in_range(5000.0, BMassFromConstraint, 5700.0)) & (in_range(750.0,Probe_Momentum_From_Mass_constraint,150000.0)) |
| DecayDescriptor  | None                                                                                                                                                                                |
| DecayDescriptors | [ 'B+ -\> J/psi(1S) e+' , 'B- -\> J/psi(1S) e-' ]                                                                                                                                 |
| Output           | Phys/DetachedEEKstarPairLine/Particles                                                                                                                                              |
