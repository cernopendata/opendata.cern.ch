[[stripping21 lines]](./stripping21-index)

# StrippingB2XGamma2pi_Ks0_Line

## Properties:

|                |                                     |
|----------------|-------------------------------------|
| OutputLocation | Phys/B2XGamma2pi_Ks0_Line/Particles |
| Postscale      | 1.0000000                           |
| HLT            | None                                |
| Prescale       | 1.0000000                           |
| L0DU           | None                                |
| ODIN           | None                                |

## Filter sequence:

CheckPV/checkPVmin1

|        |     |
|--------|-----|
| MinPVs | 1   |
| MaxPVs | -1  |

GaudiSequencer/SeqMergedKshorts

LoKi::VoidFilter/SelFilterPhys_StdLooseKsDD_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)/Particles')\>0 |

LoKi::VoidFilter/SelFilterPhys_StdLooseKsLL_Particles

|      |                                                                                          |
|------|------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)/Particles')\>0 |

FilterDesktop/MergedKshorts

|                 |                                                                                                                                             |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Code            | ALL                                                                                                                                         |
| Inputs          | [ 'Phys/[StdLooseKsDD](./stripping21-commonparticles-stdlooseksdd)' , 'Phys/[StdLooseKsLL](./stripping21-commonparticles-stdlooseksll)' ] |
| DecayDescriptor | None                                                                                                                                        |
| Output          | Phys/MergedKshorts/Particles                                                                                                                |

|                    |       |
|--------------------|-------|
| ModeOR             | True  |
| IgnoreFilterPassed | False |

FilterDesktop/KS0SelB2XGamma

|                 |                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------|
| Code            | (PT \> 1000) & (MM \> 480\*MeV) & (MM \< 515\*MeV) & (HASVERTEX) & (VFASPF(VCHI2/VDOF)\<9) |
| Inputs          | [ 'Phys/MergedKshorts' ]                                                                 |
| DecayDescriptor | None                                                                                       |
| Output          | Phys/KS0SelB2XGamma/Particles                                                              |

LoKi::VoidFilter/SelFilterPhys_StdAllNoPIDsPions_Particles

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)/Particles')\>0 |

FilterDesktop/TrackListB2XGamma

|                 |                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| Code            | (HASTRACK) & (TRCHI2DOF \< 3.0)& (MIPCHI2DV(PRIMARY) \> 16.0) & (TRGHOSTPROB \< 0.4) & (PT \> 300.0) & (P \> 1000) |
| Inputs          | [ 'Phys/[StdAllNoPIDsPions](./stripping21-commonparticles-stdallnopidspions)' ]                                  |
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

CombineParticles/DiTracks_wKS0ForRadiativeBB2XGamma

|                  |                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DiTracksForRadiativeBB2XGamma' , 'Phys/KS0SelB2XGamma' ]                                            |
| DaughtersCuts    | { '' : 'ALL' , 'KS0' : 'ALL' , 'rho(770)0' : 'ALL' }                                                          |
| CombinationCut   | (ASUM(PT) \> 1500.0) & in_range( 0.0 , AM ,7900.0)                                                            |
| MotherCut        | (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 10.0) & (PT \> 150.0) & (BPVVDCHI2 \> 0.0) & (MIPCHI2DV(PRIMARY) \> 0.0) |
| DecayDescriptor  | K\*\_2(1430)0 -\> rho(770)0 KS0                                                                               |
| DecayDescriptors | [ 'K\*\_2(1430)0 -\> rho(770)0 KS0' ]                                                                       |
| Output           | Phys/DiTracks_wKS0ForRadiativeBB2XGamma/Particles                                                             |

LoKi::VoidFilter/SelFilterPhys_StdLooseAllPhotons_Particles

|      |                                                                                                      |
|------|------------------------------------------------------------------------------------------------------|
| Code | CONTAINS('Phys/[StdLooseAllPhotons](./stripping21-commonparticles-stdlooseallphotons)/Particles')\>0 |

FilterDesktop/PhotonSelB2XGamma

|                 |                                                                                     |
|-----------------|-------------------------------------------------------------------------------------|
| Code            | (PT \> 2000.0) & (CL \> 0.0)                                                        |
| Inputs          | [ 'Phys/[StdLooseAllPhotons](./stripping21-commonparticles-stdlooseallphotons)' ] |
| DecayDescriptor | None                                                                                |
| Output          | Phys/PhotonSelB2XGamma/Particles                                                    |

CombineParticles/B2XGamma2pi_Ks0\_

|                  |                                                                                                                                                                                                                                     |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs           | [ 'Phys/DiTracks_wKS0ForRadiativeBB2XGamma' , 'Phys/PhotonSelB2XGamma' ]                                                                                                                                                          |
| DaughtersCuts    | { '' : 'ALL' , 'K\*\_2(1430)0' : 'ALL' , 'K\*\_2(1430)~0' : 'ALL' , 'gamma' : 'ALL' }                                                                                                                                               |
| CombinationCut   | in_range( 2900.0 ,AM, 9000.0 ) & (ASUM(PT) \> 5000 )                                                                                                                                                                                |
| MotherCut        | INTREE(ISBASIC & ((HASTRACK) & (P\>5000\*MeV) & (PT\>1000\*MeV) & (TRCHI2DOF\<2.5) & (MIPCHI2DV(PRIMARY)\>16) & (MIPDV(PRIMARY)\>0.1\*mm))) & (HASVERTEX) & (VFASPF(VCHI2/VDOF) \< 9.0 ) & (BPVIPCHI2() \< 9.0 ) & (BPVDIRA \> 0.0) |
| DecayDescriptor  | B0 -\> K\*\_2(1430)0 gamma                                                                                                                                                                                                          |
| DecayDescriptors | [ 'B0 -\> K\*\_2(1430)0 gamma' ]                                                                                                                                                                                                  |
| Output           | Phys/B2XGamma2pi_Ks0\_/Particles                                                                                                                                                                                                    |

TisTosParticleTagger/B2XGamma2pi_Ks0_Line

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inputs          | [ 'Phys/B2XGamma2pi_Ks0\_' ]                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DecayDescriptor | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Output          | Phys/B2XGamma2pi_Ks0_Line/Particles                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| TisTosSpecs     | { 'Hlt2Bd2KstGamma.\*Decision%TIS' : 0 , 'Hlt2Bd2KstGamma.\*Decision%TOS' : 0 , 'Hlt2Bs2PhiGamma.\*Decision%TIS' : 0 , 'Hlt2Bs2PhiGamma.\*Decision%TOS' : 0 , 'Hlt2IncPhi.\*Decision%TIS' : 0 , 'Hlt2IncPhi.\*Decision%TOS' : 0 , 'Hlt2RadiativeTopo.\*Decision%TIS' : 0 , 'Hlt2RadiativeTopo.\*Decision%TOS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TIS' : 0 , 'Hlt2Topo(2\|3\|4)Body.\*Decision%TOS' : 0 , 'Hlt2TopoRad.\*Decision%TIS' : 0 , 'Hlt2TopoRad.\*Decision%TOS' : 0 } |

AddRelatedInfo/RelatedInfo1_B2XGamma2pi_Ks0_Line

|                 |                                                  |
|-----------------|--------------------------------------------------|
| Inputs          | [ 'Phys/B2XGamma2pi_Ks0_Line' ]                |
| DecayDescriptor | None                                             |
| Output          | Phys/RelatedInfo1_B2XGamma2pi_Ks0_Line/Particles |
