[[stripping21 lines]](./stripping21-index)

# StrippingB2XEtaB2etapKSLLLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/B2XEtaB2etapKSLLLine/Particles     |
| Postscale      | 1.0000000                               |
| HLT            | (HLT_PASS_RE('Hlt1TrackAllL0Decision')) |
| Prescale       | 1.0000000                               |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingB2XEtaB2etapKSLLLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/KSforB2XEtaB2etapKSLL

|                 |                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1200.0\*MeV)&(ADMASS('KS0')\<14.0\*MeV)&(VFASPF(VCHI2/VDOF)\<15.0)&(BPVVDCHI2\>50.0)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(CHILDCUT((PT\>300.0\*MeV),1))&(CHILDCUT((PT\>300.0\*MeV),2))&(CHILDCUT((TRGHOSTPROB\<0.5),1))&(CHILDCUT((TRGHOSTPROB\<0.5),2))&(CHILDCUT((PROBNNpi\>0.1),1))&(CHILDCUT((PROBNNpi\>0.1),2)) |
| Inputs          | [ 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ]                                                                                                                                                                                                                                                                             |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/KSforB2XEtaB2etapKSLL/Particles                                                                                                                                                                                                                                                                                                                |

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

CombineParticles/B2XEtaB2etapKSLLLine

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/EtapforB2XEta' , 'Phys/KSforB2XEtaB2etapKSLL' ]                          |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'eta_prime' : 'ALL' }                               |
| CombinationCut   | (ADAMASS('B0')\<750.0\*MeV)&(ACUTDOCACHI2(15.0,''))                                |
| MotherCut        | (PT\>1500.0\*MeV)&(VFASPF(VCHI2/VDOF)\<15.0)&(BPVDIRA\>0.9995)&(BPVIPCHI2()\<20.0) |
| DecayDescriptor  | B0 -\> KS0 eta_prime                                                               |
| DecayDescriptors | [ 'B0 -\> KS0 eta_prime' ]                                                       |
| Output           | Phys/B2XEtaB2etapKSLLLine/Particles                                                |
