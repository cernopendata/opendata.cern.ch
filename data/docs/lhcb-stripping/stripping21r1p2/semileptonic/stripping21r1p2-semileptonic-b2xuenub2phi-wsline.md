[[stripping21r1p2 lines]](./stripping21r1p2-index)

# StrippingB2XuENuB2Phi_WSLine

## Properties:

|                |                                    |
|----------------|------------------------------------|
| OutputLocation | Phys/B2XuENuB2Phi_WSLine/Particles |
| Postscale      | 1.0000000                          |
| HLT1           | None                               |
| HLT2           | None                               |
| Prescale       | 0.20000000                         |
| L0DU           | None                               |
| ODIN           | None                               |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuENuB2Phi_WSLineVOIDFilter

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Code | ( recSummaryTrack(LHCb.RecSummary.nLongTracks, TrLONG) \< 250.0 ) |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseElectrons

|      |                                     |
|------|-------------------------------------|
| Code | 0StdLooseElectrons/Particles',True) |

FilterDesktop/EL0TOS_forB2XuENu

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 6000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (PIDe \> 3.0 )& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdLooseElectrons](./stripping21r1p2-commonparticles-stdlooseelectrons)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/EL0TOS_forB2XuENu/Particles                                                                                                  |

LoKi::VoidFilter/SELECT:Phys/StdLooseKaons

|      |                                 |
|------|---------------------------------|
| Code | 0StdLooseKaons/Particles',True) |

FilterDesktop/K_PhiB2XuENu

|                 |                                                                                                                                |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 )& (P\> 3000.0 \*MeV) & (PT\> 400.0 \*MeV)& (TRGHOSTPROB \< 0.5)& (PIDK\> 2.0 ) & (MIPCHI2DV(PRIMARY)\> 36 ) |
| Inputs          | [ 'Phys/[StdLooseKaons](./stripping21r1p2-commonparticles-stdloosekaons)' ]                                                  |
| DecayDescriptor | None                                                                                                                           |
| Output          | Phys/K_PhiB2XuENu/Particles                                                                                                    |

CombineParticles/PhiKKWS_forB2XuENu

|                  |                                                                                                |
|------------------|------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/K_PhiB2XuENu' ]                                                                      |
| DaughtersCuts    | { '' : 'ALL' , 'K+' : 'ALL' , 'K-' : 'ALL' }                                                   |
| CombinationCut   | (AM\< 2200.0)                                                                                  |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6 ) & (PT \> 600.0 \*MeV) & (MIPCHI2DV(PRIMARY)\> 9 ) & (BPVDIRA\> 0.9) |
| DecayDescriptor  | None                                                                                           |
| DecayDescriptors | [ '[phi(1020) -\> K+ K+]cc' ]                                                              |
| Output           | Phys/PhiKKWS_forB2XuENu/Particles                                                              |

CombineParticles/PhiEWS_forB2XuENu

|                  |                                                                                              |
|------------------|----------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/EL0TOS_forB2XuENu' , 'Phys/PhiKKWS_forB2XuENu' ]                                   |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'phi(1020)' : 'ALL' }                           |
| CombinationCut   | (AM\<5500.0\*MeV)                                                                            |
| MotherCut        | (BPVCORRM\>2500.0\*MeV) & (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.994)& (BPVVDCHI2 \>50.0) |
| DecayDescriptor  | None                                                                                         |
| DecayDescriptors | [ '[B+ -\> phi(1020) e+]cc' ]                                                            |
| Output           | Phys/PhiEWS_forB2XuENu/Particles                                                             |

TisTosParticleTagger/B2XuENuB2Phi_WSLine

|                 |                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/PhiEWS_forB2XuENu' ]                                                                                                      |
| DecayDescriptor | None                                                                                                                                |
| Output          | Phys/B2XuENuB2Phi_WSLine/Particles                                                                                                  |
| TisTosSpecs     | { 'Hlt2.\*Single.\*Electron.\*Decision%TOS' : 0 , 'Hlt2.\*TopoE2Body.\*Decision%TOS' : 0 , 'Hlt2.\*TopoE3Body.\*Decision%TOS' : 0 } |
