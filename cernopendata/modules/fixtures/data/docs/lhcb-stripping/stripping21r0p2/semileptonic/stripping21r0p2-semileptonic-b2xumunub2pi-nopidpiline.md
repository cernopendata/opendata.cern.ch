[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2XuMuNuB2Pi_NoPIDPiLine

## Properties:

|                |                                         |
|----------------|-----------------------------------------|
| OutputLocation | Phys/B2XuMuNuB2Pi_NoPIDPiLine/Particles |
| Postscale      | 1.0000000                               |
| HLT1           | None                                    |
| HLT2           | None                                    |
| Prescale       | 0.020000000                             |
| L0DU           | None                                    |
| ODIN           | None                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuMuNuB2Pi_NoPIDPiLineVOIDFilter

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

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsPions

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsPions/Particles',True) |

FilterDesktop/PiTightNoPID_forB2XuMuNu

|                 |                                                                                                                  |
|-----------------|------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 )& (P\> 10000.0 \*MeV) & (PT\> 800.0 \*MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 49 ) |
| Inputs          | [ 'Phys/[StdNoPIDsPions](./stripping21r0p2-commonparticles-stdnopidspions)' ]                                  |
| DecayDescriptor | None                                                                                                             |
| Output          | Phys/PiTightNoPID_forB2XuMuNu/Particles                                                                          |

CombineParticles/PiMuNoPIDhad_forB2XuMuNu

|                  |                                                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/MuL0TOS_forB2XuMuNuTOS' , 'Phys/PiTightNoPID_forB2XuMuNu' ]                                                         |
| DaughtersCuts    | { '' : 'ALL' , 'mu+' : 'ALL' , 'mu-' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }                                                |
| CombinationCut   | (AM\>1200.0\*MeV) & (AM\<5500.0\*MeV)                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 4.0) & (BPVDIRA\> 0.999)& (BPVVDCHI2 \>120.0) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                                          |
| DecayDescriptors | [ '[B0 -\> pi+ mu-]cc' ]                                                                                                  |
| Output           | Phys/PiMuNoPIDhad_forB2XuMuNu/Particles                                                                                       |

TisTosParticleTagger/B2XuMuNuB2Pi_NoPIDPiLine

|                 |                                                                                      |
|-----------------|--------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/PiMuNoPIDhad_forB2XuMuNu' ]                                                |
| DecayDescriptor | None                                                                                 |
| Output          | Phys/B2XuMuNuB2Pi_NoPIDPiLine/Particles                                              |
| TisTosSpecs     | { 'Hlt2.\*SingleMuon.\*Decision%TOS' : 0 , 'Hlt2.\*TopoMu2Body.\*Decision%TOS' : 0 } |
