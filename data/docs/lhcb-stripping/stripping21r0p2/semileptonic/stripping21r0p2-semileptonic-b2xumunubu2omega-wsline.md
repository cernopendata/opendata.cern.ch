[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2XuMuNuBu2Omega_WSLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2XuMuNuBu2Omega_WSLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 0.30000000                             |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuMuNuBu2Omega_WSLineVOIDFilter

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

FilterDesktop/MuTightCuts_forB2XuMuNu

|                 |                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 6000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (PIDmu \> 3.0 )& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p2-commonparticles-stdloosemuons)' ]                                                      |
| DecayDescriptor | None                                                                                                                               |
| Output          | Phys/MuTightCuts_forB2XuMuNu/Particles                                                                                             |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseResolvedPi0

|      |                                       |
|------|---------------------------------------|
| Code | 0StdLooseResolvedPi0/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseMergedPi0

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseMergedPi0/Particles',True) |

DaVinci::N3BodyDecays/Omega2PiPiPi0WS_forB2XuMuNu

|                  |                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p2-commonparticles-stdloosemergedpi0)' , 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' , 'Phys/[StdLooseResolvedPi0](./stripping21r0p2-commonparticles-stdlooseresolvedpi0)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT\> 300 \*MeV)& (MIPCHI2DV(PRIMARY)\> 25 )& (PIDK \< 0 ) & (TRGHOSTPROB \< 0.5)' , 'pi-' : '(PT\> 300 \*MeV)& (MIPCHI2DV(PRIMARY)\> 25 )& (PIDK \< 0 ) & (TRGHOSTPROB \< 0.5)' , 'pi0' : '(PT \> 500 \*MeV)' }              |
| CombinationCut   | (ADAMASS('omega(782)')\< 150)                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6) & (DMASS('omega(782)')\< 150)                                                                                                                                                                                               |
| DecayDescriptor  | [omega(782) -\> pi+ pi+ pi0]cc                                                                                                                                                                                                                      |
| DecayDescriptors | [ '[omega(782) -\> pi+ pi+ pi0]cc' ]                                                                                                                                                                                                              |
| Output           | Phys/Omega2PiPiPi0WS_forB2XuMuNu/Particles                                                                                                                                                                                                            |

CombineParticles/OmegaMuWS_forB2XuMuNu

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuTightCuts_forB2XuMuNu' , 'Phys/Omega2PiPiPi0WS_forB2XuMuNu' ]                                                     |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'omega(782)' : 'ALL' }                                                         |
| CombinationCut   | (AM\>2000.0\*MeV) & (AM\<5500.0\*MeV)                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999)& (BPVVDCHI2 \>120.0) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ '[B+ -\> omega(782) mu+]cc' ]                                                                                           |
| Output           | Phys/OmegaMuWS_forB2XuMuNu/Particles                                                                                          |

TisTosParticleTagger/B2XuMuNuBu2Omega_WSLine

|                 |                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/OmegaMuWS_forB2XuMuNu' ]                                                                                             |
| DecayDescriptor | None                                                                                                                           |
| Output          | Phys/B2XuMuNuBu2Omega_WSLine/Particles                                                                                         |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu3Body.\*Decision%TOS' : 0 } |
