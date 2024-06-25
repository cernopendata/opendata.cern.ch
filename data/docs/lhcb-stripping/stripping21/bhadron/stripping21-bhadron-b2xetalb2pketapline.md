[[stripping21 lines]](./stripping21-index)

# StrippingB2XEtaLb2pKetapLine

## Properties:

|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| OutputLocation | Phys/B2XEtaLb2pKetapLine/Particles                                                      |
| Postscale      | 1.0000000                                                                               |
| HLT            | (HLT_PASS_RE('Hlt1TrackAllL0Decision') & HLT_PASS_RE('Hlt2Topo[234]Body.\*Decision')) |
| Prescale       | 1.0000000                                                                               |
| L0DU           | None                                                                                    |
| ODIN           | None                                                                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingB2XEtaLb2pKetapLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseProtons_Particles

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)/Particles')\>0 |

FilterDesktop/ProtonsForB2XEtaLb2pKetap

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PT\>500.0\*MeV)&(TRGHOSTPROB\<0.5)&(PROBNNp\>0.1)&(BPVIPCHI2()\>20.0)        |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21-commonparticles-stdlooseprotons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/ProtonsForB2XEtaLb2pKetap/Particles                                      |

LoKi::VoidFilter/SelFilterPhys_StdLooseKaons_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)/Particles')\>0 |

FilterDesktop/KaonsForB2XEtaLb2pKetap

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (PT\>500.0\*MeV)&(TRGHOSTPROB\<0.5)&(PROBNNk\>0.1)&(BPVIPCHI2()\>20.0)    |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                      |
| Output          | Phys/KaonsForB2XEtaLb2pKetap/Particles                                    |

GaudiSequencer/SeqDaughtersForB2XEta

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21-commonparticles-stdlooseallphotons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedEta_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedEta](./stripping21-commonparticles-stdlooseresolvedeta)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

FilterDesktop/DaughtersForB2XEta

|                 |                                                                                                                                                                                                                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                           |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21-commonparticles-stdlooseallphotons)' , 'Phys/[StdLoosePions](./stripping21-commonparticles-stdloosepions)' , 'Phys/[StdLooseResolvedEta](./stripping21-commonparticles-stdlooseresolvedeta)' , 'Phys/[StdLooseResolvedPi0](./stripping21-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                          |
| Output          | Phys/DaughtersForB2XEta/Particles                                                                                                                                                                                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

DaVinci::N3BodyDecays/EtapforB2XEta

|                  |                                                                                                                                                                                                                    |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DaughtersForB2XEta' ]                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'eta' : 'ALL' , 'gamma' : 'ALL' , 'pi+' : '(PT\>300.0\*MeV)&(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.5)&(PROBNNpi\>0.1)' , 'pi-' : '(PT\>300.0\*MeV)&(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.5)&(PROBNNpi\>0.1)' } |
| CombinationCut   | (ADAMASS('eta_prime')\<100.0\*MeV)&(ACUTDOCACHI2(10.0,''))                                                                                                                                                         |
| MotherCut        | (PT\>2000.0\*MeV)&(VFASPF(VCHI2/VDOF)\<10.0)                                                                                                                                                                       |
| DecayDescriptor  | None                                                                                                                                                                                                               |
| DecayDescriptors | [ 'eta_prime -\> pi+ pi- gamma' , 'eta_prime -\> pi+ pi- eta' ]                                                                                                                                                  |
| Output           | Phys/EtapforB2XEta/Particles                                                                                                                                                                                       |

DaVinci::N3BodyDecays/B2XEtaLb2pKetapLine

|                  |                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/EtapforB2XEta' , 'Phys/KaonsForB2XEtaLb2pKetap' , 'Phys/ProtonsForB2XEtaLb2pKetap' ]    |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'eta_prime' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' } |
| CombinationCut   | (ADAMASS('Lambda_b0')\<750.0\*MeV)&(ACUTDOCACHI2(15.0,''))                                        |
| MotherCut        | (PT\>1000.0\*MeV)&(VFASPF(VCHI2/VDOF)\<15.0)&(BPVDIRA\>0.9995)&(BPVIPCHI2()\<20.0)                |
| DecayDescriptor  | [Lambda_b0 -\> p+ K- eta_prime]cc                                                               |
| DecayDescriptors | [ '[Lambda_b0 -\> p+ K- eta_prime]cc' ]                                                       |
| Output           | Phys/B2XEtaLb2pKetapLine/Particles                                                                |
