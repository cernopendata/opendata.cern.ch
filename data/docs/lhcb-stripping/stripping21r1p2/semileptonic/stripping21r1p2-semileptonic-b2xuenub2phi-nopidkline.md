[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2XuENuB2Phi_NoPIDKLine

## Properties:

|                |                                        |
|----------------|----------------------------------------|
| OutputLocation | Phys/B2XuENuB2Phi_NoPIDKLine/Particles |
| Postscale      | 1.0000000                              |
| HLT1           | None                                   |
| HLT2           | None                                   |
| Prescale       | 0.010000000                            |
| L0DU           | None                                   |
| ODIN           | None                                   |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuENuB2Phi_NoPIDKLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsElectrons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdNoPIDsElectrons/Particles',True) |

FilterDesktop/ETightNoPIDCuts_forB2XuENu

|                 |                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 6000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdNoPIDsElectrons](./stripping21r1p2-commonparticles-stdnopidselectrons)' ]                           |
| DecayDescriptor | None                                                                                                              |
| Output          | Phys/ETightNoPIDCuts_forB2XuENu/Particles                                                                         |

LoKi::VoidFilter/SELECT:Phys/StdNoPIDsKaons

|      |                                  |
|------|----------------------------------|
| Code | 0StdNoPIDsKaons/Particles',True) |

FilterDesktop/KNoPID_PhiB2XuENu

|                 |                                                                                                                |
|-----------------|----------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 )& (P\> 3000.0 \*MeV) & (PT\> 400.0 \*MeV)& (TRGHOSTPROB \< 0.5)& (MIPCHI2DV(PRIMARY)\> 36 ) |
| Inputs          | [ 'Phys/[StdNoPIDsKaons](./stripping21r1p2-commonparticles-stdnopidskaons)' ]                                |
| DecayDescriptor | None                                                                                                           |
| Output          | Phys/KNoPID_PhiB2XuENu/Particles                                                                               |

CombineParticles/PhiKKNoPID_forB2XuENu

|                  |                                                                                                |
|------------------|------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KNoPID_PhiB2XuENu' ]                                                                 |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                   |
| CombinationCut   | (AM\< 2200.0)                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6 ) & (PT \> 600.0 \*MeV) & (MIPCHI2DV(PRIMARY)\> 9 ) & (BPVDIRA\> 0.9) |
| DecayDescriptor  | None                                                                                           |
| DecayDescriptors | [ 'phi(1020) -\> K- K+' ]                                                                    |
| Output           | Phys/PhiKKNoPID_forB2XuENu/Particles                                                           |

CombineParticles/PhiE_NoPIDHad_forB2XuENu

|                  |                                                                                              |
|------------------|----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ETightNoPIDCuts_forB2XuENu' , 'Phys/PhiKKNoPID_forB2XuENu' ]                       |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'phi(1020)' : 'ALL' }                           |
| CombinationCut   | (AM\<5500.0\*MeV)                                                                            |
| MotherCut        | (BPVCORRM\>2500.0\*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.994)& (BPVVDCHI2 \>50.0) |
| DecayDescriptor  | None                                                                                         |
| DecayDescriptors | [ '[B+ -\> phi(1020) e+]cc' ]                                                            |
| Output           | Phys/PhiE_NoPIDHad_forB2XuENu/Particles                                                      |

TisTosParticleTagger/B2XuENuB2Phi_NoPIDKLine

|                 |                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/PhiE_NoPIDHad_forB2XuENu' ]                                                                                               |
| DecayDescriptor | None                                                                                                                                |
| Output          | Phys/B2XuENuB2Phi_NoPIDKLine/Particles                                                                                              |
| TisTosSpecs     | { 'Hlt2.\*Single.\*Electron.\*Decision%TOS' : 0 , 'Hlt2.\*TopoE2Body.\*Decision%TOS' : 0 , 'Hlt2.\*TopoE3Body.\*Decision%TOS' : 0 } |
