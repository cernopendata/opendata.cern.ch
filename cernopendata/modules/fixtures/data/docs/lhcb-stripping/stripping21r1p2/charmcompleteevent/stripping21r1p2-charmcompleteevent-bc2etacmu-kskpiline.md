[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingBc2EtacMu_KsKpiLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/Bc2EtacMu_KsKpiLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 1.0000000                          |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharmCompleteEvent

|      |                                                                                                                      |
|------|----------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamCharmCompleteEventBadEvent') |

LoKi::VoidFilter/StrippingBc2EtacMu_KsKpiLineVOIDFilter

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 450.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:Bc2EtacMuInputKs

GaudiSequencer/MERGEDINPUTS:Bc2EtacMuInputKs

GaudiSequencer/INPUT:Phys/StdLooseKsDD

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:Phys/StdVeryLooseKsLL

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/Bc2EtacMuInputKs

|                 |                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' , 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                                                                                        |
| Output          | Phys/Bc2EtacMuInputKs/Particles                                                                                                                             |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Bc2EtacMuSelKs

|                 |                                                                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.\*MeV) & (BPVDLS\>5) & (PT \> 500\*MeV) & (MAXTREE('pi-'==ABSID, PROBNNpi) \> 0.1) & (MAXTREE('pi-'==ABSID, TRGHOSTPROB) \< 0.4) & (MAXTREE('pi-'==ABSID, TRCHI2DOF) \< 5) |
| Inputs          | [ 'Phys/Bc2EtacMuInputKs' ]                                                                                                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                            |
| Output          | Phys/Bc2EtacMuSelKs/Particles                                                                                                                                                                   |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/Bc2EtacMuSelKaons

|                 |                                                                                                         |
|-----------------|---------------------------------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.1) & (PT \> 500\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF \< 5) & (MIPCHI2DV(PRIMARY) \> 4) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ]                           |
| DecayDescriptor | None                                                                                                    |
| Output          | Phys/Bc2EtacMuSelKaons/Particles                                                                        |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Bc2EtacMuSelPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.1) & (PT \> 500\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF \< 5)          |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Bc2EtacMuSelPions/Particles                                                      |

CombineParticles/Bc2EtacMuSelEtac2KsKPi

|                  |                                                                                              |
|------------------|----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bc2EtacMuSelKaons' , 'Phys/Bc2EtacMuSelKs' , 'Phys/Bc2EtacMuSelPions' ]            |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | in_range(2.7\*GeV, AM, 3.4\*GeV)                                                             |
| MotherCut        | in_range(2.7\*GeV, MM, 3.4\*GeV) & (VFASPF(VCHI2/VDOF) \< 9.)                                |
| DecayDescriptor  | [eta_c(1S) -\> KS0 K+ pi-]cc                                                               |
| DecayDescriptors | [ '[eta_c(1S) -\> KS0 K+ pi-]cc' ]                                                       |
| Output           | Phys/Bc2EtacMuSelEtac2KsKPi/Particles                                                        |

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

FilterDesktop/Bc2EtacMuSelMuons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNmu \> 0.1) & (PT \> 500\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF \< 5)  |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p2-commonparticles-stdloosemuons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Bc2EtacMuSelMuons/Particles                                              |

CombineParticles/Bc2EtacMu_KsKpiLine

|                  |                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bc2EtacMuSelEtac2KsKPi' , 'Phys/Bc2EtacMuSelMuons' ]                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'eta_c(1S)' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                  |
| CombinationCut   | in_range(3.2\*GeV, AM, 6.8\*GeV)                                                                                      |
| MotherCut        | in_range(3.2\*GeV, MM, 6.8\*GeV) & in_range(3.2\*GeV, BPVCORRM, 6.8\*GeV) & (VFASPF(VCHI2/VDOF) \< 9.) & (PT \> 2500) |
| DecayDescriptor  | B_c+ -\> eta_c(1S) mu+                                                                                                |
| DecayDescriptors | [ 'B_c+ -\> eta_c(1S) mu+' ]                                                                                        |
| Output           | Phys/Bc2EtacMu_KsKpiLine/Particles                                                                                    |
