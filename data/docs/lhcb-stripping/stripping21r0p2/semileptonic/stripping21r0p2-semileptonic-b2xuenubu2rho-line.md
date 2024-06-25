[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingB2XuENuBu2Rho_Line

## Properties:

|                |                                   |
|----------------|-----------------------------------|
| OutputLocation | Phys/B2XuENuBu2Rho_Line/Particles |
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

LoKi::VoidFilter/StrippingB2XuENuBu2Rho_LineVOIDFilter

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

FilterDesktop/Pi_forB2XuENu

|                 |                                                                                                                                                 |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | (TRCHI2DOF \< 4.0 )& (P\> 3000.0 \*MeV) & (PT\> 300.0 \*MeV)& (TRGHOSTPROB \< 0.5)& (PIDK \< -2.0 )& (PIDmu \< 2 ) & (MIPCHI2DV(PRIMARY)\> 36 ) |
| Inputs          | [ 'Phys/[StdLoosePions](./stripping21r0p2-commonparticles-stdloosepions)' ]                                                                   |
| DecayDescriptor | None                                                                                                                                            |
| Output          | Phys/Pi_forB2XuENu/Particles                                                                                                                    |

CombineParticles/Rho02PiPi_forB2XuENu

|                  |                                                                                                                                                                                                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/Pi_forB2XuENu' ]                                                                                                                                                                                                                                           |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '(PT\> 400.0 \*MeV) & (TRCHI2DOF \< 4.0 )& (MIPCHI2DV(PRIMARY)\> 36.0 )& (PIDK \< -2.0 ) & (TRGHOSTPROB \< 0.5)' , 'pi-' : '(PT\> 400.0 \*MeV) & (TRCHI2DOF \< 4.0 )& (MIPCHI2DV(PRIMARY)\> 36.0 )& (PIDK \< -2.0 ) & (TRGHOSTPROB \< 0.5)' } |
| CombinationCut   | (ADAMASS('rho(770)0')\< 1500.0)                                                                                                                                                                                                                                      |
| MotherCut        | (MAXTREE('pi+'==ABSID,PT )\>900.0 \*MeV )& (MAXTREE('pi+'==ABSID,P )\>5000.0 \*MeV )& (VFASPF(VCHI2/VDOF) \< 4 ) & (PT \> 1000.0 \*MeV) & (MIPCHI2DV(PRIMARY)\> 50 ) & (BPVDIRA\> 0.98)& (DMASS('rho(770)0')\< 1500.0)                                               |
| DecayDescriptor  | None                                                                                                                                                                                                                                                                 |
| DecayDescriptors | [ 'rho(770)0 -\> pi- pi+' ]                                                                                                                                                                                                                                        |
| Output           | Phys/Rho02PiPi_forB2XuENu/Particles                                                                                                                                                                                                                                  |

CombineParticles/RhoE_forB2XuENu

|                  |                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ETightCuts_forB2XuENu' , 'Phys/Rho02PiPi_forB2XuENu' ]                                                               |
| DaughtersCuts    | { '' : 'ALL' , 'e+' : 'ALL' , 'e-' : 'ALL' , 'rho(770)0' : 'ALL' }                                                             |
| CombinationCut   | (AM\>2000.0\*MeV) & (AM\<5500.0\*MeV)                                                                                          |
| MotherCut        | (VFASPF(VCHI2/VDOF)\< 6.0) & (BPVDIRA\> 0.999) & (BPVVDCHI2 \>120.0) & (BPVCORRM \> 2500.0 \*MeV) & (BPVCORRM \< 7000.0 \*MeV) |
| DecayDescriptor  | None                                                                                                                           |
| DecayDescriptors | [ '[B+ -\> rho(770)0 e+]cc' ]                                                                                              |
| Output           | Phys/RhoE_forB2XuENu/Particles                                                                                                 |

TisTosParticleTagger/B2XuENuBu2Rho_Line

|                 |                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/RhoE_forB2XuENu' ]                                                                                                        |
| DecayDescriptor | None                                                                                                                                |
| Output          | Phys/B2XuENuBu2Rho_Line/Particles                                                                                                   |
| TisTosSpecs     | { 'Hlt2.\*Single.\*Electron.\*Decision%TOS' : 0 , 'Hlt2.\*TopoE2Body.\*Decision%TOS' : 0 , 'Hlt2.\*TopoE3Body.\*Decision%TOS' : 0 } |
