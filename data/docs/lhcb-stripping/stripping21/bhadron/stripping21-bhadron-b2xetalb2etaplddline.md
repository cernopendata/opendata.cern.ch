[[stripping21 lines]](./stripping21-index)

# StrippingB2XEtaLb2etapLDDLine

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/B2XEtaLb2etapLDDLine/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

LoKi::VoidFilter/StrippingB2XEtaLb2etapLDDLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaDD_Particles

|      |                                                                                                  |
|------|--------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)/Particles')\>0 |

FilterDesktop/LambdaforB2XEtaLb2etapLDD

|                 |                                                                                                                                                                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1000.0\*MeV)&(ADMASS('Lambda0')\<20.0\*MeV)&(VFASPF(VCHI2/VDOF)\<15.0)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(CHILDCUT((PT\>300.0\*MeV),1))&(CHILDCUT((PT\>300.0\*MeV),2))&(CHILDCUT((TRGHOSTPROB\<0.5),1))&(CHILDCUT((TRGHOSTPROB\<0.5),2)) |
| Inputs          | [ 'Phys/[StdLooseLambdaDD](./stripping21-commonparticles-stdlooselambdadd)' ]                                                                                                                                                                                           |
| DecayDescriptor | None                                                                                                                                                                                                                                                                      |
| Output          | Phys/LambdaforB2XEtaLb2etapLDD/Particles                                                                                                                                                                                                                                  |

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

CombineParticles/B2XEtaLb2etapLDDLine

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/EtapforB2XEta' , 'Phys/LambdaforB2XEtaLb2etapLDD' ]                      |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'eta_prime' : 'ALL' }      |
| CombinationCut   | (ADAMASS('Lambda_b0')\<750.0\*MeV)&(ACUTDOCACHI2(15.0,''))                         |
| MotherCut        | (PT\>1000.0\*MeV)&(VFASPF(VCHI2/VDOF)\<15.0)&(BPVDIRA\>0.9995)&(BPVIPCHI2()\<20.0) |
| DecayDescriptor  | [Lambda_b0 -\> Lambda0 eta_prime]cc                                              |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda0 eta_prime]cc' ]                                      |
| Output           | Phys/B2XEtaLb2etapLDDLine/Particles                                                |
