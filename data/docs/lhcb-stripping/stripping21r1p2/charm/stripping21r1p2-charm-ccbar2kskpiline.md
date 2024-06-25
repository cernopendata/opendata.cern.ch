[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingCcbar2KsKpiLine

## Properties:

|                |                                |
|----------------|--------------------------------|
| OutputLocation | Phys/Ccbar2KsKpiLine/Particles |
| Postscale      | 1.0000000                      |
| HLT1           | None                           |
| HLT2           | None                           |
| Prescale       | 1.0000000                      |
| L0DU           | None                           |
| ODIN           | None                           |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionCharm

|      |                                                                                            |
|------|--------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamCharmBadEvent') & ~ALG_PASSED('StrippingStreamCharmBadEvent') |

LoKi::VoidFilter/StrippingCcbar2KsKpiLineVOIDFilter

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 450.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/MERGED:Ccbar2KsKpiInputKs

GaudiSequencer/MERGEDINPUTS:Ccbar2KsKpiInputKs

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

FilterDesktop/Ccbar2KsKpiInputKs

|                 |                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' , 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ] |
| DecayDescriptor | None                                                                                                                                                        |
| Output          | Phys/Ccbar2KsKpiInputKs/Particles                                                                                                                           |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

FilterDesktop/Ccbar2KsKpiSelKs

|                 |                                                                                                                                                                                                                                                     |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (ADMASS('KS0') \< 30.\*MeV) & (BPVDLS\>5) & (PT \> 1500\*MeV) & (MAXTREE('pi-'==ABSID, PROBNNpi) \> 0.2) & (MAXTREE('pi-'==ABSID, TRGHOSTPROB) \< 0.4) & (MAXTREE('pi-'==ABSID, TRCHI2DOF) \< 5) & (MAXTREE('pi-'==ABSID, MIPCHI2DV(PRIMARY)) \> 4) |
| Inputs          | [ 'Phys/Ccbar2KsKpiInputKs' ]                                                                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                                |
| Output          | Phys/Ccbar2KsKpiSelKs/Particles                                                                                                                                                                                                                     |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/Ccbar2KsKpiSelKaons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNk \> 0.2) & (PT \> 1500\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF \< 5)  |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Ccbar2KsKpiSelKaons/Particles                                            |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

FilterDesktop/Ccbar2KsKpiSelPions

|                 |                                                                                       |
|-----------------|---------------------------------------------------------------------------------------|
| Code            | (PROBNNpi \> 0.2) & (PT \> 1500\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF \< 5)         |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1p2-commonparticles-stdallnopidspions)' ] |
| DecayDescriptor | None                                                                                  |
| Output          | Phys/Ccbar2KsKpiSelPions/Particles                                                    |

CombineParticles/Ccbar2KsKpiLine

|                  |                                                                                              |
|------------------|----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Ccbar2KsKpiSelKaons' , 'Phys/Ccbar2KsKpiSelKs' , 'Phys/Ccbar2KsKpiSelPions' ]      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' } |
| CombinationCut   | in_range(2.7\*GeV, AM, 4.4\*GeV)                                                             |
| MotherCut        | in_range(2.7\*GeV, MM, 4.4\*GeV) & (VFASPF(VCHI2/VDOF) \< 9.)                                |
| DecayDescriptor  | [eta_c(1S) -\> KS0 K+ pi-]cc                                                               |
| DecayDescriptors | [ '[eta_c(1S) -\> KS0 K+ pi-]cc' ]                                                       |
| Output           | Phys/Ccbar2KsKpiLine/Particles                                                               |
