[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2XuMuNuB2Phi_Line

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/B2XuMuNuB2Phi_Line/Particles |
| Postscale      | 1.0000000                         |
| HLT1           | None                              |
| HLT2           | None                              |
| Prescale       | 1.0000000                         |
| L0DU           | None                              |
| ODIN           | None                              |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuMuNuB2Phi_LineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseMuons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseMuons/Particles',True) |

FilterDesktop/MuL0TOS_forB2XuMuNu

|                 |                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 6000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (PIDmu \> 3.0 )& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p2-commonparticles-stdloosemuons)' ]                                                      |
| DecayDescriptor | None                                                                                                                               |
| Output          | Phys/MuL0TOS_forB2XuMuNu/Particles                                                                                                 |

TisTosParticleTagger/MuL0TOS_forB2XuMuNuTOS

|                 |                                       |
|-----------------|---------------------------------------|
| Inputs          | [ 'Phys/MuL0TOS_forB2XuMuNu' ]      |
| DecayDescriptor | None                                  |
| Output          | Phys/MuL0TOS_forB2XuMuNuTOS/Particles |
| TisTosSpecs     | { 'L0.\*Muon.\*Decision%TOS' : 0 }    |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/K_PhiB2XuMuNu

|                 |                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 )& (P\> 3000.0 \*MeV) & (PT\> 400.0 \*MeV)& (TRGHOSTPROB \< 0.5)& (PIDK\> 2.0 ) & (PIDmu \< 2 ) & (MIPCHI2DV(PRIMARY)\> 49 ) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ]                                                                  |
| DecayDescriptor | None                                                                                                                                           |
| Output          | Phys/K_PhiB2XuMuNu/Particles                                                                                                                   |

CombineParticles/PhiKK_forB2XuMuNu

|                  |                                                                                                |
|------------------|------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K_PhiB2XuMuNu' ]                                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                   |
| CombinationCut   | (AM\< 2200.0)                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6 ) & (PT \> 600.0 \*MeV) & (MIPCHI2DV(PRIMARY)\> 9 ) & (BPVDIRA\> 0.9) |
| DecayDescriptor  | None                                                                                           |
| DecayDescriptors | [ 'phi(1020) -\> K- K+' ]                                                                    |
| Output           | Phys/PhiKK_forB2XuMuNu/Particles                                                               |

CombineParticles/PhiMu_forB2XuMuNu

|                  |                                                                                              |
|------------------|----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuL0TOS_forB2XuMuNuTOS' , 'Phys/PhiKK_forB2XuMuNu' ]                               |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'phi(1020)' : 'ALL' }                         |
| CombinationCut   | (AM\<5500.0\*MeV)                                                                            |
| MotherCut        | (BPVCORRM\>2500.0\*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.994)& (BPVVDCHI2 \>50.0) |
| DecayDescriptor  | None                                                                                         |
| DecayDescriptors | [ '[B+ -\> phi(1020) mu+]cc' ]                                                           |
| Output           | Phys/PhiMu_forB2XuMuNu/Particles                                                             |

TisTosParticleTagger/B2XuMuNuB2Phi_Line

|                 |                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/PhiMu_forB2XuMuNu' ]                                                                                                 |
| DecayDescriptor | None                                                                                                                           |
| Output          | Phys/B2XuMuNuB2Phi_Line/Particles                                                                                              |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu3Body.\*Decision%TOS' : 0 } |
