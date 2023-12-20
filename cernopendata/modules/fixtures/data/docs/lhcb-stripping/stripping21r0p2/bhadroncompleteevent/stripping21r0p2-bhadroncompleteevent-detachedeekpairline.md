[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingDetachedEEKPairLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/DetachedEEKPairLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

LoKi::VoidFilter/StrippingDetachedEEKPairLineVOIDFilter

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

CombineParticles/SelKE_for_DetachedEKPair

|                  |                                                                                               |
|------------------|-----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DetachedElectrons_For_ElectronRecoEff' , 'Phys/DetachedKaons_For_ElectronRecoEff' ] |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                    |
| CombinationCut   | (AM \< 5500.0)                                                                                |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 10) & (BPVVDCHI2 \> 36 ) & (VFASPF(VMINVDDV(PRIMARY)) \> 2.0 )         |
| DecayDescriptor  | None                                                                                          |
| DecayDescriptors | [ '[J/psi(1S) -\> e+ K-]cc' , '[J/psi(1S) -\> e+ K+]cc' ]                               |
| Output           | Phys/SelKE_for_DetachedEKPair/Particles                                                       |

FilterDesktop/EK_L0Decision_for_DetachedEKPair

|                 |                                                 |
|-----------------|-------------------------------------------------|
| Code            | L0TOS('L0ElectronDecision')                     |
| Inputs          | [ 'Phys/SelKE_for_DetachedEKPair' ]           |
| DecayDescriptor | None                                            |
| Output          | Phys/EK_L0Decision_for_DetachedEKPair/Particles |

FilterDesktop/EK_HLT1Selection_for_DetachedEKPair

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Code            | Hlt1TOS('Hlt1TrackAllL0.\*Decision')               |
| Inputs          | [ 'Phys/EK_L0Decision_for_DetachedEKPair' ]      |
| DecayDescriptor | None                                               |
| Output          | Phys/EK_HLT1Selection_for_DetachedEKPair/Particles |

FilterDesktop/EK_HLT2Selection_for_DetachedEKPair

|                 |                                                    |
|-----------------|----------------------------------------------------|
| Code            | Hlt2TOS('Hlt2Topo(E)?2BodyBBDTDecision')           |
| Inputs          | [ 'Phys/EK_HLT1Selection_for_DetachedEKPair' ]   |
| DecayDescriptor | None                                               |
| Output          | Phys/EK_HLT2Selection_for_DetachedEKPair/Particles |

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

CombineParticles/DetachedEEKPairLine

|                  |                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/EK_HLT2Selection_for_DetachedEKPair' , 'Phys/ForElectronRecoEffSelVeloPartsVeloElectrons' ]                                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'J/psi(1S)' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' }                                                                                                                  |
| CombinationCut   | (AM \< 6000.0)                                                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 22) & (log(B_MASS_CONSTRAINT_IP) \< -2.5) & (in_range(5000.0, BMassFromConstraint, 5700.0)) & (in_range(750.0,Probe_Momentum_From_Mass_constraint,150000.0)) |
| DecayDescriptor  | None                                                                                                                                                                                |
| DecayDescriptors | [ 'B+ -\> J/psi(1S) e+' , 'B- -\> J/psi(1S) e-' ]                                                                                                                                 |
| Output           | Phys/DetachedEEKPairLine/Particles                                                                                                                                                  |
