[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBc2EtacMu_PpbarLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/Bc2EtacMu_PpbarLine/Particles |
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

LoKi::VoidFilter/StrippingBc2EtacMu_PpbarLineVOIDFilter

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Code | ( recSummary(LHCb.RecSummary.nSPDhits,'Raw/Spd/Digits') \< 450.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseProtons

|      |                                   |
|------|-----------------------------------|
| Code | 0StdLooseProtons/Particles',True) |

FilterDesktop/Bc2EtacMuSelProtons

|                 |                                                                                   |
|-----------------|-----------------------------------------------------------------------------------|
| Code            | (PROBNNp \> 0.1) & (PT \> 400\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF \< 5)       |
| Inputs          | [ 'Phys/[StdLooseProtons](./stripping21r0p2-commonparticles-stdlooseprotons)' ] |
| DecayDescriptor | None                                                                              |
| Output          | Phys/Bc2EtacMuSelProtons/Particles                                                |

CombineParticles/Bc2EtacMuSelEtac2Ppbar

|                  |                                                               |
|------------------|---------------------------------------------------------------|
| Inputs           | [ 'Phys/Bc2EtacMuSelProtons' ]                              |
| DaughtersCuts    | { '' : 'ALL' , 'p+' : 'ALL' , 'p~-' : 'ALL' }                 |
| CombinationCut   | in_range(2.7\*GeV, AM, 3.4\*GeV)                              |
| MotherCut        | in_range(2.7\*GeV, MM, 3.4\*GeV) & (VFASPF(VCHI2/VDOF) \< 9.) |
| DecayDescriptor  | [eta_c(1S) -\> p+ p~-]cc                                    |
| DecayDescriptors | [ '[eta_c(1S) -\> p+ p~-]cc' ]                            |
| Output           | Phys/Bc2EtacMuSelEtac2Ppbar/Particles                         |

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

FilterDesktop/Bc2EtacMuSelMuons

|                 |                                                                               |
|-----------------|-------------------------------------------------------------------------------|
| Code            | (PROBNNmu \> 0.1) & (PT \> 500\*MeV) & (TRGHOSTPROB\<0.4) & (TRCHI2DOF \< 5)  |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p2-commonparticles-stdloosemuons)' ] |
| DecayDescriptor | None                                                                          |
| Output          | Phys/Bc2EtacMuSelMuons/Particles                                              |

CombineParticles/Bc2EtacMu_PpbarLine

|                  |                                                                                                                       |
|------------------|-----------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Bc2EtacMuSelEtac2Ppbar' , 'Phys/Bc2EtacMuSelMuons' ]                                                        |
| DaughtersCuts    | { '' : 'ALL' , 'eta_c(1S)' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                  |
| CombinationCut   | in_range(3.2\*GeV, AM, 6.8\*GeV)                                                                                      |
| MotherCut        | in_range(3.2\*GeV, MM, 6.8\*GeV) & in_range(3.2\*GeV, BPVCORRM, 6.8\*GeV) & (VFASPF(VCHI2/VDOF) \< 9.) & (PT \> 2500) |
| DecayDescriptor  | B_c+ -\> eta_c(1S) mu+                                                                                                |
| DecayDescriptors | [ 'B_c+ -\> eta_c(1S) mu+' ]                                                                                        |
| Output           | Phys/Bc2EtacMu_PpbarLine/Particles                                                                                    |
