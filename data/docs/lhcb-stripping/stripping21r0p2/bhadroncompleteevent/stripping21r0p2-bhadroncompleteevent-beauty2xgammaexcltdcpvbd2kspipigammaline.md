[[stripping21r0p2 lines]](./stripping21r0p2-index)

# StrippingBeauty2XGammaExclTDCPVBd2KspipiGammaLine

## Properties:

|                |                                                         |
|----------------|---------------------------------------------------------|
| OutputLocation | Phys/Beauty2XGammaExclTDCPVBd2KspipiGammaLine/Particles |
| Postscale      | 1.0000000                                               |
| HLT1           | None                                                    |
| HLT2           | None                                                    |
| Prescale       | 1.0000000                                               |
| L0DU           | None                                                    |
| ODIN           | None                                                    |

## Filter sequence:

LoKi::VoidFilter/StrippingGoodEventConditionBhadronCompleteEvent

|      |                                                                                                                          |
|------|--------------------------------------------------------------------------------------------------------------------------|
| Code | ALG_EXECUTED('StrippingStreamBhadronCompleteEventBadEvent') & ~ALG_PASSED('StrippingStreamBhadronCompleteEventBadEvent') |

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SELECT:Phys/StdLooseAllPhotons

|      |                                      |
|------|--------------------------------------|
| Code | 0StdLooseAllPhotons/Particles',True) |

FilterDesktop/PhotonSelBeauty2XGammaExclTDCPV

|                 |                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------|
| Code            | ( PT\> 2500.0\*MeV )                                                                    |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21r0p2-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                    |
| Output          | Phys/PhotonSelBeauty2XGammaExclTDCPV/Particles                                          |

LoKi::VoidFilter/SELECT:Phys/StdAllNoPIDsPions

|      |                                     |
|------|-------------------------------------|
| Code | 0StdAllNoPIDsPions/Particles',True) |

CombineParticles/2pi_combi

|                  |                                                                                                                                                                                                                                                                                                          |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/[StdAllNoPIDsPions](./stripping21r0p2-commonparticles-stdallnopidspions)' ]                                                                                                                                                                                                                    |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : '( (MIPCHI2DV(PRIMARY) \> 9.0) & (TRCHI2DOF \< 4.0) & (TRGHOSTPROB \< 0.6) & (P \> 3000.0) & (PT \> 250.0) & (PROBNNpi \> 0.05) )' , 'pi-' : '( (MIPCHI2DV(PRIMARY) \> 9.0) & (TRCHI2DOF \< 4.0) & (TRGHOSTPROB \< 0.6) & (P \> 3000.0) & (PT \> 250.0) & (PROBNNpi \> 0.05) )' } |
| CombinationCut   | (AM \< (2000.0))                                                                                                                                                                                                                                                                                         |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 25.0)                                                                                                                                                                                                                                                               |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                                                                                                                                                                                                                                                                                    |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                                                                                                                                                                                                                                                                            |
| Output           | Phys/2pi_combi/Particles                                                                                                                                                                                                                                                                                 |

GaudiSequencer/MERGED:KsSelBeauty2XGammaExclTDCPV

GaudiSequencer/MERGEDINPUTS:KsSelBeauty2XGammaExclTDCPV

GaudiSequencer/INPUT:sel_KsDD

LoKi::VoidFilter/SELECT:Phys/StdLooseKsDD

|      |                                |
|------|--------------------------------|
| Code | 0StdLooseKsDD/Particles',True) |

FilterDesktop/sel_KsDD

|                 |                                                                             |
|-----------------|-----------------------------------------------------------------------------|
| Code            | ( (BPVLTIME() \> 2.\*ps) & (PT\> 300.0\*MeV) )                              |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21r0p2-commonparticles-stdlooseksdd)' ] |
| DecayDescriptor | None                                                                        |
| Output          | Phys/sel_KsDD/Particles                                                     |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

GaudiSequencer/INPUT:sel_KsLL

LoKi::VoidFilter/SELECT:Phys/StdVeryLooseKsLL

|      |                                    |
|------|------------------------------------|
| Code | 0StdVeryLooseKsLL/Particles',True) |

FilterDesktop/sel_KsLL

|                 |                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------|
| Code            | ( (VFASPF(VCHI2/VDOF)\<25) & (PT\> 300.0\*MeV) & ( NINTREE( ('pi+'==ABSID) & goodPion ) == 2 ) ) |
| Inputs          | [ 'Phys/[StdVeryLooseKsLL](./stripping21r0p2-commonparticles-stdverylooseksll)' ]              |
| DecayDescriptor | None                                                                                             |
| Output          | Phys/sel_KsLL/Particles                                                                          |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/KsSelBeauty2XGammaExclTDCPV

