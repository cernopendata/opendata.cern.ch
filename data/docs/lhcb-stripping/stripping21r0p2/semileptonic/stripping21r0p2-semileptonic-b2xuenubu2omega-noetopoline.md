[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2XuENuBu2Omega_NoETopoLine

## Properties:

|                |                                            |
|----------------|--------------------------------------------|
| OutputLocation | Phys/B2XuENuBu2Omega_NoETopoLine/Particles |
| Postscale      | 1.0000000                                  |
| HLT1           | None                                       |
| HLT2           | None                                       |
| Prescale       | 0.20000000                                 |
| L0DU           | None                                       |
| ODIN           | None                                       |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionSemileptonic

|      |                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamSemileptonicBadEvent') & ~ALG_PASSED('StrippingStreamSemileptonicBadEvent') |

LoKi::VoidFilter/StrippingB2XuENuBu2Omega_NoETopoLineVOIDFilter

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

FilterDesktop/ETightCuts_forB2XuENu

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 ) & (P\> 6000.0 \*MeV) & (PT\> 1500.0\* MeV)& (TRGHOSTPROB \< 0.35)& (PIDe \> 3.0 )& (MIPCHI2DV(PRIMARY)\> 25 ) |
| Inputs          | [ 'Phys/[StdLooseElectrons](./stripping21r0p2-commonparticles-stdlooseelectrons)' ]                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/ETightCuts_forB2XuENu/Particles                                                                                              |

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

DaVinci::N3BodyDecays/Omega2PiPiPi0_forB2XuENu

|                  |                                                                                                                                                                                                                                                       |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdLooseMergedPi0](./stripping21r0p2-commonparticles-stdloosemergedpi0)' , 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' , 'Phys/[StdLooseResolvedPi0](./stripping21r0p2-commonparticles-stdlooseresolvedpi0)' ] |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT\> 300 \*MeV)& (MIPCHI2DV(PRIMARY)\> 25 )& (PIDK \< 0 ) & (TRGHOSTPROB \< 0.5)' , 'pi-' : '(PT\> 300 \*MeV)& (MIPCHI2DV(PRIMARY)\> 25 )& (PIDK \< 0 ) & (TRGHOSTPROB \< 0.5)' , 'pi0' : '(PT \> 500 \*MeV)' }              |
| CombinationCut   | (ADAMASS('omega(782)')\< 150)                                                                                                                                                                                                                         |
| MotherCut        | (VFASPF(VCHI2/VDOF) \< 6) & (DMASS('omega(782)')\< 150)                                                                                                                                                                                               |
| DecayDescriptor  | omega(782) -\> pi+ pi- pi0                                                                                                                                                                                                                            |
| DecayDescriptors | [ 'omega(782) -\> pi+ pi- pi0' ]                                                                                                                                                                                                                    |
| Output           | Phys/Omega2PiPiPi0_forB2XuENu/Particles                                                                                                                                                                                                               |

CombineParticles/OmegaENoETopo_forB2XuENu

|                  |                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ETightCuts_forB2XuENu' , 'Phys/Omega2PiPiPi0_forB2XuENu' ]                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'omega(782)' : 'ALL' }                                                            |
| CombinationCut   | (AM\>2000.0\*MeV) & (AM\<5500.0\*MeV)                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (BPVVDCHI2 \>120.0) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                                           |
| DecayDescriptors | [ '[B+ -\> omega(782) e+]cc' ]                                                                                             |
| Output           | Phys/OmegaENoETopo_forB2XuENu/Particles                                                                                        |

TisTosParticleTagger/B2XuENuBu2Omega_NoETopoLine

|                 |                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/OmegaENoETopo_forB2XuENu' ]                                                                                             |
| DecayDescriptor | None                                                                                                                              |
| Output          | Phys/B2XuENuBu2Omega_NoETopoLine/Particles                                                                                        |
| TisTosSpecs     | { 'Hlt2.\*Single.\*Electron.\*Decision%TOS' : 0 , 'Hlt2.\*Topo2Body.\*Decision%TOS' : 0 , 'Hlt2.\*Topo3Body.\*Decision%TOS' : 0 } |
