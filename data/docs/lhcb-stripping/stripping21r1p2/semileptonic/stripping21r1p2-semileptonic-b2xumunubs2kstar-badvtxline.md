[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2XuMuNuBs2Kstar_BadVtxLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/B2XuMuNuBs2Kstar_BadVtxLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 0.020000000                                |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuMuNuBs2Kstar_BadVtxLineVOIDFilter

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

FilterDesktop/Mu_forB2XuMuNu

|                 |                                                                                                                                    |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 3000.0 \*MeV) & (PT\> 1000.0\* MeV)& (TRGHOSTPROB \< 0.35)& (PIDmu \> 3.0 )& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdLooseMuons](./stripping21r1p2-commonparticles-stdloosemuons)' ]                                                      |
| DecayDescriptor | None                                                                                                                               |
| Output          | Phys/Mu_forB2XuMuNu/Particles                                                                                                      |

LoKi::VoidFilter/SELECT:Phys/StdLoosePions

|      |                                 |
|------|---------------------------------|
| Code | 0StdLoosePions/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseKsLD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsLD/Particles',True) |

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/KS02PiPi_forB2XuMuNu

|                 |                                                                                                                                                                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (BPVVD \>20.0\*mm) & (MM\>456.0\*MeV) & (MM\<536.0\*MeV) & (BPVVDCHI2\> 0.0 ) & (PT \> 250.0\*MeV) & (VFASPF(VCHI2PDOF) \< 4.0) & CHILDCUT((TRCHI2DOF \< 4.0),1) & CHILDCUT((TRCHI2DOF \< 4.0),2) & CHILDCUT((MIPCHI2DV(PRIMARY) \> 50.0),1) & CHILDCUT((MIPCHI2DV(PRIMARY) \> 50.0),2) & (MIPCHI2DV(PRIMARY) \> 0.0) |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r1p2-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLD](./stripping21r1p2-commonparticles-stdlooseksld)' , 'Phys/[StdVeryLooseKsLL](./stripping21r1p2-commonparticles-stdverylooseksll)' ]                                                                                   |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                  |
| Output          | Phys/KS02PiPi_forB2XuMuNu/Particles                                                                                                                                                                                                                                                                                   |

CombineParticles/Kstar_forB2XuMuNu

|                  |                                                                                                                                                                                                                                                                  |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KS02PiPi_forB2XuMuNu' , 'Phys/[StdLoosePions](./stripping21r1p2-commonparticles-stdloosepions)' ]                                                                                                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'pi+' : '(PT\> 250.0\*MeV) &(P\> 3000.0\*MeV)& (TRCHI2DOF \< 4.0 )& (MIPCHI2DV(PRIMARY)\>25.0)& (PIDK \< 2.0)' , 'pi-' : '(PT\> 250.0\*MeV) &(P\> 3000.0\*MeV)& (TRCHI2DOF \< 4.0 )& (MIPCHI2DV(PRIMARY)\>25.0)& (PIDK \< 2.0)' } |
| CombinationCut   | (ADAMASS('K\*(892)+')\< 1200 )                                                                                                                                                                                                                                   |
| MotherCut        | (PT \> 800)                                                                                                                                                                                                                                                      |
| DecayDescriptor  | None                                                                                                                                                                                                                                                             |
| DecayDescriptors | [ '[K\*(892)+ -\> KS0 pi+]cc' ]                                                                                                                                                                                                                              |
| Output           | Phys/Kstar_forB2XuMuNu/Particles                                                                                                                                                                                                                                 |

CombineParticles/KstarMuBadVtx_forB2XuMuNu

|                  |                                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Kstar_forB2XuMuNu' , 'Phys/Mu_forB2XuMuNu' ]                                                  |
| DaughtersCuts    | { '' : 'ALL' , 'K\*(892)+' : 'ALL' , 'K\*(892)-' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' }              |
| CombinationCut   | ATRUE                                                                                                   |
| MotherCut        | (VFASPF(VCHI2/VDOF)\> 6.0) & (BPVDIRA\> 0.99) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                    |
| DecayDescriptors | [ '[B_s~0 -\> K\*(892)+ mu-]cc' ]                                                                   |
| Output           | Phys/KstarMuBadVtx_forB2XuMuNu/Particles                                                                |

TisTosParticleTagger/B2XuMuNuBs2Kstar_BadVtxLine

|                 |                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/KstarMuBadVtx_forB2XuMuNu' ]                                                                                         |
| DecayDescriptor | None                                                                                                                           |
| Output          | Phys/B2XuMuNuBs2Kstar_BadVtxLine/Particles                                                                                     |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu3Body.\*Decision%TOS' : 0 } |
