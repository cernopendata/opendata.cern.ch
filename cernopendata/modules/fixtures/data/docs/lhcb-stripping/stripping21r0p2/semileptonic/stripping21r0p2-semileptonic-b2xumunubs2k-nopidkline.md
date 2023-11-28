[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2XuMuNuBs2K_NoPIDKLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2XuMuNuBs2K_NoPIDKLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 0.020000000                            |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuMuNuBs2K_NoPIDKLineVOIDFilter

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
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r0p2-commonparticles-stdloosemuons)' ]                                                      |
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

FilterDesktop/KNoPID_forB2XuMuNu

|                 |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 )& (P\> 10000.0 \*MeV) & (PT\> 1000.0 \*MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 49 ) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r0p2-commonparticles-stdloosekaons)' ]                                     |
| DecayDescriptor | None                                                                                                              |
| Output          | Phys/KNoPID_forB2XuMuNu/Particles                                                                                 |

CombineParticles/KMu_NoPIDK_forB2XuMuNu

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KNoPID_forB2XuMuNu' , 'Phys/MuL0TOS_forB2XuMuNuTOS' ]                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }                                                  |
| CombinationCut   | (AM\>1200.0\*MeV) & (AM\<5500.0\*MeV)                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.994)& (BPVVDCHI2 \>120.0) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ '[B_s~0 -\> K+ mu-]cc' ]                                                                                                |
| Output           | Phys/KMu_NoPIDK_forB2XuMuNu/Particles                                                                                         |

TisTosParticleTagger/B2XuMuNuBs2K_NoPIDKLine

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/KMu_NoPIDK_forB2XuMuNu' ]                                                  |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/B2XuMuNuBs2K_NoPIDKLine/Particles                                               |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 } |
