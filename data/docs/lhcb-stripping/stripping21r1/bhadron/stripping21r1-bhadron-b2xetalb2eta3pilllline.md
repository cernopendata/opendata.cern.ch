[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2XEtaLb2eta3piLLLLine

## Properties:

|                |                                       |
|----------------|---------------------------------------|
| OutputLocation | Phys/B2XEtaLb2eta3piLLLLine/Particles |
| Postscale      | 1.0000000                             |
| HLT            | None                                  |
| Prescale       | 1.0000000                             |
| L0DU           | None                                  |
| ODIN           | None                                  |

## Filter sequence:

LoKi::VoidFilter/StrippingB2XEtaLb2eta3piLLLLineVOIDFilter

|      |                                                               |
|------|---------------------------------------------------------------|
| Code | (recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdLooseLambdaLL_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)/Particles')\>0 |

FilterDesktop/LambdaforB2XEtaLb2etapLLL

|                 |                                                                                                                                                                                                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (PT\>1000.0\*MeV)&(ADMASS('Lambda0')\<15.0\*MeV)&(VFASPF(VCHI2/VDOF)\<15.0)&(CHILDCUT((TRCHI2DOF\<3.0),1))&(CHILDCUT((TRCHI2DOF\<3.0),2))&(CHILDCUT((PT\>300.0\*MeV),1))&(CHILDCUT((PT\>300.0\*MeV),2))&(CHILDCUT((TRGHOSTPROB\<0.5),1))&(CHILDCUT((TRGHOSTPROB\<0.5),2)) |
| Inputs          | [ 'Phys/[StdLooseLambdaLL](./stripping21r1-commonparticles-stdlooselambdall)' ]                                                                                                                                                                                         |
| DecayDescriptor | None                                                                                                                                                                                                                                                                      |
| Output          | Phys/LambdaforB2XEtaLb2etapLLL/Particles                                                                                                                                                                                                                                  |

GaudiSequencer/SeqDaughtersForB2XEta

LoKi::VoidFilter/SelFilterPhys_StdLoosePions_Particles

|      |                                                                                              |
|------|----------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21r1-commonparticles-stdlooseallphotons)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedEta_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedEta](./stripping21r1-commonparticles-stdlooseresolvedeta)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseResolvedPi0_Particles

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)/Particles')\>0 |

FilterDesktop/DaughtersForB2XEta

|                 |                                                                                                                                                                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                                                                                                                                                                                   |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r1-commonparticles-stdlooseallphotons)' , 'Phys/[StdLoosePions](./stripping21r1-commonparticles-stdloosepions)' , 'Phys/[StdLooseResolvedEta](./stripping21r1-commonparticles-stdlooseresolvedeta)' , 'Phys/[StdLooseResolvedPi0](./stripping21r1-commonparticles-stdlooseresolvedpi0)' ] |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                  |
| Output          | Phys/DaughtersForB2XEta/Particles                                                                                                                                                                                                                                                                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

DaVinci::N3BodyDecays/Eta3PiforB2XEta

|                  |                                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DaughtersForB2XEta' ]                                                                                                                                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT\>300.0\*MeV)&(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.5)&(PROBNNpi\>0.1)' , 'pi-' : '(PT\>300.0\*MeV)&(TRCHI2DOF\<3.0)&(TRGHOSTPROB\<0.5)&(PROBNNpi\>0.1)' , 'pi0' : 'ALL' } |
| CombinationCut   | (ADAMASS('eta')\<150\*MeV)&(ACUTDOCACHI2(10.0,''))                                                                                                                                               |
| MotherCut        | (PT\>2000\*MeV)&(VFASPF(VCHI2/VDOF)\<10.0)                                                                                                                                                       |
| DecayDescriptor  | eta -\> pi+ pi- pi0                                                                                                                                                                              |
| DecayDescriptors | [ 'eta -\> pi+ pi- pi0' ]                                                                                                                                                                      |
| Output           | Phys/Eta3PiforB2XEta/Particles                                                                                                                                                                   |

CombineParticles/B2XEtaLb2eta3piLLLLine

|                  |                                                                                    |
|------------------|------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Eta3PiforB2XEta' , 'Phys/LambdaforB2XEtaLb2etapLLL' ]                    |
| DaughtersCuts    | { '' : 'ALL' , 'Lambda0' : 'ALL' , 'Lambda~0' : 'ALL' , 'eta' : 'ALL' }            |
| CombinationCut   | (ADAMASS('Lambda_b0')\<750.0\*MeV)&(ACUTDOCACHI2(15.0,''))                         |
| MotherCut        | (PT\>1000.0\*MeV)&(BPVIPCHI2()\<20.0)&(VFASPF(VCHI2/VDOF)\<15.0)&(BPVDIRA\>0.9995) |
| DecayDescriptor  | [Lambda_b0 -\> Lambda0 eta]cc                                                    |
| DecayDescriptors | [ '[Lambda_b0 -\> Lambda0 eta]cc' ]                                            |
| Output           | Phys/B2XEtaLb2eta3piLLLLine/Particles                                              |
