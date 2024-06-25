[[stripping21r1 lines]](./stripping21r1-index)

# StrippingB2XGamma2pi_wCNV_Line

## Properties:

|                |                                      |
|----------------|--------------------------------------|
| OutputLocation | Phys/B2XGamma2pi_wCNV_Line/Particles |
| Postscale      | 1.0000000                            |
| HLT            | None                                 |
| Prescale       | 1.0000000                            |
| L0DU           | None                                 |
| ODIN           | None                                 |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/TrackListB2XGamma

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (HASTRACK) & (TRCHI2DOF \< 3.0)& (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.4) & (PT \> 300.0) & (P \> 1000) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21r1-commonparticles-stdallnopidspions)' ]                                |
| DecayDescriptor | None                                                                                                               |
| Output          | Phys/TrackListB2XGamma/Particles                                                                                   |

CombineParticles/DiTracksForRadiativeBB2XGamma

|                  |                                                    |
|------------------|----------------------------------------------------|
| Inputs           | [ 'Phys/TrackListB2XGamma' ]                     |
| DaughtersCuts    | { '' : 'ALL' , 'pi+' : 'ALL' , 'pi-' : 'ALL' }     |
| CombinationCut   | (ASUM(PT) \> 1500.0) & in_range( 0.0 , AM ,7900.0) |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 10.0)         |
| DecayDescriptor  | rho(770)0 -\> pi+ pi-                              |
| DecayDescriptors | [ 'rho(770)0 -\> pi+ pi-' ]                      |
| Output           | Phys/DiTracksForRadiativeBB2XGamma/Particles       |

GaudiSequencer/SeqMergedConvertedPhotons

LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaDD_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseGammaDD](./stripping21r1-commonparticles-stdallloosegammadd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdAllLooseGammaLL_Particles

|      |                                                                                                        |
|------|--------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllLooseGammaLL](./stripping21r1-commonparticles-stdallloosegammall)/Particles')\>0 |

FilterDesktop/MergedConvertedPhotons

|                 |                                                                                                                                                                         |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                                                     |
| Inputs          | [ 'Phys/[StdAllLooseGammaDD](./stripping21r1-commonparticles-stdallloosegammadd)' , 'Phys/[StdAllLooseGammaLL](./stripping21r1-commonparticles-stdallloosegammall)' ] |
| DecayDescriptor | None                                                                                                                                                                    |
| Output          | Phys/MergedConvertedPhotons/Particles                                                                                                                                   |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/ConvPhotonB2XGamma

|                 |                                                                           |
|-----------------|---------------------------------------------------------------------------|
| Code            | (MM \< 100\*MeV) & (HASVERTEX) & (VFASPF(VCHI2/VDOF)\<9) & (PT \> 1000.0) |
| Inputs          | [ 'Phys/MergedConvertedPhotons' ]                                       |
| DecayDescriptor | None                                                                      |
| Output          | Phys/ConvPhotonB2XGamma/Particles                                         |

CombineParticles/B2XGamma2pi_wCNV\_

|                  |                                                                                       |
|------------------|---------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/ConvPhotonB2XGamma' , 'Phys/DiTracksForRadiativeBB2XGamma' ]                |
| DaughtersCuts    | { '' : 'ALL' , 'gamma' : 'ALL' , 'rho(770)0' : 'ALL' }                                |
| CombinationCut   | in_range( 3280.0 ,AM, 9000.0 )& (ASUM(PT) \> 5000 )                                   |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 9.0 ) & (BPVIPCHI2() \< 9.0 ) & (BPVDIRA \> 0.0) |
| DecayDescriptor  | B0 -\> rho(770)0 gamma                                                                |
| DecayDescriptors | [ 'B0 -\> rho(770)0 gamma' ]                                                        |
| Output           | Phys/B2XGamma2pi_wCNV\_/Particles                                                     |

TisTosParticleTagger/B2XGamma2pi_wCNV_Line

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2XGamma2pi_wCNV\_' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/B2XGamma2pi_wCNV_Line/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| TisTosSpecs     | { 'Hlt2Bd2KstGamma.\*Decision%TIS' : 0 , 'Hlt2Bd2KstGamma.\*Decision%TOS' : 0 , 'Hlt2Bs2PhiGamma.\*Decision%TIS' : 0 , 'Hlt2Bs2PhiGamma.\*Decision%TOS' : 0 , 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2RadiativeTopo.\*Decision%TIS' : 0 , 'Hlt2RadiativeTopo.\*Decision%TOS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 , 'Hlt2TopoRad.\*Decision%TIS' : 0 , 'Hlt2TopoRad.\*Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_B2XGamma2pi_wCNV_Line

|                 |                                                   |
|-----------------|---------------------------------------------------|
| Inputs          | [ 'Phys/B2XGamma2pi_wCNV_Line' ]                |
| DecayDescriptor | None                                              |
| Output          | Phys/RelatedInfo1_B2XGamma2pi_wCNV_Line/Particles |