|                 |                                            |
|-----------------|--------------------------------------------|
| Code            | ALL                                        |
| Inputs          | [ 'Phys/sel_KsDD' , 'Phys/sel_KsLL' ]    |
| DecayDescriptor | None                                       |
| Output          | Phys/KsSelBeauty2XGammaExclTDCPV/Particles |

|                    |       |
|--------------------|-------|
| ModeOR             | False |
| IgnoreFilterPassed | False |

CombineParticles/KspipiSelBeauty2XGammaExclTDCPV

|                  |                                                             |
|------------------|-------------------------------------------------------------|
| Inputs           | [ 'Phys/2pi_combi' , 'Phys/KsSelBeauty2XGammaExclTDCPV' ] |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'rho(770)0' : 'ALL' }        |
| CombinationCut   | (ASUM(PT) \> 500.0) & (AM \< 1.5\*2000.0)                   |
| MotherCut        | ( (VFASPF(VCHI2/VDOF) \< 5.\*25.0) & (PT \> 500.0) )        |
| DecayDescriptor  | K\*\_2(1430)0 -\> rho(770)0 KS0                             |
| DecayDescriptors | [ 'K\*\_2(1430)0 -\> rho(770)0 KS0' ]                     |
| Output           | Phys/KspipiSelBeauty2XGammaExclTDCPV/Particles              |

CombineParticles/Bd2KspipiG_init

|                  |                                                                                                                                                                                |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/KspipiSelBeauty2XGammaExclTDCPV' , 'Phys/PhotonSelBeauty2XGammaExclTDCPV' ]                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K\*\_2(1430)0' : 'ALL' , 'K\*\_2(1430)~0' : 'ALL' , 'gamma' : 'ALL' }                                                                                          |
| CombinationCut   | ((AM \> 0.5\*4000.0) & (AM \< 2\*7000.0))                                                                                                                                      |
| MotherCut        | (VFASPF(VCHI2/VDOF) \<16.0) & (BPVIPCHI2() \< 16.0) & (PT \> 2500.0) & (M \> 0.5\*4000.0) & (M \< 2.\*7000.0) & (SUMTREE(PT, ISBASIC, 0.0) \> 3000.0) & (acos(BPVDIRA) \< 0.2) |
| DecayDescriptor  | B0 -\> K\*\_2(1430)0 gamma                                                                                                                                                     |
| DecayDescriptors | [ 'B0 -\> K\*\_2(1430)0 gamma' ]                                                                                                                                             |
| Output           | Phys/Bd2KspipiG_init/Particles                                                                                                                                                 |

FilterDesktop/Beauty2XGammaExclTDCPVBd2KspipiGamma

|                 |                                                                       |
|-----------------|-----------------------------------------------------------------------|
| Code            | ((dtf_prob \> 1e-10) & (in_range(4000.0,mB,7000.0)) & (mX \< 2000.0)) |
| Inputs          | [ 'Phys/Bd2KspipiG_init' ]                                          |
| DecayDescriptor | None                                                                  |
| Output          | Phys/Beauty2XGammaExclTDCPVBd2KspipiGamma/Particles                   |

TisTosParticleTagger/Beauty2XGammaExclTDCPVBd2KspipiGammaHlt1TISTOS

|                 |                                                                          |
|-----------------|--------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammaExclTDCPVBd2KspipiGamma' ]                        |
| DecayDescriptor | None                                                                     |
| Output          | Phys/Beauty2XGammaExclTDCPVBd2KspipiGammaHlt1TISTOS/Particles            |
| TisTosSpecs     | { 'Hlt1TrackAllL0Decision%TOS' : 0 , 'Hlt1TrackPhotonDecision%TOS' : 0 } |

TisTosParticleTagger/Beauty2XGammaExclTDCPVBd2KspipiGammaLine

|                 |                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/Beauty2XGammaExclTDCPVBd2KspipiGammaHlt1TISTOS' ]                                                           |
| DecayDescriptor | None                                                                                                                  |
| Output          | Phys/Beauty2XGammaExclTDCPVBd2KspipiGammaLine/Particles                                                               |
| TisTosSpecs     | { 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2Radiative.\*Decision%TOS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 } |
